# Task YM-012: Reconciled 19-Edge Missing-Bridge Dependency Graph

- **TASK_ID:** `YM-GOV-012`
- **GOVERNANCE_TIER:** `R2` (Scientific Recovery and Proof-Dependency Repair)
- **DATE:** 2026-09-22
- **TARGET_STATUS:** Independent Audit and Epistemic Reconciliation of the 19-Edge Graph

---

## 1. Executive Purpose & Epistemic Audit Grounding

Task `YM-003` originally formulated the 19-edge proof-dependency Directed Acyclic Graph (DAG) for the 4D Yang–Mills Existence and Mass Gap Problem. 

In Task `YM-010`, an overclaim was committed asserting that:
$$\text{"DAG COMPLETENESS: 100\% OF EDGES AND NODES TRACEABLY CLOSED"}$$
The emergency adversarial audit (`YM-GOV-011`) demonstrated that this claim was unfounded: passing repository unit tests and heuristic interface sketches did not constitute mathematical proof of edge closure.

This document establishes the **authoritative, reconciled, edge-by-edge audit** of all 19 edges in the missing-bridge graph. Every edge is classified strictly under the governed epistemic taxonomy:
- **`PROVED`**: Rigorously proved from first principles (strictly within its stated mathematical scope).
- **`REGULATED_ONLY`**: Mathematically established only in the presence of regularizations/cutoffs (e.g. lattice spacing $a > 0$, finite volume $L_0 < \infty$, or bare coupling restrictions).
- **`CONDITIONAL`**: Rigorous mathematical theorem in abstract axiomatic QFT whose physical hypotheses for 4D continuum Yang–Mills remain unproved.
- **`OPEN`**: Fundamentally unresolved non-perturbative or constructive problem.
- **`UNKNOWN`**: Insufficient mathematical clarity to classify.

---

## 2. Global Edge Status Summary

| Status Classification | Edge Count | Edge Identifiers |
|---|---|---|
| **`PROVED`** *(Strictly Perturbative Asymptotic Freedom in UV-Regularized Schemes)* | **2** | `E-UV-FREE` (`N-REG-LATTICE -> N-UV-FREE`), `E-UV-FREE-CONT` (`N-REG-CUTOFF -> N-UV-FREE`) |
| **`REGULATED_ONLY`** | **2** | `E-UV-RG`, `E-LATTICE-GAP` |
| **`CONDITIONAL`** | **5** | `E-SCHWINGER-OS2`, `E-OS-RECON`, `E-WIGHTMAN-VAC`, `E-WIGHTMAN-SPEC`, `E-GAP-CLUSTER` |
| **`OPEN`** | **10** | `E-CROSSOVER`, `E-LATTICE-CONT`, `E-THERMO`, `E-CONT-SCHWINGER`, `E-SCHWINGER-OS0`, `E-SCHWINGER-OS1`, `E-SCHWINGER-OS3`, `E-SCHWINGER-OS4`, `E-NONTRIV-WITNESS`, `E-GROUP-GEN` |
| **`UNKNOWN`** | **0** | — |
| **TOTAL** | **19** | **Full 19-Edge Load-Bearing DAG** |

> **Semantic Clarification (`YM-GOV-014` Section 6):**
> The two `PROVED` edges (`E-UV-FREE` and `E-UV-FREE-CONT`) establish **only perturbative 1-loop/2-loop asymptotic freedom** ($\beta_0 = \frac{11N}{48\pi^2} > 0$) from regulated starting nodes (`N-REG-LATTICE` and `N-REG-CUTOFF`) to `N-UV-FREE`. In particular, `E-UV-FREE-CONT` (`N-REG-CUTOFF -> N-UV-FREE`) is **perturbative asymptotic freedom in a UV-cutoff continuum renormalization scheme**, **never** non-perturbative continuum existence (`N-INT-COUPLING -> N-CONTINUUM-LIMIT`, which is `E-CONT-SCHWINGER = OPEN`).

---

## 3. Comprehensive Edge-by-Edge Audit Ledger

