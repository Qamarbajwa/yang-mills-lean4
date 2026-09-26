# Delegated evidence and migration contract

This file is a technical companion to the active governance, not a fourth project-level operational authority. Read it when implementing or validating evidence, state transitions, migration or cutover.

## Evidence dimensions

Evidence strength:

- `E1` — static inspection, schema, lint, type or configuration evidence.
- `E2` — automated behavioral evidence such as unit, integration or regression tests.
- `E3` — reproducible execution bound to an exact candidate, environment and relevant inputs/outputs.
- `E4` — qualified independent verification or reproduction.
- `E5` — externally anchored or tamper-resistant evidence where applicable.

Self-report alone is `ASSERTION`, not verification. Evidence level is never sufficient by itself; record scope, candidate, environment, method, independence, result and limitations.

Independence:

- `IND0` — writer/same task context; not independent.
- `IND1` — limited separation/fresh context; useful for bounded low-risk review only when project policy permits.
- `IND2` — distinct qualified verifier task/process with sufficient separation from authorship; default minimum for R2 and required independent paths unless strengthened.
- `IND3` — materially independent external verification; required only when bound project/domain policy demands it.

A role label or model/provider difference is not independence evidence. Governance/control/R3 paths use the role matrix in GOVERNANCE.md: writer, reviewer and final acceptor are distinct where required. R1/R2 reviewer+acceptor combination is permitted only when the project binding explicitly allows it and the acceptor is not the writer.

Environment classes may include `STATIC`, `MOCK`, `FIXTURE`, `ISOLATED_SYNTHETIC`, `INTEGRATED_LOCAL`, `REPRESENTATIVE`, `SANDBOX`, `STAGING`, `LIVE_LOCAL`, `PRODUCTION_OBSERVED` or another explicitly defined project class. Never treat environment classes as interchangeable.

## Evidence receipt minimum

A consequential evidence receipt should identify, where applicable:

- receipt ID;
- evidence scheme version;
- contract/capability and exact scope;
- candidate digest or immutable identity;
- relevant dependency/configuration/environment identity;
- command/tool/method;
- timestamp;
- result/exit code;
- producer role/task;
- independence level and provenance limits;
- artifact/evidence reference and digest;
- supported claim;
- explicit limitations.

Use `UNKNOWN` or null honestly when information is unavailable. Missing required information blocks the stronger claim rather than being invented.

Independent review records should identify writer, reviewer, observed candidate, reproduced evidence, mutation constraints, findings, verdict and remaining deviations. Acceptance records should identify the qualified acceptor, matching candidate, matching review/evidence and exact bounded outcome. Failed evidence is preserved; later success does not rewrite it.

## Stochastic / agent-behavior evidence

When the product or development agent can legitimately vary across runs, do not require identical reasoning, text or implementation shape unless the contract explicitly requires it. Bind evidence to invariant outcomes, permissions, forbidden effects, statistical/quality thresholds and sample/repetition method proportional to risk. Record sample count/seed/model/provider/configuration when relevant and available. One favorable run cannot support a stronger reliability claim.

## Governance-change improvement record

A governance candidate should record: demonstrated failures, emerging risks, obligations or measurable opportunities addressed; smallest control added/changed; expected decision difference; previous accepted baseline; effectiveness scenarios; anti-bloat results; active-authority count; owner-interruption impact; duplicated-state/source check; portability check; independent review status; and promotion/rejection decision. A candidate that adds wording but produces no testable control improvement should not be promoted.

## Exact live-effect boundary and validation limits (r3)

`validateReleaseState` is **structural only**, with fail-closed local hard-gate/blocker and future-date checks. A `hard_gates` entry in bound state is a declaration, not authenticated evidence: `PASS` requires nonempty evidence references and the exact frozen subject digest; `NOT_APPLICABLE` requires a reason. Required-gate inventory, actual evidence, applicable review, dependencies and remote blockers must be resolved by the bound `validateBoundReleaseReadiness` adapter. Without a trusted adapter or exact matching receipt the answer is NO-GO. Local receipt shape cannot authenticate the adapter.

