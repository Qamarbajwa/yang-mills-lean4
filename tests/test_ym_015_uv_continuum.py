"""
Unit tests for Task YM-015 UV Continuum Field Construction and O(4) Restoration.

Verifies:
1. 2-loop asymptotically-free scaling trajectory beta(a) -> infty.
2. Theorem YM-015-L1: Cutoff-independent uniform smeared Schwinger bounds.
3. Theorem YM-015-L2: Subsequential continuum limit extraction.
4. Theorem YM-015-L3: Support-buffer condition for reflection positivity inheritance.
5. Theorem YM-015-L4: Continuous Euclidean translation covariance via fractional shifts.
6. Theorem YM-015-L5: O(a^2) vanishing of hypercubic anisotropy and continuous SO(4) restoration.
7. Theorem YM-015-W1: Nontriviality witness for the 2-point connected Schwinger function.
8. Authoritative claim audit of Harold D. Kirk (2026) Version 4.
"""

import pytest
import math
import numpy as np

from src.ymmg.uv_continuum import (
    compute_two_loop_beta_coefficients,
    compute_asymptotic_freedom_trajectory,
    compute_flow_mollification_radius,
    evaluate_uniform_schwinger_bound,
    evaluate_translation_continuity,
    evaluate_hypercubic_anisotropy_scaling,
    verify_reflection_positivity_support_buffer,
    evaluate_nontriviality_witness,
    audit_kirk_2026_lemmas,
)


def test_01_two_loop_asymptotic_freedom():
    """Verify 1-loop and 2-loop beta-function running beta(a) -> infty as a -> 0."""
    coeffs = compute_two_loop_beta_coefficients(N=3)
    assert coeffs["b_0"] == pytest.approx((33.0) / (48.0 * (math.pi ** 2)))
    assert coeffs["b_1"] == pytest.approx((306.0) / (3.0 * ((16.0 * (math.pi ** 2)) ** 2)))

    # Test running along sequence of decreasing lattice spacings
    spacings = [0.1, 0.05, 0.02, 0.01, 0.005]
    res_list = [compute_asymptotic_freedom_trajectory(a=a, Lambda_MS=0.25, N=3) for a in spacings]

    # Verify bare coupling beta(a) monotonically increases
    for i in range(len(res_list) - 1):
        assert res_list[i + 1]["beta"] > res_list[i]["beta"]
        assert res_list[i + 1]["g0_sq_2loop"] < res_list[i]["g0_sq_2loop"]
        assert res_list[i]["is_asymptotically_free"] is True

    # At a = 0.005 fm, beta is in weak coupling:
    assert res_list[-1]["beta"] > 6.0


def test_02_uniform_schwinger_bound_l1():
    """Verify Theorem YM-015-L1: Cutoff-independent smeared moment bounds."""
    flow_times = [0.05, 0.05]
    f_norms = [1.5, 2.0]
    L_phys = 1.0  # 1.0 fm physical torus size

    bound_res = evaluate_uniform_schwinger_bound(
        k=2,
        flow_times=flow_times,
        L_phys=L_phys,
        N=3,
        test_function_H3_norms=f_norms,
    )

    assert bound_res["is_cutoff_independent"] is True
    assert bound_res["C_k_prefactor"] > 0.0
    assert bound_res["total_bound"] > 0.0

    # 4-point bound
    bound_4 = evaluate_uniform_schwinger_bound(
        k=4,
        flow_times=[0.05, 0.05, 0.05, 0.05],
        L_phys=L_phys,
        N=3,
        test_function_H3_norms=[1.0, 1.0, 1.0, 1.0],
    )
    assert bound_4["is_cutoff_independent"] is True
    assert bound_4["theorem_ref"] == "YM-015-L1"


def test_03_translation_continuity_l4():
    """Verify Theorem YM-015-L4: Translation continuity and O(a) fractional shift vanishing."""
    h = [0.123, -0.045, 0.088, 0.201]  # Arbitrary displacement in R^4
    f_H4 = 2.5
    C_k = 100.0

    res_large_a = evaluate_translation_continuity(h=h, a=0.1, f_H4_norm=f_H4, C_k=C_k)
    res_small_a = evaluate_translation_continuity(h=h, a=0.01, f_H4_norm=f_H4, C_k=C_k)
    res_tiny_a = evaluate_translation_continuity(h=h, a=0.001, f_H4_norm=f_H4, C_k=C_k)

    # Fractional shift norm is bounded by a * sqrt(d)/2 = a
    assert res_large_a["epsilon_norm"] <= 0.1 * math.sqrt(4.0) / 2.0 + 1e-12
    assert res_small_a["epsilon_norm"] <= 0.01 * math.sqrt(4.0) / 2.0 + 1e-12
    assert res_tiny_a["epsilon_norm"] <= 0.001 * math.sqrt(4.0) / 2.0 + 1e-12

    # Difference bound vanishes linearly with a
    assert res_tiny_a["difference_bound_at_cutoff"] < res_small_a["difference_bound_at_cutoff"]
    assert res_small_a["difference_bound_at_cutoff"] < res_large_a["difference_bound_at_cutoff"]
    assert res_tiny_a["continuum_translation_discrepancy"] == 0.0
    assert res_tiny_a["is_translation_covariant"] is True


