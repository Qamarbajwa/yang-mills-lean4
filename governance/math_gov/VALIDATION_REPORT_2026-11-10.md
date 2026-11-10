# MATH-GOV v0.6 — candidate validation and adoption boundaries

Date: 2026-11-10. Candidate is **UNBOUND / NO-GO FOR LIVE MATHEMATICAL GOVERNANCE**.

## Local checks executed

| Test | Observed outcome | What it establishes |
|---|---|---|
| New v0.6 `python -m unittest discover -s tests -v` | 54 tests, all PASS | Structural validation of candidate state, demo planning/reporting, Gemini local-install scanner and read-only tool-hook example |
| Inherited v0.5 `PYTHONPATH=components/v0_5 python -m unittest discover -s components/v0_5/tests -v` | 57 tests, all PASS | Existing structural mathematical step/proof obligation engine remains executable as a copied component |
| Candidate file hash verification | All 56 payload hashes match | Byte consistency of *supplied* files with *supplied* manifest, **not authenticity** |
| `runtime/governance_preview.py audit` | NO_GO_UNBOUND | Candidate explicitly has no live project authority |
| `runtime/governance_preview.py report` demo | 10 tasks; 5 executed/submitted; 2 submitted pending review; 0 independent acceptances; theorem progress UNKNOWN | Partial-task accounting without false theorem claims |
| Real `lean` and `lake` binaries | Not available in this environment | No theorem formally verified here |
| Actual Gemini repo, hooks, ADK runtime, actor credentials | NOT CONNECTED / NOT INSPECTED | No claim that any Gemini project was modified or that controls actually ran live |

The exact versioned files and current manifest define the candidate; the notes above do not serve as live execution receipts.

## Gemini auto-application controls delivered

1. `adoption/GEMINI_SELF_APPLICATION_PROTOCOL.md`: P0–P9 installation and verification procedure with separate implementer, host, mathematical verifier and independent acceptor.
2. `adoption/GEMINI_SUPERVISOR_MASTER_DIRECTIVE.md`: comprehensive research and orchestration behavior, reporting and mandatory self-application instruction.
3. `adoption/PROJECT_BOOTSTRAP_MESSAGE.txt`: one message to give to Gemini with the ZIP.
4. `adoption/GEMINI_PROJECT_CONTEXT_TEMPLATE.md`: optional Gemini CLI project context, advisory only.
5. `deployment/gemini_cli/`: fail-closed read-only hook *example*, not a trusted sandbox or production mutation policy.
6. `runtime/gemini_install_audit.py`: read-only scanner for a named actual project directory, refusing to attest live enforcement or independent acceptance.
7. `governance/`: exactly three candidate project authority files; existing canonical records are untouched.
8. `components/v0_5`: copied previous step and proof-obligation structural engine, including Lean runner adapter.

## Explicit remaining acceptance blockers

- Project root, actual original question/transcript, existing live rules and authorizations not bound.
- No trusted external write/policy host, authenticated user grants or independent watchdog/approval identities.
- No guaranteed complete prompt/tool-result capture or off-host anchor.
- No actual Gemini CLI hook installation, test, or SDK callback integration.
- No real Lean build/replay, axiom audit or semantic theorem check on the user's target.
- No end-to-end adversarial tests A01–A26 in a real host.
- No independent reviewer or qualified acceptor has approved the candidate or performed live cutover.

**Decision:** Local structural candidate is prepared, byte-consistent and unit-tested. It must not be described as deployed, independently proven, secure by construction or release-ready. The next safe action is Gemini read-only P0 inspection against the real project, followed by branch-isolated implementation and evidence-backed external acceptance.
