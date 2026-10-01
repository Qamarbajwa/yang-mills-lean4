import pytest
from pathlib import Path
import yaml
import re

ROOT = Path(__file__).resolve().parents[1]
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"


def test_01_every_rg_claim_has_source_pointer():
    """Every RG claim and reconstructed theorem must point to an explicit primary source."""
    source_map_path = LIT_DIR / "YM-004-PRIMARY-SOURCE-MAP.md"
    assert source_map_path.exists(), "YM-004-PRIMARY-SOURCE-MAP.md must exist"
    content = source_map_path.read_text(encoding="utf-8")
    
    assert "PAPER-CONST-004" in content
    assert "PAPER-CONST-005" in content
    assert "PAPER-CONST-006" in content
    assert "PAPER-CONST-007" in content
    assert "PAPER-CONST-008" in content
    assert "THM-YM-0016" in content
    assert "THM-YM-0017" in content
    assert "THM-YM-0018" in content
    assert "THM-YM-0020" in content
    assert "Commun. Math. Phys." in content


def test_02_full_target_and_regulated_results_remain_distinct():
    """Finite-volume / regulated results must never be conflated with the full Clay Millennium target."""
    lim_matrix_path = LIT_DIR / "CONSTRUCTIVE_LIMITATION_MATRIX.md"
    content = lim_matrix_path.read_text(encoding="utf-8")
    
    # All constructive results must have CLAY_SUFFICIENT: NO
    lines = [l for l in content.splitlines() if l.startswith("| THM-YM-00")]
    assert len(lines) >= 8
    for line in lines:
        assert "NO (" in line or line.strip().endswith("| NO |"), f"Row fails CLAY_SUFFICIENT: NO: {line}"


def test_03_finite_volume_cannot_be_promoted_to_infinite_volume():
    """Finite volume statements cannot be promoted to infinite volume results."""
    audit_path = LIT_DIR / "YM-004-FINITE-VOLUME-BOUNDARY-AUDIT.md"
    assert audit_path.exists()
    content = audit_path.read_text(encoding="utf-8")
    
    assert "BND-VOL-01" in content
    assert "BND-VOL-08" in content
    assert "BND-VOL-09" in content
    assert "NOT PROVED" in content
    assert "LOAD-BEARING OBSTACLE" in content
    
    # Ensure no claim of L -> infty continuum existence is made
    synthesis_path = LIT_DIR / "YM-004-FINAL-SYNTHESIS.md"
    synth_content = synthesis_path.read_text(encoding="utf-8").lower()
    assert "solved in finite volume" in synth_content or "uv stability in finite volume" in synth_content
    assert "thermodynamic" in synth_content and "infinite" in synth_content


def test_04_no_unproved_stopping_reason_represented_as_theorem():
    """The stopping point must be classified as METHOD_LIMITATION, not an impossibility theorem."""
    stopping_path = LIT_DIR / "YM-004-STOPPING-POINT-ANALYSIS.md"
    assert stopping_path.exists()
    content = stopping_path.read_text(encoding="utf-8").replace(r"\_", "_")
    
    assert "METHOD_LIMITATION" in content
    assert "PROOF_TERMINATES_HERE" in content
    assert "no theorem" in content.lower()


def test_05_obstruction_candidates_remain_candidates():
    """Obstruction candidates must remain candidates and never be upgraded to theorems."""
    obs_audit_path = LIT_DIR / "YM-004-OBSTRUCTION-CANDIDATE-AUDIT.md"
    assert obs_audit_path.exists()
    content = obs_audit_path.read_text(encoding="utf-8")
    
    assert "OBS-CAND-001" in content
    assert "OBS-CAND-002" in content
    assert "OBS-CAND-003" in content
    assert "CONFIRMED CANDIDATE" in content
    assert "No obstruction candidate is upgraded" in content


def test_06_uv_boundary_record_has_explicit_scope():
    """UV boundary record must contain quantitative parameters and explicit scope."""
    bnd_path = LIT_DIR / "YM-004-UV-BOUNDARY-RECORD.md"
    assert bnd_path.exists()
    content = bnd_path.read_text(encoding="utf-8")
    
    assert "UV-BND-YM004-001" in content
    assert "LAST_PROVED_PARAMETER_REGIME" in content
    assert "FIRST_UNPROVED_EXTENSION" in content
    assert "INPUT_FOR_YM006_NON_MEETING" in content
    assert "g_*^2 approx 0.05 - 0.15" in content or "g_*" in content


def test_07_visual_intuition_cannot_enter_evidence_authority():
    """Visual intuition data must carry explicit disclaimer and be barred from evidence."""
    vis_path = LIT_DIR / "YM-004-VISUAL-INTUITION-DATA.md"
    assert vis_path.exists()
    content = vis_path.read_text(encoding="utf-8")
    
    assert "INTUITION ONLY — NOT MATHEMATICAL EVIDENCE" in content


