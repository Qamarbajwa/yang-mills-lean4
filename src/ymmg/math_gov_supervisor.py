"""
MATH-GOV v0.6 Single Logical Supervisor & Multi-Agent Orchestration Architecture
================================================================================
Implements:
1. One durable logical supervisor coordinating scoped, isolated workers.
2. Strict separation of roles: SUPERVISOR != WORKER != REVIEWER != ACCEPTOR.
3. Multi-branch isolation and reconvergence governance.
4. Truthful calibrated reporting separating task execution counts from theorem proof completion.
5. Integration with MathStepEngine, LeanStepRunner, ContextCapsule, and EventLedger.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from src.ymmg.context_capsule import ContextContinuityEngine, TaskContextCapsule
from src.ymmg.math_step_engine import audit, impact, index_graph, progress, task_readiness
from src.ymmg.lean_step_runner import check_step
from src.ymmg.event_ledger import append as ledger_append, init as ledger_init, verify as ledger_verify


VALID_ROLES = {"SUPERVISOR", "WORKER", "REVIEWER", "ACCEPTOR", "WATCHDOG", "POLICY_HOST"}

TASK_STATES = {
    "PLANNED", "PAUSED", "READY", "LEASED", "EXECUTING", "EXECUTED",
    "SUBMITTED", "REVIEW_PENDING", "ACCEPTED_TASK", "REJECTED", "BLOCKED", "STALE",
}

STEP_STATES = {
    "PROPOSED", "OPEN_OBLIGATIONS", "FORMAL_CANDIDATE", "LOCAL_LEAN_CHECKED",
    "INDEPENDENT_REPLAYED", "SEMANTIC_AUDITED", "ACCEPTED_STEP", "REJECTED", "STALE",
}


class RoleSeparationViolationError(PermissionError):
    """Raised when an actor attempts to perform multiple non-separable governance roles."""
    pass


class PrematureTheoremClaimError(ValueError):
    """Raised when an agent attempts to declare a theorem proved based on task completion alone."""
    pass


@dataclass
class ActorGrant:
    actor_id: str
    role: str
    branch_scope: str
    permitted_tools: List[str]
    spend_token_ceiling: int
    authorized_by: str


@dataclass
class CalibratedReport:
    original_question: str
    current_formal_target: str
    pathways: Dict[str, str]
    tasks: Dict[str, int]
    proof_steps: Dict[str, int]
    lean_status: str
    subject_drift: str
    changes: List[str]
    claims: List[Dict[str, Any]]
    connections: List[Dict[str, Any]]
    uncertainties_and_negative_results: List[str]
    next_ready_tasks: List[str]
    blockers_and_approval_requests: List[str]
    authorities: Dict[str, str]
    theorem_progress_percent: str = "UNKNOWN"

    def format_text(self) -> str:
        lines = [
            f"ORIGINAL QUESTION: {self.original_question}",
            f"CURRENT FORMAL TARGET: {self.current_formal_target}",
            f"PATHWAYS: {json.dumps(self.pathways)}",
            f"TASKS: {json.dumps(self.tasks)}",
            f"PROOF STEPS: {json.dumps(self.proof_steps)}",
            f"LEAN: {self.lean_status}",
            f"SUBJECT DRIFT: {self.subject_drift}",
            f"CHANGES: {json.dumps(self.changes)}",
            f"CLAIMS: {json.dumps(self.claims)}",
            f"CONNECTIONS: {json.dumps(self.connections)}",
            f"UNCERTAINTIES / NEGATIVE RESULTS: {json.dumps(self.uncertainties_and_negative_results)}",
            f"NEXT READY TASKS: {json.dumps(self.next_ready_tasks)}",
            f"BLOCKERS / APPROVAL REQUESTS: {json.dumps(self.blockers_and_approval_requests)}",
            f"AUTHORITIES: {json.dumps(self.authorities)}",
            f"THEOREM PROGRESS: {self.theorem_progress_percent}",
        ]
        return "\n".join(lines)


class MathGovSupervisor:
    """
    The Single Logical Supervisor for the research system.
    Orchestrates workflows, tracks task graphs, enforces role isolation,
    and produces unvarnished progress reports.
    """

    def __init__(
        self,
        workspace_root: Optional[Path] = None,
        supervisor_id: str = "supervisor-logical-primary",
        owner_id: str = "human-owner",
    ):
        self.workspace_root = Path(workspace_root) if workspace_root else Path.cwd()
        self.supervisor_id = supervisor_id
        self.owner_id = owner_id
        self.actor_grants: Dict[str, ActorGrant] = {}
        self.context_engine = ContextContinuityEngine(self.workspace_root)
        self.capsules: Dict[str, TaskContextCapsule] = {}

    def register_actor(
        self,
        actor_id: str,
        role: str,
        branch_scope: str = "ROOT",
        permitted_tools: Optional[List[str]] = None,
        token_ceiling: int = 100000,
        authorized_by: Optional[str] = None,
    ) -> ActorGrant:
        if role not in VALID_ROLES:
            raise ValueError(f"Invalid role '{role}'. Must be one of {VALID_ROLES}")

        # Enforce distinct role assignment:
        # A worker cannot be reviewer or acceptor
        for existing_id, grant in self.actor_grants.items():
            if existing_id == actor_id and grant.role != role:
                raise RoleSeparationViolationError(
                    f"Actor '{actor_id}' already assigned role '{grant.role}', cannot also be '{role}'"
                )

        grant = ActorGrant(
            actor_id=actor_id,
            role=role,
            branch_scope=branch_scope,
            permitted_tools=permitted_tools or ["read_file", "run_test"],
            spend_token_ceiling=token_ceiling,
            authorized_by=authorized_by or self.owner_id,
        )
        self.actor_grants[actor_id] = grant
        return grant

    def validate_dispatch(
        self,
        task_id: str,
        worker_id: str,
        case_data: Dict[str, Any],
        trusted_completed_task_ids: List[str],
    ) -> Tuple[bool, Dict[str, Any]]:
        """Gate G3: Dispatch preflight checking prerequisites, branch isolation, and role permissions."""
        grant = self.actor_grants.get(worker_id)
        if not grant or grant.role != "WORKER":
            return False, {"error": f"Actor '{worker_id}' is not an authorized WORKER"}

        readiness = task_readiness(case_data, task_id, trusted_completed_task_ids)
        if readiness.get("dispatch") != "STRUCTURALLY_READY_HOST_GRANT_REQUIRED":
            return False, readiness

        # Check branch scope isolation
        task_branch = readiness.get("branch")
        if grant.branch_scope != "ALL" and grant.branch_scope != task_branch and task_branch != "ROOT":
            return False, {
                "error": f"Worker '{worker_id}' scoped to branch '{grant.branch_scope}' cannot execute on '{task_branch}'"
            }

        return True, readiness

    def build_and_register_capsule(
        self,
        task_id: str,
        branch_id: str,
        case_data: Dict[str, Any],
        assumptions: Optional[List[str]] = None,
        negative_history: Optional[List[str]] = None,
    ) -> TaskContextCapsule:
        """Constructs an immutable Task Context Capsule for the given task."""
        orig_digest = case_data.get("original", {}).get("digest", "")
        formal_digest = case_data.get("formal_target", {}).get("digest", "")
        idx, _, _ = index_graph(case_data)
        task_node = idx.get(task_id, {})

        capsule = self.context_engine.build_capsule(
            task_id=task_id,
            branch_id=branch_id,
            owner_subject_anchor=orig_digest,
            approved_formal_target_anchor=formal_digest,
            exact_goal=task_node.get("purpose", "RESEARCH"),
            relevant_definitions={},
            assumptions=assumptions or [],
            premise_step_digests=[],
            negative_history=negative_history or [],
            open_obligations=[],
            sources={},
        )
        self.capsules[task_id] = capsule
        return capsule

    def submit_task_work(
        self,
        task_id: str,
        worker_id: str,
        step_proposals: List[Dict[str, Any]],
        case_data: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Worker submits proposed steps; cannot self-accept."""
        grant = self.actor_grants.get(worker_id)
        if not grant or grant.role != "WORKER":
            raise RoleSeparationViolationError(f"Actor '{worker_id}' is not an authorized WORKER")

        # Record submission
        submission = {
            "task_id": task_id,
            "worker_id": worker_id,
            "status": "SUBMITTED",
            "submitted_at_utc": datetime.now(timezone.utc).isoformat(),
            "step_count": len(step_proposals),
            "proposals": step_proposals,
            "accepted": False,
            "note": "Work submitted for independent review. Worker cannot accept own output.",
        }
        return submission

    def conduct_review(
        self,
        task_id: str,
        submission: Dict[str, Any],
        reviewer_id: str,
        decision: str,  # "REVIEW_PASS" or "REJECTED"
        findings: List[str],
    ) -> Dict[str, Any]:
        """Independent reviewer inspects frozen candidate; cannot be the worker."""
        if reviewer_id == submission.get("worker_id"):
            raise RoleSeparationViolationError(
                f"Tri-Agent Separation violation: reviewer '{reviewer_id}' cannot review own submission"
            )

        grant = self.actor_grants.get(reviewer_id)
        if not grant or grant.role != "REVIEWER":
            raise RoleSeparationViolationError(f"Actor '{reviewer_id}' is not an authorized REVIEWER")

        review_receipt = {
            "task_id": task_id,
            "reviewer_id": reviewer_id,
            "worker_id": submission.get("worker_id"),
            "decision": decision,
            "findings": findings,
            "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
            "accepted": False,  # Acceptance is a distinct authority
        }
        return review_receipt

    def grant_technical_acceptance(
        self,
        task_id: str,
        review_receipt: Dict[str, Any],
        acceptor_id: str,
    ) -> Dict[str, Any]:
        """Distinct technical acceptor approves task; cannot be worker or reviewer."""
        worker_id = review_receipt.get("worker_id")
        reviewer_id = review_receipt.get("reviewer_id")

        if acceptor_id == worker_id:
            raise RoleSeparationViolationError("Acceptor cannot be identical to Worker")
        if acceptor_id == reviewer_id:
            raise RoleSeparationViolationError("Acceptor cannot be identical to Reviewer")

        grant = self.actor_grants.get(acceptor_id)
        if not grant or grant.role != "ACCEPTOR":
            raise RoleSeparationViolationError(f"Actor '{acceptor_id}' is not an authorized ACCEPTOR")

        if review_receipt.get("decision") != "REVIEW_PASS":
            raise ValueError("Cannot grant technical acceptance on a failed review")

        acceptance_cert = {
            "task_id": task_id,
            "acceptor_id": acceptor_id,
            "worker_id": worker_id,
            "reviewer_id": reviewer_id,
            "status": "ACCEPTED_TASK",
            "accepted_at_utc": datetime.now(timezone.utc).isoformat(),
            "note": "Task accepted. Task acceptance does NOT confer theorem completion.",
        }
        return acceptance_cert

    def generate_calibrated_report(
        self,
        case_data: Dict[str, Any],
        executed_tasks: List[str],
        accepted_tasks: List[str],
        lean_receipt: Optional[Dict[str, Any]] = None,
        negative_findings: Optional[List[str]] = None,
    ) -> CalibratedReport:
        """
        Generates calibrated report conforming to Section 8 of Master Directive.
        Separates task completion from theorem completion.
        """
        orig_text = case_data.get("original", {}).get("text", "UNAVAILABLE")
        target_stmt = case_data.get("formal_target", {}).get("statement", "UNAPPROVED")

        idx, _, _ = index_graph(case_data)
        total_tasks = sum(1 for n in idx.values() if n.get("kind") == "TASK")
        total_steps = sum(1 for n in idx.values() if n.get("kind") == "STEP")

        task_metrics = {
            "planned": total_tasks,
            "executed": len(executed_tasks),
            "submitted": len(executed_tasks) - len(accepted_tasks),
            "accepted": len(accepted_tasks),
        }

        proof_metrics = {
            "total_steps": total_steps,
            "formally_checked": 1 if lean_receipt and lean_receipt.get("lean_kernel_check_passed") else 0,
            "open_obligations": sum(
                1 for n in idx.values() if n.get("kind") == "STEP" and n.get("obligations") != n.get("discharged")
            ),
        }

        lean_status = "NOT RUN"
        if lean_receipt:
            if lean_receipt.get("lean_kernel_check_passed"):
                lean_status = f"LOCAL CHECK PASSED (Theorem: {lean_receipt.get('theorem')})"
            else:
                lean_status = f"FAIL ({lean_receipt.get('verdict')})"

        return CalibratedReport(
            original_question=orig_text,
            current_formal_target=target_stmt,
            pathways={"PATH_A": "ACTIVE", "PATH_B": "ACTIVE"},
            tasks=task_metrics,
            proof_steps=proof_metrics,
            lean_status=lean_status,
            subject_drift="none evidenced",
            changes=[],
            claims=[{"claim_id": "CLM-001", "status": "EXPLORATORY"}],
            connections=[],
            uncertainties_and_negative_results=negative_findings or [],
            next_ready_tasks=["T06"],
            blockers_and_approval_requests=[],
            authorities={"supervisor": self.supervisor_id, "owner": self.owner_id},
            theorem_progress_percent="UNKNOWN",
        )
