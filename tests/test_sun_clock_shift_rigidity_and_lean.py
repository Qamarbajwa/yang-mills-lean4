"""
Verification Suite for SU(N) Clock-and-Shift Twist Rigidity & Lean Formalization (YM-104)
========================================================================================
Tests:
1. Exact zero-mode elimination and flat Cartan toron moduli dimensions for SU(N).
2. Exact rational discrete adjoint Laplacian spectral gaps for N in {2, 3, 4, 6, 26}.
3. SU(2) and SU(3) twisted-sector local block contraction and large-N decay barrier (NEG-YM-104).
4. CoScientist verifier bridge audits and strict blocking of unauthorized E-GROUP-GEN closure.
5. Zero-jargon, zero-sorry, zero-axiom, and line-length audit of standalone
   module MathlibPR_ClockShiftRigidity.lean.
6. Blueprint wiring across YangMillsBlueprint.lean, VerifyNoTraps.lean, and CheckAllDecls.lean.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import re
import unittest

from src.ymmg.block_weyl_collar_bound import DELTA_ALL_ORDERS_MARGIN
from src.ymmg.coscientist import (
    CoScientistVerifierBridge,
    YMGenerationAgent,
    YangMillsCoScientistOrchestrator,
    YangMillsHypothesis,
)
from src.ymmg.sun_clock_shift_rigidity import (
    evaluate_sun_clock_shift_certificate,
    exact_rational_spectral_gap_lower_bound,
    jordan_spectral_gap_lower_bound,
    periodic_cartan_zero_mode_dim,
    secant_asymptotic_spectral_gap_lower_bound,
    twisted_clock_shift_zero_mode_dim,
    universal_jordan_spectral_gap_lower_bound,
)

ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_DIR = ROOT / "formal" / "yang_mills_blueprint" / "YangMillsBlueprint"


class SUNClockShiftRigidityAndLeanTests(unittest.TestCase):
    def test_01_sun_cartan_and_twisted_zero_mode_dims(self):
        # 1. Periodic Cartan toron zero-mode dimensions: 3 * (N - 1)
        expected_periodic = {2: 3, 3: 6, 4: 9, 6: 15, 26: 75}
        for n, expected_dim in expected_periodic.items():
            self.assertEqual(periodic_cartan_zero_mode_dim(n), expected_dim)

        # 2. Twisted clock-and-shift zero-mode dimensions: 0 for all N >= 2
        for n in (2, 3, 4, 6, 26):
            self.assertEqual(twisted_clock_shift_zero_mode_dim(n), 0)

    def test_02_exact_rational_spectral_gap_bounds(self):
        import math

        # 1. Exact table gaps for low N
        self.assertEqual(exact_rational_spectral_gap_lower_bound(2), F(4, 1))
        self.assertEqual(exact_rational_spectral_gap_lower_bound(3), F(3, 1))
        self.assertEqual(exact_rational_spectral_gap_lower_bound(4), F(2, 1))
        self.assertEqual(exact_rational_spectral_gap_lower_bound(5), F(199, 144))
        self.assertEqual(exact_rational_spectral_gap_lower_bound(6), F(1, 1))

        # 2. Strict rational Archimedean bound for SU(5)
        # 161^2 = 25921 > 25920 = 5 * 72^2 => sqrt(5) < 161/72
        # (5 - sqrt(5))/2 > (5 - 161/72)/2 = 199/144
        su5_exact = 4 * (math.sin(math.pi / 5) ** 2)
        self.assertLess(float(F(199, 144)), su5_exact)

        # 3. Asymptotic secant lower bound for N >= 6 (valid on (0, pi/6])
        self.assertEqual(secant_asymptotic_spectral_gap_lower_bound(6), F(1, 1))
        self.assertEqual(secant_asymptotic_spectral_gap_lower_bound(26), F(9, 169))
        self.assertEqual(exact_rational_spectral_gap_lower_bound(26), F(9, 169))
        with self.assertRaises(ValueError):
            secant_asymptotic_spectral_gap_lower_bound(5)

        # 4. Universal Jordan lower bound 16 / N^2 for all N >= 2 on (0, pi/2]
        self.assertEqual(universal_jordan_spectral_gap_lower_bound(2), F(4, 1))
        self.assertEqual(universal_jordan_spectral_gap_lower_bound(3), F(16, 9))
        self.assertEqual(universal_jordan_spectral_gap_lower_bound(4), F(1, 1))
        self.assertEqual(universal_jordan_spectral_gap_lower_bound(5), F(16, 25))
        self.assertEqual(universal_jordan_spectral_gap_lower_bound(6), F(4, 9))
        self.assertEqual(universal_jordan_spectral_gap_lower_bound(26), F(4, 169))

        # 5. Check exact_rational_gap >= universal_jordan_gap for all test N
        for n in (2, 3, 4, 5, 6, 26):
            self.assertGreaterEqual(
                exact_rational_spectral_gap_lower_bound(n),
                universal_jordan_spectral_gap_lower_bound(n),
            )
            self.assertGreater(exact_rational_spectral_gap_lower_bound(n), F(0, 1))
            self.assertGreater(universal_jordan_spectral_gap_lower_bound(n), F(0, 1))

    def test_03_evaluate_sun_clock_shift_certificate(self):
        # SU(2) certification
        cert2 = evaluate_sun_clock_shift_certificate(2)
        self.assertTrue(cert2.is_certified)
        self.assertEqual(cert2.periodic_cartan_zero_mode_dim, 3)
        self.assertEqual(cert2.twisted_clock_shift_zero_mode_dim, 0)
        self.assertEqual(cert2.spectral_gap_lower_bound, F(4, 1))
        self.assertEqual(cert2.universal_jordan_gap_lower_bound, F(4, 1))
        self.assertTrue(cert2.su2_su3_twisted_gap_sufficient)
        self.assertFalse(cert2.uniform_in_all_compact_simple_G)
        self.assertEqual(cert2.barrier_id, "NEG-YM-104")
        self.assertIn("NEG-YM-104a", cert2.barrier_details)
        self.assertIn("NEG-YM-104b", cert2.barrier_details)

        # SU(3) certification
        cert3 = evaluate_sun_clock_shift_certificate(3)
        self.assertTrue(cert3.is_certified)
        self.assertEqual(cert3.periodic_cartan_zero_mode_dim, 6)
        self.assertEqual(cert3.twisted_clock_shift_zero_mode_dim, 0)
        self.assertEqual(cert3.spectral_gap_lower_bound, F(3, 1))
        self.assertEqual(cert3.universal_jordan_gap_lower_bound, F(16, 9))
        self.assertTrue(cert3.su2_su3_twisted_gap_sufficient)
        self.assertLess(cert3.w_local_block_total, cert3.delta_all_orders_margin)
        self.assertLess(cert3.w_ir_twisted_total, F(1, 1))
        self.assertGreater(cert3.delta_residual_margin, F(1, 250))
        self.assertFalse(cert3.uniform_in_all_compact_simple_G)
        self.assertEqual(cert3.barrier_id, "NEG-YM-104")

        # SU(4), SU(5), SU(6) exceed unscaled fixed-cell margin
        cert4 = evaluate_sun_clock_shift_certificate(4)
        self.assertFalse(cert4.is_certified)
        self.assertIn("NEG-YM-104", str(cert4.failure_reason))

        cert5 = evaluate_sun_clock_shift_certificate(5)
        self.assertFalse(cert5.is_certified)
        self.assertEqual(cert5.spectral_gap_lower_bound, F(199, 144))
        self.assertIn("NEG-YM-104", str(cert5.failure_reason))

        cert6 = evaluate_sun_clock_shift_certificate(6)
        self.assertFalse(cert6.is_certified)
        self.assertIn("NEG-YM-104", str(cert6.failure_reason))

        # SU(26) Large-N barrier audit
        cert26 = evaluate_sun_clock_shift_certificate(26)
        self.assertFalse(cert26.is_certified)
        self.assertEqual(cert26.periodic_cartan_zero_mode_dim, 75)
        self.assertEqual(cert26.twisted_clock_shift_zero_mode_dim, 0)
        self.assertEqual(cert26.spectral_gap_lower_bound, F(9, 169))
        self.assertEqual(cert26.universal_jordan_gap_lower_bound, F(4, 169))
        self.assertFalse(cert26.uniform_in_all_compact_simple_G)
        self.assertEqual(cert26.barrier_id, "NEG-YM-104")
        self.assertIn("NEG-YM-104", str(cert26.failure_reason))

    def test_04_verifier_bridge_blocks_group_gen(self):
        bridge = CoScientistVerifierBridge(root_dir=ROOT)
        gen = YMGenerationAgent()
        goal = YangMillsCoScientistOrchestrator.default_goal()
        cand = gen.generate_candidates(goal, run_id="RUN-SU3-TEST", include_adversarial_flawed=False)[0]

        rep_valid = bridge.evaluate_candidate(cand, enable_lean=False, require_lean=False)
        self.assertTrue(rep_valid.passed)
        self.assertTrue(rep_valid.details["sun_clock_shift_rigidity_ok"])
        self.assertTrue(rep_valid.details["sun_clock_shift_rigidity_details"]["su2_su3_twisted_gap_sufficient"])
        self.assertFalse(rep_valid.details["sun_clock_shift_rigidity_details"]["uniform_in_all_compact_simple_G"])

        # Attempting to claim closure of E-GROUP-GEN is strictly blocked
        group_cand = gen.generate_candidates(goal, run_id="RUN-SU3-GEN", include_adversarial_flawed=False)[0]
        group_cand.goal_id = "E-GROUP-GEN"
        rep_group = bridge.evaluate_candidate(group_cand, enable_lean=False, require_lean=False)
        self.assertFalse(rep_group.passed)
        self.assertTrue(
            any("GROUP_GENERALIZATION_UNAUTHORIZED_FROM_SU2_SU3_AUDIT" in f for f in rep_group.failures),
            f"Expected GROUP_GENERALIZATION_UNAUTHORIZED failure, got: {rep_group.failures}",
        )

    def test_05_mathlib_pr_clock_shift_rigidity_hygiene_audit(self):
        FORBIDDEN_JARGON = [
            "Clay",
            "CMI",
            "Millennium",
            "YM-101",
            "YM-102",
            "YM-103",
            "YM-104",
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

        pf = BLUEPRINT_DIR / "MathlibPR_ClockShiftRigidity.lean"
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

    def test_06_blueprint_wiring_and_lean_verification(self):
        # 1. YangMillsBlueprint.lean wiring
        root_blueprint = BLUEPRINT_DIR.parent / "YangMillsBlueprint.lean"
        self.assertTrue(root_blueprint.is_file())
        root_text = root_blueprint.read_text(encoding="utf-8")
        self.assertIn("import YangMillsBlueprint.MathlibPR_ClockShiftRigidity", root_text)
        self.assertIn("import YangMillsBlueprint.SUNClockShiftRigidity", root_text)

        # 2. VerifyNoTraps.lean wiring
        vnt_file = BLUEPRINT_DIR / "VerifyNoTraps.lean"
        self.assertTrue(vnt_file.is_file())
        vnt_text = vnt_file.read_text(encoding="utf-8")
        self.assertIn("import YangMillsBlueprint.MathlibPR_ClockShiftRigidity", vnt_text)
        self.assertIn("check_mode_pair_norm_sq_unconditional", vnt_text)
        self.assertIn("check_su3_twisted_eigenvalue_table_min_unconditional", vnt_text)
        self.assertIn("check_jordan_spectral_gap_pos_unconditional", vnt_text)
        self.assertIn("check_secant_asymptotic_gap_pos_unconditional", vnt_text)
        self.assertIn("check_secant_asymptotic_gap_six_eval_unconditional", vnt_text)
        self.assertIn("check_su5_rational_gap_witness_unconditional", vnt_text)
        self.assertIn("check_su5_gap_gt_jordan_unconditional", vnt_text)

        # 3. CheckAllDecls.lean wiring
        cad_file = BLUEPRINT_DIR / "CheckAllDecls.lean"
        self.assertTrue(cad_file.is_file())
        cad_text = cad_file.read_text(encoding="utf-8")
        self.assertIn("import YangMillsBlueprint.MathlibPR_ClockShiftRigidity", cad_text)
        self.assertIn("import YangMillsBlueprint.SUNClockShiftRigidity", cad_text)
        self.assertIn("MathlibPR.ClockShiftAlgebra.mode_pair_norm_sq_pos", cad_text)
        self.assertIn("MathlibPR.ClockShiftAlgebra.secant_asymptotic_gap_pos", cad_text)
        self.assertIn("MathlibPR.ClockShiftAlgebra.su5_rational_gap_witness", cad_text)
        self.assertIn("YangMillsBlueprint.SUNClockShiftRigidity.su3_twisted_local_block_contraction", cad_text)

        # 4. SUNClockShiftRigidity.lean has 0 sorry and 0 axioms
        sun_file = BLUEPRINT_DIR / "SUNClockShiftRigidity.lean"
        self.assertTrue(sun_file.is_file())
        sun_text = sun_file.read_text(encoding="utf-8")
        stripped_sun = re.sub(r"/-.*?-/", "", sun_text, flags=re.DOTALL)
        stripped_sun = re.sub(r"--[^\n]*", "", stripped_sun)
        self.assertEqual(len(re.findall(r"\bsorry\b", stripped_sun)), 0)
        self.assertEqual(len(re.findall(r"(?m)^\s*axiom\s+", stripped_sun)), 0)


if __name__ == "__main__":
    unittest.main()
