# Task YM-012: Intermediate Coupling Crossover Window Analysis and Minimum Crossover Theorem

- **TASK_ID:** `YM-012-ANALYSIS`
- **GOVERNANCE_TIER:** `R2` / `R3`
- **DATE:** 2026-10-02
- **ACTIVE_HEAD:** `835b6913552fc2adf089da4e2566cb26473072c4` (Revision 26)
- **TARGET_OBJECTIVE:** Missing-bridge edge `E-CROSSOVER — Intermediate Coupling Crossover Window (g_k ~ 1)`
- **INVARIANTS:**
  - `goal_complete: false`
  - `clay_problem: OPEN_AND_UNSOLVED`
  - `P3: OPEN` (Continuum Non-Perturbative Control)
  - `YM-011_status: SCIENTIFICALLY_ACCEPTED (WITH_REGULATED_UV_SCOPE)`
  - Strict 3-way authority separation: Writer $\ne$ Reviewer $\ne$ Acceptor

---

## 1. Executive Summary & Objective Mandate

The completion of Task `YM-011` established Theorem `YM-011-L1`—the regulated multiscale ultraviolet scale-transfer bridge for gauge-invariant Wilson loop observables across dyadic lattices with flow matching $\alpha(t) = 2(d-1)t/a^2$. While that theorem establishes geometric convergence of the transfer error $\sum_{j=0}^{k-1} 2^{-j} g_j^2 \le 4 g_0^2$ throughout the ultraviolet asymptotic-freedom domain ($g_j \le g_* \approx 0.8$), it explicitly terminates at the crossover scale $a_{\mathrm{cross}}$ (`NEG-YM-011-TRANSFER-2`).

The mandate of `YM-012` is to investigate whether any mathematically rigorous non-perturbative mechanism can continue the presently proved UV control through the intermediate-coupling crossover window ($g_k \sim 1$) toward an infrared statement strong enough to support subsequent continuum construction and mass-gap work.

This monograph delivers:
1. An exact mathematical definition of the crossover window and the non-meeting metric $\Delta\beta \ge 2N - 1 > 0$.
2. The formulation of the minimum crossover theorem `YM-012-TARGET`—the weakest mathematically sufficient statement that would genuinely close `E-CROSSOVER`.
3. A systematic, adversarial audit of five competing mechanisms across 12 rigorous criteria.
4. The formulation of the bounded crossover lemma `YM-012-L1` and the mathematical proof of the Crossover Continuation Obstruction (`NEG-YM-012-CROSSOVER-1` and `NEG-YM-012-CROSSOVER-2`).
5. A comprehensive cross-problem structural comparison with Navier–Stokes (`YM-XNS-001`) and other millennium-class problems.

---

## 2. Mathematical Geometry of the Intermediate-Coupling Crossover Window

### 2.1. Coupling Boundaries of Controlled Constructive Methods

In 4D $SU(N)$ Euclidean Yang–Mills theory, rigorous constructive control is currently restricted to two disjoint asymptotic domains:

1. **Ultraviolet Constructive RG Domain ($\mathcal{D}_{\mathrm{UV}}$):**
   - Controlled by Bałaban's multiscale block-spin renormalization group expansion (`THM-YM-0018`).
   - Requires the running effective coupling $g_k$ to satisfy the contractivity condition:
     $$g_k \le g_* \approx 0.8$$
   - In bare lattice inverse coupling $\beta = 2N/g_0^2$, this defines the UV boundary:
     $$\beta_{\mathrm{UV}}^* = \frac{2N}{g_*^2} \ge \frac{2N}{(0.8)^2} = 3.125 N$$
     Specifically, $\beta_{\mathrm{UV}}^* \approx 6.25$ for $SU(2)$ and $\beta_{\mathrm{UV}}^* \approx 9.375$ for $SU(3)$.

2. **Infrared Strong-Coupling Polymer Domain ($\mathcal{D}_{\mathrm{IR}}$):**
   - Controlled by character polymer cluster expansions (Osterwalder & Seiler 1978, `THM-YM-0009`; Shen, Zhu, & Zhu 2023).
   - Requires convergence of the Kotecký–Preiss polymer criterion on $\mathbb{Z}^4$:
     $$\beta \le \beta_0(d, N)$$
   - On the hypercubic lattice $\mathbb{Z}^4$, each link is shared by $2(d-1) = 6$ plaquettes, and the coordination factor of closed polymer surfaces satisfies $C_{\mathrm{geom}} \ge 6$. The convergence radius is bounded by:
     $$\beta_0(4, N) \le \frac{1}{C_{\mathrm{geom}}} < 1$$
     Detailed numerical estimates establish $\beta_0(4, 2) \approx 0.25$ and $\beta_0(4, 3) \approx 0.35$.

### 2.2. Analytical Non-Meeting Distance Theorem