### Edge 1: `E-UV-FREE`
- **Source Node:** `N-REG-LATTICE`
- **Target Node:** `N-UV-FREE`
- **Mathematical Proposition:** Perturbative 1-loop and 2-loop beta-function coefficients are strictly negative ($\beta_0 = \frac{11N}{48\pi^2} > 0$ for $SU(N)$), establishing logarithmic asymptotic freedom on the lattice.
- **Reconciled Status:** **`PROVED`** (`PERTURBATIVE_ASYMPTOTIC_FREEDOM_ONLY`)
- **Exact Hypotheses:** Compact simple Lie group $SU(N)$; bare lattice coupling $g_0 \ll 1$; formal weak-coupling perturbation expansion.
- **Operator Scope:** Plaquette action and small-loop Wilson operators.
- **Cutoff Scope:** Bare lattice spacing $a > 0$, weak coupling.
- **Primary Sources:** Gross & Wilczek (1973), Politzer (1973).
- **Limitation:** Asymptotic series; does not prove convergence, continuum measure, or infrared confinement.

---

### Edge 2: `E-UV-FREE-CONT`
- **Source Node:** `N-REG-CUTOFF`
- **Target Node:** `N-UV-FREE`
- **Mathematical Proposition:** Continuum UV-regularized non-Abelian Yang–Mills with smooth momentum cutoff $\Lambda < \infty$ exhibits perturbative asymptotic freedom governed by a negative beta function ($\beta(g) = -\beta_0 g^3 - \beta_1 g^5 + \mathcal{O}(g^7)$) in BRST-gauge-fixed perturbation theory.
- **Reconciled Status:** **`PROVED`** (`PERTURBATIVE_ASYMPTOTIC_FREEDOM_ONLY` — **NOT** non-perturbative continuum existence)
- **Exact Hypotheses:** Smooth UV momentum cutoff $\Lambda < \infty$; local gauge fixing via Faddeev–Popov/BRST procedure; formal weak-coupling expansion $g(\Lambda) \ll 1$.
- **Operator Scope:** Perturbative renormalization group flow of gauge-fixed vertex functions at finite UV cutoff $\Lambda$.
- **Cutoff Scope:** Continuum UV cutoff $\Lambda < \infty$, formal perturbation theory.
- **Primary Sources:** Faddeev & Popov (1967), Gross & Wilczek (1973), Politzer (1973).
- **Limitation:** Strictly perturbative asymptotic freedom in a UV-cutoff renormalization scheme; does **not** remove the cutoff non-perturbatively, does **not** control Gribov horizons or large fields, and does **not** establish non-perturbative continuum existence (`E-CONT-SCHWINGER = OPEN`).

---

### Edge 3: `E-UV-RG`
- **Source Node:** `N-UV-FREE`
- **Target Node:** `N-UV-RG-BOUNDS`
- **Mathematical Proposition:** Multiscale block-spin renormalization group transformation yields a contractive effective action sequence $\|\mathcal{V}^{(k)}\| \le C g_k^2$ for effective couplings satisfying $g_k \le g_* \approx 0.28$.
- **Reconciled Status:** **`REGULATED_ONLY`**
- **Exact Hypotheses:** Finite Euclidean volume $L_0 < \infty$; bare lattice cutoff $a = L_0 2^{-N_{\text{steps}}}$; initial bare coupling $g_0 \le g_*$.
- **Operator Scope:** Small-field polymer expansion with axial gauge fixing on localized blocks.
- **Cutoff Scope:** Finite volume, UV small-field regime ($g_k \le g_*$).
- **Primary Sources:** Bałaban (1985–1989, `THM-YM-0018`).
- **Limitation:** Stops when running coupling enters intermediate scale $g_k \sim g_*$ or when volume $L_0$ is exhausted. Infinite-volume limit unproved.

---

### Edge 4: `E-CROSSOVER`
- **Source Node:** `N-UV-RG-BOUNDS`
- **Target Node:** `N-INT-COUPLING`
- **Mathematical Proposition:** Non-perturbative continuation of the functional measure from the weak-coupling RG boundary ($g_k \sim g_*$) across the intermediate crossover window ($g_k \sim 1$, $\beta \sim 1 - 2$).
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Non-perturbative integration across scales where neither small-field perturbation nor high-temperature polymer expansions converge.
- **Operator Scope:** Gauge-invariant loop observables and functional measure.
- **Cutoff Scope:** Intermediate length scales.
- **Primary Sources:** None. YM-008/YM-009 attempted flow-regularized SDP loop bootstrap, but the error bounds were stipulated rather than proved.
- **Limitation:** Unbridged chokepoint of the critical cut-set.

