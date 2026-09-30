"""
YM-011: Multiscale UV Scale-Transfer and Observables Mollification Implementation.

This module implements the mathematical machinery of Theorem YM-011-L1:
1. Exact optimal flow-matching parameter alpha(t) = 2(d-1) t / a^2.
2. Single-step Gibbs expectation transfer bound between coarse blocked observable
   and flowed fine observable.
3. Multiscale geometric convergence across the asymptotic-freedom UV hierarchy.
4. Intermediate coupling crossover stopping diagnostic (NEG-YM-011-TRANSFER-2).
5. Epistemic guardrails enforcing non-sufficiency for the continuum mass gap.
"""

from typing import Dict, Any, List, Optional
import math
import numpy as np


class CrossoverBoundaryReached(Exception):
    """Raised when multiscale RG iteration reaches the non-perturbative crossover window."""
    pass


def compute_flow_matching_parameter(t: float, a: float, d: int = 4) -> float:
    """
    Computes the exact flow-matching parameter alpha(t) = 2(d-1) * (t / a^2).
    
    This exact choice cancels the O(t/a^2) linear term in the discrepancy between
    the midpoint-exponential coarse blocking map and the Yang-Mills gradient flow.
    """
    if a <= 0.0:
        raise ValueError(f"Lattice spacing a must be positive, got {a}")
    if t < 0.0:
        raise ValueError(f"Flow time t must be non-negative, got {t}")
    if d < 2:
        raise ValueError(f"Dimension d must be >= 2, got {d}")
    return 2.0 * (d - 1) * (t / (a ** 2))


def compute_bulk_plaquette_constant(d: int = 4, N: int = 3) -> float:
    """
    Computes the bulk plaquette constant C_bulk(d, N).
    In d=4: C_bulk(4, N) = (N^2 - 1) / 4.
    """
    if d < 2 or N < 2:
        raise ValueError(f"Invalid d={d} or N={N}")
    if d == 4:
        return (N ** 2 - 1.0) / 4.0
    return (N ** 2 - 1.0) / (d * (d - 1.0))


def compute_single_step_transfer_bound(
    beta: float,
    loop_length_a: float,
    t_over_a2: float,
    d: int = 4,
    N: int = 3,
) -> Dict[str, float]:
    """
    Computes the exact analytical components of Theorem YM-011-T2:
    < | B^* W_1(C_1) - W_{0,t}(iota(C_1)) | >_{mu_0}
        <= ( C_tan(d, N) / beta + C_rem(d, N) * (t/a^2)^2 ) * (|C_1| / (2a)).
    """
    if beta <= 0.0:
        raise ValueError(f"Bare coupling beta must be positive, got {beta}")
    if loop_length_a <= 0.0:
        raise ValueError(f"Loop length in lattice units must be positive, got {loop_length_a}")
    if t_over_a2 < 0.0:
        raise ValueError(f"t/a^2 must be non-negative, got {t_over_a2}")
    if d < 2 or N < 2:
        raise ValueError(f"Invalid d={d} or N={N}")

    c_bulk = compute_bulk_plaquette_constant(d, N)
    
    # Tangent constant: 4(d-1) sqrt(N) * C_bulk
    # In d=4: 12 sqrt(N) * (N^2 - 1)/4 = 3 sqrt(N) (N^2 - 1)
    if N == 2 and d == 4:
        # Sharp SU(2) constant from exact operator-norm identity
        c_tan = 4.0 * (d - 1) * c_bulk  # 12 * 0.75 = 9.0
    else:
        c_tan = 4.0 * (d - 1) * math.sqrt(N) * c_bulk

    # Remainder constant: 4(d-1)^2 = 36 in d=4
    c_rem = 4.0 * ((d - 1) ** 2)

    # Number of coarse links: n1 = loop_length_a / 2
    n_coarse_links = loop_length_a / 2.0

    tangent_defect_bound = (c_tan / beta) * n_coarse_links
    remainder_bound = c_rem * (t_over_a2 ** 2) * n_coarse_links
    total_bound = tangent_defect_bound + remainder_bound

    return {
        "beta": beta,
        "g0_sq": 2.0 * N / beta,
        "n_coarse_links": n_coarse_links,
        "c_bulk": c_bulk,
        "c_tan": c_tan,
        "c_rem": c_rem,
        "e_plaq_bound": c_bulk / beta,
        "tangent_defect_bound": tangent_defect_bound,
        "remainder_bound": remainder_bound,
        "total_bound": total_bound,
    }


