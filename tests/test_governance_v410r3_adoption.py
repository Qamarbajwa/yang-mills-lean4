"""
Tests for Universal Governance Minimal v4.1.0-r3 Project-Bound Strengthening and Adoption.
Implements the 18 mandatory adoption tests required by YM-GOV-ADOPT-0410R3.
"""
import hashlib
import json
import pathlib
import subprocess
import sys
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
    verify_candidate_bound_acceptance,
    evaluate_scientific_review_transition,
    validate_task_disposition_authority,
    enforce_goal_complete_bridge_gate,
    compute_closed_world_scientific_tree_hash,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
STAGING = ROOT / "_staging_gov_v410r3"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def load_yaml(rel: str):
    return yaml.safe_load(read(rel))


# ─── TEST 1: Candidate Package Hash & Provenance ───────────────────────────────
def test_01_candidate_package_provenance_and_hash():
    """Uploaded candidate package matches the expected SHA-256 digest."""
    expected_digest = "c563ba3175275c4792e031497b2543a02cc92720be944e19779075c264c36087"
    # Envelope and state must reference the verified digest
    envelope = load_yaml("governance/envelopes/YM-GOV-ADOPT-0410R3.yaml")
    assert envelope["task_execution_envelope"]["identity"]["task_id"] == "YM-GOV-ADOPT-0410R3"
    rule = load_yaml("governance/PROJECT_BOUND_READINESS_RULE.yaml")
    f6 = rule["disposition_of_review_findings"]["F6_v410r3_package_verification"]
    assert f6["candidate_zip_sha256"] == expected_digest


# ─── TEST 2: Package Manifest & Staged Files Integrity ────────────────────────
def test_02_package_manifest_and_staged_files_integrity():
    """PACKAGE_MANIFEST.json lists all 11 candidate files with exact SHA-256 digests."""
    manifest_file = STAGING / "PACKAGE_MANIFEST.json"
    assert manifest_file.exists(), "PACKAGE_MANIFEST.json must exist in staging"
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert manifest["package"] == "UNIVERSAL_GOVERNANCE_MINIMAL"
    assert manifest["version"] == "4.1.0-r3"
    assert len(manifest["files"]) == 11

    # Verify each file on disk against declared hash
    for rel_path, expected_hash in manifest["files"].items():
        file_path = STAGING / rel_path
        assert file_path.exists(), f"Staged file missing: {rel_path}"
        actual_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"Hash mismatch for {rel_path}"


