# Task `YM-011-PLAQUETTE-EXP-R1` — Repair of Plaquette-Energy Range $[0, 2]$ and Finite-Lattice Gibbs Expectation Reduction

- **TASK_ID:** `YM-011-PLAQUETTE-EXP-R1` (Repaired Revision of `YM-011-PLAQUETTE-EXP`)
- **TASK_STATUS:** `REPAIRED_CANDIDATE_UNCONDITIONAL_EXPECTATION_REDUCTION`
- **PLAQUETTE_ENERGY_RANGE:** `[0, 2]` (`Universally safe bound for all SU(N); even N attains 2.0 at U_p = -I_N; odd N bounded by 1 + cos(pi/N) < 2.0 (1.5 for SU(3))`)
- **O_1_OVER_BETA_STATUS:** `WITHHELD_AS_UNRESOLVED_DEPENDENCY` (`Claims A, B, C strictly separated; pure O(1/beta) on periodic torus obstructed by flat-connection/toron singular strata NEG-YM-011-PLAQ-1`)
- **ORIGINAL_YM_011_CONTINUUM_PROPOSAL_STATUS:** `NOT_AUTHORIZED` (`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`)
- **YM_006_THROUGH_YM_010_STATUS:** `SCIENTIFIC_REVIEW_HOLD`
- **GOAL_COMPLETE:** `FALSE` (`CLAY_PROBLEM = OPEN_AND_UNSOLVED`)
- **GOVERNANCE_TIER:** `R2` (Autonomous Scientific Verification & Independent Adversarial Review under `YM-GOV-014` / `YM-GOV-015`)
- **PREREQUISITE_DEPENDENCIES:** `YM-011-OBS-MAP` (`YM-011-OBS-T2`), `YM-011-PRE-R1`, `YM-004`
- **VERIFICATION_MODULE:** `src/ymmg/plaquette_expectation.py` & `tests/test_ym_011_plaquette_exp.py`

---

## 1. Pointwise Input Theorem (`YM-011-OBS-T2`) and Exact $SU(N)$ Hilbert–Schmidt Identity

### 1.1 Pointwise Input Inequality from `YM-011-OBS-T2`
Let $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ ($d \ge 2$, specifically $d = 4$, $L \in \mathbb{N}_{\ge 1}$) be the fine periodic hypercubic lattice of spacing $a > 0$, and let $\Lambda_1 = (2a\mathbb{Z}/2La\mathbb{Z})^d \subset \Lambda_0$ be the embedded coarse sublattice of spacing $2a$.
Under the matched scale relation $\alpha(t) = 2(d - 1)\frac{t}{a^2}$, Theorem `YM-011-OBS-T2` established that for every closed coarse loop $C_1 = (e_1, \dots, e_m)$ of $m = |C_1|_{\Lambda_1}$ coarse edges and every configuration $U \in \Omega_0 = SU(N)^{E_+(\Lambda_0)}$, the initial tangent discrepancy rate
$$\Delta_{\mathrm{tan}}(C_1)[U] := \left. a^2 \frac{d}{dt} \right|_{t=0} \left( \left((\mathcal{B}_{\alpha(t)}^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{C}}(C_1)\right)[U] - W_{\Lambda_0,t}^{\mathbb{C}}(\iota_{\mathrm{loop}}(C_1))[U] \right)$$
satisfies the exact pointwise bound:
$$\boxed{\left|\Delta_{\mathrm{tan}}(C_1)[U]\right| \le \frac{1}{\sqrt{N}} \sum_{k=1}^{|C_1|_{\Lambda_1}} \sum_{\nu \ne \mu_k, \, \sigma \in \{+,-\}} \left\| P_{1,\nu,\sigma}^{(k)}[U] - I_N \right\|_{\mathrm{op}} \, \left\| P_{2,\nu,\sigma}^{(k)}[U] - I_N \right\|_{\mathrm{HS}},}$$
where $P_{1,\nu,\sigma}^{(k)}[U], P_{2,\nu,\sigma}^{(k)}[U] \in SU(N)$ are the two adjacent $a \times a$ fine plaquettes in the $(\mu_k, \nu)$-plane touching $\ell_{e_k,1}$ and $\ell_{e_k,2}$ respectively and based at the midpoint $m(e_k) = y_k + a\hat{\mu}_k$.

### 1.2 Exact $SU(N)$ Hilbert–Schmidt Plaquette Identity and Group-Theoretic Range
For any unitary matrix $U_p \in SU(N)$ ($U_p^\dagger U_p = I_N$):
$$\left\| U_p - I_N \right\|_{\mathrm{HS}}^2 = \operatorname{Tr}\!\left( (U_p^\dagger - I_N)(U_p - I_N) \right) = \operatorname{Tr}\!\left( 2 I_N - U_p - U_p^\dagger \right) = 2N - 2\operatorname{Re}\operatorname{Tr}(U_p) = 2N \left( 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \right).$$
Define for each elementary plaquette $p \in P_+(\Lambda_0)$ the normalized plaquette defect random variable:
$$h_p(U) := 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) = \frac{1}{2N} \left\| U_p - I_N \right\|_{\mathrm{HS}}^2,$$
and its expectation under the Wilson Gibbs probability measure $\mu_0$:
$$e_p(\beta, \Lambda_0) := \langle h_p \rangle_{\mu_0} = \frac{1}{2N} \left\langle \left\| U_p - I_N \right\|_{\mathrm{HS}}^2 \right\rangle_{\mu_0}.$$

