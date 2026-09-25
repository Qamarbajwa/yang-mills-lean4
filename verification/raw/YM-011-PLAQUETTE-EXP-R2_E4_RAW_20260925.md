# INDEPENDENT ADVERSARIAL MATHEMATICAL & GOVERNANCE AUDIT REPORT

- **AUDIT TARGET:** Task `YM-011-PLAQUETTE-EXP-R2` (Group-Specific Plaquette-Energy Range, Proof of Odd-$N$ Minimizer, and Expectation-Positivity Audit)
- **AUDITOR IDENTITY:** Autonomous Fresh Blind Adversarial Research Subagent (`adversarial-blind-audit-subagent`)
- **WORKSPACE ROOT:** `d:\Comfy UI\yang mills and the mass gap`
- **CANDIDATE COMMIT SHA:** `9ed117fe58a39540134fb2fb2bac3691d747b884`
- **SCIENTIFIC TREE HASH:** `18c319312f7afcd3fc4e93afa898de78b5c88500c4eee1fa04bdd08b2c08b77d` (Verified via `compute_closed_world_scientific_tree_hash`)
- **REPOSITORY TEST STATUS:** `318 passed in 2.89s` (100% passing across the entire repository)
- **FINAL VERDICT:** **`INTEGRITY_PASS`**

---

## 1. Executive Summary & Verification Scope

An independent, fresh, blind, adversarial mathematical and governance audit was conducted for candidate commit `9ed117fe58a39540134fb2fb2bac3691d747b884` on Task `YM-011-PLAQUETTE-EXP-R2`.

The audit inspected the five core files on disk:
1. `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md`
2. `src/ymmg/plaquette_expectation.py`
3. `tests/test_ym_011_plaquette_exp.py`
4. `NEGATIVE_EVIDENCE_REGISTER.md`
5. `governance/PROJECT_STATE.yaml`

All eight audit criteria were rigorously scrutinized against primary mathematical principles, spectral group theory, differential geometry on Lie groups, statistical mechanics, and repository governance protocols.

---

## 2. Detailed Findings Against the Eight Audit Criteria

### Criterion 1: Plaquette-Energy Range & Complete Proof of Odd-$N$ Constrained Minimizer
- **Status:** **VERIFIED (MATHEMATICALLY COMPLETE & RIGOROUS)**
- **Citation:** `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md` (Sec. 1.2–1.3, lines 29–77); `src/ymmg/plaquette_expectation.py` (lines 46–65); `tests/test_ym_011_plaquette_exp.py` (lines 54–116).
- **Mathematical Audit:**
  - Let $h_p(U) = 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) = \frac{1}{2N}\|U_p - I_N\|_{\mathrm{HS}}^2$ for $U_p \in SU(N)$.
  - **Even $N$ ($N = 2, 4, \dots$):** $\det(-I_N) = (-1)^N = +1 \implies -I_N \in SU(N)$. At $U_p = -I_N$, all eigenvalues are $-1 = e^{i\pi}$, yielding $\sum \theta_j = N\pi \equiv 0 \pmod{2\pi}$ and $q_N(-I_N) = -1.0$. Thus $h_{\max}(N) = 1 - (-1) = 2.0$. Exact values verified: $SU(2) = 2.0$ (attained at $-I_2$), $SU(4) = 2.0$ (attained at $-I_4$).
  - **Odd $N$ ($N = 3, 5, \dots$):** $\det(-I_N) = (-1)^N = -1 \ne 1 \implies -I_N \notin SU(N)$.
    To minimize $q_N(U) = \frac{1}{N}\sum_{j=1}^N \cos\theta_j$ under $\sum_{j=1}^N \theta_j \equiv 0 \pmod{2\pi}$, perform the coordinate shift around $\pi$: $\theta_j = \pi - \phi_j$, giving $\cos\theta_j = -\cos\phi_j$.
    Minimizing $\sum \cos\theta_j$ is equivalent to maximizing $g(\phi) = \sum_{j=1}^N \cos\phi_j$ under $\sum_{j=1}^N \phi_j \equiv \pi \pmod{2\pi}$.
    1. *Concavity & Jensen's Inequality:* On $[-\pi/2, \pi/2]$, $\frac{d^2}{d\phi^2}\cos\phi = -\cos\phi < 0$ (strictly concave). For $\phi_j \in [-\pi/2, \pi/2]$ with $\sum \phi_j = \pi$, Jensen's inequality guarantees $\frac{1}{N}\sum \cos\phi_j \le \cos(\frac{1}{N}\sum \phi_j) = \cos(\pi/N)$, with unique equality at $\phi_1 = \dots = \phi_N = \pi/N$.
    2. *Exclusion of Outer Angles:* If any $|\phi_k| > \pi/2$, $\cos\phi_k < 0$. Compensating angles strictly reduce $\sum \cos\phi_j$ below $N\cos(\pi/N)$.
    3. *Admissibility in $SU(N)$:* At $\phi_j = \pi/N$, original angles are $\theta_j = \pi - \pi/N = \frac{(N-1)\pi}{N}$. The determinant of $U = \operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_N})$ is $\prod_{j=1}^N e^{i(N-1)\pi/N} = e^{i(N-1)\pi} = (-1)^{N-1} = +1$ because $N$ is odd, making $N-1$ an even integer. Hence $U = e^{i\pi(N-1)/N} I_N \in SU(N)$ is fully admissible, attaining the exact minimum $q_N^{\min} = -\cos(\pi/N)$.
    4. *Resulting Group Bounds:* $h_{\max}(N) = 1 + \cos(\pi/N) < 2.0$.
  - **Exact Evaluated Values:**
    - $SU(2): h_{\max} = 2.0$
    - $SU(3): h_{\max} = 1 + \cos(\pi/3) = 1 + 0.5 = 1.5$
    - $SU(4): h_{\max} = 2.0$
    - $SU(5): h_{\max} = 1 + \cos(\pi/5) = 1 + \frac{1+\sqrt{5}}{4} \approx 1.809017$
  - Implemented cleanly in `su_n_plaquette_energy_range(n)` and tested against numerical Lie group elements in `test_1b_extremal_group_configurations_and_exact_range`.

