"""
Regression test suite for YM-GOV-014:
Autonomous Scientific Repair and Acceptance-Authority Correction.

Tests the 8 mandatory governance and mathematical integrity requirements:
1. A task with scientific defects cannot enter AWAITING_HUMAN_OWNER_ACCEPTANCE.
2. A task with REPAIR_REQUIRED transitions to BOUNDED_REPAIR, not owner acceptance.
3. Candidate acceptance fails if candidate_sha != reviewed_sha.
4. YM-005 no longer conflates Markov generator spectral gap with physical Hamiltonian mass gap.
5. YM-005 canonical theorem statements contain no fabricated physical-unit guarantees (0.5 fm, 0.18 GeV^2, etc.).
6. YM-006 through YM-010 remain SCIENTIFIC_REVIEW_HOLD.
7. GOAL_COMPLETE is false whenever any required bridge edge is not PROVED.
8. YM-011 cannot enter active proof execution while its precursor status is unverified or while YM-011 is PROPOSED.
"""

from pathlib import Path
import pytest
import yaml

from ymmg.ros import (
    ConstitutionalIntegrityError,
    validate_task_disposition_authority,
    evaluate_scientific_review_transition,
    verify_candidate_bound_acceptance,
    enforce_goal_complete_bridge_gate,
    check_ym011_activation_eligibility,
)
from ymmg.precursor_flow import (
    compute_gradient_flow_lipschitz_constant,
    normalized_wilson_loop_range,
    normalized_wilson_trace_properties,
    evaluate_precursor_loop_perturbation_bound,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_1_defective_task_cannot_enter_awaiting_human_owner_acceptance():
    """
    Requirement 1: A task with scientific defects cannot enter AWAITING_HUMAN_OWNER_ACCEPTANCE.
    """
    with pytest.raises(ConstitutionalIntegrityError, match="cannot enter AWAITING_HUMAN_OWNER_ACCEPTANCE"):
        validate_task_disposition_authority(
            task_id="YM-005",
            proposed_state="AWAITING_HUMAN_OWNER_ACCEPTANCE",
            has_scientific_defects=True,
        )

    # Even without defects, AWAITING_HUMAN_OWNER_ACCEPTANCE is forbidden for routine scientific tasks
    with pytest.raises(ConstitutionalIntegrityError):
        validate_task_disposition_authority(
            task_id="YM-005",
            proposed_state="AWAITING_HUMAN_OWNER_ACCEPTANCE",
            has_scientific_defects=False,
        )

    # Disqualifying audit findings during review force REPAIR_REQUIRED
    next_state = evaluate_scientific_review_transition(
        current_state="INDEPENDENT_SCIENTIFIC_REVIEW",
        event="INTEGRITY_PASS",
        audit_findings=["MATHEMATICAL_CONFLATION"],
    )
    assert next_state == "REPAIR_REQUIRED"


def test_2_repair_required_transitions_to_bounded_repair_not_owner_acceptance():
    """
    Requirement 2: A task with REPAIR_REQUIRED transitions to BOUNDED_REPAIR, not owner acceptance.
    """
    next_state = evaluate_scientific_review_transition(
        current_state="REPAIR_REQUIRED",
        event="START_BOUNDED_REPAIR",
    )
    assert next_state == "BOUNDED_REPAIR"

    reverify_state = evaluate_scientific_review_transition(
        current_state=next_state,
        event="COMPLETE_REPAIR",
    )
    assert reverify_state == "REVERIFICATION"

    review_state = evaluate_scientific_review_transition(
        current_state=reverify_state,
        event="SUBMIT_FOR_REVIEW",
    )
    assert review_state == "INDEPENDENT_SCIENTIFIC_REVIEW"

    accepted_state = evaluate_scientific_review_transition(
        current_state=review_state,
        event="INTEGRITY_PASS",
        audit_findings=[],
    )
    assert accepted_state == "SCIENTIFICALLY_ACCEPTED"

    with pytest.raises(ConstitutionalIntegrityError, match="never to owner acceptance"):
        evaluate_scientific_review_transition(
            current_state="REPAIR_REQUIRED",
            event="ROUTE_TO_OWNER_ACCEPTANCE",
        )


def test_3_candidate_acceptance_fails_if_candidate_sha_differs_from_reviewed_sha():
    """
    Requirement 3: Candidate acceptance fails if candidate_sha != reviewed_sha.
    """
    with pytest.raises(ConstitutionalIntegrityError, match="Candidate SHA mismatch"):
        verify_candidate_bound_acceptance(
            candidate_sha="e64a4008567c2f7da318b44ef784d0266f9d6231",
            reviewed_sha="1f482f5ffdece5e140b92aff0636e89e710824b1",
            review_verdict="INTEGRITY_PASS",
        )

    # Matching SHAs and clean audit pass
    assert verify_candidate_bound_acceptance(
        candidate_sha="e64a4008567c2f7da318b44ef784d0266f9d6231",
        reviewed_sha="e64a4008567c2f7da318b44ef784d0266f9d6231",
        review_verdict="INTEGRITY_PASS",
        audit_findings=[],
    )


def test_4_ym005_does_not_conflate_markov_generator_gap_with_hamiltonian_gap():
    """
    Requirement 4: YM-005 no longer conflates Markov generator spectral gap
    with physical Hamiltonian mass gap.
    """
    synth_text = (REPO_ROOT / "literature" / "YM-005-FINAL-SYNTHESIS.md").read_text(encoding="utf-8")
    audit_text = (REPO_ROOT / "literature" / "YM-005-SPECTRAL-GAP-AND-DECAY-AUDIT.md").read_text(encoding="utf-8")
    record_text = (REPO_ROOT / "literature" / "YM-005-IR-BOUNDARY-RECORD.md").read_text(encoding="utf-8")

    # Old conflated sentence must be gone
    assert "The Markov diffusion generator $-\\mathcal{L}$ and the lattice transfer operator possess a strictly positive spectral gap:\n  $$\\Delta_{\\text{lat}}(\\beta) \\ge \\frac{1}{C_{\\text{PI}}(\\beta)} > 0$$" not in synth_text

    # Explicit non-conflation statements must be present across all three canonical YM-005 documents
    assert "Strict Operator Non-Conflation (`YM-005-R1` Repair)" in synth_text
    assert "\\operatorname{gap}_{L^2(\\mu_\\infty)}(-\\mathcal{L}) \\ne \\operatorname{gap}_{\\mathcal{H}_{\\text{phys}}}(H_{\\text{lat}})" in synth_text
    assert "Strict Non-Equivalence of the Four Lattice Gap/Decay Objects (`YM-005-R1` Repair)" in audit_text
    assert "non_conflation_invariant" in record_text


def test_5_ym005_canonical_theorems_contain_no_fabricated_physical_units():
    """
    Requirement 5: YM-005 canonical theorem statements contain no fabricated
    physical-unit guarantees (0.5 fm, 0.18 GeV^2, etc.).
    """
    ym005_files = [
        REPO_ROOT / "literature" / "YM-005-FINAL-SYNTHESIS.md",
        REPO_ROOT / "literature" / "YM-005-SPECTRAL-GAP-AND-DECAY-AUDIT.md",
        REPO_ROOT / "literature" / "YM-005-IR-BOUNDARY-RECORD.md",
        REPO_ROOT / "literature" / "YM-005-11-DIMENSIONAL-THEOREM-LEDGER.md",
        REPO_ROOT / "literature" / "YM-005-VISUAL-INTUITION-DATA.md",
    ]
    forbidden_unit_tokens = ["0.5\\text{ fm}", "0.5 fm", "0.18\\text{ GeV}^2", "0.18 GeV^2", "420\\text{ MeV}", "0.4 - 0.6\\text{ fm}"]
    for path in ym005_files:
        content = path.read_text(encoding="utf-8")
        for token in forbidden_unit_tokens:
            assert token not in content, f"Forbidden fabricated physical unit '{token}' found in {path.name}"


def test_6_ym006_through_ym010_remain_scientific_review_hold():
    """
    Requirement 6: YM-006 through YM-010 remain SCIENTIFIC_REVIEW_HOLD,
    and YM-005 is SCIENTIFICALLY_ACCEPTED.
    """
    state_data = yaml.safe_load((REPO_ROOT / "governance" / "PROJECT_STATE.yaml").read_text(encoding="utf-8"))
    obj_by_id = {obj["id"]: obj for obj in state_data["objectives"]}

    assert obj_by_id["YM-005"]["status"] == "SCIENTIFICALLY_ACCEPTED"
    assert obj_by_id["YM-005"]["scope_limitation"] == "WITH_REGULATED_SCOPE"

    for tid in ["YM-006", "YM-007", "YM-008", "YM-009", "YM-010"]:
        assert obj_by_id[tid]["status"] == "SCIENTIFIC_REVIEW_HOLD", f"{tid} must remain SCIENTIFIC_REVIEW_HOLD"


def test_7_goal_complete_is_false_whenever_any_bridge_edge_not_proved():
    """
    Requirement 7: GOAL_COMPLETE is false whenever any required bridge edge is not PROVED.
    """
    state_data = yaml.safe_load((REPO_ROOT / "governance" / "PROJECT_STATE.yaml").read_text(encoding="utf-8"))
    assert state_data.get("goal_complete") is False
    assert state_data.get("clay_problem") == "OPEN_AND_UNSOLVED"

    edge_statuses = {
        "E-UV-FREE": "PROVED",
        "E-UV-FREE-CONT": "PROVED",
        "E-UV-RG": "REGULATED_ONLY",
        "E-LATTICE-GAP": "REGULATED_ONLY",
        "E-CROSSOVER": "OPEN",
        "E-LATTICE-CONT": "OPEN",
        "E-CONT-SCHWINGER": "OPEN",
    }
    assert enforce_goal_complete_bridge_gate(edge_statuses, requested_goal_complete=False) is False

    with pytest.raises(ConstitutionalIntegrityError, match="GOAL_COMPLETE cannot be True"):
        enforce_goal_complete_bridge_gate(edge_statuses, requested_goal_complete=True)


def test_8_ym011_cannot_enter_active_proof_execution_while_proposed_or_precursor_unverified():
    """
    Requirement 8: YM-011 cannot enter active proof execution while its precursor
    status is unverified or while YM-011 is PROPOSED.
    """
    state_data = yaml.safe_load((REPO_ROOT / "governance" / "PROJECT_STATE.yaml").read_text(encoding="utf-8"))
    obj_by_id = {obj["id"]: obj for obj in state_data["objectives"]}

    assert obj_by_id["YM-011-PRE"]["status"] == "SCIENTIFICALLY_ACCEPTED"
    ym011_status = obj_by_id["YM-011"]["status"]
    assert "PROPOSED" in ym011_status

    with pytest.raises(ConstitutionalIntegrityError, match="precursor"):
        check_ym011_activation_eligibility(
            ym011_status="ACTIVE",
            precursor_ym011_pre_verified=False,
        )

    with pytest.raises(ConstitutionalIntegrityError, match="cannot enter active proof execution"):
        check_ym011_activation_eligibility(
            ym011_status=ym011_status,
            precursor_ym011_pre_verified=True,
        )


def test_precursor_flow_mathematical_properties():
    """
    Verifies the 3 mathematical points of YM-011-PRE:
    1. beta cancels identically under Lüscher (2010) convention (K = 2(d-1) = 6 in d=4),
       and remains linearly under unscaled action-gradient convention.
    2. Normalized Wilson loop trace lies in [-1, 1] (attaining negative values), NOT [0, 1].
    3. Pointwise and expectation bounds hold.
    """
    info_b1 = compute_gradient_flow_lipschitz_constant(d=4, n_colors=3, beta=1.5, convention="luscher_2010")
    info_b2 = compute_gradient_flow_lipschitz_constant(d=4, n_colors=3, beta=6.0, convention="luscher_2010")
    assert info_b1["beta_cancels"] is True
    assert info_b2["beta_cancels"] is True
    assert info_b1["K_constant"] == pytest.approx(6.0)
    assert info_b2["K_constant"] == pytest.approx(6.0)

    unscaled = compute_gradient_flow_lipschitz_constant(d=4, n_colors=3, beta=6.0, convention="unscaled_action_gradient")
    assert unscaled["beta_cancels"] is False
    assert unscaled["K_constant"] == pytest.approx(6.0 * 3.0 / 3.0)

    for n_col in (2, 3, 4):
        lo, hi = normalized_wilson_loop_range(n_col)
        assert lo < 0.0, f"Normalized Wilson loop trace for SU({n_col}) must take negative values"
        assert lo >= -1.0 and hi == 1.0

    bound_res = evaluate_precursor_loop_perturbation_bound(
        n_links=8, t_flow=0.01, lattice_spacing_a=1.0, d=4, n_colors=3, beta=6.0
    )
    assert bound_res["holds_pointwise"] is True
    assert bound_res["holds_in_expectation"] is True
    assert bound_res["holds_for_complex_and_real_trace"] is True
    assert bound_res["pointwise_bound"] == pytest.approx(6.0 * 8 * 0.01)


def test_9_ym_gov_015_mathematical_and_source_scope_closeout():
    """
    YM-GOV-015 Closeout Verification:
    1. YM-011-PRE-R1 proves K=2(d-1)=6 via Hilbert-Schmidt orthogonal projection
       (||P_{su(N)}||_HS = 1.0) and Lüscher generator normalization Tr(T^a T^b) = -1/2 delta^{ab},
       and distinguishes real W_t^R(C) from complex W_t^C(C).
    2. YM-005-R2 source-to-claim correspondence in YM-005-PRIMARY-SOURCE-MAP.md has zero
       Delta_lat >= C_PI^{-1} conflations and records the vacuum-normalized transfer-matrix
       eigenvalue ratio lambda_1(beta)/lambda_0(beta).
    3. Next observable-transfer task YM-011-OBS-MAP defines probability spaces (Omega_0, F_0, mu_0)
       and (Omega_1, F_1, mu_1) and pullback map B_{0->1}^* before any error bound.
    """
    source_map_text = (REPO_ROOT / "literature" / "YM-005-PRIMARY-SOURCE-MAP.md").read_text(encoding="utf-8")
    assert "\\Delta_{\\text{lat}}(\\beta) \\ge C_{\\text{PI}}(\\beta)^{-1}" not in source_map_text
    assert "\\Delta_{\\text{lat}} \\ge C_{\\text{PI}}^{-1}" not in source_map_text
    assert "Source-to-Claim Correspondence Matrix (`YM-005-R2`)" in source_map_text
    assert "\\frac{\\lambda_1(\\beta)}{\\lambda_0(\\beta)}" in source_map_text

    spec_text = (REPO_ROOT / "literature" / "YM-011-FIRST-LOAD-BEARING-LEMMA-SPECIFICATION.md").read_text(encoding="utf-8")
    assert "\\operatorname{Tr}(T^a T^b) = -\\frac{1}{2}\\delta^{ab}" in spec_text
    assert "W_t^{\\mathbb{C}}(C)" in spec_text and "W_t^{\\mathbb{R}}(C)" in spec_text
    assert "YM-011-OBS-MAP" in spec_text
    assert "\\mathcal{B}_{0\\to 1}^*" in spec_text

    trace_su2 = normalized_wilson_trace_properties(2)
    trace_su3 = normalized_wilson_trace_properties(3)
    assert trace_su2["is_genuinely_complex_valued"] is False
    assert trace_su3["is_genuinely_complex_valued"] is True

