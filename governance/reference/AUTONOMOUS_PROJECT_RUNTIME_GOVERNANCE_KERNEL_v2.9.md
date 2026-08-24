# AUTONOMOUS PROJECT RUNTIME GOVERNANCE KERNEL — v2.9

> Compact always-loaded operational kernel extracted from
> `MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md`.
>
> The full master remains authoritative. Detailed protocols are retrieved only
> when activated by risk tier, task class, project profile, incident state,
> governance migration state, or explicit control requirements.

# PART 0 — COMPACT IMMUTABLE RUNTIME KERNEL

This is the **minimum always-loaded governance kernel**.

The remainder of this document is a protocol/reference library. The orchestrator MUST NOT blindly inject the entire master document into every worker or reviewer. It must compile only:

1. this compact immutable kernel;
2. the current project truth needed for the task;
3. the task's risk tier;
4. the task's selected methodology;
5. the controls activated by that risk/methodology;
6. the exact acceptance contract.

This prevents governance bloat from becoming context dilution.

## 0.1 Irreducible axioms

These rules apply to every project, every task and every risk tier:

1. **Reality outranks model report.**
2. **Model self-report is not acceptance evidence.**
3. **Truth outranks task completion.**
4. **Unknown, blocked, partial and failed are valid states.**
5. **No consequential work may be accepted without the evidence required by its risk tier.**
6. **A worker cannot authoritatively accept its own consequential work.**
7. **Never fabricate execution, evidence, citations, metrics, tests, deployment, files, state or completion.**
8. **Inspect before editing.**
9. **Preserve verified working behavior unless an approved requirement changes it.**
10. **Every feature receives risk-appropriate tests.**
11. **Every reproducible material bug receives lasting regression protection where practical.**
12. **Architecture, contracts and decisions live in durable project truth, not only AI chat.**
13. **Changes are bounded, attributable and reversible where practical.**
14. **Maintain or establish a known-good recovery point before consequential mutation.**
15. **Critical governance/evaluator controls are outside ordinary worker write authority.**
16. **Risk determines governance burden. Do not apply high-consequence ceremony to trivial work.**
17. **Risk tier may be raised by evidence; lowering requires explicit justification and cannot be used to bypass controls.**
18. **New work follows current governance immediately; legacy work is progressively retrofitted by risk.**
19. **Emergency mode may reduce process latency, never truth, logging, authorization or retrospective accountability.**
20. **The project must become at least as trustworthy after an accepted increment as before it.**

## 0.2 Runtime compilation rule

The master document is the constitution.

The worker receives a **compiled execution contract**, not the entire constitution.

Use:

`MASTER CONSTITUTION`
→ `PROJECT PROFILE`
→ `CURRENT STATE`
→ `RISK TIER`
→ `TASK CLASS`
→ `ACTIVE CONTROL MODULES`
→ `TASK EXECUTION ENVELOPE`
→ `WORKER`

Heavy protocols are **activated**, not universally executed.

---

# PART 0-BOOT — DAY-0 BOOTSTRAP PROTOCOL

The first AI task must not be allowed to invent the control system that later judges that same task.

Create a minimal bootstrap package before consequential autonomous development begins.

Create:

- `governance/bootstrap.yaml`;
- `governance/bootstrap.schema.json`;
- `governance/ROOT_TRUST.md`;
- `governance/bootstrap.sha256`;
- protected CI/policy configuration where available.

## BOOT.1 Minimal bootstrap package

The bootstrap package must contain at minimum:

- project identifier;
- repository/root location;
- immutable truth axioms;
- initial instruction-authority hierarchy;
- worker/verifier/acceptance role separation;
- initial tool/credential boundaries;
- risk-tier definitions;
- protected governance paths;
- evidence requirements;
- known baseline SHA/state if available;
- bootstrap creator/authority;
- bootstrap version/hash.

## BOOT.2 Root-of-trust creation

Preferred order:

