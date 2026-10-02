# YM-015R-CONTINUUM-RECONCILIATION — Continuum-Construction Stress Test and Scientific Repair

- **Document Identifier:** `YM-015R-CONTINUUM-RECONCILIATION`
- **Task Association:** `YM-015R — Post-Acceptance Stress Test and Scientific Repair`
- **Precursor Candidate SHA:** `e7edb4b57ec5feb9fd4d73f92290b819da35befd` (State Revision 31)
- **Governance Classification:** Formal Scientific Repair and Theorem Amendment Ledger
- **Status:** `SCIENTIFIC_RECONCILIATION_COMPLETED`

---

## 1. Executive Summary & Audit Mandate

Following the technical acceptance of Task `YM-015` at State Revision 31, a post-acceptance adversarial stress test was conducted on all load-bearing claims of the UV continuum field construction (`E-UV-FREE-CONT`).

The investigation revealed that while finite-lattice discrete invariance and two-loop asymptotic freedom are rigorous, multiple central claims of `YM-015` were **promoted beyond their mathematical evidence**:
1. **Theorem `YM-015-L3` (Reflection Positivity) is REFUTED in its claim of exact reflection positivity on the buffered algebra:** Parabolic gradient flow has infinite support ($K_t(x-y) \propto e^{-|x-y|^2/(4t)} > 0$ for all $x \neq y$). The root-mean-square smoothing radius $R_{\mathrm{diff}} = \sqrt{8t}$ is NOT a compact support boundary. Observables at $x_4 > 0$ depend on gauge links in $x_4 < 0$, violating $A \in \mathcal{A}_+$. Exact Osterwalder–Schrader reflection positivity (OS2) is **NOT** preserved at any finite flow time $t > 0$.
2. **Theorem `YM-015-L1` (Uniform Smeared Schwinger Bound) is DOWNGRADED:** The claimed deterministic operator bound $\sup_x |\mathcal{E}_a(x; t)| \le C_{\mathrm{flow}}/t^2$ uniformly for all $U \in \Omega_a$ conflated perturbative / small-field smoothing with a non-perturbative operator bound. On rough, non-perturbative lattice configurations, this estimate was ASSUMED without a non-perturbative flow theorem.
3. **Theorem `YM-015-L2` (Subsequential Limit & Topology) is REPAIRED:** A multilinear bound $|\Phi(f_1, \dots, f_k)| \le C \prod \|f_i\|_{H^3}$ places $\Phi$ in the dual of the projective Banach tensor product $(H^3)^{\hat{\otimes}_\pi k}$, **NOT** in the product Sobolev space $H^{-3}((\mathbb{T}^4)^k)$. By the Schwartz kernel theorem on the nuclear space $C^\infty(\mathbb{T}^4)$, it defines a distribution in $\mathcal{D}'((\mathbb{T}^4)^k)$. However, a subsequential limit of multilinear functionals does NOT constitute a full "Schwinger function system" because reflection positivity (OS2) fails and clustering/spectral gap (OS4) is open.
4. **Theorem `YM-015-L4` (Continuous Translation Covariance) is CONFIRMED CONDITIONALLY:** Discrete lattice translation invariance is an exact symmetry of the Wilson action on the torus, and fractional shift Sobolev estimates vanish as $O(a)$. This proof survives independently of L3 or L5, conditioned only on the continuity of the functional (L1).
5. **Theorem `YM-015-L5` (SO(4) Restoration) is DOWNGRADED to `PERTURBATIVE_SUPPORT_ONLY`:** Symanzik effective field theory is an asymptotic expansion in perturbation theory. Proving that non-perturbative lattice path integrals converge to $SO(4)$-invariant distributions requires non-perturbative bounds on dimension-6 operator coefficients, which have not been proved.
6. **Theorem `YM-015-W1` (Nontriviality Witness) is DOWNGRADED to `FINITE_CUTOFF_NONDEGENERACY_ONLY`:** While $\operatorname{Var}_{\mu_a}(\mathcal{O}_a(f)) > 0$ holds at each finite cutoff $a > 0$, the continuum lower bound $\inf_a \operatorname{Var}_a > 0$ relied on Lüscher's perturbative formula without non-perturbative control over remainders.
7. **Harold D. Kirk (2026) Monograph Audit is NARROWED:** Kirk Lemmas 8 and 9 are downgraded from "Independently Confirmed" to `PERTURBATIVE_SUPPORT_ONLY`, and Kirk Lemma 10 is formally classified as `REFUTED`.
8. **Missing-Bridge Edge `E-UV-FREE-CONT` is RECLASSIFIED:** The status `SUBSEQUENTIAL_CONTINUUM_LIMIT_PROVED_FINITE_VOLUME` is downgraded to:
   $$\mathbf{PRECOMPACT\_FLOWED\_MULTILINEAR\_LIMIT\_WITH\_UNRESOLVED\_RP\_AND\_SO4}.$$
   The edge remains **`OPEN_AND_UNRESOLVED`** for the construction of a genuine Osterwalder–Schrader quantum field theory.

