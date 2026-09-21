import pytest
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"

YM005_ARTIFACTS = [
    "YM-005-PRIMARY-SOURCE-MAP.md",
    "YM-005-LATTICE-FORMALISM-AUDIT.md",
    "YM-005-CLUSTER-EXPANSION-LEDGER.md",
    "YM-005-SPECTRAL-GAP-AND-DECAY-AUDIT.md",
    "YM-005-AREA-LAW-VS-MASS-GAP-AUDIT.md",
    "YM-005-11-DIMENSIONAL-THEOREM-LEDGER.md",
    "YM-005-IR-BOUNDARY-RECORD.md",
    "YM-005-OBSTRUCTION-CANDIDATE-AUDIT.md",
    "YM-005-VISUAL-INTUITION-DATA.md",
    "YM-005-FINAL-SYNTHESIS.md",
]


def test_01_all_ym005_artifacts_exist():
    """Verify that all 10 canonical YM-005 artifacts exist in literature/."""
    for filename in YM005_ARTIFACTS:
        path = LIT_DIR / filename
        assert path.exists(), f"Artifact {filename} must exist"
        assert path.stat().st_size > 500, f"Artifact {filename} must not be empty"


def test_02_primary_source_mapping():
    """Verify that primary sources are mapped and decoupled across the 6 canonical comparative dimensions."""
    content = (LIT_DIR / "YM-005-PRIMARY-SOURCE-MAP.md").read_text(encoding="utf-8")
    assert "Wilson" in content
    assert "Osterwalder" in content
    assert "Lüscher" in content or "Luscher" in content
    assert "Seiler" in content
    assert "Shen" in content and "Zhu" in content
    assert "Cao" in content and "Sheffield" in content
    
    # 6 comparative dimensions
    assert "1. Primary Objective" in content
    assert "2. Volume Regime" in content
    assert "3. Coupling Range" in content
    assert "4. Observable Controlled" in content
    assert "5. Gap / Property Proved" in content
    assert "6. Terminal Open Boundary" in content


def test_03_transfer_matrix_and_reflection_positivity():
    """Verify that lattice formalism audit establishes reflection positivity and transfer matrix self-adjointness."""
    content = (LIT_DIR / "YM-005-LATTICE-FORMALISM-AUDIT.md").read_text(encoding="utf-8")
    assert "reflection positivity" in content.lower()
    assert "transfer matrix" in content.lower() or "transfer operator" in content.lower()
    assert "Hilbert space" in content
    assert "Osterwalder" in content and "Seiler" in content
    assert "Lüscher" in content or "Luscher" in content
    assert "H_{lat}" in content or "H_{\\text{lat}}" in content
    assert "\\mathbb{T}" in content and ("\\ln \\mathbb{T}" in content or "e^{-a H" in content)


def test_04_cluster_expansion_convergence_and_stopping_point():
    """Verify that cluster expansion ledger details character expansion, polymer bounds, and calibrated failure language."""
    content = (LIT_DIR / "YM-005-CLUSTER-EXPANSION-LEDGER.md").read_text(encoding="utf-8")
    assert "Peter–Weyl" in content or "Peter-Weyl" in content
    assert "character" in content.lower()
    assert "polymer" in content.lower()
    assert "Kotecký–Preiss" in content or "Kotecky-Preiss" in content
    assert "free energy" in content.lower()
    assert "infinite-volume" in content.lower() or "thermodynamic limit" in content.lower()
    assert "PROVED_BY_SOURCE" in content
    assert "stopping point" in content.lower() or "stopping" in content.lower()


def test_05_stochastic_analysis_and_functional_inequalities():
    """Verify that stochastic analysis audit covers Shen-Zhu-Zhu, Poincaré/log-Sobolev inequalities, and curvature limits."""
    content = (LIT_DIR / "YM-005-SPECTRAL-GAP-AND-DECAY-AUDIT.md").read_text(encoding="utf-8")
    assert "Shen" in content and "Zhu" in content
    assert "Poincaré" in content or "Poincare" in content
    assert "log-Sobolev" in content.lower() or "logarithmic sobolev" in content.lower()
    assert "Dirichlet form" in content
    assert "Bakry–Émery" in content or "Bakry-Emery" in content
    assert "Ricci curvature" in content
    assert "spectral gap" in content.lower()


def test_06_area_law_vs_spectral_mass_gap_invariant():
    """Verify INV-YM005-002: WILSON_AREA_LAW != SPECTRAL_MASS_GAP_DELTA_GT_0."""
    content = (LIT_DIR / "YM-005-AREA-LAW-VS-MASS-GAP-AUDIT.md").read_text(encoding="utf-8")
    assert "INV-YM005-002" in content
    assert "WILSON_AREA_LAW" in content
    assert "SPECTRAL_MASS_GAP" in content
    assert "2D Yang–Mills" in content or "2D Yang-Mills" in content
    assert "Higgs" in content or "Fradkin–Shenker" in content or "Fradkin-Shenker" in content
    assert "Cao" in content and "Nissim" in content and "Sheffield" in content


