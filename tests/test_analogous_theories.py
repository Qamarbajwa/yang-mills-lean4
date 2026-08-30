import pytest
import yaml
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANA_DIR = ROOT / "literature" / "primary" / "solved_modified_analogous"
MANIFEST_PATH = ANA_DIR / "manifest.yaml"
MATRIX_PATH = ROOT / "literature" / "ANALOGUE_MECHANISM_MATRIX.md"
LIM_MATRIX_PATH = ROOT / "literature" / "ANALOGUE_LIMITATION_MATRIX.md"
DEP_GRAPH_PATH = ROOT / "literature" / "ANALOGUE_DEPENDENCY_GRAPH.md"
PATHWAY_PATH = ROOT / "literature" / "PATHWAY_MEMORY_REGISTER.md"
THEOREM_PATH = ROOT / "THEOREM_LEDGER.md"


def load_manifest():
    assert MANIFEST_PATH.exists(), "manifest.yaml must exist"
    data = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
    assert data["packet"] == "YM-002D"
    return data["sources"]


def test_manifest_sources_and_hashes():
    sources = load_manifest()
    assert len(sources) == 10, f"Must have exactly 10 analogue sources, found {len(sources)}"
    for s in sources:
        rec_path = ANA_DIR / s["local_file"]
        assert rec_path.exists(), f"Source file {rec_path} must exist"
        import hashlib
        actual_sha = hashlib.sha256(rec_path.read_bytes()).hexdigest()
        assert actual_sha == s["sha256"], f"Hash mismatch for {s['source_id']}"
        record = rec_path.read_text(encoding="utf-8")
        assert "RESULT_SCOPE:" in record
        assert "- **COMPLETE_SOLUTION_STATUS:** `DOES_NOT_CONSTITUTE_COMPLETE_CLAY_SOLUTION`" in record


def test_dr1_semantic_errata_preserves_scope_and_clay_non_sufficiency():
    sources = {s["source_id"]: s for s in load_manifest()}
    assert sources["PAPER-ANA-007"]["evidence_class"] == "SUPERCONFORMAL_QFT_WITH_EXACT_PROTECTED_AND_ALL_ORDER_RESULTS"
    assert sources["PAPER-ANA-008"]["evidence_class"] == "GAUGE_HIGGS_LATTICE_ANALYTICITY_AND_HIGGS_MASS_RESULT"
    assert sources["PAPER-ANA-009"]["evidence_class"] == "PROCA_EXPLICIT_MASS_STUECKELBERG_GAUGE_REFORMULATION"

    theorem_text = THEOREM_PATH.read_text(encoding="utf-8")
    analogue_block = theorem_text[theorem_text.index("THM-YM-0031"):]
    assert analogue_block.count("- **COMPLETE_SOLUTION_STATUS:** `DOES_NOT_CONSTITUTE_COMPLETE_CLAY_SOLUTION`") == 10
    assert "EXACT_CFT_SOLUTION" not in analogue_block
    assert "Fradkin–Shenker prove analyticity along a specified path" in analogue_block
    assert "Proca gives classical massive spin-1 equations" in analogue_block

    pathway_text = PATHWAY_PATH.read_text(encoding="utf-8")
    assert pathway_text.count("- **COMPLETE_SOLUTION_STATUS:** `DOES_NOT_CONSTITUTE_COMPLETE_CLAY_SOLUTION`") == 10
    assert "EXACT_RESULT != COMPLETE_SOLUTION_OF_THEORY" in pathway_text
    assert "EXACT_RESULT != COMPLETE_CLAY_SOLUTION" in pathway_text


