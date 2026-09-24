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

## 2. Verified Precursor Lemma: `YM-011-PRE` (Fixed-Lattice Gradient-Flow Loop Perturbation)

### 2.1 Exact Mathematical Statement (`YM-011-PRE`)

Let $\Lambda \subset a\mathbb{Z}^d$ ($d \ge 2$, specifically $d=4$) be a finite hypercubic lattice with spacing $a > 0$ and compact gauge group $G = SU(N)$ ($N \ge 2$). Let $S_W(U) = \frac{\beta}{N} \sum_{p \subset \Lambda} \operatorname{Re}\operatorname{Tr}(I_N - U_p)$ be the standard Wilson plaquette action with bare coupling $\beta = \frac{2N}{g_0^2} > 0$, and let $d\mu_\Lambda(U) = Z_\Lambda^{-1} e^{-S_W(U)} \prod_{\ell \in E(\Lambda)} dU_\ell$ be the fixed-lattice probability measure.

For any closed lattice loop $C = (\ell_1, \ell_2, \dots, \ell_n)$ composed of $n = |C|/a$ oriented lattice links, define the normalized Wilson loop observable:
$$W_t(C)[U] := \frac{1}{N} \operatorname{Re}\operatorname{Tr}\left( \prod_{m=1}^{n} V_t(\ell_m) \right),$$
where $t \mapsto V_t(\ell) \in SU(N)$ solves the lattice Wilson gradient flow with initial condition $V_0(\ell) = U_\ell$.

**Theorem (`YM-011-PRE`):**
For every flow time $t \ge 0$, every lattice gauge configuration $U \in SU(N)^{E(\Lambda)}$, and every closed loop $C$ of length $n = |C|/a$ links, the flowed Wilson loop satisfies both the **pointwise configuration bound**:
$$\boxed{\left| W_t(C)[U] - W_0(C)[U] \right| \le K(\beta, d, N) \, n \, \frac{t}{a^2}}$$
and the **expectation-level bound** with respect to $d\mu_\Lambda$:
$$\boxed{\left| \langle W_t(C) \rangle_\Lambda - \langle W_0(C) \rangle_\Lambda \right| \le K(\beta, d, N) \, n \, \frac{t}{a^2},}$$
where:
1. Under **Lüscher's (2010) standard dimensionless gradient-flow convention** $a^2 \partial_t V_t(\ell) = -g_0^2 \left(\partial_\ell S_W(V_t)\right) V_t(\ell)$, the bare coupling $\beta = \frac{2N}{g_0^2}$ **cancels identically**, yielding the $\beta$-independent constant:
   $$K(d, N) = 2(d - 1) \qquad (\text{so } K = 6 \text{ in } d = 4).$$
2. Under the **unscaled action-gradient flow convention** $a^2 \partial_\tau V_\tau(\ell) = -\left(\partial_\ell S_W(V_\tau)\right) V_\tau(\ell)$, the factor $\beta$ remains linearly in the constant:
   $$K(\beta, d, N) = \frac{\beta (d - 1)}{N}.$$

---

### 2.2 Complete Resolution of the Three Audit Questions (`YM-GOV-014` Section 5)

