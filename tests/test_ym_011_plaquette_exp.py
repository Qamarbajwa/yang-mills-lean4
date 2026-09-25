"""
Deterministic Mathematical & Computational Verification Suite for `YM-011-PLAQUETTE-EXP`.

Tests:
1. Exact SU(N) Hilbert-Schmidt plaquette identity ||U_p - I_N||_HS^2 = 2N (1 - (1/N) Re Tr(U_p))
   and operator-to-HS norm inequality ||U_p - I_N||_op <= ||U_p - I_N||_HS (plus exact SU(2)
   identity ||U_p - I_2||_op = (1/sqrt(2)) ||U_p - I_2||_HS).
2. Unconditional expectation reduction `YM-011-PLAQUETTE-EXP-T1` in both inhomogeneous
   boundary-condition-independent form and isotropic periodic torus form (C(d, N) = 4(d-1)sqrt(N)).
3. Periodic torus symmetry group `(Z / 2LZ)^d rtimes S_d` and exact volume-independent
   link-to-plaquette ratio |E_+(Lambda_0)| / |P_+(Lambda_0)| = 2 / (d - 1).
4. Exact partition-function derivative identity `YM-011-PLAQUETTE-EXP-T2` and
   `NUMERICAL_DIAGNOSTIC_ONLY` Bessel character verification.
5. Verification of strict separation of Claims A, B, and C, `NEG-YM-011-PLAQ-1` toron
   singular-strata obstruction, and project invariants.
"""

from pathlib import Path
import math
import numpy as np
import pytest
from scipy.linalg import expm

from src.ymmg.plaquette_expectation import (
    compute_general_inhomogeneous_expectation_bound,
    compute_unconditional_tangent_expectation_bound,
    su2_single_plaquette_thermodynamic_identity_diagnostic,
    su_n_plaquette_energy_range,
    verify_periodic_torus_plaquette_symmetry_group,
    verify_su_n_plaquette_hs_identity,
)
from src.ymmg.precursor_flow import luscher_su_n_generators
from src.ymmg.ros import compute_closed_world_scientific_tree_hash


def _random_su_n(n: int, rng: np.random.Generator, scale: float = 0.8) -> np.ndarray:
    gens = luscher_su_n_generators(n)
    coeffs = rng.normal(0.0, scale, size=len(gens))
    return expm(sum(c * g for c, g in zip(coeffs, gens)))


def test_1_su_n_plaquette_hs_identity_and_su2_exact_spectral_ratio():
    rng = np.random.default_rng(2026092501)
    for n in (2, 3, 4):
        for _ in range(8):
            u_p = _random_su_n(n, rng, scale=0.9)
            res = verify_su_n_plaquette_hs_identity(u_p)
            assert res["identity_residual"] < 1e-13
            assert res["op_to_hs_ratio"] <= 1.0 + 1e-14
            if n == 2:
                assert math.isclose(res["op_to_hs_ratio"], 1.0 / math.sqrt(2.0), rel_tol=1e-13)


