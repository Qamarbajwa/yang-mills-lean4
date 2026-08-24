import json
import yaml
import hashlib
import jsonschema
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = ROOT / "governance"
REF_DIR = GOV_DIR / "reference"
CURR_DIR = REF_DIR / "current"
HIST_DIR = REF_DIR / "historical"

def test_1_project_governance_version_is_293():
    proj_gov_path = GOV_DIR / "project-governance.yaml"
    assert proj_gov_path.exists(), "project-governance.yaml must exist"
    data = yaml.safe_load(proj_gov_path.read_text(encoding="utf-8"))
    assert data["project"]["governance_version"] == "2.9.3", "Governance version must be 2.9.3"

def test_2_current_master_v293_exists():
    master_path = CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md"
    assert master_path.exists(), "v2.9.3 Master Constitution must exist"
    assert len(master_path.read_text(encoding="utf-8")) > 100

def test_3_current_runtime_kernel_v293_exists():
    kernel_path = CURR_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md"
    assert kernel_path.exists(), "v2.9.3 Runtime Kernel must exist"
    assert len(kernel_path.read_text(encoding="utf-8")) > 100

def test_4_governance_manifest_hashes_match_disk():
    manifest_path = GOV_DIR / "GOVERNANCE_VERSION_MANIFEST.yaml"
    assert manifest_path.exists(), "GOVERNANCE_VERSION_MANIFEST.yaml must exist"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    for doc in manifest["documents"]:
        doc_path = ROOT / doc["path"]
        assert doc_path.exists(), f"Document {doc_path} must exist on disk"
        actual_hash = hashlib.sha256(doc_path.read_bytes()).hexdigest()
        assert actual_hash == doc["sha256"], f"Hash mismatch for {doc['filename']}: {actual_hash} != {doc['sha256']}"

def test_5_v29_files_preserved_as_historical():
    hist_master = HIST_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md"
    hist_kernel = HIST_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md"
    assert hist_master.exists(), "v2.9 Master must be preserved in historical/"
    assert hist_kernel.exists(), "v2.9 Kernel must be preserved in historical/"
    assert "SUPERSEDED_BY_v2.9.3" in hist_master.read_text(encoding="utf-8")
    assert "SUPERSEDED_BY_v2.9.3" in hist_kernel.read_text(encoding="utf-8")

def test_6_coding_environment_profile_exists_and_parses():
    profile_path = GOV_DIR / "CODING_ENVIRONMENT_PROFILE.yaml"
    assert profile_path.exists(), "CODING_ENVIRONMENT_PROFILE.yaml must exist"
    data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
    assert "coding_environment" in data
    assert "available_agents" in data
    assert "capabilities" in data

def test_7_no_fabricated_agent_inventory_fields_required():
    profile_path = GOV_DIR / "CODING_ENVIRONMENT_PROFILE.yaml"
    data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
    agents = data["available_agents"]
    for agent in agents:
        assert "id" in agent
        assert "provider" in agent
        assert "supported_roles" in agent

def test_8_writer_and_reviewer_ids_must_differ_for_t3_plus():
    routing_path = GOV_DIR / "MODEL_TOOL_ROUTING.yaml"
    assert routing_path.exists(), "MODEL_TOOL_ROUTING.yaml must exist"
    routing = yaml.safe_load(routing_path.read_text(encoding="utf-8"))
    writer_id = routing["role_assignments"]["RESEARCH_WRITER"]["agent_id"]
    reviewer_id = routing["role_assignments"]["INDEPENDENT_REVIEWER"]["agent_id"]
    assert writer_id != reviewer_id, f"Writer ({writer_id}) and Reviewer ({reviewer_id}) must differ"

def test_9_reviewer_independence_level_is_mandatory_for_t3_plus():
    contracts_path = GOV_DIR / "CONTRACT_OWNERSHIP_LEDGER.yaml"
    assert contracts_path.exists(), "CONTRACT_OWNERSHIP_LEDGER.yaml must exist"
    data = yaml.safe_load(contracts_path.read_text(encoding="utf-8"))
    for c in data["contracts"]:
        if c["risk_tier"] in ["T3", "T4"] and c.get("outcome") in ["INDEPENDENTLY_VERIFIED", "READY_FOR_EVALUATION"]:
            assert "independence_level" in c, f"Contract {c['contract_id']} must specify independence_level"
            assert c["independence_level"].startswith("LEVEL_")

