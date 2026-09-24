"""
Deterministic Mathematical & Computational Verification Suite for `YM-011-OBS-MAP`.

Tests:
1. Configuration space, probability measure, and blocking specification in d=4.
2. Negative structural counterexample `NEG-YM-011-OBS-1` (singular determinant locus of naive linear averaging).
3. Everywhere SU(N)-valued smoothness, orientation covariance, and exact G_0 -> G_1 gauge equivariance
   of the midpoint-exponential blocking map B^{mid}_alpha on SU(2) and SU(3).
4. Exact coaxial associativity identity `ID-OBS-2` at alpha = 0 and global loop perturbation bound `YM-011-OBS-T1`.
5. Exact midpoint staple factorization `ID-OBS-3` and non-abelian quadratic plaquette defect identity
   `YM-011-OBS-T2`, including quadratic O(epsilon_plaq^2) small-field scaling.
6. Exact Schur character factorization `YM-011-OBS-T3` and `NEG-YM-011-OBS-2` for Markov block-spin kernels.
7. Repository artifact classification and governance invariants.
"""

from pathlib import Path
import math
import numpy as np
from scipy.linalg import expm

from src.ymmg.observable_transfer import (
    block_link_midpoint_exponential,
    build_observable_transfer_spec,
    demonstrate_naive_linear_average_singularity,
    evaluate_global_loop_transfer_bound,
    midpoint_generator_from_staples,
    su2_markov_character_factor,
    verify_midpoint_staple_and_quadratic_plaquette_identity,
)
from src.ymmg.precursor_flow import (
    hilbert_schmidt_norm,
    luscher_su_n_generators,
)
from src.ymmg.ros import compute_closed_world_scientific_tree_hash


def _random_su_n(n: int, rng: np.random.Generator, scale: float = 1.0) -> np.ndarray:
    """Sample an element of SU(N) by exponentiating a random element of su(N)."""
    gens = luscher_su_n_generators(n)
    coeffs = rng.normal(0.0, scale, size=len(gens))
    x = sum(c * g for c, g in zip(coeffs, gens))
    return expm(x)


def test_1_observable_transfer_spec_and_negative_counterexample():
    spec = build_observable_transfer_spec(spacetime_dim=4, su_n=3, fine_spacing_a=0.5)
    assert spec.spacetime_dim == 4
    assert spec.su_n == 3
    assert math.isclose(spec.fine_spacing_a, 0.5)
    assert math.isclose(spec.coarse_spacing_2a, 1.0)
    assert spec.num_transverse_staples == 6
    assert math.isclose(spec.matched_alpha_over_t_a2, 6.0)

    neg = demonstrate_naive_linear_average_singularity()
    assert neg["u_coax_in_su2"] is True
    assert neg["staple_in_su2"] is True
    assert neg["is_singular"] is True
    assert math.isclose(float(neg["det_m_alpha"]), 0.0, abs_tol=1e-15)


def test_2_midpoint_exponential_su_n_orientation_and_gauge_equivariance():
    rng = np.random.default_rng(20260924)
    for n in (2, 3):
        u1 = _random_su_n(n, rng, scale=0.7)
        u2 = _random_su_n(n, rng, scale=0.7)
        staples = [_random_su_n(n, rng, scale=0.7) for _ in range(6)]
        alpha = 0.35

        b_fwd = block_link_midpoint_exponential(u1, u2, staples, alpha)
        # Verify exact SU(N) membership
        assert np.allclose(b_fwd @ b_fwd.conj().T, np.eye(n), atol=1e-13)
        assert math.isclose(float(np.real(np.linalg.det(b_fwd))), 1.0, abs_tol=1e-13)
        assert math.isclose(float(np.imag(np.linalg.det(b_fwd))), 0.0, abs_tol=1e-13)

        # Verify exact orientation reversal: B_alpha(e^{-1}) == (B_alpha(e))^{-1}
        u1_rev = u2.conj().T
        u2_rev = u1.conj().T
        staples_rev = [h.conj().T for h in staples]
        b_rev = block_link_midpoint_exponential(u1_rev, u2_rev, staples_rev, alpha)
        assert np.allclose(b_rev, b_fwd.conj().T, atol=1e-13)

        # Verify exact gauge equivariance under arbitrary fine gauge transformations
        # g_y at start, g_m at midpoint (not in coarse lattice!), g_y_prime at end
        g_y = _random_su_n(n, rng, scale=0.9)
        g_m = _random_su_n(n, rng, scale=0.9)
        g_y_prime = _random_su_n(n, rng, scale=0.9)

        u1_g = g_y @ u1 @ g_m.conj().T
        u2_g = g_m @ u2 @ g_y_prime.conj().T
        staples_g = [g_y @ h @ g_y_prime.conj().T for h in staples]

        b_gauged = block_link_midpoint_exponential(u1_g, u2_g, staples_g, alpha)
        expected_gauged = g_y @ b_fwd @ g_y_prime.conj().T
        assert np.allclose(b_gauged, expected_gauged, atol=1e-13)


