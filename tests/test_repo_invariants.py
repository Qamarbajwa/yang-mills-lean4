from pathlib import Path
from ymmg.repo import missing_required_files, load_yaml, governance_project_id

ROOT = Path(__file__).resolve().parents[1]

def test_required_files_exist():
    missing = missing_required_files(ROOT)
    assert not missing, f"Missing required files: {missing}"

def test_governance_yaml_parses():
    for rel in [
        "governance/bootstrap.yaml",
        "governance/risk-policy.yaml",
        "governance/project-governance.yaml",
        "governance/trust-anchor.yaml",
    ]:
        data = load_yaml(ROOT, rel)
        assert isinstance(data, dict), f"{rel} did not parse to a mapping"

def test_project_identity_is_consistent():
    assert governance_project_id(ROOT) == "YM-MASS-GAP"
    bootstrap = load_yaml(ROOT, "governance/bootstrap.yaml")
    risk = load_yaml(ROOT, "governance/risk-policy.yaml")
    assert bootstrap["project_id"] == "YM-MASS-GAP"
    assert risk["project_id"] == "YM-MASS-GAP"

def test_no_preaccepted_proof_claim():
    state = load_yaml(ROOT, "governance/project-governance.yaml")
    assert state["current_state"]["proof_status"] == "NO_CANDIDATE_PROOF"
    assert state["current_state"]["original_verified_lemmas"] == 0
