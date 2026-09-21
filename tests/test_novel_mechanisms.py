import pytest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"

YM007_ARTIFACTS = [
    "YM-007-EVALUATION-FRAMEWORK.md",
    "YM-007-GEOMETRIC-FLOW-EVALUATION.md",
    "YM-007-STOCHASTIC-QUANTIZATION-EVALUATION.md",
    "YM-007-LOOP-EQUATIONS-EVALUATION.md",
    "YM-007-TOPOLOGICAL-CONDENSATION-EVALUATION.md",
    "YM-007-EXACT-RG-EVALUATION.md",
    "YM-007-COMPARATIVE-MECHANISM-MATRIX.md",
    "YM-007-CANONICAL-MECHANISM-RECORD.md",
    "YM-007-FINAL-SYNTHESIS.md",
]


def test_01_all_canonical_literature_artifacts_exist():
    """Verify all 9 YM-007 canonical literature artifacts exist and have substantial content."""
    for filename in YM007_ARTIFACTS:
        path = LIT_DIR / filename
        assert path.exists(), f"Missing canonical artifact: {filename}"
        content = path.read_text(encoding="utf-8")
        assert len(content) > 500, f"Artifact {filename} is too short ({len(content)} chars)"


def test_02_clay_millennium_open_status_preserved():
    """Verify that Clay Millennium Problem #4 remains open across all YM-007 artifacts."""
    for filename in YM007_ARTIFACTS:
        content = (LIT_DIR / filename).read_text(encoding="utf-8")
        assert "CLAY SUFFICIENT: YES" not in content.upper()
        # Verify no claims that the Clay problem is solved
        assert "proved 4d continuum yang-mills" not in content.lower()
        assert "solution to the clay millennium problem" not in content.lower()

    # Check canonical record explicitly
    record_content = (LIT_DIR / "YM-007-CANONICAL-MECHANISM-RECORD.md").read_text(encoding="utf-8")
    assert 'clay_millennium_problem_status: "OPEN_AND_UNSOLVED"' in record_content


def test_03_all_five_mechanisms_evaluated():
    """Verify that all five candidate mechanisms (MECH-01 to MECH-05) are evaluated."""
    matrix_content = (LIT_DIR / "YM-007-COMPARATIVE-MECHANISM-MATRIX.md").read_text(encoding="utf-8")
    for mech_id in ["MECH-01", "MECH-02", "MECH-03", "MECH-04", "MECH-05"]:
        assert mech_id in matrix_content, f"Mechanism {mech_id} missing from comparative matrix"

    record_content = (LIT_DIR / "YM-007-CANONICAL-MECHANISM-RECORD.md").read_text(encoding="utf-8")
    for mech_id in ["MECH-01", "MECH-02", "MECH-03", "MECH-04", "MECH-05"]:
        assert f'mechanism_id: "{mech_id}"' in record_content, f"Mechanism {mech_id} missing from canonical record"


def test_04_all_eight_criteria_evaluated():
    """Verify that all eight rigorous mathematical criteria (CRIT-01 to CRIT-08) are defined and evaluated."""
    framework_content = (LIT_DIR / "YM-007-EVALUATION-FRAMEWORK.md").read_text(encoding="utf-8")
    matrix_content = (LIT_DIR / "YM-007-COMPARATIVE-MECHANISM-MATRIX.md").read_text(encoding="utf-8")

    for i in range(1, 9):
        crit_id = f"CRIT-0{i}"
        assert crit_id in framework_content, f"Criterion {crit_id} missing from evaluation framework"
        assert crit_id in matrix_content, f"Criterion {crit_id} missing from comparative matrix"


def test_05_barrier_localization_integrity():
    """Verify that every mechanism has an explicit mathematical barrier and failure locality identified."""
    matrix_content = (LIT_DIR / "YM-007-COMPARATIVE-MECHANISM-MATRIX.md").read_text(encoding="utf-8")
    assert "E-CROSSOVER" in matrix_content
    assert "E-LATTICE-CONT" in matrix_content
    assert "Failure Locality" in matrix_content
    assert "Primary Mathematical Barrier" in matrix_content