---

### Criterion 2: Expectation Range vs. Configuration Range (Three-Range Separation)
- **Status:** **VERIFIED (STRICT ARCHITECTURAL SEPARATION ENFORCED)**
- **Citation:** `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md` (Sec. 1.4, lines 78–95; Sec. 3, lines 141–145); `src/ymmg/plaquette_expectation.py` (lines 67–91, 123–154); `tests/test_ym_011_plaquette_exp.py` (lines 145–248).
- **Audit Details:**
  The repository strictly delineates three distinct ranges:
  1. `CONFIGURATION_RANGE(N) = [0, h_max(N)]` with $h_{\max} \in (0, 2]$.
  2. `EXPECTATION_RANGE(N) = [0, h_max(N)]`: For any probability measure $\mu$, convexity of the integral gives $\langle h_p \rangle_\mu \in [\inf h_p, \sup h_p] = [0, h_{\max}(N)]$. Specifically, $e_{\mathrm{plaq}} = 2.0$ is recognized and demonstrated to be strictly impossible on $SU(3)$ gauge configurations under any probability measure.
  3. `UNIVERSAL_ALL_N_RANGE = [0, 2]`: Coarse universal bound across all $N \ge 2$.
  In `src/ymmg/plaquette_expectation.py`:
  - `validate_group_plaquette_energy(mean_plaquette_energy, su_n)` strictly checks $e_{\mathrm{plaq}} \in [0, h_{\max}(SU(N))]$.
  - `compute_unconditional_tangent_expectation_bound` defaults to `enforce_group_admissibility=True`.
  - In `tests/test_ym_011_plaquette_exp.py`, `test_2b_range_boundary_validation` asserts that $e_{\mathrm{plaq}} = 2.0$ and $e_{\mathrm{plaq}} = 1.5001$ for $SU(3)$ raise `ValueError` matching `outside sharp SU(3) range`, while allowing $e_{\mathrm{plaq}} = 2.0$ only when `enforce_group_admissibility=False`.

---

