# Task YM-007: Comparative Mechanism Evaluation Matrix

- **TASK_ID:** `YM-007`
- **GOVERNANCE_TIER:** `R2`
- **DATE:** 2026-09-22

---

## 1. Comprehensive Evaluation Matrix

The table below summarizes the evaluation of the five candidate non-perturbative frameworks across the eight rigorous mathematical criteria established in `YM-007-EVALUATION-FRAMEWORK.md`:

| Mechanism ID | Framework Name | CRIT-01 Gauge Inv. | CRIT-02 OS3 Positivity | CRIT-03 Crossover Control | CRIT-04 Continuum ($a \to 0$) | CRIT-05 Thermo. ($V \to \infty$) | CRIT-06 Nontrivial | CRIT-07 Mass Gap ($\Delta > 0$) | CRIT-08 Error Control | CLAY SUFFICIENT | Epistemic Classification |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **`MECH-01`** | **Geometric / Gradient Flow** | PASS | FAIL | FAIL | PARTIAL | PASS | PASS | FAIL | PASS | **NO** | `TRANSFERABLE_METHODOLOGY` (Smearing) / `STRUCTURAL_OBSTRUCTION` (Measure) |
| **`MECH-02`** | **Stochastic Quantization SPDEs** | PARTIAL | UNKNOWN | FAIL | FAIL (4D) | FAIL (4D) | PASS | FAIL | FAIL (4D) | **NO** | `TRANSFERABLE_METHODOLOGY` (2D/3D) / `STRUCTURAL_OBSTRUCTION` (4D Criticality) |
| **`MECH-03`** | **Loop Space & Large-$N$ Bootstrap** | PASS | PARTIAL | PARTIAL | FAIL (Cont.) | PASS | PASS | CONJECTURED | PARTIAL | **NO** | `TRANSFERABLE_METHODOLOGY` (Lattice SDP) / `STRUCTURAL_OBSTRUCTION` (Contact Div.) |
| **`MECH-04`** | **Topological Condensation** | PARTIAL | PASS (Lat.) | CONJECTURED | FAIL (Cont.) | PASS (Lat.) | PASS | CONJECTURED | FAIL | **NO** | `CONJECTURED_PATHWAY` (Functionally Incomplete) |
| **`MECH-05`** | **Functional / Exact RG (ERG)** | COMPROMISED | FAIL | PARTIAL | CONJECTURED | PASS | PASS | HEURISTIC | FATAL FAIL | **NO** | `TRANSFERABLE_METHODOLOGY` (Flow) / `STRUCTURAL_OBSTRUCTION` (Truncation) |

---

## 2. Failure Locality and YM-003 DAG Reconciliation

Every mechanism breaks down at a specific, localized point in the YM-003 missing-bridge graph:

| Mechanism | Primary Mathematical Barrier | Failure Locality | Intercepted Edge in YM-003 | Obstruction Reconciliation |
|---|---|---|---|---|
| **`MECH-01`** | Flow time $t > 0$ introduces non-local averaging violating OS3; sending $t \to 0$ recovers singular unbridged crossover. | Auxiliary flow time boundary ($t \to 0$) | `E-CROSSOVER` | Does not generate measure; transports existing unbridged measure. |
| **`MECH-02`** | Spacetime white noise regularity $\alpha < -3$ in 4D causes tree diagram explosion; Hairer local subcriticality fails. | 4D critical scaling dimension ($D=4$) | `E-UV-RG` $\to$ `N-INT-COUPLING` | Fails at critical dimension before reaching the crossover scale. |
| **`MECH-03`** | Loop space Laplacian produces singular contact terms $\delta^{(4)}(x - y)$ when curves self-intersect; finite-$N$ Mandelstam entanglement. | Continuum loop geometry ($a \to 0$, finite $N$) | `E-LATTICE-CONT` | Discretized SDP bounds cannot take continuum limit without contact counterterms. |
| **`MECH-04`** | Singular 2D vortex sheets carry divergent 4D Yang–Mills action; area law $\sigma > 0$ does not imply local spectral gap $\Delta > 0$. | Continuum vortex sheet thickness ($a \to 0$) | `E-STRONG-MASS-GAP` $\to$ `N-MASS-GAP` | Area law for non-local loops does not prove spectral gap for local gauge-invariant operators. |
| **`MECH-05`** | Momentum cutoff regulator $R_k$ breaks gauge invariance (mSTI); derivative expansion has zero proved contractivity bounds at $g_k \sim 1$. | Crossover scale truncation ($k \sim \Lambda_{\text{QCD}}$) | `E-CROSSOVER` | Inability to establish error bounds $\| \Gamma_k^{\text{true}} - \Gamma_k^{\text{trunc}} \| < \epsilon$. |

---

## 3. Comparative Synthesis & Transferable Value

While **no single candidate mechanism resolves the intermediate crossover window**, each contributes distinct, high-value mathematical machinery that can be salvaged for hybrid constructive strategies:

1. **Gradient Flow (`MECH-01`):** Provides the definitive tool for non-perturbative operator renormalization and UV-finite composite observable construction.
2. **Stochastic Quantization (`MECH-02`):** Establishes the rigorous mathematical standard for gauge-covariant stochastic counterterms, providing the blueprint for lower-dimensional and regulated models.
3. **Loop Bootstrap (`MECH-03`):** Yields the only non-perturbative, non-Monte-Carlo numerical bounding technique capable of constraining observables across all coupling regimes simultaneously.
4. **Topological Defects (`MECH-04`):** Identifies the physical degree of freedom (center flux condensation) responsible for the mass scale $\Lambda_{\text{QCD}}$.
5. **Functional RG (`MECH-05`):** Provides the continuous scale-dependent framework connecting the asymptotic freedom UV flow to the IR screening mass.
