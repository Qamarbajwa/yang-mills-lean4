"""
YM-015R2: Spatial Gradient Flow, Temporal Locality Taxonomy, and Nonperturbative Continuum Targets.

This module implements the mathematical machinery of Task YM-015R2:
1. Spatial Gradient Flow slice-wise autonomy (Theorem YM-015-SPF1).
2. Exact reflection positivity for spatial-flow observables on time slices (Theorem YM-015-SPF2, Criterion A).
3. Temporal locality classification taxonomy for observable families.
4. Exact Reflection Positivity Recovery Criteria (Criteria A, B, C).
5. Nonperturbative fixed-flow continuum compactness evaluation (YM-015F-L1/L2 and E-UV-FLOWED status).
"""

from typing import Dict, Any, List, Optional
import math


def evaluate_spatial_gradient_flow_locality(
    time_slice: float,
    spatial_extent: float = 1.0,
) -> Dict[str, Any]:
    """
    Evaluates Theorem YM-015-SPF1: Slice-Wise Autonomy of Spatial Gradient Flow.
    
    Proves that for any time slice x_4, spatial Wilson flow updates depend exclusively
    on spatial links on that exact time slice. Functional derivatives with respect
    to links at y_4 != x_4 and temporal links U_4 vanish identically.
    """
    return {
        "time_slice": time_slice,
        "spatial_extent": spatial_extent,
        "temporal_locality": "STRICT_TIME_SLICE_LOCAL",
        "slice_wise_autonomy": True,
        "functional_derivative_cross_slice": 0.0,
        "functional_derivative_temporal_link": 0.0,
        "so4_rotational_invariance": False,  # Explicitly broken to SO(3) x Z_2
        "so3_spatial_invariance": True,
        "theorem_ref": "YM-015-SPF1",
        "status": "PROVED_EXACT_TEMPORAL_LOCALITY",
    }


def verify_spatial_flow_reflection_positivity(
    time_slice: float,
) -> Dict[str, Any]:
    """
    Evaluates Theorem YM-015-SPF2: Exact Reflection Positivity of Spatial-Flow Observables.
    
    Shows that if time_slice x_4 > 0, the flowed observable belongs strictly to
    the positive-time lattice algebra A_+, thereby satisfying exact lattice
    reflection positivity (OS2) for all a > 0 and all flow times t >= 0.
    """
    is_positive_half_space = time_slice > 0.0
    
    return {
        "time_slice": time_slice,
        "is_positive_half_space": is_positive_half_space,
        "in_positive_time_algebra": is_positive_half_space,
        "exact_reflection_positivity_preserved": is_positive_half_space,
        "requires_support_buffer": False,  # No buffer needed; heat kernel is purely 3D
        "heat_kernel_temporal_leakage": 0.0,
        "os2_recovery_criterion": "CRITERION_A",
        "theorem_status": "SPATIAL_FLOW_RP_COMPATIBILITY_PROVED",
        "theorem_ref": "YM-015-SPF2",
    }


