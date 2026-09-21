# Task YM-006: UV-to-IR Comparative Parameter Framework

- **TASK_ID:** `YM-006`
- **GOVERNANCE_TIER:** `R2` (Scientific non-meeting estimate calculation)
- **TASK_ENVELOPE:** `governance/envelopes/YM-006.yaml`
- **UV_INPUT:** `literature/YM-004-UV-BOUNDARY-RECORD.md` (`UV-BND-YM004-001`)
- **IR_INPUT:** `literature/YM-005-IR-BOUNDARY-RECORD.md` (`IR-BND-YM005-001`)
- **DATE:** 2026-09-22

---

## 1. Executive Summary & Objective

The objective of Task **YM-006** is to determine the exact mathematical relationship and distance between the two established rigorous boundaries in 4D Euclidean Yang–Mills theory:
1. **The UV Boundary (`YM-004`):** Bałaban's multiscale constructive renormalization group program, operating at weak coupling $g_k \le g_* \ll 1$ in finite volume $L_0 < \infty$, establishing ultraviolet stability as $a_0 \to 0$ up to scale $a_k = 1$.
2. **The IR Boundary (`YM-005`):** Osterwalder–Seiler character expansions and Shen–Zhu–Zhu Langevin stochastic functional inequalities, operating at strong coupling $\beta \le \beta_0 \ll 1$ on an infinite-volume discrete lattice $\mathbb{Z}^4$ at fixed cutoff $a > 0$.

Before computing the quantitative non-meeting distance, this document establishes the **rigorous comparative parameter dictionary** reconciling the variables, actions, cutoffs, and topologies of both frameworks.

---

## 2. Parameter Dictionary: UV Multiscale RG vs. Lattice Gauge Theory

| Dimension | UV Multiscale RG (Bałaban / MRS, YM-004) | IR Lattice Theory (Wilson / Seiler / Shen–Zhu–Zhu, YM-005) | Translation / Reconciled Relation |
|---|---|---|---|
| **Gauge Group** | Compact simple Lie group $G = SU(N)$ ($N \ge 2$) | Compact simple Lie group $G = SU(N)$ ($N \ge 2$) | Identical compact Lie algebra $\mathfrak{g} = \mathfrak{su}(N)$ |
| **Fundamental Field** | Axial/covariant gauge field $A_\mu(x) \in \mathfrak{g}$ or link variables $U_b \in G$ | Link group elements $U_e \in G$ on lattice edges $E(\Lambda)$ | $U_e = \mathcal{P} \exp\left( i \int_e A_\mu dx^\mu \right)$ |
| **Action Density** | Multiscale effective action $S^{(k)}(A) = \frac{1}{4 g_k^2} \int |F|^2 + \mathcal{R}^{(k)}$ | Wilson plaquette action $S_W(U) = \frac{\beta}{2N} \sum_p \text{Re}\text{Tr}(\mathbb{I} - U_p)$ | $\beta \leftrightarrow \frac{2N}{g^2}$ in the classical weak-coupling limit |
| **Scale / Spacing** | Scale $k \in \{0, 1, \dots, n\}$, lattice spacing $a_k = L^k a_0$ | Fixed discrete lattice spacing $a > 0$ | $a_k \leftrightarrow a$; continuum limit requires $a \to 0$ |
| **Volume Scope** | Finite volume $T_k = L_0 / a_k < \infty$ with periodic boundary conditions | Infinite volume $\mathbb{Z}^4$ via thermodynamic limit $\Lambda \nearrow \mathbb{Z}^4$ | $T_k \to \infty$ vs. $\Lambda \to \mathbb{Z}^4$; UV requires $L_0 < \infty$, IR requires $a > 0$ |
| **Coupling Variable** | Scale-dependent effective coupling $g_k$ ($g_0 = g_{\text{bare}}$) | Dimensionless lattice inverse coupling parameter $\beta$ | $\beta(g) = \frac{2N}{g^2} \iff g(\beta) = \sqrt{\frac{2N}{\beta}}$ |
| **Controlled Regime** | Weak coupling: $g_k \le g_* \ll 1$ (asymptotic freedom) | Strong coupling: $\beta \le \beta_0 \ll 1$ ($g^2 \ge g_{\text{IR}}^{*2} \gg 1$) | **DISJOINT REGIMES**: $g_* \ll 1 \ll g_{\text{IR}}^*$ |
| **Rigorous Norm** | Compound weighted polymer/field norm $\|A\|_{k} + \|\mathcal{R}^{(k)}\|$ | Polymer gas activity $|\zeta(Y)| \le e^{-\mu |Y|}$, $L^2(G^{E(\Lambda)}, d\mu)$ | Contractivity in local norms vs. cluster decay |
| **Key Mechanism** | Scale-by-scale minimization, Gaussian fluctuation integration | Character expansion (Peter–Weyl), Kirkwood–Salsburg / Kotecký–Preiss | Gaussian perturbation around vacuum vs. Haar measure orthogonality |
| **Primary Stopping Point**| Large-field activity divergence when $g_k \to g_* \sim 1$ | Loss of polymer gas contractivity when $\beta \to \beta_0 \sim 1$ | **Non-meeting crossover window around $g \sim 1, \beta \sim 1-2$** |

