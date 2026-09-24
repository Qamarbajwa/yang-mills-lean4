# YM-005 Primary Source Map: Rigorous IR and Lattice Gap Machinery

## 1. Executive Identification

- **Task ID:** `YM-005`
- **Task Title:** Rigorous IR / Lattice Gap Machinery Reproduction
- **Governance Context:** Universal Governance v4.0.3 / ROS v1.0
- **Parent Objective:** `CAP-005-lattice-gap`
- **Primary Focus:** Rigorous mathematical reproduction of strong-coupling lattice gauge theory, transfer-matrix spectral gaps, convergent cluster expansions, infinite-volume Gibbs measures, functional inequalities, and the establishment of the **Canonical IR Boundary Record** (`IR-BND-YM005-001`).

---

## 2. Catalog of Reconstructed Primary Sources

The rigorous infrared and lattice gauge theory literature is mapped across five primary eras and methodological families:

### Family A: Foundational Lattice Gauge Formulation and Strong-Coupling Confinement (1974)
- **Primary Source:** K. G. Wilson, *"Confinement of Quarks"*, *Physical Review D* **10** (1974), pp. 2445–2459.
  - **Citation Key:** `PAPER-FOUND-008` / `THM-YM-0008`
  - **Mathematical Contribution:** Introduction of the compact group gauge field lattice formulation on $a \mathbb{Z}^4$; gauge-invariant Wilson plaquette action; character expansion of Haar measure; leading-order strong-coupling area law $\langle W(C) \rangle \sim \exp(-\sigma \cdot \text{Area}(C))$ with string tension $\sigma = a^{-2} \ln(g^2) + \mathcal{O}(1/g^2)$.
  - **Rigorous Scope:** Fixed lattice spacing $a > 0$, strong coupling $g^2 \gg 1$ ($\beta = 2N/g^2 \ll 1$).
  - **Boundary Limitation:** Character expansion has a finite radius of convergence $\beta < \beta_0$; does not establish the weak-coupling continuum limit ($\beta \to \infty, a \to 0$).

### Family B: Reflection Positivity and Physical Transfer Matrix (1977–1978)
- **Primary Source B1:** K. Osterwalder, E. Seiler, *"Gauge Field Theories on a Lattice"*, *Annals of Physics* **110** (1978), pp. 440–471.
  - **Citation Key:** `PAPER-FOUND-013` / `THM-YM-0009`
  - **Mathematical Contribution:** Rigorous proof of Osterwalder–Schrader reflection positivity (OS3) on hypercubic lattices across planes of links and sites; construction of the physical lattice Hilbert space $\mathcal{H}_{\text{lat}}$ and self-adjoint contraction transfer matrix $\mathbb{T} = e^{-a H_{\text{lat}}}$.
  - **Primary Source B2:** M. Lüscher, *"Construction of a Self-Adjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories"*, *Communications in Mathematical Physics* **54** (1977), pp. 283–292.
  - **Mathematical Contribution:** Direct construction of the physical Hilbert space $\mathcal{H}$ of square-integrable gauge-invariant wave functions on temporal slices; proof that $\mathbb{T} > 0$ is strictly positive and self-adjoint, guaranteeing $H_{\text{lat}} = - \frac{1}{a} \ln \mathbb{T}$ is a densely defined positive operator ($H_{\text{lat}} \ge 0$).
  - **Rigorous Scope:** All couplings $0 < \beta < \infty$ at fixed lattice spacing $a > 0$.
  - **Boundary Limitation:** Establishes the existence of the operator $H_{\text{lat}}$ and transfer matrix, but does **not** prove a uniform lower bound $\Delta_{\text{lat}} \ge \Delta_0 > 0$ as $a \to 0$.

