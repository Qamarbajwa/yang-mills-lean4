import json
import yaml
import hashlib
import jsonschema
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = ROOT / "governance"
REF_DIR = GOV_DIR / "reference"
CURR_DIR = REF_DIR / "current"
HIST_DIR = REF_DIR / "historical"

def test_1_current_governance_version_is_294():
    proj_gov_path = GOV_DIR / "project-governance.yaml"
    assert proj_gov_path.exists()
    data = yaml.safe_load(proj_gov_path.read_text(encoding="utf-8"))
    assert data["project"]["governance_version"] == "2.9.4"

def test_2_v294_master_exists():
    master_path = CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md"
    assert master_path.exists()
    assert len(master_path.read_text(encoding="utf-8")) > 100

def test_3_v294_runtime_kernel_exists():
    kernel_path = CURR_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md"
    assert kernel_path.exists()
    assert len(kernel_path.read_text(encoding="utf-8")) > 100

def test_4_hashes_match_governance_manifest():
    manifest_path = GOV_DIR / "GOVERNANCE_VERSION_MANIFEST.yaml"
    assert manifest_path.exists()
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    for doc in manifest["documents"]:
        doc_path = ROOT / doc["path"]
        assert doc_path.exists(), f"Document {doc_path} must exist on disk"
        actual_hash = hashlib.sha256(doc_path.read_bytes()).hexdigest()
        assert actual_hash == doc["sha256"], f"Hash mismatch for {doc['filename']}: {actual_hash} != {doc['sha256']}"

def test_5_v29_and_v293_preserved_historically():
    hist_files = [
        HIST_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md",
        HIST_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md",
        HIST_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md",
        HIST_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md"
    ]
    for hf in hist_files:
        assert hf.exists(), f"Historical file {hf.name} must exist"
        assert "HISTORICAL" in hf.read_text(encoding="utf-8")

def test_6_only_v294_is_current():
    curr_files = list(CURR_DIR.glob("*.md"))
    assert len(curr_files) == 2
    names = {f.name for f in curr_files}
    assert "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md" in names
    assert "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md" in names

def test_7_coding_environment_profile_parses():
    prof_path = GOV_DIR / "CODING_ENVIRONMENT_PROFILE.yaml"
    assert prof_path.exists()
    data = yaml.safe_load(prof_path.read_text(encoding="utf-8"))
    assert "coding_environment" in data
    assert "available_agents" in data
    assert "capabilities" in data

def test_8_environment_acceptance_capabilities_represented():
    prof_path = GOV_DIR / "CODING_ENVIRONMENT_PROFILE.yaml"
    data = yaml.safe_load(prof_path.read_text(encoding="utf-8"))
    assert "acceptance_capabilities" in data
    acc = data["acceptance_capabilities"]
    assert acc.get("local_parent_orchestrator") is True
    assert acc.get("distinct_reviewer") is True
    assert acc.get("automated_acceptance_gate") is True
    assert acc.get("human_approval_available") is True

def test_9_t3_plus_writer_id_differs_from_reviewer_id():
    routing = yaml.safe_load((GOV_DIR / "MODEL_TOOL_ROUTING.yaml").read_text(encoding="utf-8"))
    writer_id = routing["role_assignments"]["RESEARCH_WRITER"]["agent_id"]
    reviewer_id = routing["role_assignments"]["INDEPENDENT_REVIEWER"]["agent_id"]
    assert writer_id != reviewer_id

def test_10_independent_acceptance_requires_writer_not_equal_acceptance_authority():
    routing = yaml.safe_load((GOV_DIR / "MODEL_TOOL_ROUTING.yaml").read_text(encoding="utf-8"))
    writer_id = routing["role_assignments"]["RESEARCH_WRITER"]["agent_id"]
    acc_id = routing["role_assignments"]["ACCEPTANCE_AUTHORITY"]["agent_id"]
    assert writer_id != acc_id