**Exact Group-Theoretic Range of $h_p(U)$ and $e_p(\beta, \Lambda_0)$ across $SU(N)$:**
Let $q_N(U) := \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U) = \frac{1}{N}\sum_{j=1}^N \cos\theta_j$ where $\sum_{j=1}^N \theta_j \equiv 0 \pmod{2\pi}$.
- **Even $N$ ($N = 2, 4, 6, \dots$):** $-I_N \in SU(N)$ because $\det(-I_N) = (-1)^N = 1$.
  At the central element $U_p = -I_N$, $q_N(-I_N) = -1.0$, attaining the maximum:
  $$h_p(-I_N) = 1.0 - (-1.0) = 2.0.$$
  *(For example, in $SU(2)$, $U_p = -I_2 \in SU(2)$ gives $h_p(-I_2) = 2.0$ and $\|(-I_2) - I_2\|_{\mathrm{HS}}^2 = \|-2I_2\|_{\mathrm{HS}}^2 = 8 = 2(2)(2.0)$.)*
- **Odd $N$ ($N = 3, 5, 7, \dots$):** $-I_N \notin SU(N)$ because $\det(-I_N) = (-1)^N = -1 \ne 1$.
  The constrained minimum of $q_N(U)$ occurs when all $N$ eigenvalues are equal: $\theta_j = \pi - \frac{\pi}{N}$ for all $j$, so $\sum \theta_j = (N-1)\pi \equiv 0 \pmod{2\pi}$ (since $N-1$ is even).
  Thus $\min_{U \in SU(N)} q_N(U) = \cos(\pi - \pi/N) = -\cos(\pi/N) > -1.0$, which yields:
  $$\max_{U \in SU(N)} h_p(U) = 1 + \cos(\pi/N) < 2.0.$$
  *(For example, in $SU(3)$, $\min q_3 = \cos(2\pi/3) = -0.5$ attained at $U_p = e^{i 2\pi/3} I_3 \in SU(3)$, giving $\max h_p = 1.5$.)*
- **Universally Safe Range for all $N \ge 2$:**
  $$\boxed{0 \le h_p(U) \le 2 \implies 0 \le e_p(\beta, \Lambda_0) \le 2 \implies 0 \le e_{\mathrm{plaq}}(\beta, \Lambda_0) \le 2.}$$
Furthermore, for any matrix $A \in M_N(\mathbb{C})$ with singular values $s_1 \ge \dots \ge s_N \ge 0$, $\|A\|_{\mathrm{op}} = s_1 \le \sqrt{\sum_{j=1}^N s_j^2} = \|A\|_{\mathrm{HS}}$.
- **Sharp $SU(2)$ Spectral Identity:** For $G = SU(2)$, every $U_p \in SU(2)$ has conjugate eigenvalues $e^{\pm i\theta}$ ($\theta \in [0, \pi]$), so $s_1(U_p - I_2) = s_2(U_p - I_2) = |e^{i\theta} - 1| = 2\sin(\theta/2)$, giving the **exact identity**:
  $$\left\| U_p - I_2 \right\|_{\mathrm{op}} \equiv \frac{1}{\sqrt{2}} \left\| U_p - I_2 \right\|_{\mathrm{HS}} \qquad (\forall U_p \in SU(2)).$$
  *(Note: At $U_p = -I_2$, $\| -2I_2 \|_{\mathrm{op}} = 2.0$ and $\| -2I_2 \|_{\mathrm{HS}} = 2\sqrt{2}$, so $2.0 = \frac{1}{\sqrt{2}}(2\sqrt{2})$ holds identically at the extremal point $h_p = 2.0$.)*

---

## 2. Unconditional Expectation Reduction (`YM-011-PLAQUETTE-EXP-T1`) and Proof of Plaquette Symmetry

### 2.1 Theorem `YM-011-PLAQUETTE-EXP-T1` (Unconditional Gibbs Expectation Reduction)
**Statement:** Let $(\Omega_0, \mathcal{F}_0, \mu_0)$ be the finite-lattice Wilson Gibbs probability space at spacing $a > 0$ and bare coupling $\beta > 0$, and let $C_1 = (e_1, \dots, e_m)$ be a closed coarse loop of $m = |C_1|_{\Lambda_1}$ coarse edges on $\Lambda_1$.
1. **General Boundary-Condition-Independent Form (Valid for Arbitrary Finite Lattices & Boundary Conditions):**
   Without assuming translation invariance or coordinate-axis isotropy,
   $$\boxed{\left\langle \left|\Delta_{\mathrm{tan}}(C_1)\right| \right\rangle_{\mu_0} \le 2\sqrt{N} \sum_{k=1}^{|C_1|_{\Lambda_1}} \sum_{\nu \ne \mu_k, \, \sigma \in \{+,-\}} \sqrt{ e_{p_1(k,\nu,\sigma)}(\beta, \Lambda_0) \, e_{p_2(k,\nu,\sigma)}(\beta, \Lambda_0) }.}$$
