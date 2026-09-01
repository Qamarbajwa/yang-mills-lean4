# YM-003 Missing-Bridge Graph Design

**Status:** `APPROVED_WITH_PREIMPLEMENTATION_RECONCILIATION`

## Goal

Determine the smallest source-bound mathematical implications whose absence
prevents currently rigorous Yang–Mills components from forming a valid Clay
target construction, without presupposing that those implications are true,
necessary, unique, or provable.

## Scope and state boundary

YM-002F remains `INDEPENDENTLY_VERIFIED / CLOSED`. Its scientific fingerprint
and E4 receipt are historical inputs, not silently rewritten. YM-003 starts at
the current handover candidate and may produce a bounded YM-002F erratum only
if the resonance audit proves the existing classification scientifically
defective. Any such erratum must receive its own candidate-bound E3 and fresh
E4 review. YM-004 and later tasks remain gated until YM-003 closes.

The constitutional YM-003 invariant is:

> Uniformity inside a regime is not control across a regime transition.

The graph therefore distinguishes the limits `a→0`, `V→∞`, and
`g_0(a)→0` from nonperturbative RG flow toward the infrared. A theorem may be
uniform in volume while remaining unusable on the asymptotically free
weak-coupling trajectory.

## Preconditions and reconciliation gate

Before graph construction, inspect the theorem-level expansion in
`literature/OBSTRUCTION_RESONANCE_MATRIX.md` against each theorem's own
limitation and dependency records. The current era-level repetition is a
presentation summary only until verified; if it assigns a source-incompatible
score, preserve the closed YM-002F record and create a bounded erratum rather
than editing its accepted history. Validate that obstruction dependencies are
irreflexive: `O13-TRANSFER` may not depend on itself unless a recursive object
is explicitly defined and tested.

## Architecture and authority direction

The six artifacts form a directed evidence packet. The authoritative data flow
is:

`BRIDGE_EDGE_REGISTER.md → derived graph/matrices/views`.

`BRIDGE_EDGE_REGISTER.md` is the authoritative edge source. The graph,
assumption-transfer matrix, and limit/regime matrix are consistency-bound
projections and may not independently redefine an edge. A contradiction
between a projection and the edge register is an E3 failure, not a choice
between representations. `MINIMAL_SUFFICIENT_ESTIMATE_REGISTER.md` is
authoritative for estimate-specific metadata, but every estimate points back
to one or more bridge edges.

The six artifacts are:

1. `MISSING_BRIDGE_GRAPH.md` is the human-readable topology from known theorem
   to missing implication/estimate to known theorem or Clay obligation.
2. `BRIDGE_EDGE_REGISTER.md` is the authoritative one-record-per-edge ledger.
3. `ASSUMPTION_TRANSFER_MATRIX.md` tracks assumptions entering, leaving, and
   newly introduced at every edge.
4. `LIMIT_AND_REGIME_MATRIX.md` tracks dimension, group, matter, regulator,
   volume, coupling, RG window, crossover, and all limit trajectories.
5. `MINIMAL_SUFFICIENT_ESTIMATE_REGISTER.md` isolates the smallest provisional
   estimates that would strictly strengthen the chain.
6. `YM-003_NEGATIVE_TRANSFER_TESTS.md` records regression cases preventing
   invalid compositions and overpromotion.

## Required edge schema

Every edge record contains:

- `EDGE_ID`;
- exact `LEFT_THEOREM_OR_STATE` and `RIGHT_THEOREM_OR_TARGET_OBLIGATION`;
- `MATHEMATICAL_PROPOSITION_NEEDED`;
- `ASSUMPTIONS_ENTERING`, `ASSUMPTIONS_LEAVING`, and
  `ASSUMPTIONS_NEWLY_INTRODUCED`;
- dimension, gauge group, matter content, model, regulator, and volume regime;
- `REGIME_FROM`, `REGIME_TO`, `BARE_COUPLING_BEHAVIOR`, `RENORMALIZED_SCALE`,
  `RG_SCALE_WINDOW`, `CROSSOVER_CONTROL`, `UNIFORM_CONSTANTS`, and
  `LIMIT_TRAJECTORY`;
- observable algebra, gauge-invariance requirements, positivity and
  reconstruction assumptions;
- evidence source, provenance, counterevidence, bypass conditions;
- epistemic status: `PROVED`, `KNOWN_CONSEQUENCE`, `INFERENCE`, `HYPOTHESIS`,
  or `UNKNOWN`;
- necessity class: `TARGET_REQUIRED`, `ROUTE_REQUIRED`, or `OPTIONAL_ROUTE`.
- `TARGET_REQUIRED` edges point to exact Clay/project requirement IDs;
  `ROUTE_REQUIRED` edges carry a `ROUTE_ID`.

