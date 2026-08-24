import re
import yaml
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_official_specification_exists_and_reconstructed():
    spec_path = ROOT / "OFFICIAL_PROBLEM_SPECIFICATION.md"
    assert spec_path.exists(), "OFFICIAL_PROBLEM_SPECIFICATION.md must exist"
    content = spec_path.read_text(encoding="utf-8")
    assert "TO_BE_RECONSTRUCTED_IN_YM-001" not in content, "Specification must no longer be placeholder"
    assert "Official Yang–Mills Existence and Mass Gap Specification" in content

def test_source_manifest_parses_and_hashes_match():
    manifest_path = ROOT / "literature" / "primary" / "clay" / "SOURCE_MANIFEST.yaml"
    assert manifest_path.exists(), "SOURCE_MANIFEST.yaml must exist"
    data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    assert "sources" in data, "Manifest must contain sources list"
    for src in data["sources"]:
        fname = src["file_name"]
        fpath = ROOT / "literature" / "primary" / "clay" / fname
        assert fpath.exists(), f"Source file {fname} must exist on disk"
        actual_sha = hashlib.sha256(fpath.read_bytes()).hexdigest()
        assert actual_sha == src["sha256"], f"SHA-256 mismatch for {fname}: {actual_sha} != {src['sha256']}"

def test_unique_ym_req_ids():
    spec_path = ROOT / "OFFICIAL_PROBLEM_SPECIFICATION.md"
    content = spec_path.read_text(encoding="utf-8")
    req_ids = re.findall(r"YM-REQ-\d+", content)
    assert req_ids, "Must find YM-REQ IDs"
    assert len(req_ids) == len(set(req_ids)), f"Duplicate YM-REQ IDs found: {req_ids}"

def test_unique_definition_ids():
    def_path = ROOT / "DEFINITION_LEDGER.md"
    assert def_path.exists()
    content = def_path.read_text(encoding="utf-8")
    def_ids = re.findall(r"DEF-YM-\d+", content)
    assert def_ids, "Must find DEF-YM IDs"
    assert len(def_ids) == len(set(def_ids)), f"Duplicate DEF-YM IDs found: {def_ids}"

def test_every_ym_req_has_source_reference():
    spec_path = ROOT / "OFFICIAL_PROBLEM_SPECIFICATION.md"
    content = spec_path.read_text(encoding="utf-8")
    table_lines = [l for l in content.splitlines() if l.strip().startswith("| YM-REQ-")]
    assert len(table_lines) >= 30, f"Expected at least 30 requirements, found {len(table_lines)}"
    for line in table_lines:
        parts = [p.strip() for p in line.split("|")[1:-1]]
        req_id, statement, source_ref, classification, status = parts
        assert "Jaffe" in source_ref, f"Requirement {req_id} missing primary Jaffe-Witten source reference"
        assert classification in ["REQUIRED", "REQUIRED_BOUNDARY", "DERIVED_CONSEQUENCE", "DESIRABLE_EXTENSION"], f"Invalid class {classification} in {req_id}"

def test_claim_evidence_matrix_matches_requirements():
    claim_path = ROOT / "CLAIM_EVIDENCE_MATRIX.md"
    assert claim_path.exists()
    content = claim_path.read_text(encoding="utf-8")
    req_ids = re.findall(r"YM-REQ-\d+", content)
    assert len(req_ids) >= 30
    assert len(req_ids) == len(set(req_ids)), "Duplicate requirement in matrix"

def test_central_exact_invariants():
    spec_path = ROOT / "OFFICIAL_PROBLEM_SPECIFICATION.md"
    content = spec_path.read_text(encoding="utf-8")
    # 1. Compact simple G
    assert "compact simple" in content
    # 2. R^4
    assert "\\mathbb{R}^4" in content or "R^4" in content
    # 3. Non-trivial quantum Yang-Mills
    assert "non-trivial" in content.lower()
    # 4. Delta > 0
    assert "\\Delta > 0" in content or "Delta > 0" in content
    # 5. No spectrum in (0, Delta)
    assert "(0, \\Delta)" in content or "(0, Delta)" in content
    # 6. Finite supremal mass m < infinity
    assert "m < \\infty" in content or "m < infinity" in content

def test_required_vs_extensions_separated():
    spec_path = ROOT / "OFFICIAL_PROBLEM_SPECIFICATION.md"
    content = spec_path.read_text(encoding="utf-8")
    assert "## 14. Extensions Not Required by the Formal Problem" in content
    assert "Isolated One-Particle State" in content
    assert "Quark Confinement" in content
    assert "Chiral Symmetry Breaking" in content

def test_weak_compactness_boundary_preserved():
    spec_path = ROOT / "OFFICIAL_PROBLEM_SPECIFICATION.md"
    content = spec_path.read_text(encoding="utf-8")
    assert "Footnote 2" in content
    assert "specifically exclude weak-existence" in content

