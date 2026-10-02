"""
Unit tests for Task YM-014R External-Evidence Reconciliation.

Verifies:
1. Exact SU(2) Makeenko-Migdal single-trace linearity (vanishing split operator).
2. Non-vanishing SU(3) loop splitting operator (multi-trace coupling).
3. Adaptive loop bootstrap scaling model.
4. Faizal-Shabir (2026) dimensional scaling defect.
5. Authoritative theorem reconciliation records and obstruction taxonomy.
"""

import pytest
from src.ymmg.evidence_reconciliation import (
    verify_su2_trace_reality_and_vanishing_split,
    verify_su3_non_vanishing_split,
    evaluate_adaptive_bootstrap_scaling,
    calculate_faizal_shabir_scaling_defect,
    get_all_theorem_reconciliations,
    AmendmentClassification,
    ObstructionType,
)


def test_01_su2_trace_reality_and_vanishing_split():
    """Verify that in SU(2), Tr(U) is real and Tr(U - U^dag) == 0 identically."""
    res = verify_su2_trace_reality_and_vanishing_split(num_samples=500, seed=123)
    assert res["su2_splitting_vanishes_identically"] is True
    assert res["max_imaginary_trace"] < 1e-14
    assert res["max_trace_split_operator"] < 1e-14


def test_02_su3_non_vanishing_split():
    """Verify that in SU(3), Tr(U - U^dag) is non-zero, proving multi-trace coupling."""
    res = verify_su3_non_vanishing_split(num_samples=500, seed=456)
    assert res["su3_splitting_is_non_zero"] is True
    assert res["non_zero_split_fraction"] > 0.95
    assert res["max_trace_split_norm"] > 0.5
    assert res["mean_im_trace_squared"] > 0.1


def test_03_adaptive_bootstrap_scaling():
    """Verify that adaptive bootstrap scaling maintains physical reach as a -> 0."""
    res_large = evaluate_adaptive_bootstrap_scaling(a=0.1, R_star_fm=0.5)
    assert res_large["adaptive_truncation_depth"] == 5
    assert res_large["adaptive_physical_reach_fm"] == pytest.approx(0.5)
    assert res_large["fixed_physical_reach_fm"] == pytest.approx(0.6)  # 6 * 0.1

    res_small = evaluate_adaptive_bootstrap_scaling(a=0.01, R_star_fm=0.5)
    assert res_small["adaptive_truncation_depth"] == 50
    assert res_small["adaptive_physical_reach_fm"] == 0.5
    # Fixed truncation physical reach collapses to 0.06 fm:
    assert res_small["fixed_physical_reach_fm"] == pytest.approx(0.06)
    assert res_small["fixed_ratio_to_target"] == pytest.approx(0.12)
    assert res_small["adaptive_ratio_to_target"] == pytest.approx(1.0)


def test_04_faizal_shabir_scaling_defect():
    """Verify that assuming dimensionless mu >= c_0 > 0 forces physical mass M_phys -> infty."""
    spacings = [0.2, 0.1, 0.05, 0.01, 0.001]
    res = calculate_faizal_shabir_scaling_defect(dimensionless_gap_mu=0.5, lattice_spacings=spacings)
    assert len(res) == len(spacings)

    # At a = 0.2 fm, M_phys = 0.5 / 0.2 = 2.5 fm^-1 ~= 493 MeV
    assert res[0]["resulting_physical_mass_inv_fm"] == pytest.approx(2.5)

    # At a = 0.001 fm (continuum limit), M_phys = 0.5 / 0.001 = 500 fm^-1 ~= 98.6 GeV (divergent)
    assert res[-1]["resulting_physical_mass_inv_fm"] == pytest.approx(500.0)

    # True dimensionless gap for 1 GeV mass must vanish as a -> 0:
    assert res[-1]["correct_dimensionless_mu_for_1gev"] == pytest.approx(5.06773 * 0.001)
    assert res[-1]["correct_dimensionless_mu_for_1gev"] < 0.01


def test_05_theorem_audit_records_completeness():
    """Verify that all 12 theorems of YM-012, YM-013, and YM-014 are audited."""
    records = get_all_theorem_reconciliations()
    assert len(records) == 12

    theorem_ids = [r.theorem_id for r in records]
    expected_ids = [
        "YM-012-T1", "YM-012-T2", "YM-012-T3", "YM-012-T4",
        "YM-013-T1", "YM-013-T2", "YM-013-T3", "YM-013-T4",
        "YM-014-T1", "YM-014-T2", "YM-014-T3", "YM-014-T4"
    ]
    assert sorted(theorem_ids) == sorted(expected_ids)


def test_06_amendment_classification_counts():
    """Verify exact distribution of amendment statuses."""
    records = get_all_theorem_reconciliations()
    status_counts = {}
    for r in records:
        status_counts[r.amendment_status] = status_counts.get(r.amendment_status, 0) + 1

    # Needs amendment: YM-013-T1 (SU(2) refuted), YM-014-T2 (extensive sign decay unproved)
    assert status_counts[AmendmentClassification.NEEDS_AMENDMENT] == 2

    # Confirmed with narrower scope: YM-012-T4, YM-013-T2, YM-013-T4, YM-014-T1, YM-014-T3, YM-014-T4
    assert status_counts[AmendmentClassification.CONFIRMED_WITH_NARROWER_SCOPE] == 6

    # Confirmed: YM-012-T1, YM-012-T2, YM-012-T3, YM-013-T3
    assert status_counts[AmendmentClassification.CONFIRMED] == 4


def test_07_obstruction_tier_categorization():
    """Verify that all obstruction theorems are classified as METHOD_SPECIFIC_OBSTRUCTION."""
    records = get_all_theorem_reconciliations()
    for r in records:
        if r.obstruction_tier is not None:
            assert r.obstruction_tier == ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
            # Ensure no premature STRUCTURAL_NO_GO exists
            assert r.obstruction_tier != ObstructionType.STRUCTURAL_NO_GO


def test_08_invalid_inputs_error_handling():
    """Verify error handling on invalid physical inputs."""
    with pytest.raises(ValueError, match="Lattice spacing 'a' must be positive"):
        evaluate_adaptive_bootstrap_scaling(a=-0.1)

    with pytest.raises(ValueError, match="Physical scale 'R_star_fm' must be positive"):
        evaluate_adaptive_bootstrap_scaling(a=0.1, R_star_fm=-1.0)
