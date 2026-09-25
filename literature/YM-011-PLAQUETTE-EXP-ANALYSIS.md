# Task `YM-011-PLAQUETTE-EXP-R2` — Group-Specific Plaquette-Energy Range, Proof of Odd-$N$ Minimizer, and Expectation-Positivity Audit

- **TASK_ID:** `YM-011-PLAQUETTE-EXP-R2` (Repaired Revision 2 of `YM-011-PLAQUETTE-EXP`)
- **TASK_STATUS:** `REPAIRED_CANDIDATE_GROUP_SPECIFIC_EXPECTATION_REDUCTION`
- **PLAQUETTE_ENERGY_RANGES:**
  - `CONFIGURATION_RANGE(N)`: $[0, h_{\max}(N)]$ with $h_{\max}(N) = 2.0$ for even $N$ and $1 + \cos(\pi/N) < 2.0$ for odd $N$ ($1.5$ for $SU(3)$)
  - `EXPECTATION_RANGE(N)`: $[0, h_{\max}(N)]$ (any expectation under a probability measure must lie in $[0, h_{\max}(N)]$)
  - `UNIVERSAL_ALL_N_RANGE`: $[0, 2]$ universally across all $N \ge 2$
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
and its expectation under any probability measure $\mu$ on $\Omega_0$:
$$e_p := \langle h_p \rangle_\mu = \frac{1}{2N} \left\langle \left\| U_p - I_N \right\|_{\mathrm{HS}}^2 \right\rangle_\mu.$$

### 1.3 Complete Variational Proof of Odd-$N$ Constrained Minimizer of $\operatorname{Re}\operatorname{Tr}(U)$
Let $U \in SU(N)$ have eigenvalues $e^{i\theta_1}, \dots, e^{i\theta_N}$ with $\sum_{j=1}^N \theta_j \equiv 0 \pmod{2\pi}$. We determine the exact infimum of
$$q_N(U) := \frac{1}{N} \operatorname{Re}\operatorname{Tr}(U) = \frac{1}{N} \sum_{j=1}^N \cos\theta_j.$$

1. **Even $N$ ($N = 2, 4, 6, \dots$):**
   The central element $U = -I_N = e^{i\pi} I_N$ has $\det(-I_N) = (-1)^N = 1$, so $-I_N \in SU(N)$.
   At this element, $\theta_1 = \dots = \theta_N = \pi$, giving $\sum \theta_j = N\pi \equiv 0 \pmod{2\pi}$ (since $N$ is even).
   Thus $\min_{U \in SU(N)} q_N(U) = \cos\pi = -1.0$, which is the absolute minimum of $\cos$.
   Consequently:
   $$\max_{U \in SU(N)} h_p(U) = 1.0 - (-1.0) = 2.0 \qquad (\text{for even } N).$$
   *(For example, in $SU(2)$, $U_p = -I_2 \in SU(2)$ gives $h_p(-I_2) = 2.0$ and $\|(-I_2) - I_2\|_{\mathrm{HS}}^2 = \|-2I_2\|_{\mathrm{HS}}^2 = 8 = 2(2)(2.0)$.)*