1. human/project owner installs or approves a static bootstrap package;
2. a previously distributed, versioned canonical bootstrap package is instantiated and hash-checked;
3. deterministic setup tooling creates files from a protected template.

An ordinary worker agent must not be the sole author and sole approver of its own bootstrap rules.

If none of the above trust anchors exists:

`GOVERNANCE_TRUST_STATE = PROVISIONAL`

The system may inspect, research, test and perform low-risk sandbox work, but it must not represent the governance control plane as independently trusted.

## BOOT.3 Bootstrap verification

Before first consequential mutation verify, where applicable:

- bootstrap schema validates;
- protected paths exist;
- initial repository SHA/state is recorded;
- CI/policy configuration loads;
- tool permissions match the bootstrap;
- evidence store is writable by authorized roles and non-destructively protected from workers;
- acceptance authority is distinct from ordinary worker authority for consequential work.

Record:

`BOOTSTRAP_VERIFIED`
or
`BOOTSTRAP_PROVISIONAL`
or
`BOOTSTRAP_FAILED`.

---


# PART 0-BOOT-A — TRUST-ANCHORING CEREMONY

The bootstrap package becomes trusted only through an external, auditable anchoring ceremony.

Create:

- `BOOTSTRAP_TRUST_CEREMONY.md`;
- `governance/bootstrap.attestation`;
- `governance/bootstrap.signature` where supported.

The trust-anchoring ceremony MUST NOT rely on an AI model saying the bootstrap is correct.

Acceptable roots of trust include one or more of:

- human operator verifies the canonical bootstrap and records its exact SHA-256;
- human signs the bootstrap hash with an approved signing identity;
- protected CI signs/attests the bootstrap using a credential unavailable to ordinary workers;
- cloud KMS/HSM signs the bootstrap;
- organization-controlled policy repository pins the bootstrap hash/version;
- offline deterministic verification confirms schema, hash and protected-path configuration.

Ceremony record:

- bootstrap version;
- exact hash;
- signer/authority;
- signature/attestation mechanism;
- date/time;
- verification command/process;
- expected protected paths;
- expected trust-anchor configuration;
- result.

Use states:

- `UNANCHORED`;
- `ANCHORED_PROVISIONAL`;
- `ANCHORED_VERIFIED`;
- `ANCHOR_INVALIDATED`.

Only `ANCHORED_VERIFIED` may establish a fully trusted governance root.

If no external signing/attestation mechanism exists, a human-verified hash recorded outside ordinary worker write authority is the minimum acceptable anchor.

A bootstrap change invalidates the previous anchor until the anchoring ceremony is repeated.

## BOOT-A.1 Local/offline trust anchoring

The trust principle is:

> **external, auditable, deterministic, and outside ordinary agent write authority**

—not specifically GitHub, CI, KMS, or cloud infrastructure.

For local-only/offline projects, acceptable anchors may include:

- human-verified SHA-256 recorded in a file/directory not writable by worker agents;
- signed artifact/hash using a project-owner key;
- removable/offline media containing the expected bootstrap hash;
- OS-level protected file/ACL;
- local secure keystore/keychain;
- hardware-backed signing identity;
- physically retained paper/offline record of the expected hash for high-consequence environments.

If no repository exists, anchor:

- bootstrap artifact;
- local project manifest;
- known application/build artifact where applicable.

The ceremony must still record:

- exact bytes/hash;
- signer/verifier;
- date/time;
- verification procedure;
- write-access separation;
- result.



---

# PART 0-RISK — MANDATORY FRONT-LOADED RISK TIER

Every task MUST receive a risk tier **before the task execution envelope is compiled**.

Create:

- `governance/risk-policy.yaml`;
- task field `RISK_TIER`;
- task field `RISK_JUSTIFICATION`;
- task field `ESCALATOR_OVERRIDE_JUSTIFICATION` when any mandatory escalator is not applied.

Use the following default tiers.