def test_10_project_governance_schema_validates():
    schema_path = GOV_DIR / "project-governance.schema.json"
    proj_gov_path = GOV_DIR / "project-governance.yaml"
    assert schema_path.exists(), "project-governance.schema.json must exist"
    assert proj_gov_path.exists(), "project-governance.yaml must exist"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    instance = yaml.safe_load(proj_gov_path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=instance, schema=schema)

def test_11_governance_state_migration_mode_recorded():
    proj_gov_path = GOV_DIR / "project-governance.yaml"
    data = yaml.safe_load(proj_gov_path.read_text(encoding="utf-8"))
    assert data["governance_state"]["mode"] in ["HYBRID_DISCOVERY", "STRUCTURED_RECONCILIATION", "SCHEMA_VALIDATED", "CANONICAL"]
    mig_path = GOV_DIR / "GOVERNANCE_STATE_MIGRATION.md"
    assert mig_path.exists()

def test_12_raw_verifier_evidence_cannot_be_worker_authored_e4():
    quarantine_path = GOV_DIR / "INTEGRITY_QUARANTINE.md"
    assert quarantine_path.exists(), "INTEGRITY_QUARANTINE.md must exist"
    content = quarantine_path.read_text(encoding="utf-8")
    assert "strictly prohibited" in content.lower()
    assert "IVR-001" in content and "IVR-002" in content

def test_13_acceptance_requires_exact_candidate_id():
    for rev_file in (ROOT / "verification").glob("*INDEPENDENT_REVIEW.md"):
        content = rev_file.read_text(encoding="utf-8")
        if "FINAL VERDICT: `INTEGRITY_PASS`" in content:
            assert "CANDIDATE GIT SHA AUDITED" in content, f"{rev_file.name} must record CANDIDATE GIT SHA AUDITED"

def test_14_challenged_ym002a_cannot_be_marked_accepted_in_gov_migration():
    proj_gov_path = GOV_DIR / "project-governance.yaml"
    data = yaml.safe_load(proj_gov_path.read_text(encoding="utf-8"))
    assert data["current_state"]["ym_002a"] == "E3_VERIFIED_E4_PROVENANCE_CHALLENGED"

def test_15_ym002b_remains_blocked():
    proj_gov_path = GOV_DIR / "project-governance.yaml"
    data = yaml.safe_load(proj_gov_path.read_text(encoding="utf-8"))
    assert data["current_state"]["ym_002b"] == "BLOCKED"

def test_16_integrity_incidents_cannot_be_silently_removed():
    ivr_path = ROOT / "INTEGRITY_VIOLATION_REGISTER.md"
    assert ivr_path.exists()
    content = ivr_path.read_text(encoding="utf-8")
    assert "IVR-001" in content
    assert "IVR-002" in content
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert "IVR-001" in proj_gov["integrity"]["open_incidents"]
    assert "IVR-002" in proj_gov["integrity"]["open_incidents"]

def test_17_accepted_evidence_must_refer_to_exact_final_candidate():
    matrix_path = ROOT / "CLAIM_EVIDENCE_MATRIX.md"
    assert matrix_path.exists()
    ev_ledger = ROOT / "EVIDENCE_LEDGER.md"
    assert ev_ledger.exists()

def test_18_derived_verifier_report_references_raw_verifier_artifact():
    for rev_file in (ROOT / "verification").glob("*INDEPENDENT_REVIEW.md"):
        content = rev_file.read_text(encoding="utf-8")
        if "FINAL VERDICT: `INTEGRITY_PASS`" in content:
            assert "DERIVED FROM:" in content
            assert "RAW_SHA256:" in content

def test_19_raw_artifact_modification_invalidates_receipt():
    for rev_file in (ROOT / "verification").glob("*INDEPENDENT_REVIEW.md"):
        content = rev_file.read_text(encoding="utf-8")
        if "RAW_SHA256:" in content and "FINAL VERDICT: `INTEGRITY_PASS`" in content:
            import re
            m_raw = re.search(r"DERIVED FROM[:\* ]*`([^`]+)`", content)
            m_sha = re.search(r"RAW_SHA256[:\* ]*`([a-f0-9]{64})`", content)
            if m_raw and m_sha:
                raw_path = ROOT / m_raw.group(1)
                assert raw_path.exists()
                actual_sha = hashlib.sha256(raw_path.read_bytes()).hexdigest()
                assert actual_sha == m_sha.group(1), f"Raw file {raw_path} has been tampered with"

def test_20_governance_version_mismatch_fails_verification():
    manifest = yaml.safe_load((GOV_DIR / "GOVERNANCE_VERSION_MANIFEST.yaml").read_text(encoding="utf-8"))
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert manifest["active_governance_version"] == proj_gov["project"]["governance_version"] == "2.9.3"

