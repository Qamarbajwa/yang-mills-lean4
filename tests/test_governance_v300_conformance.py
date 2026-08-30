"""Repository-local checks for Universal Governance v3.0.0 migration.

These checks map directly to GC-01..GC-30 in the sealed v3 conformance standard.
They verify structural and semantic boundaries; they do not manufacture an
independent review or scientific acceptance.
"""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_v3_state_and_envelopes_are_bound_and_typed():
    state = yaml.safe_load(read("GOVERNANCE_STATE.yaml"))["governance_state"]
    migration = yaml.safe_load(read("governance/envelopes/YM-GOV-300.yaml"))["task_execution_envelope"]
    objective = yaml.safe_load(read("governance/envelopes/YM-002E.yaml"))["task_execution_envelope"]

    assert state["project_binding"]["project_id"] == "YANG_MILLS_MASS_GAP"
    assert state["project_binding"]["adoption_mode"] == "MIGRATION_GOVERNED"
    assert state["standing_mandate"]["active"] is True
    assert state["standing_mandate"]["owner_technical_certification_required"] is False
    assert state["authority_policy"]["generic_approved_flag_prohibited"] is True
    assert state["risk_and_action"] == {**state["risk_and_action"], "active_risk_tier": "T4", "active_action_class": "B"}
    assert migration["base_state"]["base_candidate_id"] == "b64957789a1feaab096e08ab0b07e5acb1acf832"
    assert "5e3024b13cf531a70910956b86fcdfc9e0ad3abb" in read("GOVERNANCE_STATE.yaml")
    assert "5e3024b13cf531a70910956b86fcdfc9e0ad3abb" in read("governance/MIGRATION_RECEIPT_YM-GOV-300.md")
    assert objective["objective"]["exact_objective"].startswith("Adversarially audit every quarantined")
    assert objective["completion_record"]["release_eligibility_effect"] == "UNBLOCKS_YM-002F"


def test_gc_01_to_gc_30_conformance_boundaries():
    state = yaml.safe_load(read("GOVERNANCE_STATE.yaml"))["governance_state"]
    intent = read("PROJECT_INTENT.md")
    architecture = read("ARCHITECTURE_DECISIONS.md")
    roadmap = read("ROADMAP.md")
    migration = read("governance/MIGRATION_RECEIPT_YM-GOV-300.md")
    mapping = yaml.safe_load(read("governance/EVIDENCE_MAPPING_v3.0.0.yaml"))
    claim_audit = read("verification/YM-002E_CLAIMED_SOLUTION_ADVERSARIAL_AUDIT.md")
    task_graph = read("TASK_GRAPH.md")
    current = read("CURRENT_SCIENTIFIC_STATE.md")

    files = [
        "GOVERNANCE_STATE.yaml",
        "PROJECT_INTENT.md",
        "ARCHITECTURE_DECISIONS.md",
        "ROADMAP.md",
        "governance/envelopes/YM-GOV-300.yaml",
        "governance/envelopes/YM-002E.yaml",
        "governance/EVIDENCE_MAPPING_v3.0.0.yaml",
        "governance/OWNER_ACTION_RECLASSIFICATION_YM-GOV-300.md",
        "governance/CAPABILITY_ASSURANCE_MATRIX.md",
        "governance/project-governance.yaml",
        "governance/MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md",
        "governance/HUMAN_OWNER_ACCEPTANCE_ROS_v1.0_20260830.md",
        "EVIDENCE_LEDGER.md",
        "NEGATIVE_EVIDENCE_REGISTER.md",
        "literature/CLAIM_QUARANTINE_REGISTER.md",
    ]
    checks = {
        "GC-01": state["project_binding"]["project_id"] == "YANG_MILLS_MASS_GAP",
        "GC-02": state["project_binding"]["repository_or_workspace"] == str(ROOT),
        "GC-03": "OWNER_INTENT_CONFIRMED" in intent and state["direction"]["project_intent"]["owner_intent_confirmed"],
        "GC-04": state["standing_mandate"]["owner_technical_certification_required"] is False,
        "GC-05": all(x in state["authority_policy"] for x in ("owner_intent_authority", "implementation_authority", "verification_authority")),
        "GC-06": "GOVERNANCE_MIGRATION != SCIENTIFIC_PROGRESS" in architecture,
        "GC-07": "dependencies" in read("governance/envelopes/YM-002E.yaml"),
        "GC-08": all(x in state["blockers"][0] for x in ("id", "class", "detail")),
        "GC-09": state["risk_and_action"]["active_risk_tier"] == "T4" and state["risk_and_action"]["active_action_class"] == "B",
        "GC-10": "assurance_contract" in read("governance/envelopes/YM-GOV-300.yaml"),
        "GC-11": "## 10. Quality priorities" in intent and "roadmap" in state["direction"],
        "GC-12": all(x in mapping["dimensions"] for x in ("strength", "independence")),
        "GC-13": state["evidence_policy"]["candidate_binding_required"] is True,
        "GC-14": state["evidence_policy"]["stale_evidence_fails_closed"] is True,
        "GC-15": "ACCEPTED" in migration and "raw transcript" in migration.lower(),
        "GC-16": "owner_technical_certification_required: false" in read("GOVERNANCE_STATE.yaml").lower(),
        "GC-17": "152 passed" in migration or "152" in current,
        "GC-18": "NO_UNSUPPORTED_SOLUTION_CLAIM_ACCEPTED" in claim_audit,
        "GC-19": "release_blocking" in read("governance/envelopes/YM-002E.yaml"),
        "GC-20": state["release"]["release_eligible"] is False and state["release"]["deployment_authorized"] is False,
        "GC-21": all(x in state["release"] for x in ("exact_candidate_id", "current_state", "hard_gates_state")),
        "GC-22": state["git_or_checkpoint"]["force_push_prohibited"] is True,
        "GC-23": all((ROOT / x).exists() for x in files),
        "GC-24": "154" in migration and "non-reproducible historical" in migration,
        "GC-25": "OWNER-PUBLICATION" in read("governance/OWNER_ACTION_RECLASSIFICATION_YM-GOV-300.md"),
        "GC-26": "Remotes: none configured" in migration,
        "GC-27": "Declared limitations" in migration,
        "GC-28": "Fresh independent migration review" in migration,
        "GC-29": "YM-002E" in roadmap and "YM-002F" in roadmap,
        "GC-30": state["release"]["current_state"] == "NOT_RELEASE_ELIGIBLE" and "No public release" in migration,
    }
    assert all(checks.values()), {key: value for key, value in checks.items() if not value}


def test_migration_and_later_closeout_preserve_release_boundaries():
    task_graph = read("TASK_GRAPH.md")
    current = read("CURRENT_SCIENTIFIC_STATE.md")
    state = yaml.safe_load(read("GOVERNANCE_STATE.yaml"))["governance_state"]

    assert "YM-002E" in task_graph and "INDEPENDENTLY_VERIFIED / CLOSED" in task_graph
    assert "YM-002F" in task_graph and "READY" in task_graph
    assert "YM-002E = INDEPENDENTLY_VERIFIED / CLOSED" in current
    assert state["direction"]["active_objective_id"] == "YM-002F"
    assert state["release"]["current_state"] == "NOT_RELEASE_ELIGIBLE"


def test_historical_count_and_scientific_fingerprint_are_explicitly_preserved():
    text = read("governance/MIGRATION_RECEIPT_YM-GOV-300.md")
    assert "154 reported tests" in text
    assert "152 passed" in text
    assert "f30a330063b2ca0af772582e318bddd70af9f8c7d9e6d28c1c811c052d156474" in text
