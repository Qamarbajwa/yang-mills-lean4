# Delegated evidence, diagram, search and migration contract (v4.1.0-r3)

This file is a technical companion to the active governance, not a fourth project-level operational authority. Read it when implementing or validating evidence, diagram-first conformance, relative standards searches, specification gates, state transitions, migration or cutover.

## 1. Evidence dimensions & independence

Evidence strength:
- `E1` — static inspection, schema, lint, type, diagram-syntax or configuration evidence.
- `E2` — automated behavioral evidence such as unit, integration, diagram-to-code trace or regression tests.
- `E3` — reproducible execution bound to an exact candidate, environment and relevant inputs/outputs.
- `E4` — qualified independent verification or reproduction by a distinct Reviewer (`IND2`/`IND3`).
- `E5` — externally anchored or tamper-resistant evidence where applicable.

Self-report alone is `ASSERTION`, not verification.

Independence levels:
- `IND0` — Worker/same task context; not independent.
- `IND1` — limited separation/fresh context; insufficient for review or acceptance under the strict v4.1.0-r3 profile.
- `IND2` — distinct qualified Reviewer task/process with sufficient separation from Worker authorship; mandatory minimum across all `R0`–`R3` tasks under the strict `THREE_ROLE` profile.
- `IND3` — materially independent external verification; required when bound project/domain policy demands it.

## 2. Tri-Agent receipts (Worker, Reviewer, Acceptor)

All governed work under the strict profile requires three linked receipts from distinct Worker, Reviewer and Acceptor identities; all five actor IDs (`worker_id`, `reviewer_id`, `acceptor_id`, `router_id`, `watchdog_id`) must be mutually distinct. `IND0`/`IND1`, `SELF_CHECKED` and `REVIEW_ACCEPT` do not satisfy independent acceptance:
1. **Worker Candidate Receipt:** Identifies `worker_id`, `candidate_digest`, `specification_gate` status (`SPEC_VERIFIED`), locked `diagram_refs`, `relative_search_refs`, active paradigms, executed test commands and raw exit codes.
2. **Reviewer Audit Receipt:** Identifies `reviewer_id` (`!= worker_id`), `independence` (`IND2`+), observed `candidate_digest`, read-only verification of (a) Contract & Intent Fidelity, (b) 1:1 Diagram-to-Code Conformance, (c) Relative Standards & Paradigm Compliance, (d) Minimalist iOS UI Philosophy compliance (where UI applies), (e) Negative/Regression Test sufficiency, and (f) Brownfield characterization preservation. Outputs `REVIEW_PASS` or `REVIEW_FAIL`.
3. **Acceptor Decision Receipt:** Identifies `acceptor_id` (`!= worker_id` and `!= reviewer_id`), verifies `candidate_digest`, verifies all `required_hard_gates` are present and `PASS` (or justified `NOT_APPLICABLE`), runs `node tools/verify-package.mjs`, and records `ACCEPTED_BOUNDED` in `PROJECT_STATE.yaml`.

## 3. Specification Gate & Clarification Request Packet (CRP) contract

Before coding any capability, the Worker validates that all six pre-definition dimensions exist. If any dimension is missing or ambiguous:
- `specification_gate.status` MUST transition to `BLOCKED_MISSING_SPEC`.
- Each entry in `specification_gate.missing_specification_prompts` MUST be a non-empty string or reference to a **Clarification Request Packet (CRP)** recording:
  1. `missing_dimension` (`INTENT_ACTOR`, `DATA_INTERFACE`, `PARADIGM_BOUNDARY`, `DIAGRAM_MAPPING`, `RELATIVE_STANDARD`, or `ACCEPTANCE_CRITERIA`),
  2. `blocking_reason` (why autonomous assumptions are unsafe),
  3. `relative_search_performed` (Tier 1–4 sources checked),
  4. `standardized_options` (2–3 concrete options with trade-offs for owner decision).
- `RELEASE_ELIGIBLE` is strictly forbidden while `specification_gate.status !== "SPEC_VERIFIED"` or `specification_gate.missing_specification_prompts.length > 0`.