### Criterion 3: Lie-Laplacian Positivity Derivation & Epistemic Classification
- **Status:** **VERIFIED (DERIVATION ACCURATE, TAXONOMY SOUND, FULLY DECOUPLED)**
- **Citation:** `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md` (Sec. 3.1, lines 146–177); `NEGATIVE_EVIDENCE_REGISTER.md` (lines 108–109); `tests/test_ym_011_plaquette_exp.py` (lines 230–248).
- **Mathematical Audit:**
  - **First-Principles Derivation:**
    Using left-invariant derivatives $\partial_\ell^a$ on $SU(N)$ with trace metric $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$ and Casimir $\sum_a T^a T^a = -C_2(F)I_N = -\frac{N^2-1}{2N}I_N$, integration by parts on $SU(N)^{E_+}$ without boundary yields:
    $$\int_{\Omega_0} d\mu_{\mathrm{Haar},0} \sum_a \partial_\ell^a \left( (\partial_\ell^a S_W) e^{-S_W} \right) = 0 \implies \langle \Delta_\ell S_W \rangle_{\mu_\beta} = \sum_{a=1}^{N^2-1} \langle (\partial_\ell^a S_W)^2 \rangle_{\mu_\beta} \ge 0.$$
    Evaluating $\Delta_\ell S_W = \frac{\beta(N^2-1)}{2N^2}\sum_{p \ni \ell} \operatorname{Re}\operatorname{Tr}(U_p)$ yields:
    $$\sum_{p \ni \ell} \langle \operatorname{Re}\operatorname{Tr}(U_p) \rangle_{\mu_\beta} = \frac{2N^2}{\beta(N^2-1)} \sum_{a=1}^{N^2-1} \langle (\partial_\ell^a S_W)^2 \rangle_{\mu_\beta} \ge 0.$$
  - **Epistemic Classification:**
    - Summed plaquettes touching link $\ell$: Classified as `PROVED_FOR_WILSON_GIBBS_MEASURE`.
    - Individual plaquettes: Classified as `PROVED_ONLY_AFTER_ADDITIONAL_SYMMETRY` (requires hyperoctahedral reflections/permutations equating all $2(d-1)$ plaquettes sharing $\ell$).
    - Configuration-wise upper bound: Classified as `FALSE` (since $h_p(U)$ can reach $2.0$ for even $N$ and $1.5$ for $SU(3)$).
  - **Decoupling from Theorems:**
    Decoupled from Theorems $T1, T2$ and Lemma $L1$. In particular, under the bare Wilson measure, $e_{\mathrm{plaq}}(\beta) \le 1.0$ follows directly from Haar character orthogonality $\langle \operatorname{Tr} U_p \rangle_{\beta=0} = 0 \implies e_{\mathrm{plaq}}(0) = 1.0$ together with monotonicity $\partial_\beta e_{\mathrm{plaq}} = -\operatorname{Var}(H)/|P_+| \le 0$ for all $\beta \ge 0$, completely independent of the Lie-Laplacian identity.

---

### Criterion 4: Invariance of Theorem `YM-011-PLAQUETTE-EXP-T1`
- **Status:** **VERIFIED (MATHEMATICALLY SOUND & FULLY INVARIANT)**
- **Citation:** `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md` (Sec. 2.1–2.2, lines 100–123); `src/ymmg/plaquette_expectation.py` (lines 123–177); `tests/test_ym_011_plaquette_exp.py` (lines 118–143).
- **Audit Details:**
  Theorem $T1$ reduces $\langle |\Delta_{\mathrm{tan}}(C_1)| \rangle_{\mu_0} \le C(d, N) |C_1|_{\Lambda_1} e_{\mathrm{plaq}}(\beta, \Lambda_0)$ using:
  1. The exact algebraic identity $\|U_p - I_N\|_{\mathrm{HS}}^2 = 2N h_p(U)$.
  2. Cauchy–Schwarz on $L^2(\Omega_0, \mu_0)$: $\langle \|P_1 - I_N\|_{\mathrm{op}} \|P_2 - I_N\|_{\mathrm{HS}} \rangle \le 2N \sqrt{e_{p_1} e_{p_2}}$.
  3. Pre-factor $\frac{1}{\sqrt{N}}$ yielding $2\sqrt{N}\sqrt{e_{p_1}e_{p_2}}$ per channel.
  4. Hyperoctahedral transitive action equating all $2(d-1)$ channels per coarse edge, resulting in $C(d, N) = 4(d-1)\sqrt{N}$ ($12\sqrt{N}$ in $d=4$).
  5. For $SU(2)$, the exact spectral identity $\|U_p - I_2\|_{\mathrm{op}} \equiv \frac{1}{\sqrt{2}}\|U_p - I_2\|_{\mathrm{HS}}$ yields $C_{\mathrm{sharp}}(d, 2) = 4(d-1) = 12$ in $d=4$.
  Because Cauchy–Schwarz and the norm identity hold identically across all $L^2$ random variables regardless of numerical upper bounds, Theorem $T1$ remains completely invariant and valid for any $e_p \in [0, h_{\max}(N)] \subseteq [0, 2]$.

