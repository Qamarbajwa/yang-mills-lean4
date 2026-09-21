import pytest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"
FORMAL_DIR = ROOT / "formal" / "lean4" / "YangMills"

YM009_ARTIFACTS = [
    "YM-009-QUANTITATIVE-BOOTSTRAP-EXECUTION.md",
    "YM-009-SCALE-GLUING-ANALYSIS.md",
    "YM-009-SPECTRUM-AND-STRING-TENSION-BOUNDS.md",
    "YM-009-CONTINUUM-LIMIT-ROBUSTNESS.md",
    "YM-009-CANONICAL-QUANTITATIVE-RECORD.md",
    "YM-009-FINAL-SYNTHESIS.md",
]


def test_01_all_canonical_literature_artifacts_exist():
    """Verify all 6 YM-009 canonical literature artifacts exist and have substantial content."""
    for filename in YM009_ARTIFACTS:
        path = LIT_DIR / filename
        assert path.exists(), f"Missing canonical artifact: {filename}"
        content = path.read_text(encoding="utf-8")
        assert len(content) > 500, f"Artifact {filename} is too short ({len(content)} chars)"


def test_02_clay_millennium_open_status_preserved():
    """Verify that Clay Millennium Problem #4 remains open across all YM-009 artifacts."""
    for filename in YM009_ARTIFACTS:
        content = (LIT_DIR / filename).read_text(encoding="utf-8")
        assert "proved 4d continuum yang-mills" not in content.lower()
        assert "solution to the clay millennium problem" not in content.lower()

    # Check canonical record explicitly
    record_content = (LIT_DIR / "YM-009-CANONICAL-QUANTITATIVE-RECORD.md").read_text(encoding="utf-8")
    assert 'clay_millennium_problem_status: "OPEN_AND_UNSOLVED"' in record_content


def test_03_sdp_loop_bootstrap_formulation():
    """Verify that the SDP loop bootstrap formulation specifies moment matrix positivity and constraints."""
    content = (LIT_DIR / "YM-009-QUANTITATIVE-BOOTSTRAP-EXECUTION.md").read_text(encoding="utf-8")
    assert "\\mathcal{M}(t) \\succeq 0" in content or "M(t)" in content
    assert "Makeenko" in content
    assert "Mandelstam" in content
    assert "Joint Scaling" in content or "joint scaling" in content.lower()
    assert "t(a) = c_0" in content


def test_04_scale_gluing_theorems_and_bounds():
    """Verify that explicit non-perturbative gluing theorems are formulated for both scale interfaces."""
    content = (LIT_DIR / "YM-009-SCALE-GLUING-ANALYSIS.md").read_text(encoding="utf-8")
    assert "Interface 1" in content
    assert "Interface 2" in content
    assert "Theorem 1" in content
    assert "Theorem 2" in content
    assert "O(a^2" in content or "a^2" in content
    assert "epsilon_{matching}" in content or "\\epsilon_{\\text{matching}}" in content
    assert "Reflection Positivity (OS3)" in content or "OS3" in content


def test_05_strictly_positive_mass_gap_bound():
    """Verify that scalar glueball mass and spectral mass gap bounds are strictly positive."""
    content = (LIT_DIR / "YM-009-SPECTRUM-AND-STRING-TENSION-BOUNDS.md").read_text(encoding="utf-8")
    assert "\\Delta > 0" in content or "Delta > 0" in content
    assert "Theorem 3" in content
    assert "1.40" in content or "1.43" in content
    assert "M_{0^{++}}" in content or "M_0++" in content
    assert "String Tension" in content or "string tension" in content.lower()


def test_06_continuum_limit_robustness_and_os_axioms():
    """Verify that all 5 Osterwalder-Schrader axioms (OS0-OS4) are evaluated in the continuum limit."""
    content = (LIT_DIR / "YM-009-CONTINUUM-LIMIT-ROBUSTNESS.md").read_text(encoding="utf-8")
    assert "Axiom OS0" in content
    assert "Axiom OS1" in content
    assert "Axiom OS2" in content
    assert "Axiom OS3" in content
    assert "Axiom OS4" in content
    assert "SATISFIED" in content
    assert "Wightman" in content


def test_07_lean4_formal_module_structure():
    """Verify that Lean 4 formal module formal/lean4/YangMills/HybridStrategy.lean exists and exports declarations."""
    lean_file = FORMAL_DIR / "HybridStrategy.lean"
    assert lean_file.exists()
    content = lean_file.read_text(encoding="utf-8")
    assert "inductive ScaleRegime" in content
    assert "structure ScaleBoundaries" in content
    assert "def classifyScale" in content
    assert "structure UVIntermediateInterface" in content
    assert "theorem smearing_radius_vanishes" in content
    assert "structure IntermediateIRInterface" in content
    assert "structure LoopMomentMatrix" in content
    assert "structure SpectralGapContract" in content
    assert "theorem spectral_gap_strictly_positive" in content

    # Check that it is imported in root YangMills.lean
    root_lean = ROOT / "formal" / "lean4" / "YangMills.lean"
    assert "import YangMills.HybridStrategy" in root_lean.read_text(encoding="utf-8")


def test_08_canonical_quantitative_record_provenance():
    """Verify QUANT-REC-YM009-001 yaml structure and parameter provenance tags."""
    record_path = LIT_DIR / "YM-009-CANONICAL-QUANTITATIVE-RECORD.md"
    content = record_path.read_text(encoding="utf-8")
    assert "QUANT-REC-YM009-001" in content
    assert "PROJECT_ESTIMATE" in content
    assert "HEURISTIC_PHYSICAL_TRANSLATION" in content
    assert "Parameter Provenance Audit Table" in content


def test_09_closed_world_fingerprint_synchronization():
    """Verify that all 6 YM-009 literature files are registered in both classification YAML and ros.py."""
    from src.ymmg.ros import SCIENTIFIC_FINGERPRINT_MANIFEST

    class_path = GOV_DIR / "SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml"
    with open(class_path, "r", encoding="utf-8") as f:
        class_data = yaml.safe_load(f)

    registered_yaml = set(class_data["scientific_fingerprint"]["paths"])
    registered_py = set(SCIENTIFIC_FINGERPRINT_MANIFEST)

    for filename in YM009_ARTIFACTS:
        rel_path = f"literature/{filename}"
        assert rel_path in registered_yaml, f"Missing from classification YAML: {rel_path}"
        assert rel_path in registered_py, f"Missing from ros.py manifest: {rel_path}"


def test_10_governance_envelope_ym009_integrity():
    """Verify governance envelope governance/envelopes/YM-009.yaml exists and enforces invariants."""
    env_path = GOV_DIR / "envelopes" / "YM-009.yaml"
    assert env_path.exists()
    with open(env_path, "r", encoding="utf-8") as f:
        env_data = yaml.safe_load(f)

    env = env_data["task_execution_envelope"]
    assert env["identity"]["task_id"] == "YM-009"
    assert env["classification"]["risk_tier"] == "R2"
    assert env["classification"]["action_class"] == "B"

    invariant_ids = [inv["id"] for inv in env["execution"]["invariants"]]
    assert "INV-YM009-001" in invariant_ids
    assert "INV-YM009-002" in invariant_ids
    assert "INV-YM009-003" in invariant_ids
    assert "INV-YM009-004" in invariant_ids
