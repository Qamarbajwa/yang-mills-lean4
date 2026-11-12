"""
Verification Suite for Research Co-Scientist OS (Dark Factory Spec v0.1 + Yang-Mills Adapter)
=============================================================================================
Covers:
1. All 27 Reference Gate Kernel no-bypass invariants (CS-T001 .. CS-T036).
2. Adversarial checks on Yang-Mills Generation, Reflection (NEG-YM-101), Proximity (CS-T035),
   Blinded Ranking bias detection (CS-T011), and Evolution state/Elo reset (CS-T006).
3. Verifier Bridge checks (Exact Fractions + Dream-RSI Replay + Chrysalis Gate 2 + Live Lean 4.35).
4. Full end-to-end YangMillsCoScientistOrchestrator discovery cycle test.
"""

from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import unittest

from src.ymmg.coscientist import (
    Citation,
    CoScientistVerifierBridge,
    Denied,
    GateSignals,
    ResearchGateKernel,
    ResearchGoal,
    Stage,
    VerificationReceipt,
    YMEvolutionAgent,
    YMGenerationAgent,
    YMProximityAgent,
    YMRankingAgent,
    YMReflectionAgent,
    YangMillsCoScientistOrchestrator,
    YangMillsHypothesis,
    digest,
)

ROOT = Path(__file__).resolve().parents[1]
GOOD = GateSignals(True, True, True, True, True, True)


# ==============================================================================
# Part 1: 27 Reference Kernel No-Bypass Tests (Ported from COSCIENTIST_DF_v0_1)
# ==============================================================================


