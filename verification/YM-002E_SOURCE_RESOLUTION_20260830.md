# YM-002E — Source-Resolution and Adversarial Triage Addendum

- Date: `2026-08-30`
- Task: `YM-002E`
- Base scientific candidate: `299871d70d77dd37526bfd12555d090b49111980`
- Purpose: Resolve exact primary-artifact identities for the three quarantined queue entries without treating search results as proof.
- Method: Exact-name/title and identifier searches across primary repositories and author/deposit records. No local full text was ingested in this pass; consequently this addendum records source resolution and scope triage, not theorem verification.

## CLAIM-2024-001 — Sky Yang, 2024

- Resolution: `SOURCE_IDENTITY_UNRESOLVED`.
- No matching Yang–Mills primary manuscript, DOI, arXiv identifier, version, URL, or content hash was located for the exact author string and year supplied by the internal register.
- Search hits for other people named Sky Yang, and unrelated Yang–Mills papers by authors with similar names, are not identity matches and are not bound to this claim.
- Disposition: `QUARANTINED`; existing result `NOT_ACCEPTED_PROVENANCE_INSUFFICIENT` remains unchanged.

## CLAIM-2025-001 — Various preprints / truncated Schwinger–Dyson claim

- Resolution: `QUEUE_IDENTITY_UNRESOLVED`; the register still supplies no author, title, identifier, version, or hash.
- Non-bound relevant primary lead: Ferreira, Papavassiliou, Pawlowski, and Wink, *Physics of the gluon mass gap*, arXiv:2508.20568, DOI `10.1140/epjc/s10052-025-15027-7`.
- The paper studies a Landau-gauge gluon-propagator mass scale and functional/DSE observables. It explicitly uses an approximation dropping two-loop terms in one DSE calculation and defines its `m_gap` as a screening-type scale associated with a propagator singularity.
- Scope triage: this is not an identified match to the internal queue entry and does not, on the cited record, supply a universal compact-simple-group construction of pure Yang–Mills on `R^4` satisfying the required OS/Wightman obligations and spectral-gap theorem.
- Disposition: `NOT_BOUND / NOT_ACCEPTED`; the queue entry remains quarantined pending exact source identity and proof-level audit.

## CLAIM-2026-001 — Various preprints / finite-lattice continuum claim

- Resolution: `QUEUE_IDENTITY_UNRESOLVED`; the register still supplies no author, title, identifier, version, or hash.
- Non-bound relevant primary lead: Harold D. Kirk, *From Lattice Mass Gap to Continuum SU(2) Yang–Mills Theory: O(4) Restoration and Osterwalder–Schrader Reconstruction*, Zenodo record `18824739`, version `v1.0`, published `2026-03-01`.
- The deposit describes a four-dimensional `SU(2)` construction whose results are conditional on weak-coupling hypotheses `WC1–WC3`. A companion deposit states that a matching upper bound on the lattice mass gap remains open for obtaining a non-trivial continuum theory with finite mass gap.
- Scope triage: conditional hypotheses, a single gauge group, and an unresolved finite-mass scaling condition do not meet the universal, unconditional Clay target. The lead is therefore not accepted as a solution and is not silently substituted for the unnamed queue entry.
- Disposition: `NOT_BOUND / NOT_ACCEPTED`; the queue entry remains quarantined pending exact source identity and full artifact audit.

## Additional separate lead requiring intake, not retroactive assignment

- D. C. Jacobsen, *A Constructive Proof of Existence and Mass Gap for Pure SU(3) Yang-Mills in Four-Dimensional Space-Time*, arXiv:2506.00284.
- The abstract claims a `SU(3)` result and describes an embedding as the zero-mode sector of a five-dimensional orbifold regulator. It is not assigned to any existing queue row because the current register does not identify it.
- Immediate boundary: a `SU(3)`-only result does not discharge the universal “any compact simple gauge group” obligation; the regulator-to-target equivalence would also require a full artifact-level audit.
- Disposition: `UNASSIGNED_LEAD / QUARANTINED`.

## Triage conclusion

- Exact source identity is still missing for all three internal queue rows.
- All identified leads fail at least one mandatory boundary on the available primary record: missing identity, conditional hypotheses, single-group scope, approximation/truncation, or unresolved continuum/spectral control.
- No unsupported solution claim is accepted. `YM-002E` remains `RELEASED_IN_PROGRESS`; downstream tasks remain blocked.

## Primary source links

- https://arxiv.org/abs/2508.20568
- https://zenodo.org/records/18824739
- https://zenodo.org/records/18825033
- https://arxiv.org/abs/2506.00284

## Byte-level binding result

The three requested artifact records are now locally byte-bound:

| Source ID | Local SHA-256 | Server hash/status |
|---|---|---|
| `SRC-YM-002E-FERREIRA-2508.20568-v1` | `7c78d18c6e6222d114a05c3852b3814f45e15261fc97d336dcd0f9df46db5c30` | arXiv server SHA not exposed |
| `SRC-YM-002E-KIRK-ZENODO-18824739-v1.0` | `13b9fc8cb7109f8f55cca7b285417458bd9a2b99faccf11bc483f25d26fcd3e1` | MD5 reconciled: `f5c2be4b71128a384d6509747f1b7dee` |
| `SRC-YM-002E-JACOBSEN-2506.00284-v1` | `f97569b3bd122de923d6d7a642ec24bcccb319f8e215fa1f6f4781a241efcf51` | arXiv server SHA not exposed |

These records resolve the three artifact leads named in the continuation request. They do not rewrite the existing internal `CLAIM-2024-001 — Sky Yang` row, which remains a separate unresolved queue item pending its own exact source identity.