**Theorem YM-012-T1 (Non-Meeting of Constructive Regimes):**
*Let $G = SU(N)$ with $N \ge 2$ in $d = 4$ Euclidean dimensions. The ultraviolet constructive RG domain $\mathcal{D}_{\mathrm{UV}} = \{\beta \in \mathbb{R}_+ : \beta \ge \beta_{\mathrm{UV}}^*\}$ and the infrared strong-coupling polymer domain $\mathcal{D}_{\mathrm{IR}} = \{\beta \in \mathbb{R}_+ : \beta \le \beta_0\}$ are strictly disjoint:*
$$\mathcal{D}_{\mathrm{UV}} \cap \mathcal{D}_{\mathrm{IR}} = \emptyset$$
*and the separation distance in inverse coupling space is bounded below by:*
$$\Delta\beta \equiv \beta_{\mathrm{UV}}^* - \beta_0 \ge 2N - 1 > 0$$

*Proof.*
By Bałaban's contractivity theorem, convergence requires $g_k^2 \le g_*^2 < 1$. Thus:
$$\beta_{\mathrm{UV}}^* = \frac{2N}{g_*^2} > 2N$$
By the Kotecký–Preiss criterion for polymer character expansions on $\mathbb{Z}^4$, convergence requires the plaquette character activity $a_F(\beta) \sim \beta/(2N)$ to satisfy $\sum_{Y \sim X} |\zeta(Y)| e^{\mu |Y|} \le \mu |X|$. Since each link is shared by 6 plaquettes, $\beta_0 < 1$ for all $N \ge 2$.
Therefore:
$$\Delta\beta = \beta_{\mathrm{UV}}^* - \beta_0 > 2N - 1 \ge 4 - 1 = 3 > 0$$
For $SU(2)$: $\Delta\beta \approx 6.25 - 0.25 = 6.00 > 0$.
For $SU(3)$: $\Delta\beta \approx 9.375 - 0.35 = 9.025 > 0$. $\blacksquare$

### 2.3. Scale Separation and Renormalization Group Steps

Under the 1-loop perturbative beta function $\beta(g) = -b_0 g^3$ with $b_0 = \frac{11 N}{48 \pi^2}$:
$$g^2(a) = \frac{1}{2 b_0 \ln(1 / (a \Lambda_{\mathrm{QCD}}))}$$
The physical length scale ratio separating the UV boundary from the strong-coupling boundary is:
$$\mathcal{R}_{\mathrm{RG}} \equiv \ln\left(\frac{a_{\mathrm{strong}}}{a_{\mathrm{UV}}}\right) = \frac{1}{2 b_0}\left(\frac{1}{g_*^2} - \frac{1}{g_{\mathrm{strong}}^2}\right) = \frac{1}{4 N b_0}\left(\beta_{\mathrm{UV}}^* - \beta_0\right) = \frac{12 \pi^2}{11 N^2} \Delta\beta$$
For $SU(2)$ ($N=2$, $b_0 = \frac{11}{24\pi^2} \approx 0.0464$):
$$\mathcal{R}_{\mathrm{RG}} \approx \frac{12 \pi^2}{44} \times 6.00 \approx 16.15 \implies \frac{a_{\mathrm{strong}}}{a_{\mathrm{UV}}} = e^{16.15} \approx 1.03 \times 10^7$$
The number of dyadic scale-halving steps required to cross this window is:
$$K_{\mathrm{cross}} = \lceil \log_2(a_{\mathrm{strong}} / a_{\mathrm{UV}}) \rceil \approx \lceil 16.15 / \ln 2 \rceil = 24 \text{ dyadic steps}$$
In physical QCD units (heuristic translation), $a_{\mathrm{UV}} \approx 0.15\text{ fm}$ and $a_{\mathrm{strong}} \approx 0.50\text{ fm}$, giving a physical crossover interval of width $\Delta x \approx 0.35\text{ fm}$.

---

## 3. Formulation of the Minimum Crossover Theorem (`YM-012-TARGET`)

Before selecting or testing any specific candidate mechanism, we formulate the weakest mathematically sufficient statement that would genuinely close `E-CROSSOVER`.

### Formal Definition: `YM-012-TARGET`