`validateLiveDeploymentAuthorization` is retained as a fail-closed preflight compatibility entry; it always denies live-effect permission. Project adapters use `executeAuthorizedDeployment` or a separately reviewed equivalent real effect path. The request must include the actual artifact digest as well as candidate, environment, scope and action. The trusted `authorizeAndExecute` implementation must verify actual immutable artifact bytes **at the effect boundary**, validate authoritative grant freshness and revocation with trusted time, atomically consume one-shot grants while applying an idempotent/fenced effect, and durably record a receipt. A promise, fixture receipt or arbitrary callback does **not** prove those properties. Interrupted/ambiguous effects require reconciliation before retry, rather than issuing a second effect against an uncertain grant.

Trusted classifier/agent identity and reviewer independence, publisher authenticity, production atomicity and actual product/lifecycle performance remain project-bound evidence. Do not equate a passed test stub with independently demonstrated real-world enforcement.

## State, release and validator contract

The source distribution uses JSON-compatible YAML 1.2 for PROJECT_STATE.yaml so the dependency-free package checker can parse it strictly and reject duplicate keys. A bound project may use full YAML only when its project validator parses YAML with duplicate-key rejection and enforces the same semantics.

Current release eligibility is authoritative only for the exact candidate/environment/scope recorded under `release.eligibility`. `RELEASE_ELIGIBLE` requires a frozen candidate identity, matching candidate reference, environment/scope, evidence and a decision/freshness record. `NO-GO` grants no release permission. Deployment authorization is a separate grant and, while `AUTHORIZED`, must match the current eligible candidate/environment/scope and identify the authorized action, grant and freshness/expiry condition; `NONE`, `REVOKED`, `EXPIRED` and `CONSUMED` grant no new action. Historical deployment observations are append-only evidence and may remain present while current eligibility is NO-GO.

`candidate_identity.subject_ref/digest/scope` identifies the frozen consequential subject set. State revisions, review receipts and acceptance receipts are recorded separately and do not recursively change that subject identity unless the bound candidate scope explicitly includes them.

Where the project uses machine-readable governance/evidence, the real project validator should reject, as applicable:

- missing or dangling required evidence;
- malformed candidate/environment identity;
- unknown evidence schemes;
- invalid status transitions;
- stale candidate or state revision;
- writer self-acceptance when independence is required;
- unmet dependencies;
- failed required review;
- unknown or failed required hard gates;
- release promotion without all required gates or with inconsistent candidate/environment/scope;
- evidence references outside declared safe roots;
- acceptance of a consequential defect repair without required regression protection or documented inapplicability;
- execution beyond a bound tool/destination/retry/concurrency/time/spend envelope when such an envelope is required, counting aggregate work across retries, children and restarts.

Negative tests are required for consequential validator behavior. The role helper requires an explicit supported change class supplied by a trusted project-bound classifier; untrusted agent omission or self-classification cannot downgrade a consequential change. A shape/schema checker cannot prove truthful execution, reviewer qualification, permission, visual fidelity or real-environment behavior; `validateReleaseState` is shape/consistency validation and MUST NOT be used as a live grant. `validateLiveDeploymentAuthorization` is a fail-closed interface requiring a trusted, project-bound time and independent live grant/freshness/revocation/consumption checks. Boolean attestations from an untrusted requester are not authority. An adopting project must bind and test these checks against authoritative runtime systems before any live action. The adopter must authenticate the grant authority and trusted clock, compare exact frozen artifact bytes/digest plus environment/scope/action at the effect boundary, enforce expiry and revocation, atomically consume one-shot grants (including races/retries/replays), and test every external-effect path. A syntactically valid `valid:true` stub or non-atomic preflight receipt is NOT permission. UNBOUND, STAGED and INACTIVE may retain history but cannot assert current eligibility or AUTHORIZED.

## Post-launch and lifecycle decision evidence

Use existing capability IDs, state/evidence receipts and delegated data rather than another active lifecycle register. For consequential changes record: object type (rule, technical constraint, UI visibility, availability, service or entire product); before/after status; problem and intended outcome; observed signal and its cohort/window/limitations or absence of observations; protected obligations and dependent consumers; authorization and notice where required; data/security/quality and restoration or migration plan; exact candidate/environment; verification, rollback, outcome review and unresolved risks. A UI demotion does not imply service shutdown; retirement needs data retention/export and contractual review where applicable. An on-demand entry must not falsely advertise unverified or suspended availability. Source and current capability status live in the existing State/delegated records; `lifecycle_review_refs` is a non-authoritative index of decision/evidence references, not a second status registry. Do not generate per-change paperwork for harmless presentation adjustments or require quantified thresholds where no credible measurement exists.

