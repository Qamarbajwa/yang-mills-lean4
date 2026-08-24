import re
import yaml
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MOD_DIR = ROOT / "literature" / "primary" / "modern_2000_2026"
MANIFEST_PATH = MOD_DIR / "manifest.yaml"
THEOREM_LEDGER_PATH = ROOT / "THEOREM_LEDGER.md"
LIMITATION_MATRIX_PATH = ROOT / "literature" / "MODERN_LIMITATION_MATRIX.md"
DEPENDENCY_GRAPH_PATH = ROOT / "literature" / "MODERN_DEPENDENCY_GRAPH.md"
PATHWAY_MEMORY_PATH = ROOT / "literature" / "PATHWAY_MEMORY_REGISTER.md"
OFFICIAL_STATUS_PATH = ROOT / "OFFICIAL_PROBLEM_STATUS_INVARIANT.md"
CLAIM_QUARANTINE_PATH = ROOT / "literature" / "CLAIM_QUARANTINE_REGISTER.md"

def load_manifest():
    assert MANIFEST_PATH.exists(), "Modern manifest.yaml must exist"
    data = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
    return data["sources"]

def parse_theorems():
    assert THEOREM_LEDGER_PATH.exists(), "THEOREM_LEDGER.md must exist"
    content = THEOREM_LEDGER_PATH.read_text(encoding="utf-8")
    blocks = re.split(r"\n###\s+(THM-YM-\d+):", content)
    theorems = {}
    for i in range(1, len(blocks), 2):
        thm_id = blocks[i].strip()
        body = blocks[i+1]
        thm_data = {"id": thm_id, "raw": body}
        for line in body.split("\n"):
            line = line.strip()
            if line.startswith("- **") and ":**" in line:
                key = line.split(":**")[0].replace("- **", "").strip()
                val = line.split(":**")[1].strip()
                thm_data[key] = val
        theorems[thm_id] = thm_data
    return theorems

def parse_limitation_matrix():
    assert LIMITATION_MATRIX_PATH.exists(), "MODERN_LIMITATION_MATRIX.md must exist"
    lines = LIMITATION_MATRIX_PATH.read_text(encoding="utf-8").strip().split("\n")
    headers = [h.strip() for h in lines[2].split("|")[1:-1]]
    rows = {}
    for line in lines[4:]:
        if not line.strip() or not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if parts:
            thm_id = parts[0]
            rows[thm_id] = dict(zip(headers, parts))
    return rows

def test_manifest_sources_hashes_and_count():
    sources = load_manifest()
    assert len(sources) == 8, "Must contain exactly 8 modern primary sources"
    for s in sources:
        fpath = MOD_DIR / s["local_file"]
        assert fpath.exists(), f"Source file {fpath} must exist"
        sha = hashlib.sha256(fpath.read_bytes()).hexdigest()
        assert sha == s["sha256"], f"Hash mismatch for {s['source_id']}: {sha} != {s['sha256']}"

def test_invariant_project_register_not_in_primary_manifest():
    sources = load_manifest()
    for s in sources:
        assert "Adversarial" not in s["title"], "Project registers must not be in primary literature manifest"
        assert "Screening" not in s["title"], "Project registers must not be in primary literature manifest"

def test_invariant_official_status_not_in_theorem_ledger():
    theorems = parse_theorems()
    assert "THM-YM-0025" in theorems
    assert "Clay" not in theorems["THM-YM-0025"]["TITLE"], "Clay status must not be a mathematical theorem ID"
    assert OFFICIAL_STATUS_PATH.exists(), "OFFICIAL_PROBLEM_STATUS_INVARIANT.md must exist"

def test_invariant_2d_and_3d_stochastic_separated():
    theorems = parse_theorems()
    thm21 = theorems["THM-YM-0021"]
    thm22 = theorems["THM-YM-0022"]
    assert "2D" in thm21["TITLE"] or "2D" in thm21["DIMENSION"]
    assert "3D" in thm22["TITLE"] or "3D" in thm22["DIMENSION"]
    assert "IHÉS" in thm21["raw"] or "IHES" in thm21["raw"]
    assert "Inventiones" in thm22["raw"]
    assert "invariant" in thm22["WHAT_IT_DOES_NOT_PROVE"].lower() and "measure" in thm22["WHAT_IT_DOES_NOT_PROVE"].lower()

def test_invariant_chevyrev_shen_scoped_to_3d():
    theorems = parse_theorems()
    thm23 = theorems["THM-YM-0023"]
    assert "3D" in thm23["TITLE"]
    assert "3" in thm23["DIMENSION"]
    assert "250" in thm23["raw"]
    assert "2503.03060" in thm23["raw"]

def test_invariant_kazakov_zheng_large_and_finite_n_separated():
    theorems = parse_theorems()
    thm24 = theorems["THM-YM-0024"]
    thm25 = theorems["THM-YM-0025"]
    assert "Large N" in thm24["TITLE"] or r"SU(\infty)" in thm24["GAUGE_GROUP"] or "SU(\\infty)" in thm24["GAUGE_GROUP"]
    assert "Finite N" in thm25["TITLE"] or "SU(2)" in thm25["GAUGE_GROUP"]

def test_shen_zhu_zhu_lattice_strong_coupling_mass_gap():

    theorems = parse_theorems()
    thm26 = theorems["THM-YM-0026"]
    assert "Shen" in thm26["AUTHORS"]
    assert "Poincaré" in thm26["EXACT_RESULT"] or "Poincare" in thm26["EXACT_RESULT"]
    assert "strong coupling" in thm26["COUPLING_REGIME"].lower()
    assert "clay" in thm26["WHAT_IT_DOES_NOT_PROVE"].lower()

def test_all_modern_theorems_have_bridge_variables_and_failure_locality():
    theorems = parse_theorems()
    for tid in ["THM-YM-0021", "THM-YM-0022", "THM-YM-0023", "THM-YM-0024", "THM-YM-0025", "THM-YM-0026", "THM-YM-0027", "THM-YM-0028"]:
        assert tid in theorems, f"{tid} must exist in THEOREM_LEDGER.md"
        thm = theorems[tid]
        assert "BRIDGE_VARIABLES" in thm, f"{tid} must have BRIDGE_VARIABLES"
        assert "FAILURE_LOCALITY" in thm, f"{tid} must have FAILURE_LOCALITY"
        assert len(thm["BRIDGE_VARIABLES"]) > 3
        assert len(thm["FAILURE_LOCALITY"]) > 3

def test_modern_limitation_matrix_all_clay_sufficient_no():
    rows = parse_limitation_matrix()
    assert len(rows) == 8, "Must contain all 8 modern theorems"
    for tid, r in rows.items():
        assert "NO" in r.get("CLAY_SUFFICIENT", ""), f"{tid} cannot be marked CLAY_SUFFICIENT"
        assert len(r.get("BRIDGE_VARIABLES", "")) > 3
        assert len(r.get("FAILURE_LOCALITY", "")) > 3

def test_claim_quarantine_register_present():
    assert CLAIM_QUARANTINE_PATH.exists()
    content = CLAIM_QUARANTINE_PATH.read_text(encoding="utf-8")
    assert "PROJECT_REGISTER != PRIMARY_LITERATURE_SOURCE" in content
    assert "YM-002E" in content
