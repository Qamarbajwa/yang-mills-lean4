# YM-003 Missing-Bridge Graph Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the YM-003 missing-bridge graph as a source-bound, deterministic evidence packet that identifies the smallest mathematically explicit interfaces still separating the rigorous Yang–Mills UV, continuum, IR, lattice, correlation-decay, spectral, and reconstruction programs. Preserve every unresolved implication as `UNKNOWN` or `HYPOTHESIS`; do not turn the graph into a proof or silently alter the closed YM-002F record.

**Architecture:** `BRIDGE_EDGE_REGISTER.md` is the single authoritative edge ledger. A typed parser/validator in `src/ymmg/bridge_graph.py` reads its YAML records, checks assumptions, regimes, physical scales, observable completeness, target/route binding, and proof dependencies, and renders deterministic consistency-bound projections: `MISSING_BRIDGE_GRAPH.md`, `ASSUMPTION_TRANSFER_MATRIX.md`, and `LIMIT_AND_REGIME_MATRIX.md`. `MINIMAL_SUFFICIENT_ESTIMATE_REGISTER.md` is authoritative for estimate metadata but every estimate references one or more edge IDs. `YM-003_NEGATIVE_TRANSFER_TESTS.md` is the checked-in regression corpus and explanation of rejected compositions. Scientific artifact classification and the closed-world fingerprint are updated only after the packet is complete and verified.

**Tech Stack:** Markdown with one canonical YAML record per edge/estimate, Python 3, PyYAML, pytest, existing `ymmg.ros` candidate/fingerprint/evidence helpers, and the repository governance YAML/Markdown ledgers.

**Spec:** `docs/superpowers/specs/2026-09-01-ym003-missing-bridge-graph-design.md` (approved amended design; implementation must preserve its authority direction, field names, epistemic taxonomy, limit distinction, minimality rule, and E3/E4 gate).

## Global Constraints

- YM-002F remains `INDEPENDENTLY_VERIFIED / CLOSED`, with its historical candidate, E4 receipt, and scientific fingerprint unchanged. Do not edit accepted YM-002F science merely to make YM-003 convenient.
- Before construction, audit `literature/OBSTRUCTION_RESONANCE_MATRIX.md` against theorem-level limitation/dependency records. If a source-incompatible classification is found, record a bounded erratum with a new candidate-bound E3 and fresh E4; otherwise document that the apparent era repetition is presentation-only.
- Distinguish uniformity within a fixed regime from a regime transition. Track `a→0`, `V→∞`, `g0(a)→0`, and nonperturbative RG flow separately; never infer a continuum/IR result from a volume-uniform estimate alone.
- Every edge is either source/proof backed or explicitly `UNKNOWN`/`HYPOTHESIS`. Resonance, analogy, numerical evidence, and a project bottleneck label never upgrade an epistemic status.
- Every assumption must be preserved, discharged with evidence, strengthened, weakened, replaced, newly introduced, or explicitly unknown. No assumption may disappear between nodes.
- `TARGET_REQUIRED` edges bind to exact canonical target-requirement IDs from the official problem specification. `ROUTE_REQUIRED` edges carry an explicit `ROUTE_ID`; `OPTIONAL_ROUTE` edges cannot be used to claim target completion.
- Proof dependencies are irreflexive and acyclic by default. A cycle is accepted only when the record classifies it as a simultaneous/fixed-point construction and supplies a concrete justification; ordinary theorem composition must fail closed.
- Physical scale is explicit: record `PHYSICAL_SCALE_SETTING`, `ENERGY_NORMALIZATION`, `DIMENSIONFUL_OR_DIMENSIONLESS`, `RENORMALIZATION_CONDITION`, `REFERENCE_PHYSICAL_SCALE`, and `CONTINUUM_SCALING_BEHAVIOR`. A bare lattice eigenvalue is not a continuum mass.
- Observable/spectral claims record `OBSERVABLE_ALGEBRA`, `VACUUM_CYCLICITY_REQUIREMENT`, `DENSITY_OF_OBSERVABLE_GENERATED_STATES`, `CONNECTED_CORRELATOR_CLASS`, `SPECTRAL_REPRESENTATION_USED`, `PHYSICAL_HILBERT_SECTOR`, and `VACUUM_UNIQUENESS_ASSUMPTION`.
- The YM-003 closeout may identify either a sharply specified load-bearing estimate or `NO_SINGLE_MINIMAL_ESTIMATE_IDENTIFIED` plus the smallest justified unresolved bridge cut set. A visual “bottleneck” is not a minimality proof.
- Run focused tests after each task and the complete suite before any closeout claim. Do not claim E3/E4 or YM-003 closure from a partial test run.

## Implementation Tasks

