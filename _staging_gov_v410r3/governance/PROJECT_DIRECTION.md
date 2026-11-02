# Project direction — UNBOUND TEMPLATE

Governance version: 4.1.0-r3. This file defines intended scope, contracts, diagrams, paradigms, standards and UI philosophy—not live progress. Populate from the target project's actual owner decisions and repository truth; do not activate placeholders.

## 1. Intent, product archetype and adoption mode

Record:
- **Project Identity & Purpose:** Core problem solved, target users, desired outcomes, non-goals and unacceptable outcomes.
- **Adoption Mode:** `NEW_PROJECT` (Greenfield), `MID_PROJECT_UNGOVERNED` (Established Brownfield without prior governance), or `MIGRATION_GOVERNED` (Established Brownfield migrating from prior governance).
- **Product Archetype:** Select one primary in `project.product_archetype` and delegate secondary supported surfaces (when genuinely applicable); select from (`WEB_APP`, `MOBILE_IOS`, `DESKTOP_CAD_BIM`, `CLI_TOOL`, `API_SERVICE`, `DISTRIBUTED_SYSTEM`, `EMBEDDED_EDGE`, `DATA_ML_PIPELINE`, `AUTONOMOUS_AGENT_SWARM`, `LIBRARY_SDK`).
- **Owner, Business, Legal & Exposure Boundaries:** Reserved actions requiring explicit owner sign-off, separating milestone completion from release eligibility and live deployment.

## 2. Multi-paradigm engineering matrix

Declare the active programming and architectural paradigms governing each layer or module (`FUNCTIONAL`, `OOP`, `PROCEDURAL`, `DECLARATIVE_UI`, `REACTIVE_STREAM`, `EVENT_DRIVEN`, `ACTOR_MODEL`, `DATA_ORIENTED`, `RELATIONAL_LOGIC`):
- Define purity, state-mutation, concurrency and error-handling invariants per boundary.
- Specify explicit adapter contracts where two paradigms meet (e.g., pure `FUNCTIONAL` domain core connected to an `OOP` repository adapter or a `DECLARATIVE_UI` view layer).
- For established projects, document existing legacy paradigm boundaries and characterization rules before any refactoring.

## 3. Pre-defined capability contracts and Missing-Part Gate

Use stable capability IDs. Every capability must pre-define the **6 canonical specification dimensions (`specification_gate.dimension_refs`) before autonomous Worker coding begins**:
1. **Intent, Actors & Entry Surface (`intent_actors`):** Intended owner/user outcome, initiating actors, permitted/forbidden actions, and target surface (UI route/view, CLI, API, job, or `NONE_BY_DESIGN`).
2. **Data & Interface Contracts (`data_interfaces`):** Exact input/output payloads, validation constraints, units, persistence ownership and state transitions.
3. **Paradigm Boundaries (`paradigm_boundaries`):** Governing paradigm rules, purity invariants and cross-paradigm adapter interfaces.
4. **Diagram Mapping (`diagrams`):** Exact references to the locked diagrams governing this capability (`C4`, `SEQUENCE`, `STATE_MACHINE`, `ERD_DATA`, `UI_WIREFLOW`).
5. **Relative Standards Bound (`relative_standards`):** Specific RFCs, ISO standards, platform guidelines or security profiles discovered via the Relative Search Protocol.
6. **Acceptance, Negative & Recovery Criteria (`acceptance_negative`):** Deterministic normal/negative test conditions, error taxonomy, retry/idempotency rules, and `LOAD_CONCURRENCY_ENDURANCE` (`REQUIRED` with bounds or `N/A` with rationale).

**Missing-Part Rule:** If any of the 6 dimensions above is missing or ambiguous, mark the capability `BLOCKED_MISSING_SPEC` in `PROJECT_STATE.yaml` and issue a **Clarification Request Packet (CRP)** to the owner (or execute the Relative Search Protocol for purely technical standards) before writing code.

## 4. Diagram-First architecture & blueprint registry

Diagrams are drawn **first** relative to project intent and followed strictly during implementation and review. Register or embed canonical diagrams using deterministic text-as-code notations (`Mermaid`, `PlantUML`, `D2`, `Graphviz`, or structured `ASCII`):