def test_analogue_theorems_in_ledger():
    content = THEOREM_PATH.read_text(encoding="utf-8")
    for i in range(31, 41):
        thm_id = f"THM-YM-00{i}"
        assert thm_id in content, f"Theorem {thm_id} must be in THEOREM_LEDGER.md"
        assert f"- **THEOREM_ID:** `{thm_id}`" in content
        assert "- **TRANSFER_BARRIER:**" in content
        assert "- **TRANSFERABLE_COMPONENT:**" in content
        assert "- **NONTRANSFERABLE_COMPONENT:**" in content
        assert "- **BRIDGE_VARIABLES:**" in content
        assert "- **FAILURE_LOCALITY:**" in content


def test_analogue_mechanism_matrix():
    assert MATRIX_PATH.exists()
    content = MATRIX_PATH.read_text(encoding="utf-8")
    for i in range(1, 11):
        p_id = f"PATH-ANA-00{i}" if i < 10 else f"PATH-ANA-0{i}"
        assert p_id in content, f"Pathway {p_id} must be in ANALOGUE_MECHANISM_MATRIX.md"


def test_analogue_limitation_matrix_all_no():
    assert LIM_MATRIX_PATH.exists()
    content = LIM_MATRIX_PATH.read_text(encoding="utf-8")
    for i in range(31, 41):
        thm_id = f"THM-YM-00{i}"
        assert thm_id in content
        line = [l for l in content.splitlines() if thm_id in l][0]
        assert "NO (" in line, f"Row {thm_id} must have CLAY_SUFFICIENT: NO"


def test_analogue_dependency_graph():
    assert DEP_GRAPH_PATH.exists()
    content = DEP_GRAPH_PATH.read_text(encoding="utf-8")
    assert "flowchart TD" in content
    for i in range(31, 41):
        assert f"THM-YM-00{i}" in content


def test_pathway_memory_register_analogue_pathways_and_resonances():
    assert PATHWAY_PATH.exists()
    content = PATHWAY_PATH.read_text(encoding="utf-8")
    for i in range(1, 11):
        p_id = f"PATH-ANA-00{i}" if i < 10 else f"PATH-ANA-0{i}"
        assert p_id in content, f"Pathway {p_id} must be in PATHWAY_MEMORY_REGISTER.md"
        assert f"- **PATHWAY_ID:** `{p_id}`" in content
        assert "- **TRANSFER_BARRIER:**" in content
        assert "- **TRANSFERABLE_COMPONENT:**" in content
        assert "- **NONTRANSFERABLE_COMPONENT:**" in content
        assert "- **REOPEN_CONDITIONS:**" in content
        assert "- **OUTCOME_FINGERPRINT:**" in content

    # Check Permanent Invariants 16 to 28
    assert "EXACTLY_SOLVABLE != RIGOROUS_QFT_CONSTRUCTION" in content
    assert "2D_YM != 4D_YM" in content
    assert "LARGE_N != FINITE_N" in content
    assert "SUPERSYMMETRIC_RESULT != PURE_YM_RESULT" in content
    assert "SEIBERG_WITTEN_EXACT_CONTROL != RIGOROUS_CONSTRUCTION_OF_PURE_YM4" in content
    assert "HIGGS_MASS != DYNAMICAL_PURE_YM_MASS_GAP" in content
    assert "EXPLICIT_LAGRANGIAN_MASS != DYNAMICALLY_GENERATED_SPECTRAL_GAP" in content
    assert "PERTURBATIVE_FINITENESS != NONPERTURBATIVE_CONSTRUCTION" in content
    assert "S_DUALITY != PROVED_CLAY_THEOREM" in content
    assert "ADS_CFT != CLAY_PROOF" in content
    assert "HOLOGRAPHIC_SPECTRUM != RIGOROUS_YM4_SPECTRUM" in content
    assert "SEMICLASSICAL_CONFINEMENT != RIGOROUS_GENERAL_CONFINEMENT" in content
    assert "ANALOGUE_SUCCESS != TRANSFERABILITY_TO_PURE_YM" in content

    # Check Resonances
    assert "RES-PATH-001" in content
    assert "RES-PATH-002" in content
    assert "RES-PATH-003" in content
    assert "RES-PATH-004" in content
