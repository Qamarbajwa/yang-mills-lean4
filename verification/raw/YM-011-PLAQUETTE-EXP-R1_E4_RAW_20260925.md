# INDEPENDENT ADVERSARIAL AUDIT REPORT: TASK `YM-011-PLAQUETTE-EXP-R1`

**Auditor:** Fresh, Blind, Independent Research Subagent  
**Candidate SHA:** `5553891059c6501c022e716016feac38c475cc4a`  
**Closed-World Scientific Tree Hash:** `0e96fcdacf45c4f63721e644ad81810b7fc360df5abc90ffa2391fbe07712326`  
**Task Subject:** Repair of Plaquette-Energy Range $[0, 2]$, Invariance of Theorem T1, and Finite-Lattice Gibbs Expectation Reduction  
**Audited Artifacts:**
1. `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md`
2. `src/ymmg/plaquette_expectation.py`
3. `tests/test_ym_011_plaquette_exp.py`
4. `NEGATIVE_EVIDENCE_REGISTER.md` (`NEG-YM-011-PLAQ-1`, `NEG-YM-011-PLAQ-2`)
5. `governance/PROJECT_STATE.yaml`

---

## 1. Executive Summary & Audit Verdict

An adversarial, first-principles mathematical and governance audit of candidate commit `5553891059c6501c022e716016feac38c475cc4a` was performed.

All eight audit criteria were verified with zero defects:
- **Criterion 1 (Plaquette-Energy Range Repair `[0, 2]`):** PASS (Proven from first principles for all $SU(N)$, including the exact even/odd $N$ group-theoretic distinction).
- **Criterion 2 (Invariance of Theorem `T1`):** PASS (Rigorous Cauchy–Schwarz proof re-verified; constants $C(d, N) = 4(d-1)\sqrt{N}$ and $C_{\mathrm{sharp}}(d, 2) = 4(d-1)$ depend strictly on $\|U_p - I_N\|_{\mathrm{HS}}^2 = 2N h_p(U)$ and are completely unaffected by the range repair).
- **Criterion 3 (Repair of Theorem `T2` & Schwinger–Dyson Status):** PASS (Thermodynamic identities verified; erroneous $[0, 1]$ range removed from universal statement; Lie-Laplacian positivity correctly contextualized).
- **Criterion 4 (Volume-Uniform Bound `L1`):** PASS (Unconditional volume-independent $O(\ln\beta/\beta)$ bound verified from Haar entropy and convexity).
- **Criterion 5 (Separation of Claims A, B, C & Toron Singular Strata):** PASS (`NEG-YM-011-PLAQ-1` verified; pure $O(1/\beta)$ withheld; jumping stabilizer dimension documented).
- **Criterion 6 (Negative Evidence Register & Review Miss Disclosure):** PASS (`NEG-YM-011-PLAQ-2` recorded; root cause disclosed).
- **Criterion 7 (Extremal Configuration Tests & Determinism):** PASS (All 316 test suite cases pass; explicit tests on $I_N$, $-I_2$, $-I_4$, $e^{i2\pi/3}I_3$ and range boundaries).
- **Criterion 8 (Project Invariants & Governance Discipline):** PASS (`GOAL_COMPLETE = false`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `YM-006` through `YM-010 = SCIENTIFIC_REVIEW_HOLD`, `YM-011 = NOT AUTHORIZED`, `YM-011-TREE-GAUGE` not prematurely started).

**AUDIT VERDICT: `INTEGRITY_PASS`**

---

## 2. Detailed Criterion-by-Criterion Verification

