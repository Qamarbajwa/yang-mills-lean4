"""
MATH-GOV v0.6 Task Context Capsule (TCC) & Context Continuity Engine
====================================================================
Implements source-anchored context capsules, anchor recall verification,
and context rollover protection conforming to MATH-GOV v0.6 H09, H11, C15, C17.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


def sha256_digest(data: str | bytes) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


@dataclass
class ContextRecallProbe:
    """Probes worker recall of essential problem definitions and anchors after context transitions."""
    expected_original_digest: str
    expected_formal_digest: str
    expected_goal: str
    expected_negative_barriers: List[str]

    def verify_recall(
        self,
        reported_original_digest: str,
        reported_formal_digest: str,
        reported_goal: str,
        reported_negative_barriers: List[str],
    ) -> Tuple[bool, List[str]]:
        errors = []
        if reported_original_digest != self.expected_original_digest:
            errors.append(
                f"RECALL_FAILURE: Original question digest mismatch ({reported_original_digest} != {self.expected_original_digest})"
            )
        if reported_formal_digest != self.expected_formal_digest:
            errors.append(
                f"RECALL_FAILURE: Formal target digest mismatch ({reported_formal_digest} != {self.expected_formal_digest})"
            )
        if reported_goal.strip() != self.expected_goal.strip():
            errors.append("RECALL_FAILURE: Exact task goal text mismatch")
        for barrier in self.expected_negative_barriers:
            if barrier not in reported_negative_barriers:
                errors.append(f"RECALL_FAILURE: Historical negative barrier '{barrier}' omitted from worker memory")
        return len(errors) == 0, errors


@dataclass
class TaskContextCapsule:
    """Source-anchored task context capsule for bounded worker dispatch."""
    task_id: str
    branch_id: str
    owner_subject_anchor: str
    approved_formal_target_anchor: str
    exact_goal: str
    relevant_definitions: Dict[str, str]
    assumptions: List[str]
    premise_step_digests: List[str]
    negative_history: List[str]
    open_obligations: List[str]
    sources: Dict[str, str]  # path -> sha256
    toolchain: str
    permitted_tools: List[str]
    token_budget: int
    deadline_lease: str
    created_at_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    read_receipt: Optional[Dict[str, Any]] = None

    def canonical_json(self) -> str:
        payload = {
            "task_id": self.task_id,
            "branch_id": self.branch_id,
            "owner_subject_anchor": self.owner_subject_anchor,
            "approved_formal_target_anchor": self.approved_formal_target_anchor,
            "exact_goal": self.exact_goal,
            "relevant_definitions": self.relevant_definitions,
            "assumptions": self.assumptions,
            "premise_step_digests": sorted(self.premise_step_digests),
            "negative_history": sorted(self.negative_history),
            "open_obligations": sorted(self.open_obligations),
            "sources": self.sources,
            "toolchain": self.toolchain,
            "permitted_tools": sorted(self.permitted_tools),
            "token_budget": self.token_budget,
            "deadline_lease": self.deadline_lease,
            "created_at_utc": self.created_at_utc,
        }
        return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))

    def compute_digest(self) -> str:
        return sha256_digest(self.canonical_json())

    def record_read_receipt(self, worker_id: str, probe_answers: Dict[str, Any]) -> Tuple[bool, List[str]]:
        probe = ContextRecallProbe(
            expected_original_digest=self.owner_subject_anchor,
            expected_formal_digest=self.approved_formal_target_anchor,
            expected_goal=self.exact_goal,
            expected_negative_barriers=self.negative_history,
        )
        passed, errors = probe.verify_recall(
            reported_original_digest=probe_answers.get("original_digest", ""),
            reported_formal_digest=probe_answers.get("formal_digest", ""),
            reported_goal=probe_answers.get("goal", ""),
            reported_negative_barriers=probe_answers.get("negative_barriers", []),
        )
        receipt = {
            "worker_id": worker_id,
            "capsule_digest": self.compute_digest(),
            "acknowledged_at_utc": datetime.now(timezone.utc).isoformat(),
            "recall_probe_passed": passed,
            "recall_errors": errors,
        }
        self.read_receipt = receipt
        return passed, errors

    def is_lease_expired(self, now_iso: Optional[str] = None) -> bool:
        """Checks if absolute deadline lease has expired."""
        if self.deadline_lease.endswith("h") or self.deadline_lease.endswith("m"):
            return False
        try:
            now = datetime.fromisoformat(now_iso) if now_iso else datetime.now(timezone.utc)
            expiry = datetime.fromisoformat(self.deadline_lease)
            if expiry.tzinfo is None:
                expiry = expiry.replace(tzinfo=timezone.utc)
            if now.tzinfo is None:
                now = now.replace(tzinfo=timezone.utc)
            return now >= expiry
        except Exception:
            return False


class ContextContinuityEngine:
    """Manages creation, verification, and rollover of task context capsules."""

    def __init__(self, workspace_root: Optional[Path] = None):
        self.workspace_root = Path(workspace_root) if workspace_root else Path.cwd()

    def build_capsule(
        self,
        task_id: str,
        branch_id: str,
        owner_subject_anchor: str,
        approved_formal_target_anchor: str,
        exact_goal: str,
        relevant_definitions: Dict[str, str],
        assumptions: List[str],
        premise_step_digests: List[str],
        negative_history: List[str],
        open_obligations: List[str],
        sources: Dict[str, str],
        toolchain: str = "leanprover/lean4:v4.35.0",
        permitted_tools: Optional[List[str]] = None,
        token_budget: int = 100000,
        deadline_lease: str = "1h",
    ) -> TaskContextCapsule:
        """Validates all mandatory fields and returns an immutable TaskContextCapsule."""
        if not owner_subject_anchor or len(owner_subject_anchor) != 64:
            raise ValueError("Invalid owner_subject_anchor (must be 64-char hex digest)")
        if not approved_formal_target_anchor or len(approved_formal_target_anchor) != 64:
            raise ValueError("Invalid approved_formal_target_anchor (must be 64-char hex digest)")
        if not exact_goal.strip():
            raise ValueError("exact_goal cannot be empty")

        tools = permitted_tools or ["read_file", "run_test", "run_lean"]
        return TaskContextCapsule(
            task_id=task_id,
            branch_id=branch_id,
            owner_subject_anchor=owner_subject_anchor,
            approved_formal_target_anchor=approved_formal_target_anchor,
            exact_goal=exact_goal,
            relevant_definitions=dict(relevant_definitions),
            assumptions=list(assumptions),
            premise_step_digests=list(premise_step_digests),
            negative_history=list(negative_history),
            open_obligations=list(open_obligations),
            sources=dict(sources),
            toolchain=toolchain,
            permitted_tools=tools,
            token_budget=token_budget,
            deadline_lease=deadline_lease,
        )