### Family C: Axiomatic High-Temperature Cluster Expansions & Infinite Volume (1979–1982)
- **Primary Source C1:** L. Gross, *"The Free Energy for Small Lattice Coupling in Lattice Gauge Theories"*, *Communications in Mathematical Physics* **68** (1979), pp. 9–27.
  - **Mathematical Contribution:** High-temperature character expansions and thermodynamic limit proofs for lattice gauge models.
- **Primary Source C2:** E. Seiler, *"Gauge Theories as a Problem of Constructive Quantum Field Theory and Statistical Mechanics"*, *Lecture Notes in Physics* **159** (Springer-Verlag, 1982), pp. 1–192.
  - **Citation Key:** `PAPER-CONST-003` / `THM-YM-0015`
  - **Mathematical Contribution:** Comprehensive axiomatic foundation of lattice gauge theories; convergence of high-temperature cluster expansions for $\beta < \beta_0(d, G)$; exponential correlation decay; existence and uniqueness of the infinite-volume Gibbs measure; proof that the spectral gap $\Delta_{\text{lat}}(\beta) > 0$ is non-zero in the strong-coupling regime.
  - **Rigorous Scope:** $d \ge 2$, compact Lie groups, $\beta \le \beta_0(d, G)$, infinite volume.
  - **Boundary Limitation:** Expansions diverge when approaching the critical crossover $\beta \sim 1$; unable to access the continuum limit $\beta \to \infty$.

### Family D: Modern Stochastic Analysis and Uniform Functional Inequalities (2023)
- **Primary Source:** H. Shen, R. Zhu, X. Zhu, *"A Stochastic Analysis Approach to Lattice Yang-Mills at Strong Coupling"*, *Communications in Mathematical Physics* **400** (2023), pp. 805–851 (DOI: 10.1007/s00220-022-04609-1; arXiv:2204.12737).
  - **Citation Key:** `PAPER-MOD-007` / `THM-YM-0027`
  - **Mathematical Contribution:** Stochastic quantization via lattice Langevin/Glauber diffusions on compact Lie group manifolds $G^{|\Lambda_\ell|}$; uniform Bakry–Émery curvature bounds; proof of uniform Poincaré and log-Sobolev inequalities independent of volume for $\beta < \beta_0(d, G)$; existence and uniqueness of infinite-volume Gibbs measure on $\mathbb{Z}^d$; strictly positive **Markov / Langevin diffusion generator spectral gap** $\operatorname{gap}_{L^2(\mu_\infty)}(-\mathcal{L}) \ge C_{\text{PI}}(\beta)^{-1} > 0$ and exponential decay of Euclidean gauge-invariant correlations $m_{\text{lat}}(\beta) > 0$. *(Note: Shen–Zhu–Zhu 2023 proves the Markov generator gap on $L^2(\mu_\infty)$ and Euclidean correlation clustering; it does not construct the quantum transfer matrix $\mathbb{T}$ or quantum Hamiltonian $H_{\text{lat}}$ on $\mathcal{H}_{\text{phys}}$, which is established separately by Lüscher 1977 and Osterwalder–Seiler 1978.)*
  - **Rigorous Scope:** $d \ge 2$, compact Lie groups $SU(N)$, infinite lattice $\mathbb{Z}^d$, strong coupling $\beta < \beta_0$.
  - **Boundary Limitation:** The Poincaré constant $C_{\text{PI}}(\beta)$ blows up as $\beta \to \beta_0$; completely inapplicable to the continuum trajectory $\beta \to \infty$.

### Family E: Expanded Area Law Regimes and Random Surface Representations (2025)
- **Primary Source E1:** Y. Cao, E. Nissim, S. Sheffield, *"Expanded Regimes of Area Law for Lattice Yang-Mills Theories"*, *arXiv:2505.16585* (2025).
  - **Citation Key:** `PAPER-MOD-008` / `THM-YM-0028`
  - **Mathematical Contribution:** Rigorous expansion of the coupling range $\beta$ exhibiting Wilson loop area law for classical Lie groups ($SU(N), SO(N), Sp(N)$); random surface representation bounding Wilson loops by minimal surfaces.