---

### Criterion 5: Thermodynamic Derivative `YM-011-PLAQUETTE-EXP-T2` & Entropy–Energy Bound `L1`
- **Status:** **VERIFIED (EXACT IDENTITIES & VOLUME-INDEPENDENT BOUND RIGOROUS)**
- **Citation:** `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md` (Sec. 3, lines 126–145; Sec. 4.3, lines 209–224); `src/ymmg/plaquette_expectation.py` (lines 200–289); `tests/test_ym_011_plaquette_exp.py` (lines 249–268).
- **Audit Details:**
  - Dimensionless Hamiltonian $H(U) = \sum_{p \in P_+} (1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr} U_p) = S_W(U)/\beta$.
  - First derivative: $-\partial_\beta \ln Z_{\Lambda_0}(\beta) = \langle H \rangle_{\mu_0} = |P_+| e_{\mathrm{plaq}}(\beta, \Lambda_0)$.
  - Second derivative / Monotonicity: $-\partial_\beta e_{\mathrm{plaq}}(\beta, \Lambda_0) = \frac{\operatorname{Var}_{\mu_0}(H)}{|P_+|} \ge 0$.
  - Lemma $L1$:
    - $\beta |P_+| e_{\mathrm{plaq}}(\beta) \le \int_0^\beta \langle H \rangle_{\mu_s} ds = -\ln Z_{\Lambda_0}(\beta)$.
    - Lower bounding $Z$ on the link-ball product $\mathcal{U}_r$ yields $Z \ge e^{-8\beta r^2 |P_+|} (v_N(r))^{|E_+|}$.
    - Exact volume-independent link-to-plaquette ratio on periodic $\mathbb{T}^d$: $\frac{|E_+(\Lambda_0)|}{|P_+(\Lambda_0)|} = \frac{d(2L)^d}{\binom{d}{2}(2L)^d} = \frac{2}{d-1}$.
    - Dividing gives $e_{\mathrm{plaq}}(\beta) \le \inf_{r \in (0, \pi]} (8r^2 + \frac{2}{(d-1)\beta}\ln(1/v_N(r))) = O(\frac{\ln\beta}{\beta})$ uniformly in lattice size $L$.

---

### Criterion 6: Separation of Claims A, B, C & Toron Singular Strata (`NEG-YM-011-PLAQ-1`)
- **Status:** **VERIFIED (OBSTRUCTION FULLY DOCUMENTED & PROPERLY WITHHELD)**
- **Citation:** `literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md` (Sec. 4.1–4.2, lines 181–208; Sec. 6.3, lines 262–269); `NEGATIVE_EVIDENCE_REGISTER.md` (lines 88–94).
- **Audit Details:**
  - Claims A (fixed finite-lattice asymptotic), B (volume-uniform weak-coupling bound), and C (thermodynamic multiscale estimate) are strictly separated with explicit non-implication $\text{A} \not\implies \text{B} \not\implies \text{C}$.
  - The failure of naive Laplace / Morse–Bott asymptotics on the periodic torus is rigorously analyzed:
    - $\mathcal{M}_{\mathrm{flat}}(\mathbb{T}^d, SU(N)) \cong T^d / S_N$ has jumping stabilizer dimension (dimension $N-1$ at regular torons jumping to $N^2-1$ at singular central torons $U \in Z(SU(N))^d$).
    - At singular central torons, $(d-1)N(N-1)$ quadratic zero modes emerge where the leading action is quartic ($\operatorname{Tr}([A_\mu, A_\nu]^2) \sim \|A\|^4$, scaling as $\beta^{-1/4}$ rather than Gaussian $\beta^{-1/2}$).
  - Pure $O(1/\beta)$ is properly withheld as an unresolved dependency, deferring to `YM-011-TREE-GAUGE`.

---

