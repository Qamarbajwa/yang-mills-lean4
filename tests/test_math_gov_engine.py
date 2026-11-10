"""
MATH-GOV v0.6 Core Mathematical Step Engine Tests
=================================================
Tests:
- Graph indexing, DAG cycle detection, and edge contracts
- AND/OR task dependency resolution and task readiness
- Step obligation declaration, discharge, and validation
- Transitive invalidation on root/premise mutation
- Exact binary event ledger roundtrip, SHA-256 hash chaining, and tamper detection
- Calibrated progress reporting (no theorem completion percentages)
"""

import copy
import json
from pathlib import Path
import sqlite3
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.ymmg import math_step_engine as e
from src.ymmg import event_ledger as ev

EXAMPLE_DIR = ROOT / "governance" / "math_gov" / "examples"
DEMO_PATH = EXAMPLE_DIR / "demo_case.json"
CASE = json.loads(DEMO_PATH.read_text(encoding="utf-8"))
ORIGINAL = CASE["original"]["digest"]
FORMAL = CASE["formal_target"]["digest"]
CONTRACT = e.digest(e.canonical({"required_inventory": CASE["required_inventory"], "required_edges": CASE["required_edges"]}))
BASELINE = e.digest(e.canonical(CASE))


def mutate_node(case, node_id):
    return next(x for x in case["nodes"] if x["id"] == node_id)


class MathGovEngineStructuralTests(unittest.TestCase):
    def base(self):
        return copy.deepcopy(CASE)

    def audit(self, c, o=ORIGINAL, f=FORMAL):
        return e.audit(c, o, f, CONTRACT)

    def blocks(self, c, match):
        result = self.audit(c)
        self.assertEqual(result["verdict"], "BLOCKED", f"Expected BLOCKED, got {result}")
        self.assertIn(match, " ".join(result["errors"]))

    def test_baseline_structure(self):
        res = self.audit(self.base())
        self.assertEqual(res["verdict"], "STRUCTURAL_PREFLIGHT_PASS_ONLY")
        self.assertFalse(res["release_authorized"])

    def test_missing_external_original_anchor(self):
        self.assertIn("original-question digest", " ".join(e.audit(self.base())["errors"]))

    def test_missing_formal_anchor(self):
        self.assertIn("formal target digest", " ".join(e.audit(self.base(), ORIGINAL)["errors"]))

    def test_original_changed_and_self_rehashed(self):
        c = self.base()
        c["original"]["text"] = "The Millennium problem is trivially solved."
        c["original"]["digest"] = e.digest(c["original"]["text"])
        self.blocks(c, "owner-anchored")

    def test_formal_goal_weakening_self_rehashed(self):
        c = self.base()
        c["formal_target"]["statement"] = "True"
        c["formal_target"]["digest"] = e.digest("True")
        self.blocks(c, "approved digest")

    def test_missing_mathematical_step(self):
        c = self.base()
        c["nodes"] = [x for x in c["nodes"] if x["id"] != "S1"]
        self.blocks(c, "INVENTORY: missing S1")

    def test_missing_edge(self):
        c = self.base()
        c["edges"] = [x for x in c["edges"] if not (x["source"] == "S1" and x["target"] == "S2")]
        self.blocks(c, "required edge missing")

    def test_missing_all_required_edge_registry(self):
        c = self.base()
        del c["required_edges"]
        self.blocks(c, "missing independent required edge inventory")

    def test_undeclared_premise(self):
        c = self.base()
        mutate_node(c, "S2")["premises"].append("SRC-ORIGINAL")
        self.blocks(c, "absent from dependency graph")

    def test_fake_formal_checked_status_rejected(self):
        c = self.base()
        mutate_node(c, "S1")["state"] = "FORMALLY_CHECKED"
        self.blocks(c, "self-asserted formal verification")

    def test_unclosed_formal_candidate(self):
        c = self.base()
        mutate_node(c, "S1")["state"] = "FORMAL_CANDIDATE"
        self.blocks(c, "open obligations")

    def test_discharge_unknown_obligation(self):
        c = self.base()
        mutate_node(c, "S1")["discharged"] = ["ghost_subgoal"]
        self.blocks(c, "not in declared obligations")

    def test_duplicate_obligation_rejected(self):
        c = self.base()
        mutate_node(c, "S1")["obligations"] = ["lemma_1", "lemma_1"]
        self.blocks(c, "duplicate proof obligations")

    def test_task_self_acceptance_rejected(self):
        c = self.base()
        mutate_node(c, "T1")["state"] = "TASK_ACCEPTED"
        self.blocks(c, "untrusted task acceptance")

    def test_strong_claim_self_report_rejected(self):
        c = self.base()
        mutate_node(c, "C1")["reported_strength"] = "THEOREM_PROVED"
        self.blocks(c, "cannot be self-declared")

    def test_claim_evidence_link_removed(self):
        c = self.base()
        c["edges"] = [x for x in c["edges"] if x["target"] != "C1"]
        self.blocks(c, "required edge missing")

    def test_graph_self_cycle(self):
        c = self.base()
        c["edges"].append({"source": "T1", "target": "T1", "kind": "AND"})
        self.blocks(c, "self-edge")

    def test_graph_two_node_cycle(self):
        c = self.base()
        c["edges"].append({"source": "T2", "target": "T1", "kind": "AND"})
        self.blocks(c, "cycle")

    def test_reject_unauthorized_cross_branch(self):
        c = self.base()
        c["edges"].append({"source": "T2", "target": "T3", "kind": "AND"})
        self.blocks(c, "unauthorized cross-branch")

    def test_unregistered_node(self):
        c = self.base()
        c["nodes"].append({"id": "GHOST", "kind": "CLAIM", "reported_strength": "DRAFT_CLAIM", "evidence_refs": ["S1"]})
        self.blocks(c, "unregistered node")

    def test_missing_step_owner(self):
        c = self.base()
        mutate_node(c, "S2")["task_id"] = "GHOST_TASK"
        self.blocks(c, "missing owning TASK")

    def test_wrong_lean_digest(self):
        c = self.base()
        mutate_node(c, "S1")["lean"]["statement_digest"] = "0" * 64
        self.blocks(c, "Lean formal statement digest mismatch")

    def test_malformed_root(self):
        self.assertEqual(e.audit(None)["verdict"], "BLOCKED")

    def test_malformed_premises_is_blocked(self):
        c = self.base()
        mutate_node(c, "S1")["premises"] = 42
        self.blocks(c, "premises not array")

    def test_malformed_obligations_is_blocked(self):
        c = self.base()
        mutate_node(c, "S1")["obligations"] = None
        self.blocks(c, "invalid proof obligations")


