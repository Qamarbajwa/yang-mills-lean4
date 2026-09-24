# Task YM-011: First Load-Bearing Bridge Lemma Specification & Verified Precursor (`YM-011-PRE`)

- **TASK_ID:** `YM-011` (with Verified Fixed-Lattice Precursor `YM-011-PRE`)
- **YM-011_STATUS:** `PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`
- **PRECURSOR_STATUS (`YM-011-PRE`):** `SCIENTIFICALLY_VERIFIED_FIXED_LATTICE_PRECURSOR`
- **GOVERNANCE_TIER:** `R2` (Bounded Mathematical Lemma Formulation under `YM-GOV-014`)
- **DATE:** 2026-09-24
- **PREREQUISITE_DEPENDENCY:** `YM-004` (Bałaban's Multiscale RG Program) and `YM-011-PRE` (Fixed-Lattice Gradient-Flow Loop Perturbation)
- **TARGET_GOAL:** Establish and verify the elementary fixed-lattice gradient-flow loop perturbation precursor (`YM-011-PRE`) before any future activation of the multiscale Bałaban-measure lemma (`YM-011-L1`), without assuming a continuum mass gap.

---

## 1. Context & Architectural Isolation

The failure of previous global proof attempts (`YM-009`, `YM-010`) demonstrated that attempting to prove full non-perturbative gluing and the continuum mass gap simultaneously leads to circular reasoning, unjustified error bounds, and invalid variational inversions. Furthermore, the `YM-GOV-013` audit demonstrated that an exponential decay bound of the form $\frac{a}{|C|} \exp(-c_2 |C|^2 / t(a))$ on the difference $|\langle W_{t(a)}(C)\rangle - \langle W_0(C)\rangle|$ is mathematically implausible because for $t(a) = c_0 a^2 \to 0$ it confuses the Gaussian heat-kernel tail in spatial separation with the Taylor remainder in flow time $t$, which is linear in $t$.

Per **`YM-GOV-014` Section 5**, `YM-011` remains strictly **`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`**, and we first formulate, prove, and deterministically verify the elementary fixed-lattice precursor lemma **`YM-011-PRE` (`Fixed-Lattice Gradient-Flow Loop Perturbation`)**.

---

## 2. Verified Precursor Lemma: `YM-011-PRE` / `YM-011-PRE-R1` (Fixed-Lattice Gradient-Flow Loop Perturbation)

### 2.1 Exact Mathematical Statement (`YM-011-PRE-R1`)

Let $\Lambda \subset a\mathbb{Z}^d$ ($d \ge 2$, specifically $d=4$) be a finite hypercubic lattice with spacing $a > 0$ and compact gauge group $G = SU(N)$ ($N \ge 2$). Let $S_W(U) = \frac{\beta}{N} \sum_{p \subset \Lambda} \operatorname{Re}\operatorname{Tr}(I_N - U_p)$ be the standard Wilson plaquette action with bare coupling $\beta = \frac{2N}{g_0^2} > 0$, and let $d\mu_\Lambda(U) = Z_\Lambda^{-1} e^{-S_W(U)} \prod_{\ell \in E(\Lambda)} dU_\ell$ be the fixed-lattice probability measure on $\Omega_\Lambda = SU(N)^{E(\Lambda)}$.

For any closed lattice loop $C = (\ell_1, \ell_2, \dots, \ell_n)$ composed of $n = |C|/a$ oriented lattice links with holonomy $H_t(C) := \prod_{m=1}^n V_t(\ell_m) \in SU(N)$, distinguish the two normalized Wilson loop observables:
1. **Generally Complex Normalized Wilson Trace:**
   $$W_t^{\mathbb{C}}(C)[U] := \frac{1}{N} \operatorname{Tr}\!\left( H_t(C) \right) = \frac{1}{N} \sum_{j=1}^N e^{i\theta_j} \in \Phi_N \subset \overline{\mathbb{D}}_1 := \{z \in \mathbb{C} : |z| \le 1\},$$
   where $\Phi_N$ is the compact $N$-cusped hypocycloid region in the closed unit disk $\overline{\mathbb{D}}_1$ (for $N=2$, $\Phi_2 = [-1, 1] \subset \mathbb{R}$ is real; for $N \ge 3$, $W_t^{\mathbb{C}}(C)$ is genuinely complex-valued with $W_t^{\mathbb{C}}(C^{-1}) = \overline{W_t^{\mathbb{C}}(C)}$).
2. **Real Normalized Wilson Trace ($W_t(C) := W_t^{\mathbb{R}}(C)$):**
   $$W_t(C)[U] := W_t^{\mathbb{R}}(C)[U] = \operatorname{Re} W_t^{\mathbb{C}}(C)[U] = \frac{1}{N} \operatorname{Re}\operatorname{Tr}\!\left( H_t(C) \right) = \frac{1}{N} \sum_{j=1}^N \cos\theta_j \in \left[\min_{H \in SU(N)} \frac{1}{N}\operatorname{Re}\operatorname{Tr} H, \, 1\right] \subseteq [-1, 1].$$

**Theorem (`YM-011-PRE-R1`):**
For every flow time $t \ge 0$, every lattice gauge configuration $U \in SU(N)^{E(\Lambda)}$, and every closed loop $C$ of length $n = |C|/a$ links, both the complex trace $W_t^{\mathbb{C}}(C)$ and the real trace $W_t^{\mathbb{R}}(C)$ satisfy the **pointwise configuration bound**:
$$\boxed{\left| W_t^{\mathbb{R}}(C)[U] - W_0^{\mathbb{R}}(C)[U] \right| \le \left| W_t^{\mathbb{C}}(C)[U] - W_0^{\mathbb{C}}(C)[U] \right| \le K(\beta, d, N) \, n \, \frac{t}{a^2}}$$
and the **expectation-level bound** with respect to $d\mu_\Lambda$:
$$\boxed{\left| \langle W_t^{\mathbb{R}}(C) \rangle_\Lambda - \langle W_0^{\mathbb{R}}(C) \rangle_\Lambda \right| \le \left| \langle W_t^{\mathbb{C}}(C) \rangle_\Lambda - \langle W_0^{\mathbb{C}}(C) \rangle_\Lambda \right| \le K(\beta, d, N) \, n \, \frac{t}{a^2},}$$
where:
1. Under **Lüscher's (2010) standard dimensionless gradient-flow convention** $a^2 \partial_t V_t(\ell) = -g_0^2 \left(\partial_\ell S_W(V_t)\right) V_t(\ell)$ with anti-Hermitian generator normalization $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$, the bare coupling $\beta = \frac{2N}{g_0^2}$ and the factor of $2$ **cancel identically**, yielding the exact $\beta$- and $N$-independent constant:
   $$K(d, N) = 2(d - 1) \qquad (\text{so } K = 6 \text{ in } d = 4 \text{ for all } N \ge 2).$$
2. Under the **unscaled action-gradient flow convention** $a^2 \partial_\tau V_\tau(\ell) = -\left(\partial_\ell S_W(V_\tau)\right) V_\tau(\ell)$ (with $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$), the factor $\beta$ remains linearly in the constant:
   $$K(\beta, d, N) = \frac{\beta (d - 1)}{N}.$$

---

### 2.2 Complete First-Principles Derivation Without Any Omitted Normalization Factor (`YM-GOV-015` Audit)

#### Step 1: Exact Lie-Algebra Derivative and Lüscher Generator Normalization ($\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$)
For a single link $\ell \in E(\Lambda)$, let $S_\ell(V) = \sum_{p \ni \ell} W_p$ be the sum of the $2(d-1)$ oriented staple products ($2(4-1) = 6$ staples in $d=4$) such that $V_p = V_\ell W_p^\dagger$. The $\ell$-dependent part of $S_W(V) = \frac{\beta}{N}\sum_p \operatorname{Re}\operatorname{Tr}(I_N - V_p)$ is:
$$S_W^{(\ell)}(V) = -\frac{\beta}{N} \operatorname{Re}\operatorname{Tr}\!\left( V_\ell S_\ell(V)^\dagger \right) = -\frac{\beta}{2N} \operatorname{Tr}\!\left( V_\ell S_\ell^\dagger + S_\ell V_\ell^\dagger \right).$$
Let $\{T^a\}_{a=1}^{N^2-1} \subset \mathfrak{su}(N)$ be Lüscher's (2010, *JHEP* 1008:071, Eq. 1.2) basis of anti-Hermitian traceless generators satisfying:
$$(T^a)^\dagger = -T^a, \qquad \operatorname{Tr}(T^a) = 0, \qquad \operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}.$$
Then the directional derivative along $T^a$ ($V_\ell(\epsilon) = e^{\epsilon T^a} V_\ell$) is:
$$\partial_\ell^a S_W(V) := \left.\frac{d}{d\epsilon}\right|_{\epsilon=0} S_W(e^{\epsilon T^a} V_\ell) = -\frac{\beta}{2N} \operatorname{Tr}\!\left( T^a \left( V_\ell S_\ell^\dagger - S_\ell V_\ell^\dagger \right) \right) = -\frac{\beta}{N} \operatorname{Tr}\!\left( T^a \, \mathcal{P}_{\mathfrak{su}(N)}\!\left(V_\ell S_\ell^\dagger\right) \right),$$
where $\mathcal{P}_{\mathfrak{su}(N)}(M) := \frac{1}{2}(M - M^\dagger) - \frac{1}{2N}\operatorname{Tr}(M - M^\dagger)I_N \in \mathfrak{su}(N)$.
Because every $Y \in \mathfrak{su}(N)$ expands as $Y = \sum_{b=1}^{N^2-1} y^b T^b$ with $\operatorname{Tr}(T^a Y) = -\frac{1}{2} y^a$, contracting with $T^a$ yields the exact completeness identity:
$$\sum_{a=1}^{N^2-1} T^a \operatorname{Tr}(T^a Y) = -\frac{1}{2} Y \qquad \forall Y \in \mathfrak{su}(N).$$
Applying this identity to Lüscher's Lie-algebra differential operator $\partial_\ell S_W(V) := \sum_{a=1}^{N^2-1} T^a \partial_\ell^a S_W(V)$ gives:
$$\partial_\ell S_W(V) = -\frac{\beta}{N} \sum_{a=1}^{N^2-1} T^a \operatorname{Tr}\!\left( T^a \, \mathcal{P}_{\mathfrak{su}(N)}\!\left(V_\ell S_\ell^\dagger\right) \right) = +\frac{\beta}{2N} \, \mathcal{P}_{\mathfrak{su}(N)}\!\left( V_\ell S_\ell(V)^\dagger \right) = \frac{1}{g_0^2} \, \mathcal{P}_{\mathfrak{su}(N)}\!\left( V_\ell S_\ell(V)^\dagger \right),$$
where the factor $\frac{1}{2}$ from $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$ cancels the factor $2$ in $\beta = \frac{2N}{g_0^2}$!
Consequently, Lüscher's (2010) gradient flow equation $a^2 \partial_t V_t(\ell) = -g_0^2 \left(\partial_\ell S_W(V_t)\right) V_t(\ell)$ simplifies with **exact unit prefactor $1$** to:
$$\boxed{a^2 \partial_t V_t(\ell) = -\mathcal{P}_{\mathfrak{su}(N)}\!\left( V_t(\ell) S_\ell(V_t)^\dagger \right) V_t(\ell), \qquad Z_t(\ell) := (\partial_t V_t(\ell)) V_t(\ell)^{-1} = -\frac{1}{a^2} \mathcal{P}_{\mathfrak{su}(N)}\!\left( V_t(\ell) S_\ell(V_t)^\dagger \right).}$$
*(Remark: If instead one defines the flow using the Hilbert–Schmidt Riemannian gradient $\nabla_\ell^{\mathrm{HS}} S_W = 2 \partial_\ell S_W$ corresponding to $\operatorname{Tr}(\tilde{T}^a \tilde{T}^b) = -\delta^{ab}$, then $K_{\mathrm{HS}} = 4(d-1) = 12$ in $d=4$.)*