class ResearchGateKernelTests(unittest.TestCase):
    def setUp(self):
        self.k = ResearchGateKernel()
        self.k.add("A", "If x, then y under bounded assumptions")

    def advance_to(self, item_id: str, target: Stage):
        for state in (
            Stage.SCREENED,
            Stage.GROUNDED,
            Stage.REVIEWED,
            Stage.ELIGIBLE,
            Stage.RANKED,
            Stage.PROPOSAL_READY,
        ):
            if self.k.get(item_id).stage == target:
                return
            self.k.advance(item_id, state, GOOD, caller="policy_service")

    def receipt(self, item: str = "A", **kw) -> VerificationReceipt:
        base = dict(
            hypothesis_id=item,
            exact_target_digest=self.k.get(item).content_digest,
            evidence_digest="a" * 64,
            claim_type="MATH_PROOF",
            builder_identity="builder-x",
            verifier_identity="separate-verifier",
            independently_verified=True,
            protected_suite_passed=True,
            semantic_review_passed=True,
            verifier_authority_bound=True,
        )
        base.update(kw)
        return VerificationReceipt(**base)

    def test_starts_draft_and_unverified(self):
        self.assertEqual(self.k.get("A").stage, Stage.DRAFT)
        self.assertFalse(self.k.proposal_is_verified("A"))

    def test_safe_adjacent_move(self):
        self.assertEqual(
            self.k.advance("A", Stage.SCREENED, GOOD, caller="policy_service").stage,
            Stage.SCREENED,
        )

    def test_no_agent_state_write(self):
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.SCREENED, GOOD, caller="generation_agent")

    def test_no_skip_to_ranked(self):
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.RANKED, GOOD, caller="policy_service")

    def test_no_missing_safety(self):
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.SCREENED, GateSignals(), caller="policy_service")

    def test_missing_source(self):
        self.k.advance("A", Stage.SCREENED, GOOD, caller="policy_service")
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.GROUNDED, GateSignals(True, True), caller="policy_service")

    def test_missing_reflection(self):
        self.advance_to("A", Stage.GROUNDED)
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.REVIEWED, GateSignals(True, True, True), caller="policy_service")

    def test_missing_tournament(self):
        self.advance_to("A", Stage.ELIGIBLE)
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.RANKED, GateSignals(True, True, True, True), caller="policy_service")

    def test_report_disclosure_required(self):
        self.advance_to("A", Stage.RANKED)
        with self.assertRaises(Denied):
            self.k.advance(
                "A",
                Stage.PROPOSAL_READY,
                GateSignals(True, True, True, True, True),
                caller="policy_service",
            )

    def test_ranked_is_not_verified(self):
        self.advance_to("A", Stage.PROPOSAL_READY)
        self.assertFalse(self.k.proposal_is_verified("A"))
        self.assertEqual(self.k.get("A").formal_state, "UNTESTED")

    def test_no_backwards(self):
        self.advance_to("A", Stage.REVIEWED)
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.GROUNDED, GOOD, caller="policy_service")

    def test_evolution_resets_state_and_elo(self):
        self.advance_to("A", Stage.RANKED)
        self.k.evolve("A", "C", "A completely revised question")
        self.assertEqual(self.k.get("C").stage, Stage.DRAFT)
        self.assertEqual(self.k.get("C").elo, 1200.0)
        self.assertFalse(self.k.proposal_is_verified("C"))
        self.assertEqual(self.k.get("C").parent_ids, ("A",))

    def test_no_self_verification(self):
        self.advance_to("A", Stage.SCREENED)
        with self.assertRaises(Denied):
            self.k.verify_claim(
                self.receipt(verifier_identity="builder-x"),
                caller="independent_verification_service",
            )

    def test_exact_target_digest(self):
        self.advance_to("A", Stage.SCREENED)
        with self.assertRaises(Denied):
            self.k.verify_claim(
                self.receipt(exact_target_digest=digest("wrong")),
                caller="independent_verification_service",
            )

    def test_protected_test_required(self):
        self.advance_to("A", Stage.SCREENED)
        with self.assertRaises(Denied):
            self.k.verify_claim(
                self.receipt(protected_suite_passed=False),
                caller="independent_verification_service",
            )

    def test_bound_verifier_required(self):
        self.advance_to("A", Stage.SCREENED)
        with self.assertRaises(Denied):
            self.k.verify_claim(
                self.receipt(verifier_authority_bound=False),
                caller="independent_verification_service",
            )

    def test_semantic_review_required(self):
        self.advance_to("A", Stage.SCREENED)
        with self.assertRaises(Denied):
            self.k.verify_claim(
                self.receipt(semantic_review_passed=False),
                caller="independent_verification_service",
            )

    def test_wrong_role_denied(self):
        self.advance_to("A", Stage.SCREENED)
        with self.assertRaises(Denied):
            self.k.verify_claim(self.receipt(), caller="generation_agent")

    def test_mock_verification_distinct_from_rank(self):
        self.advance_to("A", Stage.SCREENED)
        self.k.verify_claim(self.receipt(), caller="independent_verification_service")
        self.assertTrue(self.k.proposal_is_verified("A"))
        self.assertEqual(self.k.get("A").stage, Stage.SCREENED)

    def test_quarantine_revokes(self):
        self.advance_to("A", Stage.SCREENED)
        self.k.verify_claim(self.receipt(), caller="independent_verification_service")
        self.k.quarantine("A", caller="policy_service")
        self.assertFalse(self.k.proposal_is_verified("A"))
        with self.assertRaises(Denied):
            self.k.verify_claim(self.receipt(), caller="independent_verification_service")

    def test_elo_match_requires_eligible(self):
        self.k.add("B", "Another research statement")
        with self.assertRaises(Denied):
            self.k.record_match("A", "B", "LEFT", caller="tournament_service")

    def test_elo_update_not_claim_verification(self):
        self.k.add("B", "Another research statement")
        self.advance_to("A", Stage.ELIGIBLE)
        self.advance_to("B", Stage.ELIGIBLE)
        a, b = self.k.record_match("A", "B", "LEFT", caller="tournament_service")
        self.assertEqual((a, b), (1216.0, 1184.0))
        self.assertFalse(self.k.proposal_is_verified("A"))

    def test_abstain_does_not_change_scores(self):
        self.k.add("B", "Another research statement")
        self.advance_to("A", Stage.ELIGIBLE)
        self.advance_to("B", Stage.ELIGIBLE)
        self.assertEqual(
            self.k.record_match("A", "B", "ABSTAIN", caller="tournament_service"),
            (1200.0, 1200.0),
        )

    def test_invalid_lineage(self):
        with self.assertRaises(Denied):
            self.k.add("B", "Child hypothesis", ("missing",))

    def test_duplicate_candidate_blocked(self):
        with self.assertRaises(Denied):
            self.k.add("A", "Different statement")

    def test_verification_blocked_before_safety_screen(self):
        with self.assertRaises(Denied):
            self.k.verify_claim(self.receipt(), caller="independent_verification_service")

    def test_quarantine_no_bypass(self):
        self.k.quarantine("A", caller="policy_service")
        with self.assertRaises(Denied):
            self.k.advance("A", Stage.SCREENED, GOOD, caller="policy_service")


# ==============================================================================
# Part 2: Yang-Mills Co-Scientist Discovery Roles & Verifier Bridge Tests
# ==============================================================================


