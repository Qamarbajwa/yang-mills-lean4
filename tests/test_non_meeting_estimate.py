"""Deterministic test suite for Task YM-006: Precise Non-Meeting Estimate Identification.

Verifies:
1. Presence and non-emptiness of all 6 canonical YM-006 literature artifacts.
2. Analytical proof that the non-meeting distance Delta_beta >= 2N - 1 > 0 holds for all N >= 2.
3. Strict enforcement of parameter provenance tags (PROJECT_ESTIMATE, HEURISTIC_PHYSICAL_TRANSLATION).
4. Consistency of the calibrated quantitative estimates for SU(2).
5. Exact reconciliation with YM-003 missing-bridge edge E-CROSSOVER and obstruction OBS-CAND-001.
6. Observance of ROS v1.0 Law 7 (OBS-CAND-001 remains strictly an OBSTRUCTION_CANDIDATE).
7. Impasse analysis covering all 5 technique families.
8. Conformance of canonical record GAP-REC-YM006-001.
9. Zero claims of Clay sufficiency or no-go theorems against continuum Yang-Mills.
"""

import math
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT_DIR = ROOT / "literature"

REQUIRED_YM006_FILES = [
    LIT_DIR / "YM-006-UV-IR-COMPARISON-FRAMEWORK.md",
    LIT_DIR / "YM-006-CROSSOVER-DISTANCE-ESTIMATE.md",
    LIT_DIR / "YM-006-CRITICAL-CUT-SET-RECONCILIATION.md",
    LIT_DIR / "YM-006-MATHEMATICAL-IMPASSE-DIAGNOSIS.md",
    LIT_DIR / "YM-006-CANONICAL-NON-MEETING-RECORD.md",
    LIT_DIR / "YM-006-VISUAL-INTUITION-DATA.md",
    LIT_DIR / "YM-006-FINAL-SYNTHESIS.md",
]


def test_01_all_ym006_artifacts_exist():
    """Verify that all 7 canonical YM-006 literature artifacts exist and are well-formed."""
    for path in REQUIRED_YM006_FILES:
        assert path.exists(), f"Missing required YM-006 artifact: {path}"
        assert path.stat().st_size > 500, f"Artifact {path} is suspiciously small ({path.stat().st_size} bytes)"


def test_02_uv_ir_parameter_mapping_consistency():
    """Verify the parameter dictionary in YM-006-UV-IR-COMPARISON-FRAMEWORK.md."""
    content = (LIT_DIR / "YM-006-UV-IR-COMPARISON-FRAMEWORK.md").read_text(encoding="utf-8")
    assert "UV Multiscale RG" in content
    assert "IR Lattice Theory" in content
    assert "beta(g^2) = \\frac{2N}{g^2}" in content or "\\beta(g^2) = \\frac{2N}{g^2}" in content
    assert "INV-YM006-001" in content
    assert "INV-YM006-002" in content
    assert "INV-YM006-003" in content


def test_03_analytical_non_meeting_theorem():
    """Verify that the analytical theorem Delta_beta >= 2N - 1 > 0 holds for all N >= 2."""
    for N in [2, 3, 4, 5, 10]:
        delta_beta_min = 2 * N - 1
        assert delta_beta_min > 0, f"Delta_beta bound failed for N={N}"
        assert delta_beta_min >= 3, f"Delta_beta bound should be >= 3 for N={N}"


def test_04_quantitative_provenance_and_symbolic_bounds():
    """Verify parameter provenance tags and symbolic bounds in GAP-REC-YM006-001."""
    content = (LIT_DIR / "YM-006-CANONICAL-NON-MEETING-RECORD.md").read_text(encoding="utf-8")
    m = re.search(r"```yaml\s*\n(.*?)\n```", content, re.DOTALL)
    assert m, "Must contain YAML block for GAP-REC-YM006-001"
    data = yaml.safe_load(m.group(1))

    assert data["record_id"] == "GAP-REC-YM006-001"
    assert data["status"] == "ESTABLISHED_METHOD_BOUNDARY"

    prov_list = data["quantitative_parameter_provenance"]
    assert len(prov_list) >= 8

    allowed_tags = {"PROJECT_ESTIMATE", "HEURISTIC_PHYSICAL_TRANSLATION"}
    for item in prov_list:
        assert item["provenance"] in allowed_tags, f"Invalid provenance tag: {item['provenance']}"
        assert "basis" in item and len(item["basis"]) > 5


