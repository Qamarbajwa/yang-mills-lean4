# Canonical Strategy Record: STRAT-REC-YM008-001

- **RECORD_ID:** `STRAT-REC-YM008-001`
- **GOVERNANCE_TIER:** `R2`
- **DATE:** 2026-09-22
- **ACTIVE_CONTRACT:** `CONTRACT-YM-008`
- **MANDATE:** Multi-Scale Hybrid Attack Strategy for the 4D Yang–Mills Crossover Window

---

## 1. Canonical Strategy Overview

```yaml
canonical_strategy_record:
  id: "STRAT-REC-YM008-001"
  architecture_name: "Governed Multi-Scale Hybrid Attack Strategy"
  target_problem: "Clay Millennium Problem #4 (4D Yang-Mills Existence and Mass Gap)"
  clay_millennium_problem_status: "OPEN_AND_UNSOLVED"
  strategy_classification: "MULTI_SCALE_HYBRID_HYPOTHESIS"
  adversarial_falsification_status: "SURVIVED_WITH_GUARDRAILS"
  scale_partition:
    scale_1_uv:
      range: "0 < x <= 0.15 fm (k >= 1.3 GeV)"
      machinery: "Bałaban Multiscale RG + Lüscher Wilson Flow"
      primary_role: "UV operator regularity and contractive small-field effective actions"
      provenance: "PRIMARY_SOURCE_RESULT"
    scale_2_crossover:
      range: "0.15 fm <= x <= 0.50 fm (g_k ~ 1, beta ~ 1 - 2)"
      machinery: "Semidefinite Programming (SDP) Lattice Loop Bootstrap"
      primary_role: "Non-perturbative bounds on gauge-invariant Wilson loop correlators"
      provenance: "PRIMARY_SOURCE_RESULT"
    scale_3_ir:
      range: "x >= 0.50 fm (k <= Lambda_QCD)"
      machinery: "Topological Center-Vortex Percolation + Transfer Matrix Cluster Expansion"
      primary_role: "Area-law confinement and exponential spectral clustering"
      provenance: "PRIMARY_SOURCE_RESULT"
  interfaces:
    interface_uv_crossover:
      boundary_location: "x ~ 0.15 fm"
      matching_mechanism: "Flow-Regularized Wilson Loops W_t(C) with joint scaling t(a) = c_0 a^2"
      invariants_preserved: ["Manifest Gauge Invariance", "Continuum OS3 Reflection Positivity"]
    interface_crossover_ir:
      boundary_location: "x ~ 0.50 fm"
      matching_mechanism: "SDP string tension bounds matched to vortex insertion free energy"
      invariants_preserved: ["Transfer Matrix Positivity", "Area-Law Decay"]
```

---

## 2. Quantitative Constants and Parameter Provenance

| Parameter / Scale | Symbolic Bound | Calibrated Value | Provenance Tag | Source / Derivation | Epistemic Guardrail |
|---|---|---|---|---|---|
| UV scale boundary | $x_{\text{UV}}^*$ | $\approx 0.15\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Bałaban weak-coupling limit $g_* \approx 0.28$ | Weak-coupling perturbation validity limit |
| Crossover window | $\Delta x = a_{\text{strong}}^* - x_{\text{UV}}^*$ | $\ge 0.35\text{ fm}$ | `PROJECT_ESTIMATE` | Computed in Task YM-006 | Physical non-meeting gap to be bridged |
| IR scale boundary | $a_{\text{strong}}^*$ | $\ge 0.50\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Osterwalder–Seiler radius $\beta_0 \approx 0.25$ | Strong-coupling expansion convergence limit |
| Joint scaling constant | $c_0 = t / a^2$ | $\mathcal{O}(0.01 - 0.1)$ | `PROJECT_ESTIMATE` | Flow regularization condition | Must satisfy $t \to 0$ as $a \to 0$ |
| Flow scale | $\sqrt{8t_0}$ | $\approx 0.48\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | FLAG 2021 / Lüscher reference scale | Reference length benchmark |
| String tension | $\sqrt{\sigma}$ | $\approx 440\text{ MeV}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Experimental Regge slope | Pure gauge string tension |
| Glueball mass gap | $M_{0^{++}}$ | $\approx 1.5 - 1.7\text{ GeV}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Lattice QCD glueball spectrum | Expected physical scalar glueball mass |

---

## 3. Epistemic Invariants Maintained

1. **Clay Problem Status:** `OPEN_AND_UNSOLVED`.
2. **Strategy Characterization:** Advanced mathematical hypothesis and synthesis; not an unverified claim of solution.
3. **Guardrail Integrity:** All 4 adversarial guardrails (joint scaling, gauge-invariant observables, relaxed SDP constraints, asymptotic entropy balance) are mandatory.
