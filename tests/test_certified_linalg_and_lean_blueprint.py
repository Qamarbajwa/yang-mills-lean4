"""
Comprehensive Certification Tests for the 4-Stage Upgrade
=======================================================
1. Stage 1: Two-Part Axiom-Free Lean 4.35 Architecture (`formal/yang_mills_blueprint/`)
   including `CheckAllDecls` live audit + `sorry`/`axiom` negative controls.
2. Stage 2: Multi-prime 62-bit CRT + Wang rational reconstruction & FLINT `arb` interval
   LDL^T / Quadratic-Residual Schur Congruence + Toron-Bulk physics integration.
3. Stage 3: Live physics-backed Co-Scientist discovery + `YangMillsBlueprint` Lean checks
   + Chrysalis L1 zero-disk-mutation verification + adversarial perturbation checks.
"""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
from pathlib import Path
import re
import shutil
import subprocess
import uuid

import pytest

from src.ymmg.certified_linalg import (
    certify_rational_rank_crt,
    crt_combine,
    evaluate_toron_bulk_schur_audit,
    verify_certified_interval_ldlt,
    verify_schur_coercivity_interval,
    wang_rational_reconstruct,
)
from src.ymmg.coscientist import (
    CoScientistVerifierBridge,
    YMEvolutionAgent,
    YMGenerationAgent,
    YangMillsCoScientistOrchestrator,
)
from src.ymmg.lean_step_runner import check_step
from src.ymmg.loop_bootstrap import (
    generate_and_verify_rigorous_plaquette_certificate,
    verify_interval_cholesky_psd,
    verify_rigorous_arb_ldlt_psd,
)
from src.ymmg.toron_brascamp_lieb import audit_levi_stratum_mode_balance_and_schur


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_DIR = ROOT / "formal" / "yang_mills_blueprint"


# ==============================================================================
# Stage 1 Tests: Axiom-Free Two-Part Lean 4.35 Architecture
# ==============================================================================


def test_stage1_blueprint_files_have_zero_sorry_and_zero_custom_axioms():
    assert BLUEPRINT_DIR.is_dir()
    assert (BLUEPRINT_DIR / "lean-toolchain").read_text(encoding="utf-8").strip() == "leanprover/lean4:v4.35.0"
    assert (BLUEPRINT_DIR / "lakefile.toml").is_file()
    assert (BLUEPRINT_DIR / "lake-manifest.json").is_file()

    lean_files = list((BLUEPRINT_DIR / "YangMillsBlueprint").glob("*.lean"))
    assert len(lean_files) >= 4

    for lf in lean_files:
        text = lf.read_text(encoding="utf-8")
        # Strip block and line comments before scanning for standalone `sorry` or `axiom`
        stripped = re.sub(r"/-.*?-/", "", text, flags=re.DOTALL)
        stripped = re.sub(r"--[^\n]*", "", stripped)
        assert not re.search(r"(?m)^\s*axiom\s+", stripped), f"Custom axiom forbidden in {lf.name}"
        assert not re.search(r"\bsorry\b", stripped), f"sorry forbidden in {lf.name}"


def test_stage1_lean_check_all_decls_live_kernel_and_axiom_audit():
    if not shutil.which("lake"):
        pytest.skip("lake executable unavailable")

    res = subprocess.run(
        ["lake", "env", "lean", "YangMillsBlueprint/CheckAllDecls.lean"],
        cwd=str(BLUEPRINT_DIR),
        capture_output=True,
        text=True,
        timeout=120,
    )
    combined = (res.stdout or "") + "\n" + (res.stderr or "")
    assert res.returncode == 0, f"Lean CheckAllDecls failed:\n{combined}"
    assert "sorryAx" not in combined, f"sorryAx leaked into CheckAllDecls:\n{combined}"
    assert "error:" not in combined.lower()
    assert "YangMillsBlueprint.Interfaces.conditional_clay_mass_gap_of_bridges' does not depend on any axioms" in combined
    assert "YangMillsBlueprint.Interfaces.bridge_dag_acyclic_rank' does not depend on any axioms" in combined
    assert "YangMillsBlueprint.levi_stratum_mode_conservation" in combined
    assert "YangMillsBlueprint.schur_coercivity_from_block_pivots" in combined


def test_stage1_lean_step_runner_rejects_sorry_and_custom_axiom_negative_control():
    if not shutil.which("lake"):
        pytest.skip("lake executable unavailable")

    bad_src = (
        "import YangMillsBlueprint\n"
        "namespace NegControl\n"
        "axiom fake_clay_axiom : 1 = 2\n"
        "theorem bogus : 1 = 2 := fake_clay_axiom\n"
        "end NegControl\n"
    )
    tmp_name = f"_neg_control_{uuid.uuid4().hex[:10]}.lean"
    tmp_path = BLUEPRINT_DIR / tmp_name
    try:
        raw = bad_src.encode("utf-8")
        tmp_path.write_bytes(raw)
        rep = check_step(
            project_root=str(BLUEPRINT_DIR),
            relative_source=tmp_name,
            theorem="NegControl.bogus",
            expected_statement="1 = 2",
            expected_file_sha256=hashlib.sha256(raw).hexdigest(),
            timeout=60,
        )
        assert rep["lean_kernel_check_passed"] is False
        assert rep["proof_complete"] is False
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


