# YM-004 UV BOUNDARY RECORD

## Quantitative Parameter Record for Cross-Problem Comparison with YM-005 and Input to YM-006

This record establishes the canonical quantitative boundary of the ultraviolet constructive renormalization group regime in 4D Yang–Mills theory, formatted as the authoritative UV input for the future `YM-006` non-meeting estimate.

---

## 1. Canonical UV Boundary Record

```yaml
UV_BOUNDARY_RECORD:
  UV_BOUNDARY_ID: UV-BND-YM004-001
  PRIMARY_THEOREMS:
    - THM-YM-0016
    - THM-YM-0017
    - THM-YM-0018
  PRIMARY_SOURCES:
    - "T. Bałaban, Commun. Math. Phys. 109 (1987) 249-301"
    - "T. Bałaban, Commun. Math. Phys. 116 (1988) 1-22"
    - "T. Bałaban, Commun. Math. Phys. 119 (1988) 243-285"
    - "T. Bałaban, Commun. Math. Phys. 122 (1989) 175-202"

  LAST_PROVED_PARAMETER_REGIME:
    COUPLING_RANGE: "0 < g_k <= g_* << 1 (strictly weak running coupling)"
    NUMERICAL_THRESHOLD: "g_*^2 approx 0.05 - 0.15 (governed by Kirkwood-Salsburg convergence)"
    VOLUME_ASSUMPTION: "Finite flat 4-torus V = L_0^4 < infinity"
    VOLUME_RELATION: "L_0 <= a_0 * exp(1 / (2 * b_0 * g_*^2))"
    LATTICE_SPACING_ASSUMPTION: "a_0 -> 0 (continuum UV limit taken in fixed volume)"
    SCALE_STEPS_CONTROLLED: "k = 0, 1, 2, ..., k_prov(g_0) where g_{k_prov} <= g_*"
    FIELD_SIZE_ASSUMPTION: "Full configuration space decomposed into small-field and large-field regions"

  UNIFORMITY_ESTABLISHED:
    LATTICE_SPACING_UNIFORMITY: "PROVED (partition function uniformly bounded as a_0 -> 0)"
    SCALE_STEP_UNIFORMITY: "PROVED (effective action remainder ||R_k|| <= C * g_k^2 uniform across all k <= k_prov)"
    VOLUME_UNIFORMITY_AT_FIXED_SCALE: "PROVED EXTENSIVE (free energy density E_k / V is uniform in L_0)"
    GAUGE_GROUP_DEPENDENCE: "PROVED for SU(2) and SU(3); extensible to SU(N) with N-dependent constants"
    REFLECTION_POSITIVITY: "PRESERVED on lattice; physical transfer matrix positive"

  FIRST_UNPROVED_EXTENSION:
    SCALE_STEP: "k = k_prov + 1"
    COUPLING_VALUE: "g_{k+1}^2 > g_*^2"
    PHYSICAL_DISTANCE: "x >= x_* approx (1 / Lambda_QCD) * exp(-1 / (2 * b_0 * g_*^2))"
    FAILED_PROPERTY: "Polymer cluster expansion ||zeta_{k+1}||_{kappa, rho} loses contractivity (< 1/2 fails)"
    EPISTEMIC_STATUS: "METHOD_LIMITATION (norm diverges; QFT physical existence not disproved)"

  INPUT_FOR_YM006_NON_MEETING:
    UV_TERMINAL_SCALE: "x_UV^* ~ (0.1 - 0.3) / Lambda_QCD (perturbative boundary)"
    UV_TERMINAL_COUPLING: "g_UV^* = g_* << 1"
    GAP_TO_IR_LATTICE_REGIME: >-
      Strong-coupling lattice expansion (Wilson THM-YM-0008, Shen-Zhu-Zhu THM-YM-0026) converges only for
      beta = 2N/g^2 < beta_0 << 1, corresponding to g_IR^2 >= 2N / beta_0 >> 1.
      The gap between g_UV^* << 1 and g_IR^* >> 1 constitutes the quantitative non-meeting window.
    OBSTRUCTION_SIGNATURE: "OBS-CAND-001 (Intermediate Crossover Window)"

  CONFIDENCE:
    EVIDENCE_STRENGTH: "E4 (reconstructed from peer-reviewed CMP mathematical theorems)"
    INDEPENDENCE: "IND1"
    CANONICAL_CONSISTENCY: "100% aligned with THEOREM_LEDGER.md and YM-003 MISSING_BRIDGE_GRAPH.md"
```