### 1. Reconcile the YM-002F boundary and freeze canonical inputs

- [ ] Read the accepted YM-002F E4 receipt, `literature/OBSTRUCTION_RESONANCE_MATRIX.md`, each theorem-era limitation/dependency matrix, `GOVERNANCE_STATE.yaml`, and the current fingerprint manifest. Add `tests/test_ym003_preconditions.py` with failing checks that the YM-002F state is closed, YM-003 is `READY`, the exact candidate/fingerprint are present, and obstruction dependencies contain no reflexive edge.
- [ ] Implement only the read-only precondition helpers needed by those tests (for example, `load_ym002f_boundary()` and `validate_obstruction_dependencies()` in `src/ymmg/bridge_graph.py`). Make the reconciliation result explicit as `PRESENTATION_ONLY` or `ERRATUM_REQUIRED`; do not mutate YM-002F while the test is being written.
- [ ] Run `pytest -q tests/test_ym003_preconditions.py`; then record the source comparison and decision in the YM-003 implementation evidence notes. If an erratum is required, stop packet construction at this task until its candidate-bound E3/E4 is complete.

**Interfaces:** consumes the closed YM-002F ledgers and source matrices; produces a frozen input snapshot and a tested reconciliation decision used by every later task.

### 2. Define the canonical edge/assumption/scale schema (tests first)

- [ ] Add `tests/test_ym003_bridge_graph.py` fixtures containing a valid edge and deliberately invalid variants: missing required field, silent assumption disappearance, `DISCHARGED` without `DISCHARGED_BY`, missing physical-scale field, `TARGET_REQUIRED` without an exact target ID, `ROUTE_REQUIRED` without `ROUTE_ID`, unknown epistemic label, self-dependency, ordinary dependency cycle, and a cycle with explicit fixed-point justification.
- [ ] Write failing tests for `parse_edge_records(text)`, `validate_edge_record(record)`, `validate_assumption_transfers(record)`, `validate_proof_dependency_dag(records)`, and `validate_target_route_binding(record, target_ids)`. Tests must assert actionable field-level errors and preservation of the five allowed epistemic values and seven assumption-transfer statuses.
- [ ] Implement the smallest typed parser/validator in `src/ymmg/bridge_graph.py`. Canonical serialization is one heading per edge followed by a fenced `yaml` mapping; parser output is a list of dictionaries with stable field ordering for rendering. Reject duplicate `EDGE_ID`s and duplicate assumption keys.
- [ ] Add the projection contract: a projection may omit explanatory prose but its edge IDs, endpoints, status, regime, assumptions, and estimate references must agree byte-for-byte after normalization with the authoritative register. Add a failing test for a projection that invents an edge or changes `UNKNOWN` to `PROVED`, then implement `validate_projection_consistency(...)`.

**Interfaces:** consumes Markdown/YAML text; returns normalized records and deterministic validation errors; no scientific files are written yet.

### 3. Create the authoritative `BRIDGE_EDGE_REGISTER.md`

- [ ] Add tests requiring at least the initial source-bound edge set and exact schema coverage. The initial records are `E-UV-RG`, `E-CUTOFF`, `E-VOLUME`, `E-CLUSTER`, `E-SPECTRAL`, `E-GROUP`, `E-ERROR`, and the optional `E-NONTRIV` route. Tests must require explicit statuses rather than assuming any of these implications are true.
- [ ] Write `BRIDGE_EDGE_REGISTER.md` with one canonical YAML record per edge. Each record must contain `EDGE_ID`, exact left/right nodes, `MATHEMATICAL_PROPOSITION_NEEDED`, `ASSUMPTIONS_ENTERING`, `ASSUMPTIONS_LEAVING`, `ASSUMPTIONS_NEWLY_INTRODUCED`, per-assumption transfer status plus discharge evidence where applicable, dimension, gauge group, matter content, model, regulator, volume regime, `REGIME_FROM`, `REGIME_TO`, `BARE_COUPLING_BEHAVIOR`, `RENORMALIZED_SCALE`, `RG_SCALE_WINDOW`, `CROSSOVER_CONTROL`, `UNIFORM_CONSTANTS`, `LIMIT_TRAJECTORY`, observable/gauge/positivity/reconstruction fields, physical-scale fields, evidence/provenance/counterevidence/bypass fields, epistemic status, necessity class, target/route binding, and proof-dependency fields.
- [ ] Bind source claims to theorem IDs and repository paths; mark cross-regime, spectral, universal-group, and exact-limit implications `UNKNOWN` or `HYPOTHESIS` unless a source actually proves them. Include the exact proposition that would be needed, not a prose aspiration.
- [ ] Run the focused schema and parser tests until the register validates with no warnings.