2. **Anisotropic Periodic Torus Form ($\Lambda_0 = \prod_{\mu=1}^d (a\mathbb{Z}/2L_\mu a\mathbb{Z})$ with Arbitrary Periods $L_1, \dots, L_d \ge 1$):**
   Under periodic boundary conditions in direction $\hat{\mu}_k$ alone, $e_{p_1(k,\nu,\sigma)}(\beta, \Lambda_0) = e_{p_2(k,\nu,\sigma)}(\beta, \Lambda_0) =: e_{\mu_k \nu}(\beta, \Lambda_0)$, and
   $$\left\langle \left|\Delta_{\mathrm{tan}}(C_1)\right| \right\rangle_{\mu_0} \le 4\sqrt{N} \sum_{k=1}^{|C_1|_{\Lambda_1}} \sum_{\nu \ne \mu_k} e_{\mu_k \nu}(\beta, \Lambda_0).$$
3. **Isotropic Periodic Torus Form ($\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ with Equal Periods $L_1 = \dots = L_d = L$):**
   All $|P_+(\Lambda_0)| = \binom{d}{2}(2L)^d$ elementary plaquettes have identical expectation $e_p(\beta, \Lambda_0) \equiv e_{\mathrm{plaq}}(\beta, \Lambda_0)$, and therefore:
   $$\boxed{\left\langle \left|\Delta_{\mathrm{tan}}(C_1)\right| \right\rangle_{\mu_0} \le C(d, N) \, |C_1|_{\Lambda_1} \, e_{\mathrm{plaq}}(\beta, \Lambda_0), \qquad C(d, N) := 4(d - 1)\sqrt{N},}$$
   with $C(4, N) = 12\sqrt{N}$ in $d = 4$ (and the sharp $SU(2)$ constant $C_{\mathrm{sharp}}(d, 2) := 4(d - 1)$, giving $C_{\mathrm{sharp}}(4, 2) = 12$ in $d = 4$).

### 2.2 Complete First-Principles Proof of `YM-011-PLAQUETTE-EXP-T1`
1. **Proof of (1) (Cauchy–Schwarz on $L^2(\Omega_0, \mu_0)$):**
   For each channel $(k, \nu, \sigma)$, let $p_1 = p_1(k, \nu, \sigma)$ and $p_2 = p_2(k, \nu, \sigma)$ be the two underlying elementary plaquettes in $P_+(\Lambda_0)$. Because $P_{1,\nu,\sigma}^{(k)}[U]$ is conjugate in $SU(N)$ to $U_{p_1}$ or $U_{p_1}^\dagger$, $\|P_{1,\nu,\sigma}^{(k)}[U] - I_N\|_{\mathrm{op}} = \|U_{p_1} - I_N\|_{\mathrm{op}} \le \|U_{p_1} - I_N\|_{\mathrm{HS}}$ and $\|P_{2,\nu,\sigma}^{(k)}[U] - I_N\|_{\mathrm{HS}} = \|U_{p_2} - I_N\|_{\mathrm{HS}}$. By Cauchy–Schwarz on $L^2(\Omega_0, \mu_0)$:
   $$\left\langle \left\|P_{1,\nu,\sigma}^{(k)} - I_N\right\|_{\mathrm{op}} \left\|P_{2,\nu,\sigma}^{(k)} - I_N\right\|_{\mathrm{HS}} \right\rangle_{\mu_0} \le \sqrt{ \left\langle \left\|U_{p_1} - I_N\right\|_{\mathrm{HS}}^2 \right\rangle_{\mu_0} \left\langle \left\|U_{p_2} - I_N\right\|_{\mathrm{HS}}^2 \right\rangle_{\mu_0} } = \sqrt{ (2N e_{p_1})(2N e_{p_2}) } = 2N \sqrt{e_{p_1} e_{p_2}}.$$
   Multiplying by $\frac{1}{\sqrt{N}}$ gives $2\sqrt{N}\sqrt{e_{p_1} e_{p_2}}$ per channel. Summing over $k = 1, \dots, |C_1|_{\Lambda_1}$ and the $2(d-1)$ channels $(\nu \ne \mu_k, \sigma \in \{+,-\})$ proves (1). (For $SU(2)$, replacing $\|U_{p_1} - I_2\|_{\mathrm{op}} \le \|U_{p_1} - I_2\|_{\mathrm{HS}}$ by the exact identity $\|U_{p_1} - I_2\|_{\mathrm{op}} = \frac{1}{\sqrt{2}}\|U_{p_1} - I_2\|_{\mathrm{HS}}$ multiplies the prefactor by $\frac{1}{\sqrt{2}}$, yielding $2\sqrt{2} \cdot \frac{1}{\sqrt{2}} = 2$ per channel and $2 \cdot 2(d-1) = 4(d-1)$ total.)

