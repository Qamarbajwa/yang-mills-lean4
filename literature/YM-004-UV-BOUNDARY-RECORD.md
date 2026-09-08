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
    NUMERICAL_THRESHOLD: "g_k <= g_* << 1 (symbolic small-coupling threshold; implicit/non-constructive positive constant in primary theorems satisfying polymer contractivity; no canonical numerical constant is published in CMP papers)"
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
    PHYSICAL_DISTANCE: "x >= x_* ~ c_* / Lambda_QCD (symbolic physical scale where g_k reaches g_*)"
    FAILED_PROPERTY: "Polymer cluster expansion ||zeta_{k+1}||_{kappa, rho} loses established contractivity bound"
    EPISTEMIC_STATUS: "METHOD_LIMITATION (sufficient contractivity bound lost; QFT physical existence not disproved)"

  INPUT_FOR_YM006_NON_MEETING:
    UV_TERMINAL_SCALE: "x_UV^* ~ c_* / Lambda_QCD (symbolic perturbative boundary scale; c_* is dimensionless constant)"
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

---

## 2. Quantitative Parameter Provenance Audit Table

| Quantity / Constant | Stated Value / Expression | Classification | Provenance & Literature Basis | Rigorous Mathematical Status |
|---|---|---|---|---|
| **Small-coupling threshold** | $g_*^2 \approx 0.08$ | `PROJECT_ESTIMATE` | Estimated from standard leading-order tree-graph condition $g_*^2 \approx \kappa_1 / (\ln C_4 + 1)$. | **NOT IN PRIMARY SOURCES.** Primary CMP theorems establish strictly symbolic existence: $\exists g_* > 0$ sufficiently small. |
| **Weak-coupling domain** | $g_*^2 \sim 0.05 - 0.15$ | `PROJECT_ESTIMATE` | Typical heuristic range where small-field Gaussian Hessian dominates non-Gaussian perturbations. | **NOT IN PRIMARY SOURCES.** No numerical range is published in Bałaban's CMP series. |
| **UV terminal physical distance** | $x_{\text{UV}}^* \approx 0.15\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Computed from $x \sim \hbar c / \mu$ using phenomenological $\Lambda_{\text{QCD}} \approx 250\text{ MeV}$. | **NOT A MATHEMATICAL BOUND.** The Clay problem is formulated without external physical dimensionful inputs. |
| **Intermediate crossover scale** | $x \sim 0.2 - 1.0\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Phenomenological hadronic confinement scale / string tension radius ($\sim 1\text{ fm}$). | **HEURISTIC PHYSICS ESTIMATE.** Not part of constructive functional analytic bounds. |
| **Lattice strong-coupling radius** | $a_{\text{lattice}} \ge 0.5\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Physical lattice spacing corresponding to $\beta \le \beta_0 \approx 0.39$ for $SU(2)$. | **PHENOMENOLOGICAL TRANSLATION.** Mathematical theorems bound $\beta \le \beta_0$, not physical length in fm. |

> [!IMPORTANT]
> **Provenance Invariant:**
> The primary constructive literature (Bałaban CMP 95–122, Federbush CMP 107–127, MRS CMP 155) establishes strictly **symbolic bounds** ($g_k \le g_* \ll 1$, $\beta \le \beta_0 \ll 1$). All specific decimal values and femtometer lengths are project estimates or heuristic physical translations. They are strictly barred from acting as load-bearing mathematical evidence.
