"""
Research Co-Scientist OS — Autonomous Mathematical Discovery & Verification Engine
==================================================================================
Based on Google DeepMind Co-Scientist (Nature 2026) and the Dark Factory Build Spec v0.1.
Adapted specifically for the Constructive 4D Yang-Mills Continuum QFT & Mass Gap Project.

Provides:
- 6 Specialized Research Roles (Generation, Reflection, Proximity, Evolution, Ranking, Meta-Review)
- Fail-Closed Gate Kernel (Stage transition policy, no-bypass invariants I-01..I-12)
- Information Model (Hypothesis, ResearchGoal, GateSignals, VerificationReceipt)
- Verifier Bridge (Lean 4.35 kernel preflight, Dream-RSI counterfactual replay, Chrysalis 4 security gates)
- Autonomous Research Orchestrator for Yang-Mills Crossover Obstruction Exploration
"""

from src.ymmg.coscientist.kernel import (
    Denied,
    GateSignals,
    Hypothesis,
    ResearchGateKernel,
    Stage,
    VerificationReceipt,
    digest,
)
from src.ymmg.coscientist.schemas import (
    Citation,
    EvolutionLineage,
    MetaReviewReport,
    ReflectionReport,
    ResearchGoal,
    TournamentMatch,
    YangMillsHypothesis,
)
from src.ymmg.coscientist.roles import (
    YMEvolutionAgent,
    YMGenerationAgent,
    YMMetaReviewAgent,
    YMProximityAgent,
    YMRankingAgent,
    YMReflectionAgent,
)
from src.ymmg.coscientist.verifier_bridge import (
    CoScientistVerifierBridge,
)
from src.ymmg.coscientist.orchestrator import (
    YangMillsCoScientistOrchestrator,
)

__all__ = [
    "Denied",
    "GateSignals",
    "Hypothesis",
    "ResearchGateKernel",
    "Stage",
    "VerificationReceipt",
    "digest",
    "Citation",
    "EvolutionLineage",
    "MetaReviewReport",
    "ReflectionReport",
    "ResearchGoal",
    "TournamentMatch",
    "YangMillsHypothesis",
    "YMGenerationAgent",
    "YMReflectionAgent",
    "YMProximityAgent",
    "YMEvolutionAgent",
    "YMRankingAgent",
    "YMMetaReviewAgent",
    "CoScientistVerifierBridge",
    "YangMillsCoScientistOrchestrator",
]
