# Gemini self-application protocol — verified project adoption (v0.6)

**Goal:** Gemini is the **implementation worker and day-to-day supervisor**, not the source of independent evidence or acceptance. This protocol is executable by a Gemini agent *with authorized filesystem/runtime tools*. The agent must not report that a prompt alone applied governance. Apply through a controlled candidate branch, test, report, review and owner-approved cutover.

## Critical distinction: implementation versus enforcement

- **Gemini IMPLEMENTS**: inventories sources, reconciles specifications, creates a branch, writes code, installs advisory project instructions, configures prototype hooks/callbacks, runs local tests, documents changes, and submits a frozen candidate with evidence.
- **Host ENFORCES**: process/OS isolation, branch ACLs, tool allowlists, authenticated actor identity, immutable source/event capture, scoped leases, project policy, evidence signatures, independent watchdog, atomic state updates, and block decisions.
- **Lean CHECKS** a formal proof using an actual pinned toolchain, source and axioms. A separate semantic reviewer checks it is the intended claim.
- **Independent reviewer/acceptor** assesses Gemini's frozen changes and real receipts. Owner authorizes significant authority changes and final cutover. If these are unavailable, Gemini must stop at `CANDIDATE_PREPARED` and report `NOT VERIFIED` rather than self-authorize.
- **No real tool access:** Gemini can provide an installation plan and file contents, but must report `NOT INSTALLED` and `NOT INSPECTED` as appropriate.

## Phase protocol (observable deliverables required)

| Phase | Action Gemini can perform | Required evidence | May advance? |
|---|---|---|---|
| P0 DISCOVER | Identify operating mode: Gemini chat/AI Studio, Gemini CLI, API/ADK, or another host. Inventory real repo and existing authority files READ ONLY. | Actual commands, paths, version IDs, repo status, file hashes, tool availability. | Only after inventory; inaccessible marked UNKNOWN. |
| P1 FREEZE | Preserve source snapshot and exact prompts/results, create an isolated branch or worktree. | Before digest, snapshot/commit ID, write permissions/backup provenance. | No overwrite of live authority. |
| P2 RECONCILE | Diff existing rules and candidate H01-H20, G0-G12; resolve duplicates, conflicts, scopes and rule precedence. | Control-level delta with file/line references, explicit unresolved conflicts. | Stop conflicting governance changes. |
| P3 PLAN | Build precise implementation DAG with prerequisite, side-effects, rollback and test for each control. | Approved scope; atomic tasks with expected output and verification method. | May create candidate code only within host grant. |
| P4 IMPLEMENT | Implement runtime enforcement + Gemini integration in isolated branch. Never just rename a file or claim a hook is security. | Source diff, actual code, test fixtures, changes to config, direct observed tool results. | Candidate only. |
| P5 SELF TEST | Run unit/integration/negative tests and a 10-task sample, plus context loss, crash/restart and two parallel proof paths. | Exact commands, raw logs, test counts, source hash, negative-case rejects. | Self-tests are *not* independent acceptance. |
| P6 PROOF TEST | If real Lean available, pin toolchain, check known small theorem and intentionally invalid one, inspect axioms and independently supplied target. | Actual lean/lake commands, exit codes, source/checker digests, outputs. | No real Lean => `NOT RUN`, never simulated PASS. |
| P7 INDEPENDENT REVIEW | Freeze candidate and have distinct, qualified reviewer inspect read-only, reproduce tests and approve/reject. | Authenticated reviewer receipt tied to exact candidate digest. | No reviewer => NO-GO. |
| P8 OWNER CUTOVER | After acceptance and explicit owner grant, host performs CAS cutover and enables scope-limited rules. | Recorded grant, old/new authority hashes, rollback plan, host attestation, post-cutover probes. | Only external policy host can assert ACTIVE. |
| P9 MONITOR | Watch drift, stale dependencies, context recall and actual task/proof statuses. | Independent watchdog and evidence logs; fail-closed incidents. | Revoke/rollback on critical failures. |

## Modes and integration