#### Step 2: Why the Hilbert–Schmidt Norm Gives $K = 2(d-1) = 6$ Exactly Without Spectral-Projection Inflation
Equip $\mathbb{C}^{N\times N}$ with the real Hilbert–Schmidt (Frobenius) inner product $\langle A, B \rangle_{\mathrm{HS},\mathbb{R}} := \operatorname{Re}\operatorname{Tr}(A^\dagger B)$ and norm $\|A\|_{\mathrm{HS}} := \sqrt{\operatorname{Tr}(A^\dagger A)}$.
- **Crucial Norm Distinction:** In the spectral/operator norm $\|\cdot\|_{\mathrm{op}}$, the trace-subtraction in $\mathcal{P}_{\mathfrak{su}(N)}(M) = \frac{1}{2}(M - M^\dagger) - \frac{1}{2N}\operatorname{Tr}(M - M^\dagger)I_N$ is *not* an orthogonal projection for $N \ge 3$ (its sharp spectral operator norm bound is $\|\mathcal{P}_{\mathfrak{su}(N)}(M)\|_{\mathrm{op}} \le \left(2 - \frac{2}{N}\right)\|M\|_{\mathrm{op}}$). However, in the **Hilbert–Schmidt inner product** $\langle \cdot, \cdot \rangle_{\mathrm{HS},\mathbb{R}}$, $\mathfrak{su}(N)$ is an $\mathbb{R}$-linear subspace of $\mathbb{C}^{N\times N}$ and $\mathcal{P}_{\mathfrak{su}(N)}$ is the **exact $\mathbb{R}$-orthogonal projection** onto $\mathfrak{su}(N)$:
  $$\langle X, \, M - \mathcal{P}_{\mathfrak{su}(N)}(M) \rangle_{\mathrm{HS},\mathbb{R}} = 0 \quad \forall X \in \mathfrak{su}(N) \implies \left\| \mathcal{P}_{\mathfrak{su}(N)}(M) \right\|_{\mathrm{HS}} \le \|M\|_{\mathrm{HS}} \quad (\text{exact projection norm } 1 \text{ for all } N \ge 2).$$
