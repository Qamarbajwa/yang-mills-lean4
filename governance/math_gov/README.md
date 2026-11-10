# MATH-GOV v0.6 — Complete Project Governance Adoption Candidate

**Status: UNBOUND / CANDIDATE / NO LIVE LEAN / NO AUTHENTICATED GOOGLE CHRYSALIS / NO AUTOMATIC PROMOTION.**

This is the complete *proposed project-local governance overlay* for a mathematical-research project run with Gemini or other LLMs. It contains exactly three candidate project authority files, a full operator directive, staged binding plan, technical/math controls, Python **read-only structural** host previews, tests, reproducible examples and a **versioned, unchanged** copy of the prior v0.5 Step & Proof Obligation Engine. It does not overwrite universal Governance OS v4.0.4 or any live project rules.

## Read first
1. `governance/GOVERNANCE.md` = HOW: hard/soft rules, mathematical gates, supervisor–worker–verifier separation.
2. `governance/PROJECT_DIRECTION.md` = WHAT/WHY: bind original exact question and independently authored Lean challenge.
3. `governance/PROJECT_STATE.yaml` = CURRENT EVIDENCE: intentionally UNBOUND, release false.
4. `adoption/GEMINI_SUPERVISOR_MASTER_DIRECTIVE.md` and `adoption/GEMINI_SELF_APPLICATION_PROTOCOL.md` = Gemini installation and reporting instructions, *not* a substitute for external enforcement.
5. `adoption/GEMINI_PROJECT_CONTEXT_TEMPLATE.md` and `deployment/gemini_cli/` = optional advisory CLI setup samples, not automatically installed.
5. `adoption/PROJECT_ADOPTION_PLAN.md` = real binding steps and test gates.
6. `spec/CONTROL_MATRIX.md` = control-by-control coverage; which are merely specified vs structurally tested vs require a real trusted host.
7. `diagrams/` = Mermaid architectures and lifecycle.
8. `components/v0_5/` = unmodified previously tested prototype, with its own README and verification limits.

## Use with Gemini

Upload the ZIP or make its files available in the authorized project workspace, then give Gemini `adoption/PROJECT_BOOTSTRAP_MESSAGE.txt`. It must first perform a **read-only audit** and obtain genuine authorization before any adoption. If a Gemini chat session cannot run tools, report **INTEGRATION NOT POSSIBLE FROM CHAT ALONE**, not an invented installation.

## Local inspection / demonstrations (Python 3.10+, stdlib)
```
python -m unittest discover -s tests -v
python runtime/governance_preview.py audit governance/PROJECT_STATE.yaml
python runtime/gemini_install_audit.py /PATH/TO/REAL/PROJECT --mode cli
python runtime/governance_preview.py plan examples/ten_tasks.json
python runtime/governance_preview.py capsule examples/ten_tasks.json T06
python runtime/governance_preview.py report examples/ten_tasks.json
PYTHONPATH=components/v0_5 python -m unittest discover -s components/v0_5/tests -v
```

All `runtime/` outputs are explicitly **PREVIEW / NON-AUTHORITATIVE**. They cannot dispatch, authenticate agents, mutate repositories, prove theorems, apply source diffs, or approve publication.

## What is implemented versus not implemented
**Implemented locally:** schema checks, hard-rule preflight, typed AND/OR task preview, step/claim status separation, context-package derivation from an illustrative registry, report calibration, inherited step/obligation structural engine, Lean adapter that blocks without a real toolchain, and exact-byte local SQLite ledger for manually supplied prompt/output bytes.

**Not implemented or verified:** Gemini API/ADK integration, actual supervisor running with live workers, externally attested owner binding, trusted isolated Lean execution, kernel check of a real target, source-to-proof semantic equivalence, independent mathematical reviewers, actual secret/auth boundary, full event capture, remote ledger anchoring, transactional CAS writes, real-time watchdog, production release or scientific publication assurance.

## Safety/correctness boundaries
- Never paste or grant credentials/secret material to workers.
- This template should first be installed in a separate branch or workspace, reconciled against your existing active three authority files, reviewed, then explicitly approved.
- Do not copy the three template authorities over active canonical records without a full diff and cutover process.
- Model name, long context limit and number of agents are **not** verification receipts.
- All mathematical exploration is allowed to be uncertain; no false theorem-percentage based on task counts.

## Maintained source materials and official references
- Lean 4.35 release notes: https://lean-lang.org/doc/reference/latest/releases/v4.35.0/
- Lean axioms and `#print axioms`: https://lean-lang.org/doc/reference/latest/Axioms/
- Lean `lake comparator`/`lake check`: https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/
- Google Project Chrysalis research: https://developers.googleblog.com/en/architecting-governed-self-evolving-ai-agents-on-gemini-agent-platform/
- NIST AI RMF Playbook: https://airc.nist.gov/airmf-resources/playbook/

## Gemini-applied governance: implementation is not self-attestation

Gemini can implement this package through a read-only audit, branch-isolated code changes, proof-step tests, Lean runner setup, and evidence-generating verification. Its own reports cannot authenticate its checks, reviewer independence, or a host-enforced cutover. Follow `adoption/GEMINI_SELF_APPLICATION_PROTOCOL.md`. The included CLI read-only hook is deliberately preliminary and cannot confer OS-level security.