---

### Edge 5: `E-LATTICE-GAP`
- **Source Node:** `N-REG-LATTICE`
- **Target Node:** `N-IR-CONFINEMENT`
- **Mathematical Proposition:** On a 4D hypercubic lattice at strong coupling $\beta \le \beta_0$, the character polymer expansion converges in $V \to \infty$, Wilson loops obey an area law, and the transfer matrix has a strictly positive spectral gap $a M_{\text{lat}}(\beta) > 0$.
- **Reconciled Status:** **`REGULATED_ONLY`**
- **Exact Hypotheses:** Fixed lattice spacing $a > 0$; compact group $SU(N)$; strong coupling $\beta \le \beta_0 \approx 0.25$; infinite volume $V \to \infty$.
- **Operator Scope:** Lattice transfer matrix $T = e^{-a H_{\text{lat}}}$ acting on physical Hilbert space of gauge-invariant link states.
- **Cutoff Scope:** Fixed lattice cutoff $a > 0$, strong coupling $\beta \le \beta_0$.
- **Primary Sources:** Osterwalder & Seiler (1978, `THM-YM-0009`), Mack & Petkova (1979).
- **Limitation:** The expansion diverges for $\beta > \beta_0$. The continuum limit requires $\beta \to \infty$, where this construction cannot be evaluated.

---

### Edge 6: `E-LATTICE-CONT`
- **Source Node:** `N-IR-CONFINEMENT`
- **Target Node:** `N-INT-COUPLING`
- **Mathematical Proposition:** The physical spectral mass gap $\Delta = \lim_{a \to 0} \frac{a M(a)}{a} > 0$ remains strictly positive and bounded away from zero across the continuum scaling limit $a \to 0$ ($\beta \to \infty$).
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Uniform positive lower bound on $-\frac{1}{a} \ln \lambda_1(a)$ as $a \to 0$.
- **Operator Scope:** Full continuum Hamiltonian spectrum.
- **Cutoff Scope:** Continuum limit $a \to 0$.
- **Primary Sources:** None. YM-009 attempted a variational upper bound, which cannot mathematically bound the entire Hamiltonian spectrum from below.
- **Limitation:** Critical cut-set chokepoint.

---

### Edge 7: `E-THERMO`
- **Source Node:** `N-INT-COUPLING`
- **Target Node:** `N-THERMO-LIMIT`
- **Mathematical Proposition:** Existence and uniqueness of the infinite-volume thermodynamic limit $V = L^4 \to \infty$ for all correlation functions in the continuum/intermediate regime.
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Uniform cluster estimates or correlation inequalities independent of boundary conditions as $L \to \infty$.
- **Operator Scope:** Arbitrary local gauge-invariant correlation functions.
- **Cutoff Scope:** Infinite volume $V \to \infty$ with $a \to 0$.
- **Primary Sources:** Proved in strong coupling (Osterwalder–Seiler) and finite volume (Bałaban), but open in the continuum limit.

---

