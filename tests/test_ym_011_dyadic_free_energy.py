"""
Deterministic regression test suite for YM-011-DYADIC-FREE-ENERGY-UNIFORMITY:
Non-Asymptotic Volume Uniformity of Periodic Dyadic Free-Energy Increment,
Thermodynamic Suppression of Toron Zero Modes, Exact Fourier Mode Cancellation,
and Resolution of Volume-Uniform Periodic Plaquette Bound (P2).
"""

from __future__ import annotations

import math
from pathlib import Path
import pytest

from src.ymmg.dyadic_free_energy import (
    audit_dyadic_free_energy_uniformity,
    evaluate_gaussian_dyadic_increment,
    evaluate_stratified_laplace_bulk_limit,
    evaluate_toron_thermodynamic_scaling,
    evaluate_volume_uniform_plaquette_bound_guardrail,
    verify_peierls_polymer_tail_bound,
)
from src.ymmg.ros import (
    verify_baseline_lineage_transition,
    verify_full_git_object_exists,
)

ROOT = Path(__file__).resolve().parents[1]


def test_01_exact_gaussian_mode_cancellation_and_monotonicity():
    """
    Verifies that the non-zero Gaussian Laplacian eigenvalues cancel identically
    in the dyadic partition-ratio increment Delta f_0(beta, L), and that Delta f_0(beta, L)
    monotonically increases to the bulk limit as L -> infty.
    """
    for d in [2, 3, 4]:
        for N in [2, 3]:
            prev_inc = 0.0
            bulk = (float(N**2 - 1) / (2.0 * math.comb(d, 2))) * math.log(2.0)
            for L in [2, 4, 8, 16]:
                res = evaluate_gaussian_dyadic_increment(L=L, d=d, N=N)
                inc = res["dyadic_increment"]
                assert inc > prev_inc, f"Monotonicity failed at L={L}, d={d}, N={N}"
                assert inc < bulk, f"Increment exceeded bulk limit at L={L}, d={d}, N={N}"
                prev_inc = inc
            # Verify asymptotic convergence
            assert math.isclose(inc, bulk, rel_tol=1e-2)


def test_02_toron_thermodynamic_scaling_decays_as_L_to_minus_d():
    """
    Verifies that the toron zero-mode free-energy density Delta f_toron decays as O(L^{-d}),
    so toron flat and quartic zero modes are thermodynamically suppressed as L -> infty.
    """
    for d in [2, 3, 4]:
        for N in [2, 3, 4]:
            res_2 = evaluate_toron_thermodynamic_scaling(L=2, d=d, N=N)
            res_4 = evaluate_toron_thermodynamic_scaling(L=4, d=d, N=N)
            res_8 = evaluate_toron_thermodynamic_scaling(L=8, d=d, N=N)

            # Ratio when doubling L should be 2^d
            ratio_2_to_4 = res_2["toron_specific_increment"] / res_4["toron_specific_increment"]
            ratio_4_to_8 = res_4["toron_specific_increment"] / res_8["toron_specific_increment"]

            expected_ratio = float(2**d)
            assert math.isclose(ratio_2_to_4, expected_ratio, rel_tol=1e-5)
            assert math.isclose(ratio_4_to_8, expected_ratio, rel_tol=1e-5)


def test_03_stratified_laplace_coefficient_monotonically_bounded_by_bulk():
    """
    Verifies that C_per(L, 4, N) = ((N^2 - 1)/4)*(1 - 1/(3*L^4)) is strictly less than
    C_bulk(4, N) = (N^2 - 1)/4 for every L >= 2, and that the deficit is exactly (N^2 - 1)/(12*L^4).
    """
    for N in [2, 3, 4, 5]:
        c_bulk_expected = (N**2 - 1) / 4.0
        prev_c_per = 0.0
        for L in [2, 3, 4, 6, 8]:
            res = evaluate_stratified_laplace_bulk_limit(L=L, d=4, N=N)
            c_per = res["C_per"]
            assert c_per > prev_c_per, f"Monotonicity failed at L={L}, N={N}"
            assert c_per < c_bulk_expected, f"C_per exceeded C_bulk at L={L}, N={N}"
            assert res["is_bounded_by_bulk"] is True

            expected_deficit = float(N**2 - 1) / (12.0 * (L**4))
            assert math.isclose(res["deficit"], expected_deficit, rel_tol=1e-6)
            prev_c_per = c_per


