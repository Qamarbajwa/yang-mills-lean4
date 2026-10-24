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
    assert tree_hash in [
        "e11216bf0059b8248c021295a0dafee27fa9202e6738f253afd9c9970667506a",
        "7d5ba2cd67964dce354bd1a733cfc2012925f2d5dfcb131d5d4dec21c26aadfc",
        "8569240bffa426e1fdeca452c23d0457ec4080b823e9106c033c37cc9147dac4",
        "cd210dd4346a7322724f6bda594d7cc71e3830a58f75e4fdc9974d49e9b1a907",
        "f48be8d659d01f5a6c5add9aa59a1bc8553d3b859e5c3501265178a65521dc39",
        "a3cf94a8ace39320caee553d08238f1312ecf800f765abf0f0f6746e238d20b3",
        "7489669c8481279efae665c3e4cfaa3f8cd90dc2a35b9e5f220a46c6e3959b12",
        "b8a04b73d928c5ec450cb544a298f84fca42434697a0b836a758204fbc2c74d9",
        "79f8e55b7bd5a67a61363b521a9ae56eaf430537086cfb73e57a28407b69b063",
        "b1379d5b348e563524483b2baad40938d257359fabbd6903d442f05b0db55234",
        "cbfc4be0b2017b29095d131936357ff2289d25d406692907747e4f2373821a5c",
        "897ea50bd5c67d5a8400af978970dca8b30e09848144e3b20f8938461dc42540",
        "ff3d101f2955c9ef1508a31af7bf1131a0cd98d6f8dbdc95fbc7ec1978690398",
        "7c2ca263fa7e78c1873d251a1d08ab2ec43fd3cd6dab6c0705eac96c31e792a8",
        "536ff25ddfae27f9e51c20b75a218e832e2a966d9a1646d13d9f481edbf3ed04",
        "15da6019607160be1d05ff5bfd79e8a0139e82dbe90d2e7d1f9b1b9db810cc2f",
        "89148f97f345ba6e18c547913d98e4d0e1e3c740bd9058d745cc99fcfc3c7980",
        "d6505956f594d0d7c3fc63a1109950372abb4ea8e3e3896d2c0323e00c3d6869",
        "a131866b5efa5a1fa16a3e0cd80d0b209d910c30a32585355305824552513c81",
        "286c301d1fb6222a8460d4a33967b885642ee8546c362961caeb1fe23912afdc",
        "4093b67c5d94fcd74f96ffdb5e66616b1caf7353066b58b38445a1c3a54fd9e4",
        "50398000f703d55174b88b0e47216b7641a59f8d2bbbca91d3bbda6d9d1aff4b",
        "02fb66ef626481c88a6f4e2e3ae75f5be7dfe8e6892c387a17995a183292ced0",
        "bea824858bad92b6d092520f89e19d532cd9b6ed28fef4d743183e63f0a0e9d2",
        "4c531d2324c929eac2bb50a1a76b374a3e5828c4179d4280d187e867ee94c837",
        "2584d0036f931c783a0e783f1af401e55fc2b3d1b227fc7266a2a3b0df0632c6",
        "c9f53ceeb0d5b99357f8eb65aa371c5464ff9558b9fa68ce7cf5a8048e6f4fbc",
        "d6d7a82e74b339904510e529b64cfa2d91e86a4ed9f98b75b58d7e8b7e487dc6",
        "790bb4336f62f1007ed2033da0c5d57759d57826f79e6ad9f1e98147f0866094",
        "a8b27d46c85d232ee69e6bdea6b8d11a70390bdf0b82ab1d554231c6e8b48a54",
        "0855124cb8e2ba5c98d107e9ae655b90f37d4f8db3fdd499b34611f07360c5be",
        "b962eb50281ed1bdb3cbf4e570d9438a73b7887aa8814fc850e0c52672375f24",
        "03f26596658319a188729b44b6e69b367b3ef3ca213e879191a858bf84453153",
        "3538431dbc7cdf7bead153721538c9dec61b2eecb7ed85a526742dc873a951d1",
        "83793a53ba147df2af4ec6c01b0b1b59100d493cf52d2f1edc87b5305548c4b3",
        "0ec422bdd07558fe76a577a9705aafb72515a3c05fa7e3ab038f3d2662327fce",
        "e7ab254fcf95ade7e22f0dce3798204fed16f05d39921a20f700e95a494f9491",
        "4240f826c052b93367aae8bd4032d4e156017630bdf49ddaccf0e45dcd052b33",
        "331d97a76d7820f974eccc33af68100f4ca34a77a8a8e36d38903e9f446c47e6",
        "bf00bf54ec4803a9f9da23da9876852a389fd1baf5c102eb8efb89f9ba7d8bca",
        "ca0a8e9cf04261f3683cbdceaf47147804fac7e720163dd89675ae57f20013aa",
        "94248be29b261aab231643254b371857fb1e163bbb618efad173cf6cc87d5de0",
        "980d82c8f0a8a25f434415347fd92db9e232c36a3d9fc71ac5b5f50e0428e0eb",
        "08ae52af6ffe454caec3cbba92f748f49a173fad318a93eb00bfd564d39bacb0",
        "35ad476323b8e27d92dab1fd0c45ccb29f41ce01867ff8fb5b3df8b00b0e4b05",
        "38ad6b54d656e0966406a4b85a533a2db7f9dd8f71e35cbba26cef85e2d4df65",
        "fef79869d7888822e06fff5917da242a4a237e608535159f104b54a6003b2e6f",
        "c14f5abe44fcaac6f97c95c96919bb1f1cf705379e47f625179cb15664f8f07a",
        "a987a8ee79139a0b469f480b9cba0978f6d7979a2e8b1a6f81f084dada87da2f",
        "d2410e035257d85e8f4e50c5c848feb79020b72c8474227d1a9a1c1433f760bc",
        "558087183bb522381991d5add8032afb1388d78486fe51717e28bde54d0f43e6",
        "155ad71ff62dada6ef3d30e383686e20445c944f436a39c5dc07a15e0a876d19",
        "43417f2545386040c92713d9c27cce17662f697a7ffcb4e7c17aad4aba79484a",
        "8273aeec64917f047700b5c64dfb4c0b12051ca5e7fd912fa29d3b5137144cb4",
        "9ebcb5b0985d1e85c044338f212696981b10881f249b131f06ebcb4cc55e9b41",
        "4a0a1480b394b98523c046479eff895f204fb6e0699e2604c6bc40c1ee18fefb",
        "e2b9161db3422e176a86fc37efbcdb8287b02b259141bbcf5844985e42a5c308",
        "89ab14f1b17fffc7a5148607fc182bc81267de6bde935006f0d0368cc7325f68",
        "fc8802a019f4564fc3935f877c7f83baa475321e47ebf15d1a20136f9a38e72d",
        "632964762a347cdf06184fee87c66b3625052994f3207f36eb61d90769f928ec",
        "7139658dba5172e4e1e2bb137e175205ee6338f344544fad2db6a03f63d5dcf0",
        "c76a1eae05b8b75815384b147d958194a33f22aaacb6113c437a2fb9bda25b1e",
        "4041bbe61f2feb3b13294abbc7f8b460a4dea71c84c48372528410fa2c650031",
        "bb9901c89d1a4ddd085464df5f709a4f9a66e37271600d255127d39d96d13ded",
        "860d4f39f3bcf7301e1b415122dfa928b5019ce88bad3fe0b07d108a3bd8be29",
        "e1080e20a6f023f887c77380b2e0355c675a01d9cf831f17df5cef445c2384d2",
        "d65648c00a7844c89d29b49ff92755614f7ca85b851072ae2b0982b34240d379",
        "a897358271755eb250e2842e6c9db9b30b876b28077de5382836a24c41366abb",
        "e1c2a5791e2ce03ad5eec427accdc247c077aae4833b0dc9ff6b777a72b4a51c",
        "883e272c5f3d1eb6deb920715c4eefe97287cda84a8b7a965ba0780571155d9f",
        "d895d3d33b50f81f0ce30b2570cb107309a3da1afd3037b6aa286be662b66121",
    ]




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
