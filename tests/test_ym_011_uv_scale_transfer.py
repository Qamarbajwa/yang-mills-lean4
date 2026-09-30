"""
Unit tests for YM-011: Multiscale UV Scale-Transfer and Observables Mollification.
"""

import pytest
import math
from pathlib import Path

from ymmg.uv_scale_transfer import (
    compute_flow_matching_parameter,
    compute_bulk_plaquette_constant,
    compute_single_step_transfer_bound,
    compute_multiscale_geometric_sum,
    evaluate_crossover_stopping_diagnostic,
    evaluate_bridge_lemma_guardrails,
    CrossoverBoundaryReached,
)


def test_01_flow_matching_parameter():
    # In d=4, alpha(t) = 2(4-1) * (t/a^2) = 6 * (t/a^2)
    assert math.isclose(compute_flow_matching_parameter(t=0.05, a=0.1, d=4), 30.0)
    assert math.isclose(compute_flow_matching_parameter(t=0.0, a=0.1, d=4), 0.0)
    
    # In d=3, alpha(t) = 4 * (t/a^2)
    assert math.isclose(compute_flow_matching_parameter(t=0.01, a=0.1, d=3), 4.0)

    # Error handling
    with pytest.raises(ValueError, match="Lattice spacing a must be positive"):
        compute_flow_matching_parameter(t=0.1, a=-0.1)
    with pytest.raises(ValueError, match="Flow time t must be non-negative"):
        compute_flow_matching_parameter(t=-0.1, a=0.1)
    with pytest.raises(ValueError, match="Dimension d must be >= 2"):
        compute_flow_matching_parameter(t=0.1, a=0.1, d=1)


def test_02_single_step_transfer_bound_constants():
    # SU(3) in d=4: C_bulk = (9-1)/4 = 2.0
    c_bulk_3 = compute_bulk_plaquette_constant(d=4, N=3)
    assert math.isclose(c_bulk_3, 2.0)

    # SU(2) in d=4: C_bulk = (4-1)/4 = 0.75
    c_bulk_2 = compute_bulk_plaquette_constant(d=4, N=2)
    assert math.isclose(c_bulk_2, 0.75)

    res_su3 = compute_single_step_transfer_bound(
        beta=10.0, loop_length_a=8.0, t_over_a2=0.05, d=4, N=3
    )
    # C_tan for SU(3) = 12 * sqrt(3) * 2.0 = 24 * sqrt(3) ~= 41.5692
    assert math.isclose(res_su3["c_tan"], 24.0 * math.sqrt(3.0), rel_tol=1e-5)
    assert math.isclose(res_su3["c_rem"], 36.0)
    assert math.isclose(res_su3["n_coarse_links"], 4.0)
    assert res_su3["tangent_defect_bound"] > 0.0
    assert res_su3["remainder_bound"] > 0.0
    assert math.isclose(
        res_su3["total_bound"],
        res_su3["tangent_defect_bound"] + res_su3["remainder_bound"]
    )

    # Sharp SU(2) constant: C_tan = 4*(4-1)*0.75 = 9.0
    res_su2 = compute_single_step_transfer_bound(
        beta=10.0, loop_length_a=4.0, t_over_a2=0.05, d=4, N=2
    )
    assert math.isclose(res_su2["c_tan"], 9.0)


def test_03_optimal_flow_time_scaling():
    # With t/a^2 = c0 = sqrt(2N) / beta, the remainder scales as O(beta^-2)
    # while the tangent defect scales as O(beta^-1).
    beta1 = 20.0
    beta2 = 40.0
    N = 3
    c0_1 = math.sqrt(2 * N) / beta1
    c0_2 = math.sqrt(2 * N) / beta2

    b1 = compute_single_step_transfer_bound(beta=beta1, loop_length_a=4.0, t_over_a2=c0_1, d=4, N=N)
    b2 = compute_single_step_transfer_bound(beta=beta2, loop_length_a=4.0, t_over_a2=c0_2, d=4, N=N)

    # Tangent defect should halve exactly
    assert math.isclose(b1["tangent_defect_bound"] / b2["tangent_defect_bound"], 2.0, rel_tol=1e-5)
    # Remainder should quarter (quadratic)
    assert math.isclose(b1["remainder_bound"] / b2["remainder_bound"], 4.0, rel_tol=1e-5)
    # Total bound should scale by a factor between 2.0 (linear) and 4.0 (quadratic)
    ratio = b1["total_bound"] / b2["total_bound"]
    assert 2.0 <= ratio <= 4.0


def test_04_multiscale_geometric_sum_convergence():
    g0_sq = 0.2
    res = compute_multiscale_geometric_sum(g0_sq=g0_sq, n_scales=8, d=4, N=3)
    
    assert res["is_geometrically_convergent"] is True
    assert res["cumulative_sum"] < 3.0 * g0_sq
    assert len(res["running_couplings"]) == 8

    # Running coupling should grow monotonically with scale index j
    for j in range(len(res["running_couplings"]) - 1):
        assert res["running_couplings"][j] < res["running_couplings"][j + 1]

    # Step error weights 2^{-j} * g_j^2 should decay monotonically
    for j in range(len(res["step_error_weights"]) - 1):
        assert res["step_error_weights"][j] > res["step_error_weights"][j + 1]


def test_05_crossover_stopping_diagnostic_and_exception():
    g0_sq = 0.2
    diag = evaluate_crossover_stopping_diagnostic(g0_sq=g0_sq, g_star_sq=0.64, d=4, N=3)
    assert diag["is_finite_uv_domain"] is True
    assert diag["n_cross"] > 0
    assert "NEG-YM-011-TRANSFER-2" in diag["limitation"]

    # When requesting an excessively large scale beyond the crossover horizon, CrossoverBoundaryReached is raised
    with pytest.raises(CrossoverBoundaryReached, match="nonperturbative crossover reached"):
        compute_multiscale_geometric_sum(g0_sq=0.5, n_scales=100, d=4, N=3)


def test_06_epistemic_guardrails():
    assert evaluate_bridge_lemma_guardrails() is True

    with pytest.raises(ValueError, match="does NOT prove a continuum mass gap"):
        evaluate_bridge_lemma_guardrails(claim_mass_gap=True)

    with pytest.raises(ValueError, match="Clay Millennium Problem #4 remains OPEN_AND_UNSOLVED"):
        evaluate_bridge_lemma_guardrails(claim_clay_solved=True)

    with pytest.raises(ValueError, match="Full continuum limit requires crossover bridge"):
        evaluate_bridge_lemma_guardrails(claim_continuum_limit=True)


def test_07_negative_evidence_consistency():
    repo_root = Path(__file__).resolve().parent.parent
    neg_reg = (repo_root / "NEGATIVE_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    assert "NEG-YM-011-TRANSFER-1" in neg_reg
    assert "NEG-YM-011-TRANSFER-2" in neg_reg