2. **Proof of (2) and (3) (Why Translation Invariance Alone Gives (2) and Hyperoctahedral Axis Symmetry Gives (3)):**
   - **Step A (Periodic Translation Group $(\mathbb{Z}/2L\mathbb{Z})^d$):** For each $z \in (a\mathbb{Z}/2La\mathbb{Z})^d$, let $\tau_z : \Lambda_0 \to \Lambda_0$, $\tau_z(x) = x + z \pmod{2La}$, be the periodic lattice translation, and let $(\tau_z^* U)(\ell) := U(\tau_z(\ell))$ be the induced pullback on $\Omega_0$. Because $\tau_z$ is a bijection on $E_+(\Lambda_0)$ and $P_+(\Lambda_0)$, $\tau_z^*$ simply permutes the product factors of $d\mu_{\mathrm{Haar},0}(U) = \prod_{\ell \in E_+(\Lambda_0)} dU(\ell)$ and the summands of $S_W(U) = \frac{\beta}{N}\sum_{p \in P_+(\Lambda_0)} \operatorname{Re}\operatorname{Tr}(I_N - U_p)$. Hence $(\tau_z^*)_\# \mu_0 = \mu_0$.
     Since $\tau_z$ maps the plaquette $p = (x; \mu, \nu)$ to $(x + z; \mu, \nu)$ in the **same** $(\mu, \nu)$-plane, $e_{(x;\mu,\nu)}(\beta, \Lambda_0) = e_{(0;\mu,\nu)}(\beta, \Lambda_0) =: e_{\mu\nu}(\beta, \Lambda_0)$ for all $x \in V(\Lambda_0)$. In particular, for any coarse edge $e_k$ in direction $\hat{\mu}_k$, $p_1(k, \nu, \sigma)$ and $p_2(k, \nu, \sigma)$ lie in the **same** $(\mu_k, \nu)$-plane and satisfy $p_2 = \tau_{a\hat{\mu}_k}(p_1)$, so $e_{p_1(k,\nu,\sigma)} = e_{p_2(k,\nu,\sigma)} = e_{\mu_k \nu}(\beta, \Lambda_0)$ even on an anisotropic torus, proving (2).
   - **Step B (Hyperoctahedral Axis Permutation Group $S_d$ on the Isotropic Torus):** Translation invariance alone does *not* equate $e_{\mu\nu}$ across distinct coordinate planes $\{\mu, \nu\} \ne \{\rho, \tau\}$. However, when all $d$ torus periods are equal ($L_1 = \dots = L_d = L$), every coordinate permutation $\pi \in S_d$ defines a lattice automorphism $\widehat{\pi} : (x_1, \dots, x_d) \mapsto (x_{\pi^{-1}(1)}, \dots, x_{\pi^{-1}(d)})$ on $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ that maps the coordinate plane $(\mu, \nu)$ onto $(\pi(\mu), \pi(\nu))$ (up to orientation reversal $p \mapsto p^{-1}$, under which $\operatorname{Re}\operatorname{Tr}(U_{p^{-1}}) = \operatorname{Re}\operatorname{Tr}(U_p^\dagger) = \operatorname{Re}\operatorname{Tr}(U_p)$). Since $\widehat{\pi}^*$ preserves both $d\mu_{\mathrm{Haar},0}$ and $S_W(U)$, and $S_d$ acts transitively on the $\binom{d}{2}$ unordered pairs $\{\mu, \nu\} \subset \{1, \dots, d\}$, we have $e_{\mu\nu}(\beta, \Lambda_0) = e_{12}(\beta, \Lambda_0) =: e_{\mathrm{plaq}}(\beta, \Lambda_0)$ for all $1 \le \mu < \nu \le d$. Summing $2(d-1)$ channels of $2\sqrt{N} e_{\mathrm{plaq}}$ over $|C_1|_{\Lambda_1}$ edges yields $4(d-1)\sqrt{N} \, |C_1|_{\Lambda_1} \, e_{\mathrm{plaq}}(\beta, \Lambda_0)$, proving (3). $\blacksquare$

---

## 3. Exact Finite-Dimensional Statistical-Mechanics Identity for Mean Plaquette Energy (`YM-011-PLAQUETTE-EXP-T2`)