def test_3_coaxial_identity_and_global_loop_transfer_bound_t1():
    rng = np.random.default_rng(20260925)
    n = 3
    m_edges = 4
    alpha = 0.18

    u1_list = [_random_su_n(n, rng, scale=0.6) for _ in range(m_edges)]
    u2_list = [_random_su_n(n, rng, scale=0.6) for _ in range(m_edges)]
    staples_per_edge = [[_random_su_n(n, rng, scale=0.6) for _ in range(6)] for _ in range(m_edges)]

    # At alpha = 0, (B_0^{mid})^* W(C_1) == W_0(iota(C_1)) identically
    holonomy_alpha0 = np.eye(n, dtype=np.complex128)
    holonomy_fine = np.eye(n, dtype=np.complex128)
    holonomy_alpha = np.eye(n, dtype=np.complex128)
    for k in range(m_edges):
        b0_k = block_link_midpoint_exponential(u1_list[k], u2_list[k], staples_per_edge[k], 0.0)
        ba_k = block_link_midpoint_exponential(u1_list[k], u2_list[k], staples_per_edge[k], alpha)
        holonomy_alpha0 = holonomy_alpha0 @ b0_k
        holonomy_fine = holonomy_fine @ u1_list[k] @ u2_list[k]
        holonomy_alpha = holonomy_alpha @ ba_k

    w_alpha0 = np.trace(holonomy_alpha0) / float(n)
    w_fine = np.trace(holonomy_fine) / float(n)
    w_alpha = np.trace(holonomy_alpha) / float(n)

    assert abs(w_alpha0 - w_fine) < 1e-14

    # Check global Lipschitz bound YM-011-OBS-T1: |w_alpha - w_fine| <= |alpha| * m_edges
    bounds = evaluate_global_loop_transfer_bound(
        coarse_edge_count_m=m_edges,
        alpha=alpha,
        flow_time_t=0.02,
        fine_spacing_a=1.0,
        spacetime_dim=4,
    )
    assert abs(w_alpha - w_fine) <= bounds["block_to_unflowed_bound"] + 1e-13
    assert abs(np.real(w_alpha) - np.real(w_fine)) <= abs(w_alpha - w_fine) + 1e-15


def test_4_midpoint_staple_factorization_and_quadratic_plaquette_identity_t2():
    rng = np.random.default_rng(20260926)
    for n in (2, 3):
        u1 = _random_su_n(n, rng, scale=0.5)
        u2 = _random_su_n(n, rng, scale=0.5)
        w_left = [_random_su_n(n, rng, scale=0.5) for _ in range(6)]
        w_mid = [_random_su_n(n, rng, scale=0.5) for _ in range(6)]
        w_right = [_random_su_n(n, rng, scale=0.5) for _ in range(6)]
        t_1 = [_random_su_n(n, rng, scale=0.5) for _ in range(6)]
        t_2 = [_random_su_n(n, rng, scale=0.5) for _ in range(6)]

        res = verify_midpoint_staple_and_quadratic_plaquette_identity(
            u1, u2, w_left, w_mid, w_right, t_1, t_2
        )
        assert res["max_staple_factorization_error"] < 1e-14
        assert res["max_midpoint_loop_factorization_error"] < 1e-14
        assert res["quadratic_identity_residual"] < 1e-14
        assert res["bound_satisfied"] is True

    # Verify quadratic O(epsilon^2) scaling in the small-field regime
    n = 3
    eps_values = [0.1, 0.01]
    norms = []
    for eps in eps_values:
        rng_eps = np.random.default_rng(12345)
        u1_e = _random_su_n(n, rng_eps, scale=eps)
        u2_e = _random_su_n(n, rng_eps, scale=eps)
        w_l_e = [_random_su_n(n, rng_eps, scale=eps) for _ in range(6)]
        w_m_e = [_random_su_n(n, rng_eps, scale=eps) for _ in range(6)]
        w_r_e = [_random_su_n(n, rng_eps, scale=eps) for _ in range(6)]
        t1_e = [_random_su_n(n, rng_eps, scale=eps) for _ in range(6)]
        t2_e = [_random_su_n(n, rng_eps, scale=eps) for _ in range(6)]
        res_e = verify_midpoint_staple_and_quadratic_plaquette_identity(
            u1_e, u2_e, w_l_e, w_m_e, w_r_e, t1_e, t2_e
        )
        norms.append(float(res_e["generator_mismatch_hs_norm"]))

    # When scale shrinks by 10x, quadratic plaquette defect shrinks by ~100x
    ratio = norms[0] / norms[1]
    assert 80.0 < ratio < 120.0


def test_5_markov_kernel_schur_character_factorization_t3():
    assert math.isclose(su2_markov_character_factor(0.0), 0.0, abs_tol=1e-15)
    c1 = su2_markov_character_factor(2.0)
    c2 = su2_markov_character_factor(10.0)
    c3 = su2_markov_character_factor(40.0)
    assert 0.0 < c1 < c2 < c3 < 1.0
    # Asymptotic expansion for SU(2): 1 - c_F(kappa) ~ 3 / (2 * kappa)
    assert math.isclose(1.0 - c3, 1.5 / 40.0, rel_tol=0.05)


def test_6_closed_world_fingerprint_and_governance_invariants():
    root = Path(__file__).resolve().parent.parent
    tree_hash, file_hashes = compute_closed_world_scientific_tree_hash(root)
    assert len(tree_hash) == 64
    assert "literature/YM-011-OBS-MAP-CONSTRUCTION.md" in file_hashes

    doc = (root / "literature" / "YM-011-OBS-MAP-CONSTRUCTION.md").read_text(encoding="utf-8")
    assert "YM-011-OBS-T1" in doc
    assert "YM-011-OBS-T2" in doc
    assert "YM-011-OBS-T3" in doc
    assert "NEG-YM-011-OBS-1" in doc
    assert "GOAL_COMPLETE" in doc
    assert "OPEN_AND_UNSOLVED" in doc
    assert "YM-011-PLAQUETTE-EXP" in doc
