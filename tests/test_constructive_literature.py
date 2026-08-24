import re
import yaml
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONST_DIR = ROOT / "literature" / "primary" / "constructive_1980_2000"
MANIFEST_PATH = CONST_DIR / "manifest.yaml"
THEOREM_LEDGER_PATH = ROOT / "THEOREM_LEDGER.md"
LIMITATION_MATRIX_PATH = ROOT / "literature" / "CONSTRUCTIVE_LIMITATION_MATRIX.md"
DEPENDENCY_GRAPH_PATH = ROOT / "literature" / "CONSTRUCTIVE_DEPENDENCY_GRAPH.md"
PATHWAY_MEMORY_PATH = ROOT / "literature" / "PATHWAY_MEMORY_REGISTER.md"

def load_manifest():
    assert MANIFEST_PATH.exists(), "Constructive manifest.yaml must exist"
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
    assert LIMITATION_MATRIX_PATH.exists(), "CONSTRUCTIVE_LIMITATION_MATRIX.md must exist"
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

def test_constructive_manifest_sources_match_hashes():
    sources = load_manifest()
    assert len(sources) >= 8, "Must contain at least 8 constructive primary sources"
    for s in sources:
        fpath = CONST_DIR / s["local_file"]
        assert fpath.exists(), f"Source file {fpath} must exist"
        sha = hashlib.sha256(fpath.read_bytes()).hexdigest()
        assert sha == s["sha256"], f"Hash mismatch for {s['source_id']}: {sha} != {s['sha256']}"

def test_constructive_theorems_present():
    theorems = parse_theorems()
    for tid in ["THM-YM-0013", "THM-YM-0014", "THM-YM-0015", "THM-YM-0016", "THM-YM-0017", "THM-YM-0018", "THM-YM-0019", "THM-YM-0020"]:
        assert tid in theorems, f"{tid} must be registered in THEOREM_LEDGER.md"

def test_constructive_limitation_matrix_clay_sufficient_all_no():
    rows = parse_limitation_matrix()
    assert len(rows) >= 8, "Limitation matrix must contain all constructive theorems"
    for tid, r in rows.items():
        assert "NO" in r.get("CLAY_SUFFICIENT", ""), f"{tid} cannot be marked CLAY_SUFFICIENT"

def test_balaban_uv_stability_finite_volume_only():
    theorems = parse_theorems()
    thm18 = theorems.get("THM-YM-0018")
    assert thm18, "THM-YM-0018 must exist"
    assert "infinite" in thm18.get("WHAT_IT_DOES_NOT_PROVE", "").lower() or r"v \to \infty" in thm18.get("WHAT_IT_DOES_NOT_PROVE", "").lower()


def test_magnen_rivasseau_infrared_cutoff_recorded():
    theorems = parse_theorems()
    thm20 = theorems.get("THM-YM-0020")
    assert thm20, "THM-YM-0020 must exist"
    assert "infrared cutoff" in thm20.get("TITLE", "").lower()
    assert "renormalon" in thm20.get("WHAT_IT_DOES_NOT_PROVE", "").lower() or "cutoff" in thm20.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_pathway_memory_register_complete():
    assert PATHWAY_MEMORY_PATH.exists(), "PATHWAY_MEMORY_REGISTER.md must exist"
    content = PATHWAY_MEMORY_PATH.read_text(encoding="utf-8")
    for prog in ["PATH-CONST-001", "PATH-CONST-002", "PATH-CONST-003", "PATH-CONST-004"]:
        assert prog in content, f"{prog} must be in PATHWAY_MEMORY_REGISTER.md"
    for field in ["CENTRAL_THESIS", "DIRECTION", "WHAT_SUCCEEDED", "WHAT_FAILED", "WHAT_SURVIVED", "CLOSURE_REASON", "REOPEN_CONDITIONS", "OUTCOME_FINGERPRINT"]:
        assert field in content, f"Pathway memory field {field} must be present"

def test_constructive_dependency_graph_justifications():
    assert DEPENDENCY_GRAPH_PATH.exists(), "CONSTRUCTIVE_DEPENDENCY_GRAPH.md must exist"
    content = DEPENDENCY_GRAPH_PATH.read_text(encoding="utf-8")
    assert "Explicit Edge Justifications" in content
    assert "THM-YM-0011 -> THM-YM-0013" in content
    assert "THM-YM-0016 -> THM-YM-0017" in content
    assert "CLAY_BARRIER" in content