---

## 2. Granular Re-Audit of Theorem YM-015-L1 (Uniform Smeared Bound)

### 2.1 The Claimed Estimate
Theorem `YM-015-L1` asserted:
$$\sup_{0 < a \le a_0} \left| \left\langle \prod_{i=1}^k \mathcal{O}_{a, t_i}(f_i) \right\rangle_{\mu_a} \right| \le \frac{K_k(N) L_{\mathrm{phys}}^{4k}}{\prod_{i=1}^k t_i^2} \prod_{i=1}^k \|f_i\|_{H^3(\mathbb{T}_{\mathrm{phys}}^4)}.$$

### 2.2 First-Principles Step-by-Step Epistemic Audit

| Derivation Step | Mathematical Formulation | Epistemic Classification | Justification & Failure Locality |
| :--- | :--- | :--- | :--- |
| **Step 1: Compact Group Holonomy** | $\|Q_{\mu\nu}(x; t) - I_N\|_{\mathrm{HS}} \le 2\sqrt{N}$ | `FINITE_LATTICE_EXACT` | Trivial consequence of compactness of $SU(N)$ and eigenvalues on the unit circle. Gives $|G_{\mu\nu}^a| \le C/a^2$ at finite $a$. |
| **Step 2: Deterministic Smoothing Bound** | $\sup_x |\mathcal{E}_a(x; t)| \le \frac{C_{\mathrm{flow}}(N)}{t^2} \; \forall U \in \Omega_a$ | **`ASSUMED` / `PERTURBATIVE_ONLY`** | **FATAL GAP:** Lüscher (JHEP 08 (2010) 071) establishes all-orders perturbative finiteness. Classical smooth Yang–Mills flow satisfies smoothing only below the energy bubbling threshold (Struwe 1994). On rough lattice configurations $U$, $|G^2| \le C/a^4$ deterministically, not $C/t^2$. Uniformity across all $U \in \Omega_a$ is unproved non-perturbatively. |
| **Step 3: Sobolev Embedding on Torus** | $\|f\|_{L^1(\Lambda_a)} \le C_{\mathrm{Sob}} L_{\mathrm{phys}}^4 \|f\|_{H^3(\mathbb{T}^4)}$ | `FINITE_LATTICE_EXACT` | Standard Riemann sum bound and Sobolev embedding $H^3(\mathbb{T}^4) \hookrightarrow C^0(\mathbb{T}^4)$ for $s = 3 > d/2 = 2$. |
| **Step 4: Hölder Expectation Factorization** | $|\langle \prod \mathcal{O}_i \rangle| \le \prod \|\mathcal{O}_i\|_{L^k(\mu_a)}$ | `FINITE_LATTICE_EXACT` | Exact generalized Hölder inequality on the probability space $(\Omega_a, d\mu_a)$. |
| **Step 5: Uniform Constant Synthesis** | $C_k = \frac{K_k(N) L_{\mathrm{phys}}^{4k}}{\prod t_i^2}$ independent of $a$ | **`CONDITIONAL_ON_STEP_2`** | Because Step 2 is unproved on non-perturbative rough configurations, the $a$-independence of $C_k$ is conditional on small-field / perturbative control. |