## 4. Diagram-First verification contract

Diagrams are verified before and after implementation:
- **Supported Diagram Classes:** `C4_CONTEXT`, `C4_CONTAINER`, `C4_COMPONENT`, `SEQUENCE`, `STATE_MACHINE`, `ACTIVITY_FLOW`, `ERD_DATA`, `TYPE_GRAPH`, `DATA_FLOW`, `UI_WIREFLOW`.
- **Supported Notations:** `Mermaid`, `PlantUML`, `D2`, `Graphviz`, `ASCII_STRUCTURED`.
- **Traceability Check:** Every consequential module, state machine, API sequence or UI screen must map to a locked diagram (`specification_gate.diagram_first_status == "DIAGRAM_LOCKED"`). Unmapped code edges or state transitions trigger a `DIAGRAM_DRIFT` failure in review.

## 5. Relative Standards Search receipt contract

Every Relative Search executed to resolve a technical standard or architectural pattern is recorded in `specification_gate.relative_search_refs` (and the delegated Standards Registry) with:
- `context_vector`: `{ archetype, domain_intent, paradigm_runtime, risk_tier, compatibility_mode }`,
- `tiers_searched`: `['TIER1_LOCAL', 'TIER2_FORMAL_STD', 'TIER3_PLATFORM_CANON', 'TIER4_EMPIRICAL_REF']`,
- `selected_standard`: e.g., `RFC-9457`, `ISO-19650`, `APPLE-HIG-IOS18`, `WCAG-2.2-AA`,
- `enforced_invariants`: concrete testable rules checked by the Reviewer.

## 6. Minimalist iOS / Apple HIG UI verification contract

For capabilities with a visual surface, UI evidence must verify:
1. **Deference & Negative Space:** Hairline borders (`0.5px`–`1px`), uncluttered viewport, progressive disclosure (`PRIMARY`, `SECONDARY`, `ON_DEMAND`).
2. **Translucent Materials & Concentricity:** Glassmorphic blur/saturation tokens and mathematically concentric corner radii (`R_outer = R_inner + Padding`).
3. **Typography:** `SF Pro` / `Inter` / `system-ui` hierarchy + `SF Mono` (`tabular-nums`) for metrics.
4. **Semantic Tokens:** True dark/light adaptive surfaces and WCAG AA/AAA contrast.
5. **Hit Targets & Spring Motion:** `>= 44x44pt` touch targets (`>= 28x28px` desktop) and interruptible critically damped spring transitions.

## 7. Exact live-effect boundary and v4.1.0-r3 validation repairs (F1, F2, F3 closed)

1. **Closure of F1 (Required Hard-Gate Inventory):**
   - `PROJECT_STATE.yaml` includes `required_hard_gates` (array of mandatory gate names).
   - For `RELEASE_ELIGIBLE`, `validateReleaseState` requires `required_hard_gates` to be non-empty, requires every gate listed in `required_hard_gates` to exist in `state.hard_gates`, and verifies each is `PASS` (with non-empty `evidence_refs` and matching `subject_digest`) or `NOT_APPLICABLE` (with non-empty `reason`). A single trivial gate can no longer satisfy structural validation when mandatory project gates are declared.
2. **Closure of F2 (Effect Receipt State Revision & Frozen Subject Echo):**
   - `executeAuthorizedDeployment` now strictly requires the trusted atomic adapter's receipt to echo `receipt.state_revision === state.revision` and `receipt.frozen_subject_digest === state.candidate_identity.subject_digest` in addition to `artifact_digest`, `grant_consumed === true`, `durable === true`, and `exact_artifact_verified_at_effect === true`.
3. **Closure of F3 (NO-GO Historical Field Validation):**
   - When `release.eligibility.status === 'NO-GO'`, if historical `decided_at` or `valid_until` timestamps are present, `validateReleaseState` validates that they are well-formed RFC 3339 instants, that `decided_at` is not in the future relative to `now`, and that `valid_until > decided_at`.