### Criterion 1: Plaquette-Energy Range Repair (`[0, 2]`)
**Mathematical Verification:**
The normalized plaquette defect random variable is:
$$h_p(U) := 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) = \frac{1}{2N}\|U_p - I_N\|_{\mathrm{HS}}^2.$$
For any $U_p \in SU(N)$, eigenvalues are $e^{i\theta_1}, \dots, e^{i\theta_N}$ with $\sum_{j=1}^N \theta_j \equiv 0 \pmod{2\pi}$. The normalized real trace is $q_N(U_p) = \frac{1}{N}\sum_{j=1}^N \cos\theta_j \in [-1, 1]$.
1. **Lower Bound:** At $U_p = I_N$, $\theta_j = 0$ for all $j \implies q_N(I_N) = 1 \implies h_p(I_N) = 0$. Since $\cos\theta_j \le 1$, $h_p(U) \ge 0$ universally.
2. **Upper Bound & Even/Odd $N$ Distinction:**
   - **Even $N$ ($N \in \{2, 4, 6, \dots\}$):** $\det(-I_N) = (-1)^N = 1$, so $-I_N \in SU(N)$. At $U_p = -I_N$, $q_N(-I_N) = -1.0$, which yields:
     $$h_p(-I_N) = 1 - (-1) = 2.0.$$
     For $SU(2)$, $U_p = -I_2 \in SU(2)$ gives $h_p(-I_2) = 2.0$, and $\|(-I_2) - I_2\|_{\mathrm{HS}}^2 = \|-2I_2\|_{\mathrm{HS}}^2 = 4 \times 2 = 8 = 2(2)(2.0)$.
   - **Odd $N$ ($N \in \{3, 5, 7, \dots\}$):** $\det(-I_N) = (-1)^N = -1 \ne 1$, so $-I_N \notin SU(N)$. Minimizing $\sum_{j=1}^N \cos\theta_j$ subject to $\sum \theta_j \equiv 0 \pmod{2\pi}$ yields equal angles $\theta_j = \pi - \pi/N$ (since $N(\pi - \pi/N) = (N-1)\pi \equiv 0 \pmod{2\pi}$ for odd $N$). Thus:
     $$\min_{U \in SU(N)} q_N(U) = \cos(\pi - \pi/N) = -\cos(\pi/N) > -1.0 \implies \max_{U \in SU(N)} h_p(U) = 1 + \cos(\pi/N) < 2.0.$$
     For $SU(3)$, $\min q_3 = \cos(2\pi/3) = -0.5$ attained at $U_p = e^{i 2\pi/3} I_3 \in SU(3)$, giving $\max h_p = 1.5$.
   - **Universal Range:** For all $N \ge 2$, $h_p(U) \in [0, 2]$, and for Gibbs expectation $e_{\mathrm{plaq}}(\beta, \Lambda_0) = \langle h_p \rangle_{\mu_0} \in [0, 2]$.
**Conclusion:** Verified from first principles.

---

### Criterion 2: Invariance of Theorem `YM-011-PLAQUETTE-EXP-T1`
**Proof Structure & Invariance Verification:**
From `YM-011-OBS-T2`, the tangent discrepancy satisfies:
$$|\Delta_{\mathrm{tan}}(C_1)[U]| \le \frac{1}{\sqrt{N}} \sum_{k=1}^{|C_1|_{\Lambda_1}} \sum_{\nu \ne \mu_k, \, \sigma \in \{+,-\}} \| P_{1,\nu,\sigma}^{(k)}[U] - I_N \|_{\mathrm{op}} \| P_{2,\nu,\sigma}^{(k)}[U] - I_N \|_{\mathrm{HS}}.$$
By operator norm sub-Hilbert–Schmidt inequality $\|A\|_{\mathrm{op}} \le \|A\|_{\mathrm{HS}}$ and Cauchy–Schwarz on $L^2(\Omega_0, \mu_0)$:
$$\left\langle \|P_1 - I_N\|_{\mathrm{op}} \|P_2 - I_N\|_{\mathrm{HS}} \right\rangle_{\mu_0} \le \sqrt{ \langle \|P_1 - I_N\|_{\mathrm{HS}}^2 \rangle_{\mu_0} \langle \|P_2 - I_N\|_{\mathrm{HS}}^2 \rangle_{\mu_0} } = \sqrt{(2N e_{p_1})(2N e_{p_2})} = 2N\sqrt{e_{p_1} e_{p_2}}.$$
Multiplying by $\frac{1}{\sqrt{N}}$ gives $2\sqrt{N}\sqrt{e_{p_1} e_{p_2}}$ per channel.
On the isotropic periodic torus:
1. Periodic translations $\tau_z$ map $p_1$ to $p_2$ in the same $(\mu_k, \nu)$-plane, giving $e_{p_1} = e_{p_2} = e_{\mu_k \nu}$.
2. Hyperoctahedral axis permutations $S_d$ act transitively on coordinate planes, giving $e_{\mu_k \nu} = e_{\mathrm{plaq}}$ for all planes.
3. Summing $2(d-1)$ transverse channels per coarse edge yields:
   $$C(d, N) = 2(d-1) \times 2\sqrt{N} = 4(d-1)\sqrt{N} \implies C(4, N) = 12\sqrt{N}.$$