**Interfaces:** authoritative input for all projections and estimate references; no projection may add or redefine an edge.

### 4. Render and verify `MISSING_BRIDGE_GRAPH.md`

- [ ] Add a failing test that graph topology is a directed path/branch from known theorem/state through a boxed missing implication/estimate to a known theorem or exact Clay obligation, and that every displayed edge ID exists in the register.
- [ ] Implement `render_missing_bridge_graph(records)` and write `MISSING_BRIDGE_GRAPH.md`. Show the weak-bare-UV → controlled-RG → nonperturbative-IR → uniform physical correlation decay → physical spectral gap architecture, with OS/Wightman reconstruction and gauge-invariant observables surrounding the chain. Label uniformity and regime transitions as different edge annotations.
- [ ] Make rendering deterministic and add a test that re-rendering the same register produces identical bytes and that a tampered graph fails projection consistency. Preserve `UNKNOWN`/`HYPOTHESIS` labels in every view.

**Interfaces:** consumes only normalized register records; produces the human-readable topology projection.

### 5. Render `ASSUMPTION_TRANSFER_MATRIX.md`

- [ ] Add tests that each edge’s entering assumptions appear in the matrix, each leaving/new assumption is accounted for, and every `DISCHARGED` status names a valid `DISCHARGED_BY` edge or theorem plus `DISCHARGE_EVIDENCE`.
- [ ] Implement `render_assumption_transfer_matrix(records)` and write the matrix with one row per edge/assumption, including `PRESERVED`, `DISCHARGED`, `STRENGTHENED`, `WEAKENED`, `REPLACED`, `NEW`, or `UNKNOWN`. A projection mismatch must fail E3 rather than be reconciled manually.
- [ ] Add negative fixtures for dropped gauge invariance, dropped positivity, hidden renormalization conditions, and a discharge claim pointing to a nonexistent edge.

**Interfaces:** projection of the authoritative assumption fields; consumed by E3 and fresh E4 review.

### 6. Render `LIMIT_AND_REGIME_MATRIX.md`

- [ ] Add tests requiring simultaneous explicit columns for dimension, compact simple gauge group, matter content, lattice/continuum, finite/infinite volume, regulator, bare/renormalized coupling, RG window, crossover control, constants, and limit trajectory.
- [ ] Implement `render_limit_regime_matrix(records)` and write the matrix. Represent `a→0`, `V→∞`, and `g0(a)→0` separately from RG flow; state whether a bound is uniform in a regime and whether it actually crosses into the next regime. Require physical-scale and continuum-scaling entries for every edge touching a continuum or spectral claim.
- [ ] Add regression cases proving that volume-uniform finite-lattice control does not satisfy a weak-coupling continuum edge, and that arbitrary iterated-limit interchange is not silently inferred from a joint/directed limit.

**Interfaces:** projection consumed by graph review, E3 regime checks, and E4 transition challenge.

### 7. Build `MINIMAL_SUFFICIENT_ESTIMATE_REGISTER.md`

- [ ] Add tests for the estimate schema: `ESTIMATE_ID`, exact proposition/bound, observable and scale normalization, edge references, target/route references, assumptions, regime and limit domain, epistemic status, and `MINIMALITY_CLASS`, `COMPARISON_SET`, `MINIMALITY_ARGUMENT`.
- [ ] Implement `render_estimate_register(...)` and record E1–E8 candidates:
  - E1 connected/truncated correlator bound at explicit separation for renormalized gauge-invariant observables;
  - E2 physical energy normalization, including `m_phys = Delta_lattice(a)/a` or a rigorously scale-set dimensionless ratio;
  - E3 tightness plus coincidence of all subsequential limits;
  - E4 directed/joint renormalized limit without mandatory iterated-limit interchange;
  - E5 non-Gaussian witness as a sufficient candidate, not the definition of nontriviality;
  - E6 exact OS axiom convention with observable algebra/cyclicity/density;
  - E7 exact approximation/truncation remainder control;
  - E8 one theorem schema for every compact simple `G`, with constants allowed to depend on `G`.
- [ ] If comparison does not justify one unique estimate, record `NO_SINGLE_MINIMAL_ESTIMATE_IDENTIFIED` and the smallest justified unresolved edge cut set with an explicit minimality argument. Do not call E1 or E2 “minimal” merely because they are visually central.

**Interfaces:** authoritative estimate metadata; every estimate points to one or more register edges and may be consumed by YM-004 only after YM-003 closes.

### 8. Add `YM-003_NEGATIVE_TRANSFER_TESTS.md` and executable regression coverage