def test_07_lattice_spectral_gap_vs_continuum_clay_gap_invariant():
    """Verify INV-YM005-001: LATTICE_SPECTRAL_GAP != CONTINUUM_4D_CLAY_MASS_GAP."""
    content = (LIT_DIR / "YM-005-LATTICE-FORMALISM-AUDIT.md").read_text(encoding="utf-8")
    assert "INV-YM005-001" in content or "Lattice Spectral Gap" in content
    assert "Clay" in content
    assert "continuum" in content.lower()


def test_08_quantitative_provenance_and_symbolic_bounds():
    """Verify INV-YM005-003: explicit provenance classifications and symbolic bounds in canonical IR record."""
    bnd_content = (LIT_DIR / "YM-005-IR-BOUNDARY-RECORD.md").read_text(encoding="utf-8")
    assert "PROJECT_ESTIMATE" in bnd_content
    assert "HEURISTIC_PHYSICAL_TRANSLATION" in bnd_content
    assert "beta <= beta_* << 1" in bnd_content
    assert "INV-YM005-003" in bnd_content or "Quantitative Parameter Provenance" in bnd_content


def test_09_eleven_dimensional_theorem_ledger_completeness():
    """Verify INV-YM005-004: all 11 parameters present in YM-005-11-DIMENSIONAL-THEOREM-LEDGER.md."""
    ledger_content = (LIT_DIR / "YM-005-11-DIMENSIONAL-THEOREM-LEDGER.md").read_text(encoding="utf-8")
    
    required_dimensions = [
        "GAUGE_GROUP",
        "DIMENSION",
        "LATTICE_SPACING_SCOPE",
        "VOLUME_SCOPE",
        "COUPLING_PARAMETER",
        "OBSERVABLE_SCOPE",
        "GAP_OR_DECAY_PROPERTY",
        "UNIFORMITY_ESTABLISHED",
        "CONTINUUM_LIMIT_STATUS",
        "WHAT_IS_ACTUALLY_PROVED",
        "WHAT_REMAINS_OPEN",
    ]
    for dim in required_dimensions:
        assert f"`{dim}`" in ledger_content, f"Dimension {dim} must be explicitly present"
    
    assert "THM-YM-0008" in ledger_content
    assert "THM-YM-0009" in ledger_content
    assert "THM-YM-0015" in ledger_content
    assert "THM-YM-0027" in ledger_content
    assert "THM-YM-0028" in ledger_content


def test_10_canonical_ir_boundary_record_conformance():
    """Verify IR-BND-YM005-001 structure and required fields."""
    content = (LIT_DIR / "YM-005-IR-BOUNDARY-RECORD.md").read_text(encoding="utf-8")
    assert "IR-BND-YM005-001" in content
    assert "last_proved_strong_coupling_regime" in content
    assert "beta_range" in content
    assert "lattice_spacing_scope" in content
    assert "volume_scope" in content
    assert "gap_or_decay_property" in content
    assert "uniformity_established" in content
    assert "first_unproved_extension" in content
    assert "RIGOROUS_PROVED_AT_STRONG_COUPLING_FIXED_LATTICE" in content


def test_11_obstruction_id_canonical_consistency():
    """Verify that OBS-CAND-001, 002, 003 maintain canonical definitions without remapping."""
    audit_content = (LIT_DIR / "YM-005-OBSTRUCTION-CANDIDATE-AUDIT.md").read_text(encoding="utf-8")
    assert "OBS-CAND-001" in audit_content
    assert "OBS-CAND-002" in audit_content
    assert "OBS-CAND-003" in audit_content
    assert "No obstruction candidate is upgraded to a PROVED_OBSTRUCTION_THEOREM" in audit_content.replace("\\_", "_")


def test_12_dual_boundary_visual_intuition_data():
    """Verify visual intuition data reflects UV vs IR dual-boundary structure and crossover."""
    content = (LIT_DIR / "YM-005-VISUAL-INTUITION-DATA.md").read_text(encoding="utf-8")
    assert "ULTRAVIOLET REGIME" in content
    assert "INFRARED REGIME" in content
    assert "UNBRIDGED NON-PERTURBATIVE CROSSOVER WINDOW" in content
    assert "g_k ~ 1" in content or "gk ~ 1" in content


def test_13_no_overclaims_or_clay_sufficiency():
    """Verify that final synthesis explicitly preserves Clay non-sufficiency and gates on YM-006."""
    synthesis = (LIT_DIR / "YM-005-FINAL-SYNTHESIS.md").read_text(encoding="utf-8")
    assert "YM-006" in synthesis
    assert "Locate both rigorous boundaries before trying to bridge the gap between them" in synthesis
    assert "CLAY" in synthesis.upper()
    assert "unproved" in synthesis.lower() or "unbridged" in synthesis.lower()