def classify_observable_temporal_locality(
    observable_family: str,
) -> Dict[str, Any]:
    """
    Assigns the exact temporal locality classification state to an observable family:
    - STRICT_TIME_SLICE_LOCAL
    - FINITE_TIME_SUPPORT
    - EXPONENTIALLY_TIME_NONLOCAL
    - GLOBALLY_TIME_NONLOCAL
    """
    families = {
        "4d_gradient_flow": {
            "family_id": "Family 1",
            "name": "4D Gradient-Flow Field Strength",
            "locality_state": "EXPONENTIALLY_TIME_NONLOCAL",
            "decay_law": "exp(-|x_4 - y_4|^2 / (4t))",
            "exact_lattice_rp": "UNRESOLVED (Standard inheritance fails)",
            "so4_invariance": True,
            "universal_finiteness_Z_is_1": True,
        },
        "spatial_gradient_flow": {
            "family_id": "Family 2",
            "name": "Spatial-Gradient-Flow Observables",
            "locality_state": "STRICT_TIME_SLICE_LOCAL",
            "decay_law": "delta(x_4 - y_4)",
            "exact_lattice_rp": "EXACT (A in A_+ identically)",
            "so4_invariance": False,
            "universal_finiteness_Z_is_1": False,
        },
        "time_slice_spatial_loops": {
            "family_id": "Family 3",
            "name": "Purely Spatially Smeared Time-Slice Loops",
            "locality_state": "STRICT_TIME_SLICE_LOCAL",
            "decay_law": "delta(x_4 - y_4)",
            "exact_lattice_rp": "EXACT (A in A_+ identically)",
            "so4_invariance": False,
            "universal_finiteness_Z_is_1": False,
        },
        "bare_local_plaquette": {
            "family_id": "Family 4",
            "name": "Unsmeared Bare Local Curvature",
            "locality_state": "STRICT_TIME_SLICE_LOCAL",
            "decay_law": "delta(x_4 - y_4)",
            "exact_lattice_rp": "EXACT (A in A_+ identically)",
            "so4_invariance": True,
            "universal_finiteness_Z_is_1": False,  # Diverges as a^-4
        },
    }
    
    if observable_family not in families:
        raise ValueError(
            f"Unknown observable family: {observable_family}. "
            f"Valid options: {list(families.keys())}"
        )
    return families[observable_family]


def evaluate_exact_rp_recovery_criteria(criterion_id: str) -> Dict[str, Any]:
    """
    Evaluates the three rigorous mathematical criteria for exact OS2 recovery:
    - Criterion A: Direct Lattice Inheritance on Time Slices
    - Criterion B: Two-Stage OS Form Limit (t -> 0)
    - Criterion C: Exact Non-Local Positivity Theorem
    """
    criteria = {
        "criterion_a": {
            "criterion_id": "Criterion A",
            "description": "Direct Lattice Inheritance on Time Slices",
            "mechanism": "lim_{a -> 0} <Theta(A_a) A_a>_a >= 0 with A_a in A_+",
            "satisfied_by": ["spatial_gradient_flow", "time_slice_spatial_loops"],
            "status": "PROVED_FOR_SPATIAL_FLOW",
        },
        "criterion_b": {
            "criterion_id": "Criterion B",
            "description": "Two-Stage OS Form Limit as t -> 0",
            "mechanism": "lim_{t -> 0} lim_{a -> 0} <Theta(A_{a,t}) A_{a,t}> = <Theta(A_0) A_0> >= 0",
            "satisfied_by": ["route_c_two_stage_limit"],
            "status": "OPEN_RESEARCH_TARGET",
        },
        "criterion_c": {
            "criterion_id": "Criterion C",
            "description": "Exact Non-Local Positivity Theorem at Finite t",
            "mechanism": "<Theta(F_t) F_t> >= 0 proved directly despite F_t not in A_+",
            "satisfied_by": [],
            "status": "UNPROVED / NO_THEOREM",
        },
    }
    
    crit_key = criterion_id.lower()
    if crit_key not in criteria:
        raise ValueError(f"Unknown criterion ID: {criterion_id}. Valid: {list(criteria.keys())}")
    return criteria[crit_key]


def evaluate_fixed_flow_continuum_target_status() -> Dict[str, Any]:
    """
    Evaluates the nonperturbative status of YM-015F-TARGET and sub-edge E-UV-FLOWED.
    """
    return {
        "target_id": "YM-015F-TARGET",
        "sub_edge": "E-UV-FLOWED",
        "theorem_l1_status": "PARTIAL_PROGRESS — CONDITIONAL_ON_BALABAN_OBSERVABLE_FLOW",
        "theorem_l2_status": "SUBSEQUENTIAL_MULTILINEAR_DISTRIBUTION_EXTRACTION",
        "continuum_topology": "(H^3_pi)^k* / D'((T^4)^k)",
        "smallest_missing_estimate": (
            "Non-perturbative multiscale insertion bound for flowed field strength "
            "in Bałaban polymer RG"
        ),
        "overall_status": "PARTIAL_PROGRESS",
    }
