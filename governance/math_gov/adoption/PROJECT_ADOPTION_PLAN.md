# Project adoption and cutover plan — NOT YET EXECUTED

## Step 0 — Safety and baseline
- Identify actual target (Gemini AI Studio session, Gemini API+ADK project, code repo, local Lean project or other). A Gemini chat UI is not by itself a host capable of controlling subagents or capturing every event.
- Snapshot source, branch, three existing authority files and original prompts/results with owner permission, redact/limit secrets. Record checksums and independent archive anchor.
- Review and reconcile universal canonical rule precedence; do not overwrite the installed governance files or casually introduce a fourth authority.

## Step 1 — Owner-approved research identity
- Capture original question as raw artifact and hash from authenticated user channel; retain all intuitive revisions unmodified.
- Separate human-readable exact mathematical statement and formal Lean challenge (not written by the same unchecked proof worker). Independently review quantifiers, domains, assumptions, foundations and object identities.
- Sign/version owner grant and exact intended scope; policy/risks/retention/law and budgets.

## Step 2 — Trusted host
- Establish external authenticated actor roster and role separation, tool ACL, task leases, CAS revisions, immutable audit log with off-host anchors, data backup and key lifecycle.
- Set up an actual supervisor runtime with model-specific API scopes and isolated workers. For API integrations, capture exact model ID/version and actual effective context window; avoid guessing Gemini capabilities.
- Add independent Watchdog; external enforcement of tool write access. Supervisor read/dispatch, workers scoped write to isolated branches, reviewer readonly, acceptor separate.

## Step 3 — Mathematical and context data
- Inventory the whole theorem/lemma/task/step graph and dependency types, specify OR alternatives and conditional side obligations, negative history and cross-project link taxonomy.
- Build exact source-anchored Task Context Capsules; checksum each delivered element and record context read receipt and recall probes.
- Define step-level obligations and state transitions, including acceptance criteria that cannot be satisfied by task-count alone.

## Step 4 — Real Lean environment
- Pin actual Lean and dependencies with `lean-toolchain`, `lake-manifest.json` and trusted sources; isolate untrusted code/no secrets/network restrictions.
- Run `lake build` and make sure target is in built module; inspect `#print axioms`; for Lean 4.35+ use `lake check --paranoid`; run independent challenge/solution comparison with `lake comparator` and pinned permissible axiom set. Record command, exit, stdout/stderr, time, host, source/toolchain digests.
- Qualified mathematics reviewer checks semantic correspondence and meaningfulness of the theorem target. Reviewer cannot modify frozen worker branch.

## Step 5 — Adversarial tests with negative controls
- Test undocumented source edits, altered question, missing premises, circular/hidden dependencies, open subgoals, fabricated Lean success, statement-name bait/switch, unjustified division, disallowed `sorryAx`, stale diagram, modified formal target, unreviewed cross-project link, missing events, malformed input, worker collision, supervisor crash and context recall failure.
- Reproduce a complete real session from prompt archive to a small independently verified theorem before claiming any proof gate functional.

## Step 6 — Approval and promotion
- Independent reviewer verifies exact frozen candidate and raw tool receipts; qualified, distinct acceptor approves exact digest; human owner approves mission/risks/cutover.
- Reconcile project state by compare-and-swap, record old/new authority digests, exact cutover time, backup and rollback. Remove no history.
- Only after observed working operation may reports say LIVE-ENFORCED. A successful local test suite alone yields `STRUCTURAL_TEST_PASS_ONLY`.

## Backout criteria
- On failed audit, missing evidence, source mismatch or authority conflict: stop mutations, restore prior canonical rules, retain incident log, do not invent proof or delete attempts.