4. **Closure of Specification & Diagram Gates for Release:**
   - `RELEASE_ELIGIBLE` fails closed unless `specification_gate.status === 'SPEC_VERIFIED'`, `specification_gate.diagram_first_status === 'DIAGRAM_LOCKED'`, and `specification_gate.missing_specification_prompts.length === 0`.

## 8. Minimum adoption tests (v4.1.0-r3 expanded suite)

In addition to the 30 baseline adoption tests from v4.0.6-r3, each adopting project verifies:
31. Missing or ambiguous specification halts coding (`BLOCKED_MISSING_SPEC`) and emits a Clarification Request Packet rather than guessing.
32. Consequential implementation without a locked intent-relative diagram (`DIAGRAM_LOCKED`) is rejected.
33. Code introducing undocumented module dependencies or state transitions absent from the locked diagram is rejected (`DIAGRAM_DRIFT`).
34. Relative Search Protocol queries follow the 5-axis context vector and 4-tier authority hierarchy before custom protocols/schemas are invented.
35. Tri-Agent separation (`worker_id != reviewer_id != acceptor_id`) is enforced for `THREE_ROLE` paths, and missing `required_hard_gates` entries block `RELEASE_ELIGIBLE`.
36. Atomic live-effect receipts missing exact `state_revision` or `frozen_subject_digest` echo are rejected fail-closed.

## v4.1.0-r3 pre-code evidence and isolated Super-Agent execution

Pre-code approval receipts must bind project ID, capability, six dimension refs and their actual contents/digests, design/diagram refs, diagram lock digest, standards-search record and edition, authorized Worker identity, state revision, diagram Reviewer identity/qualification and independent approval time, permitted mutation scope and validity. The project-bound `verifyPreCodeAuthorization` adapter authenticates current facts, diagram approval and freshness; the generic `validatePreCodeAuthorization` checks only shape plus the adapter response. Its synthetic unit tests are not proof of real authorization.

Router receipts identify event class/source trust, Fast/Slow classification, bound policy/mandate, rejection reason, budget, subject scope and event cursor without granting rights. Watchdog receipts identify independent clock/liveness source, stall/race/retry/cost signal, bounded cancellation/quarantine action, reconciliation condition and immutable before/after reference. Heartbeat presence alone never proves work progress. Watchdog is not a technical reviewer or acceptor. If a task has uncertain external effects, do not retry until grant/effect reconciliation is authoritative. Preserve all history, including preexisting NO-GO and `LEGACY_UNSPECIFIED` observations.

## v4.1.0-r3 subject-scope and blocker-reconciliation clarification

`specification_gate.subject_scope_ref` binds the active approved specification and diagrams to a single exact change scope. The frozen candidate may contain several scopes, but the local single-gate helper is authorized only for its explicitly approved scope. To run multiple independent Worker mandates concurrently, projects must provide an independently reviewed per-scope gate/lease adapter; never recycle one scope's approved diagram receipt for another. A structural test cannot authenticate the approval or ensure fresh repository diagram bytes.

`blockers` may use legacy strings (treated as global unresolved blockers) or structured scoped records. Until a project verifies status and scope, a missing/unknown scope is a global blocker; only `status=RESOLVED` is nonblocking locally. A distinct unresolved blocker for an unrelated exact scope may coexist with work for the approved scope, subject to project-bound overlapping/parent scope checks. Reconciliation and active-state writes remain single-writer compare-and-swap responsibilities.

## Autonomous cycle receipts and handoffs

Every autonomous phase requires a trusted receipt with `receipt_id`, `phase`, `objective_ref`, `subject_scope`, `state_revision`, `subject_digest`, `actor_id`, `outcome`, and evidence reference, checked against the exact mandate. A review must be from the Reviewer in read-only code context; acceptance must be from the distinct Acceptor. Audit the runtime adapter's identity assertions and source permissions, not merely string labels. The plan/dispatch helper is not a replacement for the trusted project gate. Stop/reconcile when receipt identity or state changes, lease expires, retry budget is exhausted, or external effects are uncertain. Never advance a stage based on a favorable synthetic receipt while claiming real-environment proof.
