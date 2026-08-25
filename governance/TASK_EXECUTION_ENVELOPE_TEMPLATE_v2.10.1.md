# TASK EXECUTION ENVELOPE — TEMPLATE v2.10.1

> The orchestrator fills this and sends it to a worker together with the Worker Micro-Kernel.
> One envelope = one bounded contract = one writer scope.
> Omit `NOT_APPLICABLE` sections for T1/T2 to keep envelopes proportional.

```yaml
envelope:
  id: <project>-<yyyymmdd>-<seq>            # e.g. talos-20260825-014
  issued_by: <orchestrator role/model id>
  governance:
    kernel_version: v2.10.1
    master_sha256: <sha of master constitution in force>
    bootstrap_level: LIGHT | STANDARD | HIGH_ASSURANCE

  project_binding:
    project: <name/id>
    root: <repo path / workspace>
    base: <branch @ SHA, or state-manifest hash>
    source_of_truth: <file/dir that is canonical>
    coding_environment: <e.g. Claude Code, Cursor, Codex CLI>

  direction:
    roadmap_increment: <INC-xxx or ADHOC(owner instruction)>   # every envelope traces to the roadmap or an explicit owner ask
    non_goals_in_force: [<from PROJECT_INTENT — copied so the worker sees them as forbidden scope>]

  task:
    objective: >
      <exact, testable objective — what done means, not how>
    task_class: <FEATURE | BUGFIX | REFACTOR | RESEARCH | UI_CHANGE | MIGRATION | ...>
    risk_tier: T1 | T2 | T3 | T4 | T5
    risk_rationale: <one line — why this tier>

  scope:
    allowed_paths: [...]
    forbidden_paths: [...]                   # protected/verifier-owned files always listed here
    allowed_tools: [...]
    forbidden_tools: [...]
    forbidden_actions: [force-push, release, deploy, pay, migrate-destructive, ...]

  roles:
    writer: <model/agent id>
    reviewer: <model/agent id or NONE(T1)>   # must differ from writer for T2+ where callable
    acceptance_authority: <local gate / human / CI>

  active_modules: [truth_core, bounded_contract, ...]
  not_activated:
    <module>: <reason>                       # only for plausibly-relevant exclusions

  acceptance_criteria:
    - <observable criterion 1>
    - <observable criterion 2>

  verification:
    required_evidence: <per tier: E2 / E3 / E3+E4 / ...>
    commands:                                # deterministic where possible
      - <exact command the worker must run>
    integration_checks: [<affected suites>]  # T3+

  rollback:
    strategy: <revert commit / restore manifest / N/A-reversible>
    checkpoint_before_start: true | false

  stop_conditions:
    - scope or risk exceeds this envelope
    - required permission/authority missing
    - base state changed underneath the task
    - protected file would need modification
    - security/secret finding requiring escalation

  git_policy:
    commit: <allowed branch + message convention>
    push: <authorized remote branch or NONE>
    verify_remote_sha: true | false

  candidate:
    identity_method: <git SHA | file-hash manifest>

  owner_contact:
    escalate_on: [T4+ authority, security finding, irreconcilable ambiguity]
    on_no_answer: <safe default — usually PAUSE>
```

## Envelope validity rules

- An envelope is stale when its `base` no longer matches reality → worker stops, orchestrator reissues.
- Widening `allowed_paths`, raising tools, or raising risk requires a **reissued envelope**, never in-place drift.
- The worker's handoff must reference this `envelope.id`.