4. For $SU(2)$, the exact spectral identity $\|U_p - I_2\|_{\mathrm{op}} \equiv \frac{1}{\sqrt{2}}\|U_p - I_2\|_{\mathrm{HS}}$ holds for all $U_p \in SU(2)$ (including at $U_p = -I_2$, where $2.0 = \frac{1}{\sqrt{2}}(2\sqrt{2})$). Replacing $\|P_1 - I_2\|_{\mathrm{op}}$ gives:
   $$C_{\mathrm{sharp}}(d, 2) = 2(d-1) \times \left(\frac{1}{\sqrt{2}} \times 2\sqrt{2}\right) = 4(d-1) \implies C_{\mathrm{sharp}}(4, 2) = 12.$$
Nowhere in the proof of $T1$ is an upper bound on $e_p$ assumed or utilized; Cauchy–Schwarz holds on $L^2(\Omega_0, \mu_0)$ for any non-negative random variable, and $\|U_p - I_N\|_{\mathrm{HS}}^2 = 2N h_p(U)$ is exact for all $h_p \in [0, 2]$. Thus $T1$ and its constants are strictly invariant.
**Conclusion:** Verified.

---

### Criterion 3: Repair of Theorem `YM-011-PLAQUETTE-EXP-T2` & Schwinger–Dyson Status
**Thermodynamic Identities & Boundary Status Verification:**
1. **First Derivative:** $Z_{\Lambda_0}(\beta) = \int_{\Omega_0} e^{-\beta H(U)} d\mu_{\mathrm{Haar},0}(U)$ with $H(U) = \sum_{p \in P_+} h_p(U)$.
   $$-\partial_\beta \ln Z_{\Lambda_0}(\beta) = \frac{\int H e^{-\beta H} d\mu_0}{Z_{\Lambda_0}(\beta)} = \langle H \rangle_{\mu_0} = \sum_{p \in P_+} e_p(\beta, \Lambda_0) = |P_+(\Lambda_0)| e_{\mathrm{plaq}}(\beta, \Lambda_0).$$
2. **Second Derivative & Monotonicity:**
   $$-\partial_\beta e_{\mathrm{plaq}}(\beta, \Lambda_0) = \frac{1}{|P_+|} \partial_\beta^2 \ln Z_{\Lambda_0}(\beta) = \frac{\operatorname{Var}_{\mu_0}(H)}{|P_+(\Lambda_0)|} \ge 0.$$
   Strictly non-increasing on $(0, \infty)$, with $\lim_{\beta \to 0^+} e_{\mathrm{plaq}}(\beta) = 1.0$ (by Haar orthogonality $\int \operatorname{Tr} U dU = 0$).
3. **Schwinger–Dyson Contextualization:**
   The erroneous claim $e_{\mathrm{plaq}} \le 1.0$ as a configuration-wise upper bound has been completely removed from Theorem $T2$.
   The Lie-Laplacian identity $\sum_a \langle (\partial_\ell^a S_W)^2 \rangle = \frac{\beta(N^2-1)}{2N}\sum_{p \ni \ell}\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \rangle \ge 0$ implies $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \rangle_{\mu_0} \ge 0 \implies e_{\mathrm{plaq}} \le 1.0$ only under translation-invariant bare Wilson measure in expectation, whereas configuration-wise $h_p(U) \in [0, 2]$. This distinction is explicitly documented in lines 102–108 of the analysis document.
**Conclusion:** Verified.

---