## Migration acceptance record

For an existing project migration, record:

- source package identity/hash;
- prior active governance binding, if any;
- exact files/surfaces owned by the migration;
- pre-change fingerprints required for rollback;
- new project-specific candidate fingerprint;
- target-project adaptations;
- stronger inherited restrictions preserved;
- delegated-source mapping;
- state/risk/evidence mapping where semantics differ;
- continuity of failures and negative history;
- required tests and actual results;
- review/acceptance references;
- cutover steps;
- post-cutover active identity;
- rollback/recovery procedure and result.

Do not numerically reinterpret an older evidence or risk label without inspecting what it actually meant. Preserve historical labels in historical evidence and derive current classification from actual consequences and proof.

Before cutover, re-read both the live state revision and migration-owned file identities under the project's serialization/concurrency method. Drift blocks cutover until reconciled. Any consequential source change after a PASS invalidates affected review/evidence and requires re-verification.

## Minimum adoption tests

Each adopting project should verify, where applicable:

1. An unbound template cannot authorize product work or deployment.
2. Existing failed/unknown gates and release blockers survive migration.
3. Evidence for one candidate cannot authorize a changed candidate.
4. Required independent review cannot be replaced by writer self-acceptance.
5. A stale state update cannot overwrite a newer accepted state.
6. Fixture/mock evidence cannot certify a stronger real-environment claim.
7. Required delegated technical specifications remain reachable after cutover.
8. Archive/history is not treated as current operational instruction.
9. Recovery preserves unrelated work and required historical provenance.
10. Autonomous next-objective selection respects dependencies and reserved actions.
11. Governance adoption grants neither product completion nor deployment permission.
12. A required UI/backend/role/responsive/accessibility/failure dimension without sufficient evidence prevents capability completion.
13. A verified stable component is not rewritten solely because a new agent prefers another framework/style.
14. A consequential refactor first characterizes current behavior, affected consumers and regression baseline.
15. A controlled consequential failure is diagnosable to operation/candidate/failure class and resulting state without secret leakage.
16. A capability with material concurrency/load/endurance risk cannot mark that concern N/A without rationale and relevant evidence.
17. A cross-agent handoff cannot override a newer repository/state candidate; the receiver rebinds before acting.
18. Repeated provider/tool failure respects bound retry/spend/concurrency/stop limits where applicable.
19. Instruction-like text from untrusted content cannot expand authority, tools, spend, mutation scope or deployment.
20. Consequential acceptance distinguishes contract conformance from intent fidelity.
21. Two different valid AI implementation paths are judged by the same contracts/invariants/evidence rather than textual similarity.
22. Secret-bearing source/log/evidence output blocks acceptance; suspected prior exposure remains an incident until authorized revocation/rotation/invalidation or an explicit unresolved-remediation record establishes the remaining risk. Moving an exposed secret to secret management alone is not containment.
23. A repaired consequential defect has durable regression protection or an explicit technically valid inapplicability record.
24. Governance improvement preserves the three active authorities, introduces no duplicated live state, and does not increase routine owner interruption without reserved-authority need.
25. No security/quality sign-off is inferred solely from a scanner reporting no findings, high KPI or owner confidence; evidence and applicable hard gates remain necessary.
26. A redundant procedural constraint is not automatically permanent, but a rarely triggered security requirement cannot be retired solely for lack of recent findings.
27. Low-use optional function may move to discoverable on-demand UI without deleting data, overriding pins, or declaring suspended functionality available. Essential/recovery/legally required access remains reachable.
28. A restored dormant function cannot be marked AVAILABLE merely because archived code exists; compatibility, authorization and relevant security/quality evidence must be current.
29. Post-launch claimed improvement refers to actual outcome measurement with affected cohorts/limitations, not mere implementation or visibility change.
30. Historical deployment observation, current release eligibility and permission for a new live action remain independent after operational change.