- Since $V_s(\ell_m) \in SU(N)$ and each of the $2(d-1)$ staples $W_p \in SU(N)$ is unitary, $\|V_s(\ell_m) W_p^\dagger\|_{\mathrm{HS}} = \sqrt{\operatorname{Tr}(I_N)} = \sqrt{N}$. By the triangle inequality for $\|\cdot\|_{\mathrm{HS}}$:
  $$\left\| \mathcal{P}_{\mathfrak{su}(N)}\!\left( V_s(\ell_m) S_{\ell_m}(V_s)^\dagger \right) \right\|_{\mathrm{HS}} \le \left\| V_s(\ell_m) S_{\ell_m}(V_s)^\dagger \right\|_{\mathrm{HS}} \le \sum_{p \ni \ell_m} \left\| V_s(\ell_m) W_p^\dagger \right\|_{\mathrm{HS}} = 2(d - 1)\sqrt{N}.$$

#### Step 3: Leibniz Rule and Cauchy–Schwarz Along the $n$-Link Holonomy
Differentiating $W_s^{\mathbb{C}}(C)[U] = \frac{1}{N}\operatorname{Tr}(H_s(C))$ along $s \in [0, t]$ using the Leibniz rule and cyclicity of the trace:
$$\frac{d}{ds} W_s^{\mathbb{C}}(C)[U] = \frac{1}{N} \sum_{m=1}^{n} \operatorname{Tr}\!\left( Z_s(\ell_m) \, \tilde{H}_s^{(m)}(C) \right),$$
where $\tilde{H}_s^{(m)}(C) := V_s(\ell_m) \cdots V_s(\ell_n) V_s(\ell_1) \cdots V_s(\ell_{m-1}) \in SU(N)$ is unitary and therefore satisfies $\|\tilde{H}_s^{(m)}(C)\|_{\mathrm{HS}} = \sqrt{N}$.
By the Cauchy–Schwarz inequality $|\operatorname{Tr}(A^\dagger B)| \le \|A\|_{\mathrm{HS}} \|B\|_{\mathrm{HS}}$ for the Hilbert–Schmidt inner product:
$$\left| \frac{1}{N} \operatorname{Tr}\!\left( Z_s(\ell_m) \, \tilde{H}_s^{(m)}(C) \right) \right| \le \frac{1}{N} \|Z_s(\ell_m)\|_{\mathrm{HS}} \, \|\tilde{H}_s^{(m)}(C)\|_{\mathrm{HS}} \le \frac{1}{N a^2} \left( 2(d - 1)\sqrt{N} \right) \sqrt{N} = \frac{2(d - 1)}{a^2}.$$
Summing over $m = 1, \dots, n$ and integrating over $s \in [0, t]$ yields the exact pointwise and expectation bounds:
$$\left| W_t^{\mathbb{R}}(C)[U] - W_0^{\mathbb{R}}(C)[U] \right| \le \left| W_t^{\mathbb{C}}(C)[U] - W_0^{\mathbb{C}}(C)[U] \right| \le \int_0^t \left| \frac{d}{ds} W_s^{\mathbb{C}}(C)[U] \right| ds \le 2(d - 1) \, n \, \frac{t}{a^2}. \quad \blacksquare$$