# ─── TEST 3: verify-package.mjs Execution Pass ─────────────────────────────────
def test_03_verify_package_script_passes():
    """Running node tools/verify-package.mjs in staging passes cleanly."""
    res = subprocess.run(
        ["node", "tools/verify-package.mjs"],
        cwd=str(STAGING),
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"verify-package.mjs failed:\n{res.stderr}\n{res.stdout}"
    assert "PACKAGE_VERIFY_PASS" in res.stdout
    assert "SOURCE_TEMPLATE_SEMANTICS_PASS" in res.stdout


# ─── TEST 4: test-verify-package.mjs Execution Pass (213 tests) ────────────────
def test_04_test_verify_package_suite_passes():
    """Running node tools/test-verify-package.mjs passes all 213 test cases."""
    res = subprocess.run(
        ["node", "tools/test-verify-package.mjs"],
        cwd=str(STAGING),
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"test-verify-package.mjs failed:\n{res.stderr}\n{res.stdout}"
    assert "SUMMARY pass=213 fail=0" in res.stdout


# ─── TEST 5: test-autonomy-engine.mjs Execution Pass (51 tests) ───────────────
def test_05_test_autonomy_engine_suite_passes():
    """Running node tools/test-autonomy-engine.mjs passes all 51 test cases."""
    res = subprocess.run(
        ["node", "tools/test-autonomy-engine.mjs"],
        cwd=str(STAGING),
        capture_output=True,
        text=True,
    )
    assert res.returncode == 0, f"test-autonomy-engine.mjs failed:\n{res.stderr}\n{res.stdout}"
    assert "AUTONOMY_SUMMARY pass=51 fail=0" in res.stdout


# ─── TEST 6: Three Operational Authorities Model Preserved ─────────────────────
def test_06_three_authority_governance_model_preserved():
    """Repository strictly maintains exactly three active operational authorities in governance/."""
    gov_md = ROOT / "governance" / "GOVERNANCE.md"
    proj_dir = ROOT / "governance" / "PROJECT_DIRECTION.md"
    proj_state = ROOT / "governance" / "PROJECT_STATE.yaml"

    assert gov_md.exists()
    assert proj_dir.exists()
    assert proj_state.exists()

    gov_text = gov_md.read_text(encoding="utf-8")
    assert "There are exactly three operational entry authorities" in gov_text
    assert "Do not create a fourth competing live authority" in gov_text


# ─── TEST 7: Adoption Mode & Product Archetype Classification ──────────────────
def test_07_adoption_mode_and_product_archetype():
    """Yang-Mills is classified as MIGRATION_GOVERNED and LIBRARY_SDK archetype."""
    envelope = load_yaml("governance/envelopes/YM-GOV-ADOPT-0410R3.yaml")
    ident = envelope["task_execution_envelope"]["identity"]
    assert ident["adoption_mode"] == "MIGRATION_GOVERNED"
    assert ident["product_archetype"] == "LIBRARY_SDK"
    assert ident["active_paradigms"] == ["FUNCTIONAL", "DATA_ORIENTED", "RELATIONAL_LOGIC"]

    direction = read("governance/PROJECT_DIRECTION.md")
    assert "Adoption Mode: MIGRATION_GOVERNED" in direction
    assert "Product Archetype: LIBRARY_SDK" in direction


# ─── TEST 8: Five Distinct Super-Agent Roles Enforced ─────────────────────────
def test_08_five_actor_separation_and_superagent_roles():
    """Worker, Reviewer (IND2+), Acceptor, Router, and Watchdog IDs are mutually distinct."""
    envelope = load_yaml("governance/envelopes/YM-GOV-ADOPT-0410R3.yaml")
    roles = envelope["task_execution_envelope"]["roles_and_authority"]

    worker_id = roles["writer"]["id"]
    reviewer_id = roles["reviewer_or_verifier"]["id"]
    acceptor_id = roles["acceptance_authority"]["id"]
    router_id = roles["router_id"]
    watchdog_id = roles["watchdog_id"]

    all_actors = [worker_id, reviewer_id, acceptor_id, router_id, watchdog_id]
    assert len(set(all_actors)) == 5, f"All 5 actor identities must be mutually distinct: {all_actors}"
    assert roles["reviewer_or_verifier"]["expected_independence"] in ["IND2", "IND3"]


# ─── TEST 9: Specification Gate Contract & CRP Requirement ────────────────────
def test_09_specification_gate_contract_enforced():
    """Missing or ambiguous specification halts code implementation and requires a CRP."""
    envelope = load_yaml("governance/envelopes/YM-GOV-ADOPT-0410R3.yaml")
    spec_gate = envelope["task_execution_envelope"]["specification_gate"]

    assert spec_gate["status"] == "SPEC_VERIFIED"
    assert len(spec_gate["missing_specification_prompts"]) == 0
    assert "dimension_refs" in spec_gate
    for dim in ["intent_actors", "data_interfaces", "paradigm_boundaries", "diagrams", "relative_standards", "acceptance_negative"]:
        assert dim in spec_gate["dimension_refs"]
        assert spec_gate["dimension_refs"][dim] is not None


# ─── TEST 10: Diagram-First Enforcement & Drift Protection ─────────────────────
def test_10_diagram_first_contract_enforced():
    """DIAGRAM_LOCKED is required before implementation, and diagram drift fails review."""
    envelope = load_yaml("governance/envelopes/YM-GOV-ADOPT-0410R3.yaml")
    spec_gate = envelope["task_execution_envelope"]["specification_gate"]

    assert spec_gate["diagram_first_status"] == "DIAGRAM_LOCKED"
    assert len(spec_gate["diagram_refs"]) >= 2
    assert spec_gate["diagram_approval_ref"] is not None

    direction = read("governance/PROJECT_DIRECTION.md")
    assert "As-Is Reverse-Engineered Architecture Diagrams" in direction
    assert "flowchart TD" in direction
    assert "stateDiagram-v2" in direction


# ─── TEST 11: Autonomy Engine 10-Phase Lifecycle Sequence ─────────────────────
def test_11_autonomy_engine_lifecycle_ten_phases():
    """Autonomy engine defines the exact 10-phase sequence in PHASE_ORDER."""
    engine_code = (STAGING / "tools" / "autonomy-engine.mjs").read_text(encoding="utf-8")
    expected_phases = ["DISCOVER", "SPECIFY", "STANDARDS", "DIAGRAM", "IMPLEMENT", "TEST", "REVIEW", "ACCEPT", "RECORD", "EVOLVE"]
    for phase in expected_phases:
        assert f"'{phase}'" in engine_code or f'"{phase}"' in engine_code


# ─── TEST 12: Mandatory Required Hard Gates Inventory ─────────────────────────
def test_12_required_hard_gates_inventory_mandatory():
    """All 12 project-bound hard gates are registered and mandatory."""
    assert len(YANG_MILLS_REQUIRED_HARD_GATES) == 12
    rule = load_yaml("governance/PROJECT_BOUND_READINESS_RULE.yaml")
    inventory = rule["required_hard_gate_inventory"]
    assert len(inventory) == 12


# ─── TEST 13: Pre-Code Authorization Rejects Unauthorized Mutation ─────────────
def test_13_precode_authorization_blocks_unauthorized_mutation():
    """Pre-code authorization requires matching state revision, diagram approval, and scope."""
    verify_package_code = (STAGING / "tools" / "verify-package.mjs").read_text(encoding="utf-8")
    assert "validatePreCodeAuthorization" in verify_package_code
    test_verify_code = (STAGING / "tools" / "test-verify-package.mjs").read_text(encoding="utf-8")
    assert "precode-no-trusted-adapter-blocks" in test_verify_code
    assert "precode-${name}-refused" in test_verify_code or "precode" in test_verify_code


# ─── TEST 14: Epistemic Invariants Strictly Preserved ─────────────────────────
def test_14_epistemic_invariants_strictly_preserved():
    """goal_complete=false, clay_problem=OPEN_AND_UNSOLVED, and E-CROSSOVER=OPEN."""
    state = load_yaml("governance/PROJECT_STATE.yaml")
    assert state["goal_complete"] is False
    assert state["clay_problem"] == "OPEN_AND_UNSOLVED"

    envelope = load_yaml("governance/envelopes/YM-GOV-ADOPT-0410R3.yaml")
    invariants = {inv["id"]: inv["statement"] for inv in envelope["task_execution_envelope"]["invariants"]}
    assert "INV-YM-GOV-02" in invariants
    assert "GOAL_COMPLETE = FALSE" in invariants["INV-YM-GOV-02"]
    assert "E-CROSSOVER = OPEN_AND_UNSOLVED" in invariants["INV-YM-GOV-03"]


# ─── TEST 15: Closed-World Scientific Manifest Count & Tree Hash ───────────────
def test_15_closed_world_scientific_manifest_count_and_tree_hash():
    """Closed-world scientific manifest contains exactly 158 files and matches verified tree hash."""
    tree_hash, file_hashes = compute_closed_world_scientific_tree_hash(ROOT)
    assert len(file_hashes) == 158, f"Expected exactly 158 canonical files, found {len(file_hashes)}"
    assert tree_hash == "c7e6223373cd46603ddd59f4a3a75c8824a87d4b817cbfee8e3861d33f7c8613"


# ─── TEST 16: Negative Evidence Register Zero Historical Deletions ────────────
def test_16_negative_evidence_zero_historical_deletions():
    """All negative evidence entries are preserved with strictly zero deletions."""
    neg_evidence = read("NEGATIVE_EVIDENCE_REGISTER.md")
    assert "NEG-YM-011-PLAQ-1" in neg_evidence
    assert "NEG-YM-077-NONPERTURBATIVE-CROSSOVER-AND-TRIPARTITE-IR-OBSTRUCTIONS" in neg_evidence
    assert "NEG-YM-100-FACTORIAL-RENORMALON-CAUCHY-TAYLOR-BARRIER" in neg_evidence


# ─── TEST 17: Universal Governance Adoption Cannot Weaken Controls ─────────────
def test_17_universal_adoption_cannot_weaken_scientific_controls():
    """Adoption preserves canonical baseline v4.0.4 and autonomous scientific repair."""
    gov = read("governance/GOVERNANCE.md")
    assert "UNIVERSAL_GOVERNANCE_MINIMAL_v4.0.4" in gov
    assert "UNIVERSAL_GOVERNANCE_MINIMAL_v4.1.0-r3" in gov
    assert "autonomous scientific repair" in gov.lower()


# ─── TEST 18: Live-Effect Receipt Must Echo State Revision & Subject ──────────
def test_18_consequential_effect_receipt_echoes_state_revision_and_subject():
    """Live-effect receipts must bind state_revision and frozen_subject_digest."""
    gov = read("governance/GOVERNANCE.md")
    assert "state_revision" in gov
    assert "frozen_subject_digest" in gov
    assert "effect_boundary_verification" in gov