### 2.3 Disposition of YM-015-L1
- **Former Status:** `MATHEMATICALLY_PROVED_IN_BOUNDED_UV_REGIME`
- **Amended Status:** **`DOWNGRADED_TO_PERTURBATIVE_AND_SMALL_FIELD_REGIME`**
- **Amendment Classification:** `AMENDMENT_L1_CONDITIONAL_ON_NONPERTURBATIVE_FLOW_BOUND`

---

## 3. Repair of Functional-Analysis Topology in Theorem YM-015-L2

### 3.1 The Fallacy in the Product Sobolev Identification
`YM-015-DISTRIBUTIONAL-COMPACTNESS.md` asserted (Equation 90):
$$\mathcal{H}_k := H^3(\mathbb{T}_{\mathrm{phys}}^4) \otimes \cdots \otimes H^3(\mathbb{T}_{\mathrm{phys}}^4) \cong H^3((\mathbb{T}_{\mathrm{phys}}^4)^k).$$
This assertion is **MATHEMATICALLY FALSE**.

#### Mathematical Proof of Non-Isomorphism:
Let $M = \mathbb{T}^4$. The Fourier representation of the Sobolev norm on $M \times M$ is:
$$\|f\|_{H^s(M \times M)}^2 = \sum_{p, q \in \mathbb{Z}^4} \left( 1 + |p|^2 + |q|^2 \right)^s |\hat{f}(p, q)|^2.$$
In contrast, the Hilbert space tensor product $H^s(M) \otimes_2 H^s(M)$ has norm:
$$\|f\|_{H^s(M) \otimes_2 H^s(M)}^2 = \sum_{p, q \in \mathbb{Z}^4} \left( 1 + |p|^2 \right)^s \left( 1 + |q|^2 \right)^s |\hat{f}(p, q)|^2.$$
Because $(1 + |p|^2)^s (1 + |q|^2)^s = 1 + |p|^2 + |q|^2 + |p|^2 |q|^2 \ge 1 + |p|^2 + |q|^2$, the space $H^s(M) \otimes_2 H^s(M)$ is the space of functions with **dominating mixed derivatives** $H^{s, s}_{\mathrm{mix}}(M \times M)$.
The topological inclusions are:
$$H^{2s}(M \times M) \subsetneq H^s(M) \otimes_2 H^s(M) \subsetneq H^s(M \times M).$$
Therefore, a bounded multilinear functional on $H^3 \times \cdots \times H^3$ does **NOT** belong to $H^{-3}((\mathbb{T}^4)^k)$!

### 3.2 Rigorous Functional Spaces and Duality
1. **Projective Banach Tensor Product:**
   A multilinear functional $\Phi : (H^3)^k \to \mathbb{R}$ satisfying:
   $$|\Phi(f_1, \dots, f_k)| \le C \prod_{i=1}^k \|f_i\|_{H^3}$$
   uniquely defines a continuous linear functional on the **projective Banach tensor product**:
   $$\mathcal{H}_\pi^{(k)} := H^3(\mathbb{T}_{\mathrm{phys}}^4) \hat{\otimes}_\pi \cdots \hat{\otimes}_\pi H^3(\mathbb{T}_{\mathrm{phys}}^4), \qquad \|\Phi\|_{(\mathcal{H}_\pi^{(k)})^*} = \sup_{\|f_i\|_{H^3} \le 1} |\Phi(f_1, \dots, f_k)| \le C.$$
2. **Schwartz Kernel Theorem on Nuclear Spaces:**
   The smooth test-function space $C^\infty(\mathbb{T}^4)$ is a **nuclear Fréchet space**. By the Grothendieck–Schwartz Kernel Theorem:
   $$C^\infty(\mathbb{T}^4) \hat{\otimes}_\pi \cdots \hat{\otimes}_\pi C^\infty(\mathbb{T}^4) \cong C^\infty((\mathbb{T}^4)^k).$$
   Every continuous multilinear functional on $(C^\infty(\mathbb{T}^4))^k$ extends to a unique generalized distribution in:
   $$\mathcal{D}'((\mathbb{T}_{\mathrm{phys}}^4)^k).$$
