# Task YM-007: Evaluation of Candidate Mechanism 5 — Functional / Exact Renormalization Group (ERG)

- **MECHANISM_ID:** `MECH-05`
- **FRAMEWORK:** Functional / Exact Renormalization Group (Wetterich Flow Equations)
- **CANONICAL_REFERENCES:** Wilson & Kogut (1974), Polchinski (1984), Wetterich (Phys. Lett. B 1993), Reuter & Wetterich (1994), Pawlowski et al. (Ann. Phys. 2006, 2018)
- **STATUS:** `TRANSFERABLE_METHODOLOGY` (Continuum Non-Perturbative Flow) / `STRUCTURAL_OBSTRUCTION` (Unbounded Truncation Error & Modified Ward Identities)

---

## 1. Mathematical Formulation

The Functional (or Exact) Renormalization Group (ERG) tracks the scale dependence of the **scale-dependent average effective action** $\Gamma_k[\Phi]$, which interpolates between the bare action $S$ at the microscopic UV scale $k = \Lambda_{\text{UV}}$ and the full quantum 1PI effective action $\Gamma$ in the physical infrared limit $k \to 0$.

### The Wetterich Equation (1993)
The scale evolution of $\Gamma_k$ is governed by a formally exact, one-loop-like functional differential equation:

$$\boxed{\partial_k \Gamma_k = \frac{1}{2} \text{Tr} \left[ \left( \Gamma_k^{(2)} + R_k \right)^{-1} \partial_k R_k \right]}$$

where:
- $\Gamma_k^{(2)}[\Phi] = \frac{\delta^2 \Gamma_k}{\delta \Phi \delta \Phi}$ is the full field-dependent Hessian (second functional derivative),
- $R_k(p)$ is an infrared regulator function providing mass-like suppression for modes with momenta $p^2 < k^2$ and vanishing identically as $k \to 0$,
- $\text{Tr}$ denotes a complete trace over spacetime coordinates, Lorentz indices, and gauge group generators.

---

## 2. Non-Perturbative Achievements in Yang–Mills

1. **Seamless Scale Traversal:**
   Unlike perturbative RG, the Wetterich equation does not diverge as $g_k$ grows; the regulator $R_k$ provides an effective infrared mass that suppresses infrared Landau pole singularities at finite $k$.
2. **Dynamical Gluon Mass Generation (Decoupling Solution):**
   In Landau gauge, non-perturbative truncations of the gluon and ghost Schwinger–Dyson / ERG flows show that the gluon propagator saturates at zero momentum:
   $$D_{\mu\nu}^{ab}(p) = \delta^{ab} \left( \delta_{\mu\nu} - \frac{p_\mu p_\nu}{p^2} \right) \frac{1}{p^2 + m_g^2(p^2)}$$
   with a dynamically generated screening mass $m_g(0) \approx 500\text{--}600\text{ MeV}$, consistent with lattice simulations.
3. **Ghost Confinement:**
   The ghost dressing function remains non-zero and infrared finite (decoupling scenario) or divergent (scaling scenario), signaling the absence of free asymptotic gluon states.

---

## 3. Evaluation Against the Eight Rigorous Criteria

| Criterion ID | Criterion | Score | Mathematical Analysis & Evidence |
|---|---|---|---|
| **`CRIT-01`** | Gauge Invariance | **COMPROMISED** | The regulator $R_k$ breaks manifest local gauge invariance; standard Ward–Takahashi identities become modified Slavnov–Taylor identities (mSTI). |
| **`CRIT-02`** | Reflection Positivity (OS3) | **FAIL** | Regulators $R_k$ violate reflection positivity at finite $k$. In truncated solutions at $k = 0$, gluon spectral functions $\rho(m^2)$ frequently contain negative or complex weight regions. |
| **`CRIT-03`** | Crossover Control | **NUMERICAL PASS / ANALYTICAL FAIL** | Traverses $k \sim \Lambda_{\text{QCD}}$ smoothly in numerical projections, but lacks contractive analytical convergence. |
| **`CRIT-04`** | Continuum Limit ($a \to 0$) | **CONJECTURED** | Formulated directly in the continuum; but existence of the flow trajectory in a Banach space of functionals is unproved. |
| **`CRIT-05`** | Thermodynamic Limit ($V \to \infty$) | **PASS** | Continuous momentum space integration is infinite-volume by definition. |
| **`CRIT-06`** | Non-Triviality | **PASS** | Non-trivial non-perturbative interaction vertices. |
| **`CRIT-07`** | Spectral Mass Gap ($\Delta > 0$) | **HEURISTIC** | Euclidean gluon screening mass $m_g > 0$ does not mathematically prove a spectral gap for physical gauge-invariant states in $\mathcal{H}$. |
| **`CRIT-08`** | Contractive Error Control | **FATAL FAIL** | No rigorous error bounds exist for operator truncations in the non-perturbative regime. |

---

## 4. Mathematical Barrier Localization

> [!CAUTION]
> **The Two Insuperable Barriers of Truncated ERG:**
> 1. **The Truncation Error Chasm:**
>    To extract concrete numbers from the Wetterich equation, one must truncate $\Gamma_k$ to a tractable finite ansatz:
>    $$\Gamma_k[A] = \int d^4x \left\{ \frac{Z_k}{4} F_{\mu\nu}^2 + \sum_{n=3}^N \Gamma_{k}^{(n)} A^n + \dots \right\}$$
>    In constructive quantum field theory (e.g. Bałaban or Osterwalder–Seiler), every expansion is accompanied by an absolute bound $\| \text{Remainder} \| \le C \epsilon^n$ with $C < 1$.
>    In functional ERG, **no contractive error theorem exists**. In the crossover region $k \sim \Lambda_{\text{QCD}}$, the coupling is of order unity ($g_k \sim 1$), meaning all operators in the infinite tower have comparable magnitude. Truncating at order $N$ introduces uncontrolled systematic errors that cannot be bounded.
>
> 2. **The Gauge-Regulator Conflict (mSTI Violation):**
>    A momentum regulator $R_k(p^2)$ depends on ordinary derivatives, not covariant derivatives $D_\mu$. Thus:
>    $$\delta_{\text{gauge}} S_{\text{reg}}[A; R_k] \ne 0$$
>    Gauge invariance is broken at all intermediate scales $k > 0$. Restoring gauge invariance as $k \to 0$ requires solving the modified Slavnov–Taylor identities (mSTI). However, truncating the action at $N$ points inevitably violates the mSTI at order $N+1$, leaving the physical limit polluted by unphysical longitudinal modes and ghost violations.

---

## 5. Epistemic Classification

$$\boxed{\textbf{CLASSIFICATION: } \text{TRANSFERABLE\_METHODOLOGY (Continuum RG Flow) with STRUCTURAL\_OBSTRUCTION (Unbounded Truncation Error)}}$$

- **Transferable Value:** High for generating physical intuition, computing non-perturbative propagators, and modeling crossover dynamics.
- **Clay Sufficiency:** **NO**. Functional ERG cannot provide a mathematically rigorous proof of the Yang–Mills existence and mass gap because it lacks a rigorous functional-analytic framework for controlling truncation errors and regulator-induced gauge violations.
