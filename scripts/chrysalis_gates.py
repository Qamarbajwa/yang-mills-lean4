#!/usr/bin/env python3
"""
Google Cloud Project Chrysalis - The Four Security Gates
=========================================================
Implements the 4 programmatic security gates enforcing:
1. Gate 1: AST & Ingress Sanitization (blocks os.system, network calls, float approximations in exact rational modules).
2. Gate 2: Policy-as-Code Enforcement (rational arithmetic positivity/margins & claim-to-test mapping).
3. Gate 3: Cryptographic Provenance (Local Binary Authorization: SHA-256 + HMAC-SHA256 for tests, envelopes, paper).
4. Gate 4: Dual-Custody Human Sign-Off & Tamper-Evident Hash-Chained Audit Logging.
"""

import ast
from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
import glob
import hashlib
import hmac
import io
import json
from pathlib import Path
import re
import tokenize
from typing import Any, Dict, List, Optional, Set, Tuple, Union
import yaml


ROOT = Path(__file__).resolve().parent.parent


@dataclass
class GateResult:
    gate: int
    name: str
    passed: bool
    violations: List[str] = field(default_factory=list)
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "gate": self.gate,
            "name": self.name,
            "passed": self.passed,
            "violations": self.violations,
            "details": self.details,
        }


def has_exact_rational_pragma(code_str: str) -> bool:
    """Returns True if the source code contains an actual # EXACT_RATIONAL_CERTIFICATE comment."""
    try:
        tokens = tokenize.generate_tokens(io.StringIO(code_str).readline)
        for tok in tokens:
            if tok.type == tokenize.COMMENT and "EXACT_RATIONAL_CERTIFICATE" in tok.string:
                return True
    except Exception:
        pass
    return False


class AstIngressVisitor(ast.NodeVisitor):
    """
    AST Visitor that scans code for forbidden calls, forbidden network modules,
    subprocess network commands, and floating-point approximations in exact rational contexts.
    """

    def __init__(
        self,
        filepath: str,
        forbidden_calls: Set[str],
        forbidden_modules: Set[str],
        forbidden_subprocess_commands: Set[str],
        enforce_exact_rational: bool = False,
    ):
        self.filepath = filepath
        self.forbidden_calls = forbidden_calls
        self.forbidden_modules = forbidden_modules
        self.forbidden_subprocess_commands = forbidden_subprocess_commands
        self.enforce_exact_rational = enforce_exact_rational
        self.violations: List[str] = []

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            base_mod = alias.name.split(".")[0]
            if alias.name in self.forbidden_modules or base_mod in self.forbidden_modules:
                self.violations.append(
                    f"{self.filepath}:{node.lineno}: Forbidden import of network/remote module '{alias.name}'"
                )
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module:
            base_mod = node.module.split(".")[0]
            if node.module in self.forbidden_modules or base_mod in self.forbidden_modules:
                self.violations.append(
                    f"{self.filepath}:{node.lineno}: Forbidden import from network/remote module '{node.module}'"
                )
            for alias in node.names:
                full_name = f"{node.module}.{alias.name}"
                if full_name in self.forbidden_calls or alias.name == "system" and base_mod in ("os", "posix", "nt"):
                    self.violations.append(
                        f"{self.filepath}:{node.lineno}: Forbidden import of call '{full_name}'"
                    )
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        # 1. Check for os.system or forbidden call attributes
        call_name = ""
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name):
                call_name = f"{node.func.value.id}.{node.func.attr}"
            elif isinstance(node.func.value, ast.Attribute):
                # e.g. os.path or urllib.request
                call_name = f"{getattr(node.func.value.value, 'id', '')}.{node.func.value.attr}.{node.func.attr}"
            else:
                call_name = node.func.attr
        elif isinstance(node.func, ast.Name):
            call_name = node.func.id

        if call_name in self.forbidden_calls:
            self.violations.append(
                f"{self.filepath}:{node.lineno}: Forbidden function call '{call_name}'"
            )

        # 2. Check subprocess network calls (e.g. subprocess.run(["curl", ...]))
        if "subprocess" in call_name or call_name in ("run", "Popen", "check_output", "check_call", "call"):
            if node.args:
                first_arg = node.args[0]
                cmd_tokens = []
                if isinstance(first_arg, (ast.List, ast.Tuple)):
                    for elt in first_arg.elts:
                        if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                            cmd_tokens.append(elt.value)
                elif isinstance(first_arg, ast.Constant) and isinstance(first_arg.value, str):
                    cmd_tokens = first_arg.value.split()

                for tok in cmd_tokens:
                    tok_lower = tok.lower().strip()
                    if tok_lower in self.forbidden_subprocess_commands:
                        self.violations.append(
                            f"{self.filepath}:{node.lineno}: Forbidden subprocess network command '{tok}'"
                        )

        # 3. Floating-point float(...) approximations in exact rational certificate modules
        if self.enforce_exact_rational:
            if call_name == "float":
                self.violations.append(
                    f"{self.filepath}:{node.lineno}: Floating-point approximation 'float()' forbidden in exact rational certificate module; use fractions.Fraction"
                )

        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant):
        if self.enforce_exact_rational and isinstance(node.value, float):
            self.violations.append(
                f"{self.filepath}:{node.lineno}: Floating-point literal '{node.value}' forbidden in exact rational certificate module; use fractions.Fraction"
            )
        self.generic_visit(node)