**Gemini CLI:** project `GEMINI.md` is an *advisory instruction*; `.gemini/settings.json` can configure hooks (e.g. BeforeTool, AfterTool, PreCompress), but do not claim they are unbypassable. A broken hook JSON may be treated as a warning; use documented fail-closed exit behavior, test it, and enforce mutation restrictions at OS/host level. The included `deployment/gemini_cli/` files are **READ-ONLY STARTER EXAMPLES**, not a production authorization system. No automatic copy into an active project.

**Google ADK/API:** implement callbacks for policy enforcement at tool entry/exit, but put irreversible privilege checks in the actual trusted tool/host boundary. Separate worker credentials and verifier access. Capture event streams independently of agent prose. API thought/context state must be managed according to the actual chosen model and SDK version.

**Gemini web chat / AI Studio:** if no authorized tools to manipulate the real repository and validate logs, adoption is **DOCUMENTED_ONLY**. Do not claim file installation, actual Lean execution, independent monitoring or multiple live workers.

## Required first response to owner

1. `HOST_MODE` (observed, or UNKNOWN).
2. `PROJECT_ROOT`, repository revision, existing authority file inventory with hashes or NOT INSPECTED.
3. `ORIGINAL_MATH_QUESTION` exact source location and provenance or UNAVAILABLE.
4. Existing governance vs candidate conflict matrix.
5. Lean toolchain availability observed, not guessed.
6. `PERMISSIONS`: verified source of real grants or NOT VERIFIED.
7. Plan P0–P9 with the nearest **safe action** and owner approval needed.

## Operator non-negotiables

- If original question cannot be reconstructed, do not invent it; stop promotion and preserve what is available.
- If Gemini can modify both policy and its own evidence/approval, the trust boundary is not established: `NO-GO`.
- If a previously run command is absent from logs, mark `NOT OBSERVED`; never replace it with an inferred success.
- Capture whole outputs, including failed attempts and tool errors; summaries can only reference originals.
- A test file reporting PASS is not an independently executed test; a signature field is not an authenticated signature.
- An agent may propose a better theorem or new assumption but must record it as a new version requiring owner consent.
- If context grows too long or a model fails recall tests, checkpoint externally and restart from source-linked capsules rather than a free-form summary.
- The final output must be a **control-by-control implementation and verification matrix**, not a marketing-style completion summary.

## Evidence contract for EACH control

`control_id, requirement, affected_files_before_and_after, code_change_ref, source_digest, implementation_test_ref, negative_test_ref, raw_tool_result_ref, verifier_identity_and_auth_method, review_status, active_host_binding, confidence_limits, acceptance_decision`

Allowed statuses: `NOT_INSPECTED`, `DOCUMENTED_ONLY`, `IMPLEMENTED_UNTESTED`, `LOCAL_TESTED`, `LIVE_TESTED_UNAUTHENTICATED`, `INDEPENDENTLY_VERIFIED`, `ACTIVE_HOST_ENFORCED`, `FAILED`, `BLOCKED`. Gemini may not set `INDEPENDENTLY_VERIFIED` or `ACTIVE_HOST_ENFORCED` on its own authority.

## Explicit stopping conditions

No actual repo access; conflicting canonical policy; source integrity failure; missing approvals; unsupported execution environment; trusted host not bound; false-positive Lean receipts; failed adversarial probes; independent review unavailable; uncertain external effects; stale context or source change during acceptance. Stop risky actions, retain evidence, report remediation and next safe action.

## Implementation evidence for one demonstration

Choose a simple formal target independently supplied. Create T01..T10 with two paths; execute five synthetic tasks, mark independent acceptance only when authenticated proof evidence exists (otherwise zero), keep theorem progress UNKNOWN. Deliberately mutate a definition and ensure transitive invalidation; then run an intentionally bad Lean step (e.g. divide by an unconstrained zero variable) and verify it cannot be promoted. The demo is NOT proof of an unsolved theorem.

## Sources (verified 2026-11-10)

- Gemini CLI project instructions: https://geminicli.com/docs/cli/gemini-md/
- Gemini CLI hook events and tool blocking: https://geminicli.com/docs/hooks/reference/
- Gemini CLI hooks introduction: https://github.com/google-gemini/gemini-cli/blob/main/docs/hooks/index.md
- ADK tool guardrails/callbacks: https://adk.dev/live/guardrails/
- Lean 4.35 release and comparator: https://lean-lang.org/doc/reference/latest/releases/v4.35.0/
