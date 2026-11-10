"""
Deterministic Unit Tests for Project Chrysalis Governance Architecture
========================================================================
Validates:
1. Gate 1: AST & Ingress Sanitization (forbidden imports, os.system, subprocess network, float-blocking).
2. Gate 2: Policy-as-Code Enforcement (rational arithmetic bounds, CLAIM_EVIDENCE_MATRIX mapping).
3. Gate 3: Cryptographic Provenance (SHA-256 + HMAC-SHA256 Local Binary Authorization).
4. Gate 4: Dual-Custody Human Sign-Off & Tamper-Evident Hash-Chained Audit Chain.
5. APEX Co-Evolution Engine (Layer 1 Ephemeral Hotpatching, Layer 2 Signed Distillation, Layer 3 Rewiring).
6. Dream-RSI Counterfactual Replay & AgentEvolver Step-Level Marginal Attribution.
"""

from fractions import Fraction
import hashlib
import hmac
import json
from pathlib import Path
import pytest
import shutil
import tempfile

from scripts.chrysalis_gates import ChrysalisGates, GateResult
from scripts.chrysalis_apex import (
    ApexCoEvolutionEngine,
    ApexHotpatchSandbox,
    ApexPrincipleDistiller,
    ApexStateRewirer,
    DualCustodyApprovalRequiredError,
)
from scripts.chrysalis_dream_rsi import DreamRsiRunner, AgentEvolverAttributor


ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def gates():
    return ChrysalisGates(root_dir=ROOT)


@pytest.fixture
def apex():
    return ApexCoEvolutionEngine(root_dir=ROOT)


# ─── 1. Gate 1: AST & Ingress Sanitization ───────────────────────────────────

def test_01_gate_1_workspace_scripts_and_tests_pass(gates):
    """All existing scripts and tests pass Gate 1 AST sanitization."""
    res = gates.run_gate_1_ast()
    assert res.passed is True, f"Violations found: {res.violations}"
    assert res.details["files_scanned"] > 40


def test_02_gate_1_blocks_os_system(gates):
    """Gate 1 AST blocks os.system calls in candidate code."""
    bad_code = """
import os
def malicious():
    os.system("rm -rf /")
"""
    res = gates.run_gate_1_ast(candidate_code=bad_code)
    assert res.passed is False
    assert any("os.system" in v for v in res.violations)


def test_03_gate_1_blocks_network_imports(gates):
    """Gate 1 AST blocks forbidden remote network imports."""
    for mod in ["requests", "urllib.request", "socket", "http.client", "aiohttp"]:
        bad_code = f"import {mod}\n"
        res = gates.run_gate_1_ast(candidate_code=bad_code)
        assert res.passed is False, f"Expected import {mod} to be blocked"
        assert any(mod in v for v in res.violations)


def test_04_gate_1_blocks_subprocess_network_commands(gates):
    """Gate 1 AST blocks subprocess network commands (curl, wget, ssh)."""
    for cmd in ["curl", "wget", "ssh", "nc"]:
        bad_code = f"""
import subprocess
def fetch():
    subprocess.run(["{cmd}", "https://example.com"])
"""
        res = gates.run_gate_1_ast(candidate_code=bad_code)
        assert res.passed is False, f"Expected command '{cmd}' to be blocked"
        assert any(cmd in v for v in res.violations)


def test_05_gate_1_ast_float_blocking_in_exact_rational_certificates(gates):
    """Gate 1 AST blocks float(...) calls and float literals in exact rational certificate modules."""
    # Float call:
    bad_float_call = """
# EXACT_RATIONAL_CERTIFICATE
from fractions import Fraction
def certificate():
    x = float(Fraction(1, 2))
    return x
"""
    res_call = gates.run_gate_1_ast(candidate_code=bad_float_call, is_candidate_exact_rational=True)
    assert res_call.passed is False
    assert any("float()" in v for v in res_call.violations)

    # Float literal:
    bad_float_literal = """
# EXACT_RATIONAL_CERTIFICATE
from fractions import Fraction
def certificate():
    delta = 0.025
    return delta
"""
    res_lit = gates.run_gate_1_ast(candidate_code=bad_float_literal, is_candidate_exact_rational=True)
    assert res_lit.passed is False
    assert any("Floating-point literal '0.025'" in v for v in res_lit.violations)

    # Pure Fraction code passes:
    clean_code = """
# EXACT_RATIONAL_CERTIFICATE
from fractions import Fraction
def certificate():
    x = Fraction(187, 7872)
    delta = Fraction(1, 57)
    return x + delta
"""
    res_clean = gates.run_gate_1_ast(candidate_code=clean_code, is_candidate_exact_rational=True)
    assert res_clean.passed is True