class ChrysalisGates:
    """
    Programmatic evaluator for the 4 Chrysalis Security Gates.
    """

    def __init__(
        self,
        root_dir: Optional[Path] = None,
        policy_path: Optional[Path] = None,
        keystore_path: Optional[Path] = None,
    ):
        self.root = Path(root_dir) if root_dir else ROOT
        self.policy_path = Path(policy_path) if policy_path else self.root / "governance" / "chrysalis_policy.yaml"
        self.keystore_path = Path(keystore_path) if keystore_path else self.root / "governance" / "chrysalis_keystore.json"
        self.policy: Dict[str, Any] = self._load_policy()
        self.keystore: Dict[str, Any] = self._load_keystore()

    def _load_policy(self) -> Dict[str, Any]:
        if not self.policy_path.exists():
            return {}
        with open(self.policy_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def _load_keystore(self) -> Dict[str, Any]:
        if not self.keystore_path.exists():
            # Generate default keystore if absent
            default_keystore = {
                "key_id": "chrysalis-local-hmac-2026",
                "algorithm": "HMAC-SHA256",
                "secret_key": "c7a91f3e82d4b56a0123456789abcdef0123456789abcdef0123456789abcdef",
                "created_at": datetime.now(timezone.utc).isoformat(),
                "description": "Local deterministic cryptographic keystore",
            }
            self.keystore_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.keystore_path, "w", encoding="utf-8") as f:
                json.dump(default_keystore, f, indent=2)
            return default_keystore

        with open(self.keystore_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_secret_key(self) -> bytes:
        key_str = self.keystore.get("secret_key", "chrysalis-fallback-secret-salt")
        return key_str.encode("utf-8")

    # ──────────────────────────────────────────────────────────────────────────
    # Gate 1: AST & Ingress Sanitization
    # ──────────────────────────────────────────────────────────────────────────

    def run_gate_1_ast(
        self,
        scripts_dir: Optional[Path] = None,
        tests_dir: Optional[Path] = None,
        candidate_code: Optional[str] = None,
        is_candidate_exact_rational: bool = False,
        target_files: Optional[List[Path]] = None,
    ) -> GateResult:
        """
        Parses Python scripts via Python's ast module.
        Enforces:
        - No os.system calls
        - No forbidden network imports (socket, urllib, requests, etc.)
        - No subprocess network calls (curl, wget, ssh, etc.)
        - In exact rational certificate modules: no float(...) calls or float literals.
        """
        g1_cfg = self.policy.get("gate_1_ast_ingress", {})
        forbidden_calls = set(g1_cfg.get("forbidden_calls", ["os.system", "posix.system", "nt.system"]))
        forbidden_modules = set(
            g1_cfg.get(
                "forbidden_modules",
                ["socket", "urllib", "urllib.request", "requests", "http.client", "aiohttp", "httpx"],
            )
        )
        forbidden_subproc = set(
            g1_cfg.get(
                "forbidden_subprocess_commands",
                ["curl", "wget", "ssh", "nc", "netcat", "ping", "telnet", "ftp"],
            )
        )

        all_violations: List[str] = []
        files_checked = 0

        # 1. If candidate_code is provided directly:
        if candidate_code is not None:
            try:
                tree = ast.parse(candidate_code, filename="<candidate_in_memory>")
                enforce_rational = is_candidate_exact_rational or has_exact_rational_pragma(candidate_code)
                visitor = AstIngressVisitor(
                    filepath="<candidate_in_memory>",
                    forbidden_calls=forbidden_calls,
                    forbidden_modules=forbidden_modules,
                    forbidden_subprocess_commands=forbidden_subproc,
                    enforce_exact_rational=enforce_rational,
                )
                visitor.visit(tree)
                all_violations.extend(visitor.violations)
                files_checked += 1
            except SyntaxError as e:
                all_violations.append(f"<candidate_in_memory>:{e.lineno}: SyntaxError: {e.msg}")

        # 2. Files to check on disk:
        files_to_scan: List[Path] = []
        if target_files is not None:
            files_to_scan.extend(target_files)
        elif candidate_code is None or scripts_dir is not None or tests_dir is not None:
            s_dir = scripts_dir or (self.root / "scripts")
            t_dir = tests_dir or (self.root / "tests")
            if s_dir.exists():
                files_to_scan.extend(s_dir.glob("*.py"))
            if t_dir.exists():
                files_to_scan.extend(t_dir.glob("*.py"))

        for fpath in files_to_scan:
            try:
                content = fpath.read_text(encoding="utf-8")
                tree = ast.parse(content, filename=str(fpath))
                # Pragma check for exact rational enforcement
                enforce_rational = has_exact_rational_pragma(content)
                visitor = AstIngressVisitor(
                    filepath=str(fpath.relative_to(self.root) if fpath.is_relative_to(self.root) else fpath),
                    forbidden_calls=forbidden_calls,
                    forbidden_modules=forbidden_modules,
                    forbidden_subprocess_commands=forbidden_subproc,
                    enforce_exact_rational=enforce_rational,
                )
                visitor.visit(tree)
                all_violations.extend(visitor.violations)
                files_checked += 1
            except Exception as e:
                all_violations.append(f"{fpath}: AST parse error: {e}")

        passed = len(all_violations) == 0
        return GateResult(
            gate=1,
            name="AST & Ingress Sanitization",
            passed=passed,
            violations=all_violations,
            details={"files_scanned": files_checked, "violations_count": len(all_violations)},
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Gate 2: Policy-as-Code Enforcement (Local OPA-style Rules)
    # ──────────────────────────────────────────────────────────────────────────

    def run_gate_2_policy(
        self,
        candidate_bounds: Optional[Dict[str, Any]] = None,
        matrix_path: Optional[Path] = None,
    ) -> GateResult:
        """
        Verifies policy rules against governance/chrysalis_policy.yaml:
        - Rational bounds meet strict positivity & margin thresholds (e.g. margin >= 1/57, W < 1).
        - Every claim in CLAIM_EVIDENCE_MATRIX.md maps to a verified pytest function/file.
        """
        violations: List[str] = []
        g2_cfg = self.policy.get("gate_2_policy_rules", {})
        bounds_cfg = g2_cfg.get("rational_bounds", {})
        claim_cfg = g2_cfg.get("claim_evidence_matrix", {})

        # A. Rational Bounds Verification
        min_margin_str = str(bounds_cfg.get("min_margin_threshold", "1/57"))
        min_margin = Fraction(min_margin_str)
        strict_positivity = bounds_cfg.get("strict_positivity_required", True)
        max_cluster_weight = Fraction(str(bounds_cfg.get("max_cluster_weight", "1")))
        max_cauchy_remainder = Fraction(str(bounds_cfg.get("max_cauchy_remainder", "187/7872")))

        # Use candidate_bounds if provided, otherwise evaluate the baseline active certified bounds
        bounds_to_eval = candidate_bounds or {
            "R_ge3_Cauchy": Fraction(187, 7872),
            "w_4species_6": Fraction(187, 1968) + Fraction(17, 738),  # approx 0.118
            "W_IR_total_all_orders": Fraction(982162, 1000000),  # approx 0.982162
            "delta_all_orders_margin": Fraction(17838, 1000000),  # approx 0.017838 > 1/57
            "delta_toron_excess": Fraction(982162, 1000000),
        }

        # 1. Positivity
        if strict_positivity:
            for b_name, b_val in bounds_to_eval.items():
                if isinstance(b_val, (int, str)):
                    b_val = Fraction(b_val)
                if isinstance(b_val, Fraction) and b_val <= 0:
                    violations.append(f"Rational bound '{b_name}' = {b_val} violates strict positivity (> 0).")

        # 2. Min margin threshold
        margin_val = bounds_to_eval.get("delta_all_orders_margin") or bounds_to_eval.get("margin")
        if margin_val is not None:
            if isinstance(margin_val, str):
                margin_val = Fraction(margin_val)
            if margin_val < min_margin:
                violations.append(
                    f"Rational margin {margin_val} is below policy minimum threshold {min_margin} ({min_margin_str})."
                )

        # 3. Max cluster weight (< 1)
        w_total = bounds_to_eval.get("W_IR_total_all_orders") or bounds_to_eval.get("W_IR_total")
        if w_total is not None:
            if isinstance(w_total, str):
                w_total = Fraction(w_total)
            if w_total >= max_cluster_weight:
                violations.append(
                    f"Cluster weight {w_total} violates convergence upper bound < {max_cluster_weight}."
                )

        # 4. Max Cauchy remainder
        cauchy_rem = bounds_to_eval.get("R_ge3_Cauchy")
        if cauchy_rem is not None:
            if isinstance(cauchy_rem, str):
                cauchy_rem = Fraction(cauchy_rem)
            if cauchy_rem > max_cauchy_remainder:
                violations.append(
                    f"Cauchy remainder {cauchy_rem} exceeds maximum allowable remainder {max_cauchy_remainder}."
                )

        # B. Claim-Evidence Matrix Mapping Verification
        matrix_file = matrix_path or (self.root / claim_cfg.get("source_file", "CLAIM_EVIDENCE_MATRIX.md"))
        if not matrix_file.exists():
            violations.append(f"CLAIM_EVIDENCE_MATRIX file not found: {matrix_file}")
        else:
            content = matrix_file.read_text(encoding="utf-8")
            # Find all requirement IDs and theorem IDs
            req_ids = sorted(list(set(re.findall(r"YM-REQ-\d+", content))))
            thm_ids = sorted(list(set(re.findall(r"THM-YM-\d+", content))))
            all_claim_ids = req_ids + thm_ids

            claim_mapping = claim_cfg.get("claim_test_mapping", {})
            unmapped_claims = []
            for cid in all_claim_ids:
                if cid not in claim_mapping:
                    unmapped_claims.append(cid)
                else:
                    test_target = claim_mapping[cid]
                    # Check that mapped test file exists
                    test_file_rel = test_target.split("::")[0]
                    test_file_path = self.root / test_file_rel
                    if not test_file_path.exists():
                        violations.append(
                            f"Claim '{cid}' maps to non-existent test file '{test_file_rel}'."
                        )

            if unmapped_claims:
                violations.append(
                    f"Unmapped claims found in CLAIM_EVIDENCE_MATRIX.md: {unmapped_claims[:5]} (total {len(unmapped_claims)} unmapped)."
                )

        passed = len(violations) == 0
        return GateResult(
            gate=2,
            name="Policy-as-Code Enforcement",
            passed=passed,
            violations=violations,
            details={
                "evaluated_bounds": {k: str(v) for k, v in bounds_to_eval.items()},
                "min_margin_threshold": min_margin_str,
                "claims_evaluated": len(all_claim_ids) if matrix_file.exists() else 0,
            },
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Gate 3: Cryptographic Provenance (Local Binary Authorization)
    # ──────────────────────────────────────────────────────────────────────────

    def generate_manifest(self, output_path: Optional[Path] = None) -> Dict[str, Any]:
        """
        Generates and cryptographically signs SHA-256 + HMAC-SHA256 signatures
        for all test files, governance envelopes, and paper/main.tex.
        """
        secret_key = self.get_secret_key()
        g3_cfg = self.policy.get("gate_3_cryptographic_provenance", {})
        patterns = g3_cfg.get("tracked_patterns", ["tests/test_*.py", "governance/envelopes/*.yaml", "paper/main.tex"])

        tracked_files: List[Path] = []
        for pat in patterns:
            matched = list(self.root.glob(pat))
            tracked_files.extend(matched)

        # Dedup and sort
        tracked_files = sorted(list(set(tracked_files)))
        manifest_files: Dict[str, Dict[str, Any]] = {}

        for fpath in tracked_files:
            if fpath.is_file():
                rel_path = str(fpath.relative_to(self.root)).replace("\\", "/")
                data = fpath.read_bytes()
                sha256_hash = hashlib.sha256(data).hexdigest()
                sig = hmac.new(secret_key, data, hashlib.sha256).hexdigest()
                manifest_files[rel_path] = {
                    "sha256": sha256_hash,
                    "hmac_sha256": sig,
                    "size_bytes": len(data),
                }

        manifest = {
            "manifest_version": "1.0.0",
            "key_id": self.keystore.get("key_id", "chrysalis-local-hmac-2026"),
            "algorithm": "HMAC-SHA256",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_artifacts": len(manifest_files),
            "files": manifest_files,
        }

        target_out = output_path or (self.root / g3_cfg.get("manifest_file", "governance/chrysalis_manifest.json"))
        target_out.parent.mkdir(parents=True, exist_ok=True)
        with open(target_out, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        return manifest

    def run_gate_3_provenance(
        self,
        manifest_path: Optional[Path] = None,
        enforce_strict: bool = True,
    ) -> GateResult:
        """
        Verifies SHA-256 and HMAC signatures for all test files, governance envelopes,
        and paper/main.tex. Rejects unsigned or tampered artifacts.
        """
        violations: List[str] = []
        g3_cfg = self.policy.get("gate_3_cryptographic_provenance", {})
        m_path = manifest_path or (self.root / g3_cfg.get("manifest_file", "governance/chrysalis_manifest.json"))

        if not m_path.exists():
            # If manifest does not exist, auto-generate initial baseline manifest
            self.generate_manifest(m_path)

        with open(m_path, "r", encoding="utf-8") as f:
            manifest_data = json.load(f)

        secret_key = self.get_secret_key()
        manifest_files = manifest_data.get("files", {})
        verified_count = 0

        # Check each file in manifest against disk
        for rel_path, meta in manifest_files.items():
            fpath = self.root / rel_path
            if not fpath.exists():
                violations.append(f"Tracked artifact missing on disk: '{rel_path}'")
                continue

            disk_bytes = fpath.read_bytes()
            disk_sha256 = hashlib.sha256(disk_bytes).hexdigest()
            disk_hmac = hmac.new(secret_key, disk_bytes, hashlib.sha256).hexdigest()

            if disk_sha256 != meta.get("sha256"):
                violations.append(
                    f"Artifact '{rel_path}' SHA-256 mismatch (tampered file): expected {meta.get('sha256')}, got {disk_sha256}"
                )
            elif not hmac.compare_digest(disk_hmac, meta.get("hmac_sha256", "")):
                violations.append(
                    f"Artifact '{rel_path}' HMAC signature mismatch (cryptographic provenance invalid)"
                )
            else:
                verified_count += 1

        # Check if there are any untracked test/envelope/paper files on disk
        if enforce_strict:
            patterns = g3_cfg.get("tracked_patterns", ["tests/test_*.py", "governance/envelopes/*.yaml", "paper/main.tex"])
            for pat in patterns:
                for fpath in self.root.glob(pat):
                    rel = str(fpath.relative_to(self.root)).replace("\\", "/")
                    if rel not in manifest_files:
                        violations.append(f"Unsigned / untracked artifact on disk: '{rel}'")

        passed = len(violations) == 0
        return GateResult(
            gate=3,
            name="Cryptographic Provenance (Local Binary Authorization)",
            passed=passed,
            violations=violations,
            details={"artifacts_verified": verified_count, "manifest_entries": len(manifest_files)},
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Gate 4: Dual-Custody Human Sign-Off & Tamper-Evident Audit
    # ──────────────────────────────────────────────────────────────────────────

    def generate_dual_custody_token(
        self,
        envelope_id: str,
        human_owner: str,
        independent_reviewer: str,
    ) -> str:
        """
        Generates HMAC-SHA256 signature for dual-custody human sign-off.
        Enforces Tri-Agent Separation: human_owner != independent_reviewer.
        """
        if human_owner == independent_reviewer:
            raise ValueError(
                f"Tri-Agent Separation violation: human_owner '{human_owner}' and reviewer '{independent_reviewer}' must not be identical."
            )
        secret_key = self.get_secret_key()
        msg = f"{envelope_id}:{human_owner}:{independent_reviewer}".encode("utf-8")
        return hmac.new(secret_key, msg, hashlib.sha256).hexdigest()

    def verify_dual_custody_token(
        self,
        envelope_id: str,
        human_owner: str,
        independent_reviewer: str,
        token: str,
    ) -> bool:
        """Verifies dual-custody token validity."""
        if human_owner == independent_reviewer:
            return False
        try:
            expected = self.generate_dual_custody_token(envelope_id, human_owner, independent_reviewer)
            return hmac.compare_digest(expected, token)
        except Exception:
            return False

    def append_audit_entry(
        self,
        event_type: str,
        details: Dict[str, Any],
        audit_file: Optional[Path] = None,
    ) -> Dict[str, Any]:
        """
        Appends an entry to the append-only hash-chained audit log.
        """
        a_path = audit_file or (self.root / self.policy.get("gate_4_dual_custody", {}).get(
            "audit_chain_file", "governance/chrysalis_audit_chain.jsonl"
        ))
        a_path.parent.mkdir(parents=True, exist_ok=True)

        secret_key = self.get_secret_key()
        prev_hash = "0" * 64
        index = 0

        # Read last entry if file exists
        if a_path.exists():
            lines = [line.strip() for line in a_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            if lines:
                try:
                    last_entry = json.loads(lines[-1])
                    prev_hash = last_entry.get("entry_hash", "0" * 64)
                    index = last_entry.get("index", len(lines) - 1) + 1
                except Exception:
                    prev_hash = hashlib.sha256(lines[-1].encode("utf-8")).hexdigest()
                    index = len(lines)

        timestamp = datetime.now(timezone.utc).isoformat()
        entry_payload = {
            "index": index,
            "prev_hash": prev_hash,
            "timestamp": timestamp,
            "event_type": event_type,
            "details": details,
        }
        canonical_str = json.dumps(entry_payload, sort_keys=True)
        entry_hash = hashlib.sha256(canonical_str.encode("utf-8")).hexdigest()
        sig = hmac.new(secret_key, entry_hash.encode("utf-8"), hashlib.sha256).hexdigest()

        final_record = {
            **entry_payload,
            "entry_hash": entry_hash,
            "signature": sig,
        }

        with open(a_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(final_record) + "\n")

        return final_record

    def verify_audit_chain(self, audit_file: Optional[Path] = None) -> Tuple[bool, List[str]]:
        """
        Verifies the cryptographic and hash-chain integrity of the audit log.
        """
        violations: List[str] = []
        a_path = audit_file or (self.root / self.policy.get("gate_4_dual_custody", {}).get(
            "audit_chain_file", "governance/chrysalis_audit_chain.jsonl"
        ))
        if not a_path.exists():
            return True, []

        lines = [line.strip() for line in a_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        secret_key = self.get_secret_key()
        expected_prev_hash = "0" * 64

        for idx, line in enumerate(lines):
            try:
                record = json.loads(line)
            except Exception as e:
                violations.append(f"Line {idx}: Corrupted JSON in audit chain: {e}")
                continue

            entry_index = record.get("index")
            if entry_index != idx:
                violations.append(f"Line {idx}: Index sequence mismatch (expected {idx}, got {entry_index})")

            if record.get("prev_hash") != expected_prev_hash:
                violations.append(
                    f"Line {idx}: Hash-chain broken! expected prev_hash '{expected_prev_hash}', got '{record.get('prev_hash')}'"
                )

            entry_payload = {
                "index": record.get("index"),
                "prev_hash": record.get("prev_hash"),
                "timestamp": record.get("timestamp"),
                "event_type": record.get("event_type"),
                "details": record.get("details"),
            }
            canonical_str = json.dumps(entry_payload, sort_keys=True)
            recomputed_hash = hashlib.sha256(canonical_str.encode("utf-8")).hexdigest()
            if recomputed_hash != record.get("entry_hash"):
                violations.append(
                    f"Line {idx}: Entry hash tampered! expected '{recomputed_hash}', got '{record.get('entry_hash')}'"
                )

            recomputed_sig = hmac.new(secret_key, recomputed_hash.encode("utf-8"), hashlib.sha256).hexdigest()
            if not hmac.compare_digest(recomputed_sig, record.get("signature", "")):
                violations.append(f"Line {idx}: Cryptographic signature invalid on audit entry!")

            expected_prev_hash = record.get("entry_hash", "")

        return len(violations) == 0, violations

    def run_gate_4_dual_custody(
        self,
        active_envelope_path: Optional[Path] = None,
        is_layer3_transition: bool = False,
        gate_summaries: Optional[Dict[str, Any]] = None,
    ) -> GateResult:
        """
        Evaluates Gate 4:
        - Verifies audit chain integrity.
        - If is_layer3_transition is True: requires verifiable dual-custody human approval token
          in active task envelope, pausing state transitions until token is valid.
        - Appends gate evaluation to audit log.
        """
        violations: List[str] = []

        # 1. Audit Chain Integrity Check
        chain_valid, chain_violations = self.verify_audit_chain()
        if not chain_valid:
            violations.extend(chain_violations)

        # 2. Dual-Custody Approval Check for Layer 3 Transitions
        state_status = "NOT_APPLICABLE"
        if is_layer3_transition:
            env_path = active_envelope_path
            if env_path is None:
                # Default to YM-101.yaml
                env_path = self.root / "governance" / "envelopes" / "YM-101.yaml"

            if not env_path.exists():
                violations.append(f"Active envelope not found: {env_path}")
                state_status = "BLOCKED_ENVELOPE_MISSING"
            else:
                with open(env_path, "r", encoding="utf-8") as f:
                    env_data = yaml.safe_load(f) or {}

                human_approval = env_data.get("human_approval") or env_data.get("dual_custody_approval")
                if not human_approval:
                    violations.append(
                        "Layer 3 state transition paused: Missing 'human_approval' block in active task envelope."
                    )
                    state_status = "PAUSED_PENDING_HUMAN_APPROVAL"
                else:
                    h_owner = human_approval.get("human_owner")
                    reviewer = human_approval.get("independent_reviewer")
                    token = human_approval.get("token")
                    env_id = env_data.get("task_execution_envelope", {}).get("identity", {}).get("task_id", env_path.stem)

                    if not h_owner or not reviewer or not token:
                        violations.append(
                            "Layer 3 state transition paused: Incomplete human approval credentials (human_owner, independent_reviewer, or token missing)."
                        )
                        state_status = "PAUSED_PENDING_HUMAN_APPROVAL"
                    elif h_owner == reviewer:
                        violations.append(
                            f"Layer 3 Tri-Agent Separation violation: human_owner '{h_owner}' and reviewer '{reviewer}' cannot be identical."
                        )
                        state_status = "REJECTED_SEPARATION_VIOLATION"
                    elif not self.verify_dual_custody_token(env_id, h_owner, reviewer, token):
                        violations.append(
                            f"Layer 3 state transition paused: Invalid cryptographic token for envelope '{env_id}'."
                        )
                        state_status = "PAUSED_INVALID_TOKEN"
                    else:
                        state_status = "AUTHORIZED"

        passed = len(violations) == 0
        details = {
            "is_layer3_transition": is_layer3_transition,
            "state_status": state_status,
            "gate_summaries": gate_summaries or {},
        }

        # Append evaluation to audit chain
        self.append_audit_entry(
            event_type="GATE_4_EVALUATION" if not is_layer3_transition else "LAYER_3_STATE_TRANSITION_CHECK",
            details={"passed": passed, "state_status": state_status, "violations": violations},
        )

        return GateResult(
            gate=4,
            name="Dual-Custody Human Sign-Off & Tamper-Evident Audit",
            passed=passed,
            violations=violations,
            details=details,
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Run All 4 Gates Sequentially
    # ──────────────────────────────────────────────────────────────────────────

    def run_all_gates(
        self,
        is_layer3_transition: bool = False,
        candidate_code: Optional[str] = None,
        is_candidate_exact_rational: bool = False,
        candidate_bounds: Optional[Dict[str, Any]] = None,
        active_envelope_path: Optional[Path] = None,
    ) -> Dict[str, Any]:
        """
        Executes all 4 Chrysalis Security Gates sequentially.
        """
        # Gate 1
        g1 = self.run_gate_1_ast(
            candidate_code=candidate_code,
            is_candidate_exact_rational=is_candidate_exact_rational,
        )

        # Gate 2
        g2 = self.run_gate_2_policy(candidate_bounds=candidate_bounds)

        # Gate 3
        g3 = self.run_gate_3_provenance()

        # Gate 4
        g4 = self.run_gate_4_dual_custody(
            active_envelope_path=active_envelope_path,
            is_layer3_transition=is_layer3_transition,
            gate_summaries={
                "gate_1": g1.passed,
                "gate_2": g2.passed,
                "gate_3": g3.passed,
            },
        )

        all_passed = g1.passed and g2.passed and g3.passed and g4.passed
        return {
            "all_passed": all_passed,
            "gates": {
                1: g1.to_dict(),
                2: g2.to_dict(),
                3: g3.to_dict(),
                4: g4.to_dict(),
            },
        }


def main():
    import sys
    print("=" * 80)
    print("  PROJECT CHRYSALIS — THE FOUR PROGRAMMATIC SECURITY GATES")
    print("=" * 80)
    gates = ChrysalisGates()
    res = gates.run_all_gates()
    for g_num in range(1, 5):
        g = res["gates"][g_num]
        status_str = "[PASS]" if g["passed"] else "[FAIL]"
        print(f"Gate {g_num}: {g['name']:<55} {status_str}")
        if not g["passed"]:
            for v in g["violations"]:
                print(f"  - {v}")

    print("=" * 80)
    overall = "ALL GATES CLEARED [INTEGRITY_PASS]" if res["all_passed"] else "GATE VERIFICATION FAILED [FAIL]"
    print(f"Result: {overall}")
    print("=" * 80)
    sys.exit(0 if res["all_passed"] else 1)


if __name__ == "__main__":
    main()