Assumption transfer is formally auditable. Each entering assumption receives a
status `PRESERVED`, `DISCHARGED`, `STRENGTHENED`, `WEAKENED`, `REPLACED`,
`NEW`, or `UNKNOWN`. A `DISCHARGED` assumption must include `DISCHARGED_BY`
and `DISCHARGE_EVIDENCE`; assumptions may not disappear silently.

The proof-dependency subgraph is acyclic by default. Any cycle requires an
explicit justification and classification as a simultaneous/fixed-point
construction; ordinary proof edges may not silently form cycles.

No edge is upgraded because multiple pathways resonate at one locality.

## Scientific focal question

The first high-value question is whether a known general theorem states that a
uniform exponential-clustering bound for renormalized gauge-invariant
observables, under explicit OS/reconstruction hypotheses, implies a positive
physical Hamiltonian spectral gap. YM-003 records the exact hypotheses and
scope if such a theorem exists; otherwise the implication remains
`UNKNOWN`/`HYPOTHESIS`. The observable algebra must be sufficiently rich to
detect physical excitations rather than merely a selected correlator family.
Each edge therefore records `OBSERVABLE_ALGEBRA`,
`VACUUM_CYCLICITY_REQUIREMENT`, `DENSITY_OF_OBSERVABLE_GENERATED_STATES`,
`CONNECTED_CORRELATOR_CLASS`, `SPECTRAL_REPRESENTATION_USED`,
`PHYSICAL_HILBERT_SECTOR`, and `VACUUM_UNIQUENESS_ASSUMPTION`.

The primary clustering candidate must use a connected/truncated correlator,
explicit separation `x`, and renormalized observables. The spectral candidate
must normalize energy physically, rather than treating an unscaled lattice
eigenvalue as a continuum mass. Applicable edges also record
`PHYSICAL_SCALE_SETTING`, `ENERGY_NORMALIZATION`,
`DIMENSIONFUL_OR_DIMENSIONLESS`, `RENORMALIZATION_CONDITION`,
`REFERENCE_PHYSICAL_SCALE`, and `CONTINUUM_SCALING_BEHAVIOR`. A candidate may
use `m_phys = Delta_lattice(a)/a` or a rigorously defined ratio such as
`m_gap/Lambda_YM`; neither is assumed without its scale-setting prescription.
Tightness requires all subsequential limits to
coincide (or an explicitly equivalent uniqueness criterion). A joint/directed
renormalized limit is sufficient in principle; arbitrary iterated-limit
interchange is not imposed as a Clay necessity. A non-Gaussian witness is a
candidate sufficient route, not the definition of nontriviality. OS claims
bind to the repository's exact axiom convention and a specified
gauge-invariant observable algebra. Universal group coverage means one theorem
schema applies to every compact simple `G`; constants may depend on `G`.

“Minimal” is not a visual judgment. Each estimate and unresolved bridge set
records `MINIMALITY_CLASS` from `ASSUMPTION_MINIMAL`, `EDGE_CUT_MINIMAL`,
`ROUTE_MINIMAL`, `LOGICAL_STRENGTH_MINIMAL`, `CURRENT_KNOWLEDGE_MINIMAL`, or
`NOT_ESTABLISHED`, together with `COMPARISON_SET` and
`MINIMALITY_ARGUMENT`. A project-identified bottleneck is not automatically a
mathematically necessary bottleneck. YM-003 may validly conclude
`NO_SINGLE_MINIMAL_ESTIMATE_IDENTIFIED` and instead record the smallest
justified unresolved bridge cut set.

## Acceptance and verification

E3 must prove deterministic structural consistency, exact candidate binding,
irreflexive obstruction dependencies, explicit regime/limit fields, projection
consistency, acyclic proof dependencies (or explicit cycle justification), and
preservation of unknown/hypothesis labels. Fresh independent E4 must challenge
source fidelity, assumption transfer/discharge, regime transitions, physical
scale setting, observable completeness, spectral inference, possible bypasses,
negative memory, and YM-004 readiness. YM-003 may close only after every edge
is either source/proof-backed or explicitly marked `UNKNOWN`/`HYPOTHESIS`, no
assumption disappears between nodes without discharge evidence, and either:

1. at least one sharply specified candidate estimate is isolated; or
2. the evidence demonstrates that no unique/single load-bearing estimate is
   justified and identifies the smallest justified unresolved bridge set.

## Non-goals

This design does not propose a proof, declare a common obstruction theorem,
promote any analogue or lattice result to a Clay solution, or authorize public
release, publication, deployment, or external spend.