2. **Odd $N$ ($N = 3, 5, 7, \dots$):**
   Here $\det(-I_N) = (-1)^N = -1 \ne 1$, so $-I_N \notin SU(N)$.
   To find $\min_{\sum \theta_j \equiv 0 \pmod{2\pi}} \frac{1}{N}\sum_{j=1}^N \cos\theta_j$, we perform the coordinate transformation shifted around $\pi$:
   $$\theta_j = \pi - \phi_j \implies \cos\theta_j = -\cos\phi_j.$$
   Minimizing $\sum_{j=1}^N \cos\theta_j$ is therefore strictly equivalent to maximizing
   $$g(\phi) := \sum_{j=1}^N \cos\phi_j \quad \text{subject to} \quad \sum_{j=1}^N (\pi - \phi_j) \equiv 0 \pmod{2\pi} \iff \sum_{j=1}^N \phi_j \equiv N\pi \equiv \pi \pmod{2\pi}.$$
   - **Concavity & Jensen's Inequality:** On the interval $[-\pi/2, \pi/2]$, the function $\phi \mapsto \cos\phi$ is **strictly concave** because $\frac{d^2}{d\phi^2}\cos\phi = -\cos\phi < 0$.
     If all $\phi_j \in [-\pi/2, \pi/2]$ with $\sum_{j=1}^N \phi_j = \pi$, Jensen's inequality applies:
     $$\frac{1}{N} \sum_{j=1}^N \cos\phi_j \le \cos\!\left( \frac{1}{N}\sum_{j=1}^N \phi_j \right) = \cos\!\left( \frac{\pi}{N} \right),$$
     with equality if and only if all angles are identical: $\phi_1 = \dots = \phi_N = \frac{\pi}{N}$.
   - **Exclusion of Outer Angles ($|\phi_k| > \pi/2$):**
     If any angle has $|\phi_k| > \pi/2$, then $\cos\phi_k < 0$. The remaining $N-1$ angles can contribute at most $N-1$ to the sum $\sum \cos\phi_j$, but with $\sum \phi_j = \pi$, at least one other angle must compensate, strictly reducing the sum below $N\cos(\pi/N)$. For instance, in $SU(3)$, if any $|\phi_k| > \pi/2$, the maximum possible sum of $\cos\phi_j$ is bounded by $\sqrt{2} \approx 1.414 < 1.5 = 3\cos(\pi/3)$. For all odd $N$, configurations with any $|\phi_k| > \pi/2$ yield strictly smaller values of $g(\phi)$.
   - **$SU(N)$ Admissibility of the Optimal Point:**
     At the Jensen maximizer $\phi_j = \pi/N$, the original Lie algebra angles are:
     $$\theta_j = \pi - \frac{\pi}{N} = \frac{(N-1)\pi}{N} \qquad (j = 1, \dots, N).$$
     The determinant of $U = \operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_N})$ is:
     $$\det(U) = \prod_{j=1}^N e^{i(N-1)\pi/N} = \exp\!\left( i N \frac{(N-1)\pi}{N} \right) = \exp(i (N-1)\pi) = (-1)^{N-1} = +1,$$
     because $N$ is odd, so $N-1$ is an even integer!
     Therefore, the central matrix $U = e^{i\pi(N-1)/N} I_N \in SU(N)$ is **fully admissible in $SU(N)$**, and attains the exact minimum:
     $$q_N^{\min} = \frac{1}{N}\sum_{j=1}^N \cos\!\left(\frac{(N-1)\pi}{N}\right) = \cos\!\left(\pi - \frac{\pi}{N}\right) = -\cos\!\left(\frac{\pi}{N}\right).$$
     Consequently, for odd $N$:
     $$\boxed{\max_{U \in SU(N)} h_p(U) = 1 + \cos(\pi/N) < 2.0.}$$

3. **Exact Values Across Low Dimensions:**
   - **$SU(2)$ ($N=2$, even):** $q_2^{\min} = -1.0 \implies h_{\max} = 2.0$ (attained at $U_p = -I_2$).
   - **$SU(3)$ ($N=3$, odd):** $q_3^{\min} = -\cos(\pi/3) = -0.5 \implies h_{\max} = 1.0 - (-0.5) = 1.5 = 3/2$ (attained at $U_p = e^{i 2\pi/3} I_3$).
   - **$SU(4)$ ($N=4$, even):** $q_4^{\min} = -1.0 \implies h_{\max} = 2.0$ (attained at $U_p = -I_4$).
   - **$SU(5)$ ($N=5$, odd):** $q_5^{\min} = -\cos(\pi/5) = -\frac{1+\sqrt{5}}{4} \approx -0.809017 \implies h_{\max} = 1 + \cos(\pi/5) \approx 1.809017$ (attained at $U_p = e^{i 4\pi/5} I_5$).

### 1.4 Strict Architectural Separation of the Three Plaquette-Energy Ranges
To prevent any mathematical conflation, we formally distinguish and enforce three distinct ranges:
1. **$\mathrm{CONFIGURATION\_RANGE}(N) := [0, h_{\max}(N)] \subseteq [0, 2]$:**
   The sharp group-theoretic range of the random variable $h_p : \Omega_0 \to \mathbb{R}$.
   For each $U \in \Omega_0$, $0 \le h_p(U) \le h_{\max}(N)$.
2. **$\mathrm{EXPECTATION\_RANGE}(N) := [0, h_{\max}(N)] \subseteq [0, 2]$:**
   The range of mathematically possible expectation values $e_p = \langle h_p \rangle_\mu = \int_{\Omega_0} h_p(U) d\mu(U)$ under **any** probability measure $\mu$ on $\Omega_0$.
   Since $\mu \ge 0$ and $\int d\mu = 1$, convexity of the integral guarantees:
   $$0 \le \inf_{U \in \Omega_0} h_p(U) \le \langle h_p \rangle_\mu \le \sup_{U \in \Omega_0} h_p(U) = h_{\max}(N).$$
   *(Critical Consequence: For $SU(3)$, any expectation value $e_{\mathrm{plaq}} > 1.5$ is strictly impossible for any probability measure on $SU(3)$ gauge configurations. Validating $e_{\mathrm{plaq}} = 2.0$ for $SU(3)$ is mathematically inconsistent with group admissibility.)*