3. **Compactness vs. Schwinger System:**
   - **Weak-* Precompactness:** Holds on equicontinuous sets in $\mathcal{D}'((\mathbb{T}^4)^k)$ and on the closed unit ball of $(\mathcal{H}_\pi^{(k)})^*$.
   - **Non-Equivalence to Schwinger System:** Extracting a subsequence $\Phi_{n_j}^{(k)} \to S_k$ establishes only a collection of multilinear distributions. It does NOT establish a physical Schwinger system until:
     * Axiom OS1 (continuous Euclidean invariance) is proved non-perturbatively;
     * Axiom OS2 (exact reflection positivity) is proved;
     * Axiom OS3 (permutation symmetry) is verified;
     * Axiom OS4 (clustering in infinite volume) is proved.

### 3.3 Disposition of YM-015-L2
- **Former Status:** `MATHEMATICALLY_PROVED_IN_BOUNDED_UV_REGIME`
- **Amended Status:** **`SUBSEQUENTIAL_MULTILINEAR_DISTRIBUTION_EXTRACTION_ON_FLOWED_OBSERVABLES`**
- **Amendment Classification:** `AMENDMENT_L2_PROJECTIVE_TENSOR_DUALITY_REPAIR`

---

## 4. Formal Refutation and Re-Opening of Theorem YM-015-L3 (Reflection Positivity)

### 4.1 The Fundamental Geometric/PDE Contradiction
Theorem `YM-015-L3` asserted that for test functions $f$ supported at distance $\delta > \sqrt{8t}$ from the time reflection hyperplane $\Sigma_0 = \{x_4 = 0\}$, the flowed observable $\mathcal{O}_{a, t}(f)$ belongs to the Osterwalder–Schrader positive-time algebra $\mathcal{A}_+$, ensuring exact reflection positivity:
$$\sum_{i, j} \overline{c_i} c_j S_2(t_i, t_j)(\Theta f_i \otimes f_j) \ge 0.$$

This assertion is **FLAWED AND REFUTED**.

#### Mathematical Proof of Refutation:
1. **Infinite Propagation Speed of Parabolic Heat Kernels:**
   The non-Abelian Yang–Mills gradient flow $\partial_t B_\mu = D_\nu G_{\nu\mu}$ has linearized leading-order evolution governed by the continuous heat operator on $\mathbb{R}^4$:
   $$K_t(x - y) = \frac{1}{(4\pi t)^2} \exp\left( -\frac{|x - y|^2}{4t} \right).$$
   For ANY flow time $t > 0$ and ANY physical separation $|x - y| > 0$:
   $$K_t(x - y) > 0 \quad \text{strictly everywhere on } \mathbb{T}^4.$$
2. **Support Non-Compactness:**
   The root-mean-square diffusion length $R_{\mathrm{diff}} = \sqrt{8t}$ is the second moment of the Gaussian distribution $\langle |x|^2 \rangle = 8t$. It is **NOT** a support radius:
   $$\operatorname{supp}(K_t) = \mathbb{T}^4 \quad (\text{the entire manifold}).$$
3. **Dependence on Negative-Time Links:**
   Let $x = (x_1, x_2, x_3, x_4)$ with $x_4 = \delta > \sqrt{8t} > 0$.
   The flowed field $B_\mu(x; t)$ receives contributions from initial gauge links $A_\nu(y)$ at all points $y \in \mathbb{T}^4$. In particular, for points $y$ in the negative Euclidean time half-space:
   $$\Lambda_{a, -} = \{ y \in \Lambda_a : -L_{\mathrm{phys}}/2 < y_4 < 0 \},$$
   the functional derivative of the flowed link with respect to negative-time bare links is strictly non-zero:
   $$\frac{\delta V_t(x, \mu)}{\delta U(y, \nu)} \sim K_t(x - y) \neq 0 \quad \forall y \in \Lambda_{a, -}.$$
4. **Violation of the Positive-Time Algebra $\mathcal{A}_+$:**
   By definition, the Osterwalder–Schrader positive-time algebra is:
   $$\mathcal{A}_+ := \operatorname{alg}\left\{ F[U] : F \text{ depends strictly on links } U(y, \mu) \text{ with } y_4 \ge 0 \text{ and } y_4 + a\hat{\mu}_4 \ge 0 \right\}.$$
   Because $V_t(x, \mu)$ depends analytically on links in $\Lambda_{a, -}$, for any flowed observable:
   $$\mathcal{O}_{a, t}(f) \notin \mathcal{A}_+ \quad \forall t > 0, \;\forall \delta < \infty.$$
