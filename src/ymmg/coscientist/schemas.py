"""
Research Co-Scientist OS — Typed Information Model
=================================================
Conforms to COSCIENTIST_DF_v0_1 schemas/hypothesis.schema.json and 05_INFORMATION_MODEL.md.
Tailored for constructive 4D Yang-Mills Continuum QFT & Mass Gap discovery.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
from typing import Any, Dict, List, Optional

from src.ymmg.coscientist.kernel import Stage, digest


@dataclass
class Citation:
    source_id: str
    source_span_id: str
    support_status: str = "NOT_CHECKED"  # NOT_CHECKED, SUPPORTS, PARTIAL, CONTRADICTS, UNRELATED, RETRACTED
    retrieved_at: Optional[str] = None


@dataclass
class ResearchGoal:
    goal_id: str
    title: str
    objective: str
    target_obstruction: str  # e.g., "NEG-YM-101"
    constraints: List[str]
    constraints_frozen_digest: str
    risk_class: str = "SAFE_THEORETICAL_MATH"
    clay_problem_status: str = "OPEN_AND_UNSOLVED"
    created_at_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class YangMillsHypothesis:
    hypothesis_id: str
    version_id: str
    goal_id: str
    run_id: str
    title: str
    statement: str
    mechanism_family: str  # e.g., TWISTED_HOLONOMY, CENTER_VORTEX, RESURGENCE, GRIBOV_HORIZON
    assumptions: List[str]
    falsifiers: List[str]
    predictions: List[str]
    rational_parameters: Dict[str, Fraction] = field(default_factory=dict)
    lean_candidate_code: Optional[str] = None
    lean_theorem_name: Optional[str] = None
    lean_formal_statement: Optional[str] = None
    citations: List[Citation] = field(default_factory=list)
    parent_version_ids: List[str] = field(default_factory=list)
    creator_role: str = "GENERATION_AGENT"
    created_at_utc: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    # Multi-axis state tracking (rank != verification)
    proposal_state: str = "DRAFT"
    evidence_state: str = "UNCHECKED"
    formal_state: str = "UNTESTED"
    empirical_state: str = "NOT_APPLICABLE"
    novelty_state: str = "UNKNOWN"
    safety_state: str = "PENDING"
    elo: float = 1200.0
    cluster_id: Optional[str] = None

    @property
    def content_digest(self) -> str:
        return digest(self.statement)

    def to_schema_dict(self) -> Dict[str, Any]:
        return {
            "hypothesis_id": self.hypothesis_id,
            "version_id": self.version_id,
            "goal_id": self.goal_id,
            "run_id": self.run_id,
            "statement": self.statement,
            "content_digest": self.content_digest,
            "parent_version_ids": list(self.parent_version_ids),
            "assumptions": list(self.assumptions),
            "falsifiers": list(self.falsifiers),
            "predictions": list(self.predictions),
            "mechanism": self.mechanism_family,
            "citations": [
                {
                    "source_id": c.source_id,
                    "source_span_id": c.source_span_id,
                    "support_status": c.support_status,
                    "retrieved_at": c.retrieved_at,
                }
                for c in self.citations
            ],
            "proposal_state": self.proposal_state,
            "evidence_state": self.evidence_state,
            "formal_state": self.formal_state,
            "empirical_state": self.empirical_state,
            "novelty_state": self.novelty_state,
            "safety_state": self.safety_state,
            "creator_role": self.creator_role,
            "created_at": self.created_at_utc,
        }


@dataclass
class ReflectionReport:
    hypothesis_id: str
    passed: bool
    negative_barriers_checked: List[str]
    matched_obstructions: List[str]
    assumption_audit: str
    falsifier_audit: str
    citation_grounding_ok: bool
    recommended_stage: Stage
    notes: List[str] = field(default_factory=list)


@dataclass
class TournamentMatch:
    match_id: str
    hypothesis_a_id: str
    hypothesis_b_id: str
    winner_id: Optional[str]  # None if tie/abstain
    ab_outcome: str  # A, B, TIE
    ba_outcome: str  # A, B, TIE
    positional_bias_detected: bool
    tie: bool
    rationale: str


@dataclass
class EvolutionLineage:
    parent_ids: List[str]
    child_id: str
    mutation_strategy: str
    rationale: str


@dataclass
class MetaReviewReport:
    run_id: str
    goal_id: str
    total_hypotheses: int
    pareto_top_ids: List[str]
    quarantined_ids: List[str]
    verified_claims_ids: List[str]
    recurring_failures: List[str]
    next_proof_obligations: List[str]
    epistemic_status: str = "OPEN_AND_UNSOLVED"
    summary: str = ""
