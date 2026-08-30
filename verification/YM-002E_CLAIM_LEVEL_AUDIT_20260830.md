# YM-002E — Claim-Level Adversarial Audit

- Date: `2026-08-30`
- Task: `YM-002E`
- Audit base candidate: `299871d70d77dd37526bfd12555d090b49111980`
- Source records: `evidence/primary/YM-002E/SOURCE_RECORD_*.yaml`
- Audit status: `E3_COMPLETE_PENDING_INDEPENDENT_CLOSEOUT`
- Governing target: `OFFICIAL_PROBLEM_SPECIFICATION.md`

## Mandatory target boundary

The Clay target requires, for every compact simple gauge group, a non-trivial quantum Yang–Mills theory on `R^4`, axiomatic control at least as strong as OS/Wightman, and a positive Hamiltonian spectral gap. Fixed-gauge propagator scales, conditional constructions, single-group results, regulator claims, or incomplete proof artifacts cannot be promoted to a solution without the missing bridge obligations being discharged.

## SRC-YM-002E-FERREIRA-2508.20568-v1

- Primary artifact: `evidence/primary/YM-002E/arxiv_2508.20568v1.pdf`
- SHA-256: `7c78d18c6e6222d114a05c3852b3814f45e15261fc97d336dcd0f9df46db5c30`
- Scope observed in artifact: Landau-gauge gluon-propagator mass scale, functional methods, DSE observables, and QCD/Yang–Mills phenomenology.
- Direct audit observations: the paper uses DSE/fRG inputs and explicitly drops two-loop terms in the background-field DSE calculation; it defines `m_gap` as a screening-type propagator scale and notes that the definition is not unique.
- Clay obligations: no construction of a universal compact-simple-group OS/Wightman theory on `R^4`; no proof that the propagator screening scale equals the Hamiltonian spectral gap; no complete constructive continuum/infinite-volume existence theorem.
- Result: `RELATED_MECHANISM_RESULT / NOT_A_CLAY_SOLUTION_CLAIM`.
- Disposition: retain in mechanism/literature memory; do not consume the claimed-solution closeout gate and do not promote.

## SRC-YM-002E-KIRK-ZENODO-18824739-v1.0

- Primary artifact: `evidence/primary/YM-002E/zenodo_18824739_v1.0.pdf`
- SHA-256: `13b9fc8cb7109f8f55cca7b285417458bd9a2b99faccf11bc483f25d26fcd3e1`; Zenodo MD5 reconciled to `f5c2be4b71128a384d6509747f1b7dee`.
- Scope observed in artifact: four-dimensional `SU(2)` lattice-to-continuum construction with OS reconstruction and a positive gap conditional on `WC1–WC3`.
- Direct audit observations: the paper states that it does not prove `WC1–WC3`; it identifies the weak-coupling package as the single unresolved essential input for the SU(2) mass-gap result. It also identifies an open continuum Schwinger–Dyson identity issue for uniqueness.
- Clay obligations: universal compact-simple-group quantification is not met by an `SU(2)` result; the unproved weak-coupling hypotheses are load-bearing; the result is therefore conditional rather than an unconditional Clay proof.
- Result: `CONDITIONAL_CLAIM / NOT_ACCEPTED_FOR_CLAY_TARGET`.
- Failure locality: `WC1–WC3` and associated lattice input package; universal-group scope.

## SRC-YM-002E-JACOBSEN-2506.00284-v1

- Claim artifact: `evidence/primary/YM-002E/arxiv_2506.00284v1_source.tar.gz`
- SHA-256: `f97569b3bd122de923d6d7a642ec24bcccb319f8e215fa1f6f4781a241efcf51`
- Scope claimed in artifact: pure `SU(3)` Yang–Mills on `R^4`, using a five-dimensional orbifold regulator, joint continuum/infinite-volume limits, OS reconstruction, and a positive glueball mass.
- Direct artifact observations from `main.tex`: the three `Proof sketch` environments contain short nonempty bodies (source lines 383–385, 404–406, and 419–421), and the bibliography entries for `ref1` through `ref11` are populated (source lines 892–937). These observations do not establish complete proofs or validate the cited technical inputs; the claimed estimates and proof obligations remain unverified and are not traceable to a complete, independently checked argument in the supplied v1 source.
- Clay obligations: universal compact-simple-group quantification is not met by an `SU(3)`-only result; the regulator-to-pure-4D target bridge and cited constructive estimates are not artifact-supported at the supplied byte level.
- Current arXiv state: v2 is withdrawn by arXiv Admin for not meeting research-content quality standards. This is recorded as provenance evidence only and is not treated as a mathematical refutation of v1.
- Result: `QUARANTINED_CLAIM / PROOF_COMPLETENESS_UNVERIFIED_AND_OUTSIDE_FULL_CLAY_GROUP_SCOPE`.
- Failure locality: proof completeness and source traceability remain unverified; universal-group scope; regulator equivalence remains unverified.

## Legacy queue reconciliation

The existing internal `CLAIM-2024-001 — Sky Yang` entry remains separate and unresolved. Bounded repository provenance recovery found only its introduction as a generic internal screening row and no primary-source identity; the external `Sky Yang Cao / Sky Cao` lead remains unproven and unbound. It is now classified `UNRESOLVED_ORPHANED_LEGACY_CLAIM` with `NOT_ACCEPTED_PROVENANCE_INSUFFICIENT`; no historical queue row was rewritten.

## E3 conclusion

- Three requested artifacts are byte-bound and individually audited at the available artifact/scope level.
- Ferreira: mechanism result, not a solution claim.
- Kirk: conditional SU(2) result, not an unconditional Clay solution.
- Jacobsen v1: quarantined claim with proof completeness/traceability unverified and SU(3)-only scope; v2 withdrawal preserved as provenance.
- Legacy Sky Yang row: `UNRESOLVED_ORPHANED_LEGACY_CLAIM` after bounded repository provenance recovery; no artifact assigned.
- `NO_UNSUPPORTED_SOLUTION_CLAIM_ACCEPTED`: `TRUE`.
- YM-002E remains `RELEASED_IN_PROGRESS`; independent closeout is still required and downstream tasks remain blocked.
