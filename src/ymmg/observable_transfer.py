"""
Exact Finite-Lattice Observable-Transfer Map Construction & Verification (`YM-011-OBS-MAP`).

Implements the mathematical objects, exact identities, and finite-lattice comparison
theorems (`YM-011-OBS-T1`, `YM-011-OBS-T2`, `YM-011-OBS-T3`) on two finite lattices
Lambda_0 (spacing a) and Lambda_1 (spacing 2a):

1. Explicit configuration spaces Omega_0 = SU(N)^{E(Lambda_0)}, Omega_1 = SU(N)^{E(Lambda_1)},
   gauge group actions G_0, G_1, and restriction homomorphism pi_G : G_0 -> G_1.
2. Coaxial decimation blocking map B^{dec}_{0->1} = B^{mid}_0 and everywhere-smooth
   SU(N)-valued midpoint-exponential transverse-smeared blocking map B^{mid}_alpha.
3. Exact orientation covariance B^{mid}_alpha(U)(e^{-1}) = (B^{mid}_alpha(U)(e))^{-1}
   and exact gauge equivariance B^{mid}_alpha(g_0 . U) = pi_G(g_0) . B^{mid}_alpha(U).
4. Exact midpoint staple factorization:
   L_{gamma_{nu,sigma}}(e)[U] = U(l_1)^dagger H_0(gamma_{nu,sigma})[U] U(l_2)^dagger
                              = P_{1,nu,sigma}^dagger P_{2,nu,sigma}^dagger.
5. Exact non-abelian quadratic plaquette defect identity (`YM-011-OBS-T2`):
   2(d-1) X_{mid}(e)[U] - Y_{flow}(e)[U]
     = sum_{nu != mu, sigma in {+,-}} P_{su(N)}((P_{1,nu,sigma}^dagger - I_N)(P_{2,nu,sigma}^dagger - I_N)).
6. Global Lipschitz comparison bound (`YM-011-OBS-T1`) and Markov kernel Schur character
   factorization (`YM-011-OBS-T3`).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

import numpy as np
from scipy.linalg import expm

from src.ymmg.precursor_flow import (
    hilbert_schmidt_norm,
    project_su_n,
)


@dataclass(frozen=True)
class ObservableTransferSpec:
    """Metadata and constants for the single-step (a -> 2a) observable-transfer map."""
    spacetime_dim: int
    su_n: int
    fine_spacing_a: float
    coarse_spacing_2a: float
    num_transverse_staples: int
    matched_alpha_over_t_a2: float


def build_observable_transfer_spec(
    spacetime_dim: int = 4,
    su_n: int = 3,
    fine_spacing_a: float = 1.0,
) -> ObservableTransferSpec:
    """Construct canonical specification for YM-011-OBS-MAP between spacings a and 2a."""
    if spacetime_dim < 2:
        raise ValueError(f"Spacetime dimension must be >= 2, got {spacetime_dim}")
    if su_n < 2:
        raise ValueError(f"SU(N) rank N must be >= 2, got {su_n}")
    if fine_spacing_a <= 0.0:
        raise ValueError(f"Fine lattice spacing a must be > 0, got {fine_spacing_a}")
    num_staples = 2 * (spacetime_dim - 1)
    return ObservableTransferSpec(
        spacetime_dim=spacetime_dim,
        su_n=su_n,
        fine_spacing_a=fine_spacing_a,
        coarse_spacing_2a=2.0 * fine_spacing_a,
        num_transverse_staples=num_staples,
        matched_alpha_over_t_a2=float(num_staples),
    )


def demonstrate_naive_linear_average_singularity() -> Dict[str, object]:
    """
    Negative structural demonstration (`NEG-YM-011-OBS-1`):
    Shows that naive linear matrix averaging M_alpha(e) = (1 - alpha) U_coax + (alpha / K) sum H_0(gamma)
    leaves SU(N) for alpha in (0, 1] and admits configurations in Omega_0 with det(M_alpha(e)) = 0
    where polar projection onto SU(N) is undefined.
    """
    u_coax = np.eye(2, dtype=np.complex128)
    staple_holonomy = -np.eye(2, dtype=np.complex128)  # valid element of SU(2) since det(-I_2) = 1
    alpha = 0.5
    m_half = (1.0 - alpha) * u_coax + alpha * staple_holonomy
    det_m = float(np.real(np.linalg.det(m_half)))
    return {
        "u_coax_in_su2": bool(np.allclose(u_coax @ u_coax.conj().T, np.eye(2)) and math.isclose(np.real(np.linalg.det(u_coax)), 1.0)),
        "staple_in_su2": bool(np.allclose(staple_holonomy @ staple_holonomy.conj().T, np.eye(2)) and math.isclose(np.real(np.linalg.det(staple_holonomy)), 1.0)),
        "alpha": alpha,
        "det_m_alpha": det_m,
        "is_singular": math.isclose(det_m, 0.0, abs_tol=1e-15),
        "m_alpha_in_su2": False,
    }


def midpoint_generator_from_staples(
    u1: np.ndarray,
    u2: np.ndarray,
    staple_holonomies: Sequence[np.ndarray],
) -> np.ndarray:
    """
    Compute the midpoint Lie-algebra generator X_mid(e)[U] in su(N):
      X_mid(e)[U] = P_{su(N)}( (1 / M) sum_{gamma} u1^dagger H_0(gamma) u2^dagger )
    where M = len(staple_holonomies) = 2(d - 1).
    """
    if not staple_holonomies:
        raise ValueError("staple_holonomies must be non-empty")
    u1_dag = u1.conj().T
    u2_dag = u2.conj().T
    accum = np.zeros_like(u1, dtype=np.complex128)
    for h_gamma in staple_holonomies:
        accum = accum + (u1_dag @ h_gamma @ u2_dag)
    accum = accum / float(len(staple_holonomies))
    return project_su_n(accum)


def block_link_midpoint_exponential(
    u1: np.ndarray,
    u2: np.ndarray,
    staple_holonomies: Sequence[np.ndarray],
    alpha: float,
) -> np.ndarray:
    """
    Evaluate the everywhere-smooth SU(N)-valued deterministic blocking map:
      B^{mid}_alpha(U)(e) = u1 exp(alpha X_mid(e)[U]) u2 in SU(N).
    """
    x_mid = midpoint_generator_from_staples(u1, u2, staple_holonomies)
    return u1 @ expm(alpha * x_mid) @ u2


def verify_midpoint_staple_and_quadratic_plaquette_identity(
    u1: np.ndarray,
    u2: np.ndarray,
    transverse_links_left: Sequence[np.ndarray],
    transverse_links_mid: Sequence[np.ndarray],
    transverse_links_right: Sequence[np.ndarray],
    longitudinal_top_1: Sequence[np.ndarray],
    longitudinal_top_2: Sequence[np.ndarray],
) -> Dict[str, object]:
    """
    Verify the exact algebraic identities of YM-011-OBS-MAP for a coarse edge e = (l_1, l_2):
    For each transverse staple channel r = 1, ..., 2(d-1):
      - 1x1 staple around u1: s_{1,r} = w_{left,r} * w_{top1,r} * w_{mid,r}^dagger
      - 1x1 staple around u2: s_{2,r} = w_{mid,r} * w_{top2,r} * w_{right,r}^dagger
      - 2x1 coarse staple: H_0(gamma_r) = w_{left,r} * w_{top1,r} * w_{top2,r} * w_{right,r}^dagger
      1. Exact staple factorization: s_{1,r} @ s_{2,r} == H_0(gamma_r) (interior link w_{mid,r} cancels).
      2. Exact midpoint loop factorization:
         L_r = u1^dagger @ H_0(gamma_r) @ u2^dagger == P_{1,r}^dagger @ P_{2,r}^dagger,
         where P_{1,r} = s_{1,r}^dagger @ u1 and P_{2,r} = u2 @ s_{2,r}^dagger are the two 1x1 fine plaquettes
         based at the midpoint m(e).
      3. Exact quadratic plaquette defect identity (`YM-011-OBS-T2`):
         2(d-1) X_{mid}(e) - Y_{flow}(e) == sum_r P_{su(N)}((P_{1,r}^dagger - I_N) @ (P_{2,r}^dagger - I_N)),
         where Y_{flow}(e) = sum_r (P_{su(N)}(P_{1,r}^dagger) + P_{su(N)}(P_{2,r}^dagger)).
    """
    m_channels = len(transverse_links_mid)
    n = u1.shape[0]
    ident = np.eye(n, dtype=np.complex128)

    staple_2x1_list: List[np.ndarray] = []
    p1_list: List[np.ndarray] = []
    p2_list: List[np.ndarray] = []
    max_staple_factor_err = 0.0
    max_midpoint_loop_err = 0.0

    for r in range(m_channels):
        w_l = transverse_links_left[r]
        w_m = transverse_links_mid[r]
        w_r = transverse_links_right[r]
        t_1 = longitudinal_top_1[r]
        t_2 = longitudinal_top_2[r]

        s1 = w_l @ t_1 @ w_m.conj().T
        s2 = w_m @ t_2 @ w_r.conj().T
        h_2x1 = w_l @ t_1 @ t_2 @ w_r.conj().T
        staple_2x1_list.append(h_2x1)

        max_staple_factor_err = max(
            max_staple_factor_err,
            float(np.linalg.norm(s1 @ s2 - h_2x1, ord="fro")),
        )

        p1 = s1.conj().T @ u1
        p2 = u2 @ s2.conj().T
        p1_list.append(p1)
        p2_list.append(p2)

        l_mid = u1.conj().T @ h_2x1 @ u2.conj().T
        rhs_mid = p1.conj().T @ p2.conj().T
        max_midpoint_loop_err = max(
            max_midpoint_loop_err,
            float(np.linalg.norm(l_mid - rhs_mid, ord="fro")),
        )

    x_mid = midpoint_generator_from_staples(u1, u2, staple_2x1_list)
    lhs_diff = float(m_channels) * x_mid

    y_flow = np.zeros((n, n), dtype=np.complex128)
    rhs_quad = np.zeros((n, n), dtype=np.complex128)
    bound_sum = 0.0

    for p1, p2 in zip(p1_list, p2_list):
        p1_dag = p1.conj().T
        p2_dag = p2.conj().T
        y_flow = y_flow + project_su_n(p1_dag) + project_su_n(p2_dag)
        quad_term = (p1_dag - ident) @ (p2_dag - ident)
        rhs_quad = rhs_quad + project_su_n(quad_term)
        op_norm_1 = float(np.linalg.norm(p1 - ident, ord=2))
        hs_norm_2 = hilbert_schmidt_norm(p2 - ident)
        bound_sum += op_norm_1 * hs_norm_2

    generator_mismatch = lhs_diff - y_flow
    identity_residual = float(np.linalg.norm(generator_mismatch - rhs_quad, ord="fro"))
    mismatch_hs = hilbert_schmidt_norm(generator_mismatch)

    return {
        "num_channels": m_channels,
        "max_staple_factorization_error": max_staple_factor_err,
        "max_midpoint_loop_factorization_error": max_midpoint_loop_err,
        "quadratic_identity_residual": identity_residual,
        "generator_mismatch_hs_norm": mismatch_hs,
        "quadratic_upper_bound_hs": bound_sum,
        "bound_satisfied": mismatch_hs <= bound_sum + 1e-12,
    }


def evaluate_global_loop_transfer_bound(
    coarse_edge_count_m: int,
    alpha: float,
    flow_time_t: float,
    fine_spacing_a: float = 1.0,
    spacetime_dim: int = 4,
) -> Dict[str, float]:
    """
    Evaluate the unconditional finite-lattice observable-transfer bounds (`YM-011-OBS-T1`)
    for a coarse loop C_1 of m = |C_1|_{Lambda_1} coarse edges (fine length 2m, physical perimeter 2ma):
      1. | (B^{mid}_alpha)^* W(C_1) - W_0(iota(C_1)) | <= |alpha| * m
      2. | W_t(iota(C_1)) - W_0(iota(C_1)) | <= 4(d - 1) * m * (t / a^2)
      3. | (B^{mid}_alpha)^* W(C_1) - W_t(iota(C_1)) | <= m * (|alpha| + 4(d - 1) * (t / a^2))
    """
    if coarse_edge_count_m < 1:
        raise ValueError("coarse_edge_count_m must be >= 1")
    if flow_time_t < 0.0:
        raise ValueError("flow_time_t must be >= 0")
    if fine_spacing_a <= 0.0:
        raise ValueError("fine_spacing_a must be > 0")

    block_perturbation_bound = abs(alpha) * float(coarse_edge_count_m)
    flow_perturbation_bound = 4.0 * float(spacetime_dim - 1) * float(coarse_edge_count_m) * (flow_time_t / (fine_spacing_a ** 2))
    total_discrepancy_bound = block_perturbation_bound + flow_perturbation_bound
    return {
        "coarse_edge_count_m": float(coarse_edge_count_m),
        "fine_edge_count_2m": float(2 * coarse_edge_count_m),
        "physical_perimeter": 2.0 * float(coarse_edge_count_m) * fine_spacing_a,
        "block_to_unflowed_bound": block_perturbation_bound,
        "flow_to_unflowed_bound": flow_perturbation_bound,
        "total_block_to_flow_bound": total_discrepancy_bound,
    }


def su2_markov_character_factor(kappa: float) -> float:
    """
    Exact analytic fundamental character ratio c_F(kappa) in [0, 1) for the normalized
    SU(2) Markov block-spin kernel:
      K(dV | B) propto exp((kappa / 2) Re Tr(V^dagger B)) dV.
    On SU(2), W = cos(theta) I_2 + i sin(theta) n . sigma with Haar measure (2/pi) sin^2(theta) dtheta
    and (kappa / 2) Re Tr(W) = kappa cos(theta), so:
      z_2(kappa) = (2/pi) int_0^pi e^{kappa cos(theta)} sin^2(theta) dtheta = 2 I_1(kappa) / kappa,
      c_F(kappa) = d/dkappa ln z_2(kappa) = I_2(kappa) / I_1(kappa) in [0, 1).
    Uses the convergent power series for modified Bessel functions I_1(kappa) and I_2(kappa).
    """
    if kappa < 0.0:
        raise ValueError(f"kappa must be >= 0, got {kappa}")
    if kappa == 0.0:
        return 0.0

    # Power series: I_nu(x) = sum_{k=0}^infty (x/2)^{2k + nu} / (k! (k + nu)!)
    half_x = 0.5 * kappa
    i1 = 0.0
    i2 = 0.0
    term1 = half_x  # k=0 for I_1: (x/2)^1 / (0! 1!)
    term2 = (half_x ** 2) / 2.0  # k=0 for I_2: (x/2)^2 / (0! 2!)
    for k in range(1, 80):
        i1 += term1
        i2 += term2
        term1 *= (half_x * half_x) / (float(k) * float(k + 1))
        term2 *= (half_x * half_x) / (float(k) * float(k + 2))
    return float(i2 / i1)