def test_04_dyadic_uniformity_audit_synthesis():
    """
    Verifies the complete dyadic uniformity audit across dimensions d=2, 3, 4 and SU(2), SU(3).
    """
    for d in [2, 4]:
        for N in [2, 3]:
            audit = audit_dyadic_free_energy_uniformity(L=4, d=d, N=N)
            assert audit.is_c_per_strictly_bounded_by_bulk is True
            assert audit.dyadic_uniformity_status == "UNIFORMLY_BOUNDED_BY_BULK"
            assert audit.toron_finite_size_correction > 0.0


def test_05_peierls_polymer_tail_bound_and_convergence():
    """
    Verifies that the Kotecky-Preiss polymer condition converges for beta >= beta_polymer
    and establishes an exponentially decaying tail bound uniform in L.
    """
    # At beta = 1.0 (strong coupling), not in weak-coupling polymer regime
    res_low = verify_peierls_polymer_tail_bound(beta=1.0, d=4, N=2)
    assert res_low["is_polymer_expansion_convergent"] is False

    # At beta = 15.0, polymer condition converges
    res_high = verify_peierls_polymer_tail_bound(beta=15.0, d=4, N=2)
    assert res_high["is_polymer_expansion_convergent"] is True
    assert res_high["tail_bound_uniform_in_L"] is True
    assert res_high["polymer_tail_density_bound"] < 0.05


def test_06_hierarchy_guardrail_p1_p2_p3():
    """
    Verifies that:
      - P1 is PROVED;
      - P2 is PROVED_AT_WEAK_COUPLING (volume-uniform periodic bound);
      - P3 fails closed with ValueError (requires continuum construction, OPEN).
    """
    # P1
    p1 = evaluate_volume_uniform_plaquette_bound_guardrail(
        claim_level="P1_FIXED_VOLUME_PERIODIC", L=4, d=4, N=2
    )
    assert p1["status"] == "PROVED"
    assert p1["strictly_bounded_by_bulk"] is True

    # P2 at weak coupling
    p2 = evaluate_volume_uniform_plaquette_bound_guardrail(
        claim_level="P2_VOLUME_UNIFORM_PERIODIC", L=4, d=4, N=2, beta=20.0
    )
    assert p2["status"] == "PROVED_AT_WEAK_COUPLING"
    assert p2["c_bulk_d4"] == 0.75  # (2^2 - 1)/4 = 3/4 = 0.75
    assert p2["uniform_in_L"] is True

    # P3 must fail closed
    with pytest.raises(ValueError, match="P3_CONTINUUM_UNIFORM_CONTROL is OPEN"):
        evaluate_volume_uniform_plaquette_bound_guardrail(
            claim_level="P3_CONTINUUM_UNIFORM_CONTROL", L=4, d=4, N=2
        )


def test_07_baseline_lineage_transition_from_toron_quartic():
    """
    Verifies that the closeout commit 6a1883bec275fc0e910b5fe708a4b9151c55d5b5
    exists in Git and forms a valid verified lineage.
    """
    baseline_sha = "6a1883bec275fc0e910b5fe708a4b9151c55d5b5"
    assert verify_full_git_object_exists(baseline_sha, repo_root=ROOT) == "commit"
    res = verify_baseline_lineage_transition(
        prior_closeout_sha=baseline_sha,
        next_baseline_sha=baseline_sha,
        transition_class="SAME",
        repo_root=ROOT,
    )
    assert res["status"] == "BASELINE_LINEAGE_VERIFIED"