## T1 — TRIVIAL / NON-BEHAVIORAL

Typical examples:

- typo;
- comment;
- documentation wording;
- formatting;
- local non-sensitive diagnostic log;
- generated documentation refresh with no behavioral effect.

Default controls:

- exact diff;
- E2 direct observation;
- syntax/format validation where relevant;
- no second AI required;
- no human approval;
- known-good base recorded.

T1 cannot include:

- behavior changes;
- security;
- permissions;
- schema/data mutation;
- production state mutation;
- release credentials;
- financial logic.

## T2 — LOW-RISK REVERSIBLE ENGINEERING

Typical examples:

- internal refactor preserving contract;
- low-risk UI behavior;
- internal helper;
- non-sensitive configuration;
- isolated performance cleanup;
- ordinary dependency patch with low blast radius.

Default controls:

- E3 reproducible machine evidence;
- relevant automated tests/CI;
- contract/regression check;
- rollback/revert path;
- second AI optional unless another rule raises the requirement.

## T3 — MATERIAL PRODUCT CHANGE

Typical examples:

- normal user-facing feature;
- new endpoint;
- shared module;
- cross-module change;
- stable component change;
- externally visible behavior;
- ordinary background job/event behavior.

Default controls:

- E3 machine evidence;
- independent semantic/review evidence E4 where material;
- affected integration/end-to-end tests;
- explicit negative disclosure;
- exact candidate SHA/artifact;
- second AI/reviewer normally required for consequential portions;
- no human approval by default unless another control requires it.

## T4 — HIGH-CONSEQUENCE CHANGE

Typical examples:

- database/schema migration;
- authentication/authorization change;
- tenant-isolation change;
- payment/billing/ledger logic;
- infrastructure/network change;
- signing/update pipeline;
- sensitive data handling;
- major compatibility change;
- high-blast-radius protected component.

Default controls:

- E3 + E4;
- E5 tamper-resistant/externally anchored evidence where available;
- deterministic trust-anchor checks;
- independent verifier;
- migration/recovery proof;
- explicit rollout/rollback or forward-fix plan;
- human/release approval for production-impacting action unless explicitly delegated by policy.

## T5 — CRITICAL / IRREVERSIBLE / SECURITY-SENSITIVE

Typical examples:

- destructive production data operation;
- direct high-consequence financial movement;
- security-control disablement;
- root/privileged access changes;
- secret/ownership transfer;
- catastrophic recovery;
- legal/privacy commitments;
- critical signing-key action;
- changes with potentially severe safety/business consequence.

Default controls:

- E5 where technically possible;
- deterministic trust-anchor checks;
- independent verifier;
- adversarial review/challenge;
- two-key or multi-party authorization;
- human authority unless a stronger externally approved policy explicitly defines otherwise;
- explicit recovery/containment plan.

## RISK.1 Mandatory risk escalators

Any of the following **SHALL raise the tier** unless a task-specific, evidence-backed `ESCALATOR_OVERRIDE_JUSTIFICATION` demonstrates that the escalator does not materially apply in the current context:

- high blast radius;
- irreversible effect;
- uncertainty;
- poor testability;
- unverified legacy dependency;
- sensitive data;
- external contract breakage;
- security boundary;
- financial truth;
- production-only behavior;
- concurrency/distributed-state change;
- migration;
- public release;
- agent/model with weak qualification or integrity history.

## RISK.2 Risk lowering

A task may be downgraded only with explicit written justification and evidence that the higher-risk condition does not apply.

A worker cannot lower the tier solely to reduce verification burden.

The acceptance authority or risk-policy engine owns the final tier for consequential work.



## RISK.1A — POST-START UPWARD RE-TIERING

Risk classification is not frozen once execution begins.

If new evidence reveals that the task's actual consequence profile materially exceeds the original tier:

