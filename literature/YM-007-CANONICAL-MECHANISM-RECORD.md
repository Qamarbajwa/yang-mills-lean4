# Canonical Mechanism Record: MECH-REC-YM007-001

- **RECORD_ID:** `MECH-REC-YM007-001`
- **GOVERNANCE_TIER:** `R2`
- **DATE:** 2026-09-22
- **ACTIVE_CONTRACT:** `CONTRACT-YM-007`
- **MANDATE:** Evaluation of Novel Theoretical Mechanisms for the Intermediate Crossover Window

---

## 1. Canonical Record Overview

```yaml
canonical_mechanism_record:
  id: "MECH-REC-YM007-001"
  crossover_window: "g_k ~ 1, beta ~ 1 - 2, Delta x >= 0.35 fm"
  overall_status: "CROSSOVER_UNBRIDGED_CANDIDATE_FRAMEWORKS_CATALOGED"
  clay_millennium_problem_status: "OPEN_AND_UNSOLVED"
  number_of_evaluated_mechanisms: 5
  evaluations:
    - mechanism_id: "MECH-01"
      name: "Geometric / Gradient Flow on Gauge Orbit Space"
      primary_authors: "Lüscher (2010), Lüscher & Weisz (2013)"
      classification: "TRANSFERABLE_METHODOLOGY"
      clay_sufficient: false
      key_strength: "UV-finite composite operator smearing without extra renormalization"
      fatal_barrier: "Flow parameter t > 0 violates OS3 reflection positivity; t -> 0 reintroduces unbridged crossover"
      provenance: "PRIMARY_SOURCE_RESULT"

    - mechanism_id: "MECH-02"
      name: "Stochastic Quantization & Regularity Structures"
      primary_authors: "Parisi & Wu (1981), Hairer (2014), Chandra, Hairer & Shen (2022, 2024), Chevyrev & Shen (2026)"
      classification: "TRANSFERABLE_METHODOLOGY"
      clay_sufficient: false
      key_strength: "Rigorous 2D invariant measure proof and 3D gauge-covariant counterterm uniqueness"
      fatal_barrier: "Local subcriticality fails in 4D (alpha < -3); infinite tree divergence at critical dimension"
      provenance: "PRIMARY_SOURCE_RESULT"

    - mechanism_id: "MECH-03"
      name: "Loop Space, Makeenko–Migdal Equations & Large-N Bootstrap"
      primary_authors: "Makeenko & Migdal (1979), Kazakov & Zheng (2023, 2024)"
      classification: "TRANSFERABLE_METHODOLOGY"
      clay_sufficient: false
      key_strength: "Manifest gauge invariance; rigorous non-perturbative SDP bounds across all beta"
      fatal_barrier: "Singular contact terms in 4D continuum loop Laplacian; finite-N Mandelstam entanglement"
      provenance: "PRIMARY_SOURCE_RESULT"

    - mechanism_id: "MECH-04"
      name: "Topological Condensation & Center Vortices / Monopoles"
      primary_authors: "'t Hooft (1978), Mack & Petkova (1979), Mandelstam (1976)"
      classification: "CONJECTURED_PATHWAY"
      clay_sufficient: false
      key_strength: "Intuitive physical mechanism for area-law confinement via center flux disordering"
      fatal_barrier: "Singular 2D vortex sheets carry divergent action in 4D continuum; area law != local spectral gap"
      provenance: "PRIMARY_SOURCE_RESULT"

    - mechanism_id: "MECH-05"
      name: "Functional / Exact Renormalization Group (ERG)"
      primary_authors: "Wetterich (1993), Reuter & Wetterich (1994), Pawlowski et al. (2006)"
      classification: "TRANSFERABLE_METHODOLOGY"
      clay_sufficient: false
      key_strength: "Smooth scale interpolation connecting asymptotic freedom to IR gluon screening mass"
      fatal_barrier: "Regulator breaks gauge invariance (mSTI); unquantifiable truncation errors in crossover window"
      provenance: "PRIMARY_SOURCE_RESULT"
```

---

## 2. Quantitative Constants and Parameter Provenance

| Parameter / Constant | Mathematical Symbol | Value / Bound | Provenance Tag | Source / Derivation | Epistemic Guardrail |
|---|---|---|---|---|---|
| Crossover window | $[g_{\text{UV}}^*, g_{\text{IR}}^*]$ | $\approx [0.20, 4.0]$ | `PROJECT_ESTIMATE` | Derived in YM-006 from Bałaban $g_*$ and Osterwalder–Seiler $\beta_0$ | Intermediate coupling window where all expansions diverge |
| Lüscher reference scale | $t_0$ | $t^2 \langle E(t) \rangle \|_{t=t_0} = 0.3$ | `PRIMARY_SOURCE_RESULT` | Lüscher (JHEP 08 (2010) 071) | Pure lattice/continuum convention; not physical length |
| Lüscher scale in physical units | $\sqrt{8t_0}$ | $\approx 0.48\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Flavour Lattice Averaging Group (FLAG 2021) | Heuristic phenomenological conversion using $r_0 \approx 0.5\text{ fm}$ |
| Stochastic critical scaling | $\alpha_{\text{white noise}}$ | $< -\frac{d+2}{2} = -3$ | `PRIMARY_SOURCE_RESULT` | Hairer (2014) parabolic Besov regularity in 4D | Proof that local subcriticality fails in 4D |
| Dynamic gluon mass scale | $m_g(0)$ | $\approx 500 - 600\text{ MeV}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Non-perturbative ERG / Landau gauge lattice | Non-perturbative screening mass in unphysical gauge |
| String tension | $\sigma$ | $\approx (440\text{ MeV})^2 \approx 1\text{ GeV/fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Phenomenological Regge trajectory / lattice potential | Pure gauge string tension benchmark |

---

## 3. Epistemic Invariants Maintained

1. **Clay Problem Status:** `OPEN_AND_UNSOLVED`.
2. **Zero Overclaim Invariant:** None of the 5 mechanisms evaluated is claimed to prove the existence of 4D quantum Yang–Mills theory or the mass gap.
3. **Barrier Localization:** Every mechanism has its primary mathematical point of failure explicitly identified.