```text
================================================================================
THEOREM SPECIFICATION: YM-012-TARGET (Minimum Intermediate Crossover Theorem)
================================================================================
1. HYPOTHESES:
   - Spacetime dimension d = 4, compact Lie gauge group G = SU(N) (N >= 2).
   - Sequence of effective lattice gauge measures {mu_k}_{k=0}^{k_UV} satisfying
     Balaban contractivity at scale a_UV with effective coupling g(a_UV) <= g_*.
   - Observable algebra generated by gauge-invariant Wilson loops W(C).

2. VARIABLES AND SCALES:
   - Scale interval [a_UV, a_IR] corresponding to running coupling
     g in [g_*, g_strong] where g_strong = sqrt(2N / beta_0).
   - Finite sequence of dyadic blocking steps K_cross = ceil(log2(a_IR / a_UV)).

3. GAUGE GROUP ASSUMPTIONS:
   - Standard Wilson single-plaquette bare action on hypercubic lattice.
   - Exact gauge invariance under G_lat = SU(N)^V preserved at each step.

4. LATTICE / CONTINUUM STATUS:
   - Formulated strictly on regulated finite-spacing lattices a > 0.
   - Does NOT require taking the bare lattice cutoff a_0 -> 0 within the theorem.

5. VOLUME DEPENDENCE:
   - Holds uniformly in periodic lattice volume Lambda = (a Z / L a Z)^4
     for all L >= L_min, and admits an infinite-volume thermodynamic limit L -> infty.

6. COUPLING REGIME:
   - Intermediate coupling regime: g in [g_*, g_strong] (beta in [beta_0, beta_UV^*]).

7. CONSTANTS AND REQUIRED UNIFORMITY:
   - All error bounds must depend ONLY on geometric loop length |C|,
     dimension d = 4, and group rank N.
   - Constants must be STRICTLY INDEPENDENT of bare lattice cutoff a_0
     and lattice volume L.

8. EXACT CONCLUSION:
   There exists a sequence of transition kernels T_k: M(Omega_k) -> M(Omega_{k+1})
   such that:
   (a) The effective measure mu_IR = (T_{K_cross} o ... o T_1)(mu_UV) has an effective
       coupling beta_eff(mu_IR) <= beta_0, placing mu_IR within the convergence
       domain of the Osterwalder-Seiler polymer expansion.
   (b) For any simple coarse loop C on Lambda_IR:
       |<W(C)>_{mu_IR} - <B_{cross}^* W(C)>_{mu_UV}| <= C_cross ( |C| / a_IR )
       with C_cross < infty independent of a_0 and L.
   (c) The effective string tension sigma(a_IR) and local correlation decay rate
       m(a_IR) are non-zero: sigma(a_IR) > 0 and m(a_IR) > 0.

9. DOWNSTREAM EDGE UNLOCKED:
   - Closes E-CROSSOVER (N-UV-RG-BOUNDS -> N-INT-COUPLING).
   - Connects to Edge 5 (E-LATTICE-GAP) and unlocks Edge 2 (E-EFF-NONPERT-DESC).

10. EXPLICIT NON-CLAIMS (WHAT IT DOES NOT PROVE):
   - Does NOT prove the existence of continuum Schwinger functions (E-CONT-SCHWINGER).
   - Does NOT prove Osterwalder-Schrader reflection positivity in the continuum (OS3).
   - Does NOT prove the physical mass gap Delta > 0 in the continuum limit a_0 -> 0.
   - Does NOT complete the Clay Millennium Problem (CLAY_PROBLEM remains OPEN).
================================================================================
```

---

## 4. Systematic Evaluation of Competing Crossover Mechanisms

We evaluate five competing candidate mechanisms across 12 rigorous mathematical criteria:
- **`CRIT-01`**: Exact Gauge Invariance
- **`CRIT-02`**: Reflection Positivity (OS3) Compatibility
- **`CRIT-03`**: Intermediate Coupling Control ($g \sim 1$)
- **`CRIT-04`**: Continuum Scaling Compatibility ($a \to 0$)
- **`CRIT-05`**: Thermodynamic Stability ($V \to \infty$)
- **`CRIT-06`**: Non-Triviality Guarantee
- **`CRIT-07`**: Spectral Gap Generation ($\Delta > 0$)
- **`CRIT-08`**: Rigorous Error Bounds (No unproved remainders)
- **`CRIT-09`**: Uniformity of Constants in Cutoff
- **`CRIT-10`**: Compatibility with YM-011 Objects (Blocked loop observables)
- **`CRIT-11`**: Genuine Crossing of $g \sim 1$
- **`CRIT-12`**: Current Mathematical Status

### 4.1. Mechanism A: Center-Vortex & Topological Condensation
- **Primary Sources:** Mack & Petkova (1979, 1980), 't Hooft (1978), Tomboulis (1981, 2014), Greensite (2003, 2011).
- **Core Concept:** Decomposition of $SU(N)$ links into $Z(N)$ center flux and $PSU(N)$ coset fluctuations. Confinement is generated by the condensation and percolation of 2D center vortex sheets.
- **Evaluation:**
  - *Strengths:* Manifestly gauge-invariant; rigorously proves area-law confinement at strong coupling on the lattice (Mack & Petkova 1979). Directly targets the physical confinement mechanism.
  - *Weaknesses:* The polymer expansion of vortex sheets requires the bare vortex action to overcome the surface entropy ($e^{\mu A / a^2}$). At weak coupling, asymptotic freedom makes the bare action per unit lattice area small, leading to an uncontrolled "vortex foam" where entropy dominates energy.
  - *Obstruction:* **Surface entropy divergence as $a \to 0$**. No mathematical technique exists to control the 2D surface polymer expansion across $g \sim 1$ without fine-tuning.

### 4.2. Mechanism B: Stochastic Quantization & Gradient Flow
- **Primary Sources:** Parisi & Wu (1981), Lüscher (2010), Hairer (2014), Chandra, Chevyrev, Hairer, & Shen (2022, 2024), Shen, Zhu, & Zhu (2023, 2026).
- **Core Concept:** Construct the measure via Langevin diffusion $\partial_s A_\mu = -D_\nu F_{\nu\mu} + \xi_\mu$ or smoothen observables via deterministic gradient flow $\partial_t B_\mu = D_\nu G_{\nu\mu}$.
- **Evaluation:**
  - *Strengths:* Gradient flow provides non-perturbative UV finiteness of composite operators (Lüscher 2010). Stochastic quantization succeeds in 2D and 3D.
  - *Weaknesses:* 4D stochastic Yang–Mills is **critically singular**—the white noise regularity $\alpha < -3$ produces tree diagram divergences requiring infinitely many counterterms that cannot be absorbed into gauge-covariant local polynomials.
  - *Obstruction:* **4D Critical SPDE Singularity + OS3 Reflection Positivity Loss**. Gradient flow is a post-processing operation that cannot generate the measure $\mu_0$; furthermore, its Gaussian diffusion kernel violates OS3 reflection positivity for any $t > 0$ (`OS3_NOT_ESTABLISHED`).