---

## 3. Verified Single-Step Observable-Transfer Map (`YM-011-OBS-MAP`) & Next Task (`YM-011-PLAQUETTE-EXP`)

> **Governance Gate (`YM-GOV-015` / `YM-011-OBS-MAP`):** The original `YM-011-L1` continuum/exponential proposal remains **`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`**, and the rejected exponential scale-transfer estimate $a \exp(-c/a^2)$ is permanently retired. The single-step finite-lattice observable-transfer map (`YM-011-OBS-MAP`) has been constructed, proved, and computationally verified in [`literature/YM-011-OBS-MAP-CONSTRUCTION.md`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/literature/YM-011-OBS-MAP-CONSTRUCTION.md) and [`src/ymmg/observable_transfer.py`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/src/ymmg/observable_transfer.py).

### 3.1 Summary of Verified Objects and Theorems in `YM-011-OBS-MAP`
1. **Fine & Coarse Probability Spaces ($\Lambda_0$ at spacing $a$, $\Lambda_1$ at spacing $2a$):**
   $(\Omega_0, \mathcal{F}_0, \mu_0)$ with $\Omega_0 = SU(N)^{E_+(\Lambda_0)}$ and Wilson Gibbs measure $d\mu_0 = Z_{\Lambda_0}(\beta)^{-1} e^{-S_W(U)} d\mu_{\mathrm{Haar},0}(U)$; $(\Omega_1, \mathcal{F}_1)$ with $\Omega_1 = SU(N)^{E_+(\Lambda_1)}$ and pushforward measure $\mu_1^{(\alpha,\kappa)} = (K^{(\alpha,\kappa)}_{0\to 1})_\# \mu_0$ (whose effective action $S_{\mathrm{eff}}^{(1)}(V)$ is explicitly proved not to retain the single-plaquette Wilson form).