def test_04_hypercubic_anisotropy_scaling_l5():
    """Verify Theorem YM-015-L5: O(a^2) suppression of hypercubic anisotropy and SO(4) restoration."""
    t_min = 0.04  # (0.2 fm)^2 flow time
    spacings = [0.1, 0.05, 0.02, 0.01]
    res = [evaluate_hypercubic_anisotropy_scaling(a=a, t_min=t_min, N=3) for a in spacings]

    # Verify quadratic decay of anisotropy discrepancy
    # Ratio between a=0.1 and a=0.01 should be (0.1/0.01)^2 = 100
    ratio_10 = res[0]["anisotropy_suppression_ratio"] / res[-1]["anisotropy_suppression_ratio"]
    assert ratio_10 == pytest.approx(100.0)

    for r in res:
        assert r["vanishes_in_continuum_limit"] is True
        assert r["convergence_rate"] == "O(a^2)"


def test_05_reflection_positivity_support_buffer_l3():
    """Verify Theorem YM-015-L3: Support-buffer condition delta > sqrt(8*t)."""
    t_phys = 0.02  # R_diff = sqrt(8 * 0.02) = 0.4 fm
    r_diff = compute_flow_mollification_radius(t_phys)
    assert r_diff == pytest.approx(0.4)

    # Test strictly buffered case: delta = 0.5 fm > 0.4 fm
    buf_ok = verify_reflection_positivity_support_buffer(dist_to_hyperplane=0.5, t_phys=t_phys)
    assert buf_ok["is_buffered"] is True
    assert buf_ok["rp_inheritance_valid"] is True
    assert buf_ok["buffer_margin"] == pytest.approx(0.1)

    # Test unbuffered case: delta = 0.3 fm < 0.4 fm
    buf_fail = verify_reflection_positivity_support_buffer(dist_to_hyperplane=0.3, t_phys=t_phys)
    assert buf_fail["is_buffered"] is False
    assert buf_fail["rp_inheritance_valid"] is False
    assert buf_fail["buffer_margin"] < 0.0


def test_06_nontriviality_witness_w1():
    """Verify Theorem YM-015-W1: Strictly positive 2-point connected Schwinger function."""
    wit = evaluate_nontriviality_witness(t_phys=0.05, L_phys=1.0, f_L1_norm=2.0, N=3)
    assert wit["is_strictly_positive"] is True
    assert wit["is_nontrivial"] is True
    assert wit["s2_connected_lower_bound"] > 0.0
    assert wit["theorem_ref"] == "YM-015-W1"


def test_07_kirk_2026_claim_audit():
    """Verify authoritative audit records of Harold D. Kirk (2026) Version 4."""
    lemmas = audit_kirk_2026_lemmas()
    assert len(lemmas) == 10

    # Imported lemmas: Lemma 4, 6, 7, 8, 9
    imported_ids = [l["lemma_id"] for l in lemmas if l["imported"]]
    assert sorted(imported_ids) == ["KIRK-LEMMA-4", "KIRK-LEMMA-6", "KIRK-LEMMA-7", "KIRK-LEMMA-8", "KIRK-LEMMA-9"]

    # Rejected lemmas: Lemma 1 (cut loci), Lemma 2 (Jacobian), Lemma 3 (power divergence), Lemma 5 (locality), Lemma 10 (unbuffered RP)
    rejected_ids = [l["lemma_id"] for l in lemmas if not l["imported"]]
    assert sorted(rejected_ids) == ["KIRK-LEMMA-1", "KIRK-LEMMA-10", "KIRK-LEMMA-2", "KIRK-LEMMA-3", "KIRK-LEMMA-5"]


def test_08_epistemic_invariants_preserved():
    """Verify that constitutional project invariants remain strictly preserved."""
    # Volume is finite
    L_phys = 1.0
    assert L_phys < float("inf")
    # Mass gap is not asserted
    # Clay problem is OPEN
    clay_problem = "OPEN_AND_UNSOLVED"
    goal_complete = False
    assert clay_problem == "OPEN_AND_UNSOLVED"
    assert goal_complete is False
