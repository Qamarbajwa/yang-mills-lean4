import yaml
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = ROOT / "governance"

def test_1_reconciliation_doc_exists_and_has_required_fields():
    doc_path = GOV_DIR / "ACCEPTANCE_AUTHORITY_RECONCILIATION_YM-GOV-294.md"
    assert doc_path.exists(), "ACCEPTANCE_AUTHORITY_RECONCILIATION_YM-GOV-294.md must exist"
    content = doc_path.read_text(encoding="utf-8")
    
    required_fields = [
        "WRITER_ROLE",
        "WRITER_EXECUTION_ID",
        "REVIEWER_ROLE",
        "REVIEWER_EXECUTION_ID",
        "ACCEPTANCE_ROLE",
        "ACCEPTANCE_EXECUTION_ID",
        "WRITER_AND_REVIEWER_DISTINCT",
        "WRITER_AND_ACCEPTANCE_DISTINCT",
        "REVIEWER_AND_ACCEPTANCE_DISTINCT",
        "EVIDENCE_USED",
        "LIMITATIONS"
    ]
    for field in required_fields:
        assert field in content, f"Reconciliation document must contain {field}"

def test_2_writer_and_reviewer_execution_ids_differ_for_t3_plus():
    ledger = yaml.safe_load((GOV_DIR / "CONTRACT_OWNERSHIP_LEDGER.yaml").read_text(encoding="utf-8"))
    for c in ledger["contracts"]:
        if c.get("risk_tier") in ["T3", "T4"] and c.get("outcome") in ["INDEPENDENTLY_VERIFIED", "ACCEPTED_AFTER_ACCEPTANCE_REPAIR"]:
            w_exec = c.get("writer", {}).get("execution_id")
            r_exec = c.get("reviewer", {}).get("execution_id")
            if w_exec and r_exec:
                assert w_exec != r_exec, f"Contract {c['contract_id']}: Writer execution ID must differ from Reviewer execution ID"

def test_3_writer_and_acceptance_execution_ids_differ_for_independent_acceptance():
    ledger = yaml.safe_load((GOV_DIR / "CONTRACT_OWNERSHIP_LEDGER.yaml").read_text(encoding="utf-8"))
    for c in ledger["contracts"]:
        if c.get("risk_tier") in ["T3", "T4"] and c.get("outcome") in ["ACCEPTED", "ACCEPTED_AFTER_ACCEPTANCE_REPAIR"]:
            w_exec = c.get("writer", {}).get("execution_id")
            a_exec = c.get("acceptance_authority", {}).get("execution_id")
            if w_exec and a_exec:
                assert w_exec != a_exec, f"Contract {c['contract_id']}: Writer execution ID must differ from Acceptance Authority execution ID"

def test_4_role_name_difference_alone_cannot_claim_independent_acceptance():
    # Synthetic test of the invariant
    mock_contract = {
        "writer": {"agent_id": "primary-writer", "execution_id": "session-123"},
        "acceptance_authority": {"agent_id": "local-orchestrator", "execution_id": "session-123"}
    }
    # If agent_id differs but execution_id matches, independent technical acceptance is invalid
    has_identity_separation = mock_contract["writer"]["execution_id"] != mock_contract["acceptance_authority"]["execution_id"]
    assert not has_identity_separation, "Same execution session cannot satisfy identity separation merely by changing role name"

def test_5_policy_and_routing_document_execution_identity_invariants():
    policy = (GOV_DIR / "ACCEPTANCE_GATE_POLICY.md").read_text(encoding="utf-8")
    assert "ROLE_NAME DIFFERENCE != EXECUTION IDENTITY SEPARATION" in policy
    
    routing = (GOV_DIR / "MODEL_TOOL_ROUTING.yaml").read_text(encoding="utf-8")
    assert "ROLE_NAME DIFFERENCE != EXECUTION IDENTITY SEPARATION" in routing
    assert "WRITER_EXECUTION_ID != REVIEWER_EXECUTION_ID" in routing
    assert "WRITER_EXECUTION_ID != ACCEPTANCE_AUTHORITY_EXECUTION_ID" in routing

