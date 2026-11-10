"""
MATH-GOV v0.6 10-Task Simulation & Calibrated Reporting Tests
============================================================
Tests the multi-pathway research simulation defined in:
governance/math_gov/examples/ten_tasks.json
governance/math_gov/examples/five_of_ten.json

Verifies:
- Exactly 5 of 10 tasks executed/submitted across 3 isolated branches (B1, B2, B3)
- 2 steps with recorded open obligations (S2, S5)
- Zero verified formal proofs (formal_proofs_verified: 0)
- Truthful calibrated reporting: theorem progress percent is strictly UNKNOWN
- Never reporting "50% theorem proved" based on 5/10 tasks executed
- Downstream task dispatch gating (T06 blocked until T02 and T05 pass review)
- Tri-Agent role separation across dispatch, submission, review, and acceptance
"""

import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.ymmg import governance_preview as gp
from src.ymmg import math_gov_supervisor as mgs
from src.ymmg import math_step_engine as e

EXAMPLES_DIR = ROOT / "governance" / "math_gov" / "examples"
TEN_TASKS_PATH = EXAMPLES_DIR / "ten_tasks.json"
FIVE_OF_TEN_PATH = EXAMPLES_DIR / "five_of_ten.json"


class MathGovTenTasksSimulationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ten_tasks = gp.read_json(TEN_TASKS_PATH)
        cls.five_of_ten = json.loads(FIVE_OF_TEN_PATH.read_text(encoding="utf-8"))

    def test_ten_tasks_structural_validation(self):
        errors, *_ = gp.validate_plan(self.ten_tasks)
        self.assertEqual(errors, [], f"Expected zero validation errors, got: {errors}")

    def test_five_of_ten_executed_metrics(self):
        rep = gp.report(self.ten_tasks)
        # Exactly 5 tasks executed or submitted
        self.assertEqual(rep["tasks_executed_or_submitted"], 5)
        # 2 submitted pending review
        self.assertEqual(rep["tasks_submitted_pending_review"], 2)
        # 2 steps with open obligations
        self.assertEqual(rep["steps_with_recorded_open_obligations"], 2)
        # 0 formal proofs verified
        self.assertEqual(rep["formal_proofs_verified"], 0)
        # Strict UNKNOWN progress
        self.assertEqual(rep["theorem_progress"], "UNKNOWN")

    def test_calibrated_reporting_forbids_theorem_percentage(self):
        """Rule H14: Never say '50% of theorem proved' based on 5 of 10 tasks."""
        rep = gp.report(self.ten_tasks)
        self.assertEqual(rep["theorem_progress"], "UNKNOWN")
        self.assertNotIn("50%", str(rep))

        prog = e.progress(self.five_of_ten)
        self.assertEqual(prog["tasks_total"], 10)
        self.assertEqual(prog["tasks_execution_finished"], 5)
        self.assertEqual(prog["theorem_progress_percent"], "UNKNOWN")
        self.assertFalse(prog["proof_verified"])

    def test_downstream_task_t06_blocked_on_unverified_prerequisites(self):
        """Task T06 requires T02 and T05. Since T02 is SUBMITTED but not accepted, T06 cannot dispatch."""
        plan_res = gp.plan(self.ten_tasks)
        t06 = next(x for x in plan_res["tasks"] if x["task_id"] == "T06")
        self.assertEqual(t06["dispatch_preview"], "DEPENDENCIES_NOT_AUTHENTICATED")

    def test_capsule_generation_for_t06_detects_incomplete_context(self):
        cap = gp.capsule(self.ten_tasks, "T06")
        self.assertEqual(cap["verdict"], "INCOMPLETE_CONTEXT_CAPSULE_NOT_DISPATCHABLE")
        self.assertTrue(cap["no_unauthorized_cross_branch_data"])

    def test_branch_isolation_across_b1_b2_b3(self):
        branches = {b["id"]: b["visibility"] for b in self.ten_tasks["branches"]}
        self.assertEqual(branches, {"B1": "ISOLATED", "B2": "ISOLATED", "B3": "ISOLATED"})

    def test_tri_agent_workflow_simulation(self):
        """Simulate dispatch -> submit -> review -> acceptance cycle for task T01."""
        supervisor = mgs.MathGovSupervisor(
            workspace_root=ROOT,
            supervisor_id="supervisor-main",
            owner_id="owner-researcher",
        )
        # 1. Register distinct actors
        w1 = supervisor.register_actor("worker-01", "WORKER", branch_scope="B1")
        r1 = supervisor.register_actor("reviewer-01", "REVIEWER", branch_scope="B1")
        a1 = supervisor.register_actor("acceptor-01", "ACCEPTOR", branch_scope="ALL")

        # 2. Worker submits proposed step S1
        submission = supervisor.submit_task_work(
            task_id="T01",
            worker_id="worker-01",
            step_proposals=[{"id": "S1", "goal": "Inventory definitions"}],
            case_data=self.five_of_ten,
        )
        self.assertEqual(submission["status"], "SUBMITTED")
        self.assertFalse(submission["accepted"])

        # 3. Independent reviewer conducts review
        review_receipt = supervisor.conduct_review(
            task_id="T01",
            submission=submission,
            reviewer_id="reviewer-01",
            decision="REVIEW_PASS",
            findings=["Definitions are complete and match literature."],
        )
        self.assertEqual(review_receipt["decision"], "REVIEW_PASS")
        self.assertFalse(review_receipt["accepted"])

        # 4. Distinct technical acceptor grants acceptance
        acceptance_cert = supervisor.grant_technical_acceptance(
            task_id="T01",
            review_receipt=review_receipt,
            acceptor_id="acceptor-01",
        )
        self.assertEqual(acceptance_cert["status"], "ACCEPTED_TASK")

        # 5. Generate calibrated supervisor report
        cal_report = supervisor.generate_calibrated_report(
            case_data=self.five_of_ten,
            executed_tasks=["T01"],
            accepted_tasks=["T01"],
            negative_findings=["NEG-YM-099: 2-loop infinite horizon obstruction"],
        )
        self.assertEqual(cal_report.theorem_progress_percent, "UNKNOWN")
        self.assertEqual(cal_report.tasks["accepted"], 1)
        self.assertEqual(cal_report.tasks["executed"], 1)


if __name__ == "__main__":
    unittest.main()