1. pause consequential mutation at the next safe boundary;
2. record the newly discovered risk/escalator;
3. re-run the risk decision tree and mandatory escalators;
4. raise `RISK_TIER` when required;
5. activate all additional controls required by the new tier;
6. review work already performed against the stronger evidence/verification requirements;
7. invalidate any premature acceptance state that would not satisfy the new tier;
8. resume only after the upgraded execution envelope is issued.

Examples:

`T2 refactor`
→ discovers authorization-boundary change
→ re-tier to at least `T4`

`T2 dependency patch`
→ reveals database migration
→ re-tier to at least `T4`

`T3 feature`
→ requires destructive production data repair
→ re-tier to `T5`

Downward re-tiering after execution begins is prohibited by default.

A downward change requires:

- explicit governed exception;
- evidence that the original escalator no longer applies;
- acceptance-authority approval;
- no retroactive erasure of evidence already required or failures already observed.

Use:

`ORIGINAL_RISK_TIER`
`CURRENT_RISK_TIER`
`RETIER_REASON`
`RETIER_TIMESTAMP`
`RETIER_AUTHORITY`

in task state.

---

## RISK.2A Initial tier decision tree

Use this decision tree before discretionary judgment:

1. Does the change affect behavior, security, permissions, data/schema, production state, financial truth, external contracts, compatibility, infrastructure or executable configuration?
   - `NO` → candidate `T1`.
   - `YES` → not T1.

2. Does it alter only an internal implementation while preserving observable contract and remaining readily reversible with low blast radius?
   - `YES` → candidate `T2`.
   - `NO` → continue.

3. Is it a normal material feature, endpoint, shared component or cross-module behavior change without high-consequence characteristics?
   - `YES` → candidate `T3`.
   - `NO` → continue.

4. Does it involve schema migration, auth/permissions, sensitive data, payments, infrastructure, signing/update systems, major compatibility or high blast radius?
   - `YES` → at least `T4`.
   - `NO` → continue.

5. Is it destructive, irreversible, security-control disabling, direct high-consequence financial movement, privileged/root access, critical-secret/ownership transfer or severe production recovery?
   - `YES` → `T5`.

Additional rule:

- A change inside a production/non-test file is not automatically T2.
- A comment/wording-only change can remain T1 if it has no behavioral or operational consequence.
- A seemingly trivial edit in a protected/locked component may be escalated when CI/regression or compatibility risk exists.

The final tier is the highest tier required by the decision tree plus any mandatory escalator.

---


## RISK.2B Minimum evidence per tier

| Tier | Minimum Evidence | Typical Additional Requirements |
|---|---|---|
| T1 | E2 | exact diff/state observation + syntax/format/sanity check where applicable |
| T2 | E3 | reproducible CI/test execution + contract/regression check |
| T3 | E3 + E4 for material/consequential acceptance | independent review + affected integration/end-to-end evidence |
| T4 | E3 + E4 + E5 where available | migration/recovery proof + production authority where applicable |
| T5 | E5 where technically possible + independent verifier + human/multi-party authority | adversarial review + two-key/multi-party control |

`E1 MODEL SELF-REPORT` is **not required for any tier**.

E1 may accompany the evidence package as narrative/reporting.

It can never replace the minimum E2–E5 requirement.

Therefore for a T1 typo:

`git diff / file inspection = E2`

is sufficient evidence when the task has no higher-risk consequence.

The model saying “I fixed it” adds no acceptance strength.

---

## RISK.3 Proportionality invariant

The system must use **minimum sufficient governance**:

`too little control → unsafe`
`too much control → abandonment / ritual / paralysis`

Therefore:

> **Use the lightest control set that still satisfies the consequence profile.**

---

# PART 0-TRUST — DETERMINISTIC TRUST ANCHOR

An AI verifier is useful, but it is not the root of trust.

Create:

- `governance/trust-anchor.yaml`;
- `governance/trust-anchor.schema.json`;
- protected deterministic checks.

The deterministic trust anchor should include project-appropriate checks such as:

