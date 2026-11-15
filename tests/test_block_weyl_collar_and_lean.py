"""
Verification Suite for Local Block-Poincaré & Weyl Collar-Bulk Bounds (YM-102)
=============================================================================
Tests:
1. Exact rational evaluation of local block-Poincaré gap lambda_min = 4.
2. Exact rational SU(2) Weyl cubic collar volume upper bound at delta = 1/5.
3. Local block total weight strictly within YM-101F all-orders margin.
4. Hard invariant in verifier_bridge: global commuting toron fiber remains open,
   barring unauthorized closure of asymptotic edge E-CROSSOVER.
5. Zero-jargon, zero-sorry, zero-axiom, and line-length audit of standalone
   modules MathlibPR_SchurComplementForms.lean and MathlibPR_CubicCollarBounds.lean.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import re
import unittest

from src.ymmg.block_weyl_collar_bound import (
    DELTA_ALL_ORDERS_MARGIN,
    W_IR_ALL_ORDERS,
    evaluate_local_block_collar_bulk_certificate,
    local_block_poincare_gap,
    local_bulk_nonabelian_residual,
    su2_weyl_collar_volume_bound,
)
from src.ymmg.coscientist import (
    CoScientistVerifierBridge,
    YMGenerationAgent,
    YangMillsCoScientistOrchestrator,
)

ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_DIR = ROOT / "formal" / "yang_mills_blueprint" / "YangMillsBlueprint"


class BlockWeylCollarAndLeanTests(unittest.TestCase):
    def test_01_exact_rational_local_block_poincare_gap(self):
        gap_2 = local_block_poincare_gap(2)
        self.assertEqual(gap_2, F(4, 1))

        gap_4 = local_block_poincare_gap(4)
        self.assertEqual(gap_4, F(1, 1))

        with self.assertRaises(ValueError):
            local_block_poincare_gap(1)

    def test_02_exact_rational_su2_weyl_collar_bound(self):
        delta = F(1, 5)
        collar = su2_weyl_collar_volume_bound(delta)
        # (452 / 1065) * (1 / 125) = 452 / 133125
        self.assertEqual(collar, F(452, 133125))

        # Must be strictly less than 1/5 of the certified YM-101F margin
        self.assertLess(collar, DELTA_ALL_ORDERS_MARGIN / 5)

        # Invalid delta domain handling
        with self.assertRaises(ValueError):
            su2_weyl_collar_volume_bound(F(0, 1))
        with self.assertRaises(ValueError):
            su2_weyl_collar_volume_bound(F(3, 5))

    def test_03_local_bulk_nonabelian_residual_and_certificate(self):
        beta_5 = F(41, 24)
        delta = F(1, 5)
        bulk = local_bulk_nonabelian_residual(beta=beta_5, delta=delta, block_side=2)
        # delta / (beta * 16) = (1/5) / (41/24 * 16) = (1/5) / (82/3) = 3/410
        self.assertEqual(bulk, F(3, 410))

        cert = evaluate_local_block_collar_bulk_certificate(beta_5=beta_5, delta=delta, block_side=2)
        self.assertTrue(cert.is_certified)
        self.assertEqual(cert.local_poincare_gap, F(4, 1))
        self.assertEqual(cert.weyl_collar_bound, F(452, 133125))
        self.assertEqual(cert.local_bulk_nonabelian_residual, F(3, 410))

        # Total local block weight 452/133125 + 3/410 = 116939/10916250
        self.assertEqual(cert.local_block_total_weight, F(116939, 10916250))
        self.assertLess(cert.local_block_total_weight, DELTA_ALL_ORDERS_MARGIN)
        self.assertLess(W_IR_ALL_ORDERS + cert.local_block_total_weight, F(1, 1))

        # Uniform local block vs open global commuting toron fiber
        self.assertTrue(cert.local_block_uniform_in_L)
        self.assertFalse(cert.global_commuting_fiber_closed)
        self.assertEqual(cert.verification_scope, "LOCAL_BLOCK_UNIFORM_GLOBAL_FIBER_OPEN")

    def test_04_verifier_bridge_rejects_asymptotic_closure_when_global_fiber_open(self):
        bridge = CoScientistVerifierBridge(root_dir=ROOT)
        gen = YMGenerationAgent()
        goal = YangMillsCoScientistOrchestrator.default_goal()
        cand = gen.generate_candidates(goal, run_id="RUN-WEYL-TEST", include_adversarial_flawed=False)[0]

        # Standard bounded hybrid candidate passes verification
        rep_valid = bridge.evaluate_candidate(cand, enable_lean=False, require_lean=False)
        self.assertTrue(rep_valid.passed)
        self.assertTrue(rep_valid.details["block_weyl_collar_ok"])
        self.assertTrue(rep_valid.details["block_weyl_collar_details"]["local_block_uniform_in_L"])
        self.assertFalse(rep_valid.details["block_weyl_collar_details"]["global_commuting_fiber_closed"])

        # Attempting to claim closure of E-CROSSOVER, E-THERMO, or E-LATTICE-CONT fails
        for edge in ("E-CROSSOVER", "E-THERMO", "E-LATTICE-CONT"):
            asymp_cand = gen.generate_candidates(goal, run_id="RUN-WEYL-ASYMP", include_adversarial_flawed=False)[0]
            asymp_cand.goal_id = edge
            rep_asymp = bridge.evaluate_candidate(asymp_cand, enable_lean=False, require_lean=False)
            self.assertFalse(rep_asymp.passed)
            self.assertTrue(any("ASYMPTOTIC_EDGE_UNAUTHORIZED_FROM_FINITE_AUDIT" in f for f in rep_asymp.failures))

    def test_05_mathlib_pr_standalone_modules_hygiene_audit(self):
        FORBIDDEN_JARGON = [
            "Clay",
            "CMI",
            "Millennium",
            "YM-101",
            "YM-102",
            "NEG-YM",
            "Chrysalis",
            "Dark Factory",
            "Toron",
            "Weitzenböck",
            "Weitzenbock",
            "Luscher",
            "Lüscher",
        ]

        pr_files = [
            BLUEPRINT_DIR / "MathlibPR_SchurComplementForms.lean",
            BLUEPRINT_DIR / "MathlibPR_CubicCollarBounds.lean",
        ]

        for pf in pr_files:
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
            # Strip comments first
            stripped = re.sub(r"/-.*?-/", "", text, flags=re.DOTALL)
            stripped = re.sub(r"--[^\n]*", "", stripped)

            sorry_hits = re.findall(r"\bsorry\b", stripped)
            self.assertEqual(len(sorry_hits), 0, f"Found sorry in {pf.name}")

            axiom_hits = re.findall(r"(?m)^\s*axiom\s+", stripped)
            self.assertEqual(len(axiom_hits), 0, f"Found axiom declaration in {pf.name}")

            # 4. 0 forbidden jargon tokens
            for word in FORBIDDEN_JARGON:
                self.assertNotIn(word.lower(), text.lower(), f"Forbidden jargon token '{word}' in {pf.name}")


if __name__ == "__main__":
    unittest.main()
