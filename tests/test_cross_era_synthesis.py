"""YM-002F deterministic gates; scientific acceptance still requires E4."""

from pathlib import Path
import re

from ymmg.ros import compute_closed_world_scientific_tree_hash

ROOT = Path(__file__).resolve().parents[1]

MATRIX = ROOT / "literature/CROSS_ERA_SYNTHESIS_MATRIX.md"
OBSTRUCTIONS = ROOT / "literature/COMMON_OBSTRUCTION_CANDIDATES.md"
RESONANCE = ROOT / "literature/OBSTRUCTION_RESONANCE_MATRIX.md"
ESTIMATES = ROOT / "literature/LOAD_BEARING_ESTIMATE_CANDIDATES.md"

EXPECTED_PATHWAYS = (
    [f"THM-YM-{i:04d}" for i in range(1, 13)]
    + [f"THM-YM-{i:04d}" for i in range(13, 21)]
    + [f"THM-YM-{i:04d}" for i in range(21, 31)]
    + [f"THM-YM-{i:04d}" for i in range(31, 41)]
    + ["CLAIM-2024-001", "CLAIM-2025-001", "CLAIM-2026-001", "YM-002E-FERREIRA", "YM-002E-KIRK", "YM-002E-JACOBSEN"]
)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def table_rows(path: Path):
    return [line for line in text(path).splitlines() if line.startswith("|") and not line.startswith("|---")]


def test_all_a_to_e_pathways_are_represented():
    matrix = text(MATRIX)
    missing = [pid for pid in EXPECTED_PATHWAYS if f"| {pid} |" not in matrix]
    assert not missing, missing
    header = next(line for line in matrix.splitlines() if line.startswith("| PATHWAY_ID"))
    width = len(header.strip("|").split("|"))
    malformed = [line for line in table_rows(MATRIX)[1:] if len(line.strip("|").split("|")) != width]
    assert not malformed, malformed[:2]


def test_obstruction_candidates_have_evidence_and_controlled_states():
    content = text(OBSTRUCTIONS)
    rows = table_rows(OBSTRUCTIONS)[1:]
    assert len(rows) >= 8
    allowed = {"OBSERVATION", "RECURRING_PATTERN", "OBSTRUCTION_CANDIDATE", "FORMALIZED_CANDIDATE", "LEMMA_CANDIDATE", "PROVED_OBSTRUCTION_THEOREM"}
    for row in rows:
        cells = [c.strip() for c in row.strip("|").split("|")]
        assert cells[0].startswith("O")
        assert cells[2] and cells[5] and cells[6]
        assert cells[-1] in allowed
    assert "IS_THE_OBSTRUCTION_PROVED" in content
    assert "NO" in content


def test_no_unknown_or_analogue_overpromotion():
    matrix = text(MATRIX)
    assert "| CLAY_SUFFICIENT |" in matrix
    assert all("| NO |" in row for row in table_rows(MATRIX)[1:])
    assert "UNRESOLVED_ORPHANED_LEGACY_CLAIM" in matrix
    assert "UNKNOWN" in matrix
    assert "CLAY_SUFFICIENT" in text(ROOT / "literature/ANALOGUE_LIMITATION_MATRIX.md")


def test_resonance_and_estimates_are_source_bound():
    resonance_rows = table_rows(RESONANCE)[1:]
    resonance_ids = {r.split("|")[1].strip().split(" ")[0] for r in resonance_rows}
    assert {"A-FOUNDATIONAL", "B-CONSTRUCTIVE", "C-MODERN", "D-ANALOGUE"} <= resonance_ids
    assert len(re.findall(r"\| E[1-8] \|", text(ESTIMATES))) == 8
    for row in resonance_rows:
        assert row.count("|") >= 12
        assert row.rsplit("|", 2)[1].strip()
    estimate_header = next(line for line in text(ESTIMATES).splitlines() if line.startswith("| ID |"))
    estimate_width = len(estimate_header.strip("|").split("|"))
    assert all(len(row.strip("|").split("|")) == estimate_width for row in table_rows(ESTIMATES)[1:])


def test_scientific_fingerprint_changed_from_ym002e_predecessor():
    current, files = compute_closed_world_scientific_tree_hash(ROOT)
    assert len(files) == 22
    assert current != "f30a330063b2ca0af772582e318bddd70af9f8c7d9e6d28c1c811c052d156474"
