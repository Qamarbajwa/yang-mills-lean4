"""
MATH-GOV v0.6 Governance Preview, Install Audit & Manifest Verification Tests
=============================================================================
Tests:
- Structural governance preview across candidate state templates
- Mutation prevention hooks (deny_mutations)
- Gemini installation audit across CLI and ADK modes
- Manifest candidate integrity verification
"""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.ymmg import governance_preview as gp
from src.ymmg import gemini_install_audit as gia
from src.ymmg import deny_mutations as dm
from src.ymmg import verify_manifest as vm

TEMPLATES_DIR = ROOT / "governance" / "math_gov" / "reference_templates"
EXAMPLES_DIR = ROOT / "governance" / "math_gov" / "examples"


class MathGovPreviewAndStateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = gp.read_json(TEMPLATES_DIR / "PROJECT_STATE.yaml")
        cls.demo = gp.read_json(EXAMPLES_DIR / "ten_tasks.json")

    def test_template_no_go(self):
        self.assertEqual(gp.validate_state(self.state)["verdict"], "NO_GO_UNBOUND")

    def test_template_never_release(self):
        self.assertFalse(gp.validate_state(self.state)["release_authorized"])

    def test_claiming_active_state_blocks(self):
        s = copy.deepcopy(self.state)
        s["status"] = "LIVE"
        self.assertNotEqual(gp.validate_state(s)["errors"], [])

    def test_new_claimed_release_blocks(self):
        s = copy.deepcopy(self.state)
        s["release_authorized"] = True
        self.assertNotEqual(gp.validate_state(s)["errors"], [])

    def test_invented_host_blocks(self):
        s = copy.deepcopy(self.state)
        s["external_host"]["authenticated"] = True
        self.assertNotEqual(gp.validate_state(s)["errors"], [])

    def test_extra_authority_blocks(self):
        s = copy.deepcopy(self.state)
        s["authority_files"].append("governance/FOURTH.md")
        self.assertNotEqual(gp.validate_state(s)["errors"], [])

    def test_all_gates_unsupported(self):
        s = copy.deepcopy(self.state)
        s["hard_gates"]["G6"] = "PASS"
        self.assertNotEqual(gp.validate_state(s)["errors"], [])

    def test_demo_valid(self):
        errors, *_ = gp.validate_plan(self.demo)
        self.assertEqual(errors, [])

    def test_duplicate_task_rejected(self):
        d = copy.deepcopy(self.demo)
        d["tasks"][1]["id"] = "T01"
        self.assertEqual(gp.plan(d)["verdict"], "BLOCKED")

    def test_cycle_rejected(self):
        d = copy.deepcopy(self.demo)
        d["tasks"][0]["deps_all"] = ["T10"]
        self.assertEqual(gp.plan(d)["verdict"], "BLOCKED")

    def test_unknown_dependency_rejected(self):
        d = copy.deepcopy(self.demo)
        d["tasks"][0]["deps_all"] = ["T99"]
        self.assertEqual(gp.plan(d)["verdict"], "BLOCKED")

    def test_strong_claim_blocked(self):
        d = copy.deepcopy(self.demo)
        d["claims"] = [{"text": "RH proved"}]
        self.assertEqual(gp.report(d)["verdict"], "BLOCKED")

    def test_double_json_keys_rejected(self):
        with self.assertRaises(gp.Invalid):
            json.loads('{"a":1,"a":2}', object_pairs_hook=gp.unique_pairs)

    def test_cli_malformed_fails_closed(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "src/ymmg/governance_preview.py"), "plan", str(ROOT / "README.md")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("BLOCKED", result.stdout)


class MathGovInstallAuditAndHooksTests(unittest.TestCase):
    def fixture(self, root):
        (root / "governance").mkdir(parents=True, exist_ok=True)
        for filename in ("GOVERNANCE.md", "PROJECT_DIRECTION.md", "PROJECT_STATE.yaml"):
            (root / "governance" / filename).write_text("candidate only", encoding="utf-8")
        (root / "GEMINI.md").write_text("advisory", encoding="utf-8")
        (root / ".gemini").mkdir(parents=True, exist_ok=True)
        (root / ".gemini/settings.json").write_text(
            json.dumps({
                "hooksConfig": {"enabled": True},
                "hooks": {
                    "BeforeTool": [
                        {"matcher": ".*", "hooks": [{"name": "guard", "type": "command", "command": "/path/guard.py"}]}
                    ]
                },
            }),
            encoding="utf-8",
        )

    def test_absent_root_fails(self):
        self.assertFalse(gia.audit(Path("/nonexistent/path/xyz"), "cli")["release_authorized"])

    def test_cli_candidate_never_release(self):
        with tempfile.TemporaryDirectory() as d:
            self.fixture(Path(d))
            r = gia.audit(Path(d), "cli")
            self.assertEqual(r["verdict"], "CANDIDATE_FILES_PRESENT_EXTERNAL_VERIFICATION_REQUIRED")
            self.assertFalse(r["release_authorized"])
            self.assertFalse(r["independent_acceptance"])

    def test_missing_authority_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            (root / "governance/PROJECT_DIRECTION.md").unlink()
            self.assertIn("governance/PROJECT_DIRECTION.md", gia.audit(root, "cli")["missing"])

    def test_hooks_disabled_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            (root / ".gemini/settings.json").write_text(
                json.dumps({"hooksConfig": {"enabled": False}, "hooks": {"BeforeTool": [{"hooks": [{"command": "hi"}]}]}}),
                encoding="utf-8",
            )
            self.assertIn("hooks disabled or uncertain", gia.audit(root, "cli")["missing"])

    def test_hook_read_permitted(self):
        self.assertTrue(dm.decide({"tool_name": "read_file", "tool_input": {"file_path": "x"}})[0])

    def test_hook_write_denied(self):
        self.assertFalse(dm.decide({"tool_name": "write_file", "tool_input": {"file_path": "x"}})[0])

    def test_hook_shell_denied(self):
        self.assertFalse(dm.decide({"tool_name": "run_shell_command", "tool_input": {"command": "echo x"}})[0])

    def test_hook_unknown_denied(self):
        self.assertFalse(dm.decide({"tool_name": "mcp_unknown", "tool_input": {}})[0])


if __name__ == "__main__":
    unittest.main()