# ==============================================================================
# Stage 2 Tests: 62-Bit Multi-Prime CRT + FLINT Interval LDL^T & Schur Congruence
# ==============================================================================


def test_stage2_wang_and_crt_exact_rational_rank_and_nullspace():
    # Rank-2 3x4 matrix with exact fractions from YM-101 scales
    mat = [
        [F(187, 7872), F(1, 4), F(42284, 73185), F(11, 432)],
        [F(1, 2), F(3, 5), F(7, 11), F(13, 17)],
        [F(187, 7872) + F(1, 1), F(1, 4) + F(6, 5), F(42284, 73185) + F(14, 11), F(11, 432) + F(26, 17)],
    ]
    cert = certify_rational_rank_crt(mat)
    assert cert.rank == 2
    assert cert.nullity == 2
    assert cert.verified_exact_mk_zero is True
    assert cert.verified_rank_nullity is True
    assert len(cert.nullspace_basis) == 2

    # Explicitly verify M @ K = 0 over fractions.Fraction
    for vec in cert.nullspace_basis:
        for row in mat:
            assert sum((row[j] * vec[j] for j in range(4)), F(0, 1)) == F(0, 1)


def test_stage2_wang_reconstruction_fails_closed_when_modulus_too_small():
    # Scalar 1 / 10^9 cannot reconstruct modulo 101*103 (= 10403)
    mat = [[F(1, 1), F(1, 10**9)]]
    cert = certify_rational_rank_crt(mat, primes=(101, 103))
    assert cert.verified_exact_mk_zero is False
    assert cert.failure_reason is not None


def test_stage2_crt_combine_and_wang_roundtrip():
    target = F(-42284, 73185)
    moduli = (4611686018427387847, 4611686018427387817)
    residues = [(target.numerator * pow(target.denominator, -1, p)) % p for p in moduli]
    combined, big_m = crt_combine(residues, moduli)
    assert wang_rational_reconstruct(combined, big_m) == target


def test_stage2_flint_interval_ldlt_beats_ieee_float_tolerance_trap():
    # Near-singular matrix with genuine negative eigenvalue approx -5e-13:
    # Old float heuristic (tol=1e-6) falsely returns True!
    bad_mat_f = [[1.0, 1.0], [1.0, 1.0 - 1e-12]]
    heuristic_ok, _ = verify_interval_cholesky_psd(bad_mat_f, tolerance=1e-6)
    assert heuristic_ok is True  # Demonstrates why Stage 2 upgrade was required!

    bad_mat_exact = [[F(1, 1), F(1, 1)], [F(1, 1), F(1, 1) - F(1, 10**12)]]
    strict_cert = verify_certified_interval_ldlt(bad_mat_exact, dps=80, strict_positive=True)
    psd_cert = verify_certified_interval_ldlt(bad_mat_exact, dps=80, strict_positive=False)
    assert strict_cert.is_certified is False
    assert psd_cert.is_certified is False

    # Strictly positive definite ill-conditioned 4x4 Hilbert matrix must be certified
    hilbert_4 = [[F(1, i + j + 1) for j in range(4)] for i in range(4)]
    h4_cert = verify_certified_interval_ldlt(hilbert_4, dps=80, strict_positive=True)
    assert h4_cert.is_certified is True

    # Outward interval straddling singularity must fail closed
    uncertain_mat = [[(F(999, 1000), F(1001, 1000)), F(1, 1)], [F(1, 1), F(1, 1)]]
    uncertain_cert = verify_certified_interval_ldlt(uncertain_mat, dps=80, strict_positive=True)
    assert uncertain_cert.is_certified is False


def test_stage2_schur_coercivity_and_toron_bulk_physics_integration():
    for L in (4, 8, 16):
        twisted = evaluate_toron_bulk_schur_audit(L=L, d=4, N=2, twisted=True)
        untwisted = evaluate_toron_bulk_schur_audit(L=L, d=4, N=2, twisted=False)

        assert twisted.schur_cert.bulk_pd_ok is True
        assert twisted.schur_cert.schur_pd_ok is True
        assert twisted.schur_cert.is_coercive is True
        assert twisted.uniform_in_L_gap is False

        assert untwisted.schur_cert.bulk_pd_ok is True
        assert untwisted.schur_cert.is_coercive is False
        assert untwisted.ir_barrier_isolated is True
        assert untwisted.crt_untwisted_nullspace_rank_cert is not None
        assert untwisted.crt_untwisted_nullspace_rank_cert.rank == 2
        assert untwisted.crt_untwisted_nullspace_rank_cert.nullity == 1
        assert untwisted.crt_untwisted_nullspace_rank_cert.verified_exact_mk_zero is True

    # Verify wrapper integration in loop_bootstrap and toron_brascamp_lieb
    rigorous_ok, pivots_str, err = verify_rigorous_arb_ldlt_psd([[F(2, 1), F(1, 1)], [F(1, 1), F(2, 1)]])
    assert rigorous_ok is True and err is None and len(pivots_str) == 2

    dual_cert = generate_and_verify_rigorous_plaquette_certificate(beta=2.4, bound_type="LOWER")
    assert dual_cert.is_certified is True

    levi_schur = audit_levi_stratum_mode_balance_and_schur(L=8, d=4, N=2)
    assert levi_schur["twisted_schur_coercive_fixed_L"] is True
    assert levi_schur["untwisted_schur_coercive_fixed_L"] is False
    assert levi_schur["untwisted_crt_nullity"] == 1
    assert levi_schur["uniform_in_L_gap_established"] is False