def compute_multiscale_geometric_sum(
    g0_sq: float,
    n_scales: int,
    d: int = 4,
    N: int = 3,
) -> Dict[str, Any]:
    """
    Computes the multiscale geometric sum of Theorem YM-011-T4:
    sum_{j=0}^{n_scales-1} 2^{-j} g_j^2
    where 1/g_j^2 = 1/g_0^2 - 2 b_0 j ln 2.
    """
    if g0_sq <= 0.0:
        raise ValueError(f"g0_sq must be positive, got {g0_sq}")
    if n_scales < 1:
        raise ValueError(f"n_scales must be >= 1, got {n_scales}")
    if d != 4:
        raise ValueError(f"Multiscale RG is formulated in d=4, got {d}")
    if N < 2:
        raise ValueError(f"Gauge group SU(N) requires N >= 2, got {N}")

    b0 = 11.0 * N / (48.0 * math.pi ** 2)
    inv_g0_sq = 1.0 / g0_sq

    gj_sq_list: List[float] = []
    step_error_weights: List[float] = []
    cumulative_sum = 0.0

    for j in range(n_scales):
        denom = inv_g0_sq - 2.0 * b0 * j * math.log(2.0)
        if denom <= 0.0:
            raise CrossoverBoundaryReached(
                f"Running coupling diverged at scale j={j}: nonperturbative crossover reached."
            )
        gj_sq = 1.0 / denom
        gj_sq_list.append(gj_sq)

        # Weight is 2^{-j} * g_j^2
        weight = (2.0 ** (-j)) * gj_sq
        step_error_weights.append(weight)
        cumulative_sum += weight

    # In the UV domain, ratio cumulative_sum / g0_sq is strictly bounded
    convergence_ratio = cumulative_sum / g0_sq

    return {
        "b0": b0,
        "g0_sq": g0_sq,
        "n_scales": n_scales,
        "running_couplings": gj_sq_list,
        "step_error_weights": step_error_weights,
        "cumulative_sum": cumulative_sum,
        "convergence_ratio": convergence_ratio,
        "is_geometrically_convergent": convergence_ratio < 4.0,
    }


def evaluate_crossover_stopping_diagnostic(
    g0_sq: float,
    g_star_sq: float = 0.64,
    d: int = 4,
    N: int = 3,
) -> Dict[str, Any]:
    """
    Evaluates the stopping scale where running coupling reaches the crossover boundary g_*^2.
    Documents NEG-YM-011-TRANSFER-2.
    """
    if g0_sq >= g_star_sq:
        raise ValueError(f"g0_sq ({g0_sq}) must be strictly less than g_star_sq ({g_star_sq})")

    b0 = 11.0 * N / (48.0 * math.pi ** 2)
    delta_inv_g = (1.0 / g0_sq) - (1.0 / g_star_sq)
    n_cross_exact = delta_inv_g / (2.0 * b0 * math.log(2.0))
    n_cross = int(math.floor(n_cross_exact))

    return {
        "b0": b0,
        "g0_sq": g0_sq,
        "g_star_sq": g_star_sq,
        "n_cross_exact": n_cross_exact,
        "n_cross": n_cross,
        "is_finite_uv_domain": n_cross > 0,
        "limitation": "NEG-YM-011-TRANSFER-2: UV scale transfer halts at n_cross; crossover unbridged.",
    }


def evaluate_bridge_lemma_guardrails(
    claim_mass_gap: bool = False,
    claim_clay_solved: bool = False,
    claim_continuum_limit: bool = False,
) -> bool:
    """
    Strict guardrail: YM-011 proves UV scale transfer, but CANNOT claim mass gap,
    continuum limit, or Clay Millennium Problem resolution.
    """
    if claim_mass_gap:
        raise ValueError("Epistemic violation: YM-011 does NOT prove a continuum mass gap.")
    if claim_clay_solved:
        raise ValueError("Epistemic violation: Clay Millennium Problem #4 remains OPEN_AND_UNSOLVED.")
    if claim_continuum_limit:
        raise ValueError("Epistemic violation: Full continuum limit requires crossover bridge (OPEN).")
    return True
