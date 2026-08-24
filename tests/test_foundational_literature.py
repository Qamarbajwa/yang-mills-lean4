import re
import yaml
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUND_DIR = ROOT / "literature" / "primary" / "foundations_1954_1980"
MANIFEST_PATH = FOUND_DIR / "manifest.yaml"
THEOREM_LEDGER_PATH = ROOT / "THEOREM_LEDGER.md"
LIMITATION_MATRIX_PATH = ROOT / "literature" / "FOUNDATIONAL_LIMITATION_MATRIX.md"

def load_manifest():
    assert MANIFEST_PATH.exists(), "Foundational literature manifest.yaml must exist"
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
    assert LIMITATION_MATRIX_PATH.exists(), "FOUNDATIONAL_LIMITATION_MATRIX.md must exist"
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

def test_paper_found_ids_unique():
    sources = load_manifest()
    paper_ids = [s["source_id"] for s in sources]
    assert len(paper_ids) == len(set(paper_ids)), "Every PAPER-FOUND ID must be unique"
    assert len(paper_ids) >= 11, "Must contain all mandatory foundational papers"

def test_thm_ym_ids_unique():
    theorems = parse_theorems()
    assert len(theorems) >= 12, "Must contain at least 12 foundational theorems"

def test_theorems_reference_registered_sources():
    sources = load_manifest()
    valid_source_ids = {s["source_id"] for s in sources}
    theorems = parse_theorems()
    for thm_id, thm in theorems.items():
        paper_id_raw = thm.get("PAPER_ID", "")
        # Can be multiple papers (e.g. OS I and OS II)
        paper_ids = [p.strip(" `") for p in paper_id_raw.split(",")]
        for pid in paper_ids:
            assert pid in valid_source_ids, f"{thm_id} references unregistered source {pid}"

def test_verified_theorems_have_source_locators():
    theorems = parse_theorems()
    for thm_id, thm in theorems.items():
        if "VERIFIED" in thm.get("STATUS", ""):
            locator = thm.get("SOURCE_LOCATOR", "")
            assert len(locator) > 5, f"Verified theorem {thm_id} must have an exact source locator"

def test_local_captured_file_hashes_match_manifest():
    sources = load_manifest()
    for s in sources:
        rel_file = s["local_file"]
        file_path = FOUND_DIR / rel_file
        assert file_path.exists(), f"Source file {file_path} must exist on disk"
        actual_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
        assert actual_hash == s["sha256"], f"Hash mismatch for {s['source_id']}: {actual_hash} != {s['sha256']}"

def test_theorems_record_dimension():
    theorems = parse_theorems()
    for thm_id, thm in theorems.items():
        assert "DIMENSION" in thm, f"{thm_id} must record DIMENSION"
        assert len(thm["DIMENSION"]) > 0

def test_theorems_record_gauge_group():
    theorems = parse_theorems()
    for thm_id, thm in theorems.items():
        assert "GAUGE_GROUP" in thm, f"{thm_id} must record GAUGE_GROUP"
        assert len(thm["GAUGE_GROUP"]) > 0

def test_theorems_record_lattice_or_continuum():
    theorems = parse_theorems()
    for thm_id, thm in theorems.items():
        domain = thm.get("DOMAIN", "").lower()
        reg = thm.get("REGULARIZATION", "").lower()
        has_domain = any(d in domain for d in ["classical", "quantum", "constructive", "lattice", "axiomatic"])
        assert has_domain, f"{thm_id} must specify valid domain"

def test_theorems_record_coupling_regime():
    theorems = parse_theorems()
    for thm_id, thm in theorems.items():
        assert "COUPLING_REGIME" in thm, f"{thm_id} must record COUPLING_REGIME"
        assert len(thm["COUPLING_REGIME"]) > 0

def test_theorems_record_what_it_does_not_prove():
    theorems = parse_theorems()
    for thm_id, thm in theorems.items():
        assert "WHAT_IT_DOES_NOT_PROVE" in thm, f"{thm_id} must explicitly record WHAT_IT_DOES_NOT_PROVE"
        assert len(thm["WHAT_IT_DOES_NOT_PROVE"]) > 10