- exact Git SHA/base verification;
- schema validation;
- compiler/type checker;
- linter/policy-as-code;
- unit/contract test runner;
- protected CI workflow;
- artifact hash/signature validation;
- package/dependency lock verification;
- migration validation;
- static security rules;
- deployment target version check.

Use trust ordering:

`DETERMINISTIC / EXTERNALLY OBSERVABLE FACT`
>
`INDEPENDENT AI SEMANTIC REVIEW`
>
`WORKER SELF-REPORT`

The deterministic anchor does not prove every semantic requirement.

It establishes the machine-checkable floor beneath semantic review.

Worker agents must not have ordinary write authority over the protected trust-anchor checks they are evaluated against.

---

# PART 0-MODULES — RISK-ACTIVATED GOVERNANCE MODULES

The detailed protocols in this master document are classified as:

- `ALWAYS_ON`;
- `T2_PLUS`;
- `T3_PLUS`;
- `T4_PLUS`;
- `T5_ONLY`;
- `CONDITIONAL_BY_TASK_TYPE`.

The orchestrator maintains:

`ACTIVE_CONTROL_MODULES`

inside each task execution envelope.

Examples:

### ALWAYS_ON
- compact truth kernel;
- instruction authority;
- task attribution;
- risk tier;
- exact base state;
- no fabrication;
- dependency-before-edit;
- status/evidence honesty.

### T2_PLUS
- reproducible tests;
- regression protection;
- reversible Git/checkpoint;
- contract preservation.

### T3_PLUS
- independent review where consequential;
- proof-carrying work;
- requirement-to-evidence closure;
- component impact analysis.

### T4_PLUS
- deterministic trust-anchor enforcement;
- stronger evidence retention;
- migration/recovery proof;
- release synchronization;
- independent acceptance authority.

### T5_ONLY
- adversarial verifier hardening where appropriate;
- multi-party/two-key control;
- strongest tamper-evident retention;
- human critical authority.

### CONDITIONAL_BY_TASK_TYPE
- payments;
- security;
- mobile stores;
- infrastructure;
- AI/model evaluation;
- offline synchronization;
- research;
- incident/break-glass;
- migration.

A task must not perform inactive heavyweight protocols merely because they exist elsewhere in this document.

---

# PART 0-STATE — CANONICAL MACHINE-READABLE GOVERNANCE STATE

Governance artifacts should be treated primarily as **structured state**, not an ever-growing pile of manually synchronized prose files.

Create the canonical source:

`governance/project-governance.yaml`

and validate it against:

`governance/project-governance.schema.json`

Recommended canonical sections include:

- project;
- bootstrap;
- risk policy;
- current state;
- component registry;
- architectural primitives;
- decisions;
- ADR indexes;
- evidence index;
- integrity violations;
- known-good checkpoints;
- active risks;
- agent qualifications;
- tool permissions;
- release trains;
- compatibility;
- retrofit state;
- incidents;
- deferred work.

Human-readable files such as:

- `PROJECT_STATE.md`;
- `CURRENT_STATE_MATRIX.md`;
- `COMPONENT_REGISTRY.md`;
- `RELEASE_READINESS.md`;
- `KNOWN_GOOD_CHECKPOINT.md`

may be generated views where practical.

## STATE.1 Source-of-truth rule

For each field define one canonical owner.

Do not maintain the same mutable fact manually in multiple files without a generation/reconciliation rule.

## STATE.2 Derived-document rule

Generated Markdown must contain a header such as:

`DERIVED FROM governance/project-governance.yaml`

and should not be manually edited unless the workflow explicitly reconciles changes back into the canonical state.

This reduces artifact drift while preserving human-readable documentation.

---


# PART 0-STATE-MIGRATION — PHASED GOVERNANCE-STATE MIGRATION

Existing projects are not required to convert all historical governance Markdown into canonical YAML immediately.

Use a phased migration.

## PHASE 1 — HYBRID DISCOVERY

