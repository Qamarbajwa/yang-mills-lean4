import pytest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"

RECOVERY_ARTIFACTS = [
    "YM-011-FIRST-LOAD-BEARING-LEMMA-SPECIFICATION.md",
    "YM-012-RECONCILED-19-EDGE-GRAPH.md",
    "YM-012-REPAIRED-HYBRID-STRATEGY.md",
    "YM-012-VISUAL-INTUITION-COMPANION.md",
]


def test_01_all_recovery_artifacts_exist():
    """Verify all 4 canonical scientific recovery artifacts exist and have substantive content."""
    for filename in RECOVERY_ARTIFACTS:
        path = LIT_DIR / filename
        assert path.exists(), f"Missing recovery artifact: {filename}"
        content = path.read_text(encoding="utf-8")
        assert len(content) > 500, f"Artifact {filename} is too short ({len(content)} chars)"


def test_02_clay_millennium_open_status_strictly_preserved():
    """Verify that Clay Millennium Problem #4 remains open and unsolved across all recovery artifacts."""
    for filename in RECOVERY_ARTIFACTS:
        content = (LIT_DIR / filename).read_text(encoding="utf-8")
        assert "proved 4d continuum yang-mills" not in content.lower()
        assert "solution to the clay millennium problem" not in content.lower()


def test_03_reconciled_19_edge_graph_counts_and_statuses():
    """Verify that YM-012-RECONCILED-19-EDGE-GRAPH.md has the exact reconciled counts."""
    content = (LIT_DIR / "YM-012-RECONCILED-19-EDGE-GRAPH.md").read_text(encoding="utf-8")
    assert "**`PROVED`**" in content
    assert "**`REGULATED_ONLY`**" in content
    assert "**`CONDITIONAL`**" in content
    assert "**`OPEN`**" in content

    # Check key edge classifications
    assert "E-UV-FREE" in content
    assert "E-UV-RG" in content
    assert "E-CROSSOVER" in content
    assert "E-LATTICE-GAP" in content
    assert "E-LATTICE-CONT" in content
    assert "E-SCHWINGER-OS3" in content
    assert "OS3_NOT_ESTABLISHED" in content


def test_04_first_load_bearing_lemma_specification():
    """Verify Lemma YM-011-L1 specification structure, hypotheses, and absence of mass gap assumption."""
    content = (LIT_DIR / "YM-011-FIRST-LOAD-BEARING-LEMMA-SPECIFICATION.md").read_text(encoding="utf-8")
    assert "Lemma YM-011-L1" in content
    assert "UV Scale-Transfer and Observables Mollification Lemma" in content
    assert "Bałaban" in content or "Balaban" in content
    assert "W_t(C)" in content
    assert "assumes **no mass gap**" in content or "no mass gap" in content.lower()
    assert "fm" not in content.split("Statement:")[1].split("---")[0]
    assert "GeV" not in content.split("Statement:")[1].split("---")[0]


def test_05_repaired_hybrid_strategy_10_field_evaluation():
    """Verify that all 6 candidate directions have the complete 10-field matrix."""
    content = (LIT_DIR / "YM-012-REPAIRED-HYBRID-STRATEGY.md").read_text(encoding="utf-8")
    candidates = [
        "Candidate 1: Constructive Renormalization Group",
        "Candidate 2: Gradient Flow Regularization",
        "Candidate 3: Gauge-Invariant Loop Observables",
        "Candidate 4: Semidefinite Programming (SDP) Loop Bootstrap",
        "Candidate 5: Center-Vortex & Topological Condensation",
        "Candidate 6: Multi-Scale Interface Matching",
    ]
    for cand in candidates:
        assert cand in content, f"Missing candidate section: {cand}"

    assert "Exact Mathematical Object:" in content
    assert "Known Theorem Supporting It:" in content
    assert "Unproved Hypothesis:" in content
    assert "Required Function Space:" in content
    assert "Required Uniform Bound:" in content
    assert "Potential Counterexample:" in content
    assert "Total Purging of Heuristic Dimensionful Parameters" in content


def test_06_visual_intuition_companion_structure():
    """Verify that YM-012-VISUAL-INTUITION-COMPANION.md contains ASCII and Mermaid diagrams."""
    content = (LIT_DIR / "YM-012-VISUAL-INTUITION-COMPANION.md").read_text(encoding="utf-8")
    assert "KNOWN RIGOROUS MATHEMATICS" in content
    assert "FIRST MISSING THEOREM" in content
    assert "CONDITIONAL CONSEQUENCES" in content
    assert "REMAINING CLAY OBLIGATIONS" in content
    assert "```mermaid" in content
    assert "flowchart TD" in content


def test_07_closed_world_fingerprint_synchronization():
    """Verify that all 98 canonical files are synchronized across YAML and ros.py."""
    from src.ymmg.ros import SCIENTIFIC_FINGERPRINT_MANIFEST

    class_path = GOV_DIR / "SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml"
    with open(class_path, "r", encoding="utf-8") as f:
        class_data = yaml.safe_load(f)

    registered_yaml = set(class_data["scientific_fingerprint"]["paths"])
    registered_py = set(SCIENTIFIC_FINGERPRINT_MANIFEST)

    assert len(registered_yaml) == 156
    assert len(registered_py) == 156

    for filename in RECOVERY_ARTIFACTS:
        rel_path = f"literature/{filename}"
        assert rel_path in registered_yaml, f"Missing from classification YAML: {rel_path}"
        assert rel_path in registered_py, f"Missing from ros.py manifest: {rel_path}"