- **Primary Source E2:** Y. Cao, E. Nissim, S. Sheffield, *"A Dynamical Approach to Lattice Yang-Mills in the 't Hooft Limit"*, *arXiv:2505.16586* (2025).
  - **Citation Key:** `PAPER-MOD-009` / `THM-YM-0029`
  - **Mathematical Contribution:** Dynamical string and loop equation framework in the 't Hooft large-$N$ limit ($N \to \infty$, $\lambda = g^2 N$ fixed).
  - **Rigorous Scope:** Discrete lattice $a > 0$, expanded coupling domains.
  - **Boundary Limitation:** Proves **only** Wilson-loop area laws ($\sigma_{\text{lat}}(\beta) > 0$) for static quark loops; does **not** prove either a quantum Hamiltonian transfer-matrix spectral gap $\Delta_{\text{lat}}(\beta, a) > 0$ or a Markov generator gap $\operatorname{gap}(-\mathcal{L}) > 0$.

---

## 3. Decoupling and Source-to-Claim Correspondence Matrix (`YM-005-R2`)

To prevent conceptual conflation or unsupported theorem attribution, the five methodological families are strictly mapped across their exact proved mathematical claims:

| Comparative Dimension | Family A (Wilson 1974, `THM-YM-0008`) | Family B (Lüscher 1977; Osterwalder–Seiler 1978, `THM-YM-0009`) | Family C (Gross 1979; Seiler 1982, `THM-YM-0015`) | Family D (Shen–Zhu–Zhu 2023, `THM-YM-0027`) | Family E (Cao–Nissim–Sheffield 2025, `THM-YM-0028`) |
|---|---|---|---|---|---|
| **1. Primary Objective** | Formalize lattice gauge invariance & strong-coupling confinement | Establish reflection positivity (OS3), physical Hilbert space $\mathcal{H}_{\text{phys}}$, & transfer-matrix gap | Prove polymer cluster convergence, correlation decay, & transfer-matrix gap | Establish uniform Poincaré/log-Sobolev inequalities & Langevin generator gap | Expand rigorous Wilson-loop area-law parameter bounds |
| **2. Volume Regime** | Finite and formal infinite box | Finite spatial box (Lüscher) & infinite volume (Osterwalder–Seiler) | Infinite-volume thermodynamic limit $\Lambda \to \mathbb{Z}^d$ | Infinite-volume lattice $\mathbb{Z}^d$ | Infinite-volume lattice $\mathbb{Z}^d$ |
| **3. Coupling Range** | Strong coupling $\beta \ll 1$ | $\mathbb{T} > 0$ for all $0 < \beta < \infty$; gap for $0 < \beta \le \beta_0(d,G)$ | Strong coupling $0 \le \beta < \beta_0(d, G)$ | Strong coupling $0 \le \beta < \beta_0(d, G)$ | Expanded strong-coupling regime $0 \le \beta < \beta_1(d, G)$ |
| **4. Observable Controlled** | Planar Wilson loop $\langle W(C) \rangle$ | OS inner product $\langle \theta F, F \rangle$; Normalized transfer operator $\widehat{\mathbb{T}} = \mathbb{T}/\lambda_0$ | Truncated correlations $\langle A B \rangle_T$; Free energy $f(\beta)$; $\widehat{\mathbb{T}}$ | Variance $\text{Var}_\mu(F)$; Dirichlet form $\mathcal{E}(F,F)$; correlations | Wilson loop $\langle W(C) \rangle$; Dimensionless string tension $\sigma_{\text{lat}}$ |
| **5. Exact Gap / Decay Proved** | **Area law only:** $\sigma_{\text{lat}}(\beta) > 0$ (no Hamiltonian or Markov gap) | **Hamiltonian transfer-matrix gap:** $\Delta_{\text{lat}} = -\frac{1}{a}\ln(\lambda_1/\lambda_0) > 0$ ($\beta \le \beta_0$) & clustering $m_{\text{lat}} > 0$ | **Hamiltonian transfer-matrix gap:** $\Delta_{\text{lat}} = -\frac{1}{a}\ln(\lambda_1/\lambda_0) > 0$, clustering $m_{\text{lat}} > 0$, & area law $\sigma_{\text{lat}} > 0$ | **Markov generator gap:** $\operatorname{gap}_{L^2(\mu_\infty)}(-\mathcal{L}) \ge C_{\text{PI}}^{-1} > 0$ & clustering $m_{\text{lat}} > 0$ (**NOT** $H_{\text{lat}}$ directly) | **Area law only:** $\sigma_{\text{lat}}(\beta) \ge \sigma_0 > 0$ (no Hamiltonian or Markov gap) |
| **6. Terminal Open Boundary** | Expansion diverges as $\beta \to \infty$ | Does not bound gap $\Delta(a)$ as $a \to 0$ ($\beta \to \infty$) | Cluster expansion loses contractivity at $\beta_0$ | Curvature bound degenerates as $\beta \to \beta_0$ | Does not prove spectral mass gap or $a \to 0$ limit |