2. **Globally Smooth, Everywhere $SU(N)$-Valued Midpoint-Exponential Blocking Map $\mathcal{B}_\alpha^{\mathrm{mid}} : \Omega_0 \to \Omega_1$:**
   $$\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) := U(\ell_{e,1}) \, \exp\!\left( \alpha \, X_{\mathrm{mid}}(e)[U] \right) \, U(\ell_{e,2}) \in SU(N), \qquad X_{\mathrm{mid}}(e)[U] := \mathcal{P}_{\mathfrak{su}(N)}\!\left( \frac{1}{2(d-1)} \sum_{\nu \ne \mu, \, \sigma \in \{+,-\}} U(\ell_{e,1})^\dagger H_0(\gamma_{\nu,\sigma}(e))[U] U(\ell_{e,2})^\dagger \right),$$
   which eliminates the determinant singular locus (`NEG-YM-011-OBS-1`) and satisfies exact orientation covariance $\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e^{-1}) = (\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e))^{-1}$ and exact gauge equivariance $\mathcal{B}_\alpha^{\mathrm{mid}}(g_0 \cdot U) = \pi_{\mathcal{G}}(g_0) \cdot \mathcal{B}_\alpha^{\mathrm{mid}}(U)$.
3. **Verified Finite-Lattice Comparison Theorems:**
   - **`YM-011-OBS-T1` (Unconditional Pointwise & $L^1(\mu_0)$ Bound):** $\left| ((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}(C_1))[U] - W_{\Lambda_0,t}(\iota_{\mathrm{loop}}(C_1))[U] \right| \le |C_1|_{\Lambda_1} \left(|\alpha| + 4(d-1)\frac{t}{a^2}\right)$.
   - **`YM-011-OBS-T2` (Exact Quadratic Plaquette Defect Identity & Small-Field Tangent Cancellation):** Under $\alpha(t) = 2(d-1)\frac{t}{a^2}$, $2(d-1) X_{\mathrm{mid}}(e)[U] - Y_{\mathrm{flow}}(e)[U] \equiv \sum_{\nu \ne \mu, \sigma \in \{+,-\}} \mathcal{P}_{\mathfrak{su}(N)}((P_{1,\nu,\sigma}^\dagger - I_N)(P_{2,\nu,\sigma}^\dagger - I_N))$, giving $|\Delta_{\mathrm{tan}}(C_1)[U]| \le 2(d-1)|C_1|_{\Lambda_1} \epsilon_{\mathrm{plaq}}^2$ on $\Omega_0(\epsilon_{\mathrm{plaq}})$.
   - **`YM-011-OBS-T3` (Markov Kernel Schur Factorization):** $((K^{(\alpha,\kappa)}_{0\to 1})^* W_{\Lambda_1}(C_1))[U] = c_F(\kappa)^{|C_1|_{\Lambda_1}} ((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}(C_1))[U]$ for every simple coarse loop $C_1$.