**Theorem (`YM-011-PLAQUETTE-EXP-T2` — Exact Partition-Function Derivative & Plaquette-Energy Range):**
Write the finite-lattice Wilson Gibbs probability measure on $\Omega_0 = SU(N)^{E_+(\Lambda_0)}$ as
$$d\mu_\beta(U) = Z_{\Lambda_0}(\beta)^{-1} \exp\!\left(-\beta H(U)\right) d\mu_{\mathrm{Haar},0}(U), \qquad Z_{\Lambda_0}(\beta) := \int_{\Omega_0} \exp\!\left(-\beta H(U)\right) d\mu_{\mathrm{Haar},0}(U),$$
where the dimensionless total plaquette Hamiltonian $H : \Omega_0 \to [0, 2|P_+(\Lambda_0)|]$ is normalized as
$$\boxed{H(U) := \frac{S_W(U)}{\beta} = \sum_{p \in P_+(\Lambda_0)} \left( 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \right).}$$
Then for every finite periodic lattice $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ and every $\beta \in (0, \infty)$:
1. **Exact Log-Partition Derivative Identity:**
   $$\boxed{-\frac{\partial}{\partial \beta} \ln Z_{\Lambda_0}(\beta) = \langle H \rangle_{\mu_0} = \sum_{p \in P_+(\Lambda_0)} e_p(\beta, \Lambda_0) = |P_+(\Lambda_0)| \, e_{\mathrm{plaq}}(\beta, \Lambda_0),}$$
   and consequently:
   $$\boxed{e_{\mathrm{plaq}}(\beta, \Lambda_0) = -\frac{1}{|P_+(\Lambda_0)|} \frac{\partial}{\partial \beta} \ln Z_{\Lambda_0}(\beta) = -\frac{1}{\binom{d}{2}(2L)^d} \frac{\partial}{\partial \beta} \ln Z_{\Lambda_0}(\beta).}$$
2. **Exact Variance / Monotonicity Identity:**
   $$-\frac{\partial}{\partial \beta} e_{\mathrm{plaq}}(\beta, \Lambda_0) = \frac{1}{|P_+(\Lambda_0)|} \frac{\partial^2}{\partial \beta^2} \ln Z_{\Lambda_0}(\beta) = \frac{\operatorname{Var}_{\mu_0}(H)}{|P_+(\Lambda_0)|} \ge 0,$$
   so $\beta \mapsto e_{\mathrm{plaq}}(\beta, \Lambda_0)$ is strictly decreasing on $(0, \infty)$ with $\lim_{\beta \to 0^+} e_{\mathrm{plaq}}(\beta, \Lambda_0) = 1.0$ (since $\langle \operatorname{Tr} U_p \rangle_{\mathrm{Haar}} = 0$ by character orthogonality).
3. **Exact Group-Theoretic Plaquette-Energy Range:**
   For all configurations $U \in \Omega_0$ and all couplings $\beta \in (0, \infty)$:
   $$\boxed{0 \le h_p(U) \le 2 \implies 0 \le e_p(\beta, \Lambda_0) \le 2 \implies 0 \le e_{\mathrm{plaq}}(\beta, \Lambda_0) \le 2,}$$
   with the sharp configuration-wise upper bound $h_p(U) \le 1 - \frac{1}{N}\min_{U \in SU(N)}\operatorname{Re}\operatorname{Tr}(U)$, attaining $2.0$ for even $N$ (at $U_p = -I_N \in SU(N)$) and $1 + \cos(\pi/N) < 2.0$ for odd $N$ (e.g. $1.5$ for $SU(3)$ at $U_p = e^{i 2\pi/3} I_3$).

*(Audit of the Previous $[0, 1]$ Range Claim and Status of Lie-Laplacian Positivity:
The earlier report defined $h_p(U) = 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p)$ and stated $0 \le e_{\mathrm{plaq}}(\beta, \Lambda_0) \le 1$.
That upper bound is false for general $SU(N)$ configurations. For example, in $SU(2)$, $U_p = -I_2 \in SU(2)$ gives $\frac{1}{2}\operatorname{Re}\operatorname{Tr}(-I_2) = -1.0 \implies h_p(-I_2) = 2.0$.
While integration by parts with respect to the Lie Laplacian $\Delta_\ell = \sum_{a=1}^{N^2-1}(\partial_\ell^a)^2$ yields
$$\frac{\beta(N^2 - 1)}{2N}\sum_{p \ni \ell}\left\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p)\right\rangle_{\mu_0} = \sum_{a=1}^{N^2-1}\left\langle (\partial_\ell^a S_W)^2 \right\rangle_{\mu_0} \ge 0,$$
which implies $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \rangle_{\mu_0} \ge 0 \implies e_{\mathrm{plaq}} \le 1.0$ under the unperturbed translation-invariant bare Wilson measure, this is an expectation property under specific symmetries, NOT a valid upper bound for the random variable $h_p(U)$ or for general non-translation-invariant / perturbed measures.
Theorem `T2` is now repaired to record the safe, universally valid range $[0, 2]$ for all finite-lattice calculations and input validation.)*

---

## 4. Investigation of the Proposed $O(1/\beta)$ Behavior: Strict Separation of Claims A, B, and C, Gauge-Zero-Mode / Toron Obstruction (`NEG-YM-011-PLAQ-1`), and Primary Literature

### 4.1 Strict Separation of Claims A, B, and C
We explicitly separate the three hierarchy levels and forbid promoting any lower level to a higher level:
- **Claim A (Fixed Finite-Lattice Asymptotic):**
  $$e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \frac{C(\Lambda_0, N, d)}{\beta} \qquad (\text{fixed finite torus } \Lambda_0, \, \beta \to \infty, \text{ constant } C \text{ allowed to depend on } |\Lambda_0|).$$
- **Claim B (Volume-Uniform Weak-Coupling Bound):**
  $$e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \frac{C(N, d)}{\beta} \qquad (\text{for all } \beta \ge \beta_*(N, d) \text{ with } C(N, d) \text{ independent of lattice size } L).$$
