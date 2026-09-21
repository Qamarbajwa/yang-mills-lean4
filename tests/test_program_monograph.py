import pytest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"
FORMAL_DIR = ROOT / "formal" / "lean4" / "YangMills"

YM010_ARTIFACTS = [
    "YM-010-PROGRAM-MONOGRAPH-AND-SYNTHESIS.md",
    "YM-010-GLOBAL-THEOREM-AND-BRIDGE-CLOSURE.md",
    "YM-010-FORMAL-VERIFICATION-ROADMAP.md",
    "YM-010-CANONICAL-PROGRAM-RECORD.md",
]


def test_01_all_canonical_literature_artifacts_exist():
    """Verify all 4 YM-010 canonical literature artifacts exist and have substantial content."""
    for filename in YM010_ARTIFACTS:
        path = LIT_DIR / filename
        assert path.exists(), f"Missing canonical artifact: {filename}"
        content = path.read_text(encoding="utf-8")
        assert len(content) > 500, f"Artifact {filename} is too short ({len(content)} chars)"


def test_02_clay_millennium_open_status_strictly_preserved():
    """Verify that Clay Millennium Problem #4 remains open and unsolved across all YM-010 artifacts."""
    for filename in YM010_ARTIFACTS:
        content = (LIT_DIR / filename).read_text(encoding="utf-8")
        assert "proved 4d continuum yang-mills" not in content.lower()
        assert "solution to the clay millennium problem" not in content.lower()

    # Check canonical program record explicitly
    record_content = (LIT_DIR / "YM-010-CANONICAL-PROGRAM-RECORD.md").read_text(encoding="utf-8")
    assert 'clay_millennium_problem_status: "OPEN_AND_UNSOLVED"' in record_content


def test_03_program_monograph_foundations_and_axioms():
    """Verify that the monograph documents foundational axioms, historical eras, and mass gap."""
    content = (LIT_DIR / "YM-010-PROGRAM-MONOGRAPH-AND-SYNTHESIS.md").read_text(encoding="utf-8")
    assert "Jaffe & Witten" in content
    assert "Wightman" in content
    assert "Osterwalder" in content
    assert "\\Delta > 0" in content or "Delta > 0" in content
    assert "Foundational Era" in content
    assert "Constructive RG Era" in content
    assert "Modern Rigorous Advances" in content


def test_04_global_bridge_closure_matrix_completeness():
    """Verify that the global bridge closure matrix maps all 12 nodes and 19 edges with CLOSED status."""
    content = (LIT_DIR / "YM-010-GLOBAL-THEOREM-AND-BRIDGE-CLOSURE.md").read_text(encoding="utf-8")
    
    # 12 structural nodes
    nodes = [
        "N-SPEC", "N-FOUND", "N-CONSTRUCT", "N-ANALOGUE", "N-RG", "N-LATTICE",
        "N-GAP-LAT", "N-CROSSOVER", "N-MEASURE", "N-MASS-GAP", "N-RECONSTRUCT", "N-WIGHTMAN"
    ]
    for node in nodes:
        assert node in content, f"Node {node} missing from closure matrix"
    
    # 19 structural edges
    for i in range(1, 20):
        edge_id = f"E{i:02d}"
        assert edge_id in content, f"Edge {edge_id} missing from closure matrix"
    
    # Verify all edges are closed
    assert content.count("**CLOSED**") >= 19


def test_05_lean4_formal_verification_roadmap():
    """Verify that the Lean 4 roadmap audits all 5 modules and machine-checked theorems."""
    content = (LIT_DIR / "YM-010-FORMAL-VERIFICATION-ROADMAP.md").read_text(encoding="utf-8")
    assert "ClaySpecification.lean" in content
    assert "WightmanAxioms.lean" in content
    assert "OsterwalderSchraderAxioms.lean" in content
    assert "MissingBridgeDAG.lean" in content
    assert "HybridStrategy.lean" in content
    assert "bridge_graph_is_acyclic" in content
    assert "spectral_gap_strictly_positive" in content


def test_06_canonical_program_record_structure_and_provenance():
    """Verify PROG-REC-YM010-001 yaml structure, milestone ledger, and parameter provenance."""
    record_path = LIT_DIR / "YM-010-CANONICAL-PROGRAM-RECORD.md"
    content = record_path.read_text(encoding="utf-8")
    assert "PROG-REC-YM010-001" in content
    assert "programme_milestone_ledger" in content
    assert "structural_metrics" in content
    assert "Parameter Provenance" in content
    assert "PROJECT_ESTIMATE" in content
    assert "PRIMARY_SOURCE_RESULT" in content
    assert "HEURISTIC_PHYSICAL_TRANSLATION" in content


def test_07_closed_world_fingerprint_synchronization():
    """Verify that all 4 YM-010 literature files are registered in both classification YAML and ros.py."""
    from src.ymmg.ros import SCIENTIFIC_FINGERPRINT_MANIFEST

    class_path = GOV_DIR / "SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml"
    with open(class_path, "r", encoding="utf-8") as f:
        class_data = yaml.safe_load(f)

    registered_yaml = set(class_data["scientific_fingerprint"]["paths"])
    registered_py = set(SCIENTIFIC_FINGERPRINT_MANIFEST)

    assert len(registered_yaml) == 94
    assert len(registered_py) == 94

    for filename in YM010_ARTIFACTS:
        rel_path = f"literature/{filename}"
        assert rel_path in registered_yaml, f"Missing from classification YAML: {rel_path}"
        assert rel_path in registered_py, f"Missing from ros.py manifest: {rel_path}"


def test_08_governance_envelope_ym010_integrity():
    """Verify governance envelope governance/envelopes/YM-010.yaml exists and enforces invariants."""
    env_path = GOV_DIR / "envelopes" / "YM-010.yaml"
    assert env_path.exists()
    with open(env_path, "r", encoding="utf-8") as f:
        env_data = yaml.safe_load(f)

    env = env_data["task_execution_envelope"]
    assert env["identity"]["task_id"] == "YM-010"
    assert env["classification"]["risk_tier"] == "R2"
    assert env["classification"]["action_class"] == "B"

    invariant_ids = [inv["id"] for inv in env["execution"]["invariants"]]
    assert "INV-YM010-001" in invariant_ids
    assert "INV-YM010-002" in invariant_ids
    assert "INV-YM010-003" in invariant_ids
    assert "INV-YM010-004" in invariant_ids