5. **Breakdown of Osterwalder–Seiler Factorization:**
   The Osterwalder–Seiler lattice reflection positivity proof relies on the factorization of the Haar measure and Boltzmann weight across the time reflection hyperplanes $\Sigma_0 = \{x_4 = 0\}$ and $\Sigma_{1/2} = \{x_4 = L_{\mathrm{phys}}/2\}$:
   $$\langle \Theta(A) B \rangle = \int d\mu_{\Sigma_0} d\mu_{\Sigma_{1/2}} \left( \int_{\Lambda_+} d\mu_+ \, \overline{\Theta(A)} \right) \left( \int_{\Lambda_+} d\mu_+ \, B \right).$$
   When $A$ depends on links in $\Lambda_-$, $\Theta(A)$ depends on links in $\Lambda_+$. Thus, $\Theta(A)$ and $A$ depend on the **SAME** links in both half-spaces!
   The integral does not factorize, and the positivity of the transfer matrix cannot be applied.
6. **Quantification of the Reflection Positivity Defect:**
   The probability mass of the heat kernel leaking across the boundary into the negative half-space is:
   $$P_{\mathrm{leak}}(t, \delta) = \int_{-\infty}^0 \frac{1}{\sqrt{4\pi t}} e^{-(x_4 - y_4)^2 / (4t)} dy_4 = \frac{1}{2} \operatorname{erfc}\left( \frac{\delta}{\sqrt{4t}} \right).$$
   For $\delta = \sqrt{8t}$, this gives:
   $$\frac{\delta}{\sqrt{4t}} = \sqrt{2} \approx 1.414 \implies P_{\mathrm{leak}} = \frac{1}{2} \operatorname{erfc}(\sqrt{2}) \approx 0.0228 \neq 0.$$
   The reflection positivity bilinear form evaluates to:
   $$\langle \Theta(\mathcal{O}_t(f)) \mathcal{O}_t(f) \rangle_{\mu_a} = (\text{Positive}) - \Delta_{\mathrm{RP}}(t, \delta),$$
   where $\Delta_{\mathrm{RP}}(t, \delta) \sim O\left( e^{-\delta^2 / (4t)} \right)$ is **strictly non-zero**.
   In constructive axiomatic QFT, an inequality holding up to an exponentially small error is **NOT AN AXIOM**. The Osterwalder–Schrader reconstruction theorem strictly requires:
   $$\langle \Theta(A) A \rangle \ge 0 \quad \text{identically with ZERO defect}.$$

### 4.2 Disposition of YM-015-L3
- **Former Status:** `MATHEMATICALLY_PROVED_WITH_SUPPORT_BUFFER`
- **Amended Status:** **`REFUTED_FOR_EXACT_RP_AT_FINITE_FLOW_TIME`**
- **Amendment Classification:** `AMENDMENT_L3_HEAT_KERNEL_NONLOCALITY_REFUTATION`

---

## 5. Re-Audit of Theorem YM-015-L4 (Continuous Translation Covariance)

### 5.1 First-Principles Reconstruction
Theorem `YM-015-L4` asserted that the continuum distributions satisfy:
$$S_k(\tau_h f_1, \dots, \tau_h f_k) = S_k(f_1, \dots, f_k) \quad \forall h \in \mathbb{R}^4.$$

### 5.2 Independent Verification
1. **Exact Lattice Symmetries:**
   On the hypercubic lattice $\Lambda_a = (\mathbb{Z}/(L/a)\mathbb{Z})^4$ with periodic boundary conditions, discrete translation by any lattice vector $v = a n \in a\mathbb{Z}^4$ is an exact measure-preserving automorphism:
   $$S_W(\tau_v U) = S_W(U), \qquad d\mu_{\Lambda_a, \beta}(\tau_v U) = d\mu_{\Lambda_a, \beta}(U).$$
   Therefore, for every finite lattice spacing $a_n > 0$:
   $$\left\langle \prod_{i=1}^k \mathcal{O}_{a, t_i}(\tau_v f_i) \right\rangle_{\mu_a} = \left\langle \prod_{i=1}^k \mathcal{O}_{a, t_i}(f_i) \right\rangle_{\mu_a} \quad \forall v \in a\mathbb{Z}^4.$$
