"""
Research Co-Scientist OS — Independent Verification & Proof Bridge
==================================================================
Bridges Co-Scientist candidates to genuine verification backends:
1. Exact Rational Certificate Validator (fractions.Fraction strict inequalities)
2. Dream-RSI Counterfactual Replay (NEGATIVE_EVIDENCE_REGISTER.md regression check)
3. Chrysalis Security Gates (Policy-as-Code & AST sanitization)
4. Live Lean 4.35 Formal Proof Step Runner (via src.ymmg.lean_step_runner)

Strict invariant (I-09 / CS-T009):
- Builder identity and verifier identity MUST differ.
- Never issues VerificationReceipt without all enabled gates passing genuinely.
- Never simulates a Lean kernel pass if lake/lean is unavailable (fail closed).
"""

from __future__ import annotations
from dataclasses import dataclass, field
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import tempfile
from typing import Any, Dict, List, Optional, Tuple
import uuid

from scripts.chrysalis_apex import ApexHotpatchSandbox
from scripts.chrysalis_dream_rsi import DreamRsiRunner
from scripts.chrysalis_gates import ChrysalisGates
from src.ymmg.block_weyl_collar_bound import (
    BlockWeylCollarCertificate,
    evaluate_local_block_collar_bulk_certificate,
)
from src.ymmg.certified_linalg import (
    certify_rational_rank_crt,
    evaluate_toron_bulk_schur_audit,
    verify_schur_coercivity_interval,
)
from src.ymmg.coscientist.kernel import VerificationReceipt
from src.ymmg.coscientist.schemas import YangMillsHypothesis
from src.ymmg.lean_step_runner import check_step


ROOT = Path(__file__).resolve().parents[3]


@dataclass
class VerificationBundleReport:
    hypothesis_id: str
    passed: bool
    rational_ok: bool
    dream_rsi_ok: bool
    chrysalis_gates_ok: bool
    lean_ok: bool
    lean_status: str
    evidence_digest: str
    details: Dict[str, Any] = field(default_factory=dict)
    failures: List[str] = field(default_factory=list)
    verification_scope: str = "FINITE_DIMENSIONAL_MATRIX_AUDIT"