| Diagram Class | When Required | Required Style & Granularity | Code Conformance Invariant |
|---|---|---|---|
| `C4_CONTEXT` & `C4_CONTAINER` | Every project (Greenfield upfront; Brownfield As-Is discovery) | Hierarchical boundary boxes, explicit protocol/dependency arrows | No cross-module import or network call allowed unless an explicit arrow exists. |
| `C4_COMPONENT` | Complex services, kernels, CAD/BIM engines, agent swarms | Internal module decomposition and interface ports | Directory/module exports must match component ports 1:1. |
| `SEQUENCE` | All API flows, async jobs, external integrations, 3-agent handoffs | Temporal lifelines, sync/async arrowheads, error/timeout alt-blocks | Handler invocation order, timeout bounds and error payloads must match lifelines. |
| `STATE_MACHINE` | Autonomous workflows, UI view states, entity lifecycles, concurrency | Finite state nodes, explicit event triggers, `[guard]` conditions | Every state enum and transition function in code must map 1:1 to statechart edges. |
| `ERD_DATA` & `TYPE_GRAPH` | Databases, file formats, domain models, state stores | Crow's foot cardinality or algebraic sum/product type trees | Migrations, schemas and type definitions must match entity attributes and relations. |
| `DATA_FLOW` (DFD) | Security boundaries, AI/ML pipelines, untrusted input parsing | Process nodes, data stores, explicit trust-boundary dashed lines | Input sanitization and auth checks must sit on every trust-boundary crossing. |
| `UI_WIREFLOW` | All user-facing screens, modals, toolbars and interactive canvases | Minimalist wireframe nodes connected by user gesture/action edges | Route tables, navigation controllers and view states (`empty`/`loading`/`error`/`ready`) must match. |

For established (`MID_PROJECT_UNGOVERNED` / `MIGRATION_GOVERNED`) projects, maintain both **As-Is Baseline Diagrams** (characterizing current reality) and **To-Be Target Diagrams** (defining authorized deltas).

## 5. Relative Standards Search Registry

Record all domain, protocol, security, architectural and UI standards discovered and bound via the **Relative Search Protocol** (`[Product Archetype + Domain Intent + Paradigm/Runtime + Risk Tier + Compatibility Boundary]`):
- **Tier 1 (Local Canon):** Project-specific contracts, schemas and historical decisions.
- **Tier 2 (Formal Standards):** IETF RFCs, W3C, ISO/IEC, NIST, OWASP, OpenAPI/AsyncAPI, JSON Schema.
- **Tier 3 (Platform Canon):** Apple HIG, language RFCs/PEPs, CNCF specifications.
- **Tier 4 (Empirical Reference):** Verified high-assurance open-source architectures.

For each bound standard, record: `Standard ID`, `Version`, `Applicable Scope`, `Enforced Invariants`, and `Verification Method`.

## 6. Shared presentation & Minimalist iOS / HIG UI Philosophy (when applicable)

For projects with a visual user interface (mark `N/A` with rationale for headless/CLI/library projects), enforce the **Minimalist iOS / Apple HIG Design Philosophy**:
- **Visual Deference & Spatial Clarity:** Content-first viewport; generous whitespace; subtle `0.5px`–`1px` hairline dividers (`rgba(255,255,255,0.10)` dark / `rgba(0,0,0,0.08)` light); zero visual clutter.
- **Translucent Layering & Concentric Radii:** Glassmorphic panels (`backdrop-filter: blur(20px) saturate(180%)`), subtle elevation shadows, and concentric border radii (`R_outer = R_inner + Padding`).
- **Typography & Data Density:** `SF Pro` / `Inter` / `system-ui` proportional hierarchy (`400`/`500`/`600` weights) paired with `SF Mono` / `JetBrains Mono` (`tabular-nums`) for technical/numeric precision.
- **Adaptive Semantic Palette:** True dark-mode (`#000000` / `#1C1C1E` / `#2C2C2E`) and crisp light-mode (`#F2F2F7` / `#FFFFFF`) surface tokens with a single high-legibility semantic accent tint and WCAG AA/AAA contrast.
- **Ergonomics & Spring Physics:** Direct canvas manipulation, progressive disclosure (`PRIMARY`, `SECONDARY`, `ON_DEMAND`), `>= 44x44pt` touch targets (`>= 28x28px` dense desktop controls), and interruptible critically-damped spring animations (`dampingRatio: 0.85–1.0`, `response: 0.3s`).

## 7. Delegated source map

For each delegated technical file (design tokens, diagram directory, OpenAPI specs, DB schemas, standards registry, test suites, evidence companion), record:
- `Path / Resource ID`, `Narrow Role`, `Owner`, `Version/Decision`, and `Supersession Rule`.