- [ ] Add failing tests for invalid theorem composition: era analogy promoted to proof, resonance promoted to a theorem, finite-volume result promoted to infinite-volume, uniform-in-volume estimate used across coupling regimes, gauge-variant observable used for a physical gap, non-cyclic algebra used as complete spectrum, unscaled lattice eigenvalue called a mass, `UNKNOWN` upgraded by projection, missing discharge evidence, and ordinary dependency cycles.
- [ ] Implement these cases as named pytest fixtures and write the same cases with expected failure reason and epistemic classification in `YM-003_NEGATIVE_TRANSFER_TESTS.md`. Include bypass conditions where a different route could avoid an edge, without deleting the unresolved edge from the graph.
- [ ] Ensure negative tests are deterministic and independent of current candidate hash; they test schema/logic, not a claim about the Clay problem.

**Interfaces:** executable guardrail corpus referenced by E3/E4; no negative case may be used as positive evidence.

### 9. Integrate the packet with the closed-world scientific identity

- [ ] Add tests that the six YM-003 scientific artifacts are classified `SCIENTIFIC`, listed exactly once in `SCIENTIFIC_FINGERPRINT_MANIFEST`, and declared identically in `governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml`. Update the existing manifest-length assertion (currently 22) to the new exact count and reject unlisted scientific files.
- [ ] Add the six paths to `src/ymmg/ros.py` and the classification policy in stable order. Keep `docs/superpowers/...` administrative and out of the scientific fingerprint. Recompute the scientific tree hash only after all scientific content is final.
- [ ] Update `RESEARCH_LEDGER.md`, `CURRENT_SCIENTIFIC_STATE.md`, `EVIDENCE_LEDGER.md`, `literature/PATHWAY_MEMORY_REGISTER.md`, `NEGATIVE_EVIDENCE_REGISTER.md`, `TASK_GRAPH.md`, `ROADMAP.md`, `NEXT_ACTION.md`, and `governance/envelopes/YM-003.yaml` with candidate-bound YM-003 scope, exact artifacts, gates, and the unchanged YM-002F historical boundary. Keep administrative edits separate from scientific edits when recording the candidate.

**Interfaces:** connects the bridge packet to repository identity, provenance, and task governance; candidate binding is exact and fail-closed.

### 10. Run YM-003 E3, independent E4, and close only on the amended gate

- [ ] Add `tests/test_ym003_acceptance.py` covering deterministic parse/render output, exact candidate binding, all six artifact presence, projection consistency, explicit regime/limit fields, assumption discharge, physical scale, observable completeness, unknown/hypothesis preservation, and dependency-cycle rules.
- [ ] Run focused tests, then the complete suite (`pytest -q`). Record an E3 receipt with candidate ID, scientific fingerprint, test count, artifact hashes, and any reconciliation result. A scientific edit after E3 invalidates E3 and requires a new candidate-bound receipt.
- [ ] Obtain a fresh independent E4 review that specifically challenges source fidelity, hidden assumption transfer, uniformity versus regime transitions, physical scale setting, observable cyclicity/density, spectral inference, bypasses, negative memory, and YM-004 readiness. Store raw and derived E4 records under `verification/` with exact candidate binding.
- [ ] Close YM-003 only if every edge is source/proof-backed or explicitly `UNKNOWN`/`HYPOTHESIS`, no assumption disappears, every regime change is visible, and either a sharply specified minimal estimate or the justified unresolved cut-set alternative is present. Then set YM-004 to `READY` only as permitted by governance; otherwise leave it gated and record the precise blocker.

**Interfaces:** E3 and E4 receipts consume the complete packet and repository identity; governance closeout consumes both receipts and the amended acceptance rule.

## Verification Checklist

- [ ] `pytest -q tests/test_ym003_preconditions.py tests/test_ym003_bridge_graph.py tests/test_ym003_acceptance.py`
- [ ] `pytest -q` (full repository suite; no deselected scientific gates)
- [ ] Recompute and independently verify the scientific fingerprint; confirm the exact candidate ID in E3, raw E4, derived E4, evidence ledger, and governance state.
- [ ] Re-render every projection from `BRIDGE_EDGE_REGISTER.md` and assert byte identity with the checked-in projections.
- [ ] Confirm `git diff --check`, no accidental `.pytest_*` or generated verification output enters the scientific manifest, and no accepted YM-002F file changed without a bounded erratum.
- [ ] Confirm YM-003 closeout state and YM-004 gating match the governance envelope and task graph; do not claim release/publication readiness.

## Execution Handoff

After this plan is reviewed, execute it either with the `superpowers:subagent-driven-development` workflow (recommended: one bounded task per worker with review between tasks) or with `superpowers:executing-plans` in this session. The plan is intentionally implementation-ready, but no implementation or scientific fingerprint change is authorized until an execution workflow is selected.