class YangMillsCoScientistComponentTests(unittest.TestCase):
    def setUp(self):
        self.goal = YangMillsCoScientistOrchestrator.default_goal()
        self.gen = YMGenerationAgent()
        self.reflector = YMReflectionAgent(register_path=ROOT / "NEGATIVE_EVIDENCE_REGISTER.md")
        self.proximity = YMProximityAgent()
        self.ranker = YMRankingAgent()
        self.evolver = YMEvolutionAgent()
        self.bridge = CoScientistVerifierBridge(root_dir=ROOT)

    def test_reflection_quarantines_neg_ym_101_violation(self):
        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=True)
        flawed = [h for h in cands if h.hypothesis_id == "HYP-YM-NAIVE-PERTURB-FAIL"][0]
        rep = self.reflector.reflect(flawed)
        self.assertFalse(rep.passed)
        self.assertIn("NEG-YM-101", rep.matched_obstructions)
        self.assertFalse(rep.citation_grounding_ok)
        self.assertEqual(rep.recommended_stage, Stage.QUARANTINED)

    def test_reflection_accepts_twisted_holonomy_candidate(self):
        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=False)
        twist = [h for h in cands if h.hypothesis_id == "HYP-YM-TWIST-HOLONOMY-v1"][0]
        rep = self.reflector.reflect(twist)
        self.assertTrue(rep.passed)
        self.assertEqual(rep.matched_obstructions, [])
        self.assertEqual(rep.recommended_stage, Stage.REVIEWED)

    def test_proximity_suppresses_duplicates_and_overflow(self):
        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=False)
        dup = YangMillsHypothesis(
            hypothesis_id="HYP-DUP",
            version_id="v1",
            goal_id=self.goal.goal_id,
            run_id="TEST-RUN",
            title="Duplicate",
            statement=cands[0].statement,
            mechanism_family=cands[0].mechanism_family,
            assumptions=cands[0].assumptions,
            falsifiers=cands[0].falsifiers,
            predictions=cands[0].predictions,
        )
        clusters, rejected = self.proximity.cluster_and_deduplicate([cands[0], dup, cands[1]], max_per_family=2)
        self.assertIn("HYP-DUP", rejected)
        self.assertEqual(len(clusters[cands[0].mechanism_family]), 1)

    def test_blinded_ranking_detects_positional_bias(self):
        class BiasedRankingAgent(YMRankingAgent):
            # Intentionally breaks symmetry: always favors first argument regardless of reversal
            def _judge_order(self, first, second):
                return "A"

        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=False)
        m = BiasedRankingAgent().compare_pair_blinded("M-BIAS", cands[0], cands[2])
        self.assertTrue(m.positional_bias_detected)
        self.assertIsNone(m.winner_id)

        # Standard unbiased agent: cands[0] vs cands[2] has different scores -> decisive winner
        m_decisive = self.ranker.compare_pair_blinded("M-DECISIVE", cands[0], cands[2])
        self.assertFalse(m_decisive.positional_bias_detected)
        self.assertEqual(m_decisive.winner_id, "HYP-YM-TWIST-HOLONOMY-v1")
        self.assertFalse(m_decisive.tie)

        # Standard unbiased agent: cands[0] vs cands[1] has identical scores -> honest tie
        m_tie = self.ranker.compare_pair_blinded("M-TIE", cands[0], cands[1])
        self.assertFalse(m_tie.positional_bias_detected)
        self.assertIsNone(m_tie.winner_id)
        self.assertTrue(m_tie.tie)

    def test_evolution_resets_child_and_tightens_toron_bound(self):
        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=False)
        p1, p2 = cands[0], cands[1]
        p1.elo = 1264.0
        p1.formal_state = "APPROVED_PROOF"
        child, lineage = self.evolver.evolve_hybrid(p1, p2, new_id="HYP-HYBRID-TEST", run_id="TEST-RUN")
        self.assertEqual(child.proposal_state, "DRAFT")
        self.assertEqual(child.formal_state, "UNTESTED")
        self.assertEqual(child.elo, 1200.0)
        self.assertEqual(child.parent_version_ids, [p1.hypothesis_id, p2.hypothesis_id])
        self.assertLess(
            child.rational_parameters["w_toron_vol"],
            min(p1.rational_parameters["w_toron_vol"], p2.rational_parameters["w_toron_vol"]),
        )
        self.assertEqual(lineage.child_id, "HYP-HYBRID-TEST")

    def test_verifier_bridge_rejects_flawed_and_self_verification(self):
        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=True)
        flawed = [h for h in cands if h.hypothesis_id == "HYP-YM-NAIVE-PERTURB-FAIL"][0]
        receipt, report = self.bridge.build_verification_receipt(flawed, enable_lean=False, require_lean=False)
        self.assertIsNone(receipt)
        self.assertFalse(report.passed)
        self.assertFalse(report.rational_ok)
        self.assertFalse(report.dream_rsi_ok)

        # Same identity between builder and verifier is denied
        twist = [h for h in cands if h.hypothesis_id == "HYP-YM-TWIST-HOLONOMY-v1"][0]
        receipt_self, _ = self.bridge.build_verification_receipt(
            twist,
            builder_identity=self.bridge.verifier_identity,
            enable_lean=False,
            require_lean=False,
        )
        self.assertIsNone(receipt_self)

    def test_verifier_bridge_live_lean_4_35_twisted_holonomy(self):
        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=False)
        twist = [h for h in cands if h.hypothesis_id == "HYP-YM-TWIST-HOLONOMY-v1"][0]
        receipt, report = self.bridge.build_verification_receipt(
            twist,
            builder_identity="ym-coscientist-builder",
            enable_lean=True,
            require_lean=True,
        )
        self.assertTrue(report.rational_ok)
        self.assertTrue(report.dream_rsi_ok)
        self.assertTrue(report.chrysalis_gates_ok)
        self.assertTrue(report.lean_ok, f"Expected live Lean verification pass, got: {report.details}")
        self.assertEqual(report.lean_status, "LOCAL_LEAN_STEP_CHECK_PASS_PENDING_INDEPENDENT_RECHECK")
        self.assertIsNotNone(receipt)
        self.assertEqual(len(receipt.evidence_digest), 64)

    def test_schema_serialization_keys(self):
        cands = self.gen.generate_candidates(self.goal, run_id="TEST-RUN", include_adversarial_flawed=False)
        d = cands[0].to_schema_dict()
        for key in (
            "hypothesis_id",
            "version_id",
            "goal_id",
            "run_id",
            "statement",
            "content_digest",
            "assumptions",
            "falsifiers",
            "predictions",
            "citations",
            "proposal_state",
            "formal_state",
        ):
            self.assertIn(key, d)