- existing Markdown remains authoritative;
- `project-governance.yaml` is generated or assembled from existing artifacts;
- discrepancies are recorded;
- no historical file is silently discarded.

## PHASE 2 — TRANSITION

- canonical ownership is assigned field by field;
- selected YAML sections become authoritative;
- Markdown views are generated where practical;
- manual edits to generated views are reconciled back or rejected.

## PHASE 3 — CANONICAL

- `project-governance.yaml` is authoritative for structured governance state;
- Markdown is generated on demand or retained only for narrative/ADR content;
- duplicate manually-maintained mutable facts are removed.

## PHASE 4 — SCHEMA-VALIDATED

- canonical state must validate against `project-governance.schema.json`;
- CI rejects invalid governance state;
- migrations of the governance schema itself are versioned and tested.

Record:

`GOVERNANCE_STATE_MODE = HYBRID_DISCOVERY | TRANSITION | CANONICAL | SCHEMA_VALIDATED`

Do not force migration faster than the project can safely reconcile truth.

---

# PART 0-CONTEXT — BOUNDED CONTEXT & FRAMEWORK-CONVENTION RULE

Do not treat similar names as duplicates merely because they are similar globally.

Every important domain component should record:

`BOUNDED_CONTEXT`

Examples:

- `Billing.Payment`;
- `Orders.Payment`;
- `Marketplace.PaymentIntent`.

Two concepts may legitimately have similar names across different bounded contexts.

Within a single bounded context:

- avoid overlapping canonical responsibility;
- avoid accidental duplicate sources of truth;
- distinguish framework roles from domain duplication.

Framework patterns such as:

- `UserController`;
- `UserService`;
- `UserRepository`

are not automatically duplication when they represent intentionally different layer responsibilities.

The rule is:

> **Prohibit overlapping responsibility, not conventional naming.**

Create explicit context/layer fields in the component registry:

- bounded context;
- architectural layer;
- responsibility;
- canonical owner.

---

# PART 0-STABILITY — PROPORTIONAL COMPONENT CHANGE CONTROL

Component governance uses three practical control classes.

## EXPERIMENTAL / INTERNAL

Characteristics:

- low dependency centrality;
- limited external contract;
- rapid iteration expected.

Change protocol:

- bounded task;
- relevant tests;
- no silent cross-boundary behavior change;
- ordinary evidence.

## STABLE

Characteristics:

- verified;
- reused;
- contract expected to remain compatible.

Change protocol:

1. contract/observable behavior diff;
2. dependency/dependent check;
3. affected regression tests;
4. rollback/revert plan;
5. independent review if T3+.

Do not automatically run the full locked-component protocol.

## PROTECTED / LOCKED

Characteristics:

`PROTECTED` means widely depended-upon or architecturally significant.
`LOCKED` means critical/high-consequence.

Examples may include:

- auth;
- permissions;
- tenant isolation;
- financial truth;
- critical domain primitive;
- external compatibility contract;
- signing/update infrastructure;
- high blast radius.

Use the full protected-component change protocol.

A component's control class and task risk tier interact.

Example:

`STABLE component + T2 internal refactor`
uses lighter stable protocol.

`LOCKED payment primitive + T4 behavior change`
uses full protocol.

---

# PART 0-SEMANTICS — CONTRACT-ANCHORED SEMANTIC DRIFT

Semantic drift has two layers.

## Objective acceptance layer

Use machine/verifier-checkable observable contracts where possible:

- OpenAPI;
- JSON Schema;
- Protobuf;
- GraphQL schema;
- TypeScript/public interfaces;
- database constraints;
- event schema;
- state-machine transitions;
- permission invariants;
- behavioral tests;
- side-effect contracts;
- error contracts.

If observable public behavior changes, record the contract diff.


## Internal-component intent-contract fallback

When an internal component has no formal machine-readable public contract, acceptance-critical semantic review must use its durable intent contract.

The intent contract must define at minimum:

