"""
Unit tests for Task YM-015R2: Exact RP Status Repair and Nonperturbative Flowed-Continuum Bridge.

Verifies:
1. Four-tier distinction in reflection positivity: heat kernel leakage vs absence of explicit counterexample.
2. Theorem YM-015-L3 reclassification to EXACT_RP_UNRESOLVED_FOR_FINITE_4D_FLOW_TIME.
3. Sub-result: STANDARD_HALF_SPACE_RP_INHERITANCE_FAILS_AS_A_PROOF_METHOD.
4. Excision of heuristic defect formula as CONJECTURAL_ERROR_MODEL.
5. Reclassification of Route C to CANDIDATE_LOCALITY_RECOVERY_ARCHITECTURE.
6. Spatial gradient flow slice-wise autonomy (Theorem YM-015-SPF1).
7. Exact reflection positivity for spatial flow on time slices (Theorem YM-015-SPF2, Criterion A).
8. Temporal locality taxonomy across candidate observable families.
9. Formal evaluation of exact RP recovery Criteria A, B, and C.
10. Target specification for YM-015F-TARGET and sub-edge E-UV-FLOWED.
"""

import pytest
import math

from src.ymmg.uv_continuum import (
    verify_reflection_positivity_support_buffer,
    evaluate_locality_replacement_routes,
    compute_heat_kernel_rp_defect,
)
from src.ymmg.spatial_flow import (
    evaluate_spatial_gradient_flow_locality,
    verify_spatial_flow_reflection_positivity,
    classify_observable_temporal_locality,
    evaluate_exact_rp_recovery_criteria,
    evaluate_fixed_flow_continuum_target_status,
)


def test_01_four_tier_rp_distinction():
    """Verify that heat-kernel leakage proves non-membership in A_+ but not falsification of RP."""
    res = verify_reflection_positivity_support_buffer(dist_to_hyperplane=0.5, t_phys=0.02)
    
    # Tier 1 & 2: Proved True
    assert res["in_standard_positive_time_algebra"] is False
    assert res["standard_rp_inheritance_applicable"] is False
    assert res["sub_result"] == "STANDARD_HALF_SPACE_RP_INHERITANCE_FAILS_AS_A_PROOF_METHOD"
    
    # Tier 3 & 4: Unproved / No Counterexample
    assert res["has_explicit_counterexample"] is False
    assert res["theorem_status"] == "EXACT_RP_UNRESOLVED_FOR_FINITE_4D_FLOW_TIME"


def test_02_conjectural_error_model_excision():
    """Verify that the schematic RP defect formula is classified as CONJECTURAL_ERROR_MODEL."""
    res = verify_reflection_positivity_support_buffer(dist_to_hyperplane=0.5, t_phys=0.02)
    assert res["rp_defect_model_status"] == "CONJECTURAL_ERROR_MODEL"
    
    routes = evaluate_locality_replacement_routes(t_phys=0.02, delta=0.5)
    assert routes["route_C_two_stage_limit"]["rp_defect_model_status"] == "CONJECTURAL_ERROR_MODEL"


def test_03_route_c_candidate_status():
    """Verify Route C is classified as CANDIDATE_LOCALITY_RECOVERY_ARCHITECTURE under Criterion B."""
    routes = evaluate_locality_replacement_routes(t_phys=0.02, delta=0.5)
    route_c = routes["route_C_two_stage_limit"]
    
    assert route_c["status"] == "CANDIDATE_LOCALITY_RECOVERY_ARCHITECTURE"
    assert route_c["recovery_criterion"] == "CRITERION_B"
    assert route_c["temporal_locality_at_finite_t"] == "EXPONENTIALLY_TIME_NONLOCAL"
    assert route_c["temporal_locality_at_t_zero"] == "STRICT_LOCAL"


def test_04_spatial_flow_slice_autonomy():
    """Verify Theorem YM-015-SPF1: Slice-Wise Autonomy of Spatial Gradient Flow."""
    spf = evaluate_spatial_gradient_flow_locality(time_slice=1.0)
    
    assert spf["temporal_locality"] == "STRICT_TIME_SLICE_LOCAL"
    assert spf["slice_wise_autonomy"] is True
    assert spf["functional_derivative_cross_slice"] == 0.0
    assert spf["functional_derivative_temporal_link"] == 0.0
    assert spf["so4_rotational_invariance"] is False
    assert spf["so3_spatial_invariance"] is True
    assert spf["theorem_ref"] == "YM-015-SPF1"


