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
    assert len(sources) == 10, "Must contain exactly 10 modern primary sources"
    for s in sources:
        fpath = MOD_DIR / s["local_file"]
        assert fpath.exists(), f"Source file {fpath} must exist"
        sha = hashlib.sha256(fpath.read_bytes()).hexdigest()
        assert sha == s["sha256"], f"Hash mismatch for {s['source_id']}: {sha} != {s['sha256']}"

def test_invariant_2d_markov_process_not_invariant_measure_proof():
    theorems = parse_theorems()
    thm21 = theorems["THM-YM-0021"]
    assert "Markov" in thm21["TITLE"] or "Markov" in thm21["EXACT_RESULT"]
    assert "Chevyrev" in thm21["WHAT_IT_DOES_NOT_PROVE"] or "2026" in thm21["WHAT_IT_DOES_NOT_PROVE"]
    thm22 = theorems["THM-YM-0022"]
    assert "CPAM" in thm22["raw"] or "Communications on Pure and Applied Mathematics" in thm22["raw"]
    assert "unique invariant measure" in thm22["EXACT_RESULT"]

def test_invariant_shen_zhu_zhu_cmp_metadata():
    sources = {s["source_id"]: s for s in load_manifest()}
    szz = sources["PAPER-MOD-007"]
    assert szz["year"] == 2023
    assert "Communications in Mathematical Physics" in szz["title"] or "10.1007/s00220-022-04609-1" in szz["doi"]
    theorems = parse_theorems()
    thm27 = theorems["THM-YM-0027"]
    assert "400" in thm27["raw"]
    assert "2023" in thm27["YEAR"]

def test_invariant_two_cns_papers_separated():
    sources = {s["source_id"]: s for s in load_manifest()}
    cns1 = sources["PAPER-MOD-008"]
    cns2 = sources["PAPER-MOD-009"]
    assert "Expanded" in cns1["title"]
    assert "Dynamical" in cns2["title"]
    theorems = parse_theorems()
    thm28 = theorems["THM-YM-0028"]
    thm29 = theorems["THM-YM-0029"]
    assert "Expanded" in thm28["TITLE"]
    assert "Dynamical" in thm29["TITLE"]
    assert "2509.04688" in thm29["raw"]

def test_invariant_kazakov_zheng_finite_n_jhep_metadata():
    sources = {s["source_id"]: s for s in load_manifest()}
    kz_fin = sources["PAPER-MOD-006"]
    assert kz_fin["year"] == 2025
    assert "JHEP" in kz_fin["doi"]
    theorems = parse_theorems()
    thm26 = theorems["THM-YM-0026"]
    assert "2025" in thm26["YEAR"]
    assert "JHEP" in thm26["raw"]

def test_invariant_chatterjee_pmp_metadata():
    sources = {s["source_id"]: s for s in load_manifest()}
    chat = sources["PAPER-MOD-010"]
    assert chat["year"] == 2026
    assert "Probability and Mathematical Physics" in chat["title"] or "10.2140/pmp.2026.7.339" in chat["doi"]
    theorems = parse_theorems()
    thm30 = theorems["THM-YM-0030"]
    assert "2026" in thm30["YEAR"]
    assert "Probability and Mathematical Physics" in thm30["raw"]

def test_all_modern_theorems_have_bridge_variables_and_failure_locality():
    theorems = parse_theorems()
    for tid in [f"THM-YM-{i:04d}" for i in range(21, 31)]:
        assert tid in theorems, f"{tid} must exist in THEOREM_LEDGER.md"
        thm = theorems[tid]
        assert "BRIDGE_VARIABLES" in thm, f"{tid} must have BRIDGE_VARIABLES"
        assert "FAILURE_LOCALITY" in thm, f"{tid} must have FAILURE_LOCALITY"
        assert len(thm["BRIDGE_VARIABLES"]) > 3
        assert len(thm["FAILURE_LOCALITY"]) > 3

def test_modern_limitation_matrix_all_clay_sufficient_no():
    rows = parse_limitation_matrix()
    assert len(rows) == 10, "Must contain all 10 modern theorems"
    for tid, r in rows.items():
        assert "NO" in r.get("CLAY_SUFFICIENT", ""), f"{tid} cannot be marked CLAY_SUFFICIENT"
        assert len(r.get("BRIDGE_VARIABLES", "")) > 3
        assert len(r.get("FAILURE_LOCALITY", "")) > 3
