# YM-004 PRIMARY SOURCE MAP

## Rigorous UV / Constructive Renormalization Group Primary Sources

This artifact provides the authoritative primary-source map for the mathematical reproduction of the 4D ultraviolet constructive renormalization group machinery in Yang–Mills theory (Task `YM-004`).

---

## 1. Primary Source Inventory

| Source ID | Paper Citation | Authors | Year | Core Mathematical Contribution | Scope & Boundaries |
|---|---|---|---|---|---|
| `PAPER-CONST-004` | *Commun. Math. Phys.* 95 (1984) 419–440; 96 (1984) 223–250; 98 (1985) 17–52 | T. Bałaban | 1984–1985 | Gauge-covariant block averaging transformation $Q(A)$, effective lattice propagators, local block gauge fixing, and exponential Green's function decay. | Multiscale block-spin step; finite block lattices; perturbative weak-coupling propagator bounds. |
| `PAPER-CONST-005` | *Commun. Math. Phys.* 109 (1987) 249–301; 114 (1988) 627–687; 115 (1988) 407–483 | T. Bałaban | 1987–1988 | Inductive small-field effective action theorem: non-perturbative realization of asymptotic freedom, Callan–Symanzik flow, and local counterterm stability. | Small-field region only ($\|F_p\| \le \epsilon_0 g_k^{-\gamma}$); finite torus volume $\mathbb{T}^4 = (L\mathbb{Z})^4$; UV cutoff $a > 0$. |
| `PAPER-CONST-006` | *Commun. Math. Phys.* 116 (1988) 1–22; 119 (1988) 243–285; 122 (1989) 175–202 | T. Bałaban | 1988–1989 | Large-field polymer cluster expansion and full proof of Ultraviolet Stability: uniform partition function bounds as $a \to 0$ in fixed finite volume $V$. | Finite volume $V = L^4 < \infty$; infrared cutoff at scale $L$; stops when effective coupling reaches $g_k \sim 1$. |
| `PAPER-CONST-007` | *Commun. Math. Phys.* 107 (1986) 319–329; 114 (1988) 317–343; 127 (1990) 433–457 | P. Federbush | 1986–1990 | Phase-cell cluster expansion, master inequalities for non-Abelian link fluctuations, and independent constructive verification of multiscale stability. | Bounded spatial domains; fixed cutoff or finite volume; weak-coupling stability. |
| `PAPER-CONST-008` | *Commun. Math. Phys.* 155 (1993) 325–383 | J. Magnen, V. Rivasseau, R. Sénéor | 1993 | Constructive existence of 4D Euclidean Yang–Mills Schwinger distributions with fixed infrared cutoff $\Lambda_{\text{IR}} > 0$; Borel summability in $g^2$. | Explicit IR cutoff $\Lambda_{\text{IR}} > 0$ required; cutoff removal obstructed by IR renormalons and unproved mass gap. |

---

## 2. Granular Primary Citation & Theorem Extraction

### Source 1: Bałaban 1984–1985 (CMP 95, 96, 98) — Averaging & Propagators
- **Theorem ID:** `THM-YM-0016`
- **Exact Proposition:** On a hypercubic lattice $\Lambda^{(k)}$ with spacing $a_k$, for any gauge connection $A$, the block-averaging operation $A' = Q(A)$ defined on the coarsened lattice $\Lambda^{(k+1)}$ with spacing $a_{k+1} = L a_k$ satisfies:
  $$\| Q(A) \|_{L^2(\Lambda^{(k+1)})} \le C_1 \| A \|_{L^2(\Lambda^{(k)})}$$
  and the conditional Green's operator $\Delta_Q^{-1} = (-\Delta + \alpha^{-1} Q^* Q)^{-1}$ in the axial block gauge satisfies the uniform exponential decay estimate:
  $$| \Delta_Q^{-1}(x, y) | \le C_2 a_k^{-2} \exp\left( - m_0 \frac{|x - y|}{a_k} \right)$$
- **Scope:** Dimension $d=4$, compact gauge group $G=SU(N)$, finite block lattice.
- **Indispensable Hypotheses:** Gauge covariance up to local gauge transformations; lattice spacing $a_k > 0$; block scale factor $L \in \mathbb{N}_{\ge 2}$.
- **What is Proved:** Stable functional-analytic foundation for multiscale integration step.
- **What is NOT Proved:** Non-perturbative integration over large field fluctuations or removal of ultraviolet/infrared cutoffs.