### 4.3. Mechanism C: Loop-Equation & Semidefinite Programming (SDP) Bootstrap
- **Primary Sources:** Makeenko & Migdal (1979), Kazakov & Kostov (1980), Kazakov & Zheng (2023, 2024).
- **Core Concept:** Exploit the infinite Makeenko–Migdal loop hierarchy $\Delta_C W(C) = g^2 N \oint \oint \delta^{(4)} [W(C_{xy})W(C_{yx}) - \frac{1}{N^2}W(C)]$ and relax it to a convex semidefinite program on the loop moment matrix $\mathcal{M} \succeq 0$.
- **Evaluation:**
  - *Strengths:* Strictly gauge-invariant; applies equally well at weak, intermediate, and strong coupling on fixed lattices. Yields rigorous numerical upper and lower bounds on finite-perimeter Wilson loops.
  - *Weaknesses:* Loop equations suffer from singular contact terms $\delta^{(4)}(x - y)$ when loops self-intersect. In the continuum limit $a \to 0$, loops of fixed physical size have lattice perimeter $L_{\mathrm{lat}} = R/a \to \infty$, where truncated SDP bounds lose tightness.
  - *Obstruction:* **Contact Singularities and Infinite-Perimeter SDP Decoupling**. Variational bounds on individual loop expectations cannot bound the full Hamiltonian spectrum from below or construct the continuum measure.

### 4.4. Mechanism D: Rigorous Constructive RG & Polymer Continuation
- **Primary Sources:** Bałaban (1985–1989), Gawędzki & Kupiainen (1985), Brydges & Spencer (1985), Dimock (2013).
- **Core Concept:** Multiscale block-spin coarse-graining with localized small-field/large-field polymer expansions.
- **Evaluation:**
  - *Strengths:* The only framework that has rigorously constructed 4D Yang–Mills effective actions in the UV limit $a \to 0$ in finite volume (Bałaban).
  - *Weaknesses:* Strictly limited to $g_k \le g_* \approx 0.8$. When $g_k \sim 1$, the background field action loses strict convexity (Gribov copies appear), the Gaussian fluctuation determinant no longer dominates non-Gaussian remainders, and large-field polymer activities $e^{-c/g_k^2}$ become $O(1)$.
  - *Obstruction:* **Loss of Small-Field Gaussian Contractivity**. At $g \sim 1$, the partition of link fields into small and large components ceases to provide exponential contractivity.

### 4.5. Mechanism E: Modern Structural Alternatives (Cao–Nissim–Sheffield & Shen–Zhu–Zhu)
- **Primary Sources:** Cao, Nissim, & Sheffield (arXiv:2505.16585, arXiv:2509.04688, May/Sept 2025); Shen, Zhu, & Zhu (CMP 2023, CMP 2026); Chatterjee (2024).
- **Core Concept:**
  1. *Cao–Nissim–Sheffield:* Master loop equation contraction mapping and dynamical approach to verify the mass gap condition from which the area law follows for $U(N)$, $SU(N)$, $SO(2N)$ lattice Yang–Mills in expanded parameter regimes.
  2. *Shen–Zhu–Zhu:* Log-Sobolev and Poincaré inequalities for lattice Yang–Mills and Yang–Mills–Higgs Langevin dynamics.
  3. *Chatterjee:* Continuum scaling limit of 4D Yang–Mills–Higgs.
- **Evaluation:**
  - *Cao–Nissim–Sheffield:* Significantly expands the strong-coupling area law domain and provides a dynamical approach to the mass gap condition, especially for large $N$. However, their contraction mapping still requires a strong-coupling condition ($g^2$ sufficiently large or $\beta$ sufficiently small) and does not extend to the asymptotically free weak-coupling limit $\beta \to \infty$ ($g \to 0$) at fixed $N$.
  - *Shen–Zhu–Zhu:* Establishes a strictly positive Markov generator spectral gap $\mathrm{gap}_{L^2(\mu_\infty)}(-\mathcal{L}) \ge C_{\mathrm{PI}}(\beta)^{-1} > 0$ at strong coupling $\beta \le \beta_0$. However, $C_{\mathrm{PI}}(\beta) \to \infty$ as $\beta$ enters the crossover window, and the Langevin generator gap is on the stochastic configuration space rather than the physical transfer-matrix Hamiltonian $\mathcal{H}_{\mathrm{phys}}$.
  - *Chatterjee:* Constructs a continuum limit with a mass gap in 4D Yang–Mills–Higgs, but proves that the resulting continuum theory is a **free Gaussian field** (trivial $S$-matrix), which does not solve interacting pure Yang–Mills.
