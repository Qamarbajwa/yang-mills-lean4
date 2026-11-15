"""
Research Co-Scientist OS — Fail-Closed Research Gate Kernel
============================================================
Conforms to COSCIENTIST_DF_v0_1 06_STATES_AND_GATES.md and reference_kernel/core.py.
Enforces no-bypass state invariants I-01 through I-12:
- State transitions are server-authoritative, caller-gated ('policy_service' only).
- Non-adjacent or backward stage transitions are strictly denied.
- Source provenance and reflection are mandatory prerequisites before tournament ranking.
- Elo ranking and tournament victories NEVER automatically grant formal verification.
- Verification requires an authenticated VerificationReceipt with strict identity separation
  (builder != verifier, exact target digest match, protected suite pass).
"""

from __future__ import annotations
from dataclasses import dataclass, replace
from enum import Enum
from hashlib import sha256
from typing import Dict, List, Optional, Tuple


class Denied(ValueError):
    """Fail-closed gate denial."""
    pass


class Stage(str, Enum):
    DRAFT = "DRAFT"
    SCREENED = "SCREENED"
    GROUNDED = "GROUNDED"
    REVIEWED = "REVIEWED"
    ELIGIBLE = "ELIGIBLE"
    RANKED = "RANKED"
    PROPOSAL_READY = "PROPOSAL_READY"
    QUARANTINED = "QUARANTINED"


ORDER = (
    Stage.DRAFT,
    Stage.SCREENED,
    Stage.GROUNDED,
    Stage.REVIEWED,
    Stage.ELIGIBLE,
    Stage.RANKED,
    Stage.PROPOSAL_READY,
)


@dataclass(frozen=True)
class Hypothesis:
    hypothesis_id: str
    statement: str
    content_digest: str
    parent_ids: Tuple[str, ...] = ()
    stage: Stage = Stage.DRAFT
    evidence_state: str = "UNCHECKED"
    formal_state: str = "UNTESTED"
    empirical_state: str = "NOT_APPLICABLE"
    elo: float = 1200.0


@dataclass(frozen=True)
class GateSignals:
    goal_safe: bool = False
    hypothesis_safe: bool = False
    source_verified: bool = False
    reflection_completed: bool = False
    tournament_assessed: bool = False
    report_discloses_limits: bool = False


@dataclass(frozen=True)
class VerificationReceipt:
    hypothesis_id: str
    exact_target_digest: str
    evidence_digest: str
    claim_type: str  # "MATH_PROOF" or "EMPIRICAL_REPLICATION"
    builder_identity: str
    verifier_identity: str
    independently_verified: bool
    protected_suite_passed: bool
    semantic_review_passed: bool
    verifier_authority_bound: bool
    verification_scope: str = "FINITE_DIMENSIONAL_MATRIX_AUDIT"


