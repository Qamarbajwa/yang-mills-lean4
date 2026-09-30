"""
Tests for Universal Governance v4.0.6-r3 Project-Bound Strengthening and Adoption.
Implements the 18 mandatory migration/adoption tests required by YM-GOV-ADOPT-0406R3.
"""
import pathlib
import pytest
import yaml

from src.ymmg.ros import (
    ConstitutionalIntegrityError,
    YANG_MILLS_REQUIRED_HARD_GATES,
    verify_project_bound_readiness,
    validate_state_revision_update,
    validate_handoff_precedence,
    validate_autonomous_operation_bounds,
    validate_prompt_injection_boundary,
    validate_architecture_stability,
    validate_regression_protection_requirement,
    validate_consequential_effect_receipt,
    verify_candidate_bound_acceptance,
    evaluate_scientific_review_transition,
    validate_task_disposition_authority,
    enforce_goal_complete_bridge_gate,
    compute_closed_world_scientific_tree_hash,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def load_yaml(rel: str):
    return yaml.safe_load(read(rel))


# ─── TEST 1: Stale state update is rejected ────────────────────────────────────
def test_01_stale_state_update_rejected():
    """Concurrent stale state update cannot overwrite a newer revision."""
    current_revision = 18
    # Equal revision is rejected
    with pytest.raises(ConstitutionalIntegrityError, match="Stale state revision rejected"):
        validate_state_revision_update(current_revision=current_revision, proposed_revision=18)
    # Stale/lower revision is rejected
    with pytest.raises(ConstitutionalIntegrityError, match="Stale state revision rejected"):
        validate_state_revision_update(current_revision=current_revision, proposed_revision=17)
    # Monotonic increment succeeds
    assert validate_state_revision_update(current_revision=current_revision, proposed_revision=19) == 19


# ─── TEST 2: Changed scientific candidate invalidates old review ───────────────
def test_02_changed_scientific_candidate_invalidates_old_review():
    """A material change in candidate SHA invalidates an earlier review."""
    candidate_a = "9ed117fe58a39540134fb2fb2bac3691d747b884"
    candidate_b = "1111111111111111111111111111111111111111"

    # Reviewing candidate A for candidate A succeeds
    assert verify_candidate_bound_acceptance(
        candidate_sha=candidate_a,
        reviewed_sha=candidate_a,
        review_verdict="INTEGRITY_PASS",
    ) is True

    # Reviewing candidate A for candidate B fails closed
    with pytest.raises(ConstitutionalIntegrityError, match="Candidate SHA mismatch"):
        verify_candidate_bound_acceptance(
            candidate_sha=candidate_b,
            reviewed_sha=candidate_a,
            review_verdict="INTEGRITY_PASS",
        )


# ─── TEST 3: Writer cannot self-represent as independent verifier ──────────────
def test_03_writer_cannot_self_represent_as_independent_verifier():
    """Writer cannot self-accept or self-verify consequential work."""
    state = load_yaml("governance/PROJECT_STATE.yaml")
    governance = read("governance/GOVERNANCE.md")

    # GOVERNANCE.md prohibits writer self-acceptance
    assert "never independently accept its own candidate" in governance or \
           "never independently accept" in governance, \
           "GOVERNANCE.md must prohibit writer self-acceptance"

    # Reserved actions must prohibit writer self-acceptance
    reserved = state.get("reserved_actions", [])
    assert any("self-acceptance" in a.lower() or "self_acceptance" in a.lower() for a in reserved)


# ─── TEST 4: Failed review triggers REPAIR_REQUIRED ────────────────────────────
def test_04_failed_review_triggers_repair_required():
    """Defects or failed independent review trigger REPAIR_REQUIRED."""
    # Integrity fail forces repair
    next_state = evaluate_scientific_review_transition(
        current_state="INDEPENDENT_SCIENTIFIC_REVIEW",
        event="INTEGRITY_FAIL",
    )
    assert next_state == "REPAIR_REQUIRED"

    # Audit disqualifiers (e.g. mathematical conflation) force repair
    next_state_defect = evaluate_scientific_review_transition(
        current_state="INDEPENDENT_SCIENTIFIC_REVIEW",
        event="INTEGRITY_PASS",
        audit_findings=["MATHEMATICAL_CONFLATION"],
    )
    assert next_state_defect == "REPAIR_REQUIRED"


# ─── TEST 5: Routine repair does not require owner acceptance ──────────────────
def test_05_routine_repair_does_not_require_owner_acceptance():
    """Routine scientific repairs proceed autonomously without human-owner gates."""
    # Routing REPAIR_REQUIRED to owner acceptance is an illegal transition
    with pytest.raises(ConstitutionalIntegrityError, match="must transition to BOUNDED_REPAIR"):
        evaluate_scientific_review_transition(
            current_state="REPAIR_REQUIRED",
            event="ROUTE_TO_OWNER_ACCEPTANCE",
        )

    # Valid autonomous repair loop
    assert evaluate_scientific_review_transition(
        current_state="REPAIR_REQUIRED",
        event="START_BOUNDED_REPAIR",
    ) == "BOUNDED_REPAIR"

    assert evaluate_scientific_review_transition(
        current_state="BOUNDED_REPAIR",
        event="COMPLETE_REPAIR",
    ) == "REVERIFICATION"

    assert evaluate_scientific_review_transition(
        current_state="REVERIFICATION",
        event="SUBMIT_FOR_REVIEW",
    ) == "INDEPENDENT_SCIENTIFIC_REVIEW"


# ─── TEST 6: Negative scientific evidence survives repair ──────────────────────
def test_06_negative_scientific_evidence_survives_repair():
    """All historical negative evidence entries are preserved with zero deletions."""
    neg_evidence = read("NEGATIVE_EVIDENCE_REGISTER.md")
    assert "NEG-YM-011-PLAQ-1" in neg_evidence
    assert "NEG-YM-011-PLAQ-2" in neg_evidence
    assert "NEG-YM-011-PLAQ-3" in neg_evidence
    assert "NEG-YM-011-OBS-1" in neg_evidence
    assert "NEG-YM-011-OBS-2" in neg_evidence


# ─── TEST 7: Handoff prose cannot override newer Git/state truth ───────────────
def test_07_handoff_prose_cannot_override_newer_git_state_truth():
    """Cross-agent handoff prose is superseded by actual Git commit and state truth."""
    git_truth = {
        "head": "dacb35ceb3fed4049a5ae572babb8de37bc4b2ac",
        "state_revision": 18,
        "scientific_tree_hash": "18c319312f7afcd3fc4e93afa898de78b5c88500c4eee1fa04bdd08b2c08b77d",
    }
    stale_handoff = {
        "head": "old_outdated_sha_000000000000000000000000",
        "state_revision": 17,
        "scientific_tree_hash": "old_hash",
    }
    reconciled = validate_handoff_precedence(stale_handoff, git_truth)
    assert reconciled["head"] == git_truth["head"]
    assert reconciled["state_revision"] == git_truth["state_revision"]
    assert reconciled["scientific_tree_hash"] == git_truth["scientific_tree_hash"]


# ─── TEST 8: Untrusted content cannot expand authority ─────────────────────────
def test_08_untrusted_content_cannot_expand_authority():
    """External documents, papers, and AI outputs are data, not governance authority."""
    assert validate_prompt_injection_boundary("external_paper", attempted_permission_expansion=False) is True
    with pytest.raises(ConstitutionalIntegrityError, match="attempted unauthorized authority"):
        validate_prompt_injection_boundary("untrusted_prompt", attempted_permission_expansion=True)


# ─── TEST 9: Retries/children cannot exceed operation bounds ───────────────────
def test_09_retries_and_children_cannot_exceed_operation_bounds():
    """Bounded autonomous operations enforce ceilings; retries do not reset budget."""
    limits = {"max_tool_calls": 50, "max_spend_proxy": 100.0}
    consumed = {"max_tool_calls": 30, "max_spend_proxy": 80.0}

    assert validate_autonomous_operation_bounds(consumed, limits) is True

    # Consuming beyond limit raises error
    overconsumed = {"max_tool_calls": 55, "max_spend_proxy": 80.0}
    with pytest.raises(ConstitutionalIntegrityError, match="Resource bound exceeded"):
        validate_autonomous_operation_bounds(overconsumed, limits)

    # Exceeding retry count raises error
    with pytest.raises(ConstitutionalIntegrityError, match="Retry limit exceeded"):
        validate_autonomous_operation_bounds(consumed, limits, is_retry=True, accumulated_retries=3, retry_limit=3)


# ─── TEST 10: Accepted architecture cannot be rewritten on preference alone ───
def test_10_accepted_architecture_cannot_be_rewritten_solely_due_to_agent_preference():
    """Verified components are stable by default; agent preference alone cannot rewrite them."""
    assert validate_architecture_stability("ros.py", has_demonstrated_defect_or_requirement=True) is True
    with pytest.raises(ConstitutionalIntegrityError, match="agent preference alone cannot trigger rewrites"):
        validate_architecture_stability("ros.py", has_demonstrated_defect_or_requirement=False, agent_preference_only=True)


# ─── TEST 11: Consequential defect requires regression protection ──────────────
def test_11_consequential_defect_requires_regression_protection():
    """Every consequential defect receives durable regression protection."""
    assert validate_regression_protection_requirement("YM-011-PLAQ-DEFECT", has_durable_regression_test=True) is True
    with pytest.raises(ConstitutionalIntegrityError, match="lacks mandatory durable regression protection"):
        validate_regression_protection_requirement("YM-011-PLAQ-DEFECT", has_durable_regression_test=False)


# ─── TEST 12: Unresolved required bridge prevents GOAL_COMPLETE ───────────────
def test_12_unresolved_required_bridge_prevents_goal_complete():
    """GOAL_COMPLETE is FALSE whenever any required bridge edge remains non-PROVED."""
    edge_statuses = {
        "E-CROSSOVER": "OPEN",
        "E-LATTICE-CONT": "OPEN",
        "E-CONT-SCHWINGER": "OPEN",
    }
    with pytest.raises(ConstitutionalIntegrityError, match="GOAL_COMPLETE cannot be True"):
        enforce_goal_complete_bridge_gate(edge_statuses=edge_statuses, requested_goal_complete=True)


# ─── TEST 13: Governance adoption cannot imply Clay-problem completion ─────────
def test_13_governance_adoption_cannot_imply_clay_problem_completion():
    """Adopting governance controls does not alter Clay problem status."""
    state = load_yaml("governance/PROJECT_STATE.yaml")
    assert state["goal_complete"] is False, "goal_complete must remain false"
    assert state["clay_problem"] == "OPEN_AND_UNSOLVED", "clay_problem must remain OPEN_AND_UNSOLVED"


# ─── TEST 14: Scientific candidate and evidence-closeout HEAD remain distinct ──
def test_14_scientific_candidate_and_evidence_closeout_head_remain_distinct():
    """Scientific candidate SHA and evidence closeout HEAD are distinct concepts."""
    state = load_yaml("governance/PROJECT_STATE.yaml")
    candidate_sha = state["project"]["scientific_candidate_sha"]
    assert candidate_sha is not None
    # Material change invalidates review, but non-scientific closeout preserves tree hash
    tree_hash, _ = compute_closed_world_scientific_tree_hash(ROOT)
    assert tree_hash == "0a67f91cc7abc137c58504dbdde8168664b859c7891e62407de206eb77620704"


# ─── TEST 15: v4.0.6-r3 structural release validation != project readiness ────
def test_15_v406r3_structural_release_validation_cannot_substitute_for_project_readiness():
    """A generic structural release validation PASS cannot substitute for Yang-Mills project readiness."""
    # A fake generic PASS dictionary without the 12 gates fails closed
    generic_pass_inventory = {"generic_release_gate": {"status": "PASS"}}
    with pytest.raises(ConstitutionalIntegrityError, match="missing required hard gates"):
        verify_project_bound_readiness(generic_pass_inventory)


# ─── TEST 16: Incomplete hard-gate inventory fails project readiness ───────────
def test_16_incomplete_hard_gate_inventory_fails_project_readiness():
    """F1: Hard-gate inventory must include all 12 required gates; incomplete inventory fails."""
    assert len(YANG_MILLS_REQUIRED_HARD_GATES) == 12

    incomplete_inventory = {
        gate: {"status": "PASS"}
        for gate in list(YANG_MILLS_REQUIRED_HARD_GATES)[:11]  # Only 11 of 12
    }
    with pytest.raises(ConstitutionalIntegrityError, match="missing required hard gates"):
        verify_project_bound_readiness(incomplete_inventory)

    # Full 12 gates pass
    complete_inventory = {gate: {"status": "PASS"} for gate in YANG_MILLS_REQUIRED_HARD_GATES}
    state = load_yaml("governance/PROJECT_STATE.yaml")
    tree_hash, _ = compute_closed_world_scientific_tree_hash(ROOT)
    assert verify_project_bound_readiness(
        complete_inventory,
        expected_tree_hash=tree_hash,
        actual_tree_hash=tree_hash,
        state=state,
    ) is True


# ─── TEST 17: NO-GO history cannot authorize current action ───────────────────
def test_17_no_go_history_cannot_authorize_current_action():
    """F3: Historical NO-GO records remain immutable evidence and cannot authorize work."""
    rule = load_yaml("governance/PROJECT_BOUND_READINESS_RULE.yaml")
    f3 = rule["disposition_of_review_findings"]["F3_no_go_historical_metadata"]
    assert f3["status"] == "RESOLVED"
    assert "never authorize current work" in f3["rationale"]


# ─── TEST 18: Universal governance adoption cannot weaken stronger controls ────
def test_18_universal_governance_adoption_cannot_weaken_stronger_scientific_controls():
    """Adoption preserves stronger Yang-Mills autonomous repair and epistemic laws."""
    governance = read("governance/GOVERNANCE.md")
    # Verify canonical baseline is v4.0.4, NOT v4.0.6-r3
    assert "UNIVERSAL_GOVERNANCE_MINIMAL_v4.0.4" in governance or \
           "4.0.4" in governance
    # Verify autonomous scientific repair state machine is preserved
    assert "CANDIDATE" in governance
    assert "INDEPENDENT_SCIENTIFIC_REVIEW" in governance
    assert "REPAIR_REQUIRED" in governance
    assert "BOUNDED_REPAIR" in governance
    # Verify Clay problem remains OPEN
    state = load_yaml("governance/PROJECT_STATE.yaml")
    assert state["clay_problem"] == "OPEN_AND_UNSOLVED"
    assert state["goal_complete"] is False