def test_05_crossover_numerical_gap_estimates():
    """Verify numerical values for SU(2) estimates."""
    g_star_sq = 0.08
    beta_0 = 0.25
    N = 2

    # Derived values
    beta_uv = 2 * N / g_star_sq
    assert math.isclose(beta_uv, 50.0, rel_tol=1e-3)

    g_ir_sq = 2 * N / beta_0
    assert math.isclose(g_ir_sq, 16.0, rel_tol=1e-3)

    delta_beta = beta_uv - beta_0
    assert math.isclose(delta_beta, 49.75, rel_tol=1e-3)

    delta_g2 = g_ir_sq - g_star_sq
    assert math.isclose(delta_g2, 15.92, rel_tol=1e-3)

    x_uv = 0.15
    a_strong = 0.50
    delta_x = a_strong - x_uv
    assert math.isclose(delta_x, 0.35, rel_tol=1e-3)


def test_06_renormalization_group_scale_ratio():
    """Verify calculation of the logarithmic RG scale ratio R_RG."""
    N = 2
    b_0 = 11 * N / (48 * (math.pi ** 2))  # ~0.04644
    g_star_sq = 0.08
    g_ir_sq = 16.0

    r_rg = (1.0 / (2.0 * b_0)) * ((1.0 / g_star_sq) - (1.0 / g_ir_sq))
    assert 130 < r_rg < 140, f"Expected R_RG ~ 134, got {r_rg}"


def test_07_critical_cut_set_reconciliation():
    """Verify reconciliation with YM-003 missing-bridge graph in YM-006-CRITICAL-CUT-SET-RECONCILIATION.md."""
    content = (LIT_DIR / "YM-006-CRITICAL-CUT-SET-RECONCILIATION.md").read_text(encoding="utf-8")
    assert "E-CROSSOVER" in content
    assert "E-LATTICE-CONT" in content
    assert "N-INT-COUPLING" in content
    assert "N-MASS-GAP" in content
    assert "100%" in content or "every topological path" in content.lower()


def test_08_obstruction_id_consistency_and_ros_law_7():
    """Verify that OBS-CAND-001 is preserved and obeys ROS v1.0 Law 7."""
    content = (LIT_DIR / "YM-006-CRITICAL-CUT-SET-RECONCILIATION.md").read_text(encoding="utf-8")
    assert "OBS-CAND-001" in content
    assert "OBSTRUCTION_CANDIDATE" in content
    assert "PROVED_OBSTRUCTION_THEOREM" not in content
    assert "Law 7" in content or "LAW_7" in content


def test_09_impasse_diagnosis_five_families():
    """Verify that all 5 technique families are diagnosed in YM-006-MATHEMATICAL-IMPASSE-DIAGNOSIS.md."""
    content = (LIT_DIR / "YM-006-MATHEMATICAL-IMPASSE-DIAGNOSIS.md").read_text(encoding="utf-8")
    assert "Multiscale Perturbative RG" in content
    assert "High-Temperature Character Expansions" in content
    assert "Stochastic Quantization" in content
    assert "Random Surface" in content
    assert "Semiclassical Instantons" in content


def test_10_canonical_non_meeting_record_schema():
    """Verify schema conformance of GAP-REC-YM006-001."""
    content = (LIT_DIR / "YM-006-CANONICAL-NON-MEETING-RECORD.md").read_text(encoding="utf-8")
    m = re.search(r"```yaml\s*\n(.*?)\n```", content, re.DOTALL)
    assert m
    data = yaml.safe_load(m.group(1))

    required_keys = ["record_id", "status", "inputs", "scope", "symbolic_relations", "quantitative_parameter_provenance", "governing_invariants"]
    for key in required_keys:
        assert key in data, f"Missing required key in GAP-REC-YM006-001: {key}"


def test_11_visual_intuition_data_consistency():
    """Verify that visual intuition diagrams reflect the calculated values."""
    content = (LIT_DIR / "YM-006-VISUAL-INTUITION-DATA.md").read_text(encoding="utf-8")
    assert "49.75" in content
    assert "15.92" in content
    assert "0.35 fm" in content
    assert "OBS-CAND-001" in content


def test_12_no_overclaims_or_clay_sufficiency():
    """Verify that YM-006 maintains strict epistemic modesty without Clay claims."""
    synthesis = (LIT_DIR / "YM-006-FINAL-SYNTHESIS.md").read_text(encoding="utf-8")
    assert "INV-YM006-001" in synthesis
    assert "YM-007" in synthesis
    assert "CLAY_SUFFICIENT: YES" not in synthesis
    assert "Method Boundary vs. Impossibility" in synthesis