2. **Fractional Shift Decomposition:**
   For any physical displacement $h \in \mathbb{R}^4$, decompose $h = a n(h) + \epsilon(h, a)$ with $n(h) \in \mathbb{Z}^4$ and $\epsilon(h, a) \in [-a/2, a/2]^4$.
   The fractional shift has norm $\|\epsilon(h, a)\| \le \frac{\sqrt{d}}{2} a = a$.
3. **Test Function Continuity:**
   By Taylor's theorem on $C^\infty(\mathbb{T}^4)$:
   $$\|\tau_\epsilon f - f\|_{C^0} \le a \|\nabla f\|_{C^0} \le a C_{\mathrm{Sob}} \|f\|_{H^3}.$$
   By multilinear telescoping:
   $$\left| \Phi_a(\tau_h f_1, \dots, \tau_h f_k) - \Phi_a(f_1, \dots, f_k) \right| \le C_k a \sum_{i=1}^k \|f_i\|_{H^4} \prod_{j \neq i} \|f_j\|_{H^3} \xrightarrow{a \to 0} 0.$$
4. **Independence of Questionable Steps:**
   This proof depends strictly on:
   - Discrete translation invariance of the lattice action (exact);
   - Uniform continuity of the multilinear functional (conditional on L1).
   It does **NOT** depend on reflection positivity (L3) or $SO(4)$ restoration (L5).

### 5.3 Disposition of YM-015-L4
- **Former Status:** `MATHEMATICALLY_PROVED_IN_BOUNDED_UV_REGIME`
- **Amended Status:** **`CONFIRMED_CONDITIONALLY_ON_L1`**
- **Amendment Classification:** `AMENDMENT_L4_TRANSLATION_COVARIANCE_SURVIVES`

---

## 6. Re-Audit of Theorem YM-015-L5 (SO(4) Rotational Restoration)

### 6.1 Demarcation of Three Logical Statements
Theorem `YM-015-L5` claimed exact continuous $SO(4)$ rotational covariance in the continuum limit. To determine its mathematical standing, three distinct statements must be separated:

1. **Statement 1: Representation-Theoretic Classification (Standard & Valid):**
   Under the hypercubic subgroup $H_4 \subset SO(4)$, the irreducible representations of $SO(4)$ decompose:
   $$\mathbf{35} \longrightarrow \mathbf{1} \oplus \mathbf{2} \oplus \mathbf{3} \oplus \mathbf{3} \oplus \mathbf{6} \oplus \mathbf{8} \oplus \dots$$
   Gauge-invariant operators of mass dimension $\le 4$ on hypercubic lattices belong exclusively to the trivial singlet $\mathbf{1}$ of $SO(4)$. The lowest-dimension non-singlet operator breaking $SO(4) \to H_4$ has mass dimension 6:
   $$\mathcal{O}_{\mathrm{aniso}}^{(6)}(x) = \sum_{\mu, \nu} \operatorname{Tr}\left( D_\mu F_{\mu\nu} D_\mu F_{\mu\nu} \right).$$
   *Classification:* `PROVED_REPRESENTATION_THEORY`.

2. **Statement 2: Symanzik Perturbative Effective Action (Perturbative Expectation):**
   In perturbation theory, the effective lattice action expands as $S_{\mathrm{eff}} = S_{\mathrm{cont}} + a^2 \int d^4 x \, c_6 \mathcal{O}^{(6)} + O(a^4)$.
   By power counting, dimension-6 operators have classical RG dimension $-2$ and contract as $O(a^2)$ up to logarithmic corrections.
   *Classification:* `PERTURBATIVE_EXPANSION_ONLY`.

