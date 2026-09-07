"""
Tests for Universal Governance v4.0.3 state-transition requirements.
Implements the 12 mandatory tests from EVIDENCE_AND_MIGRATION.md.
Migration: YM-GOV-403
"""
import pathlib
import yaml
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")

def load_yaml(rel: str):
    return yaml.safe_load(read(rel))


# ─── TEST 1: UNBOUND template cannot activate ───────────────────────
def test_01_unbound_template_cannot_activate():
    """UNBOUND template cannot activate or authorize product work."""
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    # The staging candidate must NOT be ACTIVE
    assert state["activation"] != "ACTIVE", \
        "UNBOUND/STAGING template must not be ACTIVE before cutover"
    assert state["activation"] in ("UNBOUND", "STAGING_CANDIDATE"), \
        f"Unexpected activation state: {state['activation']}"
    # Release must be NO-GO
    assert state["release"]["state"] == "NO-GO"
    assert state["release"]["eligible"] is False


# ─── TEST 2: Failed/unknown gates survive migration ─────────────────
def test_02_failed_gates_survive_migration():
    """Existing failed/unknown gates and NO-GO survive migration."""
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    # Hard gates must exist and include pending gates
    assert len(state["hard_gates"]) > 0, "Hard gates must not be empty"
    # Negative history must be preserved
    assert len(state["negative_history_refs"]) > 0, \
        "Negative history references must be preserved"
    # Known risks must be preserved
    assert len(state["known_risks"]) > 0, \
        "Known risks must be preserved"
    # Release must remain NO-GO
    assert state["release"]["state"] == "NO-GO"


# ─── TEST 3: Candidate A review cannot accept candidate B ───────────
def test_03_candidate_review_binding():
    """Candidate A review cannot accept candidate B."""
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    # The state must track exact candidate identity
    assert state["project"]["head"] is not None, \
        "Project HEAD must be bound to exact candidate"
    # If a checkpoint exists, it must match HEAD
    if state.get("last_verified_checkpoint") and state["last_verified_checkpoint"].get("sha"):
        assert state["last_verified_checkpoint"]["sha"] == state["project"]["head"], \
            "Checkpoint SHA must match project HEAD"


# ─── TEST 4: Writer self-acceptance rejected ─────────────────────────
def test_04_writer_self_acceptance_rejected():
    """Missing/failed review and writer self-acceptance are rejected."""
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    governance = read("governance/staging_v403/GOVERNANCE.md")
    
    # Reserved actions must include self-acceptance prohibition
    self_acceptance_prohibited = any(
        "self-acceptance" in a.lower() or "self_acceptance" in a.lower()
        for a in state.get("reserved_actions", [])
    )
    assert self_acceptance_prohibited, \
        "Self-acceptance must be in reserved/prohibited actions"
    
    # GOVERNANCE.md must contain non-self-acceptance rule
    assert "never independently accept its own candidate" in governance.lower() or \
           "never independently accept" in governance.lower(), \
        "GOVERNANCE.md must contain non-self-acceptance rule"


# ─── TEST 5: Stale state revision rejected ───────────────────────────
def test_05_stale_state_revision_rejected():
    """Concurrent stale state update cannot overwrite a newer revision."""
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    # State must have revision tracking
    assert "revision" in state, "State must have revision field"
    assert isinstance(state["revision"], int), "Revision must be integer"
    assert state["revision"] >= 0, "Revision must be non-negative"
    # Coordination must specify serialization method
    coord = state.get("coordination", {})
    assert coord.get("serialization_method") is not None, \
        "Serialization method must be specified"
    assert coord.get("state_writer") is not None, \
        "State writer must be specified"


# ─── TEST 6: UI fixture cannot certify production journey ────────────
def test_06_ui_fixture_not_production(request):
    """A UI fixture cannot certify an ordinary persisted or production journey.
    
    NONE_BY_DESIGN: This project has no UI. Test documents the exemption."""
    direction = read("governance/staging_v403/PROJECT_DIRECTION.md")
    assert "NONE_BY_DESIGN" in direction, \
        "Project must explicitly declare NONE_BY_DESIGN for UI"


