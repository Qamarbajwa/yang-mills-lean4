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

def test_modern_manifest_sources_match_hashes():
    sources = load_manifest()
    assert len(sources) >= 6, "Must contain at least 6 modern sources/records"
    for s in sources:
        fpath = MOD_DIR / s["local_file"]
        assert fpath.exists(), f"Source file {fpath} must exist"
        sha = hashlib.sha256(fpath.read_bytes()).hexdigest()
        assert sha == s["sha256"], f"Hash mismatch for {s['source_id']}: {sha} != {s['sha256']}"

def test_modern_theorems_present():
    theorems = parse_theorems()
    for tid in ["THM-YM-0021", "THM-YM-0022", "THM-YM-0023", "THM-YM-0024", "THM-YM-0025"]:
        assert tid in theorems, f"{tid} must be registered in THEOREM_LEDGER.md"

def test_modern_theorems_have_bridge_variables_and_failure_locality():
    theorems = parse_theorems()
    for tid in ["THM-YM-0021", "THM-YM-0022", "THM-YM-0023", "THM-YM-0024", "THM-YM-0025"]:
        thm = theorems[tid]
        assert "BRIDGE_VARIABLES" in thm, f"{tid} must declare BRIDGE_VARIABLES"
        assert "FAILURE_LOCALITY" in thm, f"{tid} must declare FAILURE_LOCALITY"
        assert len(thm["BRIDGE_VARIABLES"]) > 3
        assert len(thm["FAILURE_LOCALITY"]) > 3

def test_modern_limitation_matrix_clay_sufficient_all_no():
    rows = parse_limitation_matrix()
    assert len(rows) >= 5, "Limitation matrix must contain all modern theorems"
    for tid, r in rows.items():
        assert "NO" in r.get("CLAY_SUFFICIENT", ""), f"{tid} cannot be marked CLAY_SUFFICIENT"
        assert len(r.get("BRIDGE_VARIABLES", "")) > 3
        assert len(r.get("FAILURE_LOCALITY", "")) > 3

def test_modern_pathway_memory_has_bridge_and_failure_locality():
    assert PATHWAY_MEMORY_PATH.exists(), "PATHWAY_MEMORY_REGISTER.md must exist"
    content = PATHWAY_MEMORY_PATH.read_text(encoding="utf-8")
    for prog in ["PATH-MOD-001", "PATH-MOD-002", "PATH-MOD-003", "PATH-MOD-004"]:
        assert prog in content, f"{prog} must be in PATHWAY_MEMORY_REGISTER.md"
    assert "BRIDGE_VARIABLES" in content
    assert "FAILURE_LOCALITY" in content

def test_chatterjee_gaussian_triviality_recorded():
    theorems = parse_theorems()
    thm24 = theorems.get("THM-YM-0024")
    assert thm24, "THM-YM-0024 must exist"
    assert "gaussian" in thm24.get("EXACT_RESULT", "").lower()
    assert "gaussian" in thm24.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_stochastic_cchs_2d_3d_limitation_recorded():
    theorems = parse_theorems()
    thm21 = theorems.get("THM-YM-0021")
    assert thm21, "THM-YM-0021 must exist"
    assert "2d, 3d" in thm21.get("DIMENSION", "").lower()
    assert "4d" in thm21.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_modern_dependency_graph_justifications():
    assert DEPENDENCY_GRAPH_PATH.exists(), "MODERN_DEPENDENCY_GRAPH.md must exist"
    content = DEPENDENCY_GRAPH_PATH.read_text(encoding="utf-8")
    assert "Explicit Edge Justifications" in content
    assert "THM-YM-0005 -> THM-YM-0021" in content
    assert "CLAY_BARRIER" in content
