"""
Deterministic Unit Tests for ChrysalisHostAdapter (CAP-010 / YM-ARCH-CHRYSALIS-001)
=====================================================================================
Validates in-memory dynamic research topology, marginal credit assignment,
operational invariant distillation, dual-custody cryptographic sign-off,
and UGM v4.1.0-r3 host adapter compliance.
"""

from fractions import Fraction
import pathlib
import pytest
import re

from src.ymmg.chrysalis_host_adapter import (
    ChrysalisHostAdapter,
    RECOGNIZED_MATHEMATICAL_DOMAINS,
    RESERVED_AUTONOMY_ACTIONS,
)
from src.ymmg.ros import ConstitutionalIntegrityError


@pytest.fixture
def adapter():
    """Provides a fresh ChrysalisHostAdapter instance with known secret salt."""
    return ChrysalisHostAdapter(secret_salt="TEST_SECRET_SALT_2026")


# ─── 1. In-Memory Dynamic Specialist Topology ─────────────────────────────────

def test_01_adapter_initialization(adapter):
    """Adapter initializes with empty in-memory topology and ledgers."""
    assert adapter.ephemeral_topology == {}
    assert adapter.credit_ledger == []
    assert adapter.invariant_cache == []
    assert adapter.active_leases == [] or isinstance(adapter.active_leases, dict)
    assert len(adapter.get_active_specialists()) == 0


def test_02_specialist_instantiation_allowed_domains(adapter):
    """Ephemeral specialist agents can be instantiated across all recognized QFT domains."""
    for domain in RECOGNIZED_MATHEMATICAL_DOMAINS:
        spec = adapter.instantiate_specialist(
            domain=domain,
            objective_scope="edge:E-CROSSOVER",
            tools=["rational_fraction_calculator"],
            parent_agent="primary_worker",
        )
        assert spec["specialist_id"].startswith(f"specialist-{domain.lower()}-")
        assert spec["domain"] == domain
        assert spec["status"] == "ACTIVE_IN_MEMORY"
        assert spec["in_memory_only"] is True
        assert "rational_fraction_calculator" in spec["tools"]

    active = adapter.get_active_specialists()
    assert len(active) == len(RECOGNIZED_MATHEMATICAL_DOMAINS)


def test_03_specialist_instantiation_rejects_unallowed_domains(adapter):
    """Instantiating an unapproved domain raises ValueError."""
    with pytest.raises(ValueError, match="Unrecognized mathematical domain"):
        adapter.instantiate_specialist(
            domain="ARBITRARY_GENERAL_LLM_HEURISTIC",
            objective_scope="edge:E-CROSSOVER",
        )


def test_04_specialist_instantiation_validates_scope(adapter):
    """Instantiating with empty objective_scope raises ValueError."""
    with pytest.raises(ValueError, match="objective_scope must be a non-empty string"):
        adapter.instantiate_specialist(
            domain="CLUSTER_EXPANSION",
            objective_scope="",
        )


def test_05_specialist_dissolution_lifecycle(adapter):
    """Dissolving a specialist marks status as DISSOLVED and updates active lists."""
    spec = adapter.instantiate_specialist(
        domain="TORON_MODULI",
        objective_scope="moduli:toron_vacuum",
    )
    spec_id = spec["specialist_id"]

    assert len(adapter.get_active_specialists(domain="TORON_MODULI")) == 1

    dissolved = adapter.dissolve_specialist(spec_id)
    assert dissolved["specialist_id"] == spec_id
    assert dissolved["status"] == "DISSOLVED"
    assert "dissolved_at" in dissolved

    # Active query must now return 0
    assert len(adapter.get_active_specialists(domain="TORON_MODULI")) == 0

    # Dissolving again or non-existent raises KeyError
    with pytest.raises(KeyError):
        adapter.dissolve_specialist("non-existent-id")


# ─── 2. Marginal Credit Assignment & Path Pruning ─────────────────────────────