def test_06_smearing_vs_measure_generation_distinction():
    """Verify Invariant INV-YM007-003: Lüscher flow is recognized as operator smearing, not measure generation."""
    flow_content = (LIT_DIR / "YM-007-GEOMETRIC-FLOW-EVALUATION.md").read_text(encoding="utf-8")
    assert "not generate" in flow_content.lower() or "not define an independent probability measure" in flow_content.lower()
    assert "OS3" in flow_content or "reflection positivity" in flow_content.lower()
    assert "Lüscher" in flow_content or "Luscher" in flow_content


def test_07_spde_4d_criticality_barrier():
    """Verify that 4D stochastic quantization explicitly documents the failure of local subcriticality."""
    spde_content = (LIT_DIR / "YM-007-STOCHASTIC-QUANTIZATION-EVALUATION.md").read_text(encoding="utf-8")
    assert "subcriticality" in flow_safe(spde_content)
    assert "4D Criticality Wall" in spde_content or "critical" in flow_safe(spde_content)
    assert "-3" in spde_content or "-d/2" in spde_content or "parabolic" in spde_content.lower()
    assert "Chandra" in spde_content
    assert "Chevyrev" in spde_content
    assert "Hairer" in spde_content


def test_08_loop_equations_contact_term_barrier():
    """Verify that loop equations explicitly document continuum contact-term singularities."""
    loop_content = (LIT_DIR / "YM-007-LOOP-EQUATIONS-EVALUATION.md").read_text(encoding="utf-8")
    assert "contact" in loop_content.lower()
    assert "Makeenko" in loop_content
    assert "Migdal" in loop_content
    assert "Kazakov" in loop_content
    assert "Zheng" in loop_content
    assert "Mandelstam" in loop_content


def test_09_vortex_sheet_action_divergence_barrier():
    """Verify that topological condensation documents singular sheet action divergence and area law vs gap distinction."""
    vortex_content = (LIT_DIR / "YM-007-TOPOLOGICAL-CONDENSATION-EVALUATION.md").read_text(encoding="utf-8")
    assert "diverg" in vortex_content.lower()
    assert "thickness" in vortex_content.lower()
    assert "'t Hooft" in vortex_content or "t Hooft" in vortex_content
    assert "Mack" in vortex_content
    assert "area law" in vortex_content.lower()


def test_10_erg_truncation_error_barrier():
    """Verify that functional RG documents the truncation error barrier and modified Slavnov-Taylor identities."""
    erg_content = (LIT_DIR / "YM-007-EXACT-RG-EVALUATION.md").read_text(encoding="utf-8")
    assert "truncation" in erg_content.lower()
    assert "Wetterich" in erg_content
    assert "mSTI" in erg_content or "Slavnov" in erg_content or "Ward" in erg_content


def test_11_canonical_mechanism_record_provenance():
    """Verify MECH-REC-YM007-001 yaml structure and parameter provenance tags."""
    record_path = LIT_DIR / "YM-007-CANONICAL-MECHANISM-RECORD.md"
    content = record_path.read_text(encoding="utf-8")
    assert "PROJECT_ESTIMATE" in content
    assert "PRIMARY_SOURCE_RESULT" in content
    assert "HEURISTIC_PHYSICAL_TRANSLATION" in content
    assert "MECH-REC-YM007-001" in content


def test_12_envelope_and_governance_conformance():
    """Verify YM-007 envelope exists, is active, and contract is registered in ledger."""
    env_path = GOV_DIR / "envelopes" / "YM-007.yaml"
    assert env_path.exists(), "YM-007 envelope must exist"
    env_data = yaml.safe_load(env_path.read_text(encoding="utf-8"))
    assert env_data["task_execution_envelope"]["identity"]["task_id"] == "YM-007"
    assert env_data["task_execution_envelope"]["classification"]["risk_tier"] == "R2"

    ledger_path = GOV_DIR / "CONTRACT_OWNERSHIP_LEDGER.yaml"
    ledger_data = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
    contract_ids = [c["contract_id"] for c in ledger_data["contracts"]]
    assert "CONTRACT-YM-007" in contract_ids, "CONTRACT-YM-007 must be registered in ledger"


def flow_safe(text: str) -> str:
    """Helper to lowercase text without special character issues."""
    return text.lower()