### Criterion 4: Volume-Uniform Entropy–Energy Bound `YM-011-PLAQUETTE-EXP-L1`
**Log-Convexity & Haar Measure Bounds Verification:**
1. Monotonicity of $s \mapsto \langle H \rangle_{\mu_s}$ on $[0, \beta]$ implies:
   $$\beta |P_+(\Lambda_0)| e_{\mathrm{plaq}}(\beta, \Lambda_0) = \beta \langle H \rangle_{\mu_\beta} \le \int_0^\beta \langle H \rangle_{\mu_s} ds = -\ln Z_{\Lambda_0}(\beta) + \ln Z_{\Lambda_0}(0) = -\ln Z_{\Lambda_0}(\beta).$$
2. On $\mathcal{U}_r = \{ U \in \Omega_0 : \forall \ell, U(\ell) = e^{X_\ell}, \|X_\ell\|_{\mathrm{op}} \le r \}$, plaquettes satisfy $\|U_p - I_N\|_{\mathrm{op}} \le 4r$, so $h_p(U) \le \frac{1}{2}\|U_p - I_N\|_{\mathrm{op}}^2 \le 8r^2$. Thus $H(U) \le 8r^2 |P_+(\Lambda_0)|$.
3. Lower bounding the partition function on $\mathcal{U}_r$:
   $$Z_{\Lambda_0}(\beta) \ge e^{-8\beta r^2 |P_+(\Lambda_0)|} \left( v_N(r) \right)^{|E_+(\Lambda_0)|}.$$
4. Taking $-\ln$ and dividing by $\beta |P_+(\Lambda_0)|$:
   $$e_{\mathrm{plaq}}(\beta, \Lambda_0) \le 8r^2 + \frac{|E_+(\Lambda_0)|}{|P_+(\Lambda_0)|} \frac{1}{\beta}\ln(1/v_N(r)).$$
5. For any periodic hypercubic lattice $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$, $|E_+| = d(2L)^d$ and $|P_+| = \binom{d}{2}(2L)^d$. Thus:
   $$\frac{|E_+(\Lambda_0)|}{|P_+(\Lambda_0)|} = \frac{d}{\binom{d}{2}} = \frac{2}{d - 1},$$
   which is strictly volume-independent for all $L \ge 1$.
6. For $r = \beta^{-1/2}$ ($\beta \ge 1$), $v_N(r) \ge c_N r^{N^2-1} \implies \ln(1/v_N(r)) \le \frac{N^2-1}{2}\ln\beta + \ln(1/c_N)$, which gives:
   $$e_{\mathrm{plaq}}(\beta, \Lambda_0) \le O\left(\frac{\ln\beta}{\beta}\right) \qquad (\forall L \ge 1).$$
**Conclusion:** Verified.

---

### Criterion 5: Separation of Claims A, B, C & Toron Singular Strata (`NEG-YM-011-PLAQ-1`)
**Epistemic Separation & Obstruction Verification:**
- Claims A (fixed finite lattice asymptotic), B (volume-uniform weak coupling $O(1/\beta)$), and C (thermodynamic / continuum-uniform multiscale bound) are explicitly demarcated as logically independent: $A \not\implies B$ and $B \not\implies C$. Pure $O(1/\beta)$ is NOT claimed as proved.
- The failure of naive Morse–Bott Laplace asymptotics on the un-gauge-fixed periodic torus is rigorously articulated (`NEG-YM-011-PLAQ-1`):
  1. Global minima $\mathcal{Z}_0 = \{ H = 0 \}$ quotiented by $\mathcal{G}_0$ is the flat-connection moduli space $\mathcal{M}_{\mathrm{flat}} \cong T^d / S_N$.
  2. Stabilizers jump: $\dim \operatorname{Stab}(U_{\mathrm{reg}}) = N - 1$ at regular torons, jumping to $N^2 - 1$ at singular central torons $U \in Z(SU(N))^d$.
  3. The quadratic Hessian $\nabla^2 H(U)$ drops rank: its kernel jumps by $(d-1)N(N-1)$ directions along which the action is quartic ($\sim \|A\|^4$).
  4. This eliminates smooth Morse–Bott integration and constitutes a genuine mathematical obstruction to un-gauge-fixed periodic torus asymptotics.
**Conclusion:** Verified.

---