def test_06_marginal_credit_positive_contraction(adapter):
    """A reduction in obstruction gap awards positive credit and accepts candidate."""
    # Example: reducing Schur downfolding remainder from 5/4 to 16707/19516
    prior = Fraction(5, 4)
    post = Fraction(16707, 19516)

    res = adapter.evaluate_marginal_credit(
        prior_metric=prior,
        post_metric=post,
        higher_is_better=False,
        metric_name="beta6_crossover_gap",
        task_ref="YM-096",
    )

    assert res["accepted"] is True
    assert res["delta_m"] > 0
    assert res["rationale"] == "POSITIVE_OBSTRUCTION_CONTRACTION"
    assert adapter.get_cumulative_credit(task_ref="YM-096") > 0


def test_07_marginal_credit_zero_or_negative_pruning(adapter):
    """Stagnant or increasing obstruction gap yields non-positive credit and prunes."""
    res = adapter.evaluate_marginal_credit(
        prior_metric=1.0,
        post_metric=1.2,
        higher_is_better=False,
        metric_name="cluster_expansion_weight",
    )

    assert res["accepted"] is False
    assert res["delta_m"] < 0
    assert res["rationale"] == "ZERO_OR_NEGATIVE_UTILITY_PRUNED"


def test_08_marginal_credit_higher_is_better_mode(adapter):
    """When higher_is_better is True, credit is awarded for increases in the metric."""
    res = adapter.evaluate_marginal_credit(
        prior_metric=0.15,
        post_metric=0.25,
        higher_is_better=True,
        metric_name="mass_gap_spectral_lower_bound",
    )

    assert res["accepted"] is True
    assert pytest.approx(res["delta_m"]) == 0.10


# ─── 3. Operational Invariant Distillation (ROS Law 4) ────────────────────────

def test_09_distill_operational_invariant_success(adapter):
    """Valid negative findings are distilled into immutable ROS Law 4 records."""
    finding = "Factorial renormalon growth sum (2n)! a_n diverges; requires non-perturbative trans-series completion."
    record = adapter.distill_operational_invariant(
        defect_id="NEG-YM-100",
        finding_statement=finding,
        obstruction_classification="RENORMALON_FACTORIAL_DIVERGENCE",
        bound_reference="Lemma YM-100F",
    )

    assert record["invariant_id"] == "INV-NEG-YM-100"
    assert record["defect_ref"] == "NEG-YM-100"
    assert record["immutable"] is True
    assert "| `NEG-YM-100` |" in record["append_table_row"]
    assert "RENORMALON_FACTORIAL_DIVERGENCE" in record["append_table_row"]

    all_invs = adapter.get_distilled_invariants()
    assert len(all_invs) == 1
    assert all_invs[0]["invariant_id"] == "INV-NEG-YM-100"


def test_10_distill_operational_invariant_rejects_invalid_inputs(adapter):
    """Rejects malformed defect IDs and non-descriptive trivial statements."""
    with pytest.raises(ValueError, match="Invalid defect_id"):
        adapter.distill_operational_invariant(
            defect_id="INVALID-DEFECT-FORMAT",
            finding_statement="Valid length statement describing the theoretical failure.",
        )

    with pytest.raises(ValueError, match="finding_statement must be a descriptive formal assertion"):
        adapter.distill_operational_invariant(
            defect_id="NEG-YM-099",
            finding_statement="Too short",
        )


# ─── 4. Cryptographic Dual-Custody Approval Verification ──────────────────────