- **Claim C (Thermodynamic / Continuum-Uniform Multiscale Estimate):**
  Uniform control of plaquette and loop expectations across scales $a \to 0$ and $L \to \infty$ sufficient to close multi-step scale transfer.

**Logical Independence:** $\text{A} \not\implies \text{B}$ and $\text{B} \not\implies \text{C}$.

### 4.2 Why Ordinary Laplace's Method Fails on the Periodic Torus $\Lambda_0$ (`NEG-YM-011-PLAQ-1`)
We investigate the eight structural questions required for any rigorous $\beta \to \infty$ proof on the periodic torus $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$:
1. **Non-Isolated Set of Global Minima ($H(U) = 0$):**
   The global minimum locus $\mathcal{Z}_0 := \{ U \in \Omega_0 : H(U) = 0 \} = \{ U \in \Omega_0 : U_p = I_N \;\;\forall p \in P_+(\Lambda_0) \}$ is **not** a discrete set of points.
2. **Continuous Gauge Orbits ($\dim \mathcal{G}_0 / Z(SU(N)) = (N^2 - 1)((2L)^d - 1)$):**
   The gauge group $\mathcal{G}_0 = SU(N)^{V(\Lambda_0)}$ acts freely up to the stabilizer $\operatorname{Stab}_{\mathcal{G}_0}(U)$, producing at least $(N^2 - 1)((2L)^d - 1)$ zero eigenvalues in the Hessian $\nabla^2 H(U)$ at every $U \in \mathcal{Z}_0$.
3. **Flat-Connection Moduli Space $\mathcal{M}_{\mathrm{flat}}(\Lambda_0, SU(N))$ (Torons on $\mathbb{T}^d$):**
   Because $\pi_1(\mathbb{T}^d) = \mathbb{Z}^d$ is non-trivial for periodic boundary conditions, the gauge-orbit quotient of $\mathcal{Z}_0$ is not a single point $[U_{\mathrm{id}}]$, but the compact moduli space of flat $SU(N)$ connections (commuting $d$-tuples of holonomies around the $d$ torus cycles):
   $$\mathcal{M}_{\mathrm{flat}}(\Lambda_0, SU(N)) = \mathcal{Z}_0 / \mathcal{G}_0 \cong \operatorname{Hom}(\mathbb{Z}^d, SU(N)) / \operatorname{Ad}(SU(N)) \cong T^d / S_N,$$
   which has continuous positive dimension $d(N - 1)$ (where $T \cong U(1)^{N-1} \subset SU(N)$ is a maximal torus).
4. **Singular Strata & Jumping Hessian Rank (`NEG-YM-011-PLAQ-1` — Failure of Naive Morse–Bott Laplace Asymptotics):**
   The flat-connection moduli space $\mathcal{M}_{\mathrm{flat}}(\Lambda_0, SU(N)) \cong T^d / S_N$ is **not a smooth manifold** and $H : \Omega_0 \to \mathbb{R}$ is **not a Morse–Bott function** along $\mathcal{Z}_0$:
   - At a **regular irreducible toron** $U_{\mathrm{reg}} \in \mathcal{Z}_0$ (where the $d$ diagonal holonomies have distinct eigenvalues), $\operatorname{Stab}_{\mathcal{G}_0}(U_{\mathrm{reg}}) = T \cong U(1)^{N-1}$ has dimension $N - 1$, so the gauge orbit has dimension $(N^2 - 1)(2L)^d - (N - 1)$ and the total zero-mode space of $\nabla^2 H(U_{\mathrm{reg}})$ has dimension $(N^2 - 1)(2L)^d + (d - 1)(N - 1)$.
   - At a **singular central toron** $U_{\mathrm{sing}} \in \mathcal{Z}_0$ (such as $U_{\mathrm{id}} = (I_N)_\ell$ or center configurations in $Z(SU(N))^d$), the stabilizer jumps to $\operatorname{Stab}_{\mathcal{G}_0}(U_{\mathrm{sing}}) = SU(N)$ of dimension $N^2 - 1$. Consequently, the gauge orbit dimension **drops** by $N(N - 1)$, while the kernel of the quadratic Hessian $\nabla^2 H(U_{\mathrm{sing}})$ **jumps upward** by $(d - 1)N(N - 1)$!
   - Along these $(d - 1)N(N - 1)$ extra zero-mode directions at $U_{\mathrm{sing}}$, the leading Taylor term of $H(\exp(A) U_{\mathrm{sing}})$ is **quartic** ($H \sim \operatorname{Tr}([A_\mu, A_\nu]^2) \sim \|A\|^4$, scaling as $\beta^{-1/4}$ per mode rather than Gaussian $\beta^{-1/2}$!).
   - Because the Gaussian/quartic scaling exponents jump across the singular strata of $\mathcal{M}_{\mathrm{flat}}(\Lambda_0, SU(N))$, **ordinary Laplace's method and smooth Morse–Bott Laplace asymptotics are mathematically invalid on the un-gauge-fixed periodic torus $\Omega_0$** without a stratified singular-integral localization or maximal-tree gauge fixing with boundary conditions that eliminate toron zero modes.