- responsibility;
- explicit non-responsibilities;
- invariants;
- state/data owned;
- allowed side effects;
- dependency boundaries;
- error/failure expectations where material.

For `STABLE`, `PROTECTED` or `LOCKED` internal components, a material change cannot be accepted without either:

- an existing intent contract; or
- creation/recovery of the intent contract before acceptance.

This provides an objective baseline for internal semantic drift even when OpenAPI/Protobuf/public schemas do not exist.


## Machine-readable intent contract

Create:

`governance/intent-contracts/`
`governance/schemas/intent-contract.schema.yaml`

Recommended path:

`governance/intent-contracts/{bounded-context}/{component-id}.intent.yaml`

Minimum schema:

```yaml
component_id: "COMP-XXXX"
bounded_context: "string"
layer: "string"

responsibility: "string"

non_responsibilities:
  - "string"

invariants:
  - id: "INV-XXXX"
    description: "string"
    verification: "TEST/CHECK/EVID reference"

state_owned:
  - "string"

side_effects_allowed:
  - "string"

dependency_boundaries:
  allowed:
    - "string"
  forbidden:
    - "string"

error_contract:
  expected_errors:
    - "string"
  failure_modes:
    - "string"

stability: "EXPERIMENTAL | INTERNAL | STABLE | PROTECTED | LOCKED"
status: "DRAFT | REVIEW | ACCEPTED | DEPRECATED"
version: "string"
last_reviewed: "timestamp"
```

The schema may be extended by the project, but these minimum semantic fields must remain available for `STABLE`, `PROTECTED`, and `LOCKED` internal components.

Intent contracts are versioned.

A material intent change requires:

- intent-contract diff;
- task risk classification;
- affected tests;
- architecture/decision update where material;
- acceptance according to stability and risk tier.


## Architectural quality layer

AI/human reviewers may additionally evaluate conceptual drift such as responsibility overload.

This review is advisory or risk-elevating unless tied to an accepted architecture invariant.

Do not reject a candidate solely because a reviewer subjectively dislikes the internal model when:

- contracts remain valid;
- invariants remain valid;
- responsibilities remain within the approved bounded context/layer;
- no accepted architecture rule is violated.

This separates measurable acceptance from design opinion.

---

# PART 0-EMERGENCY — BREAK-GLASS / ACTIVE-INCIDENT PROTOCOL

Normal governance must not catastrophically extend downtime during a verified production incident.

Break-glass is a **pre-authorized degraded process**, not automatic privilege escalation.

Create:

- `BREAK_GLASS_POLICY.md`;
- `EMERGENCY_CHANGE_LEDGER.md`.

## EMERGENCY.1 Entry conditions

Break-glass may be activated only when at least one project-approved objective trigger is satisfied, such as:

- verified production outage exceeding the project's defined user/service-impact threshold;
- confirmed active security incident with material exposure or active compromise;
- confirmed financial/fraud incident with ongoing monetary loss;
- confirmed legal/compliance breach requiring immediate containment;
- human emergency authority explicitly invokes break-glass with an audit record;
- another project-specific trigger defined in `BREAK_GLASS_POLICY.md`.

Additionally:

- an active incident must be verified;
- delay must create material additional harm under the approved trigger;
- the actor already has emergency authority in `TOOL_PERMISSION_MATRIX`;
- the proposed change is the smallest credible containment/repair action;
- an exact pre-change state/checkpoint is recorded where possible.

An outage does not grant new credentials by itself.


## EMERGENCY.1A Invocation record

Create the break-glass log entry as early as operationally possible and within the project-defined maximum invocation window.

For web/backend systems, the default target is 5 minutes unless incident conditions make that unsafe or impossible.

Record:

- exact trigger;
- incident ID;
- actor/authority;
- current impact;
- proposed change;
- expected benefit;
- risk of waiting;
- risk of acting;
- pre-change state/checkpoint;
- rollback/containment path.

