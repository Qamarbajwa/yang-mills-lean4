"""
Research Co-Scientist OS — Yang-Mills Discovery & Verification Orchestrator
===========================================================================
Coordinates the 6 specialized roles (Generation, Reflection, Proximity,
Ranking, Evolution, Meta-Review) through the fail-closed ResearchGateKernel
and Independent Verification Bridge (Exact Rational + Dream-RSI + Chrysalis
Gates + Live Lean 4.35 Kernel).

Never mutates master, preserves all negative evidence, and strictly maintains
the epistemic boundary: `clay_problem == "OPEN_AND_UNSOLVED"`.
"""

from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.ymmg.coscientist.kernel import (
    GateSignals,
    ResearchGateKernel,
    Stage,
    VerificationReceipt,
    digest,
)
from src.ymmg.coscientist.roles import (
    YMEvolutionAgent,
    YMGenerationAgent,
    YMMetaReviewAgent,
    YMProximityAgent,
    YMRankingAgent,
    YMReflectionAgent,
)
from src.ymmg.coscientist.schemas import (
    EvolutionLineage,
    MetaReviewReport,
    ReflectionReport,
    ResearchGoal,
    TournamentMatch,
    YangMillsHypothesis,
)
from src.ymmg.coscientist.verifier_bridge import (
    CoScientistVerifierBridge,
    VerificationBundleReport,
)


ROOT = Path(__file__).resolve().parents[3]