def test_large_n_records_n_to_infinity():
    theorems = parse_theorems()
    thm7 = theorems.get("THM-YM-0007")
    assert thm7, "THM-YM-0007 must exist"
    assert "N" in thm7.get("LIMITS", "") and ("\\infty" in thm7.get("LIMITS", "") or "infinity" in thm7.get("LIMITS", "").lower())
    assert "finite" in thm7.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_wilson_not_marked_continuum_mass_gap():
    theorems = parse_theorems()
    thm8 = theorems.get("THM-YM-0008")
    assert thm8, "THM-YM-0008 must exist"
    assert "continuum" in thm8.get("WHAT_IT_DOES_NOT_PROVE", "").lower()
    assert "mass gap" in thm8.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_bpst_not_marked_quantum_mass_gap():
    theorems = parse_theorems()
    thm10 = theorems.get("THM-YM-0010")
    assert thm10, "THM-YM-0010 must exist"
    assert "classical" in thm10.get("DOMAIN", "").lower()
    assert "mass gap" in thm10.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_polyakov_2plus1_not_marked_4d_pure_ym():
    theorems = parse_theorems()
    thm11 = theorems.get("THM-YM-0011")
    assert thm11, "THM-YM-0011 must exist"
    assert "2+1" in thm11.get("DIMENSION", "")
    assert "3+1" in thm11.get("WHAT_IT_DOES_NOT_PROVE", "") or "4d" in thm11.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_os_reconstruction_not_marked_ym_existence():
    theorems = parse_theorems()
    thm5 = theorems.get("THM-YM-0005")
    assert thm5, "THM-YM-0005 must exist"
    assert "not an existence proof" in thm5.get("WHAT_IT_DOES_NOT_PROVE", "").lower() or "does not construct" in thm5.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_asymptotic_freedom_not_marked_mass_gap():
    theorems = parse_theorems()
    thm6 = theorems.get("THM-YM-0006")
    assert thm6, "THM-YM-0006 must exist"
    assert "mass gap" in thm6.get("WHAT_IT_DOES_NOT_PROVE", "").lower()

def test_no_theorem_marked_clay_sufficient():
    lim_matrix = parse_limitation_matrix()
    for thm_id, row in lim_matrix.items():
        assert row.get("CLAY_SUFFICIENT") == "NO", f"{thm_id} cannot be marked CLAY_SUFFICIENT without complete existence + mass gap"

def test_faddeev_popov_does_not_attribute_gribov_to_1967_source():
    theorems = parse_theorems()
    thm2 = theorems.get("THM-YM-0002")
    assert thm2, "THM-YM-0002 must exist"
    # The exact result or assumptions must not claim 1967 paper discovered Gribov ambiguity
    assert "gribov" not in thm2.get("ASSUMPTIONS", "").lower()
    assert "gribov" not in thm2.get("EXACT_RESULT", "").lower()
    assert "gribov" not in thm2.get("WHAT_IT_PROVES", "").lower()
    # It must be attributed to later corrections
    assert "1978" in thm2.get("KNOWN_LATER_CORRECTIONS", "")
    assert "Gribov" in thm2.get("KNOWN_LATER_CORRECTIONS", "")

def test_polyakov_1977_evidence_class_is_semiclassical_not_rigorous_theorem():
    theorems = parse_theorems()
    thm11 = theorems.get("THM-YM-0011")
    assert thm11, "THM-YM-0011 must exist"
    ev_class = thm11.get("EVIDENCE_CLASS", "").strip(" `")
    assert ev_class in ["SEMICLASSICAL_DERIVATION", "PHYSICAL_PROOF_ARGUMENT"]
    assert ev_class != "RIGOROUS_MATHEMATICAL_THEOREM"

def test_evidence_class_taxonomy_valid():
    theorems = parse_theorems()
    allowed_classes = {
        "RIGOROUS_MATHEMATICAL_THEOREM",
        "CONTROLLED_MATHEMATICAL_EXPANSION",
        "PERTURBATIVE_QFT_RESULT",
        "SEMICLASSICAL_DERIVATION",
        "PHYSICAL_PROOF_ARGUMENT",
        "AXIOMATIC_MATHEMATICS",
        "CLASSICAL_EXACT_SOLUTION",
        "CONJECTURE_OR_PROPOSAL"
    }
    for thm_id, thm in theorems.items():
        ev_class = thm.get("EVIDENCE_CLASS", "").strip(" `")
        assert ev_class in allowed_classes, f"{thm_id} has invalid EVIDENCE_CLASS: {ev_class}"