def test_11_dual_custody_token_generation_and_verification(adapter):
    """Valid cryptographic dual-custody tokens verify correctly."""
    request_id = "REQ-CROSSOVER-CLOSEOUT-001"
    requester = "agent-primary-worker"
    reviewer = "agent-blind-reviewer"

    token = adapter.generate_dual_custody_token(
        request_id=request_id,
        requester_id=requester,
        reviewer_id=reviewer,
    )

    assert isinstance(token, str)
    assert len(token) == 64  # SHA-256 hex length

    # Verification must succeed
    assert adapter.verify_dual_custody_approval(
        request_id=request_id,
        requester_id=requester,
        reviewer_id=reviewer,
        cryptographic_token=token,
    ) is True

    # Tampered token must fail
    tampered_token = token[:-4] + "ffff"
    assert adapter.verify_dual_custody_approval(
        request_id=request_id,
        requester_id=requester,
        reviewer_id=reviewer,
        cryptographic_token=tampered_token,
    ) is False


def test_12_dual_custody_enforces_tri_agent_separation(adapter):
    """Self-review attempts violate Tri-Agent Separation and are strictly rejected."""
    same_actor = "agent-monolithic-compromised"

    with pytest.raises(ConstitutionalIntegrityError, match="Tri-Agent Separation violation"):
        adapter.generate_dual_custody_token(
            request_id="REQ-TAMPER",
            requester_id=same_actor,
            reviewer_id=same_actor,
        )

    assert adapter.verify_dual_custody_approval(
        request_id="REQ-TAMPER",
        requester_id=same_actor,
        reviewer_id=same_actor,
        cryptographic_token="dummy_token",
    ) is False


# ─── 5. UGM v4.1.0-r3 Autonomy Host Adapter Interface ─────────────────────────

def test_13_attest_control_planes_isolation(adapter):
    """attestControlPlanes verifies router/watchdog no-mutation and isolation."""
    valid_state = {
        "coordination": {
            "active_role_assignment": {
                "router_id": "gov-router-01",
                "watchdog_id": "gov-watchdog-01",
            }
        }
    }
    res = adapter.attestControlPlanes(valid_state, {})
    assert res["authenticated"] is True
    assert res["router_no_mutation"] is True
    assert res["watchdog_no_acceptance"] is True
    assert res["isolation_verified"] is True

    # Missing roles fail
    bad_state = {"coordination": {"active_role_assignment": {}}}
    bad_res = adapter.attestControlPlanes(bad_state, {})
    assert bad_res["authenticated"] is False


def test_14_authenticate_actors_role_separation(adapter):
    """authenticateActors enforces 5 unique, non-colliding role assignments."""
    valid_state = {
        "revision": 159,
        "coordination": {
            "active_role_assignment": {
                "worker_id": "worker-01",
                "reviewer_id": "reviewer-01",
                "acceptor_id": "acceptor-01",
                "router_id": "router-01",
                "watchdog_id": "watchdog-01",
            }
        },
    }
    res = adapter.authenticateActors(valid_state, {})
    assert res["authenticated"] is True
    assert res["state_revision"] == 159
    assert len(res["actor_ids"]) == 5

    # Colliding assignments fail
    colliding_state = {
        "revision": 159,
        "coordination": {
            "active_role_assignment": {
                "worker_id": "worker-01",
                "reviewer_id": "worker-01",  # Colliding
                "acceptor_id": "acceptor-01",
                "router_id": "router-01",
                "watchdog_id": "watchdog-01",
            }
        },
    }
    bad_res = adapter.authenticateActors(colliding_state, {})
    assert bad_res["authenticated"] is False
    assert bad_res["reason"] == "COLLIDING_ROLE_ASSIGNMENTS"


def test_15_scope_lease_lifecycle(adapter):
    """Exclusive scope lease acquisition and release."""
    req = {
        "scope": "edge:E-CROSSOVER",
        "objective_ref": "YM-101",
        "expected_revision": 159,
        "budget_ref": "BUDGET-001",
    }
    lease = adapter.acquireScopeLease(req)
    assert lease["exclusive"] is True
    assert lease["scope"] == "edge:E-CROSSOVER"
    assert lease["active"] is True

    # Conflicting lease on same scope raises PermissionError
    with pytest.raises(PermissionError, match="is already leased"):
        adapter.acquireScopeLease(req)

    # Release lease allows re-acquisition
    released = adapter.releaseScopeLease(lease)
    assert released is True
    assert lease["active"] is False


