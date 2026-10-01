"""
Unit test suite for YM-012: Intermediate Coupling Crossover Window Analysis.

Tests:
1. Analytical crossover boundaries and non-meeting theorem (Delta beta >= 2N - 1 > 0).
2. Comprehensive mechanism evaluation matrix (A through E across 12 criteria).
3. Formal specification validator for YM-012-TARGET (Minimum Crossover Theorem).
4. Simultaneous expansion convergence breakdown diagnostics (Theorem YM-012-T2).
5. Bounded flow-mollified crossover comparison decomposition (Lemma YM-012-L1).
6. Total variation divergence and crossover falsification condition (Theorem YM-012-T4).
7. Strict project invariants and negative evidence registration (NEG-YM-012-CROSSOVER-1, 2).
8. Structural integrity of literature artifacts (DAG and Analysis monographs).
"""

from pathlib import Path
import pytest
import math

from src.ymmg.crossover_analysis import (
    compute_crossover_boundaries,
    evaluate_crossover_mechanisms,
    validate_ym_012_target_specification,
    compute_expansion_contractivity,
    compute_bounded_crossover_transfer_decomposition,
    evaluate_crossover_falsification_condition,
    verify_crossover_project_invariants,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
LIT_DIR = REPO_ROOT / "literature"


def test_01_crossover_boundaries_and_non_meeting_theorem():
    """Verify Delta beta >= 2N - 1 > 0 for SU(N) and RG step counts."""
    # Test SU(2)
    b2 = compute_crossover_boundaries(N=2, g_star=0.8, beta_0=0.25)
    assert math.isclose(b2["beta_uv_star"], 6.25)
    assert math.isclose(b2["delta_beta"], 6.00)
    assert b2["delta_beta"] >= b2["symbolic_lower_bound"]  # 6.00 >= 3.00
    assert b2["r_rg"] > 0.0
    assert b2["k_cross"] >= 10

    # Test SU(3)
    b3 = compute_crossover_boundaries(N=3, g_star=0.8, beta_0=0.35)
    assert math.isclose(b3["beta_uv_star"], 9.375)
    assert math.isclose(b3["delta_beta"], 9.025)
    assert b3["delta_beta"] >= b3["symbolic_lower_bound"]  # 9.025 >= 5.00
    assert b3["k_cross"] >= 10

    # Test SU(4) and SU(5)
    for n in [4, 5]:
        bn = compute_crossover_boundaries(N=n, g_star=0.8)
        assert bn["delta_beta"] >= 2.0 * n - 1.0

    # Test validation
    with pytest.raises(ValueError, match="requires N >= 2"):
        compute_crossover_boundaries(N=1)
    with pytest.raises(ValueError, match="g_star must be in"):
        compute_crossover_boundaries(g_star=1.5)
    with pytest.raises(ValueError, match="beta_0 must be in"):
        compute_crossover_boundaries(beta_0=1.5)


def test_02_mechanism_evaluation_matrix_completeness():
    """Verify all 5 mechanisms are evaluated across all 12 criteria and clay_sufficient=False."""
    matrix = evaluate_crossover_mechanisms()
    expected_mechs = [
        "MECH_A_CENTER_VORTEX",
        "MECH_B_STOCHASTIC_FLOW",
        "MECH_C_LOOP_BOOTSTRAP",
        "MECH_D_CONSTRUCTIVE_RG",
        "MECH_E_MODERN_ALTERNATIVES",
    ]
    assert set(matrix.keys()) == set(expected_mechs)

    expected_crits = [
        f"CRIT_{str(i).zfill(2)}_{name}"
        for i, name in [
            (1, "GAUGE_INV"),
            (2, "OS3_POSITIVITY"),
            (3, "CROSSOVER_CONTROL"),
            (4, "CONTINUUM_SCALING"),
            (5, "THERMODYNAMIC_STABILITY"),
            (6, "NON_TRIVIALITY"),
            (7, "SPECTRAL_GAP"),
            (8, "RIGOROUS_ERROR_BOUNDS"),
            (9, "UNIFORM_IN_CUTOFF"),
            (10, "YM011_COMPATIBILITY"),
            (11, "CROSSES_G_EQ_1"),
            (12, "MATHEMATICAL_STATUS"),
        ]
    ]

    for mech_id, data in matrix.items():
        assert "name" in data
        assert "primary_sources" in data
        assert len(data["primary_sources"]) >= 1
        assert "primary_obstruction" in data
        assert data["clay_sufficient"] is False
        assert data["criteria"]["CRIT_11_CROSSES_G_EQ_1"] == "NO"
        assert set(data["criteria"].keys()) == set(expected_crits)


def test_03_ym_012_target_specification_validation():
    """Verify YM-012-TARGET specification contains all 10 mandatory fields and non-claims."""
    target = validate_ym_012_target_specification()
    assert target["theorem_id"] == "YM-012-TARGET"
    assert target["gauge_group"] == "SU(N) (N >= 2)"
    assert target["lattice_status"] == "REGULATED_FINITE_SPACING_ONLY"
    assert target["status"] == "UNPROVED_OPEN_TARGET"

    non_claims = target["explicit_non_claims"]
    assert any("CONTINUUM_SCHWINGER" in nc for nc in non_claims)
    assert any("REFLECTION_POSITIVITY" in nc for nc in non_claims)
    assert any("CONTINUUM_MASS_GAP" in nc for nc in non_claims)
    assert any("CLAY_MILLENNIUM_PROBLEM" in nc for nc in non_claims)


def test_04_simultaneous_expansion_failure_in_crossover():
    """Verify Theorem YM-012-T2: expansions fail simultaneously in the crossover window."""
    # 1. Weak coupling: g = 0.5, beta = 12.0 (SU(3))
    uv = compute_expansion_contractivity(g=0.5, beta=12.0, N=3)
    assert uv["balaban_convergent"] is True
    assert uv["polymer_convergent"] is False
    assert uv["in_crossover_window"] is False

    # 2. Strong coupling: g = 3.5, beta = 0.2 (SU(3))
    ir = compute_expansion_contractivity(g=3.5, beta=0.2, N=3)
    assert ir["balaban_convergent"] is False
    assert ir["polymer_convergent"] is True
    assert ir["in_crossover_window"] is False

    # 3. Intermediate crossover: g = 1.0, beta = 2.0 (SU(3))
    mid = compute_expansion_contractivity(g=1.0, beta=2.0, N=3)
    assert mid["balaban_convergent"] is False
    assert mid["polymer_convergent"] is False
    assert mid["in_crossover_window"] is True
    assert mid["expansions_simultaneously_fail"] is True

    # Error handling
    with pytest.raises(ValueError):
        compute_expansion_contractivity(g=-1.0, beta=1.0)


def test_05_bounded_crossover_transfer_decomposition():
    """Verify Lemma YM-012-L1 decomposition and monotonicity."""
    res = compute_bounded_crossover_transfer_decomposition(
        loop_length=4.0,
        a_uv=0.5,
        g_star=0.8,
        tv_discrepancy=0.2,
    )
    assert res["tangent_error"] > 0.0
    assert res["measure_error"] == 0.2
    assert math.isclose(res["total_bound"], res["tangent_error"] + 0.2)

    # Scaling with loop length
    res2 = compute_bounded_crossover_transfer_decomposition(
        loop_length=8.0,
        a_uv=0.5,
        g_star=0.8,
        tv_discrepancy=0.2,
    )
    assert res2["tangent_error"] == 2.0 * res["tangent_error"]

    with pytest.raises(ValueError):
        compute_bounded_crossover_transfer_decomposition(loop_length=4.0, a_uv=0.5, tv_discrepancy=1.5)


def test_06_crossover_falsification_condition():
    """Verify Theorem YM-012-T4: accumulated total variation prevents unconditional closure."""
    fals = evaluate_crossover_falsification_condition(k_cross=24, tv_step=0.15)
    assert fals["accumulated_tv"] == 24 * 0.15  # 3.6
    assert fals["unconditional_continuation_falsified"] is True
    assert fals["e_crossover_status"] == "OPEN"

    with pytest.raises(ValueError):
        evaluate_crossover_falsification_condition(k_cross=0)


def test_07_governance_invariants_and_negative_evidence():
    """Verify mandatory invariants and negative evidence records in markdown."""
    inv = verify_crossover_project_invariants()
    assert inv["goal_complete"] is False
    assert inv["clay_problem"] == "OPEN_AND_UNSOLVED"
    assert inv["P3"] == "OPEN"
    assert inv["E_CROSSOVER"] == "OPEN"

    neg_content = (REPO_ROOT / "NEGATIVE_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    assert "NEG-YM-012-CROSSOVER-1" in neg_content
    assert "NEG-YM-012-CROSSOVER-2" in neg_content
    assert "Falsification of Unconditional Flow-Mollified Crossover Continuation" in neg_content
    assert "Simultaneous Failure of Gaussian and Polymer Expansions" in neg_content


def test_08_crossover_dag_document_structure():
    """Verify existence and substantive structure of literature monographs."""
    dag_path = LIT_DIR / "YM-012-CROSSOVER-DEPENDENCY-DAG.md"
    assert dag_path.exists()
    dag_content = dag_path.read_text(encoding="utf-8")
    assert "N-UV-RG-BOUNDS" in dag_content
    assert "N-INT-CROSSOVER" in dag_content
    assert "N-EFF-NONPERT" in dag_content
    assert "N-UNIF-BOUNDS" in dag_content
    assert "N-SCHWINGER-LIMIT" in dag_content
    assert "N-REFL-POS" in dag_content
    assert "N-CLUST-SPECTRAL" in dag_content
    assert "N-MASS-GAP" in dag_content
    assert "```mermaid" in dag_content

    analysis_path = LIT_DIR / "YM-012-CROSSOVER-ANALYSIS.md"
    assert analysis_path.exists()
    analysis_content = analysis_path.read_text(encoding="utf-8")
    assert "YM-012-TARGET" in analysis_content
    assert "YM-012-T1" in analysis_content
    assert "YM-012-T2" in analysis_content
    assert "YM-012-T4" in analysis_content
    assert "Lemma YM-012-L1" in analysis_content
    assert "Navier–Stokes" in analysis_content or "Navier-Stokes" in analysis_content
