# Universal bounded adoption prompt (v4.1.0-r3)

Use this prompt only after the owner has identified the target project and authorized governance adoption. The universal package itself remains unbound and project-neutral.

---

Apply Universal Governance Minimal 4.1.0-r3 to the target project as one bounded, reversible adoption candidate.

## 1. Repository Intake, Mode Detection & Product Archetype Classification

First inspect the actual project. Do not infer missing facts from this template:
1. **Determine Adoption Mode:**
   - `NEW_PROJECT` (Greenfield repository without existing implementation),
   - `MID_PROJECT_UNGOVERNED` (Established codebase with existing implementation but no formal governance),
   - `MIGRATION_GOVERNED` (Established codebase operating under an existing governance framework).
2. **Classify Product Archetype & Active Paradigms:**
   - Identify the exact product surface (`WEB_APP`, `MOBILE_IOS`, `DESKTOP_CAD_BIM`, `CLI_TOOL`, `API_SERVICE`, `DISTRIBUTED_SYSTEM`, `EMBEDDED_EDGE`, `DATA_ML_PIPELINE`, `AUTONOMOUS_AGENT_SWARM`, `LIBRARY_SDK`).
   - Identify the programming and architectural paradigms in use or intended (`FUNCTIONAL`, `OOP`, `PROCEDURAL`, `DECLARATIVE_UI`, `REACTIVE_STREAM`, `EVENT_DRIVEN`, `ACTOR_MODEL`, `DATA_ORIENTED`, `RELATIONAL_LOGIC`).
3. **Establish Repository Truth:**
   - Record repository/root identity, branch/HEAD or candidate digest, dirty state, current instructions, architecture, capability scope, existing diagrams, standards, tests, evidence, external systems, blockers, release state, reserved actions and available Tri-Agent (`Worker`, `Reviewer`, `Acceptor`) execution capability.

## 2. Non-Destructive Staging & Three-Authority Binding

Prepare the new three-authority candidate in non-active staging while preserving current project truth:
- Populate `governance/GOVERNANCE.md`, `governance/PROJECT_DIRECTION.md` and `governance/PROJECT_STATE.yaml` only from the target project's actual facts.
- Bind `EVIDENCE_AND_MIGRATION.md` in `governance_binding.evidence_companion_ref`, plus delegated paths for `standards_registry_ref`, `diagram_registry_ref`, and `ui_philosophy_ref`.
- Populate `required_hard_gates` in `PROJECT_STATE.yaml` with all mandatory release gates for the project.
- Preserve stronger existing safety, security, legal, financial, independent-review and release gates, as well as failures and `NO-GO` conditions.

## 3. Established (Brownfield) vs. New (Greenfield) Onboarding Rules

- **For `MID_PROJECT_UNGOVERNED` and `MIGRATION_GOVERNED` (Established Projects):**
  1. **Characterize-Before-Modify:** Do not rewrite working legacy subsystems for preference alone.
  2. **Reverse-Engineer As-Is Diagrams:** Inspect actual imports, call graphs, state stores and schemas to generate truthful **As-Is Diagrams** (`C4_CONTAINER`, `SEQUENCE`, `STATE_MACHINE`, `ERD_DATA`) before planning changes.
  3. **Identify Unspecified Legacy Modules:** Record undocumented legacy capabilities honestly as `PARTIAL` or `BLOCKED_MISSING_SPEC` rather than fabricating `VERIFIED` status.
- **For `NEW_PROJECT` (Greenfield Projects):**
  1. Lock project intent, product archetype, paradigm boundaries and UI philosophy in `PROJECT_DIRECTION.md` first.
  2. Execute the **Relative Search Protocol** to bind formal standards before designing custom schemas or protocols.
  3. Draw and lock foundational `C4_CONTEXT`, `C4_CONTAINER`, `STATE_MACHINE`, `ERD_DATA` and `UI_WIREFLOW` diagrams before scaffolding production code.

## 4. Pre-Defined Specification Gate & Missing-Part Protocol

Autonomous development requires **pre-defined specifications** (`specification_gate.status == "SPEC_VERIFIED"`). If any specification dimension is missing, ambiguous or contradictory:
- Immediately halt execution on that scope, set `specification_gate.status` to `BLOCKED_MISSING_SPEC`, record a `SPECIFICATION_MISSING` blocker, and either:
  1. Run the **Relative Search Protocol** (Tier 1 Local Canon -> Tier 2 Formal Standards IETF/ISO/W3C/NIST/OWASP -> Tier 3 Platform Canon Apple HIG/Language RFCs -> Tier 4 Reference Architectures) parameterized by `[Product Archetype + Domain Intent + Paradigm/Runtime + Risk Tier + Compatibility Boundary]` if the gap is a technical standard; or
  2. Ask the owner via a structured **Clarification Request Packet (CRP)** stating *(a) what is missing, (b) why it blocks deterministic implementation, and (c) 2–3 researched standardized options*.