### Source 2: Bałaban 1987–1988 (CMP 109, 114, 115) — Small-Field Effective Actions
- **Theorem ID:** `THM-YM-0017`
- **Exact Proposition:** Let $g_0$ be sufficiently small ($g_0 < \epsilon_0$). Under $k$ successive block-spin RG transformations, as long as the effective coupling $g_k$ remains within the weak-coupling regime ($g_k \le g_* \ll 1$), the small-field effective action $S_k(A_k)$ on $\Lambda^{(k)}$ takes the canonical form:
  $$S_k(A_k) = \frac{1}{4 g_k^2} \int \mathrm{Tr}(F_{\mu\nu}^2) + \sum_{j} c_{j,k} \mathcal{O}_{j,\text{local}}(A_k) + R_k(A_k)$$
  where:
  1. $g_k^2$ evolves according to the asymptotic freedom recursion:
     $$\frac{1}{g_k^2} = \frac{1}{g_0^2} - 2 b_0 k \ln L + \mathcal{O}(1), \quad b_0 = \frac{11 N}{48 \pi^2} > 0$$
  2. $\mathcal{O}_{j,\text{local}}$ are local gauge-invariant counterterms of engineering dimension $\le 4$.
  3. The remainder functional $R_k(A_k)$ is analytic in the field $A_k$ in the small-field domain $\mathcal{D}_{\text{small}}(k) = \{ A_k : \sup_p |F_p(A_k)| \le \epsilon g_k^{-\gamma} \}$ and obeys the uniform bound:
     $$\| R_k \|_{\rho, \kappa} \le C g_k^2 \cdot \mathrm{Vol}(\mathbb{T}^4)$$
- **Scope:** Dimension $d=4$, $G=SU(N)$, finite torus $\mathbb{T}^4$, small-field domain.
- **What is Proved:** Rigorous mathematical realization of perturbative renormalization and asymptotic freedom in non-perturbative lattice functional integrals within small-field regions.
- **What is NOT Proved:** Control outside the small-field region; behavior when $g_k \sim 1$; thermodynamic limit $V \to \infty$.

### Source 3: Bałaban 1988–1989 (CMP 116, 119, 122) — Large-Field Polymers & UV Stability
- **Theorem ID:** `THM-YM-0018`
- **Exact Proposition:** In a fixed finite 4D torus $\mathbb{T}^4 = (\mathbb{R} / L_0 \mathbb{Z})^4$, the partition function $Z(\mathbb{T}^4, a_0, g_0)$ of $SU(N)$ lattice Yang–Mills theory, with bare coupling $g_0(a_0)$ tuned along the asymptotic freedom trajectory, admits the convergent multiscale representation:
  $$Z(\mathbb{T}^4, a_0, g_0) = \exp\left( - E_n(\mathbb{T}^4) \right) \int d\mu(A_n) \, e^{-S_n(A_n)} \left[ 1 + \sum_{Y \subset \Lambda^{(n)}} \zeta_n(Y, A_n) \right]$$
  where the polymer activities $\zeta_n(Y)$ satisfy the exponential suppression bound:
  $$|\zeta_n(Y)| \le \exp\left( - \frac{\kappa_0}{g_n^2} |Y| \right)$$
  yielding the uniform stability estimate:
  $$0 < C_{\min}^{V} \le Z(\mathbb{T}^4, a_0, g_0) \le C_{\max}^{V} < \infty$$
  uniformly as $a_0 \to 0$ for fixed volume $V = L_0^4$.
- **Scope:** Dimension $d=4$, $G=SU(N)$, finite volume $V < \infty$, UV limit $a_0 \to 0$.
- **What is Proved:** Complete proof of ultraviolet stability in finite volume.
- **What is NOT Proved:** Thermodynamic limit $V \to \infty$; infinite-volume continuum Schwinger functions; spectral mass gap $\Delta > 0$.

### Source 4: Magnen, Rivasseau & Sénéor 1993 (CMP 155) — Construction with IR Cutoff
- **Theorem ID:** `THM-YM-0020`
- **Exact Proposition:** For 4D Euclidean $SU(N)$ Yang–Mills theory with fixed infrared cutoff $\Lambda_{\text{IR}} > 0$ (implemented via an effective gluon mass or infrared volume cutoff), the ultraviolet continuum limit $a \to 0$ of the connected Schwinger functions $S_n^{\Lambda_{\text{IR}}}(x_1, \dots, x_n)$ exists as tempered distributions, and the perturbation series in the renormalized coupling $g_r^2$ is Borel summable to the non-perturbative Schwinger functions.
- **Scope:** Dimension $d=4$, $G=SU(N)$, continuum spacetime $\mathbb{R}^4$ with IR cutoff $\Lambda_{\text{IR}} > 0$.
- **What is Proved:** Constructive existence of 4D Euclidean Yang–Mills under infrared regularization.
- **What is NOT Proved:** Removal of $\Lambda_{\text{IR}} \to 0$ without a mass gap; proof of the spectral mass gap $\Delta > 0$ in the continuum.

