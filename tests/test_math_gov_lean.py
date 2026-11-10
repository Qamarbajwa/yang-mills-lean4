"""
MATH-GOV v0.6 Lean 4 Integration & Step Verifier Tests
======================================================
Tests:
- Live Lean 4.35 compilation on host
- Axiom extraction from Lean `#print axioms` output
- Rejection of disallowed axioms (including `sorryAx`)
- Rejection of path traversal and unpinned projects
- Detection of mutated or stale source files
- Integrated step verification with cryptographic anchor validation
"""

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.ymmg import lean_step_runner as l
from src.ymmg import step_verifier as sv
from src.ymmg import math_step_engine as e

EXAMPLES_DIR = ROOT / "governance" / "math_gov" / "examples"
LEAN_DEMO_PROJECT = EXAMPLES_DIR / "LeanDemoProject"
DEMO_CASE_PATH = EXAMPLES_DIR / "demo_case.json"
CASE = json.loads(DEMO_CASE_PATH.read_text(encoding="utf-8"))
ORIGINAL = CASE["original"]["digest"]
FORMAL = CASE["formal_target"]["digest"]
CONTRACT = e.digest(e.canonical({"required_inventory": CASE["required_inventory"], "required_edges": CASE["required_edges"]}))


def mutate_node(case, node_id):
    return next(x for x in case["nodes"] if x["id"] == node_id)


class MathGovLeanAxiomsParserTests(unittest.TestCase):
    def test_axioms_clean_empty(self):
        out = l.extract_axioms("MathGov.step1 does not depend on any axioms", "MathGov.step1")
        self.assertEqual(out, [])

    def test_axioms_sorry_detected(self):
        out = l.extract_axioms("MathGov.step1 depends on axioms: [sorryAx]", "MathGov.step1")
        self.assertEqual(out, ["sorryAx"])

    def test_axioms_standard_classical_allowed(self):
        out = l.extract_axioms("MathGov.step1 depends on axioms: [propext, Classical.choice, Quot.sound]", "MathGov.step1")
        self.assertEqual(out, ["propext", "Classical.choice", "Quot.sound"])

    def test_axioms_unknown_format_returns_none(self):
        out = l.extract_axioms("some compiler warning occurred here", "MathGov.step1")
        self.assertIsNone(out)


class MathGovLeanSecurityAndPinningTests(unittest.TestCase):
    def test_path_traversal_denied(self):
        res = l.check_step(LEAN_DEMO_PROJECT, "../evil.lean", "MathGov.step1", "True", "0" * 64)
        self.assertEqual(res["verdict"], "SOURCE_PATH_DENIED")

    def test_unpinned_project_denied(self):
        # ROOT has no lakefile.toml or lean-toolchain at root
        proof_path = EXAMPLES_DIR / "ProofSteps.lean"
        digest = l.sha(proof_path.read_bytes())
        res = l.check_step(ROOT, "governance/math_gov/examples/ProofSteps.lean", "MathGov.step1", "True", digest)
        self.assertEqual(res["verdict"], "UNPINNED_LEAN_PROJECT")

    def test_stale_or_changed_source_denied(self):
        res = l.check_step(LEAN_DEMO_PROJECT, "ProofSteps.lean", "MathGov.step1", "True", "0" * 64)
        self.assertEqual(res["verdict"], "STALE_OR_CHANGED_SOURCE")

    def test_missing_lean_returns_unavailable(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / "Proof.lean").write_text("theorem a : True := trivial")
            (root / "lean-toolchain").write_text("leanprover/lean4:v4.35.0")
            (root / "lakefile.toml").write_text('name = "temp"')
            (root / "lake-manifest.json").write_text("{}")
            with patch.object(l.shutil, "which", return_value=None):
                res = l.check_step(root, "Proof.lean", "a", "True", l.sha((root / "Proof.lean").read_bytes()))
            self.assertEqual(res["verdict"], "LEAN_UNAVAILABLE")

    def test_mock_sorry_axiom_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / "Proof.lean").write_text("theorem a : True := by sorry")
            (root / "lean-toolchain").write_text("leanprover/lean4:v4.35.0")
            (root / "lakefile.toml").write_text('name = "temp"')
            (root / "lake-manifest.json").write_text("{}")
            with patch.object(l.shutil, "which", return_value="/fake/lake"), \
                 patch.object(l.subprocess, "run", return_value=SimpleNamespace(returncode=0, stdout="a depends on axioms: [sorryAx]", stderr="")):
                res = l.check_step(root, "Proof.lean", "a", "True", l.sha((root / "Proof.lean").read_bytes()))
            self.assertEqual(res["verdict"], "DISALLOWED_AXIOMS")
            self.assertIn("sorryAx", res["axioms"])

    def test_mock_clean_pass_does_not_authorize_release(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / "Proof.lean").write_text("theorem a : True := trivial")
            (root / "lean-toolchain").write_text("leanprover/lean4:v4.35.0")
            (root / "lakefile.toml").write_text('name = "temp"')
            (root / "lake-manifest.json").write_text("{}")
            with patch.object(l.shutil, "which", return_value="/fake/lake"), \
                 patch.object(l.subprocess, "run", return_value=SimpleNamespace(returncode=0, stdout="a does not depend on any axioms", stderr="")):
                res = l.check_step(root, "Proof.lean", "a", "True", l.sha((root / "Proof.lean").read_bytes()))
            self.assertEqual(res["verdict"], "LOCAL_LEAN_STEP_CHECK_PASS_PENDING_INDEPENDENT_RECHECK")
            self.assertFalse(res["release_authorized"])
            self.assertFalse(res["proof_complete"])


class MathGovLiveHostLeanCompilationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lean_available = bool(shutil.which("lake") or shutil.which("lean"))

    def test_live_lean_detects_compiler_warning_and_fails_closed(self):
        """ProofSteps.lean in candidate distribution contains an unnecessary simpa which triggers

        a Lean 4.35 compiler linter warning. The runner must fail closed on warnings."""
        if not self.lean_available:
            self.skipTest("Lean 4 / Lake is not installed on this host")

        source_file = LEAN_DEMO_PROJECT / "ProofSteps.lean"
        source_digest = l.sha(source_file.read_bytes())

        res = l.check_step(
            project_root=LEAN_DEMO_PROJECT,
            relative_source="ProofSteps.lean",
            theorem="MathGov.step1",
            expected_statement="forall (n : Nat), n + 0 = n",
            expected_file_sha256=source_digest,
            timeout=60,
        )
        self.assertEqual(res["verdict"], "LEAN_COMPILATION_OR_WARNING")
        self.assertFalse(res["release_authorized"])

    def test_live_lean_compilation_warning_free_step(self):
        """A clean, warning-free step compiles and passes local preflight with allowed axioms."""
        if not self.lean_available:
            self.skipTest("Lean 4 / Lake is not installed on this host")

        clean_src = (
            "namespace MathGov\n\n"
            "theorem step1 (n : Nat) : n + 0 = n := by\n"
            "  simp\n\n"
            "end MathGov\n"
        )
        test_file = LEAN_DEMO_PROJECT / "CleanProofStep.lean"
        test_file.write_bytes(clean_src.encode("utf-8"))
        try:
            source_digest = l.sha(test_file.read_bytes())
            res = l.check_step(
                project_root=LEAN_DEMO_PROJECT,
                relative_source="CleanProofStep.lean",
                theorem="MathGov.step1",
                expected_statement="forall (n : Nat), n + 0 = n",
                expected_file_sha256=source_digest,
                timeout=60,
            )
            self.assertEqual(
                res["verdict"],
                "LOCAL_LEAN_STEP_CHECK_PASS_PENDING_INDEPENDENT_RECHECK",
                f"Expected check pass, got: {res}"
            )
            self.assertEqual(res["axioms"], ["propext"])
            self.assertFalse(res["release_authorized"])
            self.assertFalse(res["proof_complete"])
        finally:
            if test_file.exists():
                test_file.unlink()


class MathGovIntegratedStepVerifierTests(unittest.TestCase):
    def test_runner_fails_when_unpinned(self):
        case = copy.deepcopy(CASE)
        step = mutate_node(case, "S1")
        out = sv.check_formal_step(
            case, "S1", ROOT, "governance/math_gov/examples/ProofSteps.lean",
            ORIGINAL, FORMAL, step["goal_digest"], step["lean"]["source_digest"], CONTRACT
        )
        self.assertEqual(out["verdict"], "BLOCKED")
        self.assertEqual(out["reason"], "LEAN_CHECK_FAILED_OR_NOT_AVAILABLE")
        self.assertFalse(out["proof_verified"])

    def test_step_cannot_fabricate_goal_binding(self):
        case = copy.deepcopy(CASE)
        step = mutate_node(case, "S1")
        out = sv.check_formal_step(
            case, "S1", LEAN_DEMO_PROJECT, "ProofSteps.lean",
            ORIGINAL, FORMAL, "0" * 64, step["lean"]["source_digest"], CONTRACT
        )
        self.assertEqual(out["reason"], "STEP_GOAL_ANCHOR_MISMATCH")

    def test_step_cannot_fabricate_source_binding(self):
        case = copy.deepcopy(CASE)
        step = mutate_node(case, "S1")
        out = sv.check_formal_step(
            case, "S1", LEAN_DEMO_PROJECT, "ProofSteps.lean",
            ORIGINAL, FORMAL, step["goal_digest"], "0" * 64, CONTRACT
        )
        self.assertEqual(out["reason"], "STEP_LEAN_SOURCE_ANCHOR_MISMATCH")

    def test_worker_cannot_claim_self_verified_status(self):
        case = copy.deepcopy(CASE)
        step = mutate_node(case, "S1")
        step["state"] = "FORMALLY_CHECKED"
        out = sv.check_formal_step(
            case, "S1", LEAN_DEMO_PROJECT, "ProofSteps.lean",
            ORIGINAL, FORMAL, step["goal_digest"], step["lean"]["source_digest"], CONTRACT
        )
        self.assertEqual(out["reason"], "STRUCTURAL_OR_SOURCE_ANCHOR_FAILURE")


if __name__ == "__main__":
    unittest.main()