def test_1b_extremal_group_configurations_and_exact_range():
    # 1. Identity configuration: U_p = I_N => h_p = 0.0
    for n in (2, 3, 4):
        u_id = np.eye(n, dtype=np.complex128)
        res_id = verify_su_n_plaquette_hs_identity(u_id)
        assert math.isclose(res_id["plaquette_energy_h_p"], 0.0, abs_tol=1e-15)
        assert math.isclose(res_id["hs_norm_squared"], 0.0, abs_tol=1e-15)
        assert math.isclose(res_id["identity_residual"], 0.0, abs_tol=1e-15)

    # 2. SU(2) extremal negative central element: U_p = -I_2 in SU(2)
    # det(-I_2) = (-1)^2 = 1.
    u_neg_i2 = -np.eye(2, dtype=np.complex128)
    res_neg_i2 = verify_su_n_plaquette_hs_identity(u_neg_i2)
    assert math.isclose(res_neg_i2["re_tr_norm"], -1.0, abs_tol=1e-15)
    assert math.isclose(res_neg_i2["plaquette_energy_h_p"], 2.0, abs_tol=1e-15)
    # ||-I_2 - I_2||_HS^2 = ||-2 I_2||_HS^2 = 4 * 2 = 8 = 2 * 2 * 2.0
    assert math.isclose(res_neg_i2["hs_norm_squared"], 8.0, abs_tol=1e-15)
    assert math.isclose(res_neg_i2["rhs_2n_one_minus_retr"], 8.0, abs_tol=1e-15)
    assert res_neg_i2["identity_residual"] < 1e-14
    assert math.isclose(res_neg_i2["operator_norm"], 2.0, abs_tol=1e-15)
    assert math.isclose(res_neg_i2["hs_norm"], 2.0 * math.sqrt(2.0), abs_tol=1e-15)
    # Exact spectral ratio holds even at the extremal element h_p = 2.0:
    assert math.isclose(res_neg_i2["op_to_hs_ratio"], 1.0 / math.sqrt(2.0), rel_tol=1e-14)

    # 3. SU(4) extremal negative central element: U_p = -I_4 in SU(4)
    # det(-I_4) = (-1)^4 = 1.
    u_neg_i4 = -np.eye(4, dtype=np.complex128)
    res_neg_i4 = verify_su_n_plaquette_hs_identity(u_neg_i4)
    assert math.isclose(res_neg_i4["re_tr_norm"], -1.0, abs_tol=1e-15)
    assert math.isclose(res_neg_i4["plaquette_energy_h_p"], 2.0, abs_tol=1e-15)
    assert math.isclose(res_neg_i4["hs_norm_squared"], 16.0, abs_tol=1e-15)
    assert res_neg_i4["identity_residual"] < 1e-14

    # 4. SU(3) odd-N minimum trace configuration:
    # U_p = exp(i 2pi/3) I_3 in SU(3), det(U_p) = (exp(i 2pi/3))^3 = exp(i 2pi) = 1.
    # Note: -I_3 is NOT in SU(3) because det(-I_3) = -1.
    omega3 = np.exp(2.0j * np.pi / 3.0)
    u_su3_min = omega3 * np.eye(3, dtype=np.complex128)
    res_su3_min = verify_su_n_plaquette_hs_identity(u_su3_min)
    assert math.isclose(res_su3_min["re_tr_norm"], -0.5, abs_tol=1e-15)
    assert math.isclose(res_su3_min["plaquette_energy_h_p"], 1.5, abs_tol=1e-15)
    # ||omega3 I_3 - I_3||_HS^2 = 3 * |omega3 - 1|^2 = 3 * 3 = 9 = 2 * 3 * 1.5
    assert math.isclose(res_su3_min["hs_norm_squared"], 9.0, abs_tol=1e-15)
    assert res_su3_min["identity_residual"] < 1e-14

    # 5. Check exact group-theoretic range function across even and odd N
    assert su_n_plaquette_energy_range(2) == (0.0, 2.0)
    assert math.isclose(su_n_plaquette_energy_range(3)[1], 1.5, abs_tol=1e-15)
    assert su_n_plaquette_energy_range(4) == (0.0, 2.0)
    assert math.isclose(su_n_plaquette_energy_range(5)[1], 1.0 + math.cos(math.pi / 5.0), abs_tol=1e-15)
    assert su_n_plaquette_energy_range(6) == (0.0, 2.0)


def test_2_unconditional_expectation_reduction_t1():
    res_su3 = compute_unconditional_tangent_expectation_bound(
        coarse_edge_count_m=4,
        mean_plaquette_energy=0.15,
        spacetime_dim=4,
        su_n=3,
    )
    assert math.isclose(res_su3.universal_constant_c_d_n, 12.0 * math.sqrt(3.0), rel_tol=1e-15)
    assert math.isclose(res_su3.universal_upper_bound, 12.0 * math.sqrt(3.0) * 4.0 * 0.15, rel_tol=1e-15)
    assert res_su3.su2_sharp_constant_c_d_2 is None

    res_su2 = compute_unconditional_tangent_expectation_bound(
        coarse_edge_count_m=4,
        mean_plaquette_energy=0.15,
        spacetime_dim=4,
        su_n=2,
    )
    assert math.isclose(res_su2.universal_constant_c_d_n, 12.0 * math.sqrt(2.0), rel_tol=1e-15)
    assert math.isclose(float(res_su2.su2_sharp_constant_c_d_2), 12.0, rel_tol=1e-15)
    assert math.isclose(float(res_su2.su2_sharp_upper_bound), 12.0 * 4.0 * 0.15, rel_tol=1e-15)

    # Check general inhomogeneous reduction reduces to isotropic formula when all e_p = e_plaq
    pairs = [(0.15, 0.15) for _ in range(4 * 6)]
    inhom_bound = compute_general_inhomogeneous_expectation_bound(pairs, su_n=3)
    assert math.isclose(inhom_bound, res_su3.universal_upper_bound, rel_tol=1e-15)