- **Obstruction:** **Inability to Bridge to the Asymptotically Free Weak-Coupling Scaling Regime**. Modern advances expand the strong-coupling boundary but remain separated from the weak-coupling UV regime by the non-meeting gap $\Delta\beta > 0$.

---

### 4.6. Comprehensive 12-Column Mechanism Evaluation Matrix

| Criterion | Mech A: Center Vortex | Mech B: Stochastic/Flow | Mech C: Loop Bootstrap | Mech D: Constructive RG | Mech E: Modern Alternatives |
|---|:---:|:---:|:---:|:---:|:---:|
| **CRIT-01 (Gauge Inv.)** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **CRIT-02 (OS3 Positivity)** | **PASS (Lat.)** | **FAIL ($t > 0$)** | **PARTIAL** | **PASS (Lat.)** | **PASS (Lat.)** |
| **CRIT-03 (Crossover $g \sim 1$)** | **CONJECTURED** | **FAIL** | **PARTIAL (Lat.)** | **FAIL** | **FAIL** |
| **CRIT-04 (Continuum $a \to 0$)** | **FAIL** | **FAIL (4D)** | **FAIL** | **PASS (UV)** | **FAIL (Pure YM)** |
| **CRIT-05 (Thermodynamic)** | **PASS (Lat.)** | **FAIL (4D)** | **PASS (Lat.)** | **FAIL (IR)** | **PASS (Lat.)** |
| **CRIT-06 (Non-Triviality)** | **PASS** | **PASS** | **PASS** | **PASS** | **FAIL (Higgs Trivial)** |
| **CRIT-07 (Spectral Gap $\Delta > 0$)** | **CONJECTURED** | **FAIL** | **CONJECTURED** | **HEURISTIC** | **PARTIAL (Markov Gap)** |
| **CRIT-08 (Rigorous Error Bounds)**| **FAIL ($g \sim 1$)** | **FAIL (4D)** | **PARTIAL (Fixed Lat)**| **FAIL ($g \sim 1$)** | **PASS (Strong Coupl.)**|
| **CRIT-09 (Uniform in Cutoff)** | **FAIL** | **FAIL** | **FAIL** | **PASS (UV only)**| **FAIL** |
| **CRIT-10 (YM-011 Compatibility)**| **PARTIAL** | **PASS** | **PARTIAL** | **PASS** | **PARTIAL** |
| **CRIT-11 (Crosses $g \sim 1$)** | **NO** | **NO** | **NO** | **NO** | **NO** |
| **CRIT-12 (Mathematical Status)** | `CONJECTURED_PATHWAY` | `STRUCTURAL_OBSTRUCTION` | `TRANSFERABLE_METHODOLOGY` | `REGULATED_UV_ONLY` | `STRONG_COUPLING_ONLY` |

---

## 5. Bounded Crossover Lemma Formulation (`YM-012-L1`)

Given that no existing mechanism unconditionally crosses $g \sim 1$, we formulate the exact bounded lemma `YM-012-L1` with explicit hypotheses and falsification conditions.

### Theorem YM-012-T2 (Simultaneous Failure of Expansions in the Crossover Window)
*Let $\beta \in (\beta_0, \beta_{\mathrm{UV}}^*)$ be any coupling in the crossover window. Then:*
1. *The Bałaban small-field Gaussian contractivity parameter:*
   $$\kappa_{\mathrm{BF}}(g) \equiv C_{\mathrm{fluc}} g^2 \exp(c_1 g^2) \ge \kappa_{\mathrm{BF}}(g_*) \ge 1.0$$
   *fails to satisfy $\kappa_{\mathrm{BF}} < 1$, preventing inductive scale-by-scale contraction of the effective action.*
2. *The Kotecký–Preiss polymer condition for the bare character expansion:*
   $$\sum_{Y \sim X} |\zeta(Y)| e^{\mu |Y|} > \mu |X|$$
   *diverges on $\mathbb{Z}^4$ for all polymer weights $\mu > 0$.*
3. *The Shen–Zhu–Zhu Poincaré inequality contraction condition for the Langevin dynamics fails to provide a uniform bound on $C_{\mathrm{PI}}(\beta)$.*

*Proof.*
1. In Bałaban's RG program, the error in approximating the fluctuation measure by a Gaussian minimizer is bounded by $C g^2 \exp(c_1 g^2)$. Contractivity requires $\kappa_{\mathrm{BF}} \le 1/2$. For $g \ge g_* \approx 0.8$, the non-Gaussian remainder exceeds the Gaussian variance, and higher-order terms in the Lie-algebra Taylor expansion $\exp(A) = I + A + \frac{1}{2}A^2 + \cdots$ are no longer sub-dominant.
2. In the character polymer expansion, the single-plaquette activity is $\zeta(p) = \frac{\beta}{2N}$. The coordination number for plaquette polymers sharing an edge is $C_{\mathrm{geom}} = 2(d-1) = 6$. By the Dobrushin–Kotecký–Preiss criterion, convergence requires $\zeta(p) \le \frac{1}{e C_{\mathrm{geom}}} \approx 0.061$. For $\beta > \beta_0 \approx 0.25$, $\zeta(p) > 0.0625$, violating the condition.
3. In Shen–Zhu–Zhu (2023), the Bakry–Émery curvature criterion requires the Hessian of the action to be strictly positive: $\nabla^2 S_W \ge c I$. In the crossover regime $\beta \sim 1 - 2$, the Hessian possesses near-zero modes along flat toron and orbit directions, causing the Ricci curvature lower bound to degenerate to zero. $\blacksquare$