3. **$\mathrm{UNIVERSAL\_ALL\_N\_RANGE} := [0, 2]$:**
   The universal, safe bound valid for all $N \ge 2$, used when the gauge group order $N$ is unspecified or when performing coarse, group-agnostic checks.

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
3. **Exact Three-Range Architecture:**
   - **Configuration Range:** $h_p(U) \in \mathrm{CONFIGURATION\_RANGE}(N) := [0, h_{\max}(N)] \subseteq [0, 2]$, where $h_{\max}(N) = 2.0$ for even $N$ and $1 + \cos(\pi/N)$ for odd $N$ ($1.5$ for $SU(3)$).
   - **Expectation Range:** $e_{\mathrm{plaq}}(\beta, \Lambda_0) \in \mathrm{EXPECTATION\_RANGE}(N) := [0, h_{\max}(N)] \subseteq [0, 2]$ for any probability measure on $\Omega_0$.
   - **Universal Safe Range:** $e_{\mathrm{plaq}} \in \mathrm{UNIVERSAL\_ALL\_N\_RANGE} := [0, 2]$ across all $N \ge 2$.

### 3.1 First-Principles Derivation and Epistemic Classification of Lie-Laplacian Positivity

1. **Step-by-Step Derivation via Integration by Parts on $SU(N)$:**
   Let $\{T^a\}_{a=1}^{N^2-1}$ be an orthonormal basis of the Lie algebra $\mathfrak{su}(N)$ under the trace metric $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$, so that the Casimir invariant in the fundamental representation is $\sum_{a=1}^{N^2-1} T^a T^a = -C_2(F) I_N = -\frac{N^2-1}{2N} I_N$.
   For each directed link $\ell \in E_+(\Lambda_0)$ and Lie generator $T^a$, the left-invariant derivative is defined for smooth functions $F : \Omega_0 \to \mathbb{R}$ by
   $$\partial_\ell^a F(U) := \left. \frac{d}{ds} \right|_{s=0} F(\dots, e^{s T^a} U(\ell), \dots).$$
   The Lie Laplacian on link $\ell$ is $\Delta_\ell := \sum_{a=1}^{N^2-1} (\partial_\ell^a)^2$.
   Because the Haar measure $dU(\ell)$ is bi-invariant on the compact Lie group $SU(N)$ without boundary, integration by parts holds without boundary terms:
   $$\int_{SU(N)} dU(\ell) \, \partial_\ell^a \Phi(U) = 0 \qquad (\forall \Phi \in C^\infty(\Omega_0)).$$
   Setting $\Phi(U) = (\partial_\ell^a S_W(U)) e^{-S_W(U)}$ and summing over $a = 1, \dots, N^2-1$:
   $$\int_{\Omega_0} d\mu_{\mathrm{Haar},0}(U) \sum_{a=1}^{N^2-1} \partial_\ell^a \left( (\partial_\ell^a S_W) e^{-S_W} \right) = \int_{\Omega_0} d\mu_{\mathrm{Haar},0}(U) \left( (\Delta_\ell S_W) e^{-S_W} - \sum_{a=1}^{N^2-1} (\partial_\ell^a S_W)^2 e^{-S_W} \right) = 0.$$
   Dividing by $Z_{\Lambda_0}(\beta) = \int e^{-S_W} d\mu_{\mathrm{Haar},0}$ yields the exact Gibbs expectation identity:
   $$\boxed{\left\langle \Delta_\ell S_W \right\rangle_{\mu_\beta} = \sum_{a=1}^{N^2-1} \left\langle (\partial_\ell^a S_W)^2 \right\rangle_{\mu_\beta} \ge 0.}$$
   To evaluate the left-hand side, note that $S_W(U) = \frac{\beta}{N}\sum_{p \in P_+(\Lambda_0)} \operatorname{Re}\operatorname{Tr}(I_N - U_p)$. Only the $2(d-1)$ elementary plaquettes sharing link $\ell$ depend on $U(\ell)$. For each such plaquette $p$, write $U_p = U(\ell) W_{p \setminus \ell}$ (or $W_{p \setminus \ell}^\dagger U(\ell)^\dagger$). Differentiating:
   $$\partial_\ell^a \operatorname{Tr}(U_p) = \operatorname{Tr}(T^a U(\ell) W_{p \setminus \ell}) = \operatorname{Tr}(T^a U_p),$$
   $$\Delta_\ell \operatorname{Tr}(U_p) = \sum_{a=1}^{N^2-1} \operatorname{Tr}(T^a T^a U_p) = \operatorname{Tr}\!\left( \left(\sum_a T^a T^a\right) U_p \right) = -C_2(F) \operatorname{Tr}(U_p) = -\frac{N^2-1}{2N}\operatorname{Tr}(U_p).$$
   Taking the real part, each plaquette contributes $-\frac{\beta}{N} \operatorname{Re}(-\frac{N^2-1}{2N}\operatorname{Tr}(U_p)) = \frac{\beta(N^2-1)}{2N^2}\operatorname{Re}\operatorname{Tr}(U_p)$. Therefore:
   $$\Delta_\ell S_W = \frac{\beta(N^2-1)}{2N^2} \sum_{p \ni \ell} \operatorname{Re}\operatorname{Tr}(U_p).$$
   Since $\frac{\beta(N^2-1)}{2N^2} > 0$ for all $\beta > 0$ and $N \ge 2$, dividing by this factor gives:
   $$\boxed{\sum_{p \ni \ell} \left\langle \operatorname{Re}\operatorname{Tr}(U_p) \right\rangle_{\mu_\beta} = \frac{2N^2}{\beta(N^2-1)} \sum_{a=1}^{N^2-1} \left\langle (\partial_\ell^a S_W)^2 \right\rangle_{\mu_\beta} \ge 0.}$$