### Criterion 6: Negative Evidence Register & Review Miss Disclosure (`NEG-YM-011-PLAQ-2`)
**Registration & Governance Disclosure Verification:**
- `NEGATIVE_EVIDENCE_REGISTER.md` lines 95–102 record `NEG-YM-011-PLAQ-2`:
  - Epistemic classification: `[EXACT_MATHEMATICAL_COUNTEREXAMPLE_AND_GOVERNANCE_AUDIT]`.
  - Counterexamples: $-I_N$ for even $N$ ($h_p(-I_2) = 2.0$), odd $N$ minimum trace $-\cos(\pi/N)$ ($h_p \le 1.5$ for $SU(3)$).
  - Root cause of review miss explicitly disclosed: Subagent `7fa5a506-82bd-4978-820b-3106cc051995` verified symbolic algebra of Cauchy–Schwarz and the thermodynamic derivative but did not evaluate $h_p(U)$ at extremal Lie group elements $U_p = -I_N$ or separate configuration-wise range from expectation properties under translation invariance.
  - Resolution documented.
**Conclusion:** Verified.

---

### Criterion 7: Extremal Configuration Regression Tests & Determinism
**Test Suite Execution & Boundary Coverage:**
1. `python -m pytest` executed cleanly: **316 passed in 2.22s**.
2. Explicit test coverage in `tests/test_ym_011_plaquette_exp.py`:
   - `test_1b_extremal_group_configurations_and_exact_range`:
     - $U_p = I_N \implies h_p = 0.0$ ($N=2, 3, 4$).
     - $U_p = -I_2 \in SU(2) \implies h_p = 2.0$, identity residual $< 10^{-14}$, exact spectral ratio holds identically: $\|U_p - I_2\|_{\mathrm{op}}/\|U_p - I_2\|_{\mathrm{HS}} = 1/\sqrt{2}$.
     - $U_p = -I_4 \in SU(4) \implies h_p = 2.0$.
     - $U_p = e^{i 2\pi/3} I_3 \in SU(3) \implies h_p = 1.5$.
     - `su_n_plaquette_energy_range(n)` validated for $n \in \{2, 3, 4, 5, 6\}$.
   - `test_2b_range_boundary_validation`:
     - Evaluates $e_{\mathrm{plaq}} = 2.0$ for $SU(2)$ and $SU(3)$.
     - Evaluates $e_{\mathrm{plaq}} = 0.0$.
     - Asserts `ValueError` when $e_{\mathrm{plaq}} < 0.0$ or $e_{\mathrm{plaq}} > 2.0$.
3. Closed-world scientific tree hash verified deterministically: `0e96fcdacf45c4f63721e644ad81810b7fc360df5abc90ffa2391fbe07712326`.
**Conclusion:** Verified.

---

### Criterion 8: Project Invariants & Governance Discipline
**Repository Invariant Verification:**
In `governance/PROJECT_STATE.yaml`:
- Line 6: `goal_complete: false`
- Line 7: `clay_problem: OPEN_AND_UNSOLVED`
- Lines 110, 119, 128, 137, 146: Objectives `YM-006` through `YM-010` remain locked at `status: SCIENTIFIC_REVIEW_HOLD`.
- Line 211: Original `YM-011` remains `status: PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`.
- Line 202: `YM-011-TREE-GAUGE` remains `status: BLOCKED_ON_YM_011_PLAQUETTE_EXP_R1`, with no premature implementation.
- Line 29: `active_contract: "YM-011-PLAQUETTE-EXP-R1"`.
- Line 193: Objective `YM-011-PLAQUETTE-EXP` has `status: REPAIR_REQUIRED` awaiting this audit.
- Working tree is clean on `master` at candidate SHA `5553891059c6501c022e716016feac38c475cc4a`.
**Conclusion:** Verified.

---

## 3. Final Verdict

All eight audit criteria have been independently audited from first principles and verified without defect. The mathematical repair of the plaquette-energy range to $[0, 2]$, the invariance of Theorem $T1$, the volume-independent bound $L1$, the toron singular-strata negative result `NEG-YM-011-PLAQ-1`, the review miss disclosure `NEG-YM-011-PLAQ-2`, the regression suite, and project governance are in full conformance.

```
================================================================================
FINAL AUDIT VERDICT: INTEGRITY_PASS
================================================================================
```