### Criterion 7: Negative Evidence Register & Operational Disclosure Integrity
- **Status:** **VERIFIED (ALL THREE DISCLOSURES REGISTERED WITH HIGH INTEGRITY)**
- **Citation:** `NEGATIVE_EVIDENCE_REGISTER.md` (lines 88–114).
- **Audit Details:**
  - `NEG-YM-011-PLAQ-1`: Failure of ordinary and smooth Morse–Bott Laplace asymptotics on the periodic torus due to flat-connection / toron singular strata (`[EXACT_GEOMETRIC_DEGENERACY_OBSTRUCTION]`).
  - `NEG-YM-011-PLAQ-2`: False configuration-wise plaquette energy range $[0, 1]$ and root-cause disclosure of independent review miss in R0 (`[EXACT_MATHEMATICAL_COUNTEREXAMPLE_AND_GOVERNANCE_AUDIT]`).
  - `NEG-YM-011-PLAQ-3`: Group-specific plaquette admissibility inconsistency and verification separation (`[INTERNAL_SPECIFICATION_INCONSISTENCY_AND_VERIFICATION_REPAIR]`), disclosing the R1 QA test inconsistency (evaluating $e_{\mathrm{plaq}} = 2.0$ for $SU(3)$) and resolving it via 3-range separation and group validators.

---

### Criterion 8: Code Implementation, Regression Tests, and Governance Gates
- **Status:** **VERIFIED (ALL TESTS PASSING, ALL GATES SECURE)**
- **Citation:** `governance/PROJECT_STATE.yaml` (lines 6–7, 106–150, 188–215); `src/ymmg/plaquette_expectation.py`; `tests/test_ym_011_plaquette_exp.py`.
- **Audit Details:**
  - Code implementation provides `validate_group_plaquette_energy`, `validate_universal_plaquette_energy`, and default `enforce_group_admissibility=True`.
  - Tests verify $SU(2)$, $SU(3)$, $SU(5)$, strict rejection of $e_{\mathrm{plaq}} = 2.0$ and $1.5001$ for $SU(3)$ under group validator, and allowance under universal validator.
  - Test suite execution: `python -m pytest` executes and passes all 318 repository tests (`318 passed in 2.89s`).
  - Governance checks in `PROJECT_STATE.yaml`:
    - `goal_complete: false`
    - `clay_problem: OPEN_AND_UNSOLVED`
    - `YM-006` through `YM-010`: `SCIENTIFIC_REVIEW_HOLD`
    - `YM-011-TREE-GAUGE`: `BLOCKED_PENDING_R2_CLOSEOUT` (not prematurely started)
    - `YM-011`: `PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`
    - Candidate SHA and Evidence Closeout HEAD properly decoupled.

---

## 3. Remaining Limitations

1. **Volume-Uniform Logarithmic Factor ($O(\ln\beta/\beta)$ vs. Pure $O(1/\beta)$):**
   Lemma $L1$ establishes an unconditional volume-uniform upper bound $O(\frac{\ln\beta}{\beta})$. The elimination of the $\ln\beta$ factor on the periodic torus requires gauge-fixing and singular toron moduli analysis, which is correctly identified and delegated to `YM-011-TREE-GAUGE`.
2. **Single-Plaquette Lie-Laplacian Positivity Under Asymmetry:**
   The Lie-Laplacian integration-by-parts identity unconditionally proves $\sum_{p \ni \ell} \langle \operatorname{Re}\operatorname{Tr} U_p \rangle \ge 0$ under the bare Wilson Gibbs measure. Reduction to single-plaquette expectation $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr} U_p \rangle \ge 0 \iff e_p \le 1.0$ requires hyperoctahedral symmetry equating the $2(d-1)$ plaquettes sharing link $\ell$. On asymmetric or boundary-distorted lattices, this does not hold for individual plaquettes; however, Theorems $T1, T2, L1$ do not require $e_p \le 1.0$ and remain completely valid for all $e_p \in [0, h_{\max}(N)]$.
3. **Diagnostic Nature of Single-Plaquette Numerical Routine:**
   The single-plaquette Bessel character evaluation in `su2_single_plaquette_thermodynamic_identity_diagnostic` is strictly labeled `NUMERICAL_DIAGNOSTIC_ONLY` and is not part of any formal proof.

None of these limitations represent mathematical flaws or integrity violations; all are properly characterized, documented, and bounded.

---

## 4. Final Verdict

- **FINAL AUDIT VERDICT:** **`INTEGRITY_PASS`**
- **CLOSING SUMMARY:** Candidate SHA `9ed117fe58a39540134fb2fb2bac3691d747b884` (Scientific Tree Hash: `18c319312f7afcd3fc4e93afa898de78b5c88500c4eee1fa04bdd08b2c08b77d`) fully and rigorously satisfies all eight mathematical, verification, and governance criteria. Task `YM-011-PLAQUETTE-EXP-R2` is cleared for provenance recording and closeout.
