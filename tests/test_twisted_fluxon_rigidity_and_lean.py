"""
Verification Suite for Quaternion Twist-Eater Rigidity & Sector Contraction (YM-103)
=====================================================================================
Tests:
1. Exact rational quaternion multiplication, anti-commutator, and adjoint centralizer kernel.
2. Exact discrete fluxon adjoint Hessian matrix diag(4, 4, 8) and spectral gap lambda = 4.
3. Twisted sector all-orders polymer weight < 1 and residual margin > 1/141.
4. Hard epistemic barrier in verifier_bridge: periodic_twist_decoupling_closed = False
   blocks unauthorized closure of asymptotic edges (E-CROSSOVER, E-THERMO, E-LATTICE-CONT).
5. Zero-jargon, zero-sorry, zero-axiom, and line-length audit of standalone
   module MathlibPR_QuaternionTwistRigidity.lean.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import re
import unittest

from src.ymmg.coscientist import (
    CoScientistVerifierBridge,
    YMGenerationAgent,
    YangMillsCoScientistOrchestrator,
)
from src.ymmg.twisted_fluxon_rigidity import (
    TWIST_P,
    TWIST_Q,
    compute_adjoint_kernel_dimension,
    evaluate_twisted_fluxon_sector_certificate,
    fluxon_spectral_gap,
    quat,
    quat_add,
    quat_commutator,
    quat_mul,
    quat_norm_sq,
    su2_adjoint_action,
    su2_adjoint_commutator_matrix,
    su2_adjoint_hessian_matrix,
)

ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_DIR = ROOT / "formal" / "yang_mills_blueprint" / "YangMillsBlueprint"


class TwistedFluxonRigidityAndLeanTests(unittest.TestCase):
    def test_01_quaternion_algebra_and_twist_eater_centralizer(self):
        # 1. P^2 = Q^2 = -1
        p2 = quat_mul(TWIST_P, TWIST_P)
        q2 = quat_mul(TWIST_Q, TWIST_Q)
        self.assertEqual(p2, quat(-1, 0, 0, 0))
        self.assertEqual(q2, quat(-1, 0, 0, 0))

        # 2. PQ + QP = 0 (orthogonal anticommutation, z_12 = -1)
        pq = quat_mul(TWIST_P, TWIST_Q)
        qp = quat_mul(TWIST_Q, TWIST_P)
        self.assertEqual(pq, quat(0, 0, 0, 1))
        self.assertEqual(qp, quat(0, 0, 0, -1))
        anticomm = quat_add(pq, qp)
        self.assertEqual(anticomm, quat(0, 0, 0, 0))

        # 3. Adjoint action on su(2) basis
        ad_p_e1 = su2_adjoint_action(TWIST_P, (F(1), F(0), F(0)))
        ad_p_e2 = su2_adjoint_action(TWIST_P, (F(0), F(1), F(0)))
        ad_p_e3 = su2_adjoint_action(TWIST_P, (F(0), F(0), F(1)))
        self.assertEqual(ad_p_e1, (F(0), F(0), F(0)))
        self.assertEqual(ad_p_e2, (F(0), F(0), F(2)))
        self.assertEqual(ad_p_e3, (F(0), F(-2), F(0)))

        ad_q_e1 = su2_adjoint_action(TWIST_Q, (F(1), F(0), F(0)))
        ad_q_e2 = su2_adjoint_action(TWIST_Q, (F(0), F(1), F(0)))
        ad_q_e3 = su2_adjoint_action(TWIST_Q, (F(0), F(0), F(1)))
        self.assertEqual(ad_q_e1, (F(0), F(0), F(-2)))
        self.assertEqual(ad_q_e2, (F(0), F(0), F(0)))
        self.assertEqual(ad_q_e3, (F(2), F(0), F(0)))

        # 4. Trivial kernel on su(2): twisted_toron_zero_mode_dim == 0
        ker_dim = compute_adjoint_kernel_dimension()
        self.assertEqual(ker_dim, 0)

    def test_02_fluxon_adjoint_hessian_and_spectral_gap(self):
        h = su2_adjoint_hessian_matrix()
        expected_h = [
            [F(4, 1), F(0, 1), F(0, 1)],
            [F(0, 1), F(4, 1), F(0, 1)],
            [F(0, 1), F(0, 1), F(8, 1)],
        ]
        self.assertEqual(h, expected_h)

        gap = fluxon_spectral_gap()
        self.assertEqual(gap, F(4, 1))

        # Verify quadratic form lower bound for arbitrary rational vectors
        test_vectors = [
            (F(1), F(0), F(0)),
            (F(0), F(1), F(0)),
            (F(0), F(0), F(1)),
            (F(3), F(-2), F(5)),
            (F(-7, 3), F(4, 5), F(1, 2)),
        ]
        for b, c, d in test_vectors:
            x_norm_sq = b * b + c * c + d * d
            x_su2 = (b, c, d)
            ad_p = su2_adjoint_action(TWIST_P, x_su2)
            ad_q = su2_adjoint_action(TWIST_Q, x_su2)
            norm_ad = (
                ad_p[0] ** 2 + ad_p[1] ** 2 + ad_p[2] ** 2
                + ad_q[0] ** 2 + ad_q[1] ** 2 + ad_q[2] ** 2
            )
            # Must satisfy norm_ad >= 4 * x_norm_sq
            self.assertGreaterEqual(norm_ad, F(4, 1) * x_norm_sq)

    def test_03_twisted_fluxon_sector_certificate(self):
        cert = evaluate_twisted_fluxon_sector_certificate()
        self.assertTrue(cert.is_certified)
        self.assertEqual(cert.twisted_toron_zero_mode_dim, 0)
        self.assertEqual(cert.periodic_toron_zero_mode_dim, 3)
        self.assertEqual(cert.fluxon_spectral_gap, F(4, 1))

        # Total twisted-sector IR weight < 1
        self.assertLess(cert.w_ir_twisted_total, F(1, 1))

        # Remaining twisted-sector safety margin > 1/141
        self.assertGreater(cert.delta_twisted_residual_margin, F(1, 141))

        # Epistemic separation
        self.assertTrue(cert.twisted_sector_contractive_uniform_in_L)
        self.assertFalse(cert.periodic_twist_decoupling_closed)
        self.assertEqual(cert.verification_scope, "TWISTED_SECTOR_CLOSED_PERIODIC_DECOUPLING_OPEN")
        self.assertEqual(cert.barrier_id, "NEG-YM-103")

    def test_04_verifier_bridge_blocks_asymptotic_closure_when_twist_decoupling_open(self):
        bridge = CoScientistVerifierBridge(root_dir=ROOT)
        gen = YMGenerationAgent()
        goal = YangMillsCoScientistOrchestrator.default_goal()
        cand = gen.generate_candidates(goal, run_id="RUN-TWIST-TEST", include_adversarial_flawed=False)[0]

        rep_valid = bridge.evaluate_candidate(cand, enable_lean=False, require_lean=False)
        self.assertTrue(rep_valid.passed)
        self.assertTrue(rep_valid.details["twisted_fluxon_rigidity_ok"])
        self.assertTrue(rep_valid.details["twisted_fluxon_rigidity_details"]["twisted_sector_contractive_uniform_in_L"])
        self.assertFalse(rep_valid.details["twisted_fluxon_rigidity_details"]["periodic_twist_decoupling_closed"])

        # Attempting to claim closure of E-CROSSOVER, E-THERMO, or E-LATTICE-CONT fails
        for edge in ("E-CROSSOVER", "E-THERMO", "E-LATTICE-CONT"):
            asymp_cand = gen.generate_candidates(goal, run_id="RUN-TWIST-ASYMP", include_adversarial_flawed=False)[0]
            asymp_cand.goal_id = edge
            rep_asymp = bridge.evaluate_candidate(asymp_cand, enable_lean=False, require_lean=False)
            self.assertFalse(rep_asymp.passed)
            self.assertTrue(any("ASYMPTOTIC_EDGE_UNAUTHORIZED_FROM_FINITE_AUDIT" in f for f in rep_asymp.failures))

    def test_05_mathlib_pr_quaternion_twist_rigidity_hygiene_audit(self):
        FORBIDDEN_JARGON = [
            "Clay",
            "CMI",
            "Millennium",
            "YM-101",
            "YM-102",
            "YM-103",
            "NEG-YM",
            "Chrysalis",
            "Dark Factory",
            "Toron",
            "Weitzenböck",
            "Weitzenbock",
            "Luscher",
            "Lüscher",
            "Hooft",
        ]

        pf = BLUEPRINT_DIR / "MathlibPR_QuaternionTwistRigidity.lean"
        self.assertTrue(pf.is_file(), f"Expected file {pf.name} to exist")
        text = pf.read_text(encoding="utf-8")
        lines = text.splitlines()

        # 1. 0 lines > 100 characters
        long_lines = [(i + 1, len(l), l) for i, l in enumerate(lines) if len(l) > 100]
        self.assertEqual(len(long_lines), 0, f"Found lines > 100 chars in {pf.name}: {long_lines}")

        # 2. 0 internal project imports
        imports = [l for l in lines if l.strip().startswith("import")]
        self.assertEqual(len(imports), 0, f"Found forbidden imports in {pf.name}: {imports}")

        # 3. 0 sorry, 0 custom axioms, 0 commands
        stripped = re.sub(r"/-.*?-/", "", text, flags=re.DOTALL)
        stripped = re.sub(r"--[^\n]*", "", stripped)

        sorry_hits = re.findall(r"\bsorry\b", stripped)
        self.assertEqual(len(sorry_hits), 0, f"Found sorry in {pf.name}")

        axiom_hits = re.findall(r"(?m)^\s*axiom\s+", stripped)
        self.assertEqual(len(axiom_hits), 0, f"Found axiom declaration in {pf.name}")

        cmd_hits = re.findall(r"(?m)^\s*#(check|print|eval)\b", stripped)
        self.assertEqual(len(cmd_hits), 0, f"Found diagnostic commands in {pf.name}: {cmd_hits}")

        # 4. 0 forbidden jargon tokens
        for word in FORBIDDEN_JARGON:
            self.assertNotIn(word.lower(), text.lower(), f"Forbidden jargon token '{word}' in {pf.name}")

    def test_06_prior_art_audit_and_universal_audit_and_traps_and_author_block(self):
        import json

        # 1. prior_art_audit_receipt.json exists and is valid
        receipt_file = ROOT / "prior_art_audit_receipt.json"
        self.assertTrue(receipt_file.is_file(), "prior_art_audit_receipt.json must exist")
        receipt_data = json.loads(receipt_file.read_text(encoding="utf-8"))
        self.assertIn("targets", receipt_data)
        self.assertEqual(len(receipt_data["targets"]), 6)
        total_code = sum(t["total_code_hits"] for t in receipt_data["targets"])
        total_pr = sum(t["total_pr_hits"] for t in receipt_data["targets"])
        self.assertGreater(total_code, 0, "Expected non-zero code hits across scan")
        self.assertGreater(total_pr, 0, "Expected non-zero PR hits across scan")

        # 2. docs/UNIVERSAL_SOLVED_VS_UNSOLVED_AUDIT.md exists and contains all 4 buckets
        audit_doc = ROOT / "docs" / "UNIVERSAL_SOLVED_VS_UNSOLVED_AUDIT.md"
        self.assertTrue(audit_doc.is_file(), "docs/UNIVERSAL_SOLVED_VS_UNSOLVED_AUDIT.md must exist")
        doc_text = audit_doc.read_text(encoding="utf-8")
        self.assertIn("Bucket 1", doc_text)
        self.assertIn("Bucket 2", doc_text)
        self.assertIn("Bucket 3", doc_text)
        self.assertIn("Bucket 4", doc_text)
        self.assertIn("OPEN_AND_UNSOLVED", doc_text)

        # 3. VerifyNoTraps.lean exists, has 0 sorry/axioms, and is imported in YangMillsBlueprint.lean
        vnt_file = BLUEPRINT_DIR / "VerifyNoTraps.lean"
        self.assertTrue(vnt_file.is_file(), "VerifyNoTraps.lean must exist")
        vnt_text = vnt_file.read_text(encoding="utf-8")
        stripped_vnt = re.sub(r"/-.*?-/", "", vnt_text, flags=re.DOTALL)
        stripped_vnt = re.sub(r"--[^\n]*", "", stripped_vnt)
        self.assertEqual(len(re.findall(r"\bsorry\b", stripped_vnt)), 0, "Found sorry in VerifyNoTraps.lean")
        self.assertEqual(len(re.findall(r"(?m)^\s*axiom\s+", stripped_vnt)), 0, "Found axiom in VerifyNoTraps.lean")

        root_blueprint = BLUEPRINT_DIR.parent / "YangMillsBlueprint.lean"
        self.assertTrue(root_blueprint.is_file(), "YangMillsBlueprint.lean must exist")
        root_text = root_blueprint.read_text(encoding="utf-8")
        self.assertIn("import YangMillsBlueprint.VerifyNoTraps", root_text)
        self.assertIn("import YangMillsBlueprint.CheckAllDecls", root_text)

        # 4. paper/main.tex author block check
        paper_file = ROOT / "paper" / "main.tex"
        self.assertTrue(paper_file.is_file(), "paper/main.tex must exist")
        paper_text = paper_file.read_text(encoding="utf-8")
        self.assertIn("Qamar Munawer", paper_text)
        self.assertIn("Brandenburg University of Technology Cottbus--Senftenberg", paper_text)
        self.assertNotIn("Department", paper_text)
        self.assertNotIn("Faculty", paper_text)


if __name__ == "__main__":
    unittest.main()
