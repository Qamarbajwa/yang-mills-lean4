# YM-002E — Final Four-Claim Obligation Synthesis

- Date: `2026-08-30`
- Task: `YM-002E`
- Synthesis parent candidate: `b2d063f`
- Governing target: `OFFICIAL_PROBLEM_SPECIFICATION.md`
- Status: `E3_FINAL_SYNTHESIS_READY_FOR_INDEPENDENT_CLOSEOUT`

## Decision boundary

The Clay target requires a non-trivial quantum Yang–Mills theory on `R^4` for every compact simple gauge group, axiomatic control at least as strong as OS/Wightman, and a positive Hamiltonian spectral gap. A propagator screening scale, conditional construction, single-group result, incomplete proof artifact, or orphaned internal record cannot be promoted to a Clay solution.

## Claim-obligation matrix

| Record | Artifact/provenance state | Claim-specific audit | Clay-obligation disposition | Final classification |
|---|---|---|---|---|
| Ferreira et al. | Exact arXiv `2508.20568v1` bytes bound by source record | Landau-gauge gluon-propagator/DSE screening mechanism; two-loop truncation; non-unique screening-scale definition | No universal constructive continuum theory, OS/Wightman construction, or proof that the propagator scale is a Hamiltonian spectral gap | `RELATED_MECHANISM_RESULT / NOT_A_CLAY_SOLUTION_CLAIM` |
| Kirk | Exact Zenodo `18824739` v1.0 bytes bound by source record | 4D `SU(2)` lattice-to-continuum program conditional on unproved `WC1–WC3`; companion record retains an open mass-scaling bound | Single-group scope and load-bearing unproved hypotheses prevent unconditional universal Clay acceptance | `CONDITIONAL_CLAIM / NOT_ACCEPTED_FOR_CLAY_TARGET` |
| Jacobsen | Exact arXiv `2506.00284v1` source bytes bound; v2 withdrawal preserved as provenance only | `SU(3)`-only claimed construction; three proof sketches and populated references exist, but proof completeness and source traceability are unverified | Universal-group scope is not met; regulator-to-pure-4D bridge and claimed estimates remain unverified | `QUARANTINED_CLAIM / PROOF_COMPLETENESS_UNVERIFIED_AND_OUTSIDE_FULL_CLAY_GROUP_SCOPE` |
| Legacy `CLAIM-2024-001 — Sky Yang` | No primary artifact, identifier, URL, title, quote, imported source, or hash recovered from bounded repository history; external `Sky Yang Cao / Sky Cao` remains an unproven lead | Row first appears as a generic internal screening entry in `d9fc71a`; no later Git revision supplies source identity | No claim artifact is identifiable; no solution claim can be audited or promoted; historical row must remain preserved | `UNRESOLVED_ORPHANED_LEGACY_CLAIM / NOT_ACCEPTED_PROVENANCE_INSUFFICIENT` |

## Synthesis result

- No one of the four records supplies an accepted solution of the Clay target.
- No unsupported solution claim is promoted.
- The three exact external artifacts remain byte-bound and quarantined or mechanism-classified according to their actual scope.
- The Sky Yang row is formally dispositioned as an unresolved orphan after bounded provenance recovery; it is not silently mapped to Sky Cao or any other artifact.
- Historical `154` versus reproducible `152` test-count records remain unchanged.

This is the final E3 technical synthesis. Candidate-bound independent E4 closeout review is required before changing `YM-002E` to `INDEPENDENTLY_VERIFIED / CLOSED` or releasing `YM-002F`.