def test_08_closed_world_scientific_artifact_registration():
    """All 10 canonical YM-004 artifacts must be tracked in the scientific classification."""
    class_path = GOV_DIR / "SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml"
    assert class_path.exists()
    content = class_path.read_text(encoding="utf-8")
    data = yaml.safe_load(content)
    
    required_ym004_artifacts = [
        "literature/YM-004-PRIMARY-SOURCE-MAP.md",
        "literature/YM-004-RG-ARCHITECTURE.md",
        "literature/YM-004-SCALE-BY-SCALE-LEDGER.md",
        "literature/YM-004-SMALL-LARGE-FIELD-AUDIT.md",
        "literature/YM-004-FINITE-VOLUME-BOUNDARY-AUDIT.md",
        "literature/YM-004-STOPPING-POINT-ANALYSIS.md",
        "literature/YM-004-UV-BOUNDARY-RECORD.md",
        "literature/YM-004-OBSTRUCTION-CANDIDATE-AUDIT.md",
        "literature/YM-004-VISUAL-INTUITION-DATA.md",
        "literature/YM-004-FINAL-SYNTHESIS.md"
    ]
    
    registered_paths = set(data["scientific_fingerprint"]["paths"])
    for p in required_ym004_artifacts:
        assert p in registered_paths, f"Artifact {p} must be registered in SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml"


def test_09_no_stale_governance_authority_used():
    """Verify that Universal Governance v4.0.3 is active and GOVERNANCE_STATE.yaml is marked superseded."""
    gov_state = ROOT / "GOVERNANCE_STATE.yaml"
    assert gov_state.exists()
    header = gov_state.read_text(encoding="utf-8")[:300]
    assert "SUPERSEDED AT CUTOVER" in header
    
    proj_state = GOV_DIR / "PROJECT_STATE.yaml"
    assert proj_state.exists()
    state_data = yaml.safe_load(proj_state.read_text(encoding="utf-8"))
    assert state_data["activation"] == "ACTIVE"
    assert state_data["schema_version"] == "4.0.3"
    assert state_data["current_objective"] in [
        "YM-004", "YM-005", "YM-006", "YM-007", "YM-008", "YM-009", "YM-010",
        "YM-GOV-011", "YM-GOV-012", "YM-GOV-013", "YM-GOV-014", "YM-GOV-015",
        "YM-011-PRE", "YM-011-OBS-MAP", "YM-011-PLAQUETTE-EXP", "YM-011-PLAQUETTE-EXP-R1", "YM-011-PLAQUETTE-EXP-R2", "YM-GOV-ADOPT-0406R3", "YM-011-TREE-GAUGE", "YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB", "YM-011", "YM-012", "E-CROSSOVER",
    ]


def test_10_source_to_claim_traceability_complete():
    """Verify that every reconstructed paper maps to its canonical theorems."""
    synthesis = (LIT_DIR / "YM-004-FINAL-SYNTHESIS.md").read_text(encoding="utf-8").replace(r"\_", "_")
    assert "THM-YM-0018" in synthesis
    assert "THM-YM-0020" in synthesis
    assert "Bałaban" in synthesis or "Balaban" in synthesis
    assert "Magnen" in synthesis
    assert "METHOD_LIMITATION" in synthesis


def test_11_obstruction_id_canonical_consistency():
    """Verify that OBS-CAND-001, 002, 003 maintain canonical definitions without remapping."""
    audit_path = LIT_DIR / "YM-004-OBSTRUCTION-CANDIDATE-AUDIT.md"
    assert audit_path.exists()
    content = audit_path.read_text(encoding="utf-8")
    
    # Must have canonical reconciliation table
    assert "Canonical Obstruction-ID Reconciliation Table" in content
    assert "OBS-CAND-001" in content
    assert "OBS-CAND-002" in content
    assert "OBS-CAND-003" in content
    assert "O2-CONTINUUM" in content
    assert "O8-OS" in content
    assert "O4-CUTOFF" in content
    assert "Intermediate Crossover Window" in content
    assert "Gauge-Fixing / Positivity Conflict" in content
    assert "Lattice Continuum Scaling" in content


def test_12_quantitative_constants_provenance_explicit():
    """Verify that quantitative constants have explicit provenance classifications and bounds remain symbolic."""
    bnd_path = LIT_DIR / "YM-004-UV-BOUNDARY-RECORD.md"
    content = bnd_path.read_text(encoding="utf-8")
    
    assert "Quantitative Parameter Provenance Audit Table" in content
    assert "PROJECT_ESTIMATE" in content
    assert "HEURISTIC_PHYSICAL_TRANSLATION" in content
    assert "symbolic small-coupling threshold" in content.lower()
    assert "NOT IN PRIMARY SOURCES" in content


def test_13_calibrated_failure_language():
    """Verify that failure language is calibrated (sufficient bound lost vs unconditional divergence)."""
    audit_path = LIT_DIR / "YM-004-SMALL-LARGE-FIELD-AUDIT.md"
    content = audit_path.read_text(encoding="utf-8")
    
    assert "Audit of \"Failure\" and \"Divergence\" Language" in content
    assert "DERIVED_WITH_EXPLICIT_ASSUMPTIONS" in content
    assert "PROVED_BY_SOURCE" in content
    assert "METHOD_RECONSTRUCTION" in content
    assert "sufficient contractivity" in content.lower() or "sufficient convergence" in content.lower()


def test_14_balaban_mrs_theorem_separation():
    """Verify that Bałaban finite-volume UV stability and MRS IR-cutoff construction are separated across 6 dimensions."""
    source_map = (LIT_DIR / "YM-004-PRIMARY-SOURCE-MAP.md").read_text(encoding="utf-8")
    
    assert "Separation of Independent Programs: Bałaban vs. Magnen–Rivasseau–Sénéor" in source_map
    assert "Construction Achieved" in source_map
    assert "Volume Regime" in source_map
    assert "Cutoff Regime" in source_map
    assert "Observables / Functionals Controlled" in source_map
    assert "Uniformity Established" in source_map
    assert "What Remains Open" in source_map
    assert "Bibliographic Clarification on Bałaban Sources" in source_map

