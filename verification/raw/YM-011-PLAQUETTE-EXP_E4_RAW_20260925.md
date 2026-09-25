# Raw E4 Independent Verification Receipt — `YM-011-PLAQUETTE-EXP`

- **Subagent Conversation ID:** `7fa5a506-82bd-4978-820b-3106cc051995`
- **Transcript URI:** `file:///C:/Users/arqam/.gemini/antigravity/brain/7fa5a506-82bd-4978-820b-3106cc051995/.system_generated/logs/transcript.jsonl`
- **Audited Candidate SHA:** `6b2c45d345a053e2e7790b3a646a2ba8a73dd214`
- **Scientific Tree Hash:** `a26a5c2dcd74a2b711a47c6e6ebb28bee7f5d33eb31c3d6c7cc0b9d8e60d43cb`
- **Timestamp:** `2026-09-25T11:53:39Z`
- **Verdict:** `INTEGRITY_PASS`

---

## Verbatim Report

# Independent Adversarial Mathematical & Governance Audit Report: `YM-011-PLAQUETTE-EXP`

- **Audited Task:** `YM-011-PLAQUETTE-EXP` (*Finite-Lattice Gibbs Expectation Bound for the Quadratic Plaquette Tangent Defect*)
- **Candidate SHA:** `6b2c45d345a053e2e7790b3a646a2ba8a73dd214`
- **Scientific Tree Hash (`F_scientific`):** `a26a5c2dcd74a2b711a47c6e6ebb28bee7f5d33eb31c3d6c7cc0b9d8e60d43cb`
- **Audited Artifacts:**
  1. `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md`
  2. `src/ymmg/plaquette_expectation.py`
  3. `tests/test_ym_011_plaquette_exp.py`
  4. `NEGATIVE_EVIDENCE_REGISTER.md` (`NEG-YM-011-PLAQ-1`)

---

## 1. Item-by-Item First-Principles Mathematical & Governance Audit

### Item 1: The Expectation Inequality (`YM-011-PLAQUETTE-EXP-T1`) — **VERIFIED**
- **Pointwise Input (`YM-011-OBS-T2`):** Verified against `literature/YM-011-OBS-MAP-CONSTRUCTION.md` (lines 170–183) that under the scale-matching relation $\alpha(t) = 2(d-1)\frac{t}{a^2}$, the initial tangent discrepancy rate of a closed coarse loop $C_1 = (e_1, \dots, e_m)$ satisfies
  $$\left|\Delta_{\mathrm{tan}}(C_1)[U]\right| \le \frac{1}{\sqrt{N}} \sum_{k=1}^{|C_1|_{\Lambda_1}} \sum_{\nu \ne \mu_k, \, \sigma \in \{+,-\}} \left\| P_{1,\nu,\sigma}^{(k)}[U] - I_N \right\|_{\mathrm{op}} \, \left\| P_{2,\nu,\sigma}^{(k)}[U] - I_N \right\|_{\mathrm{HS}}.$$
- **Exact $SU(N)$ Hilbert–Schmidt Identity:** For any $U_p \in SU(N)$ ($U_p^\dagger U_p = I_N$),
  $$\left\|U_p - I_N\right\|_{\mathrm{HS}}^2 = \operatorname{Tr}\!\left((U_p^\dagger - I_N)(U_p - I_N)\right) = \operatorname{Tr}(2I_N - U_p - U_p^\dagger) = 2N\left(1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p)\right),$$
  so $\left\langle \|U_p - I_N\|_{\mathrm{HS}}^2 \right\rangle_{\mu_0} = 2N \, e_p(\beta, \Lambda_0)$.
- **Cauchy–Schwarz on $L^2(\Omega_0, \mu_0)$:** Since $P_{j,\nu,\sigma}^{(k)}[U]$ is conjugate in $SU(N)$ to $U_{p_j}$ or $U_{p_j}^\dagger$, unitary invariance of $\|\cdot\|_{\mathrm{op}}$ and $\|\cdot\|_{\mathrm{HS}}$ together with $\|A\|_{\mathrm{op}} \le \|A\|_{\mathrm{HS}}$ and Cauchy–Schwarz yield:
  $$\left\langle \left\|P_{1,\nu,\sigma}^{(k)} - I_N\right\|_{\mathrm{op}} \left\|P_{2,\nu,\sigma}^{(k)} - I_N\right\|_{\mathrm{HS}} \right\rangle_{\mu_0} \le \sqrt{(2N e_{p_1})(2N e_{p_2})} = 2N\sqrt{e_{p_1} e_{p_2}}.$$