def test_16_authorize_mandate_reserved_action_denial(adapter):
    """Mandates with reserved actions (DEPLOY, SPEND, etc.) are strictly denied."""
    for reserved in RESERVED_AUTONOMY_ACTIONS:
        plan = {
            "action": reserved,
            "state_revision": 159,
            "subject_scope": "edge:E-CROSSOVER",
            "budget_ref": "BUDGET-001",
        }
        res = adapter.authorizeMandate(plan)
        assert res["authorized"] is False
        assert "ACTION_RESERVED" in res["reason"]

    # Allowed research action
    allowed_plan = {
        "action": "SOLVE_LEMMA",
        "state_revision": 159,
        "subject_scope": "edge:E-CROSSOVER",
        "budget_ref": "BUDGET-001",
    }
    ok_res = adapter.authorizeMandate(allowed_plan)
    assert ok_res["authorized"] is True
    assert ok_res["external_effects_disabled"] is True


def test_17_precode_authorization_verification(adapter):
    """Pre-code check requires SPEC_VERIFIED and DIAGRAM_LOCKED."""
    locked = {
        "status": "SPEC_VERIFIED",
        "diagram_first_status": "DIAGRAM_LOCKED",
        "diagram_lock_subject_digest": "SHA256_LOCK_DIGEST",
    }
    assert adapter.verifyPreCodeAuthorization(locked)["ok"] is True

    unverified = {
        "status": "UNVERIFIED",
        "diagram_first_status": "DIAGRAM_PENDING",
    }
    assert adapter.verifyPreCodeAuthorization(unverified)["ok"] is False


def test_18_step_execution_and_cas_commit(adapter):
    """Step execution produces candidate-bound receipts and CAS validates revision advancement."""
    review_plan = {
        "phase": "REVIEW",
        "actor_id": "reviewer-01",
        "objective_ref": "YM-101",
        "subject_scope": "edge:E-CROSSOVER",
        "state_revision": 159,
        "subject_digest": "SHA256_CANDIDATE_DIGEST",
    }
    receipt = adapter.executeStep(review_plan)
    assert receipt["outcome"] == "PASS"
    assert receipt["read_only"] is True
    assert receipt["reviewer_independence"] == "IND2"

    verify_proof = adapter.verifyReceipt({"receipt": receipt, "plan": review_plan})
    assert verify_proof["authentic"] is True
    assert verify_proof["candidate_bound"] is True

    # CAS Commit validation
    cas_payload = {
        "expected_revision": 159,
        "proposed_state": {"revision": 160},
        "reason": "ADVANCE_AUTONOMOUS_PHASE",
    }
    cas_res = adapter.commitStateCAS(cas_payload)
    assert cas_res["committed"] is True
    assert cas_res["new_revision"] == 160

    # Stale CAS Commit
    stale_payload = {
        "expected_revision": 159,
        "proposed_state": {"revision": 159},
    }
    stale_res = adapter.commitStateCAS(stale_payload)
    assert stale_res["committed"] is False


def test_19_topology_telemetry_export(adapter):
    """Full telemetry accurately reports counts of ephemeral specialists, credit, and invariants."""
    adapter.instantiate_specialist(domain="CLUSTER_EXPANSION", objective_scope="scope:test")
    adapter.evaluate_marginal_credit(prior_metric=10, post_metric=5)
    adapter.distill_operational_invariant(
        defect_id="DEF-YM-001",
        finding_statement="Detailed description of identified operational defect in cluster expansion.",
    )

    telemetry = adapter.export_topology_telemetry()
    assert telemetry["active_specialist_count"] == 1
    assert telemetry["credit_evaluations_count"] == 1
    assert telemetry["distilled_invariants_count"] == 1
    assert telemetry["cumulative_marginal_credit"] == 5.0
