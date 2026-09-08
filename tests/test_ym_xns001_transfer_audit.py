"""
Unit tests for YM-XNS-001: Navier-Stokes Breakthrough -> Yang-Mills Transfer Audit.
Verifies canonical artifact completeness, epistemic status calibrations,
non-promotion ceilings, reflection positivity constraints, and governance integration.
"""
import pathlib
import yaml
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")

def load_yaml(rel: str):
    return yaml.safe_load(read(rel))

CANONICAL_XNS_ARTIFACTS = [
    "literature/YM-XNS-001-NAVIER-STOKES-STATUS-AUDIT.md",
    "literature/YM-XNS-001-PROOF-ARCHITECTURE.md",
    "literature/YM-XNS-001-MECHANISM-LEDGER.md",
    "literature/YM-XNS-001-YM-TRANSFER-MATRIX.md",
    "literature/YM-XNS-001-NEIGHBORING-PROBLEM-RANKING.md",
    "literature/YM-XNS-001-RESIDUAL-CANCELLATION-AUDIT.md",
    "literature/YM-XNS-001-CLASSICAL-YM-COMPARISON.md",
    "literature/YM-XNS-001-FORMAL-VERIFICATION-ROADMAP.md",
    "literature/YM-XNS-001-MULTI-AGENT-RESEARCH-TOPOLOGY.md",
    "literature/YM-XNS-001-FINAL-SYNTHESIS.md",
]


def test_xns_01_all_canonical_artifacts_exist():
    """All 10 canonical YM-XNS-001 literature artifacts must exist and have non-trivial content."""
    for rel_path in CANONICAL_XNS_ARTIFACTS:
        path = ROOT / rel_path
        assert path.exists(), f"Missing canonical artifact: {rel_path}"
        content = path.read_text(encoding="utf-8")
        assert len(content) > 500, f"Artifact {rel_path} is suspiciously brief"


def test_xns_02_status_audit_calibrated_distinctions():
    """Status audit must distinguish FORMALIZED, COMMUNITY_ACCEPTED, and CLAY_ACCEPTED."""
    content = read("literature/YM-XNS-001-NAVIER-STOKES-STATUS-AUDIT.md")
    assert "FORMALIZED" in content
    assert "COMMUNITY" in content and "ACCEPTED" in content
    assert "CLAY" in content and "ACCEPTED" in content
    assert "PROPOSED_FORMALIZED_UNACCEPTED" in content or "PROPOSED\\_FORMALIZED\\_UNACCEPTED" in content
    assert "Statement (C)" in content or "Statement (D)" in content
    assert "unsolved" in content.lower()


def test_xns_03_proof_architecture_completeness():
    """Proof architecture must include defect calculation, high-frequency corrections, and forcing."""
    content = read("literature/YM-XNS-001-PROOF-ARCHITECTURE.md")
    assert "TARGET PROPOSITION" in content or "Target Proposition" in content
    assert "Residual" in content or "Defect" in content
    assert "High-Frequency Correction" in content or "high-frequency" in content.lower()
    assert "Forcing" in content or "forcing" in content


def test_xns_04_mechanism_ledger_strict_layer_separation():
    """Mechanism ledger must separate mathematical mechanisms (Layer A) from research process (Layer B)."""
    content = read("literature/YM-XNS-001-MECHANISM-LEDGER.md")
    assert "Layer A: Pure Mathematical Mechanisms" in content or "Layer A" in content
    assert "Layer B: Research Methodology" in content or "Layer B" in content
    assert "MECH-M" in content
    assert "MECH-P" in content


def test_xns_05_transfer_matrix_forbids_unproved_transfers():
    """Transfer matrix must forbid assigning TRANSFER_PROVED as a status."""
    content = read("literature/YM-XNS-001-YM-TRANSFER-MATRIX.md")
    assert "| `TRANSFER_PROVED` |" not in content
    assert "| TRANSFER_PROVED |" not in content
    assert "CROSS_PROBLEM_TRANSFER_CANDIDATE" in content.replace(r"\_", "_")
    assert "E-CROSSOVER" in content
    assert "E-LATTICE-CONT" in content
    assert "E-THERMO" in content


