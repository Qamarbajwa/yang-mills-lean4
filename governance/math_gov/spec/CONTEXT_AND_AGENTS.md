# Supervisor, worker and context specification

## Roles and one-supervisor principle
Use ONE durable logical supervisor per governed mathematical project with independently controlled **policy**, **watchdog**, **proof verification** and **acceptance**. Model process may restart; only the trusted host holds stable state. Worker count varies with task independence, capability and budget. Multiple Chrysalis-inspired self-evolving governors are not needed for individual tasks.

## Task Context Capsule (TCC)
Mandatory content: `task_id`, `branch_id`, `owner_subject_anchor`, `approved_formal_target_anchor`, `exact_goal`, `relevant definitions`, `assumptions`, `premise step digests`, `negative_history`, `open obligations`, `sources with hashes and trust labels`, `toolchain and allowed commands`, `role+grant`, `deadline/lease`, `token budget`, `output_schema`, `acceptance criteria`, `snapshot_digest`, `read_receipt`. Missing => cannot dispatch high-risk work.

The worker must verify source access, report unavailable documents as UNKNOWN, and answer a recall test about exact definitions, target, side conditions and negative history before proof mutation. A large context window never guarantees correct recall.

## Branch behavior
- SEQUENTIAL: step n requires verified prerequisites from earlier steps; handoff when the predecessor status is legitimate.
- PARALLEL: branch-scoped workers may explore different pathways in isolation, with separate evidence snapshots and no cross-branch visibility until authorized.
- RECONVERGENCE: supervisor compares claims, brings over only qualified results and records why accepted/rejected; do not delete failed branches.
- ISOLATED REVIEW: reviewer receives frozen artifact and needed definitions, not editable worker branch; blinding where appropriate.

## Mid-run state, 5 of 10 example
Count only tasks with `EXECUTED`/`SUBMITTED` etc for execution progress; show distinct VERIFIED_TASK, FORMAL_STEP, THEOREM results. A task performed and awaiting review must not become a verified proof. Pending/failed branches remain in record. `UNKNOWN` theorem progress is preferred to invented percentages.

## Watchdog
Independent heartbeat/liveness source + actual output/diff receipts; detect stalled work, excessive budgets, repeated false-positive progress, source drift, model context pressure, duplicate workers or unauthorized tool call. It cannot declare the mathematics correct. Escalate after bounded retries with exact blocker; don't spin forever.

## Model capability gating
Before assigning advanced work, test whether that model+tool environment can solve representative lower-risk step tasks, use Lean correctly, handle counterexamples, preserve assumptions, and reproduce instructions across a synthetic context rollover. Maintain per-task type empirical pass/failure, budget and reviewer effort. No capabilities inferred solely from 'Gemini 3.8' product label.

## Context rollover policy
Trigger rehydration at model-specific calibrated capacity, repeated recall failures, changed definitions or large nested branches. Keep immutable archive, independently generated project snapshot, active branch task capsule and compact working memory distinct. The supervisor requests the necessary originals by ID, not by trusting summary-only memory. Use configurable limits and measure retrieval recall, not a universal context percentage.