def test_05_spatial_flow_exact_rp():
    """Verify Theorem YM-015-SPF2: Exact Reflection Positivity of Spatial-Flow Observables."""
    # Positive time slice x_4 > 0
    pos_res = verify_spatial_flow_reflection_positivity(time_slice=0.5)
    assert pos_res["is_positive_half_space"] is True
    assert pos_res["in_positive_time_algebra"] is True
    assert pos_res["exact_reflection_positivity_preserved"] is True
    assert pos_res["heat_kernel_temporal_leakage"] == 0.0
    assert pos_res["os2_recovery_criterion"] == "CRITERION_A"
    assert pos_res["theorem_status"] == "SPATIAL_FLOW_RP_COMPATIBILITY_PROVED"
    assert pos_res["theorem_ref"] == "YM-015-SPF2"

    # Non-positive time slice x_4 <= 0
    neg_res = verify_spatial_flow_reflection_positivity(time_slice=-0.5)
    assert neg_res["is_positive_half_space"] is False
    assert neg_res["in_positive_time_algebra"] is False
    assert neg_res["exact_reflection_positivity_preserved"] is False


def test_06_observable_temporal_locality_taxonomy():
    """Verify temporal locality classification across all 4 candidate observable families."""
    f1 = classify_observable_temporal_locality("4d_gradient_flow")
    assert f1["locality_state"] == "EXPONENTIALLY_TIME_NONLOCAL"
    assert f1["so4_invariance"] is True
    assert f1["universal_finiteness_Z_is_1"] is True

    f2 = classify_observable_temporal_locality("spatial_gradient_flow")
    assert f2["locality_state"] == "STRICT_TIME_SLICE_LOCAL"
    assert f2["exact_lattice_rp"] == "EXACT (A in A_+ identically)"
    assert f2["so4_invariance"] is False

    f3 = classify_observable_temporal_locality("time_slice_spatial_loops")
    assert f3["locality_state"] == "STRICT_TIME_SLICE_LOCAL"
    assert f3["exact_lattice_rp"] == "EXACT (A in A_+ identically)"

    f4 = classify_observable_temporal_locality("bare_local_plaquette")
    assert f4["locality_state"] == "STRICT_TIME_SLICE_LOCAL"
    assert f4["universal_finiteness_Z_is_1"] is False  # UV divergent


def test_07_exact_rp_recovery_criteria():
    """Verify formal definitions and satisfaction of Criteria A, B, and C."""
    crit_a = evaluate_exact_rp_recovery_criteria("criterion_a")
    assert crit_a["criterion_id"] == "Criterion A"
    assert "spatial_gradient_flow" in crit_a["satisfied_by"]
    assert crit_a["status"] == "PROVED_FOR_SPATIAL_FLOW"

    crit_b = evaluate_exact_rp_recovery_criteria("criterion_b")
    assert crit_b["criterion_id"] == "Criterion B"
    assert "route_c_two_stage_limit" in crit_b["satisfied_by"]
    assert crit_b["status"] == "OPEN_RESEARCH_TARGET"

    crit_c = evaluate_exact_rp_recovery_criteria("criterion_c")
    assert crit_c["status"] == "UNPROVED / NO_THEOREM"


def test_08_fixed_flow_continuum_target():
    """Verify target specification and smallest missing estimate for YM-015F-TARGET."""
    target = evaluate_fixed_flow_continuum_target_status()
    assert target["target_id"] == "YM-015F-TARGET"
    assert target["sub_edge"] == "E-UV-FLOWED"
    assert "CONDITIONAL" in target["theorem_l1_status"]
    assert target["theorem_l2_status"] == "SUBSEQUENTIAL_MULTILINEAR_DISTRIBUTION_EXTRACTION"
    assert "Bałaban" in target["smallest_missing_estimate"]
    assert target["overall_status"] == "PARTIAL_PROGRESS"