---

## 3. Separation of Independent Programs: Bałaban vs. Magnen–Rivasseau–Sénéor

To prevent synthetic theorem conflation, Bałaban's finite-volume ultraviolet stability program and the Magnen–Rivasseau–Sénéor infrared-regulated continuum program are strictly distinguished across all six canonical comparative dimensions:

| Canonical Dimension | Bałaban Multiscale RG Program (CMP 109, 116, 119, 122) | Magnen–Rivasseau–Sénéor Program (CMP 155, 1993) |
|---|---|---|
| **1. Construction Achieved** | Multiscale block-spin effective action recursion; uniform UV stability bounds on the vacuum functional. | Continuum regularized Schwinger distributions via phase-space cluster expansion; Borel summability in $g_r^2$. |
| **2. Volume Regime** | Finite flat 4-torus $\mathbb{T}^4 = (\mathbb{R}/L_0\mathbb{Z})^4$ ($L_0 < \infty$). | Infinite volume $\mathbb{R}^4$ (thermodynamic limit taken with fixed IR mass cutoff $\Lambda_{\text{IR}} > 0$). |
| **3. Cutoff Regime** | UV lattice cutoff removed ($a_0 \to 0$); runs down to scale $a_*$ where $g_k \le g_* \ll 1$. | UV cutoff removed ($\Lambda_{\text{UV}} \to \infty$); explicit fixed non-zero IR cutoff $\Lambda_{\text{IR}} > 0$ retained. |
| **4. Observables / Functionals Controlled** | Vacuum functional $\Xi_k(B)$, effective action remainders $R_k(A_k)$, small/large field polymer activities. | Regularized connected Schwinger functions / gauge-invariant correlation functions $S_n^{\Lambda_{\text{IR}}}$. |
| **5. Uniformity Established** | Uniform in UV lattice spacing $a_0 \to 0$ and scale steps $k \le k_{\text{prov}}$ at fixed finite volume $L_0$. | Uniform in UV cutoff $\Lambda_{\text{UV}} \to \infty$ at fixed non-zero infrared regulator $\Lambda_{\text{IR}} > 0$. |
| **6. What Remains Open** | Continuum thermodynamic limit $L_0 \to \infty$; intermediate crossover $g_k \sim 1$; continuum Schwinger distributions. | Removal of IR cutoff $\Lambda_{\text{IR}} \to 0$; nonperturbative IR renormalon control; reflection positivity of gauge-invariant observables. |

---

## 4. Bibliographic Clarification on Bałaban Sources

- **Lattice Gauge Theory Primary Sources:**
  - CMP 95 (1984) 419–440: *Propagators and Renormalization Transformations for Lattice Gauge Theories. I*
  - CMP 96 (1984) 223–250: *Propagators and Renormalization Transformations for Lattice Gauge Theories. II*
  - CMP 98 (1985) 17–52: *Averaging Operations for Lattice Gauge Theories*
  - CMP 109 (1987) 249–301: *Renormalization Group Methods in Gauge Theories: (I) Small Fields and Planar Gauges*
  - CMP 114 (1988) 627–687: *Renormalization Group Methods in Gauge Theories: (II) Small Fields and Covariant Gauges*
  - CMP 115 (1988) 407–483: *Renormalization Group Methods in Gauge Theories: (III) Effective Actions*
  - CMP 116 (1988) 1–22: *Convergent Expansions for Lattice Gauge Theories*
  - CMP 119 (1988) 243–285: *Large Field Expansions for Lattice Gauge Theories*
  - CMP 122 (1989) 175–202: *Ultraviolet Stability for Lattice Gauge Theories*
- **Scalar Background Precursors (Not Yang–Mills Theorem Evidence):**
  - Bałaban's separate scalar papers (e.g. *Ultraviolet stability in field theory. The $\phi^4_3$ model*, CMP 102 (1985) 255–272; CMP 104 (1986) 357–380) are methodological precursors for scalar fields in 3 dimensions and are **NOT** cited as theorem evidence for 4D Yang–Mills theory.

---

## 5. Epistemic Status & Governance Compliance

All sources cited are peer-reviewed mathematical physics papers published in *Communications in Mathematical Physics*.
In accordance with ROS v1.0 Law 1:
$$\text{Claim Strength} \le \text{Evidence Strength}$$
- No result is promoted to an infinite-volume continuum theorem without an infrared cutoff.
- No result is promoted to satisfying the Clay Millennium Problem requirements.
- Bałaban's UV stability in finite volume and MRS's construction with an IR cutoff remain strictly independent theorems.
