import pytest
from pathlib import Path
import yaml
import re

ROOT = Path(__file__).resolve().parents[1]
LIT_DIR = ROOT / "literature"

from ymmg.bridge_graph import (
    parse_edge_records,
    validate_edge_record,
    validate_proof_dependency_dag,
    compute_critical_cut_sets,
    ALLOWED_EDGE_STATUSES,
    ALLOWED_ASSUMPTION_STATUSES,
    REQUIRED_EDGE_FIELDS,
    REQUIRED_SCOPE_FIELDS,
    REQUIRED_PHYSICAL_SCALE_FIELDS,
    BridgeGraphValidationError
)


@pytest.fixture(scope="module")
def edge_records():
    register_path = LIT_DIR / "BRIDGE_EDGE_REGISTER.md"
    assert register_path.exists(), "literature/BRIDGE_EDGE_REGISTER.md must exist"
    content = register_path.read_text(encoding="utf-8")
    records = parse_edge_records(content)
    assert len(records) >= 18, f"Expected at least 18 edge records, got {len(records)}"
    return records


def test_edge_schema_completeness(edge_records):
    """Every edge record must adhere strictly to schema requirements."""
    for r in edge_records:
        validate_edge_record(r)
        
        # Verify required fields
        for field in REQUIRED_EDGE_FIELDS:
            assert field in r, f"Edge {r.get('EDGE_ID')} missing required field: {field}"
            
        # Verify scope
        scope = r["SCOPE"]
        for field in REQUIRED_SCOPE_FIELDS:
            assert field in scope, f"Edge {r.get('EDGE_ID')} SCOPE missing required field: {field}"
            
        # Verify physical scale
        pscale = r["PHYSICAL_SCALE"]
        for field in REQUIRED_PHYSICAL_SCALE_FIELDS:
            assert field in pscale, f"Edge {r.get('EDGE_ID')} PHYSICAL_SCALE missing: {field}"
            
        # Verify status taxonomy
        assert r["PRIMARY_STATUS"] in ALLOWED_EDGE_STATUSES


def test_assumption_transfers_rigor(edge_records):
    """Ensure all assumption transfers are accounted for and discharges are justified."""
    for r in edge_records:
        for a in r.get("ASSUMPTION_TRANSFERS", []):
            st = a["STATUS"]
            assert st in ALLOWED_ASSUMPTION_STATUSES
            if st == "DISCHARGED":
                assert a.get("DISCHARGED_BY"), f"Edge {r['EDGE_ID']} assumption {a.get('ASSUMPTION')} discharged without DISCHARGED_BY"
                assert a.get("DISCHARGE_EVIDENCE"), f"Edge {r['EDGE_ID']} assumption {a.get('ASSUMPTION')} discharged without DISCHARGE_EVIDENCE"


def test_proof_dependency_dag_is_acyclic(edge_records):
    """Proof dependencies must form a strictly acyclic directed graph."""
    validate_proof_dependency_dag(edge_records)


def test_critical_cut_sets_decomposition(edge_records):
    """Critical cut-set analysis must detect no proved path to mass gap."""
    cut_analysis = compute_critical_cut_sets(edge_records)
    
    assert cut_analysis["total_paths_count"] > 0, "Graph must contain directed paths from regularizers to target"
    assert cut_analysis["is_connected_by_proved_only"] is False, "Target must NOT be connected entirely by PROVED edges"
    assert len(cut_analysis["open_edges_on_paths"]) > 0, "Path chokepoints must be identified"
    
    # Specific chokepoints
    open_edges = cut_analysis["open_edges_on_paths"]
    assert "E-CROSSOVER" in open_edges or "E-CONT-SCHWINGER" in open_edges
    assert "E-SCHWINGER-OS4" in open_edges


def test_non_promotion_epistemic_invariants(edge_records):
    """Strictly verify that unproved steps are never marked PROVED."""
    records_by_id = {r["EDGE_ID"]: r for r in edge_records}
    
    # Crossover window g_k ~ 1
    assert records_by_id["E-CROSSOVER"]["PRIMARY_STATUS"] == "OPEN"
    assert records_by_id["E-CROSSOVER"]["OBSTRUCTION_CANDIDATE"] == "OBS-CAND-001"
    
    # Thermodynamic limit in continuum
    assert records_by_id["E-THERMO"]["PRIMARY_STATUS"] == "OPEN"
    assert records_by_id["E-THERMO"]["OBSTRUCTION_CANDIDATE"] in {"OBS-CAND-001", "OBS-CAND-002"}
    
    # Lattice gap continuum scaling limit
    assert records_by_id["E-LATTICE-CONT"]["PRIMARY_STATUS"] == "OPEN"
    assert records_by_id["E-LATTICE-CONT"]["OBSTRUCTION_CANDIDATE"] == "OBS-CAND-003"
    
    # Continuum Schwinger function existence
    assert records_by_id["E-CONT-SCHWINGER"]["PRIMARY_STATUS"] == "OPEN"
    
    # OS4 cluster decomposition
    assert records_by_id["E-SCHWINGER-OS4"]["PRIMARY_STATUS"] == "OPEN"
    
    # Arbitrary compact simple G universality
    assert records_by_id["E-GROUP-GEN"]["PRIMARY_STATUS"] == "OPEN"
    
    # Regulated results must remain REGULATED_ONLY
    assert records_by_id["E-UV-RG"]["PRIMARY_STATUS"] == "REGULATED_ONLY"
    assert records_by_id["E-UV-RG"]["SCOPE"]["VOLUME_REGIME"] == "FINITE_VOLUME"
    assert records_by_id["E-LATTICE-GAP"]["PRIMARY_STATUS"] == "REGULATED_ONLY"
    assert records_by_id["E-LATTICE-GAP"]["SCOPE"]["CUTOFF_STATE"] in {"FIXED_LATTICE", "FIXED_LATTICE_A"}


def test_artifacts_coherence():
    """Verify that all 9 canonical literature artifacts exist and are consistent."""
    required_files = [
        "BRIDGE_EDGE_REGISTER.md",
        "MISSING_BRIDGE_GRAPH.md",
        "ASSUMPTION_TRANSFER_MATRIX.md",
        "LIMIT_AND_REGIME_MATRIX.md",
        "OPEN_EDGE_REGISTER.md",
        "SOURCE_TO_EDGE_TRACEABILITY_MATRIX.md",
        "CRITICAL_CUT_SET_REPORT.md",
        "MINIMAL_SUFFICIENT_ESTIMATE_REGISTER.md",
        "YM-003_NEGATIVE_TRANSFER_TESTS.md"
    ]
    for fn in required_files:
        p = LIT_DIR / fn
        assert p.exists(), f"Missing artifact: {fn}"
        assert p.stat().st_size > 100, f"Artifact {fn} is suspiciously small"


def test_negative_transfer_tests_content():
    """Ensure negative transfer tests catalog contains key negative assertions."""
    path = LIT_DIR / "YM-003_NEGATIVE_TRANSFER_TESTS.md"
    content = path.read_text(encoding="utf-8")
    
    assert "Case NEG-001" in content
    assert "Case NEG-002" in content
    assert "Case NEG-003" in content
    assert "Case NEG-004" in content
    assert "Case NEG-005" in content
    assert "Case NEG-006" in content
    assert "Case NEG-007" in content
    assert "LATTICE_CONTINUUM_CONFLATION" in content
    assert "CIRCULAR_PROOF_DEPENDENCY" in content
    assert "SILENT_ASSUMPTION_DISAPPEARANCE" in content