# ─── 2. Gate 2: Policy-as-Code Enforcement ───────────────────────────────────

def test_06_gate_2_policy_rational_bounds_pass(gates):
    """Valid exact rational bounds pass Gate 2 policy thresholds."""
    valid_bounds = {
        "R_ge3_Cauchy": Fraction(187, 7872),
        "delta_all_orders_margin": Fraction(17838, 1000000),  # > 1/57
        "W_IR_total_all_orders": Fraction(982162, 1000000),   # < 1
        "delta_toron_excess": Fraction(982162, 1000000),      # > 0
    }
    res = gates.run_gate_2_policy(candidate_bounds=valid_bounds)
    assert res.passed is True
    assert res.details["min_margin_threshold"] == "1/57"


def test_07_gate_2_policy_rejects_non_positive_margin(gates):
    """Gate 2 rejects bounds with non-positive margin or W >= 1."""
    # Negative margin:
    bad_bounds_1 = {
        "delta_all_orders_margin": Fraction(-1, 100),
        "W_IR_total_all_orders": Fraction(105, 100),
    }
    res_1 = gates.run_gate_2_policy(candidate_bounds=bad_bounds_1)
    assert res_1.passed is False
    assert any("violates strict positivity" in v for v in res_1.violations)
    assert any("violates convergence upper bound" in v for v in res_1.violations)

    # Margin below threshold (e.g. 1/1000 < 1/57):
    bad_bounds_2 = {
        "delta_all_orders_margin": Fraction(1, 1000),
        "W_IR_total_all_orders": Fraction(999, 1000),
    }
    res_2 = gates.run_gate_2_policy(candidate_bounds=bad_bounds_2)
    assert res_2.passed is False
    assert any("below policy minimum threshold" in v for v in res_2.violations)


def test_08_gate_2_claim_evidence_matrix_mapping(gates):
    """Gate 2 verifies all 42 claims in CLAIM_EVIDENCE_MATRIX.md map to valid tests."""
    res = gates.run_gate_2_policy()
    assert res.passed is True
    assert res.details["claims_evaluated"] >= 42


# ─── 3. Gate 3: Cryptographic Provenance ─────────────────────────────────────

def test_09_gate_3_provenance_verification(gates):
    """Gate 3 verifies SHA-256 + HMAC-SHA256 signatures for all tracked artifacts."""
    # Refresh manifest to ensure all test files are included
    gates.generate_manifest()
    res = gates.run_gate_3_provenance()
    assert res.passed is True
    assert res.details["artifacts_verified"] >= 64


def test_10_gate_3_detects_tampered_artifact(gates):
    """Gate 3 detects tampering if file content or hash diverges."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_root = Path(tmp_dir)
        # Copy a minimal workspace
        gov_dir = tmp_root / "governance"
        gov_dir.mkdir(parents=True)
        shutil.copy(ROOT / "governance" / "chrysalis_keystore.json", gov_dir / "chrysalis_keystore.json")
        shutil.copy(ROOT / "governance" / "chrysalis_policy.yaml", gov_dir / "chrysalis_policy.yaml")

        p_dir = tmp_root / "paper"
        p_dir.mkdir(parents=True)
        tex_file = p_dir / "main.tex"
        tex_file.write_text("% Genuine paper content", encoding="utf-8")

        tmp_gates = ChrysalisGates(root_dir=tmp_root)
        tmp_gates.generate_manifest()

        # Check clean pass
        res_before = tmp_gates.run_gate_3_provenance(enforce_strict=False)
        assert res_before.passed is True

        # Tamper with file
        tex_file.write_text("% Tampered paper content!", encoding="utf-8")
        res_after = tmp_gates.run_gate_3_provenance(enforce_strict=False)
        assert res_after.passed is False
        assert any("tampered file" in v for v in res_after.violations)


# ─── 4. Gate 4: Dual-Custody Human Sign-Off & Audit Chain ───────────────────

def test_11_gate_4_hash_chain_integrity(gates):
    """Gate 4 maintains an unbroken, cryptographically signed hash chain."""
    valid, violations = gates.verify_audit_chain()
    assert valid is True
    assert len(violations) == 0


def test_12_gate_4_detects_tampered_audit_chain(gates):
    """Tampering with any line in the audit chain breaks verification."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_audit = Path(tmp_dir) / "audit.jsonl"
        tmp_gates = ChrysalisGates(root_dir=ROOT)

        # Append 3 entries
        tmp_gates.append_audit_entry("EVENT_1", {"msg": "first"}, audit_file=tmp_audit)
        tmp_gates.append_audit_entry("EVENT_2", {"msg": "second"}, audit_file=tmp_audit)
        tmp_gates.append_audit_entry("EVENT_3", {"msg": "third"}, audit_file=tmp_audit)

        valid_before, _ = tmp_gates.verify_audit_chain(audit_file=tmp_audit)
        assert valid_before is True

        # Tamper with line 1
        lines = tmp_audit.read_text(encoding="utf-8").splitlines()
        rec1 = json.loads(lines[1])
        rec1["details"]["msg"] = "tampered!"
        lines[1] = json.dumps(rec1)
        tmp_audit.write_text("\n".join(lines) + "\n", encoding="utf-8")

        valid_after, violations = tmp_gates.verify_audit_chain(audit_file=tmp_audit)
        assert valid_after is False
        assert any("Entry hash tampered" in v or "Hash-chain broken" in v for v in violations)