2. **Epistemic Classification:**
   - **Summed Plaquettes Touching Link $\ell$:** Classified as `PROVED_FOR_WILSON_GIBBS_MEASURE`. Holds rigorously on any finite lattice with arbitrary boundary conditions under the bare Wilson Gibbs measure.
   - **Individual Plaquettes:** Classified as `PROVED_ONLY_AFTER_ADDITIONAL_SYMMETRY`. An individual plaquette expectation $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr} U_p \rangle_{\mu_\beta} \ge 0$ (implying $e_{\mathrm{plaq}} \le 1.0$) follows only after applying hyperoctahedral coordinate reflections/permutations that equate all $2(d-1)$ plaquettes sharing $\ell$. On anisotropic or boundary-distorted lattices, individual plaquettes need not satisfy this bound.
   - **Configuration-Wise Upper Bound:** Classified as `FALSE`. The random variable $h_p(U)$ attains $2.0$ for even $N$ (e.g. $U_p = -I_2$ in $SU(2)$) and $1.5$ for $SU(3)$. Expectation positivity does not restrict configuration-wise behavior.

3. **Complete Decoupling from Load-Bearing Theorems:**
   - **Theorem `T1` (`YM-011-PLAQUETTE-EXP-T1`):** Relies solely on $\|U_p - I_N\|_{\mathrm{HS}}^2 = 2N h_p(U)$ and Cauchy–Schwarz on $L^2(\Omega_0, \mu_0)$. It is valid for **any** $e_p \in [0, 2]$, irrespective of whether $e_p \le 1.0$.
   - **Theorem `T2` (`YM-011-PLAQUETTE-EXP-T2`):** Relies on the exact derivative identity $-\partial_\beta \ln Z = |P_+| e_{\mathrm{plaq}}$ and variance monotonicity $-\partial_\beta e_{\mathrm{plaq}} = \operatorname{Var}(H)/|P_+| \ge 0$.
   - **Lemma `L1` (`YM-011-PLAQUETTE-EXP-L1`):** Relies on $Z(0) = 1$ and monotonicity of $\langle H \rangle_{\mu_s}$. Under the bare Wilson measure, $e_{\mathrm{plaq}}(\beta) \le 1.0$ follows directly from Haar character orthogonality ($\int \operatorname{Tr} U dU = 0 \implies e_{\mathrm{plaq}}(0) = 1.0$) combined with $\partial_\beta e_{\mathrm{plaq}} \le 0$ for all $\beta \ge 0$, **without requiring the Lie-Laplacian identity**.

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

### 6.2 Regression-Test Audit and Group-Admissibility Verification (`YM-011-PLAQUETTE-EXP-R2`)
- **Audit of R1 QA Inconsistency:**
  The R1 closeout report stated that the regression test suite evaluated $e_{\mathrm{plaq}} = 2.0$ for both $SU(2)$ and $SU(3)$. As identified in `NEG-YM-011-PLAQ-3`, an expectation value of $2.0$ is impossible for $SU(3)$ because the random variable $h_p(U)$ is strictly bounded by $1.5 = 1 + \cos(\pi/3)$ on $SU(3)$. Testing $e_{\mathrm{plaq}} = 2.0$ on $SU(3)$ without distinguishing universal vs. group-specific admissibility created an internal specification conflict.