#### Question 1: Does $\beta$ cancel under the chosen gradient-flow convention or remain in $K(\beta, d, N)$?
- **Exact Derivation:**
  For a single link $\ell \in E(\Lambda)$, let $S_\ell(V) = \sum_{p \ni \ell} U_p^{\text{staple}}$ be the sum of the $2(d-1)$ staple products incident on link $\ell$ ($2(4-1) = 6$ staples in $d=4$). Varying $S_W(V) = \frac{\beta}{N} \sum_p \operatorname{Re}\operatorname{Tr}(I_N - V_p)$ along $V_\ell \mapsto e^{\epsilon X} V_\ell$ ($X \in \mathfrak{su}(N)$) gives the Lie-algebra gradient:
  $$\partial_\ell S_W(V) = -\frac{\beta}{2N} \, \mathcal{P}_{\mathfrak{su}(N)}\!\left( V_\ell S_\ell(V)^\dagger \right) = -\frac{1}{g_0^2} \, \mathcal{P}_{\mathfrak{su}(N)}\!\left( V_\ell S_\ell(V)^\dagger \right),$$
  where $\mathcal{P}_{\mathfrak{su}(N)}(M) = \frac{1}{2}(M - M^\dagger) - \frac{1}{2N}\operatorname{Tr}(M - M^\dagger) I_N$ is the orthogonal projection onto traceless anti-Hermitian matrices $\mathfrak{su}(N)$, and we used the fundamental relation $\beta = \frac{2N}{g_0^2}$.
  - **Under Lüscher's (2010) convention** $a^2 \partial_t V_t(\ell) = -g_0^2 (\partial_\ell S_W(V_t)) V_t(\ell)$:
    Multiplying $\partial_\ell S_W(V_t)$ by $-g_0^2$ produces the factor $g_0^2 \cdot \frac{\beta}{2N} = \frac{2N}{\beta} \cdot \frac{\beta}{2N} \equiv 1$. Thus **$\beta$ and $g_0^2$ cancel identically**! Since each of the $2(d-1)$ staples is a product of three $SU(N)$ matrices, $\|U_p^{\text{staple}}\|_{\mathrm{op}} = 1$, and $\|\mathcal{P}_{\mathfrak{su}(N)}(M)\|_{\mathrm{op}} \le \|M\|_{\mathrm{op}} \le 2(d-1)$, we obtain for every link $\ell$ and all $t \ge 0$:
    $$\left\| \partial_t V_t(\ell) \right\|_{\mathrm{op}} \le \frac{2(d - 1)}{a^2}.$$
  - **Under the unscaled action-gradient flow** $a^2 \partial_\tau V_\tau(\ell) = -(\partial_\ell S_W(V_\tau)) V_\tau(\ell)$:
    The factor $g_0^2$ is absent, so the prefactor $\frac{\beta}{2N}$ remains, giving $\|\partial_\tau V_\tau(\ell)\|_{\mathrm{op}} \le \frac{\beta(d-1)}{N a^2}$.

#### Question 2: Why does the normalized Wilson loop trace satisfy $W_t(C) \in [-1, 1]$, and NOT $[0, 1]$?
- **Exact Proof:**
  For any closed loop $C$, the holonomy $H_t(C) := \prod_{m=1}^n V_t(\ell_m)$ is a product of elements of $SU(N)$ and therefore lies in $SU(N)$. Every $U \in SU(N)$ is unitary with eigenvalues $\lambda_1, \dots, \lambda_N \in S^1 \subset \mathbb{C}$ of the form $\lambda_j = e^{i\theta_j}$ ($\theta_j \in \mathbb{R}$, $\sum_{j=1}^N \theta_j \equiv 0 \pmod{2\pi}$). Therefore:
  $$W_t(C) = \frac{1}{N} \operatorname{Re}\operatorname{Tr}(H_t(C)) = \frac{1}{N} \sum_{j=1}^N \cos\theta_j.$$
  Since $\cos\theta_j \in [-1, 1]$ for all $j$, we have $W_t(C) \in [-1, 1]$ (with $|\operatorname{Re}\operatorname{Tr}(M)| \le N \|M\|_{\mathrm{op}}$ for any $N \times N$ matrix $M$). Specifically:
  - At $H_t(C) = I_N$, $W_t(C) = +1$.
  - For even $N = 2k$, $-I_N \in SU(N)$ has $\det(-I_N) = (-1)^{2k} = +1$ and $W_t(C) = -1$.
  - For odd $N \ge 3$, choosing $\theta_1 = \dots = \theta_{N-1} = \frac{\pi(N-1)}{N}$ and $\theta_N = -\frac{\pi(N-1)^2}{N} \equiv \frac{\pi(N-1)}{N} \pmod{2\pi}$ gives $W_t(C) = \cos\!\left(\frac{\pi(N-1)}{N}\right) < 0$ (e.g., $-\frac{1}{2}$ for $SU(3)$).
  Hence $W_t(C)$ takes strictly negative values for every $N \ge 2$, and its universal normalized range is **$[-1, 1]$, never $[0, 1]$**.