class MathGovEngineImpactAndTransitiveInvalidationTests(unittest.TestCase):
    def base(self):
        return copy.deepcopy(CASE)

    def test_impacted_descendants_source_change(self):
        c = self.base()
        n = mutate_node(c, "SRC-DEFS")
        n["content"] = "mutated definition"
        n["content_digest"] = e.digest("mutated definition")
        result = e.impact(CASE, c, BASELINE)
        self.assertEqual(result["verdict"], "IMPACT_REPORT_NOT_APPLIED", result)
        expected_affected = {"SRC-DEFS", "S1", "T1", "S2", "T2", "C1", "D1", "P1"}
        self.assertTrue(expected_affected.issubset(result["must_revalidate"]))

    def test_unrelated_branch_not_overinvalidated(self):
        c = self.base()
        n = mutate_node(c, "S2")
        n["goal"] = "other goal"
        n["goal_digest"] = e.digest("other goal")
        result = e.impact(CASE, c, BASELINE)
        self.assertNotIn("T3", result["must_revalidate"])

    def test_root_change_invalidates_all(self):
        c = self.base()
        c["original"]["text"] = "mutated intent"
        c["original"]["digest"] = e.digest("mutated intent")
        result = e.impact(CASE, c, BASELINE)
        self.assertEqual(set(result["must_revalidate"]), set(CASE["required_inventory"]))

    def test_diff_anchor_mismatch_blocked(self):
        self.assertEqual(e.impact(CASE, CASE, "0" * 64)["verdict"], "BLOCKED")

    def test_task_readiness_requires_prerequisites(self):
        self.assertEqual(e.task_readiness(CASE, "T2")["dispatch"], "BLOCKED_DEPENDENCIES")
        r = e.task_readiness(CASE, "T2", ["T1"])
        self.assertEqual(r["dispatch"], "STRUCTURALLY_READY_HOST_GRANT_REQUIRED")
        self.assertEqual(r["original_digest"], ORIGINAL)

    def test_task_cannot_self_advance(self):
        c = self.base()
        mutate_node(c, "T1")["state"] = "TASK_ACCEPTED"
        self.assertEqual(e.task_readiness(c, "T2")["dispatch"], "BLOCKED")

    def test_or_dependency_resolution(self):
        c = self.base()
        c["nodes"].append({"id": "T4", "kind": "TASK", "purpose": "RESEARCH", "state": "PLANNED", "branch": "ROOT", "step_ids": []})
        c["required_inventory"].append("T4")
        edge = {"source": "T4", "target": "T2", "kind": "OR", "group": "alternatives"}
        c["edges"].append(edge)
        c["required_edges"].append(edge)
        # T1 alone does not satisfy T2 because T4 alternative is also in OR group
        self.assertEqual(e.task_readiness(c, "T2", ["T1"])["dispatch"], "BLOCKED_DEPENDENCIES")
        # Providing both T1 and T4 satisfies it
        self.assertEqual(e.task_readiness(c, "T2", ["T1", "T4"])["dispatch"], "STRUCTURALLY_READY_HOST_GRANT_REQUIRED")

    def test_progress_strictly_unknown_without_kernel_proof(self):
        out = e.progress(CASE)
        self.assertEqual(out["tasks_execution_finished"], 1)
        self.assertEqual(out["theorem_progress_percent"], "UNKNOWN")
        self.assertFalse(out["proof_verified"])