## 5. Diagram-First Mandate & Minimalist iOS UI Philosophy

- **Diagram-First Execution:** Require intent-relative diagrams (`C4_CONTEXT`, `C4_CONTAINER`, `C4_COMPONENT`, `SEQUENCE`, `STATE_MACHINE`, `ACTIVITY_FLOW`, `ERD_DATA`, `DATA_FLOW`, `UI_WIREFLOW`) in `Mermaid`, `PlantUML`, `D2`, `Graphviz` or structured `ASCII` to be drawn and locked (`specification_gate.diagram_first_status == "DIAGRAM_LOCKED"`) *before* implementation code is written. All code must follow the approved diagrams 1:1.
- **Minimalist iOS / Apple HIG UI Philosophy (when UI applies):** Enforce content-first deference, generous negative space, `0.5px`–`1px` hairline dividers, translucent materials, concentric corner radii (`R_outer = R_inner + Padding`), crisp `SF Pro`/`Inter` + `SF Mono` (`tabular-nums`) typography, adaptive dark/light semantic tokens, `>= 44x44pt` touch targets, and interruptible spring-physics motion.

## 6. Tri-Agent Separation of Duties (Worker, Reviewer, Acceptor)

Bind and enforce the three distinct technical roles (and separately distinct Router and Watchdog IDs) in `coordination.active_role_assignment`. `THREE_ROLE` with `IND2`+ is mandatory for every risk tier; legacy `SELF_CHECKED`/`REVIEW_ACCEPT` is not an acceptance mode:
1. **WORKER (`worker_id`):** Verifies spec completeness -> executes Relative Search -> draws/updates diagrams first -> implements code & tests -> produces candidate digest & evidence receipts.
2. **REVIEWER (`reviewer_id != worker_id`, read-only):** Audits code against contract, owner intent, locked diagrams, bound standards, paradigm rules, Minimalist iOS UI philosophy, and negative/regression tests.
3. **ACCEPTOR (`acceptor_id != worker_id` and `!= reviewer_id`):** Verifies candidate digest, runs `node tools/verify-package.mjs` and project test suites, checks `required_hard_gates` completeness, records `ACCEPTED_BOUNDED`, and updates `PROJECT_STATE.yaml`.


## v4.1.0-r3 strict Super-Agent adoption rules

Discover the actual archetype/paradigms and classify Greenfield/Brownfield first. Record six capability specification dimensions and standards/diagram refs; prohibit source-folder scaffolding and production edits until a qualified distinct Reviewer has approved the intent-relative diagrams and the trusted project pre-code adapter allows the exact scope/revision. In established repositories, first characterize live source behavior and write As-Is diagrams and regression evidence, then approve To-Be delta diagrams; leave production unchanged until these gates clear. Record `LEGACY_UNSPECIFIED` where legacy subsystems lack contracts, without misrepresenting them as failures or silently refactoring.

Bind actual isolated Worker, Reviewer, Acceptor, resident Router, and separate scheduled Watchdog task/process identities. Router tools: **no** shell/file mutation/deployment/secret or live provider writes. Pass only scoped mandates through a trusted scheduler with real disjoint locks, bounded time/retries/spend and cancellation. Deploy/merge only after independent bounded acceptance and separately authorized action. Project-local files in `governance/` remain exactly the three operational authority entries; delegate diagrams and standards elsewhere. If the required runtime adapters/independent agents are missing, mark affected execution as pending or blocked, never fabricate successful work.

Before activating r3, migrate the active task's specification gate to record a genuine `subject_scope_ref` and independently approved diagram/standards receipts. Inventory and scope unresolved blockers; never silently mark a blocker resolved or reuse a lock for another task. Validate all Worker/Reviewer/Acceptor/Router/Watchdog identities in the actual runtime and establish the project-specific pre-code adapter and watchdog scheduler.

## Enable autonomous development (explicit project binding only)

1. Build a verified project inventory and classify Greenfield/Brownfield. Freeze a reversible governance adoption candidate and get distinct review/acceptance.
2. Bind `autonomy` with `mode=BOUNDED`, `enabled=true`, a trusted execution budget, runtime adapters, task/role identities, true scope leases, and CAS-protected state writes; activate only after project migration is accepted.
3. Populate dependency-safe `objectives` in the existing state authority. Preserve legacy failures and NO-GO. Enable a separate project scheduler to invoke `planAutonomousCycle` and, with trusted adapters, `executeAutonomousCycle`.
4. When requirements are technical, research and prepare automatically. When product intent, business/legal policy, or external exposure is missing, issue an owner CRP, without blocking unrelated fully specified work.
5. Do not represent this generic distribution as a long-lived agent runner, real independent review service, or permission to merge/deploy. Prove those integrations for the exact project.
