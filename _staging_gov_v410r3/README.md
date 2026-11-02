# Universal Governance Minimal v4.1.0-r3 — autonomous development candidate

**Status:** UNPROMOTED / NO AUTOMATIC ADOPTION. v4.1.0-r1 is the immediate repair baseline for this candidate; no change to the canonical governance authority is claimed.

This iteration adds an autonomous engineering lifecycle policy and an executable, dependency-free scheduler/dispatch interface. The package is project-neutral and retains exactly three project-level operational authorities inside `governance/`. Detailed runtime integration requirements live in the non-authoritative `AUTONOMY_RUNTIME.md`.

## Quick checks

```sh
node tools/verify-package.mjs
node tools/test-verify-package.mjs
node tools/test-autonomy-engine.mjs
node tools/autonomy-engine.mjs --plan
```

The final command reports `AUTONOMY_INACTIVE` for the unbound source template. Running this ZIP does **not** write production code, run a real AI model, merge branches or deploy anything. A connected project host with authenticated agents, limited scopes, scheduler and transactional state store is necessary for true unattended development.

## Safety, three authorities and evidence

The active entry authorities remain `governance/GOVERNANCE.md`, `governance/PROJECT_DIRECTION.md`, and `governance/PROJECT_STATE.yaml`. `AUTONOMY_RUNTIME.md`, this README, and the test/engine files are delegated supporting material, not additional authorities. All sample state is deliberately `UNBOUND` and in `NO-GO`. Verification proves package shape and limited synthetic engine behavior, **not** production isolation, agent qualification, intent fidelity, authenticated approvals, grant atomicity or deployment readiness.

## Model of autonomy

A trusted project-specific host maintains the event scheduler and executes isolated Router/Worker/Reviewer/Acceptor/Watchdog sessions. The engine derives a bounded next action, demands a trusted scope lease and actor authorization, checks frozen candidate scope and spec/diagram gates before code writes, validates exact phase receipts, and submits a CAS update request to the sole state writer. The owner is contacted only on actual reserved intent/business/legal/deployment decisions. Governance can propose and implement improvements to itself under an isolated candidate, but cannot self-promote.

## Handoff and review

Compare v4.1.0-r2 and v4.1.0-r3; run tests from a fresh ZIP; challenge `AUTONOMY_RUNTIME.md` boundaries and the synthetic mocks; then obtain distinct qualified review and acceptance before promoting. No project has been bound or migrated by creating this distribution.

## r3 adversarial fixes

The r3 candidate repairs active-autonomy role completeness (F1), post-diagram scope/digest mismatches and second-objective stale diagram locks (F2/F3), strict-role prose drift (F4), canonical six-dimensional contract alignment (F5), and consistent test fixture neutrality exemptions (F6). Switching to a new objective invalidates the old active scope lock; source mutation remains blocked until newly scoped specifications and diagrams are approved by a qualified independent Reviewer through the trusted project runtime. Test output is synthetic and does not establish actual runtime independence or safe deployment.