3. **Statement 3: Rigorous Non-Perturbative Spacing-Uniform Estimate (Missing):**
   To close the continuum missing bridge non-perturbatively, one must prove:
   $$\left| \langle \prod \mathcal{O}(R f_i) \rangle_{\mu_a} - \langle \prod \mathcal{O}(f_i) \rangle_{\mu_a} \right| \le C \frac{a^2}{t_{\min}} \prod \|f_i\|_{H^4}$$
   directly from the lattice measure $\mu_a$, with $C$ uniform across bare coupling, volume, and RG depth, taking into account large-field configurations.
   *Classification:* `UNPROVED_NONPERTURBATIVELY`.

### 6.2 Disposition of YM-015-L5
- **Former Status:** `MATHEMATICALLY_PROVED_IN_BOUNDED_UV_REGIME`
- **Amended Status:** **`PERTURBATIVE_SUPPORT_ONLY`**
- **Amendment Classification:** `AMENDMENT_L5_SO4_RESTORATION_PERTURBATIVE_ONLY`

---

## 7. Re-Audit of Theorem YM-015-W1 (Nontriviality Witness)

### 7.1 Finite Cutoff vs. Continuum Limit
Theorem `YM-015-W1` asserted:
$$S_2^c(t_{\mathrm{phys}}, t_{\mathrm{phys}})(f \otimes f) \ge c_0(t, f, N) > 0 \quad \forall f \ge 0, \; f \not\equiv 0.$$

### 7.2 Defect Analysis
1. At finite lattice spacing $a > 0$, the measure $\mu_a$ has full support on the compact group manifold $SU(N)^E$ with strictly positive Boltzmann weight $\exp(-\beta S_W) > 0$. Since $\mathcal{O}_a(f)$ is a non-constant polynomial function, its variance is strictly positive:
   $$\operatorname{Var}_{\mu_a}(\mathcal{O}_a(f)) > 0 \quad \forall a > 0.$$
2. However, the claim that $\lim_{a \to 0} \operatorname{Var}_{\mu_a}(\mathcal{O}_a(f)) \ge c_0 > 0$ was derived by substituting Lüscher's perturbative formula $\langle \mathcal{E}(x; t) \mathcal{E}(y; t) \rangle_{\mathrm{conn}} = \frac{3(N^2-1) g^4(t)}{128 \pi^4 t^4} H + O(g^6)$ and asserting that the leading order dominates.
3. This assumes the very continuum limit being constructed and assumes that non-perturbative large-field corrections cannot cancel the perturbative variance.
4. Furthermore, claiming positivity for *every* non-negative test function $f$ exceeds available evidence: non-triviality requires only the existence of at least *one* test function $f$ with non-zero limit.

### 7.3 Disposition of YM-015-W1
- **Former Status:** `NONTRIVIALITY_WITNESS_PROVED_AT_TWO_POINT_LEVEL`
- **Amended Status:** **`FINITE_CUTOFF_NONDEGENERACY_ONLY`**
- **Amendment Classification:** `AMENDMENT_W1_NONTRIVIALITY_WITNESS_DOWNGRADE`

---

## 8. Comprehensive Re-Audit of Harold D. Kirk (2026) Imports

| Lemma ID & Topic | Original Claim in Kirk (2026) | YM-015 Classification | YM-015R Re-Audit Verdict | Surviving Epistemic Scope |
| :--- | :--- | :--- | :--- | :--- |
| **KIRK-LEMMA-4** (Tightness) | Weak-* compactness in $\mathcal{D}'(\mathbb{T}^4)$ | `IMPORTED` | **`CONDITIONALLY_PRECOMPACT_ONLY`** | Precompactness of multilinear forms on flowed operators holds conditionally on L1; does not yield a full Schwinger system. |
| **KIRK-LEMMA-6** (2-Loop Beta Running) | Asymptotic freedom scaling $g_0^2(a) \to 0$ | `IMPORTED` | **`VALID_STANDARD`** | Standard 2-loop perturbative asymptotic freedom in 4D $SU(N)$. |
| **KIRK-LEMMA-7** (Translation Covariance) | Fractional shift estimate $\tau_h - I \sim O(|h|)$ | `IMPORTED` | **`CONFIRMED_CONDITIONALLY_ON_L1`** | Independent derivation verified; independent of L3/L5. |
| **KIRK-LEMMA-8** (Dim-6 Hypercubic Suppression) | $O(a^2)$ suppression of non-$SO(4)$ operators | `IMPORTED` | **`PERTURBATIVE_SUPPORT_ONLY`** | Symanzik effective field theory is perturbative; non-perturbative bound unproved. |
| **KIRK-LEMMA-9** (SO(4) Restoration) | $SO(4)$ covariance in finite volume | `IMPORTED` | **`PERTURBATIVE_SUPPORT_ONLY`** | Consequence of Lemma 8; unproved non-perturbatively. |
| **KIRK-LEMMA-10** (Reflection Positivity) | RP without support buffer | `REJECTED` (Required buffer) | **`REFUTED_ALL_VERSIONS`** | Both Kirk's unbuffered claim and YM-015's buffered claim are refuted by heat-kernel non-compactness. |