### Item 2: All Numerical Constants — **VERIFIED**
- **Per-Channel Constant:** Multiplying $2N\sqrt{e_{p_1} e_{p_2}}$ by the outer factor $\frac{1}{\sqrt{N}}$ yields $\frac{1}{\sqrt{N}}(2N\sqrt{e_{p_1} e_{p_2}}) = 2\sqrt{N}\sqrt{e_{p_1} e_{p_2}}$ per channel, confirming the inhomogeneous bound `YM-011-PLAQUETTE-EXP-T1(1)`.
- **Isotropic Periodic Torus Constant $C(d, N)$:** Summing over the $2(d-1)$ transverse channels $(\nu \ne \mu_k, \sigma \in \{+,-\})$ per coarse edge gives $C(d, N) = 2(d-1)\cdot 2\sqrt{N} = 4(d-1)\sqrt{N}$, which evaluates to $C(4, N) = 12\sqrt{N}$ in $d=4$ ($12\sqrt{3}$ for $SU(3)$, $12\sqrt{2}$ for universal $SU(2)$).
- **Sharp $SU(2)$ Constant $C_{\mathrm{sharp}}(d, 2)$:** Every $U_p \in SU(2)$ has conjugate eigenvalues $e^{\pm i\theta}$, so $U_p - I_2$ has equal singular values $s_1 = s_2 = 2\sin(\theta/2)$, yielding the exact identity $\|U_p - I_2\|_{\mathrm{op}} \equiv \frac{1}{\sqrt{2}}\|U_p - I_2\|_{\mathrm{HS}}$. Multiplying $C(d, 2) = 4(d-1)\sqrt{2}$ by $\frac{1}{\sqrt{2}}$ gives $C_{\mathrm{sharp}}(d, 2) = 4(d-1)$ ($= 12$ in $d=4$).

### Item 3: Plaquette Translation Invariance & Hyperoctahedral Axis Symmetry — **VERIFIED**
- **Periodic Translations $(\mathbb{Z}/2L\mathbb{Z})^d$:** For each coarse edge $e_k$ in direction $\hat{\mu}_k$, the adjacent plaquettes $p_1(k, \nu, \sigma)$ and $p_2(k, \nu, \sigma)$ lie in the same $(\mu_k, \nu)$-plane and satisfy $p_2 = \tau_{a\hat{\mu}_k}(p_1)$. Because $\tau_z^*$ preserves both $d\mu_{\mathrm{Haar},0}$ and $S_W(U)$, $e_{p_1(k,\nu,\sigma)} = e_{p_2(k,\nu,\sigma)} = e_{\mu_k \nu}(\beta, \Lambda_0)$ holds even on an anisotropic torus (`YM-011-PLAQUETTE-EXP-T1(2)`).
- **Hyperoctahedral Coordinate Permutations $S_d$:** On the isotropic torus $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$, coordinate permutations $\pi \in S_d$ act transitively on the $\binom{d}{2}$ unordered planes $\{\mu, \nu\} \subset \{1, \dots, d\}$ while preserving $d\mu_{\mathrm{Haar},0}$ and $S_W(U)$ (since orientation reversal sends $U_p \mapsto U_p^\dagger$, leaving $\operatorname{Re}\operatorname{Tr}(U_p)$ invariant), proving $e_{\mu\nu}(\beta, \Lambda_0) \equiv e_{\mathrm{plaq}}(\beta, \Lambda_0)$ (`YM-011-PLAQUETTE-EXP-T1(3)`).

### Item 4: Partition-Function Derivative Normalization (`YM-011-PLAQUETTE-EXP-T2`) — **VERIFIED**
- With $H(U) := S_W(U)/\beta = \sum_{p \in P_+(\Lambda_0)} (1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p))$ and $Z_{\Lambda_0}(\beta) = \int_{\Omega_0} e^{-\beta H(U)} d\mu_{\mathrm{Haar},0}(U)$, differentiation under the compact Haar integral yields:
  $$-\frac{\partial}{\partial \beta} \ln Z_{\Lambda_0}(\beta) = \langle H \rangle_{\mu_0} = |P_+(\Lambda_0)| \, e_{\mathrm{plaq}}(\beta, \Lambda_0) \implies e_{\mathrm{plaq}}(\beta, \Lambda_0) = -\frac{1}{\binom{d}{2}(2L)^d}\frac{\partial}{\partial \beta} \ln Z_{\Lambda_0}(\beta),$$
  together with $-\partial_\beta e_{\mathrm{plaq}}(\beta, \Lambda_0) = \operatorname{Var}_{\mu_0}(H)/|P_+(\Lambda_0)| \ge 0$ and the exact Lie-Laplacian integration-by-parts positivity $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \rangle_{\mu_0} \ge 0 \implies e_{\mathrm{plaq}}(\beta, \Lambda_0) \in [0, 1]$.