def test_2b_range_boundary_validation():
    # 1. Exact evaluation at maximum energy e_plaq = 2.0
    res_su2_max = compute_unconditional_tangent_expectation_bound(
        coarse_edge_count_m=4,
        mean_plaquette_energy=2.0,
        spacetime_dim=4,
        su_n=2,
    )
    assert math.isclose(float(res_su2_max.su2_sharp_upper_bound), 12.0 * 4.0 * 2.0, rel_tol=1e-15)
    assert math.isclose(res_su2_max.universal_upper_bound, 12.0 * math.sqrt(2.0) * 4.0 * 2.0, rel_tol=1e-15)

    res_su3_max = compute_unconditional_tangent_expectation_bound(
        coarse_edge_count_m=4,
        mean_plaquette_energy=2.0,
        spacetime_dim=4,
        su_n=3,
    )
    assert math.isclose(res_su3_max.universal_upper_bound, 12.0 * math.sqrt(3.0) * 4.0 * 2.0, rel_tol=1e-15)

    # 2. Exact evaluation at minimum energy e_plaq = 0.0
    res_zero = compute_unconditional_tangent_expectation_bound(
        coarse_edge_count_m=4,
        mean_plaquette_energy=0.0,
        spacetime_dim=4,
        su_n=2,
    )
    assert math.isclose(res_zero.universal_upper_bound, 0.0, abs_tol=1e-15)
    assert math.isclose(float(res_zero.su2_sharp_upper_bound), 0.0, abs_tol=1e-15)

    # 3. Reject negative and out-of-range energies
    with pytest.raises(ValueError, match="mean_plaquette_energy must lie in"):
        compute_unconditional_tangent_expectation_bound(coarse_edge_count_m=4, mean_plaquette_energy=-0.001)

    with pytest.raises(ValueError, match="mean_plaquette_energy must lie in"):
        compute_unconditional_tangent_expectation_bound(coarse_edge_count_m=4, mean_plaquette_energy=2.001)


def test_3_periodic_torus_symmetry_and_volume_independent_link_plaquette_ratio():
    for l_size in (1, 2, 4, 8):
        sym = verify_periodic_torus_plaquette_symmetry_group(spacetime_dim=4, coarse_length_l=l_size)
        assert sym["link_to_plaquette_ratio_is_volume_independent"] is True
        assert math.isclose(float(sym["link_to_plaquette_ratio"]), 2.0 / 3.0, rel_tol=1e-15)
        assert sym["translations_transitive_on_vertices"] is True
        assert sym["axis_permutations_transitive_on_planes"] is True


def test_4_thermodynamic_identity_and_numerical_diagnostics():
    prev_e_plaq = 1.0
    for beta in (0.5, 2.0, 10.0, 50.0):
        diag = su2_single_plaquette_thermodynamic_identity_diagnostic(beta)
        assert diag["thermodynamic_identity_residual"] < 1e-10
        assert 0.0 < diag["e_plaq_exact"] < prev_e_plaq
        prev_e_plaq = diag["e_plaq_exact"]
    diag_large = su2_single_plaquette_thermodynamic_identity_diagnostic(100.0)
    assert math.isclose(diag_large["beta_times_e_plaq"], 1.5, rel_tol=0.02)


def test_5_claims_separation_and_governance_invariants():
    root = Path(__file__).resolve().parent.parent
    tree_hash, file_hashes = compute_closed_world_scientific_tree_hash(root)
    assert len(tree_hash) == 64
    assert "literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md" in file_hashes

    doc = (root / "literature" / "YM-011-PLAQUETTE-EXP-ANALYSIS.md").read_text(encoding="utf-8")
    assert "YM-011-PLAQUETTE-EXP-T1" in doc
    assert "YM-011-PLAQUETTE-EXP-T2" in doc
    assert "YM-011-PLAQUETTE-EXP-L1" in doc
    assert "NEG-YM-011-PLAQ-1" in doc
    assert "NUMERICAL_DIAGNOSTIC_ONLY" in doc
    assert "Claim A" in doc and "Claim B" in doc and "Claim C" in doc
    assert "WITHHELD_AS_UNRESOLVED_DEPENDENCY" in doc
    assert "YM-011-TREE-GAUGE" in doc
    assert "GOAL_COMPLETE" in doc and "OPEN_AND_UNSOLVED" in doc