---

## 9. Comprehensive Theorem Amendment Summary

| Theorem / Claim ID | Original Status (Rev 31) | Amended Status (Rev 31R) | Action Code | Epistemic Summary |
| :--- | :--- | :--- | :--- | :--- |
| **`YM-015-L1`** | `PROVED` | `DOWNGRADED_TO_PERTURBATIVE_AND_SMALL_FIELD` | `NEEDS_AMENDMENT` | Uniform $C_k$ bound is conditional on non-perturbative flow contractivity. |
| **`YM-015-L2`** | `PROVED` | `REPAIRED_PROJECTIVE_TENSOR_DUALITY` | `NEEDS_AMENDMENT` | Dual space is $(\mathcal{H}_\pi^{(k)})^*$ and $\mathcal{D}'((\mathbb{T}^4)^k)$, not $H^{-3}((\mathbb{T}^4)^k)$. |
| **`YM-015-L3`** | `PROVED` | `REFUTED` | `REFUTED` | 4D gradient flow violates exact OS reflection positivity for all finite buffers $\delta < \infty$. |
| **`YM-015-L4`** | `PROVED` | `CONFIRMED_CONDITIONALLY_ON_L1` | `CONFIRMED_WITH_NARROWER_SCOPE` | Continuous translation covariance verified; conditioned on functional continuity. |
| **`YM-015-L5`** | `PROVED` | `PERTURBATIVE_SUPPORT_ONLY` | `NEEDS_AMENDMENT` | Symanzik $O(a^2)$ suppression is perturbative, not a non-perturbative theorem. |
| **`YM-015-W1`** | `PROVED` | `FINITE_CUTOFF_NONDEGENERACY_ONLY` | `NEEDS_AMENDMENT` | Variance $> 0$ proved at finite $a$; continuum uniform lower bound unproved non-perturbatively. |

---

## 10. Recalculation of Missing-Bridge Edge Status

### 10.1 Edge `E-UV-FREE-CONT` Disposition
- **Previous Recorded Status:** `SUBSEQUENTIAL_CONTINUUM_LIMIT_PROVED_FINITE_VOLUME`
- **Re-Audited Status:**
  $$\mathbf{PRECOMPACT\_FLOWED\_MULTILINEAR\_LIMIT\_WITH\_UNRESOLVED\_RP\_AND\_SO4}$$
- **Missing-Bridge Status:** **`OPEN_AND_UNRESOLVED`**

The edge `E-UV-FREE-CONT` was prematurely marked as closed. While subsequential extraction of flowed multilinear distributions is mathematically sound, it does **NOT** construct an Osterwalder–Schrader quantum field theory because:
1. Exact reflection positivity (OS2) is broken by the non-local parabolic tails of the 4D flow;
2. Continuous $SO(4)$ covariance (OS1) is supported only perturbatively;
3. Spacing-uniform non-perturbative bounds (L1) require a non-perturbative flow theorem.

### 10.2 Global Program Invariants
- `goal_complete`: **`false`**
- `clay_problem`: **`OPEN_AND_UNSOLVED`**
- `P3`: **`OPEN`**
- `E-CROSSOVER`: **`OPEN`**
- `STRUCTURAL_NO_GO_COUNT`: **`0`**
- `YM-016`: **`BLOCKED_PENDING_YM-015R`**
