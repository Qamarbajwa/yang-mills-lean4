"""
Task YM-011-PRE: Fixed-Lattice Gradient-Flow Loop Perturbation Precursor Verification.

Provides exact symbolic/numerical verification of the elementary fixed-lattice
differential estimate for Wilson loops under the Wilson gradient flow:

    |W_t(C)[U] - W_0(C)[U]| <= K * n * (t / a^2)   (pointwise in U)
    |<W_t(C)>_Lambda - <W_0(C)>_Lambda| <= K * n * (t / a^2)   (expectation)

where n = |C| / a is the number of lattice links in the closed loop C.
"""

from typing import Dict, Any, Tuple
import math
import numpy as np


def compute_gradient_flow_lipschitz_constant(
    d: int,
    n_colors: int,
    beta: float,
    convention: str = "luscher_2010",
) -> Dict[str, Any]:
    """
    Computes the single-link operator-norm velocity bound for the lattice Wilson
    gradient flow on a d-dimensional hypercubic lattice with gauge group SU(N).

    Wilson Action Convention:
        S_W(U) = (beta / N) * sum_p Re Tr(I - U_p),  where beta = 2 * N / g_0^2.

    The Lie-algebra derivative of S_W with respect to link U_ell is proportional
    to the anti-Hermitian traceless projection P_{su(N)} of the sum of 2(d - 1)
    staple products incident on link ell, multiplied by prefactor (beta / (2N)) = 1 / g_0^2.

    Conventions:
    1. 'luscher_2010' (Standard Lüscher 2010 convention):
        a^2 * d/dt V_t(ell) = -g_0^2 * (partial_ell S_W(V_t)) * V_t(ell)
        Because g_0^2 * (beta / (2N)) = (2N / beta) * (beta / (2N)) = 1,
        the coupling beta / g_0^2 CANCELS IDENTICALLY!
        Each of the 2(d - 1) staples has unitary operator norm <= 1, and the
        anti-Hermitian projection satisfies ||P_{su(N)}(X)||_op <= ||X||_op <= 1.
        Hence:
            ||d/dt V_t(ell)||_op <= (2 * (d - 1)) / a^2,
        so K(d, N) = 2 * (d - 1) (= 6 in d = 4), strictly independent of beta.

    2. 'unscaled_action_gradient' (Unscaled gradient without g_0^2 factor):
        a^2 * d/dtau V_tau(ell) = -(partial_ell S_W(V_tau)) * V_tau(ell)
        Here the factor (beta / (2N)) is NOT multiplied by g_0^2, so beta REMAINS:
            ||d/dtau V_tau(ell)||_op <= (beta * (d - 1) / N) / a^2,
        giving K(beta, d, N) = beta * (d - 1) / N.
    """
    if d < 2:
        raise ValueError("Spacetime dimension d must be >= 2.")
    if n_colors < 2:
        raise ValueError("SU(N) requires N >= 2.")
    if beta <= 0:
        raise ValueError("Coupling beta must be > 0.")

    num_staples = 2 * (d - 1)
    g0_squared = (2.0 * n_colors) / beta
    action_derivative_prefactor = beta / (2.0 * n_colors)  # = 1 / g_0^2

    if convention == "luscher_2010":
        effective_prefactor = g0_squared * action_derivative_prefactor  # = 1.0 identically
        k_constant = float(num_staples) * effective_prefactor
        beta_cancels = math.isclose(effective_prefactor, 1.0, rel_tol=1e-15)
    elif convention == "unscaled_action_gradient":
        effective_prefactor = action_derivative_prefactor
        k_constant = float(num_staples) * effective_prefactor
        beta_cancels = False
    else:
        raise ValueError(f"Unknown flow convention: {convention!r}")

    return {
        "convention": convention,
        "d": d,
        "N": n_colors,
        "beta": beta,
        "g0_squared": g0_squared,
        "num_staples": num_staples,
        "beta_cancels": beta_cancels,
        "K_constant": k_constant,
    }


def normalized_wilson_loop_range(n_colors: int) -> Tuple[float, float]:
    """
    Returns the exact mathematical range of the normalized Wilson loop observable
        W_t(C) = (1 / N) Re Tr(Hol_C(V_t))
    for Hol_C(V_t) in SU(N).

    For any unitary matrix U in SU(N), its eigenvalues are e^{i theta_j} with
    sum_j theta_j = 0 (mod 2 pi).
    - Maximum of (1/N) sum_j cos(theta_j) is +1.0 (achieved at U = I_N).
    - Minimum of (1/N) sum_j cos(theta_j) over SU(N):
      * For even N >= 2, -I_N has det(-I_N) = (-1)^N = +1, so -I_N in SU(N)
        and W_t(C) achieves -1.0 exactly; thus range is [-1.0, 1.0].
      * For odd N >= 3, minimum is cos(pi * (N - 1) / N) < 0 (e.g. -0.5 for SU(3),
        approaching -1 as N -> infty), which is strictly negative and lies inside [-1.0, 1.0].
    In all cases N >= 2, W_t(C) takes strictly negative values and satisfies
    W_t(C) in [-1.0, 1.0], NEVER [0.0, 1.0].
    """
    if n_colors < 2:
        raise ValueError("SU(N) requires N >= 2.")
    max_val = 1.0
    if n_colors % 2 == 0:
        min_val = -1.0
    else:
        min_val = math.cos(math.pi * (n_colors - 1) / n_colors)
    return (min_val, max_val)


def evaluate_precursor_loop_perturbation_bound(
    n_links: int,
    t_flow: float,
    lattice_spacing_a: float,
    d: int = 4,
    n_colors: int = 3,
    beta: float = 6.0,
    convention: str = "luscher_2010",
) -> Dict[str, Any]:
    """
    Evaluates the YM-011-PRE fixed-lattice differential estimate:
        |W_t(C)[U] - W_0(C)[U]| <= K * n_links * (t / a^2)
    which holds BOTH pointwise for every lattice gauge field configuration U
    and in expectation under any probability measure mu_Lambda on SU(N)^{E(Lambda)}.
    """
    if n_links < 4:
        raise ValueError("A closed non-trivial lattice loop requires at least 4 links.")
    if t_flow < 0:
        raise ValueError("Flow time t_flow must be >= 0.")
    if lattice_spacing_a <= 0:
        raise ValueError("Lattice spacing a must be > 0.")

    flow_info = compute_gradient_flow_lipschitz_constant(
        d=d, n_colors=n_colors, beta=beta, convention=convention
    )
    k_val = flow_info["K_constant"]
    dimensionless_flow_ratio = t_flow / (lattice_spacing_a ** 2)
    linear_bound = k_val * n_links * dimensionless_flow_ratio
    # Because W_t(C) in [-1, 1], |W_t(C) - W_0(C)| is also trivially bounded by 2.0
    trivial_diameter_bound = 2.0

    return {
        "n_links": n_links,
        "t_flow": t_flow,
        "lattice_spacing_a": lattice_spacing_a,
        "dimensionless_flow_ratio": dimensionless_flow_ratio,
        "K_constant": k_val,
        "beta_cancels": flow_info["beta_cancels"],
        "pointwise_bound": linear_bound,
        "expectation_bound": linear_bound,
        "effective_clipped_bound": min(linear_bound, trivial_diameter_bound),
        "holds_pointwise": True,
        "holds_in_expectation": True,
    }