# ==============================================================================
# Part 3: Full End-to-End Discovery Orchestrator Tests
# ==============================================================================


class YangMillsOrchestratorE2ETests(unittest.TestCase):
    def test_full_discovery_cycle_with_live_lean_and_epistemic_honesty(self):
        orch = YangMillsCoScientistOrchestrator(root_dir=ROOT)
        res = orch.run_discovery_cycle(enable_lean=True, require_lean_for_proof=True)

        hyps = res["hypotheses"]
        meta = res["meta_report"]
        receipts = res["verified_receipts"]

        # 1. Adversarial control must be QUARANTINED and NOT verified
        self.assertEqual(hyps["HYP-YM-NAIVE-PERTURB-FAIL"].proposal_state, "QUARANTINED")
        self.assertFalse(orch.kernel.proposal_is_verified("HYP-YM-NAIVE-PERTURB-FAIL"))
        self.assertIn("HYP-YM-NAIVE-PERTURB-FAIL", meta.quarantined_ids)

        # 2. Evolved hybrid child must exist and outrank or tie at top with Lean verification
        self.assertGreaterEqual(len(res["lineages"]), 1)
        child_id = res["lineages"][0].child_id
        self.assertIn(child_id, hyps)
        self.assertTrue(orch.kernel.proposal_is_verified(child_id))
        self.assertEqual(hyps[child_id].formal_state, "APPROVED_PROOF")

        # 3. Hypotheses without Lean proofs (RESURGENCE / GRIBOV_HORIZON) remain UNTESTED despite PROPOSAL_READY
        self.assertEqual(hyps["HYP-YM-RESURGENT-BION-v1"].proposal_state, "PROPOSAL_READY")
        self.assertEqual(hyps["HYP-YM-RESURGENT-BION-v1"].formal_state, "UNTESTED")
        self.assertNotIn("HYP-YM-RESURGENT-BION-v1", receipts)

        # 4. Strict epistemic guard: Clay Millennium Problem remains OPEN_AND_UNSOLVED
        self.assertEqual(res["clay_problem"], "OPEN_AND_UNSOLVED")
        self.assertEqual(meta.epistemic_status, "OPEN_AND_UNSOLVED")
        self.assertIn("OPEN_AND_UNSOLVED", meta.summary)


if __name__ == "__main__":
    unittest.main()