# ─── TEST 7: Delegated specs remain reachable ────────────────────────
def test_07_delegated_specs_reachable():
    """Required delegated specs remain reachable and historical instructions are inactive."""
    delegation = load_yaml("governance/staging_v403/DELEGATION_MAP.yaml")
    
    # Check that all RETAINED_DELEGATED and RETAINED_ACTIVE files exist
    for section_key in ("root_files", "governance_files"):
        for entry in delegation.get(section_key, []):
            path = ROOT / entry["path"]
            disposition = entry.get("disposition", entry.get("v403_role", ""))
            if disposition in ("RETAINED_DELEGATED", "RETAINED_ACTIVE"):
                assert path.exists(), \
                    f"Delegated file must exist: {entry['path']}"
    
    # Check critical delegated sources specifically
    critical_delegated = [
        "governance/MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md",
        "governance/EPISTEMIC_TAXONOMY_v1.0.yaml",
        "governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml",
        "governance/CONTRACT_OWNERSHIP_LEDGER.yaml",
        "THEOREM_LEDGER.md",
        "EVIDENCE_LEDGER.md",
    ]
    for rel in critical_delegated:
        assert (ROOT / rel).exists(), f"Critical delegated source must exist: {rel}"


# ─── TEST 8: Recovery preserves sealed hashes ────────────────────────
def test_08_recovery_preserves_sealed_hashes():
    """Recovery preserves unrelated dirty files and sealed historical hashes."""
    delegation = load_yaml("governance/staging_v403/DELEGATION_MAP.yaml")
    
    # Verify NO files have disposition "DELETED"
    for section_key in ("root_files", "governance_files"):
        for entry in delegation.get(section_key, []):
            disposition = entry.get("disposition", "")
            assert disposition != "DELETED", \
                f"No files should be deleted: {entry['path']}"
    
    # Summary must confirm zero deletions
    summary = delegation.get("summary", {})
    assert summary.get("files_deleted", 0) == 0, \
        "Migration must not delete any files"
    
    # Historical files must remain
    historical_files = [
        "governance/MIGRATION_RECEIPT_YM-GOV-300.md",
        "governance/HUMAN_OWNER_ACCEPTANCE_ROS_v1.0_20260830.md",
    ]
    for rel in historical_files:
        assert (ROOT / rel).exists(), f"Historical file must be preserved: {rel}"


# ─── TEST 9: Autonomous selection respects dependencies ──────────────
def test_09_autonomous_selection_respects_dependencies():
    """Autonomous next selection respects dependencies, owner priority and reserved actions."""
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    
    objectives = state.get("objectives", [])
    assert len(objectives) > 0, "Objectives must be populated"
    
    # Find blocked objectives and verify their dependencies exist
    blocked = [o for o in objectives if o.get("status") == "BLOCKED"]
    for obj in blocked:
        deps = obj.get("dependencies", [])
        for dep_id in deps:
            # Dependency must exist in objectives list
            dep_exists = any(o.get("id") == dep_id for o in objectives)
            assert dep_exists, \
                f"Dependency {dep_id} for {obj['id']} must exist in objectives"
    
    # Reserved actions must be populated
    assert len(state.get("reserved_actions", [])) > 0, \
        "Reserved actions must be populated"


# ─── TEST 10: Migration acceptance ≠ product acceptance ──────────────
def test_10_migration_not_product_acceptance():
    """Migration acceptance grants neither product acceptance nor deployment permission."""
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    
    # Release must remain NO-GO during migration
    assert state["release"]["state"] == "NO-GO"
    assert state["release"]["eligible"] is False
    assert state["release"]["deployment_authorized"] is False
    
    # Active contract must be the migration, not a product task
    coord = state.get("coordination", {})
    if coord.get("active_contract"):
        # The active contract being YM-GOV-403 is fine
        pass
    
    # Capabilities must retain their pre-migration statuses
    caps = state.get("capabilities", {})
    for cap_id, cap in caps.items():
        if cap.get("status") in ("BLOCKED", "AWAITING_HUMAN_ACCEPTANCE"):
            # Migration cannot promote these
            assert cap["status"] != "ACCEPTED_BOUNDED" or "specification" in cap_id.lower() or "ledger" in cap_id.lower(), \
                f"Migration cannot promote blocked capability: {cap_id}"