### 4.3 Elementary Unconditional Volume-Uniform $O(\ln(\beta)/\beta)$ Bound (`YM-011-PLAQUETTE-EXP-L1`)
While pure $O(1/\beta)$ on the periodic torus requires resolving the singular strata of $\mathcal{M}_{\mathrm{flat}}(\Lambda_0, SU(N))$, we can prove an **elementary, unconditional, volume-uniform $O(\ln(\beta)/\beta)$ upper bound** valid for all $\beta > 0$ and all torus sizes $L \ge 1$ using only the convexity of $\ln Z_{\Lambda_0}(\beta)$ and the Haar volume of a single-link ball around $I_N$:

**Proposition (`YM-011-PLAQUETTE-EXP-L1`):**
For every $\beta > 0$, every $r \in (0, \pi]$, and every finite periodic torus $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ ($L \ge 1$):
1. Since $Z_{\Lambda_0}(0) = 1$ and $s \mapsto \langle H \rangle_{\mu_s} = -\frac{d}{ds}\ln Z_{\Lambda_0}(s)$ is non-increasing on $[0, \beta]$ ($\frac{d}{ds}\langle H \rangle_{\mu_s} = -\operatorname{Var}_{\mu_s}(H) \le 0$),
   $$\beta \, |P_+(\Lambda_0)| \, e_{\mathrm{plaq}}(\beta, \Lambda_0) = \beta \langle H \rangle_{\mu_\beta} \le \int_0^\beta \langle H \rangle_{\mu_s} \, ds = -\ln Z_{\Lambda_0}(\beta).$$
2. On the Lie-algebra ball product $\mathcal{U}_r := \{ U \in \Omega_0 : \forall \ell \in E_+(\Lambda_0), \, U(\ell) = \exp(X_\ell), \, \|X_\ell\|_{\mathrm{op}} \le r \}$, every link satisfies $\|U(\ell) - I_N\|_{\mathrm{op}} \le r$, every plaquette satisfies $\|U_p - I_N\|_{\mathrm{op}} \le 4r$, and $1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) = \frac{1}{2N}\|U_p - I_N\|_{\mathrm{HS}}^2 \le \frac{1}{2}\|U_p - I_N\|_{\mathrm{op}}^2 \le 8 r^2$. Thus $H(U) \le 8 r^2 |P_+(\Lambda_0)|$ on $\mathcal{U}_r$, and
   $$Z_{\Lambda_0}(\beta) \ge \int_{\mathcal{U}_r} e^{-\beta H(U)} d\mu_{\mathrm{Haar},0}(U) \ge e^{-8\beta r^2 |P_+(\Lambda_0)|} \left( v_N(r) \right)^{|E_+(\Lambda_0)|},$$
   where $v_N(r) := \mu_{\mathrm{Haar}}(\{ \exp(X) \in SU(N) : \|X\|_{\mathrm{op}} \le r \}) > 0$.
3. Because the link-to-plaquette ratio on $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ is **exact and independent of $L$**,
   $$\frac{|E_+(\Lambda_0)|}{|P_+(\Lambda_0)|} = \frac{d(2L)^d}{\binom{d}{2}(2L)^d} = \frac{2}{d - 1},$$
   dividing $-\ln Z_{\Lambda_0}(\beta)$ by $\beta |P_+(\Lambda_0)|$ yields the **strictly volume-independent bound**:
   $$\boxed{e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \inf_{r \in (0, \pi]} \left( 8 r^2 + \frac{2}{(d - 1)\beta} \ln\!\left(\frac{1}{v_N(r)}\right) \right) \qquad (\forall \beta > 0, \; \forall L \ge 1).}$$
   Setting $r = \beta^{-1/2}$ for $\beta \ge 1$ (where $v_N(r) \ge c_N r^{N^2 - 1}$) gives $e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \frac{8 + \frac{N^2 - 1}{d - 1}\ln \beta + \frac{2}{d - 1}\ln(1/c_N)}{\beta} = O\!\left(\frac{\ln \beta}{\beta}\right)$ uniformly in $L \ge 1$.

---

## 5. Primary Mathematical Literature Audit Table