class YangMillsCoScientistOrchestrator:
    """
    End-to-end dark-factory research orchestrator for discovering, critiquing,
    evolving, ranking, and formally checking Yang-Mills crossover mechanisms.
    """

    def __init__(
        self,
        root_dir: Optional[Path] = None,
        builder_identity: str = "ym-coscientist-builder",
        verifier_identity: str = "independent-ym-verifier-service",
    ):
        self.root = Path(root_dir) if root_dir else ROOT
        self.builder_identity = builder_identity
        self.kernel = ResearchGateKernel()
        self.generator = YMGenerationAgent()
        self.reflector = YMReflectionAgent(register_path=self.root / "NEGATIVE_EVIDENCE_REGISTER.md")
        self.proximity = YMProximityAgent()
        self.ranker = YMRankingAgent()
        self.evolver = YMEvolutionAgent()
        self.meta_reviewer = YMMetaReviewAgent()
        self.verifier = CoScientistVerifierBridge(root_dir=self.root, verifier_identity=verifier_identity)

    @staticmethod
    def default_goal() -> ResearchGoal:
        constraints = [
            "Preserve exact fractions.Fraction arithmetic (zero floating-point tolerances).",
            "Do not regress against any historical barrier in NEGATIVE_EVIDENCE_REGISTER.md (NEG-YM-097..101).",
            "Maintain honest epistemic state: clay_problem = OPEN_AND_UNSOLVED unless full constructive continuum limit proved.",
            "Distinguish Elo tournament prioritization from Lean/rational sub-lemma formal verification.",
        ]
        constraints_digest = digest("\n".join(constraints))
        return ResearchGoal(
            goal_id="GOAL-YM-CROSSOVER-IR-001",
            title="Discover & Verify Mechanisms Resolving the SU(N) Yang-Mills IR Crossover Toron Barrier (NEG-YM-101)",
            objective=(
                "Generate, critique, evolve, and formally check mathematical strategies capable of projecting "
                "or bounding toron zero-mode moduli weight w_toron_vol strictly below the certified all-orders "
                "Cauchy polydisk margin 17838/1000000 across Edge E-CROSSOVER (Lemmas YM-059F, YM-060F, YM-101F)."
            ),
            target_obstruction="NEG-YM-101",
            constraints=constraints,
            constraints_frozen_digest=constraints_digest,
        )

    def _sync_hyp_from_kernel(self, hyp: YangMillsHypothesis) -> None:
        k_item = self.kernel.get(hyp.hypothesis_id)
        hyp.proposal_state = k_item.stage.value
        hyp.evidence_state = k_item.evidence_state
        hyp.formal_state = k_item.formal_state
        hyp.empirical_state = k_item.empirical_state
        hyp.elo = k_item.elo
        hyp.safety_state = "BLOCKED" if k_item.stage == Stage.QUARANTINED else "SAFE"

    def _screen_ground_reflect_to_reviewed(
        self,
        hyp: YangMillsHypothesis,
        reflection_reports: Dict[str, ReflectionReport],
    ) -> bool:
        """
        Drives a single DRAFT hypothesis sequentially through:
        DRAFT -> SCREENED -> GROUNDED -> REVIEWED, or QUARANTINED if unsafe/ungrounded/flawed.
        Always computes ReflectionReport for transparency.
        """
        # 1. Safety screening (DRAFT -> SCREENED)
        self.kernel.advance(
            hyp.hypothesis_id,
            Stage.SCREENED,
            GateSignals(goal_safe=True, hypothesis_safe=True),
            caller="policy_service",
        )

        # 2. Adversarial reflection (always computed for audit trail)
        rep = self.reflector.reflect(hyp)
        reflection_reports[hyp.hypothesis_id] = rep

        # 3. Citation grounding check before SCREENED -> GROUNDED
        if not rep.citation_grounding_ok:
            self.kernel.quarantine(
                hyp.hypothesis_id,
                "MISSING_OR_UNGROUNDED_CITATIONS",
                caller="evidence_verifier",
            )
            self._sync_hyp_from_kernel(hyp)
            return False

        self.kernel.advance(
            hyp.hypothesis_id,
            Stage.GROUNDED,
            GateSignals(goal_safe=True, hypothesis_safe=True, source_verified=True),
            caller="policy_service",
        )

        # 4. Full reflection gate (GROUNDED -> REVIEWED or QUARANTINED)
        if not rep.passed:
            reason = ",".join(rep.matched_obstructions) or "REFLECTION_CRITIQUE_FAILED"
            self.kernel.quarantine(hyp.hypothesis_id, reason, caller="safety_verifier")
            self._sync_hyp_from_kernel(hyp)
            return False

        self.kernel.advance(
            hyp.hypothesis_id,
            Stage.REVIEWED,
            GateSignals(
                goal_safe=True,
                hypothesis_safe=True,
                source_verified=True,
                reflection_completed=True,
            ),
            caller="policy_service",
        )
        self._sync_hyp_from_kernel(hyp)
        return True

    def run_discovery_cycle(
        self,
        goal: Optional[ResearchGoal] = None,
        run_id: str = "RUN-YM-COSCIENTIST-001",
        enable_lean: bool = True,
        require_lean_for_proof: bool = True,
        include_adversarial_flawed: bool = True,
    ) -> Dict[str, Any]:
        """
        Executes a complete governed Co-Scientist discovery & verification cycle.
        """
        active_goal = goal or self.default_goal()
        hypotheses_map: Dict[str, YangMillsHypothesis] = {}
        reflection_reports: Dict[str, ReflectionReport] = {}
        matches: List[TournamentMatch] = []
        lineages: List[EvolutionLineage] = []
        verification_reports: Dict[str, VerificationBundleReport] = {}
        verified_receipts: Dict[str, VerificationReceipt] = {}

        # ── Step 1: Generation ────────────────────────────────────────────────
        generated = self.generator.generate_candidates(
            active_goal,
            run_id=run_id,
            include_adversarial_flawed=include_adversarial_flawed,
        )
        for hyp in generated:
            self.kernel.add(hyp.hypothesis_id, hyp.statement, tuple(hyp.parent_version_ids))
            hypotheses_map[hyp.hypothesis_id] = hyp
            self._sync_hyp_from_kernel(hyp)

        # ── Step 2 & 3: Screening, Grounding, and Adversarial Reflection ───────
        reviewed_hyps: List[YangMillsHypothesis] = []
        for hyp in generated:
            if self._screen_ground_reflect_to_reviewed(hyp, reflection_reports):
                reviewed_hyps.append(hyp)

        # ── Step 4: Proximity Deduplication & Tournament Eligibility ──────────
        clusters, duplicate_rejects = self.proximity.cluster_and_deduplicate(reviewed_hyps)
        eligible_hyps: List[YangMillsHypothesis] = []
        for hyp in reviewed_hyps:
            if hyp.hypothesis_id in duplicate_rejects:
                self.kernel.quarantine(
                    hyp.hypothesis_id,
                    "PROXIMITY_DUPLICATE_OR_FAMILY_CAP",
                    caller="policy_service",
                )
                self._sync_hyp_from_kernel(hyp)
                continue

            self.kernel.advance(
                hyp.hypothesis_id,
                Stage.ELIGIBLE,
                GateSignals(
                    goal_safe=True,
                    hypothesis_safe=True,
                    source_verified=True,
                    reflection_completed=True,
                ),
                caller="policy_service",
            )
            self._sync_hyp_from_kernel(hyp)
            eligible_hyps.append(hyp)

        # ── Step 5: Blinded Round-Robin Tournament (Round 1) ──────────────────
        match_counter = 0
        for i in range(len(eligible_hyps)):
            for j in range(i + 1, len(eligible_hyps)):
                match_counter += 1
                ha = eligible_hyps[i]
                hb = eligible_hyps[j]
                m = self.ranker.compare_pair_blinded(f"MATCH-{match_counter:03d}", ha, hb)
                matches.append(m)
                if m.positional_bias_detected:
                    self.kernel.record_match(ha.hypothesis_id, hb.hypothesis_id, "ABSTAIN", caller="tournament_service")
                elif m.tie or m.winner_id is None:
                    self.kernel.record_match(ha.hypothesis_id, hb.hypothesis_id, "TIE", caller="tournament_service")
                else:
                    loser_id = hb.hypothesis_id if m.winner_id == ha.hypothesis_id else ha.hypothesis_id
                    self.kernel.record_match(m.winner_id, loser_id, "LEFT", caller="tournament_service")
                self._sync_hyp_from_kernel(ha)
                self._sync_hyp_from_kernel(hb)

        # ── Step 6: Evolution & Child Verification Pipeline ───────────────────
        ranked_r1 = sorted(eligible_hyps, key=lambda h: h.elo, reverse=True)
        if len(ranked_r1) >= 2:
            p1, p2 = ranked_r1[0], ranked_r1[1]
            child_id = f"{p1.hypothesis_id}-HYBRID"
            child_hyp, lineage = self.evolver.evolve_hybrid(p1, p2, new_id=child_id, run_id=run_id)
            lineages.append(lineage)
            # Register child via kernel.evolve (invariant: child starts fresh in DRAFT at 1200.0 Elo)
            self.kernel.evolve(p1.hypothesis_id, child_hyp.hypothesis_id, child_hyp.statement)
            hypotheses_map[child_hyp.hypothesis_id] = child_hyp
            self._sync_hyp_from_kernel(child_hyp)

            if self._screen_ground_reflect_to_reviewed(child_hyp, reflection_reports):
                self.kernel.advance(
                    child_hyp.hypothesis_id,
                    Stage.ELIGIBLE,
                    GateSignals(
                        goal_safe=True,
                        hypothesis_safe=True,
                        source_verified=True,
                        reflection_completed=True,
                    ),
                    caller="policy_service",
                )
                self._sync_hyp_from_kernel(child_hyp)
                eligible_hyps.append(child_hyp)

                # Tournament matches against top-2 parents while both remain ELIGIBLE
                for parent in (p1, p2):
                    match_counter += 1
                    m = self.ranker.compare_pair_blinded(f"MATCH-{match_counter:03d}", child_hyp, parent)
                    matches.append(m)
                    if m.positional_bias_detected:
                        self.kernel.record_match(child_hyp.hypothesis_id, parent.hypothesis_id, "ABSTAIN", caller="tournament_service")
                    elif m.tie or m.winner_id is None:
                        self.kernel.record_match(child_hyp.hypothesis_id, parent.hypothesis_id, "TIE", caller="tournament_service")
                    else:
                        loser_id = parent.hypothesis_id if m.winner_id == child_hyp.hypothesis_id else child_hyp.hypothesis_id
                        self.kernel.record_match(m.winner_id, loser_id, "LEFT", caller="tournament_service")
                    self._sync_hyp_from_kernel(child_hyp)
                    self._sync_hyp_from_kernel(parent)

        # ── Step 7: Advance ELIGIBLE -> RANKED -> PROPOSAL_READY ──────────────
        proposal_ready_hyps: List[YangMillsHypothesis] = []
        for hyp in eligible_hyps:
            self.kernel.advance(
                hyp.hypothesis_id,
                Stage.RANKED,
                GateSignals(
                    goal_safe=True,
                    hypothesis_safe=True,
                    source_verified=True,
                    reflection_completed=True,
                    tournament_assessed=True,
                ),
                caller="policy_service",
            )
            self.kernel.advance(
                hyp.hypothesis_id,
                Stage.PROPOSAL_READY,
                GateSignals(
                    goal_safe=True,
                    hypothesis_safe=True,
                    source_verified=True,
                    reflection_completed=True,
                    tournament_assessed=True,
                    report_discloses_limits=True,
                ),
                caller="policy_service",
            )
            self._sync_hyp_from_kernel(hyp)
            proposal_ready_hyps.append(hyp)

        # ── Step 8: Independent External Verification Bridge ──────────────────
        # Order by Elo descending and verify each proposal against independent checks.
        proposal_ready_hyps.sort(key=lambda h: h.elo, reverse=True)
        for hyp in proposal_ready_hyps:
            receipt, vrep = self.verifier.build_verification_receipt(
                hyp,
                builder_identity=self.builder_identity,
                enable_lean=enable_lean,
                require_lean=require_lean_for_proof,
            )
            verification_reports[hyp.hypothesis_id] = vrep
            if receipt is not None:
                self.kernel.verify_claim(receipt, caller="independent_verification_service")
                verified_receipts[hyp.hypothesis_id] = receipt
                self._sync_hyp_from_kernel(hyp)

        # ── Step 9: Meta-Review Synthesis ─────────────────────────────────────
        all_hyps = list(hypotheses_map.values())
        meta_report: MetaReviewReport = self.meta_reviewer.synthesize(
            run_id=run_id,
            goal_id=active_goal.goal_id,
            hypotheses=all_hyps,
            reflection_reports=reflection_reports,
            verified_ids=list(verified_receipts.keys()),
        )

        return {
            "goal": active_goal,
            "hypotheses": hypotheses_map,
            "reflection_reports": reflection_reports,
            "clusters": clusters,
            "duplicate_rejects": duplicate_rejects,
            "matches": matches,
            "lineages": lineages,
            "verification_reports": verification_reports,
            "verified_receipts": verified_receipts,
            "meta_report": meta_report,
            "audit_log": list(self.kernel.audit),
            "clay_problem": "OPEN_AND_UNSOLVED",
        }
