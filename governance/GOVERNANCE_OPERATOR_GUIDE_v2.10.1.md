# GOVERNANCE OPERATOR GUIDE — v2.10.1

> How to deploy this governance set into any project, any coding environment, any model.
> Written for the human owner. Nothing here is worker-loaded.

## The file set

| File | Size class | Who loads it | When |
|---|---|---|---|
| MASTER ... v2.9.10_FINAL.md | ~305 KB | Nobody, by default | Reference authority. Orchestrator extracts modules from it via the index. |
| MASTER_MODULE_INDEX_v2.10.0.json | small | Orchestrator | To locate and extract only the parts a task needs. |
| RUNTIME_GOVERNANCE_KERNEL_v2.10.1.md | ~13 KB | Orchestrator | Always, every session. |
| WORKER_MICRO_KERNEL_v2.10.1.md | ~4 KB | Every worker | Always, with its envelope. |
| TASK_EXECUTION_ENVELOPE_TEMPLATE_v2.10.1.md | small | Orchestrator (fills), worker (receives) | Per task. |
| GOVERNANCE_STATE_TEMPLATE_v2.10.1.yaml | small | Lives in the repo | Filled once per project, updated at checkpoints. |
| SHA256 manifest | small | You / orchestrator | Verify file integrity before trusting a copy. |

## Three ways to start

### A. New project (Day-0)
1. Copy `GOVERNANCE_STATE_TEMPLATE` → `GOVERNANCE_STATE.yaml` in the repo root; fill it; commit.
2. Load the Runtime Kernel into your orchestrator (see per-tool loading below).
3. Set `bootstrap_level: LIGHT` for prototypes; upgrade before the first T3+ work.

### B. Mid-project adoption
1. Same as A, but set `adoption_mode: MID_PROJECT`.
2. First orchestrator task: baseline snapshot — record branch@SHA, list T4 domains present (auth/payments/migrations), list protected paths, note retrofit debt. This maps to master PART V-A.
3. Existing code is governed from now forward; do not retro-audit everything at once.

### C. Ad-hoc single session
Paste the Runtime Kernel + a minimal envelope into one chat. No state file. Accept that session continuity (§2A) is manual: you are the checkpoint.

## Loading per environment

| Environment | Orchestrator kernel goes in | Worker micro-kernel goes in |
|---|---|---|
| Claude Code | `CLAUDE.md` at repo root (or `@import` it) | Subagent definition / Task prompt prefix |
| Codex / AGENTS-style tools | `AGENTS.md` | Same file — these tools are single-agent; kernel §4 fallback applies |
| Cursor / Windsurf | `.cursorrules` / rules file | Composer/agent task prompt |
| Plain chat (any model) | First message of session | First message of worker chat + envelope |
| API pipelines | System prompt of orchestrator | System prompt of worker + envelope as user turn |

Single-agent environments: the same model plays writer and (degraded) reviewer. The kernel now handles this explicitly — fresh context review, `INDEPENDENCE: LOW` recorded, evidence bar raised.

## Module extraction (how the compiler actually works now)

The kernel says "compile only task-relevant modules." Concretely:

1. Orchestrator classifies the task (class, risk, affected components).
2. Looks up needed parts in `MASTER_MODULE_INDEX_v2.10.0.json` (e.g. payments task → PART 0-BOUND.16, PART XXXVI-*, security parts).
3. Extracts only those line ranges from the master.
4. Sends: micro-kernel + envelope + extracted modules. Never the full master.

The index is bound to the master's sha256. **If you edit the master, regenerate the index** (any script that maps `# ` headings to line ranges).

## Versioning discipline

- Every file change → bump version → regenerate SHA256 manifest.
- `GOVERNANCE_STATE.yaml` in each project records which master SHA is in force there, so projects can lag safely behind your latest governance version.
- Never edit a `_FINAL` file in place; supersede it.

## What changed in v2.10.0 (from v2.9.10 kernels)

Runtime Kernel:
- §0 Instruction authority / prompt-injection defense promoted from master PART II into the always-on kernel.
- §2A Session continuity: context loss, compaction and model switches are first-class events with a re-bind procedure.
- §4 Single-model degraded-review fallback made explicit.
- §8 E1–E5 defined inline (previously the kernel referenced levels defined only in the master).
- §12A Secrets hygiene.
- §18 Owner escalation contract (when to interrupt you, and how).
- Status labels extended with `UNKNOWN`, `NEEDS_HUMAN_AUTHORITY` (aligning with master 0-A.2).

Worker Micro-Kernel:
- Invariants 19–22: injection defense, secrets, evidence recording format, restart behavior.
- Standardized YAML handoff report so every model returns parseable, comparable output.

New artifacts:
- Task Execution Envelope template (referenced everywhere, previously shipped nowhere).
- GOVERNANCE_STATE.yaml project-binding template.
- MASTER_MODULE_INDEX.json (machine-readable map of all 177 master parts).
- This guide.

Master Constitution v2.9.10 is intentionally unchanged and remains reference authority.

## v2.10.1 — Direction layer

Problem addressed: governance tells the AI HOW to work but nothing tells it WHAT to build; agents drift or stall between owner instructions.

New per-project direction files (templates shipped):

| File | Author | Authority |
|---|---|---|
| PROJECT_INTENT.md | Owner (protected; AI proposes diffs only) | Why / done / non-goals |
| ARCHITECTURE_DECISIONS.md | Co-authored, decision log append-only | Decided shape; changing DECIDED = T3 |
| ROADMAP.md | Owner sets goals; orchestrator decomposes + maintains status | Sole source of next increments |

Kernel changes (v2.10.1): new §2B direction binding; §18 gains roadmap-empty and open-architecture-question escalations; §21 loop now defines SELECT NEXT VALID INCREMENT = top READY roadmap item, never invention. Envelope gains a `direction` block (roadmap_increment trace + non-goals as forbidden scope). GOVERNANCE_STATE.yaml gains a `direction` section and protects PROJECT_INTENT.md. UNIVERSAL_ACTIVATION_PROMPT_v2.10.1.md now ships as a file, including the interview flow for missing intent and approval-gated first roadmap batch.

Workers are unchanged apart from version: direction stays orchestrator-side; workers only ever see it compiled into envelope scope.