---

## 3. Coupling Space Parameterization

The two frameworks formulate the coupling parameter inversely:
1. **UV Constructive RG:** Expresses the theory in terms of the gauge coupling constant squared:
   $$g^2 = g_k^2$$
   Perturbative asymptotic freedom governs the regime $g^2 \to 0$ ($g_k \le g_* \ll 1$).
2. **Lattice Gauge Theory:** Expresses the theory in terms of the Wilson inverse coupling parameter:
   $$\beta = \frac{2N}{g^2}$$
   High-temperature character expansions govern the regime $\beta \to 0$ ($g^2 \to \infty$).

### 3.1. Reconciled Coupling Mapping
For any $SU(N)$ gauge group in $d = 4$ spacetime dimensions:
$$\beta(g^2) = \frac{2N}{g^2} \iff g^2(\beta) = \frac{2N}{\beta}$$

Under this bijective mapping on $\mathbb{R}_+^*$:
- **UV Weak-Coupling Convergence Boundary:**
  $$g_k^2 \le g_*^2 \ll 1 \iff \beta \ge \beta_{\text{UV}}^* = \frac{2N}{g_*^2} \gg 1$$
- **IR Strong-Coupling Convergence Boundary:**
  $$\beta \le \beta_0 \ll 1 \iff g^2 \ge g_{\text{IR}}^{*2} = \frac{2N}{\beta_0} \gg 1$$

Because $g_*^2 \ll 1$ and $\beta_0 \ll 1$, we have:
$$\beta_{\text{UV}}^* = \frac{2N}{g_*^2} \gg 1 \gg \beta_0$$
$$g_{\text{IR}}^{*2} = \frac{2N}{\beta_0} \gg 1 \gg g_*^2$$

The two rigorous domains of convergence are strictly **disjoint** in coupling space:
$$\boxed{[0, \beta_0] \cap [\beta_{\text{UV}}^*, \infty) = \emptyset}$$
$$\boxed{[0, g_*^2] \cap [g_{\text{IR}}^{*2}, \infty) = \emptyset}$$

---

## 4. Length Scale and Physical Momentum Parameterization

Under non-perturbative QCD dimensional transmutation:
$$\Lambda_{\text{QCD}} = \mu \exp\left( - \frac{1}{2 b_0 g^2(\mu)} \right) \left( b_0 g^2(\mu) \right)^{-\frac{b_1}{2 b_0^2}} \left( 1 + \mathcal{O}(g^2) \right)$$
where $b_0 = \frac{11 N}{48 \pi^2}$ for pure $SU(N)$ gauge theory.

1. **UV Validity Length Scale:**
   The UV RG flow remains mathematically rigorous only for physical length scales $x$ satisfying:
   $$x \le x_{\text{UV}}^* \sim \frac{c_*}{\Lambda_{\text{QCD}}} \quad (c_* \ll 1)$$
   For $x > x_{\text{UV}}^*$, the running coupling $g(x)$ exceeds $g_*$, and multiscale contractivity fails.

2. **IR Validity Length Scale:**
   The lattice strong-coupling expansion is rigorous only for fixed lattice spacings $a$ satisfying:
   $$a \ge a_{\text{strong}}^* \sim \frac{c_{\text{IR}}}{\Lambda_{\text{QCD}}} \quad (c_{\text{IR}} \gg 1)$$
   For $a < a_{\text{strong}}^*$, taking the continuum limit requires $\beta(a) \to \infty$, which strictly violates $\beta \le \beta_0$.

3. **The Unbridged Intermediate Window:**
   The spatial separation between the maximum UV scale and the minimum IR scale forms a physical non-meeting window:
   $$\boxed{x_{\text{UV}}^* \sim \frac{c_*}{\Lambda_{\text{QCD}}} \ll \frac{1}{\Lambda_{\text{QCD}}} \ll a_{\text{strong}}^* \sim \frac{c_{\text{IR}}}{\Lambda_{\text{QCD}}}}$$

---

## 5. Epistemic Invariant Enforcements

1. **`INV-YM006-001` (Method Boundary vs. Impossibility):**
   The non-meeting distance $\Delta\beta = \beta_{\text{UV}}^* - \beta_0 > 0$ reflects the boundaries of *existing constructive techniques* (multiscale polymer expansions and character expansions). It does NOT prove that continuum quantum Yang–Mills theory does not exist.
2. **`INV-YM006-002` (Provenance Discipline):**
   All numerical values ($g_*^2 \approx 0.08$, $\beta_0 \approx 0.25$, $\beta_{\text{UV}}^* \approx 50$) are explicitly cataloged as `PROJECT_ESTIMATE` or `HEURISTIC_PHYSICAL_TRANSLATION`. Canonical statements enforce strictly symbolic relations: $\beta_{\text{UV}}^* \gg 1 \gg \beta_0$.
3. **`INV-YM006-003` (Symbolic Non-Meeting Invariant):**
   The canonical non-meeting record enforces:
   $$\beta_{\text{UV}}^* - \beta_0 > 0 \quad \text{and} \quad g_{\text{IR}}^{*2} - g_*^2 > 0$$