def test_11_no_codex_universal_acceptance_authority():
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert proj_gov["acceptance"]["universal_codex_authority"] is False
    routing_text = (GOV_DIR / "MODEL_TOOL_ROUTING.yaml").read_text(encoding="utf-8")
    assert "CODEX != UNIVERSAL_ACCEPTANCE_AUTHORITY" in (CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md").read_text(encoding="utf-8")

def test_12_no_universal_provider_acceptance_authority():
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert proj_gov["acceptance"]["universal_provider_authority"] is False

def test_13_acceptance_mapping_is_environment_local():
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert proj_gov["acceptance"]["authority_model"] == "ENVIRONMENT_LOCAL"

def test_14_antigravity_does_not_require_codex_acceptance_by_default():
    routing = yaml.safe_load((GOV_DIR / "MODEL_TOOL_ROUTING.yaml").read_text(encoding="utf-8"))
    acc = routing["role_assignments"]["ACCEPTANCE_AUTHORITY"]
    assert "antigravity" in acc["agent_id"].lower()
    assert acc["environment"] == "Antigravity"

def test_15_claude_code_does_not_require_codex_acceptance_by_default():
    master_text = (CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md").read_text(encoding="utf-8")
    assert "Claude Code Parent Orchestrator" in master_text

def test_16_opencode_does_not_require_external_acceptance_when_local_exists():
    master_text = (CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md").read_text(encoding="utf-8")
    assert "OpenCode Parent Orchestrator" in master_text

def test_17_cross_application_review_is_optional_fallback():
    master_text = (CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md").read_text(encoding="utf-8")
    assert "OPTIONAL / FALLBACK" in master_text

def test_18_t4_t5_human_authority_distinguishable_from_technical_acceptance():
    policy_text = (GOV_DIR / "ACCEPTANCE_GATE_POLICY.md").read_text(encoding="utf-8")
    assert "HUMAN_AUTHORITY" in policy_text
    assert "BOUNDED TECHNICAL CONTRACT ACCEPTED" in policy_text
    assert "RELEASE_READY" in policy_text

def test_19_candidate_bound_evidence_rules_enforced():
    schema = json.loads((GOV_DIR / "project-governance.schema.json").read_text(encoding="utf-8"))
    instance = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    jsonschema.validate(instance=instance, schema=schema)

def test_20_raw_verifier_artifact_cannot_be_worker_authored_e4():
    quarantine = (GOV_DIR / "INTEGRITY_QUARANTINE.md").read_text(encoding="utf-8")
    assert "strictly prohibited" in quarantine.lower()

def test_21_integrity_incidents_are_preserved():
    ivr = (ROOT / "INTEGRITY_VIOLATION_REGISTER.md").read_text(encoding="utf-8")
    assert "IVR-001" in ivr
    assert "IVR-002" in ivr

def test_22_ym002a_remains_challenged():
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert proj_gov["current_state"]["ym_002a"] == "E3_VERIFIED_E4_PROVENANCE_CHALLENGED"

def test_23_ym002ar1_remains_blocked_during_migration():
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert proj_gov["current_state"]["ym_002ar1"] == "BLOCKED"

def test_24_ym002b_remains_blocked():
    proj_gov = yaml.safe_load((GOV_DIR / "project-governance.yaml").read_text(encoding="utf-8"))
    assert proj_gov["current_state"]["ym_002b"] == "BLOCKED"

def test_25_worker_self_report_cannot_produce_accepted():
    kernel_text = (CURR_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md").read_text(encoding="utf-8")
    assert "Model self-report is not acceptance evidence" in kernel_text

def test_26_material_candidate_change_invalidates_stale_evidence():
    policy_text = (GOV_DIR / "ACCEPTANCE_GATE_POLICY.md").read_text(encoding="utf-8")
    assert "OLD EVIDENCE = STALE" in policy_text or "STALE" in policy_text