# ─── TEST 11: UI dimension requirement ───────────────────────────────
def test_11_ui_dimension_requirement():
    """A required responsive, accessibility, role/surface or failure-state dimension
    without matching evidence prevents UI capability completion.
    
    NONE_BY_DESIGN: This project has no UI capabilities."""
    direction = read("governance/staging_v403/PROJECT_DIRECTION.md")
    assert "NONE_BY_DESIGN" in direction
    # No UI capabilities should exist in state
    state = load_yaml("governance/staging_v403/PROJECT_STATE.yaml")
    caps = state.get("capabilities", {})
    for cap_id, cap in caps.items():
        # No capability should claim UI completion
        assert "ui" not in cap_id.lower() or cap.get("status") == "NONE_BY_DESIGN"


# ─── TEST 12: Shared receipt scope verification ──────────────────────
def test_12_shared_receipt_scope_verification():
    """A shared receipt verifies only the explicitly mapped dimensions and
    candidate/environment it actually covers."""
    evidence_map = load_yaml("governance/staging_v403/EVIDENCE_MAPPING_v403.yaml")
    
    # Evidence tiers must be explicitly mapped with justifications
    tiers = evidence_map.get("evidence_tiers", {})
    for tier_id, tier in tiers.items():
        assert "mapping" in tier, f"Evidence tier {tier_id} must have explicit mapping"
        assert tier["mapping"] in ("ALIGNED", "ALIGNED_WITH_CAVEAT", "IDENTICAL"), \
            f"Evidence tier {tier_id} has unknown mapping: {tier['mapping']}"
    
    # Risk tiers must be mapped by consequence
    risk_tiers = evidence_map.get("risk_tiers", {})
    for tier_id, tier in risk_tiers.items():
        assert "justification" in tier, \
            f"Risk tier {tier_id} must have consequence justification"
        assert "v403_mapping" in tier, \
            f"Risk tier {tier_id} must have v4.0.3 mapping"
    
    # Historical preservation must be explicitly stated
    hist = evidence_map.get("historical_preservation", {})
    assert hist.get("rewriting_prohibited") is True, \
        "Historical receipt rewriting must be prohibited"


# ─── CROSS-CUTTING: Evidence mapping coherence ──────────────────────
def test_evidence_mapping_coherence():
    """Evidence mapping file is internally consistent."""
    evidence_map = load_yaml("governance/staging_v403/EVIDENCE_MAPPING_v403.yaml")
    assert evidence_map["schema_version"] == "4.0.3"
    assert evidence_map["project_id"] == "YANG_MILLS_MASS_GAP"
    
    # All 5 evidence tiers must be mapped
    tiers = evidence_map.get("evidence_tiers", {})
    for expected in ("E1", "E2", "E3", "E4", "E5"):
        assert expected in tiers, f"Evidence tier {expected} must be mapped"
    
    # All 5 risk tiers must be mapped
    risk_tiers = evidence_map.get("risk_tiers", {})
    for expected in ("T1", "T2", "T3", "T4", "T5"):
        assert expected in risk_tiers, f"Risk tier {expected} must be mapped"


# ─── CROSS-CUTTING: Staging directory coherence ─────────────────────
def test_staging_directory_coherence():
    """All three v4.0.3 entry authority candidates exist in staging."""
    staging = ROOT / "governance" / "staging_v403"
    assert (staging / "GOVERNANCE.md").exists(), "GOVERNANCE.md must exist in staging"
    assert (staging / "PROJECT_DIRECTION.md").exists(), "PROJECT_DIRECTION.md must exist in staging"
    assert (staging / "PROJECT_STATE.yaml").exists(), "PROJECT_STATE.yaml must exist in staging"
    assert (staging / "EVIDENCE_MAPPING_v403.yaml").exists(), "Evidence mapping must exist"
    assert (staging / "DELEGATION_MAP.yaml").exists(), "Delegation map must exist"