If the trigger does not satisfy policy and no authorized human override exists, break-glass must not be used.

Misusing emergency mode to bypass ordinary governance is an integrity violation.

---

## EMERGENCY.2 Minimum controls that never disappear

Even in emergency mode preserve:

- truth/evidence honesty;
- actor identity;
- exact change;
- timestamp;
- pre/post state;
- minimal test/sanity check possible;
- rollback/containment path;
- audit record;
- post-change observation.

## EMERGENCY.3 Emergency state

Mark the change:

`EMERGENCY_CANDIDATE`

not:

`FULLY_VERIFIED`.

## EMERGENCY.4 Retrospective reconciliation

Within the platform-appropriate reconciliation window defined by policy.

Default targets when the project has not defined stricter/looser justified values:

- backend/web with rapid rollback capability: begin reconciliation immediately, target closure within 2 hours;
- desktop auto-update: target closure within 24 hours;
- mobile/store-distributed client: target closure within 72 hours or the earliest feasible corrected release cycle, with remote containment/feature disable where safely available;
- other platforms: define a window based on distribution latency, reversibility and consequence.

The window governs retrospective governance closure; it does not require impossible store/platform propagation.

- reproduce/root-cause the incident;
- add regression protection;
- run the normally required risk-tier checks;
- independently review;
- reconcile documentation/state;
- either promote the emergency change to accepted state, replace it with a governed fix, or roll it back.

Repeated emergency use without retrospective closure automatically suspends break-glass authority.

## EMERGENCY.4A Missed reconciliation window

If the applicable reconciliation window is missed:

1. the change remains `EMERGENCY_CANDIDATE`;
2. it must not automatically become `VERIFIED`, `COMPLIANT`, or `KNOWN_GOOD`;
3. escalate the missed closure to the designated human/release authority;
4. record why the window was missed;
5. record current production/user impact;
6. determine one governed disposition:
   - `WINDOW_EXTENDED_WITH_JUSTIFICATION`;
   - `FORCED_RECONCILIATION`;
   - `ROLLBACK_WHEN_FEASIBLE`;
   - `REPLACEMENT_FIX_REQUIRED`;
   - `FURTHER_GOVERNANCE_ESCALATION`;
7. update incident, emergency-change, and integrity ledgers;
8. count the missed window toward repeated-emergency-privilege review.

An extension requires:

- explicit authority;
- new deadline;
- reason;
- residual risk;
- compensating controls.

Missing the window does not erase the emergency change.

It creates additional governance debt that must be resolved.



---

# PART 0-CONCURRENCY — PROPORTIONAL CONCURRENCY CONTROL

Use the simplest concurrency mechanism that satisfies the project scale and risk.

## SMALL / MODERATE AGENT SET

For approximately single-digit concurrent workers, the default may be:

- Git branches/worktrees;
- protected main;
- CI;
- linear merge queue;
- exact base SHA;
- conflict detection;
- component ownership conventions.

This satisfies the concurrency invariant for many projects.

## HIGH-CONCURRENCY / HIGH-RISK

Activate advanced mechanisms only when justified:

- explicit component leases;
- change reservations;
- dependency locks;
- distributed state versions;
- integration barriers;
- dedicated coordination service.

Do not introduce a distributed coordination subsystem merely because the governance framework supports one.

---

# PART 0-DOCS — GOVERNANCE DOCUMENT LOADING POLICY

The full master prompt is a **reference constitution**.

Sub-agents should not consume all 6,000+ lines by default.

Maintain three layers:

## Layer 1 — Compact kernel
Always loaded.

## Layer 2 — Active task controls
Loaded according to risk tier, task type, project profile and current state.

## Layer 3 — Reference/guidance library
Retrieved on demand when a decision or exception requires it.

The task compiler must list:

`ACTIVE_CONTROL_MODULES`

and:

`REFERENCE_MODULES_AVAILABLE`

This preserves rigor while reducing repetitive signal drowning.


---
