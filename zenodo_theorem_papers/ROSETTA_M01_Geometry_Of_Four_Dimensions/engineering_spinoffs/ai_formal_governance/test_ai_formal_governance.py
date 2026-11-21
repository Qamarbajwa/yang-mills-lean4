"""
Test Suite for AI Formal Governance Sandbox
Author: Qamar Munawer
Affiliation: Brandenburg University of Technology Cottbus-Senftenberg
Methodology: ai is being used as a tool
"""

import unittest
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))

from premise_a_bridge_harness import (
    MunicipalPremiseA,
    ScientificPremiseA,
    ZeroTrustMunicipalBridge,
    ZeroTrustScientificBridge,
    VerdictStatus,
    run_governance_benchmark
)

class TestAIFormalGovernance(unittest.TestCase):
    def test_compliant_municipal_plan(self):
        """Verify that a compliant architectural proposal passes."""
        plan = MunicipalPremiseA(
            project_id="P01",
            plot_area_sqm=1000.0,
            total_built_up_area_sqm=1500.0,
            max_allowable_far=1.80,
            occupancy_count=100,
            egress_width_meters=1.50,
            beam_span_meters=8.0,
            beam_depth_meters=0.50,
            front_setback_meters=4.0,
            rear_setback_meters=3.5,
            side_setback_meters=2.5
        )
        res = ZeroTrustMunicipalBridge.verify(plan)
        self.assertEqual(res["verdict"], VerdictStatus.PROVEN_COMPLIANT)
        self.assertEqual(len(res["violations"]), 0)

    def test_far_violation_rejection(self):
        """Verify that FAR exceeding statutory maximum is flagged as PROVEN_VIOLATION."""
        plan = MunicipalPremiseA(
            project_id="P02_FAR_VIOLATION",
            plot_area_sqm=1000.0,
            total_built_up_area_sqm=2500.0, # FAR 2.5 > 1.8
            max_allowable_far=1.80,
            occupancy_count=100,
            egress_width_meters=1.50,
            beam_span_meters=8.0,
            beam_depth_meters=0.50,
            front_setback_meters=4.0,
            rear_setback_meters=3.5,
            side_setback_meters=2.5
        )
        res = ZeroTrustMunicipalBridge.verify(plan)
        self.assertEqual(res["verdict"], VerdictStatus.PROVEN_VIOLATION)
        self.assertTrue(any("FAR violation" in v for v in res["violations"]))

    def test_fire_egress_violation_rejection(self):
        """Verify that insufficient fire escape width is caught."""
        plan = MunicipalPremiseA(
            project_id="P03_EGRESS_VIOLATION",
            plot_area_sqm=1000.0,
            total_built_up_area_sqm=1500.0,
            max_allowable_far=1.80,
            occupancy_count=500, # required: 500 * 0.005 = 2.50 m
            egress_width_meters=1.50, # only 1.50 m provided
            beam_span_meters=8.0,
            beam_depth_meters=0.50,
            front_setback_meters=4.0,
            rear_setback_meters=3.5,
            side_setback_meters=2.5
        )
        res = ZeroTrustMunicipalBridge.verify(plan)
        self.assertEqual(res["verdict"], VerdictStatus.PROVEN_VIOLATION)
        self.assertTrue(any("Egress width violation" in v for v in res["violations"]))

    def test_epistemic_millennium_settlement_rejection(self):
        """Verify that any agent claiming an open Millennium problem is unconditionally solved is rejected."""
        claim = ScientificPremiseA(
            claim_id="INVALID_OVERCLAIM",
            finite_metric_name="fake_gap",
            finite_metric_value=1.0,
            finite_metric_floor=0.0,
            lean4_certified=True,
            axioms_used=["propext", "Classical.choice", "Quot.sound"],
            open_horizon_lock_active=True,
            claims_millennium_settled=True # Forbidden overclaim
        )
        res = ZeroTrustScientificBridge.verify(claim)
        self.assertEqual(res["verdict"], VerdictStatus.REJECTED_EPISTEMIC_VIOLATION)

    def test_custom_axiom_rejection(self):
        """Verify that non-standard custom axioms in Lean 4 proofs are flagged."""
        claim = ScientificPremiseA(
            claim_id="NON_STANDARD_AXIOM",
            finite_metric_name="metric",
            finite_metric_value=2.0,
            finite_metric_floor=0.0,
            lean4_certified=True,
            axioms_used=["propext", "Classical.choice", "Quot.sound", "MagicAxiom"],
            open_horizon_lock_active=True,
            claims_millennium_settled=False
        )
        res = ZeroTrustScientificBridge.verify(claim)
        self.assertEqual(res["verdict"], VerdictStatus.PROVEN_VIOLATION)
        self.assertIn("MagicAxiom", res["reason"])

    def test_benchmark_receipt_generation(self):
        """Verify that run_governance_benchmark generates a valid PASS receipt."""
        receipt_path = "test_gov_receipt.json"
        try:
            receipt = run_governance_benchmark(receipt_path)
            self.assertEqual(receipt["overall_status"], "PASS")
            self.assertTrue(os.path.exists(receipt_path))
        finally:
            if os.path.exists(receipt_path):
                os.remove(receipt_path)

if __name__ == "__main__":
    unittest.main()