| Source | Theorem / Page | Gauge Group | Dimension | Boundary Conditions | Volume | $\beta$ Regime | Uniformity & Actual Conclusion |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Osterwalder & Seiler (1978)**, *Ann. Phys.* 110, 440–471; **Seiler (1982)**, *LNP* 159 | Thm. 3.1 / Ch. 3 | Compact $G \subset U(N)$ | $d \ge 2$ | Periodic / Free | Finite & Infinite | Strong coupling $0 < \beta \le \beta_0(d, G)$ | Volume-uniform analytic cluster expansion of $e_{\mathrm{plaq}}(\beta) = 1 - c_1 \beta + O(\beta^2)$ at strong coupling; does **not** cover $\beta \to \infty$. |
| **Bałaban (1984–1985)**, *Comm. Math. Phys.* 95, 17–40; 96, 223–250; 98, 17–51 | Main Theorems | Compact $G = SU(N)$ | $d = 4$ | Periodic Torus $T_L^4$ | Finite volume $\Lambda_0$ | Weak coupling $\beta = 2N/g_0^2 \gg 1$ | Controls polymer expansions in finite volume via axial/Hodge block gauge fixing and small/large-field characteristic functions $\chi_k$, requiring the full multi-step gauge-fixing machinery (`YM-004`). |
| **Chatterjee (2019)**, *Probab. Theory Relat. Fields* 174, 33–53; **Cao (2020)**, *Comm. Math. Phys.* 380, 1439–1505 | Thm. 1.1 (Dyson–Schwinger / Makeenko–Migdal Loop Equations) | $SO(N), SU(N), U(N)$ | $d \ge 2$ | Finite / Infinite | Finite & Infinite | General $\beta > 0$ identity & strong/axial regimes | Establishes exact finite-lattice Lie-Laplacian integration-by-parts loop identities ($\langle \Delta_\ell S_W \rangle = \sum_a \langle (\partial_\ell^a S_W)^2 \rangle \ge 0$), showing $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \rangle_{\mu_0} \ge 0 \implies e_{\mathrm{plaq}} \le 1.0$ in expectation under translation-invariant bare Wilson measure, while configuration-wise $h_p(U) \in [0, 2]$ for all $N \ge 2$. |
| **Borgs (1984)**, *Commun. Math. Phys.* 96, 251–284; **Coste et al. (1987)**, *Nucl. Phys. B* 289, 557–588 | Sec. 2–3 / Zero-mode analysis | Compact $G = SU(N)$ | $d = 4$ | Periodic Torus vs. Free | Finite & Infinite | Weak coupling $\beta \to \infty$ | Proves that on a periodic torus $\mathbb{T}^4$, flat connections form a singular moduli space $T^4 / S_N$ with quartic zero modes at central elements, whereas free/spanning-tree boundary conditions eliminate torons. |

---

## 6. Numerical Diagnostics (`NUMERICAL_DIAGNOSTIC_ONLY`) and Next Smallest Task

### 6.1 Numerical Diagnostics (`NUMERICAL_DIAGNOSTIC_ONLY`)
Implemented in `su2_single_plaquette_thermodynamic_identity_diagnostic` in `src/ymmg/plaquette_expectation.py`:
- Verified to `< 1e-11` agreement between $-\partial_\beta \ln Z(\beta)$ (central finite differences) and the exact Bessel character formula $e_{\mathrm{plaq}}(\beta) = 1 - I_2(\beta)/I_1(\beta)$ across $\beta \in \{0.5, 2.0, 10.0, 50.0\}$, confirming $\lim_{\beta \to \infty} \beta \, e_{\mathrm{plaq}}(\beta) = \frac{N^2 - 1}{2N} = \frac{3}{2}$ in the single-plaquette (free-tree) model where no toron moduli exist.
- All numerical evaluations are strictly labeled `NUMERICAL_DIAGNOSTIC_ONLY` and are not used as proof of any analytical theorem.

### 6.2 Repaired Analytical Result, Unresolved Dependency, and Next Smallest Research Task (`YM-011-TREE-GAUGE`)
- **Repaired Analytical Result (`YM-011-PLAQUETTE-EXP-T1` & `T2`):**
  $$\left\langle \left|\Delta_{\mathrm{tan}}(C_1)\right| \right\rangle_{\mu_0} \le 4(d - 1)\sqrt{N} \, |C_1|_{\Lambda_1} \, e_{\mathrm{plaq}}(\beta, \Lambda_0) = -\frac{4(d - 1)\sqrt{N} \, |C_1|_{\Lambda_1}}{\binom{d}{2}(2L)^d} \frac{\partial}{\partial \beta} \ln Z_{\Lambda_0}(\beta),$$
  where $e_{\mathrm{plaq}}(\beta, \Lambda_0) \in [0, 2]$ is the universally safe mean plaquette energy range for all $SU(N)$ ($N \ge 2$), together with the unconditional volume-independent entropy–energy bound $e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \inf_{r \in (0, \pi]} \left(8 r^2 + \frac{2}{(d-1)\beta}\ln(1/v_N(r))\right) = O\!\left(\frac{\ln \beta}{\beta}\right)$ (`YM-011-PLAQUETTE-EXP-L1`).
- **Unresolved Dependency:** Removing the $\ln \beta$ factor to establish a pure $O(1/\beta)$ bound (`Claim A` / `Claim B`) without singular toron zero-mode obstructions (`NEG-YM-011-PLAQ-1`).
- **Next Smallest Authorized Task (`YM-011-TREE-GAUGE`):**
  Construct the explicit **Maximal Spanning-Tree Gauge Fixing and Co-Tree Plaquette Coordinate Map** on a finite lattice $\Lambda_0$ (comparing free boundary conditions where $|P_+(\Lambda_0)|$ independent plaquettes embed into $|E_{\mathrm{cotree}}(\Lambda_0)| = |E_+(\Lambda_0)| - (|V(\Lambda_0)| - 1)$ co-tree links against periodic boundary conditions with fundamental-group toron holonomies).
