import re
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATHWAY_PATH = ROOT / "literature" / "PATHWAY_MEMORY_REGISTER.md"
TASK_GRAPH_PATH = ROOT / "TASK_GRAPH.md"
NEGATIVE_EVIDENCE_PATH = ROOT / "NEGATIVE_EVIDENCE_REGISTER.md"

def test_pathway_memory_file_exists():
    assert PATHWAY_PATH.exists(), "PATHWAY_MEMORY_REGISTER.md must exist"

def test_pathway_governing_invariants_present():
    content = PATHWAY_PATH.read_text(encoding="utf-8")
    assert "FAILED_EXPERIMENT != FALSIFIED_PATHWAY" in content
    assert "NO_KNOWN_EXTENSION != PROVED_NONEXTENDABILITY" in content
    assert "SOURCE_STATED_LIMITATION != PROJECT_SYNTHESIS" in content
    assert "DORMANT_PATHWAY != SCIENTIFICALLY_DEAD_PATHWAY" in content

def test_pathway_epistemic_tags_defined_and_used():
    content = PATHWAY_PATH.read_text(encoding="utf-8")
    tags = [
        "[PRIMARY_SOURCE_RESULT]",
        "[PRIMARY_SOURCE_LIMITATION]",
        "[LATER_LITERATURE_LIMITATION]",
        "[PROJECT_SYNTHESIS]",
    ]
    for tag in tags:
        assert tag in content, f"Tag {tag} must be present in PATHWAY_MEMORY_REGISTER.md"

def test_path_const_001_monopole_loop_geometry_accuracy():
    content = PATHWAY_PATH.read_text(encoding="utf-8")
    assert "SOLVED_LOWER_DIMENSIONAL_ANALOGUE_UNEXTENDABLE_TO_4D" not in content,         "Unjustified absolute unextendability fingerprint must not be present"
    assert "SOLVED_LOWER_DIMENSIONAL_ABELIAN_ANALOGUE_NO_DIRECT_EXTENSION_ESTABLISHED_TO_4D_NONABELIAN_YM" in content
    assert "1D closed worldlines / current loops" in content
    assert "Dirac sheets" in content

def test_negative_evidence_register_monopole_accuracy():
    content = NEGATIVE_EVIDENCE_PATH.read_text(encoding="utf-8")
    assert "1D closed worldlines / current loops" in content
    assert "2D Dirac sheets" in content

def test_mrs_pathway_exact_locators_and_epistemic_separation():
    content = PATHWAY_PATH.read_text(encoding="utf-8")
    assert "p. 326" in content
    assert "[PRIMARY_SOURCE_LIMITATION]" in content
    assert "[LATER_LITERATURE_LIMITATION]" in content or "[PROJECT_SYNTHESIS]" in content

def test_balaban_pathway_epistemic_separation():
    content = PATHWAY_PATH.read_text(encoding="utf-8")
    assert "PATH-CONST-002" in content
    assert "[PRIMARY_SOURCE_RESULT]" in content
    assert "[PRIMARY_SOURCE_LIMITATION]" in content

def test_task_graph_ym002_subtask_completeness():
    content = TASK_GRAPH_PATH.read_text(encoding="utf-8")
    assert "YM-002 | Build theorem/literature ledger | YM-001R1 | T2 | primary literature + theorem-level extraction | IN_PROGRESS" in content
    for st in ["YM-002A", "YM-002AR1", "YM-002B", "YM-002BR1", "YM-002C", "YM-002CR1", "YM-002CR2", "YM-002CR2A", "YM-002D", "YM-002E", "YM-002F"]:
        assert st in content, f"Subtask {st} must be present in TASK_GRAPH.md"
    assert any(
        s in content for s in [
            "YM-003 | Construct missing-bridge graph | YM-002F | T3 | independent semantic review | READY",
            "YM-003 | Construct missing-bridge graph | YM-002F | T3 | independent semantic review | IN_PROGRESS",
            "YM-003 | Construct missing-bridge graph | YM-002F | T3 | independent semantic review | AWAITING_HUMAN_ACCEPTANCE"
        ]
    )

def test_analogue_pathways_epistemic_structure():
    content = PATHWAY_PATH.read_text(encoding="utf-8")
    allowed_evidence_classes = [
        "RIGOROUS_MATHEMATICAL_CONSTRUCTION",
        "RIGOROUS_MATHEMATICAL_THEOREM",
        "EXACTLY_SOLVABLE_PHYSICS_MODEL",
        "EXACT_SUPERSYMMETRIC_PHYSICS_RESULT",
        "SUPERCONFORMAL_QFT_WITH_EXACT_PROTECTED_AND_ALL_ORDER_RESULTS",
        "SEMICLASSICAL_MECHANISM",
        "PROCA_EXPLICIT_MASS_STUECKELBERG_GAUGE_REFORMULATION",
        "GAUGE_HIGGS_LATTICE_ANALYTICITY_AND_HIGGS_MASS_RESULT",
        "DUALITY_BASED_RESULT",
        "HOLOGRAPHIC_CONJECTURAL_ANALOGUE",
        "PROJECT_SYNTHESIS",
        "UNKNOWN"
    ]
    for i in range(1, 11):
        p_id = f"PATH-ANA-00{i}" if i < 10 else f"PATH-ANA-0{i}"
        assert p_id in content, f"Pathway {p_id} must be in PATHWAY_MEMORY_REGISTER.md"
        assert f"- **PATHWAY_ID:** `{p_id}`" in content
        assert "- **TRANSFER_BARRIER:**" in content
        assert "- **TRANSFERABLE_COMPONENT:**" in content
        assert "- **NONTRANSFERABLE_COMPONENT:**" in content
        assert "- **REOPEN_CONDITIONS:**" in content
        assert "- **OUTCOME_FINGERPRINT:**" in content
