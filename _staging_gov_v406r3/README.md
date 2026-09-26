# Universal Governance Minimal v4.0.6-r3 — CANDIDATE

A project-neutral governance distribution for new projects, existing projects without governance, and existing governed projects.

## Project-neutrality rule

This package contains no target-project identity, repository path, port, provider choice, model assignment, capability ID, release status, historical project name, or project-specific implementation assumption. All target-project facts are discovered during adoption and written only into the target project's bound governance files or delegated technical sources.

Do not copy values from any unrelated project into a new adoption. Templates remain unbound until the target project is inspected and the adoption candidate is accepted.

## Active project authorities after adoption

Only these three files are project-level operational authorities:

- `governance/GOVERNANCE.md` — HOW the project operates.
- `governance/PROJECT_DIRECTION.md` — WHAT/WHY, capability contracts, architecture and intended roadmap.
- `governance/PROJECT_STATE.yaml` — current machine-readable operational state.

Other files in this distribution support adoption, evidence binding, migration, or package-integrity checking. They do not become competing project-level governance authorities.

## Adoption modes

The same package supports:

- `NEW_PROJECT`
- `MID_PROJECT_UNGOVERNED`
- `MIGRATION_GOVERNED`

The adopting agent must determine the actual mode from repository truth rather than from assumptions.

## Use

1. Preserve this distribution unchanged as the source package.
2. Stage adoption in a non-active location in the target project.
3. Run `node tools/verify-package.mjs` with Node.js 18+ to verify strict manifest/inventory integrity, unbound source-template semantics and a limited automated neutrality scan. The source PROJECT_STATE.yaml intentionally uses JSON-compatible YAML 1.2 so this check is dependency-free and duplicate-key strict. These checks do not prove publisher authenticity, target-project conformance, trustworthy time, live grant/revocation status or deployment permission.
4. Read `ADOPTION_PROMPT.md` and inspect the target project's actual repository, instructions, state, tests, evidence and release restrictions.
5. Populate the three project files from target-project truth. Do not copy sample or foreign project values.
6. Preserve stronger existing restrictions, failures, negative evidence and release blockers.
7. Perform required testing and independent review before cutover.
8. After accepted cutover, archive or deactivate superseded governance so only one current project-level governance set remains active.

## Candidate content and status

This further repaired candidate incorporates the standalone technical-acceptance amendment and repairs release/role/source-template validation found by adversarial review. It carries the unpromoted 4.0.5-r1 technical repairs and adds risk-proportionate security/quality outcome acceptance, lifecycle review of governing constraints, post-launch evidence-led evolution, and separate capability visibility/availability/retirement. The changes are not themselves acceptance or proof of real-world effectiveness.

Preserve reviewed source and prior candidate identities in external review receipts. This candidate is unpromoted until independent challenge of both inherited and new controls and separate acceptance; the previously approved project-level governance is not automatically replaced by the latest ZIP.

## Minimality rule

Do not create a new governance document merely because a new engineering concern is discovered. Prefer:

- a durable universal rule in `GOVERNANCE.md`;
- project-specific intent/architecture/contract information in `PROJECT_DIRECTION.md`;
- current status/evidence/blockers in `PROJECT_STATE.yaml`; or
- a narrowly delegated technical specification/test/evidence artifact where the information belongs technically.

## Archive rule

Historical governance is preserved for audit and provenance but is not active instruction. Archive material may be consulted only for history, migration, contradiction analysis, regression investigation or provenance.

## Limits

This package is not an enforcement service, reviewer, browser, scheduler, deployment system or proof of product correctness. The target project must connect its real tools, agents, validators and reviewers. Passing the package checker does not prove publisher authenticity, project conformance, product behavior, release eligibility, deployment safety, semantic project-neutrality beyond the limited automated patterns, or reviewer independence. Run `node tools/test-verify-package.mjs` to execute maintained positive/negative checker fixtures.

## v4.0.6-r3 targeted repairs

Strict nested unbound-source keys, activation/release consistency, closed change-class set, explicit-clock rejection and clean malformed-manifest failure are verified by maintained fixtures. Actual deployment-grant adapter security, real agent independence and post-launch behavior remain unproven by this package. The supplied role helper requires an explicit, recognized changeClass but validates strings, not authenticated identity or trusted classification. The R0/R1 reversible self-check path remains.

## r3 bounded executable contracts

`validateReleaseState` checks structural release consistency and declared gates/blockers but does not verify truth of evidence or completeness of project-specific gate policy. `validateBoundReleaseReadiness` requires a trusted project-bound adapter. `validateLiveDeploymentAuthorization` always fails closed as preflight-only; use `executeAuthorizedDeployment` with a trusted, atomic effect adapter, or an independently reviewed equivalent integration. Synthetic test adapters prove input/output validation only, not atomic storage, independent AI identities, publisher authenticity or production deployment safety. Reconcile uncertain effects before retry.