### Item 5: Claimed Weak-Coupling Rate & Strict Separation of Claims A, B, C — **VERIFIED**
- Pure $O(1/\beta)$ (`Claim A` / `Claim B`) is **not** claimed as proved on the periodic torus; `O_1_OVER_BETA_STATUS` is explicitly marked `WITHHELD_AS_UNRESOLVED_DEPENDENCY`.
- `Claims A, B, C` are strictly separated in Section 4.1 with explicit non-implication guards $\text{A} \not\implies \text{B}$ and $\text{B} \not\implies \text{C}$.
- The elementary entropy–energy bound `YM-011-PLAQUETTE-EXP-L1` rigorously proves:
  $$e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \inf_{r \in (0, \pi]} \left( 8r^2 + \frac{2}{(d-1)\beta} \ln\!\left(\frac{1}{v_N(r)}\right) \right) = O\!\left(\frac{\ln \beta}{\beta}\right)$$
  for all $\beta > 0$ and all $L \ge 1$ using monotonicity of $\langle H \rangle_{\mu_s}$ and the 4-link plaquette estimate $\|U_p - I_N\|_{\mathrm{op}} \le 4r \implies 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \le \frac{1}{2}\|U_p - I_N\|_{\mathrm{op}}^2 \le 8r^2$ on the product Lie-algebra ball $\mathcal{U}_r$.

### Item 6: Dependence on Volume — **VERIFIED**
- On $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$, the link-to-plaquette ratio
  $$\frac{|E_+(\Lambda_0)|}{|P_+(\Lambda_0)|} = \frac{d(2L)^d}{\binom{d}{2}(2L)^d} = \frac{2}{d - 1}$$
  cancels $(2L)^d$ identically in `YM-011-PLAQUETTE-EXP-L1`, and no hidden volume-dependent constants appear in `YM-011-PLAQUETTE-EXP-T1`.

### Item 7: Gauge-Zero-Mode & Flat-Connection Toron Singular-Strata Treatment (`NEG-YM-011-PLAQ-1`) — **VERIFIED**
- On the periodic torus $\mathbb{T}^d$, the flat-connection moduli space $\{H(U) = 0\}/\mathcal{G}_0 = \mathcal{M}_{\mathrm{flat}}(\Lambda_0, SU(N)) \cong T^d / S_N$ has dimension $d(N-1)$.
- At regular irreducible torons $U_{\mathrm{reg}}$, $\dim \operatorname{Stab}_{\mathcal{G}_0}(U_{\mathrm{reg}}) = N-1$, giving gauge orbit dimension $(N^2-1)(2L)^d - (N-1)$ and total Hessian kernel dimension $(N^2-1)(2L)^d + (d-1)(N-1)$.
- At singular central torons $U_{\mathrm{sing}} \in Z(SU(N))^d$, $\dim \operatorname{Stab}_{\mathcal{G}_0}(U_{\mathrm{sing}}) = N^2-1$, so the gauge orbit dimension drops by $N(N-1)$ while $\dim \ker \nabla^2 H(U_{\mathrm{sing}}) = (N^2-1)(2L)^d + (d-1)(N^2-1)$ jumps upward by $(d-1)N(N-1)$ quartic zero modes ($H \sim \operatorname{Tr}(-[A_\mu, A_\nu]^2) \sim \|A\|^4$), obstructing naive un-gauge-fixed Laplace or smooth Morse–Bott stationary-phase asymptotics (`NEG-YM-011-PLAQ-1`).

### Item 8: Absence of Silent Continuum-Limit Assumptions & Preservation of Project Invariants — **VERIFIED**
- `NUMERICAL_DIAGNOSTIC_ONLY` labeling is strictly enforced in both `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md` and `src/ymmg/plaquette_expectation.py`.
- All project governance invariants are explicitly preserved:
  - `GOAL_COMPLETE = FALSE` (`CLAY_PROBLEM = OPEN_AND_UNSOLVED`)
  - `YM-006` through `YM-010 = SCIENTIFIC_REVIEW_HOLD`
  - Original `YM-011` continuum proposal `NOT AUTHORIZED` (`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`)

---

## 2. Final Audit Verdict

`INTEGRITY_PASS`