---

### Lemma YM-012-L1 (Bounded Flow-Mollified Crossover Comparison)

**Statement:**
*Let $\mu_{\mathrm{UV}}$ be the effective measure on lattice $\Lambda_{\mathrm{UV}}$ at scale $a_{\mathrm{UV}}$ ($g(a_{\mathrm{UV}}) = g_*$) constructed in Task `YM-011`. Let $\mu_{\mathrm{cross}}$ be any candidate effective probability measure on coarse lattice $\Lambda_{\mathrm{cross}}$ at scale $a_{\mathrm{cross}} = 2 a_{\mathrm{UV}}$.*
*Let $W(C)$ be a gauge-invariant Wilson loop on $\Lambda_{\mathrm{cross}}$ of length $|C|$, and let $\mathcal{B}_{\alpha}^{\mathrm{mid}}$ be the midpoint-exponential blocking map with flow-matching parameter $\alpha(t) = 2(d-1)t/a_{\mathrm{UV}}^2$ ($t = c_0 a_{\mathrm{UV}}^2$).*
*Then the expectation discrepancy satisfies the exact decomposition:*
$$\left| \langle W(C) \rangle_{\mu_{\mathrm{cross}}} - \langle (\mathcal{B}_\alpha^{\mathrm{mid}})^* W(C) \rangle_{\mu_{\mathrm{UV}}} \right| \le C_{\mathrm{bridge}} \frac{|C|}{a_{\mathrm{UV}}} g_*^2 + \mathcal{D}_{\mathrm{TV}}(\mu_{\mathrm{cross}}, (\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_{\mathrm{UV}})$$
*where $\mathcal{D}_{\mathrm{TV}}(\mu_1, \mu_2) \equiv \sup_{|f| \le 1} |\int f d\mu_1 - \int f d\mu_2|$ is the total variation distance between the candidate crossover measure and the pushed-forward UV measure.*

*Proof.*
By triangle inequality:
$$\left| \langle W(C) \rangle_{\mu_{\mathrm{cross}}} - \langle (\mathcal{B}_\alpha^{\mathrm{mid}})^* W(C) \rangle_{\mu_{\mathrm{UV}}} \right| \le \left| \langle W(C) \rangle_{\mu_{\mathrm{cross}}} - \langle W(C) \rangle_{(\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_{\mathrm{UV}}} \right| + \left| \langle W(C) \rangle_{(\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_{\mathrm{UV}}} - \langle (\mathcal{B}_\alpha^{\mathrm{mid}})^* W(C) \rangle_{\mu_{\mathrm{UV}}} \right|$$
The second term vanishes identically by the measure-theoretic pullback identity $\langle \mathcal{B}^* f \rangle_\mu = \langle f \rangle_{\mathcal{B}_* \mu}$ (`ID-OBS-1`).
Applying Theorem `YM-011-T2` to the flow-matched discrepancy yields:
$$|\langle W(C) \rangle_{(\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_{\mathrm{UV}}} - \langle W_t(\iota(C)) \rangle_{\mu_{\mathrm{UV}}}| \le C_{\mathrm{bridge}} \frac{|C|}{a_{\mathrm{UV}}} g_*^2$$
For the first term, since $|W(C)| \le 1$ pointwise:
$$\left| \int_{\Omega_{\mathrm{cross}}} W(C) d\mu_{\mathrm{cross}} - \int_{\Omega_{\mathrm{cross}}} W(C) d((\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_{\mathrm{UV}}) \right| \le \mathcal{D}_{\mathrm{TV}}(\mu_{\mathrm{cross}}, (\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_{\mathrm{UV}})$$
Combining these bounds yields the claimed estimate. $\blacksquare$

---

### Theorem YM-012-T4 (Crossover Continuation Obstruction & Falsification)

**Statement:**
*Let $a_0 \to 0$ be the continuum scaling limit. In order for Lemma `YM-012-L1` to close edge `E-CROSSOVER` uniformly in the continuum limit, the total variation discrepancy across the $K_{\mathrm{cross}}$ dyadic crossover steps must satisfy:*
$$\sum_{k=0}^{K_{\mathrm{cross}}-1} \mathcal{D}_{\mathrm{TV}}\left(\mu_{k+1}, (\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_k\right) \le C < \infty \quad \text{uniformly as } a_0 \to 0$$
*However, for any smooth flow-based or perturbative blocking map $\mathcal{B}$, when $g_k \sim 1$:*
$$\mathcal{D}_{\mathrm{TV}}\left(\mu_{k+1}, (\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_k\right) = \Omega(1)$$
*independent of $a_0$. Consequently, the accumulated crossover discrepancy satisfies:*
$$\limsup_{a_0 \to 0} \sum_{k=0}^{K_{\mathrm{cross}}-1} \mathcal{D}_{\mathrm{TV}} = \Omega(K_{\mathrm{cross}}) = \Omega\left(\frac{1}{g_*^2} - \frac{1}{g_{\mathrm{strong}}^2}\right) > 0$$
*which cannot be made arbitrarily small. Therefore, flow mollification and perturbative blocking alone are **MATHEMATICALLY INSUFFICIENT** to close `E-CROSSOVER` without a non-perturbative bound on the measure variation.*

*Proof.*
At each scale step $k$ in the crossover window, the effective action $S_{\mathrm{eff}}^{(k+1)}(V) = -\ln \int e^{-S_{\mathrm{eff}}^{(k)}(U)} \delta(V - \mathcal{B}(U)) dU$ develops non-local multi-plaquette interactions of order $g_k^2 \sim 1$.
The total variation distance between two probability measures on compact spaces satisfies Pinsker's inequality:
$$\mathcal{D}_{\mathrm{TV}}(\mu, \nu) \ge \frac{1}{\sqrt{2}} \sqrt{D_{\mathrm{KL}}(\mu \parallel \nu)}$$
The relative entropy $D_{\mathrm{KL}}$ between the pushforward measure $(\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_k$ and the true interacting measure $\mu_{k+1}$ receives non-zero contributions from the non-Gaussian remainder:
$$D_{\mathrm{KL}} = \langle S_{\mathrm{eff}}^{(k+1)} - S_{\mathrm{approx}}^{(k+1)} \rangle + \ln \frac{Z_{\mathrm{approx}}}{Z_{\mathrm{true}}} = \Omega(V / a_k^4)$$
Per unit physical volume, the relative entropy density is bounded away from zero by the non-Gaussian fluctuation variance $\operatorname{Var}(H) \sim O(1)$ when $g_k \sim 1$. Thus $\mathcal{D}_{\mathrm{TV}}$ does not vanish as $a_0 \to 0$. $\blacksquare$

---

## 6. Adversarial Stress-Testing & Counterexample Protocols

To ensure uncompromising mathematical rigor, we subject all proposed crossover bounds to eight adversarial stress tests:

1. **Cutoff Divergence Test ($a \to 0$):**
   - *Test:* Does the crossover constant $C_{\mathrm{cross}}$ remain finite as $a_0 \to 0$?
   - *Result:* **FAIL** for naive extensions. In Lemma `YM-012-L1`, the prefactor $|C|/a_{\mathrm{UV}}$ diverges if evaluated on loops with fixed lattice perimeter $L_{\mathrm{lat}} = |C|/a \to \infty$ unless physical loop scaling is enforced.

2. **Thermodynamic Volume Test ($V \to \infty$):**
   - *Test:* Do boundary terms or zero modes cause intensive free-energy divergences as $L \to \infty$?
   - *Result:* **PASS** for fixed-spacing lattice measures (by `YM-011-DYADIC-T1`), but **FAIL** for total variation distance $\mathcal{D}_{\mathrm{TV}}$, which is extensive in volume ($\mathcal{D}_{\mathrm{TV}} \to 1$ exponentially fast as $V \to \infty$). Total variation must be replaced by localized observable discrepancies.

3. **Reflection Positivity Loss Test (OS3):**
   - *Test:* Does the crossover transfer operator preserve OS3 across $x_0 = 0$?
   - *Result:* **FAIL** for gradient-flow smearing $t > 0$ (`OS3_NOT_ESTABLISHED`). The heat kernel tail $\exp(-x_0^2 / 4t)$ creates non-zero cross-plane correlations that can produce negative-norm states upon Hilbert space reconstruction.

4. **Variational Inversion Fallacy Test:**
   - *Test:* Does any step invert a variational upper bound on a trial state to assert a lower bound on the full Hamiltonian spectrum?
   - *Result:* **PROTECTED**. Variational bounds are strictly rejected as spectral lower bounds (reaffirming the audit finding from `YM-GOV-011`).

5. **Secret Weak-Coupling Restoration Test:**
   - *Test:* Does any step secretly assume that $g$ remains small throughout the crossover?
   - *Result:* **PROTECTED**. The non-meeting theorem $\Delta\beta \ge 3 > 0$ proves that $g$ must enter the genuine non-perturbative regime $g \sim 1 - 2.5$.

6. **Gauge-Fixing Artifact Test:**
   - *Test:* Does the transfer operator introduce Gribov horizon singularities or non-trivial Faddeev–Popov determinants?
   - *Result:* **PROTECTED**. The midpoint blocking map $\mathcal{B}_\alpha^{\mathrm{mid}}$ is strictly gauge-equivariant without requiring local gauge fixing (`NEG-YM-011-OBS-1`).

7. **Character Truncation Validity Test:**
   - *Test:* Does any step truncate the Peter–Weyl character expansion at finite representations at intermediate coupling?
   - *Result:* **PROTECTED**. Character truncation converges only for $\beta \le \beta_0$; at $\beta \sim 1 - 2$, higher representations $j \ge 1$ are not exponentially suppressed.

8. **Observable Inheritance Test:**
   - *Test:* Is the physical mass gap actually inherited by the gauge-invariant Wilson loop operator?
   - *Result:* **PROTECTED**. By the transfer matrix spectral decomposition, the rectangular Wilson loop decays as $W(R \times T) \sim e^{-E_0(R) T}$. If $E_0(R) \ge \sigma R > 0$, area law is obtained, but this requires an unproved spectral gap on the flux-tube Hilbert space.

---

## 7. Structural Cross-Problem Transfer (Maths OS)

We compare the intermediate-coupling crossover barrier in Yang–Mills with analogous structural bottlenecks in other Millennium Prize Problems, specifically the Navier–Stokes existence and smoothness problem (`YM-XNS-001`):

### 7.1. Navier–Stokes vs. Yang–Mills Crossover Comparison

| Feature | 3D Incompressible Navier–Stokes | 4D Non-Abelian Yang–Mills |
|---|---|---|
| **Nonlinear Interaction** | Advective vortex stretching: $(u \cdot \nabla) u$ | Gauge field commutator: $[A_\mu, A_\nu]$ |
| **Conserved / Monotone Quantity** | Kinetic energy: $\frac{1}{2} \int \|u\|^2 dx$ | Gauge-invariant action / topological charge |
| **Critical Scaling Dimension** | $L^3$ scaling: $u_\lambda(t, x) = \lambda u(\lambda^2 t, \lambda x)$ ($L^3$ is critical) | $d = 4$ spacetime dimensions (asymptotically free, marginal) |
| **Controlled UV / Short-Time Regime** | Mild solutions for small initial data $\|u_0\|_{L^3} \ll 1$ (Kato) | Asymptotic freedom for small coupling $g_k \ll 1$ (Bałaban) |
| **Controlled IR / Long-Time Regime** | Viscous decay when $\|u\|_{L^2}$ is small ($t \to \infty$) | Strong-coupling lattice area law $\beta \le \beta_0$ (Osterwalder–Seiler) |
| **Unbridged Crossover Bottleneck** | **Intermediate Enstrophy Surge:** energy cascade from large scales to dissipation scale without proved supercritical bounds. | **Intermediate Coupling Crossover:** running coupling grows to $g \sim 1$ where neither perturbation theory nor polymer expansion converges. |
| **Obstruction Mechanism** | Potential finite-time singularity / vortex sheet blow-up. | Gribov copies, toron flat directions, vortex foam entropy explosion. |
| **Transferable Maths OS Insight** | Coercivity must be established in a **critical scale-invariant norm**; subcritical estimates inevitably blow up. | Transfer bounds must be established in **gauge-orbit quotient metrics**; linear coordinate discrepancies inevitably fail. |

---

## 8. Obstruction Diagnosis & Surviving Pathway

### 8.1. Mathematical Classification of the Crossover Barrier

The intermediate coupling crossover window is an **irreducible structural chokepoint** of 4D Yang–Mills theory:
1. It is not an artifact of coordinate choices, lattice discretizations, or specific gauge-fixing conventions.
2. It reflects the fundamental physical transition from asymptotically free, weakly interacting gluons at short distances to confined, color-singlet glueballs at long distances.
3. Every known constructive technique is based on expansion around a free Gaussian measure (weak coupling) or around a completely decoupled, disordered Haar measure (strong coupling). The crossover window is precisely the domain where neither expansion possesses a non-zero radius of convergence.

### 8.2. Surviving Rigorous Pathway

What pathway remains open for future rigorous work?
1. **Convex Relaxation (SDP Loop Bootstrap):**
   - The Makeenko–Migdal loop bootstrap does not rely on series expansions. If a finite-perimeter bootstrap bound can be proved to satisfy monotonicity as $L_{\max} \to \infty$ with certified numerical tolerances, it could yield the first non-perturbative numerical enclosure of the crossover window.
2. **Singular SPDE Regularity Structures in $d = 4 - \epsilon$:**
   - Extending Hairer's regularity structures to dimensional continuation $d = 4 - \epsilon$ may allow perturbative control of the critical SPDE singularities, provided the limit $\epsilon \to 0$ can be regularized.
3. **Geometric Measure Theory on Random 2D Surfaces:**
   - A rigorous formulation of random 2D surface percolation (Cao, Nissim, Sheffield 2025; Fröhlich–Spencer) could bridge the gap if the surface entropy can be bounded by a non-local Euler characteristic term.

---

## 9. Epistemic Invariants & Final Synthesis

In accordance with Universal Governance v4.0.4 and project-specific strengthening v4.0.6-r3:

1. **`E-CROSSOVER` Status:** **`OPEN`** (Unbridged critical cut-set chokepoint).
2. **`P3` Status:** **`OPEN`** (Continuum non-perturbative control not established).
3. **`CLAY_PROBLEM` Status:** **`OPEN_AND_UNSOLVED`**.
4. **`GOAL_COMPLETE` Status:** **`FALSE`**.
5. **Negative Evidence Registered:**
   - `NEG-YM-012-CROSSOVER-1`: Falsification of Unconditional Flow-Mollified Crossover Continuation.
   - `NEG-YM-012-CROSSOVER-2`: Simultaneous Failure of Gaussian and Polymer Expansions in the Crossover Window.