### 3.2 Pullback Map $\mathcal{B}_{0\to 1}^*$ and Next Smallest Authorized Research Task (`YM-011-PLAQUETTE-EXP`)
The pullback observable map $\mathcal{B}_{0\to 1}^* : \mathcal{A}_{\mathrm{loop}}(\Lambda_1) \to L^\infty(\Omega_0, \mu_0)$ satisfies the exact measure-theoretic identity $\langle W_{\Lambda_1}(C_1) \rangle_{\mu_1} \equiv \langle \mathcal{B}_{0\to 1}^* W_{\Lambda_1}(C_1) \rangle_{\mu_0}$. Before any multi-step RG iteration or effective-action comparison (`YM-011-ACT-DEFECT`), the next smallest bounded research task is **`YM-011-PLAQUETTE-EXP` (`Finite-Lattice Gibbs Expectation Bound for the Quadratic Plaquette Tangent Defect`)**, which bounds $\langle |\Delta_{\mathrm{tan}}(C_1)| \rangle_{\mu_0}$ in terms of the finite-lattice plaquette expectation $e_{\mathrm{plaq}}(\beta, \Lambda_0) = \langle 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \rangle_{\mu_0}$.

### Lemma YM-011-L1 (UV Scale-Transfer and Observables Mollification Lemma)

> **Governance Gate (`YM-GOV-015` / `YM-011-OBS-MAP`):** Lemma `YM-011-L1` remains in status **`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`**. This formulation assumes **no mass gap**, no infinite-volume thermodynamic limit, and no specific infrared behavior.

**Statement:**
Any future multi-step quantitative estimate on $\mathcal{D}_{0\to 1}(C_1; t)$ must be derived directly from the verified finite-lattice observable-transfer map (`YM-011-OBS-MAP`), the quadratic plaquette expectation (`YM-011-PLAQUETTE-EXP`), and the fixed-lattice differential identity of `YM-011-PRE-R1` without stipulating exponential decay in $1/a^2$.


---

## 4. Governance & Acceptance Criteria (`YM-GOV-014` Failure-Driven Workflow)

Under **`YM-GOV-014`**, routine bounded scientific tasks and precursor lemmas follow the failure-driven scientific review state machine:
$$\texttt{CANDIDATE} \longrightarrow \texttt{INDEPENDENT\_SCIENTIFIC\_REVIEW} \longrightarrow \{\texttt{SCIENTIFICALLY\_ACCEPTED}, \texttt{REPAIR\_REQUIRED}, \texttt{REVIEW\_HOLD}\}$$
1. **Complete, Step-by-Step Proof:** All constants $K(\beta, d, N)$, operator norms, trace ranges ($[-1, 1]$), and conventions must be explicitly derived without hand-waving.
2. **Deterministic Verification:** Verified via `src/ymmg/precursor_flow.py` and unit test suite `tests/test_ym_gov_014_autonomous_repair.py`.
3. **Candidate-Bound Independent Scientific Review:** Audited by an independent reviewer subagent with `candidate_sha == reviewed_sha` (or declared non-scientific metadata only).
4. **Activation Gate for `YM-011`:** `YM-011` cannot enter active proof execution while `YM-011` is in status `PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`.

---

## 5. Relationship to the Clay Target

Proving the fixed-lattice precursor `YM-011-PRE` (or any future `YM-011-L1` lemma) **does not solve the Clay Millennium Problem** (`GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`). It establishes the elementary fixed-lattice differential baseline required before any multiscale UV observable transfer can be rigorously analyzed.