# ==============================================================================
# Stage 3 Tests: Live Physics Co-Scientist + Blueprint Lean Bridge
# ==============================================================================


def test_stage3_coscientist_bridge_verifies_blueprint_lean_and_rejects_perturbation():
    gen = YMGenerationAgent()
    evolver = YMEvolutionAgent()
    bridge = CoScientistVerifierBridge(root_dir=ROOT)

    goal = YangMillsCoScientistOrchestrator.default_goal()
    cands = gen.generate_candidates(goal, run_id="RUN-S4", include_adversarial_flawed=False)
    twist, vortex = cands[0], cands[1]

    # Evolved hybrid child synthesizes live Lean 4.35 theorem importing YangMillsBlueprint
    child, _ = evolver.evolve_hybrid(twist, vortex, new_id="HYP-YM-S4-HYBRID", run_id="RUN-S4")
    rep = bridge.evaluate_candidate(child, enable_lean=True, require_lean=True)
    assert rep.passed is True, f"Expected full bundle pass, failures={rep.failures}"
    assert rep.details["certified_linalg_ok"] is True
    assert rep.details["gate_details"]["chrysalis_l1_disk_preserved"] is True
    assert rep.details["certified_linalg_details"]["untwisted_crt_nullity"] == 1

    # Adversarial perturbation: push w_toron_vol above margin -> must fail Schur & rational gates
    bad_child = evolver.evolve_hybrid(twist, vortex, new_id="HYP-YM-S4-BAD", run_id="RUN-S4")[0]
    bad_child.rational_parameters["w_toron_vol"] = bad_child.rational_parameters["delta_all_orders_margin"] + F(1, 10000)
    bad_rep = bridge.evaluate_candidate(bad_child, enable_lean=False, require_lean=False)
    assert bad_rep.passed is False
    assert bad_rep.rational_ok is False
    assert bad_rep.details["certified_linalg_ok"] is False


def test_stage2_scope_tagging_and_asymptotic_separation():
    # 1. Certificate scope tagging
    crt = certify_rational_rank_crt([[F(1, 1), F(2, 1)], [F(2, 1), F(4, 1)]])
    assert crt.verification_scope == "FINITE_DIMENSIONAL_MATRIX_AUDIT"

    ldlt = verify_certified_interval_ldlt([[F(2, 1), F(1, 1)], [F(1, 1), F(2, 1)]])
    assert ldlt.verification_scope == "FINITE_DIMENSIONAL_MATRIX_AUDIT"

    schur = verify_schur_coercivity_interval([[F(2, 1), F(1, 1)], [F(1, 1), F(2, 1)]], split_index=1)
    assert schur.verification_scope == "FINITE_DIMENSIONAL_MATRIX_AUDIT"

    audit = evaluate_toron_bulk_schur_audit(L=4, d=4, N=2, twisted=True)
    assert audit.verification_scope == "FINITE_DIMENSIONAL_MATRIX_AUDIT"

    # 2. Receipt and Report scope tagging
    gen = YMGenerationAgent()
    bridge = CoScientistVerifierBridge(root_dir=ROOT)
    goal = YangMillsCoScientistOrchestrator.default_goal()
    twist = gen.generate_candidates(goal, run_id="RUN-SCOPE", include_adversarial_flawed=False)[0]

    receipt, report = bridge.build_verification_receipt(twist, enable_lean=False, require_lean=False)
    assert report.verification_scope == "FINITE_DIMENSIONAL_MATRIX_AUDIT"
    assert receipt is not None
    assert receipt.verification_scope == "FINITE_DIMENSIONAL_MATRIX_AUDIT"

    # 3. Hard invariant barring finite-dimensional audit from closing asymptotic edges
    for edge in ("E-CROSSOVER", "E-THERMO", "E-LATTICE-CONT"):
        asymp_cand = gen.generate_candidates(goal, run_id="RUN-ASYMP", include_adversarial_flawed=False)[0]
        asymp_cand.goal_id = edge
        rep_asymp = bridge.evaluate_candidate(asymp_cand, enable_lean=False, require_lean=False)
        assert rep_asymp.passed is False
        assert any("ASYMPTOTIC_EDGE_UNAUTHORIZED_FROM_FINITE_AUDIT" in f for f in rep_asymp.failures)