def test_xns_06_neighboring_problem_ranking_structure():
    """Neighboring problem ranking must evaluate Bałaban and Magnen-Rivasseau-Sénéor as top candidates."""
    content = read("literature/YM-XNS-001-NEIGHBORING-PROBLEM-RANKING.md")
    assert "Euler First" in content
    assert "Bałaban" in content or "Balaban" in content
    assert "Magnen–Rivasseau–Sénéor" in content or "MRS" in content
    assert "Fixed Lattice Gauge Theory" in content or "Wilson" in content
    assert "Tier 1" in content


def test_xns_07_residual_cancellation_preserves_quantum_barriers():
    """Residual cancellation audit must evaluate gauge invariance, OS3 reflection positivity, and unforced vacuum."""
    content = read("literature/YM-XNS-001-RESIDUAL-CANCELLATION-AUDIT.md")
    assert "Reflection Positivity" in content or "OS3" in content
    assert "Gauge Invariance" in content or "gauge invariance" in content.lower()
    assert "Unforced Vacuum Constraint" in content or "unforced" in content.lower()
    assert "Naive PDE residual cancellation cannot transfer" in content


def test_xns_08_classical_ym_comparison_eardley_moncrief():
    """Classical YM comparison must cite Eardley-Moncrief global regularity and the quadruple barrier."""
    content = read("literature/YM-XNS-001-CLASSICAL-YM-COMPARISON.md")
    assert "Eardley" in content and "Moncrief" in content
    assert "Global Regularity" in content or "global regularity" in content.lower()
    assert "CLASSICAL_YM_PDE" in content.replace(r"\_", "_")
    assert "QUANTUM_MASS_GAP" in content.replace(r"\_", "_")
    assert "scale-invariant" in content.lower() or "scale invariance" in content.lower()


def test_xns_09_formal_verification_roadmap_six_layers():
    """Formal verification roadmap must specify the 6 layers and identify smallest useful target."""
    content = read("literature/YM-XNS-001-FORMAL-VERIFICATION-ROADMAP.md")
    assert "LAYER 1" in content
    assert "LAYER 2" in content
    assert "LAYER 3" in content
    assert "LAYER 4" in content
    assert "LAYER 5" in content
    assert "LAYER 6" in content
    assert "SMALLEST" in content and "USEFUL" in content and "TARGET" in content


def test_xns_10_multi_agent_topology_twelve_tracks():
    """Multi-agent topology must define tracks A through L with adversarial falsification track L."""
    content = read("literature/YM-XNS-001-MULTI-AGENT-RESEARCH-TOPOLOGY.md")
    for track_letter in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]:
        assert f"Track {track_letter}:" in content, f"Missing Track {track_letter} definition"
    assert "Constitutional Invariant 1" in content
    assert "Adversarial Falsification" in content


def test_xns_11_final_synthesis_answers_all_five_questions():
    """Final synthesis must explicitly answer all five consequential questions Q1 through Q5."""
    content = read("literature/YM-XNS-001-FINAL-SYNTHESIS.md")
    assert "Question 1:" in content
    assert "Question 2:" in content
    assert "Question 3:" in content
    assert "Question 4:" in content
    assert "Question 5:" in content
    assert "Analogy generates hypotheses; it does not transfer proofs" in content


def test_xns_12_governance_integration():
    """Governance ledger, envelope, and task graph must record YM-XNS-001."""
    task_graph = read("TASK_GRAPH.md")
    assert "YM-XNS-001" in task_graph
    
    contract_ledger = read("governance/CONTRACT_OWNERSHIP_LEDGER.yaml")
    assert "CONTRACT-YM-XNS-001" in contract_ledger
    
    envelope_path = ROOT / "governance" / "envelopes" / "YM-XNS-001.yaml"
    assert envelope_path.exists()
    envelope = yaml.safe_load(envelope_path.read_text(encoding="utf-8"))
    assert envelope["task_execution_envelope"]["identity"]["task_id"] == "YM-XNS-001"