def digest(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


class ResearchGateKernel:
    """Deterministic, fail-closed policy kernel for hypothesis lifecycle governance."""

    def __init__(self) -> None:
        self._items: Dict[str, Hypothesis] = {}
        self._verified: Dict[str, VerificationReceipt] = {}
        self._matches: List[Tuple[str, str, str]] = []
        self.audit: List[str] = []

    def get(self, hypothesis_id: str) -> Hypothesis:
        try:
            return self._items[hypothesis_id]
        except KeyError as e:
            raise Denied("UNKNOWN_HYPOTHESIS") from e

    def all_hypotheses(self) -> List[Hypothesis]:
        return list(self._items.values())

    def add(
        self,
        hypothesis_id: str,
        statement: str,
        parent_ids: Tuple[str, ...] = (),
    ) -> Hypothesis:
        if not hypothesis_id or not statement.strip() or hypothesis_id in self._items:
            raise Denied("INVALID_OR_DUPLICATE_CANDIDATE")
        if len(set(parent_ids)) != len(parent_ids) or hypothesis_id in parent_ids:
            raise Denied("INVALID_LINEAGE")
        for parent_id in parent_ids:
            self.get(parent_id)
        candidate = Hypothesis(hypothesis_id, statement, digest(statement), parent_ids)
        self._items[hypothesis_id] = candidate
        self.audit.append(f"ADD {hypothesis_id} {candidate.content_digest}")
        return candidate

    def evolve(self, parent_id: str, new_id: str, new_statement: str) -> Hypothesis:
        self.get(parent_id)
        # Crucial invariant: child has no inherited gate, proof, or Elo credibility.
        return self.add(new_id, new_statement, (parent_id,))

    def advance(
        self,
        hypothesis_id: str,
        target: Stage,
        signals: GateSignals,
        *,
        caller: str,
    ) -> Hypothesis:
        item = self.get(hypothesis_id)
        if caller != "policy_service":
            raise Denied("ONLY_POLICY_SERVICE_CAN_ADVANCE")
        if item.stage not in ORDER or target not in ORDER:
            raise Denied("QUARANTINE_OR_UNKNOWN_STAGE")
        pos = ORDER.index(item.stage)
        if pos + 1 >= len(ORDER) or target != ORDER[pos + 1]:
            raise Denied("NON_ADJACENT_OR_REVERSE_TRANSITION")
        if not (signals.goal_safe and signals.hypothesis_safe):
            raise Denied("SAFETY_NOT_ALLOWED")
        if target in (
            Stage.GROUNDED,
            Stage.REVIEWED,
            Stage.ELIGIBLE,
            Stage.RANKED,
            Stage.PROPOSAL_READY,
        ) and not signals.source_verified:
            raise Denied("SOURCE_PROVENANCE_UNVERIFIED")
        if target in (
            Stage.REVIEWED,
            Stage.ELIGIBLE,
            Stage.RANKED,
            Stage.PROPOSAL_READY,
        ) and not signals.reflection_completed:
            raise Denied("SOURCE_GROUNDED_REFLECTION_MISSING")
        if target in (Stage.RANKED, Stage.PROPOSAL_READY) and not signals.tournament_assessed:
            raise Denied("TOURNAMENT_EVIDENCE_MISSING")
        if target == Stage.PROPOSAL_READY and not signals.report_discloses_limits:
            raise Denied("REPORT_DISCLOSURE_INCOMPLETE")

        item = replace(item, stage=target)
        if target == Stage.GROUNDED:
            item = replace(item, evidence_state="SOURCE_GROUNDED")
        self._items[item.hypothesis_id] = item
        self.audit.append(f"ADVANCE {item.hypothesis_id} {target.value}")
        return item

    def quarantine(
        self,
        hypothesis_id: str,
        reason: str = "POLICY_QUARANTINE",
        *,
        caller: str,
    ) -> Hypothesis:
        if caller not in ("policy_service", "safety_verifier", "evidence_verifier"):
            raise Denied("UNAUTHORIZED_QUARANTINE_CALLER")
        item = replace(
            self.get(hypothesis_id),
            stage=Stage.QUARANTINED,
            formal_state="REVOKED",
            empirical_state="REVOKED",
        )
        self._items[hypothesis_id] = item
        self.audit.append(f"QUARANTINE {hypothesis_id} {reason}")
        # Revoke verified status if quarantined
        if hypothesis_id in self._verified:
            del self._verified[hypothesis_id]
            self.audit.append(f"REVOKE_VERIFICATION {hypothesis_id}")
        return item

    def record_match(
        self,
        left_id: str,
        right_id: str,
        outcome: str = "LEFT",
        *,
        caller: str,
        tie: bool = False,
        abstain: bool = False,
    ) -> Tuple[float, float]:
        if caller != "tournament_service":
            raise Denied("ONLY_TOURNAMENT_SERVICE_RECORDS_MATCHES")
        if abstain:
            outcome = "ABSTAIN"
        elif tie:
            outcome = "TIE"
        if left_id == right_id or outcome not in ("LEFT", "RIGHT", "TIE", "ABSTAIN"):
            raise Denied("INVALID_MATCH")
        a = self.get(left_id)
        b = self.get(right_id)
        if a.stage not in (Stage.ELIGIBLE, Stage.RANKED) or b.stage not in (Stage.ELIGIBLE, Stage.RANKED):
            raise Denied("CANDIDATES_NOT_TOURNAMENT_ELIGIBLE")
        if outcome == "ABSTAIN":
            self._matches.append((left_id, right_id, "ABSTAIN"))
            self.audit.append(f"MATCH {left_id}:{a.elo:.1f} {right_id}:{b.elo:.1f} ABSTAIN")
            return a.elo, b.elo

        # Standard logistic Elo update (K = 32)
        kw = 32.0
        exp_a = 1.0 / (1.0 + 10.0 ** ((b.elo - a.elo) / 400.0))
        score_a = 1.0 if outcome == "LEFT" else 0.0 if outcome == "RIGHT" else 0.5
        score_b = 1.0 - score_a
        exp_b = 1.0 - exp_a

        new_a_elo = a.elo + kw * (score_a - exp_a)
        new_b_elo = b.elo + kw * (score_b - exp_b)

        self._items[left_id] = replace(a, elo=new_a_elo)
        self._items[right_id] = replace(b, elo=new_b_elo)
        self._matches.append((left_id, right_id, outcome))
        self.audit.append(f"MATCH {left_id}:{new_a_elo:.1f} {right_id}:{new_b_elo:.1f} {outcome}")
        return new_a_elo, new_b_elo

    def verify_claim(self, receipt: VerificationReceipt, *, caller: str) -> str:
        """
        External, protected verification path.
        Completely decoupled from tournament rank or Elo.
        """
        if caller != "independent_verification_service":
            raise Denied("ONLY_INDEPENDENT_VERIFIER_AUTHORIZED")
        item = self.get(receipt.hypothesis_id)
        if item.stage in (Stage.DRAFT, Stage.QUARANTINED):
            raise Denied("CANNOT_VERIFY_UNSCREENED_OR_QUARANTINED_CANDIDATE")
        if item.content_digest != receipt.exact_target_digest:
            raise Denied("EXACT_TARGET_MISMATCH")
        if not receipt.evidence_digest or len(receipt.evidence_digest) != 64:
            raise Denied("MISSING_EVIDENCE_DIGEST")
        if not receipt.verifier_identity or receipt.verifier_identity == receipt.builder_identity:
            raise Denied("SELF_VERIFICATION_FORBIDDEN")
        if not (
            receipt.independently_verified
            and receipt.protected_suite_passed
            and receipt.semantic_review_passed
            and receipt.verifier_authority_bound
        ):
            raise Denied("VERIFICATION_PREREQUISITES_MISSING")
        if receipt.claim_type not in ("MATH_PROOF", "EMPIRICAL_REPLICATION"):
            raise Denied("UNSUPPORTED_CLAIM_TYPE")

        self._verified[item.hypothesis_id] = receipt
        state = "APPROVED_PROOF" if receipt.claim_type == "MATH_PROOF" else "INDEPENDENTLY_REPLICATED"
        if receipt.claim_type == "MATH_PROOF":
            item = replace(item, formal_state=state)
        else:
            item = replace(item, empirical_state=state)
        self._items[item.hypothesis_id] = item
        self.audit.append(f"SIMULATED_CLAIM_VERIFICATION {item.hypothesis_id} {state}")
        return state

    def proposal_is_verified(self, hypothesis_id: str) -> bool:
        """Proposal progression or high Elo is never a shortcut to external verification."""
        return hypothesis_id in self._verified

    def get_verification_receipt(self, hypothesis_id: str) -> Optional[VerificationReceipt]:
        return self._verified.get(hypothesis_id)