---

## 4. Governing Epistemic Invariants

Under **ROS v1.0**, **Universal Governance v4.0.3**, and **`YM-GOV-015`**, all analyses of these primary sources enforce four inviolable invariants:

1. **`INV-YM005-001` (Spectral Separation):**
   $$\boxed{\text{LATTICE\_SPECTRAL\_GAP } \Delta_{\text{lat}}(\beta, a) = -\frac{1}{a}\ln\!\left(\frac{\lambda_1(\beta)}{\lambda_0(\beta)}\right) > 0 \ne \text{CONTINUUM\_4D\_CLAY\_MASS\_GAP } \Delta > 0}$$
   A spectral gap established on a discrete lattice at fixed spacing $a > 0$ is a property of a regulated lattice Hamiltonian $H_{\text{lat}} = -\frac{1}{a}\ln(\mathbb{T}/\lambda_0)$, not of a continuum Wightman quantum field theory.

2. **`INV-YM005-002` (Strict Separation of Area Law, Hamiltonian Gap, and Markov Generator Gap):**
   $$\boxed{\langle W(C) \rangle \le C e^{-\sigma_{\text{lat}} \cdot \text{Area}(C)/a^2} \;\; \centernot\implies \;\; \Delta_{\text{lat}}(\beta, a) > 0, \qquad \operatorname{gap}_{L^2(\mu_\infty)}(-\mathcal{L}) \ne \Delta_{\text{lat}}(\beta, a)}$$
   The area law for Wilson loops (Wilson 1974; Cao–Nissim–Sheffield 2025), the Langevin diffusion generator gap on $L^2(\mu_\infty)$ (Shen–Zhu–Zhu 2023), and the quantum Hamiltonian transfer-matrix gap on $\mathcal{H}_{\text{phys}}$ (Osterwalder–Seiler 1978; Seiler 1982) are distinct mathematical objects proved by distinct theorems.

3. **`INV-YM005-003` (Quantitative Provenance Discipline):**
   All parameters are classified with explicit provenance (`PROVED_BY_SOURCE`, `PROJECT_ESTIMATE`, or `HEURISTIC_PHYSICAL_TRANSLATION`), and canonical theorem statements remain strictly dimensionless and symbolic ($\beta \le \beta_0(d, G) \ll 1$, fixed $a > 0$).

4. **`INV-YM005-004` (11-Dimensional Parameter Scope):**
   Every reconstructed theorem is cataloged with its full 11-dimensional parameter scope:
   `gauge group`, `dimension`, `lattice spacing`, `volume`, `coupling parameter`, `observable`, `gap/decay property`, `uniformity`, `continuum-limit status`, `what is proved`, `what remains open`.