## 8. Roadmap, Tri-Agent workflow and completion criteria

Define bounded objectives, dependencies, capability IDs, required risk tiers (`R0`–`R3`), and mandatory `required_hard_gates`. Every consequential objective progresses through:
1. **Pre-Definition & Relative Search Check** (`SPEC_VERIFIED`),
2. **Diagram-First Authoring & Lock** (`DIAGRAM_LOCKED`),
3. **Worker Implementation & Evidence Generation** (`CANDIDATE_COMPLETE`),
4. **Independent Reviewer Audit** (`REVIEW_PASS`),
5. **Distinct Acceptor Verification & State Promotion** (`ACCEPTED_BOUNDED`).


## 8A. Autonomous execution contract — bind per project

For each objective, define its stable ID, predecessor IDs, priority, risk, scope ownership, permitted autonomous decisions, reserved actions, source-of-truth contract/diagram refs, acceptance and negative evidence, tool/data/secret boundary, time/retry/spend budget, stop and reconciliation policy. The scheduler may propose further objectives based on witnessed gaps, but no proposal becomes permission to change product goals, live data, cost ceilings, governance promotion or deployment. Assign accountable Worker, independent read-only Reviewer, distinct Acceptor, no-write Router and independent Watchdog. Bind the actual trusted project runtime and scheduled trigger; the universal package cannot supply these credentials or isolation. Discovery must prefer the existing owner's backlog, and unknown intent invokes a CRP rather than inventing features. Preserve source knowledge and results after each session so a new agent can resume from `PROJECT_STATE.yaml` and the versioned evidence.

Autonomous engineering completion means verified specifications, code/diagram alignment, negative/recovery tests, independent code review, bounded technical acceptance, and persistent state update. It does **not** imply production release or permission to perform externally consequential actions. Governance OS self-evolution uses a separate `GOVERNANCE` class mandate with stronger independent validation and no silent cutover.

## 9. Post-launch outcomes and capability lifecycle (when applicable)

Define intended user/task outcomes, privacy-safe observation boundaries, and lifecycle rules separating UI visibility (`PRIMARY`, `SECONDARY`, `ON_DEMAND`) from service availability (`ACTIVE`, `SUSPENDED`, `RETIRED`).

## 10. Update rule

Update `PROJECT_DIRECTION.md` only when intent, architecture, diagrams, standards, capability contracts or roadmap change. Revalidate affected consumers and mark stale evidence in `PROJECT_STATE.yaml`.


## 11. DeepSeek Super-Agent binding (delegated technical specifications, not another authority)

Define the authorized Router input channels and deterministic Fast-Path classifications, Slow-Path escalation conditions, exact absence of shell/file-mutation/deployment permissions, event retention limits and CRP-only default notification contract. Define Worker/Reviewer/Acceptor subprocess identities, independent evidence access, serialized state writer, `subject_scope` leasing and candidate-bound mandate format. Define Watchdog heartbeat intervals, stall/retry/budget thresholds, cancellation/fencing, safe recovery versus human-reserved escalation and ambiguous-effect reconciliation. All must be backed by real runtime/tool restrictions rather than a model's self-attestation.

The diagrams for this system live in a delegated technical directory **outside `governance/`**, selected at adoption. At minimum its runtime contract needs a Router sequence diagram, Watchdog recovery statechart, Worker→Reviewer→Acceptor handoff sequence, subject-lock statechart and cross-boundary trust-flow diagram where relevant. `PROJECT_STATE.yaml` holds only live refs/identities, never a parallel status registry.

## 12. Authoritative pre-code handoff

An individual capability's six specification dimensions must be referenced by `specification_gate.dimension_refs` (`intent_actors`, `data_interfaces`, `paradigm_boundaries`, `diagrams`, `relative_standards`, `acceptance_negative`). The distinct qualified Reviewer signs a scoped `diagram_approval_ref`; `diagram_lock_subject_digest` and `diagram_refs` bind the reviewed diagram design to the Worker task. A project-bound trusted pre-code adapter must verify those refs, actual files, ownership, intended scope, approved diagram version, and actual immutable candidate identity before granting filesystem write permission. On changed requirements/diagrams, return to review rather than keep a stale lock.

## r1 specification scope binding

For each capability, record the intended `subject_scope_ref`, the exact scope of As-Is / To-Be diagrams, and each applicable approval receipt. A task changing a different scope needs its own verified gate and diagram approval even if the larger candidate's SHA-256 digest is unchanged.