#### Question 3: Is the bound proved pointwise in the gauge configuration and/or in expectation?
- **Exact Proof of Both Pointwise and Expectation Bounds:**
  Fix any gauge configuration $U \in SU(N)^{E(\Lambda)}$. By the Leibniz product rule along the $n$ links $\ell_1, \dots, \ell_n$ of $C$:
  $$\frac{d}{ds} H_s(C) = \sum_{m=1}^{n} V_s(\ell_1) \cdots V_s(\ell_{m-1}) \left( \partial_s V_s(\ell_m) \right) V_s(\ell_{m+1}) \cdots V_s(\ell_n).$$
  Since each $V_s(\ell_j) \in SU(N)$ is unitary, $\|V_s(\ell_j)\|_{\mathrm{op}} = 1$. By submultiplicativity and the triangle inequality of the operator norm:
  $$\left\| \frac{d}{ds} H_s(C) \right\|_{\mathrm{op}} \le \sum_{m=1}^{n} \left\| \partial_s V_s(\ell_m) \right\|_{\mathrm{op}} \le n \, \frac{K(\beta, d, N)}{a^2}.$$
  Using $\left|\frac{1}{N} \operatorname{Re}\operatorname{Tr}(M)\right| \le \|M\|_{\mathrm{op}}$ and the Fundamental Theorem of Calculus for $s \in [0, t]$:
  $$\left| W_t(C)[U] - W_0(C)[U] \right| \le \int_0^t \left| \frac{d}{ds} W_s(C)[U] \right| ds \le \int_0^t \left\| \frac{d}{ds} H_s(C) \right\|_{\mathrm{op}} ds \le K(\beta, d, N) \, n \, \frac{t}{a^2}.$$
  This proves the bound **pointwise for every gauge configuration $U$**. Integrating against any normalized probability measure $d\mu_\Lambda(U)$ on $SU(N)^{E(\Lambda)}$ and applying Jensen's inequality $|\mathbb{E}_\Lambda[X]| \le \mathbb{E}_\Lambda[|X|]$ immediately gives the **expectation-level bound**:
  $$\left| \langle W_t(C) \rangle_\Lambda - \langle W_0(C) \rangle_\Lambda \right| \le \int_{SU(N)^{E(\Lambda)}} \left| W_t(C)[U] - W_0(C)[U] \right| d\mu_\Lambda(U) \le K(\beta, d, N) \, n \, \frac{t}{a^2}. \quad \blacksquare$$

---

## 3. Proposed Future Multiscale Lemma: `YM-011-L1` (`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`)

### Lemma YM-011-L1 (UV Scale-Transfer and Observables Mollification Lemma)

> **Governance Gate (`YM-GOV-014`):** Lemma `YM-011-L1` below defines the proposed multiscale Bałaban-measure extension of `YM-011-PRE`. It remains in status **`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`** until separately authorized after `YM-011-PRE` closeout.

Let $G = SU(N)$ with $N \ge 2$ in $d = 4$ spacetime dimensions on a finite hypercubic lattice $\Lambda = a \mathbb{Z}^4 \cap [-L_0, L_0]^4$. Let $d\mu^{(k)}[A]$ be Bałaban's $k$-th scale small-field effective measure at physical block scale $L_k = a 2^k \le L_*$ with $g_k \le g_*$. This formulation assumes **no mass gap**, no infinite-volume thermodynamic limit, and no specific infrared behavior.

**Statement:**
Determine whether Schwinger–Dyson integration by parts on the Bałaban effective measure $d\mu^{(k)}[A]$ improves the elementary fixed-lattice linear bound $K \cdot (|C|/a) \cdot (t/a^2)$ of `YM-011-PRE` to a block-scale estimate uniform in $a \to 0$ for fixed physical flow time $t$ and physical perimeter $|C|$.

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