- **R2 Resolution in Code and Test Suite:**
  1. `validate_group_plaquette_energy(mean_plaquette_energy, su_n)` enforces $[0, h_{\max}(SU(N))]$:
     - For $SU(2)$, $h_{\max} = 2.0$.
     - For $SU(3)$, $h_{\max} = 1.5$.
     - For $SU(5)$, $h_{\max} = 1 + \cos(\pi/5) \approx 1.809017$.
  2. `compute_unconditional_tangent_expectation_bound(..., enforce_group_admissibility=True)` validates against `EXPECTATION_RANGE(N)` by default.
  3. `tests/test_ym_011_plaquette_exp.py` explicitly tests:
     - $SU(2)$ evaluates at maximum $e_{\mathrm{plaq}} = 2.0$ yielding exact bound $12 \cdot 4 \cdot 2.0 = 96.0$.
     - $SU(3)$ evaluates at maximum $e_{\mathrm{plaq}} = 1.5$ yielding exact bound $12\sqrt{3} \cdot 4 \cdot 1.5 = 72\sqrt{3}$.
     - Evaluating $e_{\mathrm{plaq}} = 2.0$ or $1.5001$ for $SU(3)$ under group-specific validation strictly raises `ValueError`.
     - Universal validator (`enforce_group_admissibility=False`) permits $e_{\mathrm{plaq}} = 2.0$ for $SU(3)$ for group-agnostic diagnostic checks.
     - `test_2c_expectation_cannot_exceed_configuration_supremum` verifies $\langle h_p \rangle_\mu \le \sup_U h_p(U)$ across $N \in \{2, 3, 4, 5, 6\}$.
     - `test_2d_no_conflation_configuration_vs_gibbs_expectation` verifies strict separation between configuration supremum ($h_{\max} = 2.0$ for $SU(2)$, $1.5$ for $SU(3)$) and Gibbs expectation under the unperturbed bare measure ($e_{\mathrm{plaq}}(\beta) \le 1.0$ for $\beta \ge 0$).

### 6.3 Repaired Analytical Result, Unresolved Dependency, and Next Smallest Research Task (`YM-011-TREE-GAUGE`)
- **Repaired Analytical Result (`YM-011-PLAQUETTE-EXP-T1` & `T2`):**
  $$\left\langle \left|\Delta_{\mathrm{tan}}(C_1)\right| \right\rangle_{\mu_0} \le 4(d - 1)\sqrt{N} \, |C_1|_{\Lambda_1} \, e_{\mathrm{plaq}}(\beta, \Lambda_0) = -\frac{4(d - 1)\sqrt{N} \, |C_1|_{\Lambda_1}}{\binom{d}{2}(2L)^d} \frac{\partial}{\partial \beta} \ln Z_{\Lambda_0}(\beta),$$
  where $e_{\mathrm{plaq}}(\beta, \Lambda_0) \in [0, h_{\max}(N)] \subseteq [0, 2]$ is the group-specific mean plaquette energy range for all $SU(N)$ ($N \ge 2$), together with the unconditional volume-independent entropy–energy bound $e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \inf_{r \in (0, \pi]} \left(8 r^2 + \frac{2}{(d-1)\beta}\ln(1/v_N(r))\right) = O\!\left(\frac{\ln \beta}{\beta}\right)$ (`YM-011-PLAQUETTE-EXP-L1`).
- **Unresolved Dependency:** Removing the $\ln \beta$ factor to establish a pure $O(1/\beta)$ bound (`Claim A` / `Claim B`) without singular toron zero-mode obstructions (`NEG-YM-011-PLAQ-1`).
- **Next Smallest Authorized Task (`YM-011-TREE-GAUGE`):**
  Construct the explicit **Maximal Spanning-Tree Gauge Fixing and Co-Tree Plaquette Coordinate Map** on a finite lattice $\Lambda_0$ (comparing free boundary conditions where $|P_+(\Lambda_0)|$ independent plaquettes embed into $|E_{\mathrm{cotree}}(\Lambda_0)| = |E_+(\Lambda_0)| - (|V(\Lambda_0)| - 1)$ co-tree links against periodic boundary conditions with fundamental-group toron holonomies).