class MathGovEventLedgerTests(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        ev.init(self.conn)

    def test_exact_binary_roundtrip(self):
        prompt_bytes = b"user prompt with binary \x00\xff and \n newlines"
        result_bytes = b"model response \x00\xc3\xa9 utf-8 stream"
        ev.append(self.conn, "PROMPT_RESULT", "worker_node_1", "S1", prompt_bytes, result_bytes)
        stored_raw = self.conn.execute("SELECT event FROM events").fetchone()[0]
        stored_obj = json.loads(stored_raw)
        self.assertEqual(ev.verify_bytes(stored_obj["prompt"]), prompt_bytes)
        self.assertEqual(ev.verify_bytes(stored_obj["result"]), result_bytes)

    def test_ledger_hash_chain_verification(self):
        ev.append(self.conn, "EVENT_1", "worker", "S1", b"p1", b"r1")
        ev.append(self.conn, "EVENT_2", "worker", "S2", b"p2", b"r2")
        ev.append(self.conn, "EVENT_3", "reviewer", "S2", b"p3", b"r3")
        res = ev.verify(self.conn)
        self.assertEqual(res["verdict"], "LOCAL_CHAIN_VALID_UNAUTHENTICATED")
        self.assertEqual(res["count"], 3)

    def test_ledger_tamper_detection(self):
        ev.append(self.conn, "EVENT_1", "worker", "S1", b"original", b"res")
        self.conn.execute("UPDATE events SET event = ? WHERE seq = 1", (json.dumps({"tampered": True}),))
        self.conn.commit()
        res = ev.verify(self.conn)
        self.assertIn(res["verdict"], ("TAMPER_DETECTED", "TAMPER_OR_INVALID_EVENT"))

    def test_ledger_truncation_detection(self):
        ev.append(self.conn, "EVENT_1", "worker", "S1", b"one", b"two")
        ev.append(self.conn, "EVENT_2", "worker", "S2", b"three", b"four")
        self.conn.execute("DELETE FROM events WHERE seq = 2")
        self.conn.commit()
        res = ev.verify(self.conn, expected_count=2)
        self.assertEqual(res["verdict"], "EVENT_COUNT_MISMATCH")

    def test_ledger_external_anchor_mismatch(self):
        ev.append(self.conn, "EVENT_1", "worker", "S1", b"one", b"two")
        res = ev.verify(self.conn, externally_anchored_head="0" * 64)
        self.assertEqual(res["verdict"], "EXTERNAL_ANCHOR_MISMATCH")


if __name__ == "__main__":
    unittest.main()