def test_13_gate_4_layer3_pauses_without_human_approval(gates):
    """Layer 3 transition is paused when active envelope lacks human_approval block."""
    res = gates.run_gate_4_dual_custody(is_layer3_transition=True)
    assert res.passed is False
    assert res.details["state_status"] == "PAUSED_PENDING_HUMAN_APPROVAL"


def test_14_gate_4_layer3_rejects_self_signed_token(gates):
    """Layer 3 rejects approvals where human_owner == independent_reviewer."""
    with pytest.raises(ValueError, match="Tri-Agent Separation violation"):
        gates.generate_dual_custody_token("YM-101", "actor-alice", "actor-alice")


def test_15_gate_4_layer3_passes_with_valid_dual_custody_token(gates):
    """Layer 3 transition succeeds when a valid dual-custody token is provided."""
    env_id = "YM-101"
    h_owner = "human-owner"
    reviewer = "distinct-technical-acceptor"
    token = gates.generate_dual_custody_token(env_id, h_owner, reviewer)

    assert gates.verify_dual_custody_token(env_id, h_owner, reviewer, token) is True
    # Wrong token fails:
    assert gates.verify_dual_custody_token(env_id, h_owner, reviewer, "bad-token") is False


# ─── 5. APEX Engine (Three Timescales) ────────────────────────────────────────

def test_16_apex_layer1_ephemeral_hotpatch_preserves_disk(apex):
    """Layer 1 executes candidate bounds in memory without modifying files on disk."""
    candidate_bounds = {
        "R_ge3_Cauchy": Fraction(187, 7872),
        "delta_all_orders_margin": Fraction(17838, 1000000),
        "W_IR_total_all_orders": Fraction(982162, 1000000),
    }

    res = apex.layer1_sandbox.evaluate_candidate_bounds_in_memory(
        candidate_bounds=candidate_bounds,
        candidate_code="# EXACT_RATIONAL_CERTIFICATE\nfrom fractions import Fraction\nx = Fraction(187, 7872)\n",
    )
    assert res.success is True
    assert res.disk_preserved is True
    assert res.error is None


def test_17_apex_layer2_signed_principle_distillation(apex):
    """Layer 2 distills verified principles and negative obstructions into signed ledger."""
    principle = apex.layer2_distiller.distill_principle(
        rule_id="TEST-RULE-CAUCHY-BOUND",
        status="VERIFIED_PRINCIPLE",
        mathematical_statement="All-orders Cauchy contour remainder contracts strictly within 2-loop margin.",
        rational_parameters={"R_ge3_Cauchy": Fraction(187, 7872)},
        negative_evidence_ref="NEG-YM-100",
        claim_ref="YM-REQ-007",
    )
    assert principle.principle_id.startswith("PRIN-TEST-RULE-")
    assert len(principle.signature) == 64

    # Verify distilled ledger
    valid, violations = apex.layer2_distiller.verify_distilled_ledger()
    assert valid is True
    assert len(violations) == 0