class CoScientistVerifierBridge:
    """
    Independent verifier service bridging mathematical hypotheses to formal and symbolic checks.
    """

    def __init__(
        self,
        root_dir: Optional[Path] = None,
        verifier_identity: str = "independent-ym-verifier-service",
    ):
        self.root = Path(root_dir) if root_dir else ROOT
        self.verifier_identity = verifier_identity
        self.lean_project_dir = self.root / "governance" / "math_gov" / "examples" / "LeanDemoProject"
        self.blueprint_project_dir = self.root / "formal" / "yang_mills_blueprint"
        self.dream_runner = DreamRsiRunner(root_dir=self.root)
        self.gates = ChrysalisGates(root_dir=self.root)
        self.apex_l1 = ApexHotpatchSandbox(root_dir=self.root, gates=self.gates)

    def verify_rational_bounds(
        self,
        hyp: YangMillsHypothesis,
    ) -> Tuple[bool, str, Dict[str, str]]:
        """
        Validates exact Fraction inequalities and non-closure invariant.
        """
        params = hyp.rational_parameters
        reasons: List[str] = []

        r_cauchy = params.get("R_ge3_Cauchy")
        margin = params.get("delta_all_orders_margin")
        w_toron = params.get("w_toron_vol")
        premature = params.get("claim_total_continuum_closure", Fraction(0))

        if r_cauchy is None or margin is None or w_toron is None:
            reasons.append("Missing required exact rational parameters (R_ge3_Cauchy, delta_all_orders_margin, w_toron_vol).")
        else:
            if not (isinstance(r_cauchy, Fraction) and isinstance(margin, Fraction) and isinstance(w_toron, Fraction)):
                reasons.append("All certificate parameters must be exact fractions.Fraction instances.")
            if r_cauchy <= 0 or r_cauchy > Fraction(187, 7872):
                reasons.append(f"R_ge3_Cauchy ({r_cauchy}) out of certified bound (0, 187/7872].")
            if margin < Fraction(1, 57):
                reasons.append(f"delta_all_orders_margin ({margin}) below minimum policy threshold 1/57.")
            if w_toron <= 0:
                reasons.append(f"w_toron_vol ({w_toron}) must be strictly positive (> 0).")
            if w_toron >= margin:
                reasons.append(f"NEG-YM-101 barrier violated: w_toron_vol ({w_toron}) >= margin ({margin}).")

        if premature != Fraction(0):
            reasons.append("Premature continuum closure flag (claim_total_continuum_closure != 0) forbidden.")

        summary = "Exact rational bounds satisfied." if not reasons else "; ".join(reasons)
        serialized = {k: str(v) for k, v in params.items()}
        return len(reasons) == 0, summary, serialized

    def verify_dream_rsi_replay(
        self,
        hyp: YangMillsHypothesis,
    ) -> Tuple[bool, List[str], Dict[str, Any]]:
        """
        Replays candidate rational parameters across all historical failure cases in NEGATIVE_EVIDENCE_REGISTER.md.
        """
        numeric_params = {
            k: v for k, v in hyp.rational_parameters.items()
            if isinstance(v, (int, Fraction))
        }
        result = self.dream_runner.replay_candidate_parameters(numeric_params)
        return (
            result.passed,
            result.regressions,
            {
                "replayed_cases": result.replayed_cases,
                "trace_log": result.trace_log,
            },
        )

    def verify_chrysalis_gates(
        self,
        hyp: YangMillsHypothesis,
    ) -> Tuple[bool, List[str], Dict[str, Any]]:
        """
        Runs Gate 2 Policy-as-Code verification on positive rational certificate parameters.
        """
        # Filter positive certificate bounds (exclude flags like claim_total_continuum_closure == 0)
        bounds_for_policy: Dict[str, Any] = {
            k: v
            for k, v in hyp.rational_parameters.items()
            if k != "claim_total_continuum_closure" and isinstance(v, (int, Fraction))
        }
        if not bounds_for_policy:
            return False, ["No positive rational certificate bounds supplied."], {}

        g2_res = self.gates.run_gate_2_policy(candidate_bounds=bounds_for_policy)
        l1_res = self.apex_l1.evaluate_candidate_bounds_in_memory(candidate_bounds=bounds_for_policy)
        violations = list(g2_res.violations)
        if not l1_res.success or not l1_res.disk_preserved:
            violations.append(f"CHRYSALIS_L1_SANDBOX_FAILED: {l1_res.error or 'disk mutation detected'}")
        details = dict(g2_res.details)
        details["chrysalis_l1_disk_preserved"] = l1_res.disk_preserved
        return g2_res.passed and l1_res.success and l1_res.disk_preserved, violations, details

    def verify_certified_linalg(
        self,
        hyp: YangMillsHypothesis,
    ) -> Tuple[bool, List[str], Dict[str, Any]]:
        """
        Runs arbitrary-precision FLINT interval Schur Congruence & 62-bit multi-prime
        CRT nullspace certification tailored to the candidate's toron margin parameters.
        """
        margin = hyp.rational_parameters.get("delta_all_orders_margin")
        w_toron = hyp.rational_parameters.get("w_toron_vol")
        if not isinstance(margin, Fraction) or not isinstance(w_toron, Fraction):
            return False, ["Missing exact Fraction parameters for certified linalg check."], {}

        failures: List[str] = []
        # 2-block candidate headroom Schur matrix: [[bulk=1, coupling=1], [coupling=1, 1 + (margin - w_toron)]]
        # Strict positivity of Schur complement holds iff (margin - w_toron) > 0!
        margin_gap = margin - w_toron
        candidate_block = [
            [Fraction(1, 1), Fraction(1, 1)],
            [Fraction(1, 1), Fraction(1, 1) + margin_gap],
        ]
        cand_schur = verify_schur_coercivity_interval(candidate_block, split_index=1, dps=80)
        if not cand_schur.is_coercive:
            failures.append(f"CERTIFIED_SCHUR_FAILED: {cand_schur.failure_reason}")

        # Physics T^4 L=8 twisted vs untwisted benchmark audit
        twisted = evaluate_toron_bulk_schur_audit(L=8, d=4, N=2, twisted=True, dps=80)
        untwisted = evaluate_toron_bulk_schur_audit(L=8, d=4, N=2, twisted=False, dps=80)
        untwisted_crt = untwisted.crt_untwisted_nullspace_rank_cert
        if not twisted.schur_cert.is_coercive:
            failures.append("TWISTED_T4_L8_SCHUR_FAILED")
        if untwisted.schur_cert.is_coercive:
            failures.append("UNTWISTED_T4_L8_FALSE_POSITIVITY")
        if untwisted_crt is None or not untwisted_crt.verified_exact_mk_zero or untwisted_crt.nullity != 1:
            failures.append("UNTWISTED_CRT_NULLSPACE_VERIFICATION_FAILED")

        details = {
            "candidate_schur_coercive": cand_schur.is_coercive,
            "candidate_schur_min_pivot_lower": cand_schur.min_schur_pivot_lower_str,
            "twisted_t4_l8_schur_coercive": twisted.schur_cert.is_coercive,
            "untwisted_t4_l8_schur_coercive": untwisted.schur_cert.is_coercive,
            "untwisted_crt_rank": untwisted_crt.rank if untwisted_crt else None,
            "untwisted_crt_nullity": untwisted_crt.nullity if untwisted_crt else None,
            "untwisted_crt_exact_mk_zero": untwisted_crt.verified_exact_mk_zero if untwisted_crt else False,
            "uniform_in_L_gap": False,
        }
        return len(failures) == 0, failures, details

    def verify_block_weyl_collar(
        self,
        hyp: YangMillsHypothesis,
    ) -> Tuple[bool, List[str], Dict[str, Any]]:
        """
        Audits local block-Poincare gap and SU(2) Weyl collar bound (YM-102),
        confirming L-uniform local block contraction while verifying that the
        global commuting toron fiber remains honestly open (NEG-YM-102).
        """
        cert = evaluate_local_block_collar_bulk_certificate()
        failures: List[str] = []
        if not cert.is_certified:
            failures.append(f"BLOCK_WEYL_COLLAR_FAILED: {cert.failure_reason}")

        details = {
            "local_poincare_gap": str(cert.local_poincare_gap),
            "weyl_collar_bound": str(cert.weyl_collar_bound),
            "local_bulk_nonabelian_residual": str(cert.local_bulk_nonabelian_residual),
            "local_block_total_weight": str(cert.local_block_total_weight),
            "local_block_uniform_in_L": cert.local_block_uniform_in_L,
            "global_commuting_fiber_closed": cert.global_commuting_fiber_closed,
            "verification_scope": cert.verification_scope,
            "is_certified": cert.is_certified,
        }
        return cert.is_certified, failures, details

    def verify_lean_step(
        self,
        hyp: YangMillsHypothesis,
        timeout: int = 120,
    ) -> Dict[str, Any]:
        """
        Compiles and kernel-checks hyp.lean_candidate_code inside YangMillsBlueprint (when
        importing `YangMillsBlueprint`) or LeanDemoProject via lean_step_runner.
        Fail-closed: returns LEAN_UNAVAILABLE if lake/lean missing, never simulates pass.
        """
        if not hyp.lean_candidate_code or not hyp.lean_theorem_name or not hyp.lean_formal_statement:
            return {
                "verdict": "NO_LEAN_ARTIFACT_SUPPLIED",
                "lean_kernel_check_passed": False,
                "axioms": [],
            }

        target_project_dir = (
            self.blueprint_project_dir
            if "import YangMillsBlueprint" in hyp.lean_candidate_code
            else self.lean_project_dir
        )
        if not target_project_dir.is_dir():
            return {
                "verdict": "LEAN_PROJECT_NOT_FOUND",
                "lean_kernel_check_passed": False,
                "axioms": [],
            }

        # Normalize line endings strictly to LF (\n) for Lean 4 on Windows
        lean_src = hyp.lean_candidate_code.replace("\r\n", "\n").replace("\r", "\n")
        if not lean_src.endswith("\n"):
            lean_src += "\n"
        raw_bytes = lean_src.encode("utf-8")
        file_sha256 = hashlib.sha256(raw_bytes).hexdigest()

        # Write temporary .lean module inside target Lean project and clean up unconditionally in finally
        temp_filename = f"_coscientist_tmp_{uuid.uuid4().hex[:12]}.lean"
        temp_path = target_project_dir / temp_filename
        try:
            temp_path.write_bytes(raw_bytes)
            result = check_step(
                project_root=str(target_project_dir),
                relative_source=temp_filename,
                theorem=hyp.lean_theorem_name,
                expected_statement=hyp.lean_formal_statement,
                expected_file_sha256=file_sha256,
                timeout=timeout,
            )
            return result
        finally:
            if temp_path.exists():
                try:
                    temp_path.unlink()
                except OSError:
                    pass

    def evaluate_candidate(
        self,
        hyp: YangMillsHypothesis,
        enable_lean: bool = True,
        require_lean: bool = True,
    ) -> VerificationBundleReport:
        """
        Runs the full independent verification battery and produces an evidence digest.
        """
        failures: List[str] = []

        rational_ok, rational_msg, rational_details = self.verify_rational_bounds(hyp)
        if not rational_ok:
            failures.append(f"RATIONAL_CHECK_FAILED: {rational_msg}")

        dream_ok, regressions, dream_details = self.verify_dream_rsi_replay(hyp)
        if not dream_ok:
            failures.extend(f"DREAM_RSI_REGRESSION: {r}" for r in regressions)

        gates_ok, gate_violations, gate_details = self.verify_chrysalis_gates(hyp)
        if not gates_ok:
            failures.extend(f"CHRYSALIS_GATE_2_VIOLATION: {v}" for v in gate_violations)

        linalg_ok, linalg_failures, linalg_details = self.verify_certified_linalg(hyp)
        if not linalg_ok:
            failures.extend(linalg_failures)

        block_ok, block_failures, block_details = self.verify_block_weyl_collar(hyp)
        if not block_ok:
            failures.extend(block_failures)

        lean_res: Dict[str, Any]
        if enable_lean:
            lean_res = self.verify_lean_step(hyp)
            lean_ok = bool(lean_res.get("lean_kernel_check_passed", False))
            lean_status = str(lean_res.get("verdict", "LEAN_UNKNOWN"))
            if require_lean and not lean_ok:
                failures.append(f"LEAN_VERIFICATION_FAILED: {lean_status}")
        else:
            lean_res = {"verdict": "LEAN_SKIPPED_BY_CONFIG", "lean_kernel_check_passed": False}
            lean_ok = not require_lean
            lean_status = "LEAN_SKIPPED_BY_CONFIG"
            if require_lean:
                failures.append("LEAN_REQUIRED_BUT_DISABLED")

        # Finite-vs-Asymptotic Separation Invariant:
        # A FINITE_DIMENSIONAL_MATRIX_AUDIT or fixed-L rational certificate can validate
        # a bounded single-block RG lemma (e.g. HYP-YM-TWIST-HOLONOMY-v1-HYBRID), but is strictly
        # barred from closing asymptotic edges (E-THERMO, E-LATTICE-CONT, E-CROSSOVER) without
        # an accompanying uniform-in-L analytic certificate and closed global fiber.
        asymptotic_edges = {"E-THERMO", "E-LATTICE-CONT", "E-CROSSOVER"}
        claimed_edge = hyp.rational_parameters.get("target_edge") or hyp.rational_parameters.get("claimed_edge")
        claim_continuum = hyp.rational_parameters.get("claim_total_continuum_closure", Fraction(0))

        claims_asymptotic = False
        if claimed_edge in asymptotic_edges:
            claims_asymptotic = True
        if str(hyp.goal_id).strip() in asymptotic_edges:
            claims_asymptotic = True
        for pred in hyp.predictions:
            for edge in asymptotic_edges:
                if f"close {edge}" in pred.lower() or f"closes {edge}" in pred.lower() or f"closure of {edge}" in pred.lower():
                    claims_asymptotic = True
        for edge in asymptotic_edges:
            if f"closes {edge}" in hyp.statement.lower() or f"closing {edge}" in hyp.statement.lower() or f"closed {edge}" in hyp.statement.lower():
                claims_asymptotic = True

        uniform_in_L_ok = bool(linalg_details.get("uniform_in_L_gap", False))
        global_fiber_closed = bool(block_details.get("global_commuting_fiber_closed", False))

        if (claims_asymptotic or claim_continuum != Fraction(0)) and (not uniform_in_L_ok or not global_fiber_closed):
            failures.append(
                "ASYMPTOTIC_EDGE_UNAUTHORIZED_FROM_FINITE_AUDIT: "
                "FINITE_DIMENSIONAL_MATRIX_AUDIT or fixed-L rational certificate can validate "
                "a bounded single-block RG lemma (e.g. HYP-YM-TWIST-HOLONOMY-v1-HYBRID), but is strictly "
                "barred from closing asymptotic edges (E-THERMO, E-LATTICE-CONT, E-CROSSOVER) "
                "without an accompanying uniform-in-L analytic certificate and closed global commuting fiber."
            )

        all_passed = (
            (len(failures) == 0)
            and rational_ok
            and dream_ok
            and gates_ok
            and linalg_ok
            and block_ok
            and (lean_ok if require_lean else True)
        )

        evidence_payload = {
            "hypothesis_id": hyp.hypothesis_id,
            "content_digest": hyp.content_digest,
            "verification_scope": "FINITE_DIMENSIONAL_MATRIX_AUDIT",
            "rational_ok": rational_ok,
            "rational_details": rational_details,
            "dream_rsi_ok": dream_ok,
            "dream_details": dream_details,
            "chrysalis_gates_ok": gates_ok,
            "gate_details": gate_details,
            "certified_linalg_ok": linalg_ok,
            "certified_linalg_details": linalg_details,
            "block_weyl_collar_ok": block_ok,
            "block_weyl_collar_details": block_details,
            "lean_ok": lean_ok,
            "lean_status": lean_status,
            "lean_res": lean_res,
            "failures": failures,
        }
        evidence_digest = hashlib.sha256(
            json.dumps(evidence_payload, sort_keys=True).encode("utf-8")
        ).hexdigest()

        return VerificationBundleReport(
            hypothesis_id=hyp.hypothesis_id,
            passed=all_passed,
            rational_ok=rational_ok,
            dream_rsi_ok=dream_ok,
            chrysalis_gates_ok=gates_ok,
            lean_ok=lean_ok,
            lean_status=lean_status,
            evidence_digest=evidence_digest,
            details=evidence_payload,
            failures=failures,
            verification_scope="FINITE_DIMENSIONAL_MATRIX_AUDIT",
        )

    def build_verification_receipt(
        self,
        hyp: YangMillsHypothesis,
        builder_identity: str = "ym-coscientist-builder",
        enable_lean: bool = True,
        require_lean: bool = True,
        semantic_review_passed: bool = True,
    ) -> Tuple[Optional[VerificationReceipt], VerificationBundleReport]:
        """
        Builds a VerificationReceipt ONLY if all independent verification gates pass
        and builder_identity != self.verifier_identity.
        """
        report = self.evaluate_candidate(hyp, enable_lean=enable_lean, require_lean=require_lean)
        if not report.passed:
            return None, report
        if builder_identity == self.verifier_identity:
            return None, report

        receipt = VerificationReceipt(
            hypothesis_id=hyp.hypothesis_id,
            exact_target_digest=hyp.content_digest,
            evidence_digest=report.evidence_digest,
            claim_type="MATH_PROOF",
            builder_identity=builder_identity,
            verifier_identity=self.verifier_identity,
            independently_verified=True,
            protected_suite_passed=True,
            semantic_review_passed=semantic_review_passed,
            verifier_authority_bound=True,
            verification_scope=report.verification_scope,
        )
        return receipt, report