### Edge 8: `E-CONT-SCHWINGER`
- **Source Node:** `N-INT-COUPLING`
- **Target Node:** `N-CONTINUUM-LIMIT`
- **Mathematical Proposition:** Weak convergence of the sequence of regularized Euclidean measures $d\mu_a$ as $a \to 0$ to a continuum probability measure $d\mu$ on $\mathcal{S}'(\mathbb{R}^4)$.
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Tightness of the sequence of measures (Prokhorov's theorem) and uniform distribution bounds.
- **Operator Scope:** Euclidean functional measure and Schwinger functions $S_n$.
- **Cutoff Scope:** $a \to 0$.
- **Primary Sources:** Unresolved in 4D.

---

### Edge 9: `E-SCHWINGER-OS0`
- **Source Node:** `N-CONTINUUM-LIMIT`
- **Target Node:** `N-OS-TEMPERED`
- **Mathematical Proposition:** Continuum Schwinger functions satisfy tempered distribution growth bounds: $|S_n(f_1 \otimes \dots \otimes f_n)| \le c_n \prod \|f_i\|$.
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Uniform bounds in Schwartz space norms on all $n$-point correlation functions.
- **Operator Scope:** $S_n \in \mathcal{S}'((\mathbb{R}^4)^n)$.
- **Cutoff Scope:** Continuum $\mathbb{R}^4$.
- **Primary Sources:** Unresolved in 4D.

---

### Edge 10: `E-SCHWINGER-OS1`
- **Source Node:** `N-CONTINUUM-LIMIT`
- **Target Node:** `N-OS-EUCLIDEAN`
- **Mathematical Proposition:** Continuum Schwinger functions are invariant under full continuous Euclidean rotations and translations $E(4) = \mathbb{R}^4 \rtimes O(4)$.
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Proof that lattice hypercubic anisotropy perturbations vanish non-perturbatively as $a \to 0$ for all $n$-point functions.
- **Operator Scope:** $E(4)$ group action on $S_n$.
- **Cutoff Scope:** Continuum $\mathbb{R}^4$.
- **Primary Sources:** Unresolved non-perturbatively.

---

### Edge 11: `E-SCHWINGER-OS2`
- **Source Node:** `N-CONTINUUM-LIMIT`
- **Target Node:** `N-OS-SYMMETRY`
- **Mathematical Proposition:** Permutation symmetry of Schwinger functions under exchange of arguments: $S_n(x_{\pi(1)}, \dots, x_{\pi(n)}) = S_n(x_1, \dots, x_n)$.
- **Reconciled Status:** **`CONDITIONAL`**
- **Exact Hypotheses:** Bosonic observable integration; conditional on the existence and temperedness of the limiting Schwinger functions (Edges 8 and 9).
- **Operator Scope:** Permutation group $S_n$ on test functions.
- **Cutoff Scope:** Continuum $\mathbb{R}^4$.
- **Primary Sources:** Automatic for commutative path integrals once measure exists.

---

### Edge 12: `E-SCHWINGER-OS3`
- **Source Node:** `N-CONTINUUM-LIMIT`
- **Target Node:** `N-OS-REFL-POS`
- **Mathematical Proposition:** Reflection positivity of the continuum Euclidean functional measure: $\langle \Theta f, f \rangle \ge 0$ for all test functions supported at positive times $x_0 > 0$.
- **Reconciled Status:** **`OPEN` (`OS3_NOT_ESTABLISHED`)**
- **Exact Hypotheses Required:** Preservation of positive-semidefiniteness of the transfer matrix under continuum limits and scale mollifications.
- **Operator Scope:** Quadratic form on $\mathcal{S}_+((\mathbb{R}^4)^n)$.
- **Cutoff Scope:** Continuum $\mathbb{R}^4$.
- **Audit Ground:** Wilson lattice theory satisfies OS3; however, gradient flow smearing leaks across $x_0 = 0$ via infinite Gaussian tails, so OS3 is unestablished for the hybrid construction.

---

### Edge 13: `E-SCHWINGER-OS4`
- **Source Node:** `N-CONTINUUM-LIMIT`
- **Target Node:** `N-OS-CLUSTER`
- **Mathematical Proposition:** Exponential cluster decomposition of Schwinger functions with decay rate $\Delta > 0$: $|S_2(x, y) - S_1(x)S_1(y)| \le C e^{-\Delta |x - y|}$.
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Existence of continuum measure (Edge 8) and strictly positive spectral gap $\Delta > 0$ (Edge 6).
- **Operator Scope:** Connected 2-point Schwinger functions.
- **Cutoff Scope:** Continuum $\mathbb{R}^4$.
- **Primary Sources:** Unresolved.

---

### Edge 14: `E-OS-RECON`
- **Source Node:** `N-OS-REFL-POS`
- **Target Node:** `N-WIGHTMAN-RECON`
- **Mathematical Proposition:** Osterwalder–Schrader Reconstruction Theorem: Any Euclidean field theory satisfying axioms OS0–OS3 reconstructs a unique relativistic Wightman QFT on Minkowski spacetime.
- **Reconciled Status:** **`CONDITIONAL`**
- **Exact Hypotheses:** OS0 (temperedness), OS1 (Euclidean invariance), OS2 (symmetry), OS3 (reflection positivity).
- **Operator Scope:** Analytic continuation via Wick rotation to physical Hilbert space $\mathcal{H}$.
- **Cutoff Scope:** Continuum $\mathbb{R}^{1,3}$.
- **Primary Sources:** Osterwalder & Schrader (1973, 1975, `THM-YM-0007`).
- **Limitation:** Proved in functional analysis, but conditional on proving OS0–OS3 for 4D Yang–Mills.

---

### Edge 15: `E-WIGHTMAN-VAC`
- **Source Node:** `N-WIGHTMAN-RECON`
- **Target Node:** `N-VACUUM-UNIQUE`
- **Mathematical Proposition:** The reconstructed Wightman theory possesses a unique, Poincaré-invariant vacuum state $|\Omega\rangle \in \mathcal{H}$.
- **Reconciled Status:** **`CONDITIONAL`**
- **Exact Hypotheses:** Osterwalder–Schrader reconstruction plus cluster property OS4 (ergodicity of Euclidean time translations).
- **Operator Scope:** GNS representation of physical Hilbert space.
- **Cutoff Scope:** Continuum $\mathbb{R}^{1,3}$.
- **Primary Sources:** Streater & Wightman (1964), Glimm & Jaffe (1987).

---

### Edge 16: `E-WIGHTMAN-SPEC`
- **Source Node:** `N-WIGHTMAN-RECON`
- **Target Node:** `N-SPECTRAL-REP`
- **Mathematical Proposition:** Relativistic spectrum condition: Energy-momentum spectrum lies in the closed forward lightcone $\mathrm{spec}(H, \vec{P}) \subseteq \overline{V_+}$.
- **Reconciled Status:** **`CONDITIONAL`**
- **Exact Hypotheses:** OS reconstruction from reflection positivity OS3.
- **Operator Scope:** Self-adjoint Hamiltonian $H$ and momentum operator $\vec{P}$.
- **Cutoff Scope:** Continuum $\mathbb{R}^{1,3}$.
- **Primary Sources:** Osterwalder & Schrader (1973, 1975).

---

### Edge 17: `E-GAP-CLUSTER`
- **Source Node:** `N-OS-CLUSTER`
- **Target Node:** `N-MASS-GAP`
- **Mathematical Proposition:** Equivalence between Euclidean exponential clustering rate $\Delta > 0$ and the relativistic spectral mass gap $\mathrm{spec}(H) \cap (0, \Delta) = \emptyset$.
- **Reconciled Status:** **`CONDITIONAL`**
- **Exact Hypotheses:** Källén–Lehmann spectral representation; conditional on OS4 and OS reconstruction.
- **Operator Scope:** Transfer matrix and Hamiltonian spectrum.
- **Cutoff Scope:** Continuum $\mathbb{R}^{1,3}$.
- **Primary Sources:** Glimm & Jaffe (1987).

---

### Edge 18: `E-NONTRIV-WITNESS`
- **Source Node:** `N-WIGHTMAN-RECON`
- **Target Node:** `N-NONTRIV-DEF`
- **Mathematical Proposition:** Non-triviality of the reconstructed theory: The Wightman field operators do not satisfy linear field equations (non-trivial scattering $S \neq \mathbf{1}$).
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Non-vanishing truncated 4-point Schwinger function $S_4^c \neq 0$ in the continuum limit.
- **Operator Scope:** Truncated correlation functions and $S$-matrix.
- **Cutoff Scope:** Continuum $\mathbb{R}^{1,3}$.
- **Primary Sources:** Unresolved in 4D.

---

### Edge 19: `E-GROUP-GEN`
- **Source Node:** `N-MASS-GAP`
- **Target Node:** `N-COMPACT-SIMPLE-G`
- **Mathematical Proposition:** The existence and mass gap theorems hold for any compact simple Lie group $G$ (including $SU(N)$, $SO(N)$, $Sp(N)$, $G_2, F_4, E_6, E_7, E_8$).
- **Reconciled Status:** **`OPEN`**
- **Exact Hypotheses Required:** Arbitrary compact simple Lie group $G$.
- **Operator Scope:** General group representations.
- **Cutoff Scope:** Continuum $\mathbb{R}^{1,3}$.
- **Primary Sources:** Unresolved.