def test_18_apex_layer3_structural_rewiring_guard(apex):
    """Layer 3 requires valid dual-custody approval before structural rewiring."""
    rewirer = apex.layer3_rewirer
    h_owner = "human-owner"
    reviewer = "distinct-technical-acceptor"
    token = apex.gates.generate_dual_custody_token("YM-101", h_owner, reviewer)

    # Valid approval:
    receipt = rewirer.authorize_structural_transition(
        envelope_id="YM-101",
        human_owner=h_owner,
        independent_reviewer=reviewer,
        approval_token=token,
    )
    assert receipt["authorized"] is True
    assert receipt["receipt_id"].startswith("REC-L3-YM-101-")

    # Invalid token raises DualCustodyApprovalRequiredError:
    with pytest.raises(DualCustodyApprovalRequiredError):
        rewirer.authorize_structural_transition(
            envelope_id="YM-101",
            human_owner=h_owner,
            independent_reviewer=reviewer,
            approval_token="invalid-token",
        )


# ─── 6. Dream-RSI & AgentEvolver Attribution ─────────────────────────────────

def test_19_dream_rsi_counterfactual_replay_passes_valid():
    """Dream-RSI trace runner validates non-regressive parameter vectors."""
    runner = DreamRsiRunner(root_dir=ROOT)
    valid_params = {
        "eta_CT": Fraction(1, 16),
        "w_Peierls": Fraction(11, 27),
        "eta_dim6": Fraction(1, 4),
        "eta_elliptic": Fraction(1, 4),
        "raw_animal_tail": Fraction(187, 492),
        "R_ge3_Cauchy": Fraction(187, 7872),
        "w_toron_vol": Fraction(1, 1),
        "delta_all_orders_margin": Fraction(17838, 1000000),
        "claim_total_continuum_closure": Fraction(0),
    }
    res = runner.replay_candidate_parameters(valid_params)
    assert res.passed is True
    assert len(res.regressions) == 0
    assert len(res.replayed_cases) == 5


def test_20_dream_rsi_counterfactual_replay_catches_regressions():
    """Dream-RSI catches regression if candidate violates historical obstruction barriers."""
    runner = DreamRsiRunner(root_dir=ROOT)

    # Violating NEG-YM-101 (premature claim of closure while toron excess exists)
    regressive_1 = {
        "eta_CT": Fraction(1, 16),
        "eta_dim6": Fraction(1, 4),
        "eta_elliptic": Fraction(1, 4),
        "R_ge3_Cauchy": Fraction(187, 7872),
        "w_toron_vol": Fraction(1, 1),
        "delta_all_orders_margin": Fraction(17838, 1000000),
        "claim_total_continuum_closure": Fraction(1),  # Falsely claims closure!
    }
    res_1 = runner.replay_candidate_parameters(regressive_1)
    assert res_1.passed is False
    assert any("NEG-YM-101" in r for r in res_1.regressions)

    # Violating NEG-YM-100 (untruncated 3-loop remainder exceeding 2-loop margin)
    regressive_2 = {
        "eta_CT": Fraction(1, 16),
        "eta_dim6": Fraction(1, 4),
        "eta_elliptic": Fraction(1, 4),
        "R_ge3_Cauchy": Fraction(187, 1312),  # Untruncated 3-loop excess
        "delta_IR_2loop_full": Fraction(495, 10000),
        "w_toron_vol": Fraction(1, 1),
        "delta_all_orders_margin": Fraction(17838, 1000000),
    }
    res_2 = runner.replay_candidate_parameters(regressive_2)
    assert res_2.passed is False
    assert any("NEG-YM-100" in r for r in res_2.regressions)


def test_21_agent_evolver_marginal_attribution_scoring():
    """AgentEvolver scores tasks based on rational inequality strictness and 0 regressions."""
    evolver = AgentEvolverAttributor(root_dir=ROOT)
    report = evolver.evaluate_task_attribution(
        task_id="YM-101",
        candidate_bounds={
            "W_IR_total_all_orders": Fraction(982162, 1000000),
            "prior_obstruction": Fraction(93011, 1000000),
            "post_obstruction": Fraction(0),
        },
        test_passed_count=532,
        test_failed_count=0,
    )
    assert report.zero_regression is True
    assert report.rational_margin == Fraction(17838, 1000000)
    assert report.marginal_credit == Fraction(93011, 1000000)
    assert report.attribution_score > 0.7
    assert report.promotable is True
