import pytest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"

YM008_ARTIFACTS = [
    "YM-008-HYBRID-ARCHITECTURE-SPECIFICATION.md",
    "YM-008-SCALE-INTERFACE-ANALYSIS.md",
    "YM-008-ADVERSARIAL-FALSIFICATION-PROTOCOL.md",
    "YM-008-LEAN-FORMALIZATION-BLUEPRINT.md",
    "YM-008-CANONICAL-STRATEGY-RECORD.md",
    "YM-008-FINAL-SYNTHESIS.md",
]


def test_01_all_canonical_literature_artifacts_exist():
    """Verify all 6 YM-008 canonical literature artifacts exist and have substantial content."""
    for filename in YM008_ARTIFACTS:
        path = LIT_DIR / filename
        assert path.exists(), f"Missing canonical artifact: {filename}"
        content = path.read_text(encoding="utf-8")
        assert len(content) > 500, f"Artifact {filename} is too short ({len(content)} chars)"


def test_02_clay_millennium_open_status_preserved():
    """Verify that Clay Millennium Problem #4 remains open across all YM-008 artifacts."""
    for filename in YM008_ARTIFACTS:
        content = (LIT_DIR / filename).read_text(encoding="utf-8")
        assert "proved 4d continuum yang-mills" not in content.lower()
        assert "solution to the clay millennium problem" not in content.lower()

    # Check canonical record explicitly
    record_content = (LIT_DIR / "YM-008-CANONICAL-STRATEGY-RECORD.md").read_text(encoding="utf-8")
    assert 'clay_millennium_problem_status: "OPEN_AND_UNSOLVED"' in record_content


def test_03_three_scale_partition_completeness():
    """Verify that all three physical scales (UV, Crossover, IR) are rigorously specified."""
    spec_content = (LIT_DIR / "YM-008-HYBRID-ARCHITECTURE-SPECIFICATION.md").read_text(encoding="utf-8")
    assert "Scale 1: Ultraviolet" in spec_content or "SCALE 1: ULTRAVIOLET" in spec_content
    assert "Scale 2: Intermediate Crossover" in spec_content or "SCALE 2: CROSSOVER" in spec_content
    assert "Scale 3: Infrared" in spec_content or "SCALE 3: INFRARED" in spec_content
    assert "0.15" in spec_content
    assert "0.50" in spec_content


def test_04_scale_interface_matching_equations():
    """Verify that explicit matching equations are formulated for both scale interfaces."""
    iface_content = (LIT_DIR / "YM-008-SCALE-INTERFACE-ANALYSIS.md").read_text(encoding="utf-8")
    assert "Interface 1" in iface_content
    assert "Interface 2" in iface_content
    assert "W_t(C)" in iface_content or "Flow-Regularized Wilson Loop" in iface_content
    assert "t(a) = c_0" in iface_content or "t(a)" in iface_content
    assert "sigma_bootstrap" in iface_content or "sigma" in iface_content


def test_05_adversarial_falsification_stress_tests():
    """Verify that all 5 adversarial stress tests are documented with explicit guardrails."""
    adv_content = (LIT_DIR / "YM-008-ADVERSARIAL-FALSIFICATION-PROTOCOL.md").read_text(encoding="utf-8")
    assert "Stress Test 1" in adv_content
    assert "Stress Test 2" in adv_content
    assert "Stress Test 3" in adv_content
    assert "Stress Test 4" in adv_content
    assert "Stress Test 5" in adv_content
    assert "OS3 Reflection Positivity Leakage" in adv_content
    assert "Gauge Invariance Anomaly" in adv_content
    assert "Feasibility Collapse" in adv_content


def test_06_os3_joint_scaling_guardrail():
    """Verify Invariant INV-YM008-002: Joint scaling t(a) = c_0 a^2 protects reflection positivity."""
    adv_content = (LIT_DIR / "YM-008-ADVERSARIAL-FALSIFICATION-PROTOCOL.md").read_text(encoding="utf-8")
    assert "t(a) = c_0" in adv_content
    assert "a^2" in adv_content


def test_07_finite_n_sdp_convex_relaxation():
    """Verify that finite-N Mandelstam constraints use relaxed convex SDP bounds."""
    adv_content = (LIT_DIR / "YM-008-ADVERSARIAL-FALSIFICATION-PROTOCOL.md").read_text(encoding="utf-8")
    assert "relaxed SDP" in adv_content or "convex" in adv_content.lower()


def test_08_lean4_formalization_blueprint():
    """Verify that Lean 4 signatures and micro-lemmas are specified."""
    blueprint_content = (LIT_DIR / "YM-008-LEAN-FORMALIZATION-BLUEPRINT.md").read_text(encoding="utf-8")
    assert "ScaleRegime" in blueprint_content
    assert "UVIntermediateInterface" in blueprint_content
    assert "IntermediateIRInterface" in blueprint_content
    assert "smearing_radius_vanishes" in blueprint_content
    assert "LEM-LEAN-01" in blueprint_content


def test_09_canonical_strategy_record_provenance():
    """Verify STRAT-REC-YM008-001 yaml structure and parameter provenance tags."""
    record_path = LIT_DIR / "YM-008-CANONICAL-STRATEGY-RECORD.md"
    content = record_path.read_text(encoding="utf-8")
    assert "PROJECT_ESTIMATE" in content
    assert "PRIMARY_SOURCE_RESULT" in content
    assert "HEURISTIC_PHYSICAL_TRANSLATION" in content
    assert "STRAT-REC-YM008-001" in content


def test_10_envelope_and_governance_conformance():
    """Verify YM-008 envelope exists, is active, and contract is registered in ledger."""
    env_path = GOV_DIR / "envelopes" / "YM-008.yaml"
    assert env_path.exists(), "YM-008 envelope must exist"
    env_data = yaml.safe_load(env_path.read_text(encoding="utf-8"))
    assert env_data["task_execution_envelope"]["identity"]["task_id"] == "YM-008"
    assert env_data["task_execution_envelope"]["classification"]["risk_tier"] == "R2"

    ledger_path = GOV_DIR / "CONTRACT_OWNERSHIP_LEDGER.yaml"
    ledger_data = yaml.safe_load(ledger_path.read_text(encoding="utf-8"))
    contract_ids = [c["contract_id"] for c in ledger_data["contracts"]]
    assert "CONTRACT-YM-008" in contract_ids, "CONTRACT-YM-008 must be registered in ledger"
