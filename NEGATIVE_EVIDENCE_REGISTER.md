# NEGATIVE EVIDENCE REGISTER

## Registered Negative Findings and Operational Disclosures

### NEG-001: Packaging and editable install failure during YM-000 bootstrap
- **Discovery Date:** 2026-08-24
- **Finding:** Editable installation (`pip install -e .`) failed in isolated environments without build tools.
- **Resolution:** Removed unnecessary editable-install dependency, switching to clean PYTHONPATH-based test execution.

### NEG-002: YM-001 Negative Disclosure and Inaccessible / Partial Definitions
- **Discovery Date:** 2026-08-24
- **Items Not Present or Partially Defined in Official Source:**
  1. *Operational Definition of "Non-trivial":* The official text uses the phrase "non-trivial quantum Yang–Mills theory" without providing a single closed algebraic equation. Marked `PARTIAL_SOURCE_DEFINITION` / `REQUIRES_FOLLOWUP`.
  2. *Full Reconstruction of OS / Wightman Axioms:* Detailed line-by-line reconstruction of the full Osterwalder–Schrader ([35]) and Wightman ([45]) axiom sets is bounded into follow-up tasks (YM-001A / YM-001B).
  3. *Unresolved Differences in Non-Gauge-Invariant Observables:* The Euclidean OS reconstruction specifically addresses gauge-invariant local observables; full gauge-dependent operator reconstruction is noted as mathematically open in the literature.

### NEG-003: Foundational Literature Scope Boundaries (1954–1980)
- **Discovery Date:** 2026-08-24
- **Scope Boundaries Established:**
  1. *Classical vs. Quantum:* The 1954 Yang–Mills classical equations (`THM-YM-0001`) describe massless waves; classical non-Abelian gauge invariance does not imply a quantum mass gap.
  2. *Perturbative Renormalizability vs. Non-Perturbative Existence:* 't Hooft's 1971 proof (`THM-YM-0003`) and 't Hooft–Veltman dimensional regularization (`THM-YM-0004`) establish order-by-order perturbative renormalizability, but the perturbation series is divergent (renormalons) and does not yield a non-perturbative measure.
  3. *UV Asymptotic Freedom vs. IR Mass Gap:* Asymptotic freedom (`THM-YM-0006`) provides logarithmic weak coupling at short distances, but leads to strong coupling in the infrared where perturbation theory fails to determine the mass spectrum.
  4. *Fixed-Lattice Strong-Coupling Confinement vs. Continuum Limit:* Wilson's 1974 lattice area law (`THM-YM-0008`) holds for $g^2 \gg 1$ at fixed $a > 0$, but the continuum limit requires $a \to 0$ ($g \to 0$), which cannot be reached via strong-coupling expansions alone.
  5. *Lower-Dimensional Monopole Gap vs. 4D Pure Yang–Mills:* Polyakov's 1977 mass gap result (`THM-YM-0011`) provides a semiclassical derivation in $2+1$ dimensions for compact $U(1)$ (elevated to a rigorous lattice theorem by Göpfert & Mack 1981 / Brydges et al. 1980), but cannot be transferred to $3+1$ dimensions where the 4D dilute instanton gas is infrared-divergent and uncontrolled (`THM-YM-0012`).
  6. *Reconstruction Machinery vs. Field Construction:* Osterwalder–Schrader reconstruction (`THM-YM-0005`) provides the necessary conditions to pass from Euclidean to Minkowski QFT (with OS II 1975 extending and correcting OS I 1973), but does not construct the 4D Yang–Mills measure.

### NEG-004: Gribov Ambiguity and Global Gauge Fixing Obstruction
- **Discovery Date:** 2026-08-24
- **Finding:** Faddeev–Popov gauge fixing (`THM-YM-0002`, 1967) relies on a local gauge condition $f(A)=0$. Gribov (1978, `PAPER-FOUND-014`) proved that for large field amplitudes, non-Abelian gauge orbits intersect the gauge condition multiple times (Gribov copies). Thus, Faddeev–Popov quantization is strictly a local perturbative tool and cannot be extended globally without resolving Gribov horizon boundaries.


### NEG-CONST-001: The 4D Infinite-Volume Infrared Boundary in Bałaban's RG Program
- **Discovery Date:** 2026-08-24
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[LATER_LITERATURE_LIMITATION]`
- **Finding:** Bałaban's multi-scale block-spin RG program achieves complete mathematical control over the ultraviolet limit ($a \to 0$) in any finite volume $V < \infty$, but was bounded at the finite-volume boundary. In 4D, as the RG scale descends toward the infrared ($V \to \infty$), asymptotic freedom causes the effective coupling to grow ($g_k \sim 1$), preventing small-field inductive bounds and large-field polymer expansions from controlling the thermodynamic infinite-volume limit without a separate non-perturbative infrared closure mechanism.

### NEG-CONST-002: Infrared Cutoff Removal Obstruction in Constructive $YM_4$
- **Discovery Date:** 2026-08-24
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[LATER_LITERATURE_LIMITATION]`
- **Finding:** Magnen, Rivasseau, and Sénéor (1993, *CMP* 155, 325) proved that 4D Euclidean Yang–Mills exists constructively in the presence of an artificial infrared cutoff $\Lambda_{IR} > 0$, explicitly stating that the removal of the infrared cutoff ($\Lambda_{IR} \to 0$) remains open. In constructive field theory literature, removing $\Lambda_{IR}$ without an established isolated vacuum and positive mass gap $\Delta > 0$ encounters infrared renormalon divergences and unbounded long-distance fluctuations.

### NEG-CONST-003: Dimensional and Non-Abelian Boundaries in Monopole Confinement
- **Discovery Date:** 2026-08-24
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** Göpfert & Mack (1981) rigorously proved confinement and mass gap for 3D $U(1)$ lattice gauge theory via monopole Coulomb gas duality. In 4D Euclidean spacetime, magnetic monopoles form 1D closed worldlines / current loops rather than 0D point events (with Dirac strings forming 2D Dirac sheets bounded by the loops), and the non-Abelian field self-interaction $[A_\mu, A_\nu]$ obstructs direct Hodge-star scalar duality. No direct mathematical extension from 3D Abelian duality to 4D non-Abelian Yang–Mills has been established, though no impossibility theorem rules out confinement via dual superconductor mechanisms.

### NEG-MOD-001: Dimensional Criticality Barrier in 4D Stochastic Yang–Mills Quantization
- **Discovery Date:** 2026-08-25
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** While Chandra et al. constructed 2D Yang–Mills invariant Langevin measure (2022) and 3D local-in-time flow (2024), 4D stochastic Yang–Mills is critically singular, meaning that local polynomial counterterms and regularity structures are insufficient to control UV fluctuations, leaving 4D stochastic quantization open.

### NEG-MOD-002: Infinite-Loop Truncation Barrier in Continuum Lattice Bootstrap
- **Discovery Date:** 2026-08-25
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** The Makeenko–Migdal loop equation bootstrap (Kazakov & Zheng 2023, 2024) provides rigorous upper and lower bounds on lattice observables at fixed lattice spacing $a > 0$ for large $N$ and finite $N$. However, taking the continuum limit $a \to 0$ requires loops of arbitrarily large perimeter ($L_{max} \to \infty$), causing truncated semidefinite bootstrap matrices to lose rigorous closure without independent non-perturbative continuum bounds.

### NEG-MOD-003: Non-Extendability of Lattice Strong-Coupling Mass Gap to Continuum Weak Coupling
- **Discovery Date:** 2026-08-25
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** Shen, Zhu, and Zhu (2022) proved an infinite-volume lattice mass gap $\Delta_{lat}(\beta) > 0$ via uniform Poincaré and log-Sobolev inequalities for $\beta < \beta_0$. However, taking the continuum limit $a \to 0$ requires the asymptotically free weak-coupling limit $\beta \to \infty$ ($g \to 0$), where strong-coupling functional inequalities and polymer convergence fail. Thus, a strong-coupling lattice mass gap does not establish the continuum Clay mass gap without a non-perturbative weak-coupling bridge.

### NEG-MOD-004: Triviality of the Massive Continuum Scaling Limit in Gauge-Higgs Systems
- **Discovery Date:** 2026-08-25
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** Chatterjee (2024) proved that 4D $SU(2)$ Yang–Mills–Higgs under joint parameter scaling produces a continuum field with a strictly positive mass gap $m > 0$. However, because the mass generation is driven by Higgs condensation, the resulting continuum field is a free Gaussian field (trivial $S$-matrix), which does not solve the interacting non-Abelian pure Yang–Mills problem.

### NEG-YM-002F-001: Recurrent Interface Is Not a No-Go Theorem
- **Discovery Date:** 2026-08-31
- **Epistemic Classification:** `[PROJECT_SYNTHESIS]` / `[UNKNOWN]`
- **Hypothesis tested:** Repeated failure of existing pathways at the UV-to-IR, limit, and spectral interfaces might prove that a common obstruction has been found.
- **Result:** Rejected as an impossibility claim. The evidence supports only recurring method limitations and Clay obligations. Lower-dimensional exact theories, strong-coupling lattice theorems, and OS reconstruction provide counterexamples to any blanket assertion that the interfaces are mathematically impossible.
- **Surviving insight:** The same interfaces are sufficiently recurrent and mathematically explicit to prioritize YM-003, especially joint `a→0`/`V→∞` control, gauge-invariant IR decay, and spectral-gap persistence.
- **Regression check:** `tests/test_cross_era_synthesis.py` requires controlled candidate states, preserves `UNKNOWN`, enforces `CLAY_SUFFICIENT = NO` for analogue rows, and rejects silent orphan remapping.

### NEG-YM-011-OBS-1: Singular Determinant Locus of Naive Linear Block-Spin Matrix Averaging (`YM-011-OBS-MAP`)
- **Discovery Date:** 2026-09-24
- **Epistemic Classification:** `[EXACT_FINITE_LATTICE_COUNTEREXAMPLE]`
- **Hypothesis tested:** Whether naive linear staple averaging $M_\alpha^{\mathrm{lin}}(e)[U] = (1-\alpha) U(\ell_{e,1}) U(\ell_{e,2}) + \frac{\alpha}{2(d-1)} \sum_{\gamma \in \Gamma_{\mathrm{staple}}(e)} H_0(\gamma)[U]$ followed by polar projection $\Pi_{SU(N)}(M) = M(M^\dagger M)^{-1/2}(\det(\cdots))^{-1/N}$ defines a globally smooth $SU(N)$-valued blocking map $\Omega_0 \to \Omega_1$.
- **Result:** Falsified on $\Omega_0$. For $G = SU(2)$, $\alpha = 1/2$, $U(\ell_{e,1}) U(\ell_{e,2}) = I_2 \in SU(2)$, and $H_0(\gamma)[U] = -I_2 \in SU(2)$, $M_{1/2}^{\mathrm{lin}}(e)[U] = 0_{2\times 2}$ has $\det M_{1/2}^{\mathrm{lin}} = 0$. Polar projection is undefined on the non-empty singular locus $\Sigma_\alpha \subset \Omega_0$.
- **Surviving resolution:** Resolved in `YM-011-OBS-MAP` by constructing the midpoint-exponential blocking map $\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) = U(\ell_{e,1}) \exp(\alpha X_{\mathrm{mid}}(e)[U]) U(\ell_{e,2}) \in SU(N)$, which is everywhere $C^\infty$ on $\Omega_0$ with zero singular locus, exact orientation reversal, and exact $\mathcal{G}_0 \to \mathcal{G}_1$ gauge equivariance.

### NEG-YM-011-OBS-2: Artificial Perimeter Attenuation in Finite-$\kappa$ Stochastic Markov Block-Spin Kernels (`YM-011-OBS-MAP`)
- **Discovery Date:** 2026-09-24
- **Epistemic Classification:** `[EXACT_REPRESENTATION_THEORETIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether a randomized Markov block-spin transition kernel $K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U)$ with finite concentration parameter $\kappa < \infty$ preserves Wilson loop expectations without multiplicative perimeter distortion.
- **Result:** Falsified for all $\kappa \in [0, \infty)$. By Schur's Lemma (`YM-011-OBS-T3`), $((K^{(\alpha,\kappa)}_{0\to 1})^* W_{\Lambda_1}(C_1))[U] = c_F(\kappa)^{|C_1|_{\Lambda_1}} ((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}(C_1))[U]$ where $c_F(\kappa) = \frac{d}{d\kappa}\ln z_N(\kappa) \in [0, 1)$, introducing an artificial perimeter-law decay factor $\exp(-\gamma(\kappa) L_{\mathrm{phys}}(C_1)/(2a))$ with $\gamma(\kappa) = -\ln c_F(\kappa) > 0$ purely from kernel noise. Only in the deterministic limit $\kappa \to \infty$ ($\mathcal{B}_\alpha^{\mathrm{mid}}$) does $c_F(\infty) = 1$ avoid artificial Markov perimeter attenuation.

### NEG-YM-011-PLAQ-1: Failure of Ordinary and Smooth Morse–Bott Laplace Asymptotics on the Periodic Torus Due to Flat-Connection / Toron Singular Strata (`YM-011-PLAQUETTE-EXP`)
- **Discovery Date:** 2026-09-25
- **Epistemic Classification:** `[EXACT_GEOMETRIC_DEGENERACY_OBSTRUCTION]`
- **Hypothesis tested:** Whether ordinary Laplace's method or smooth Morse–Bott stationary-phase asymptotics directly applies to $Z_{\Lambda_0}(\beta) = \int_{\Omega_0} e^{-\beta H(U)} d\mu_{\mathrm{Haar},0}(U)$ on the periodic torus $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ ($d \ge 2$) to prove a uniform $e_{\mathrm{plaq}}(\beta, \Lambda_0) = O(1/\beta)$ bound without gauge fixing or singular-strata analysis.
- **Result:** Falsified as a naive un-gauge-fixed proof method. The global minimum locus $\{H(U) = 0\} / \mathcal{G}_0 = \mathcal{M}_{\mathrm{flat}}(\Lambda_0, SU(N)) \cong T^d / S_N$ is a non-manifold orbifold whose gauge stabilizer $\operatorname{Stab}_{\mathcal{G}_0}(U)$ jumps from dimension $N - 1$ at regular irreducible torons to dimension $N^2 - 1$ at singular central torons ($U \in Z(SU(N))^d$), causing the kernel of $\nabla^2 H(U)$ to jump by $(d - 1)N(N - 1)$ quartic zero modes ($H \sim \operatorname{Tr}([A_\mu, A_\nu]^2) \sim \|A\|^4$).
- **Surviving resolution:** `YM-011-PLAQUETTE-EXP` establishes the unconditional reduction $\langle |\Delta_{\mathrm{tan}}(C_1)| \rangle_{\mu_0} \le 4(d-1)\sqrt{N} |C_1|_{\Lambda_1} e_{\mathrm{plaq}}(\beta, \Lambda_0)$ (`YM-011-PLAQUETTE-EXP-T1`) and the volume-uniform $O(\ln(\beta)/\beta)$ bound (`YM-011-PLAQUETTE-EXP-L1`), while withholding pure $O(1/\beta)$ as an unresolved dependency (`YM-011-TREE-GAUGE`).
- **Post-Tree-Gauge Re-Evaluation (`YM-011-TREE-GAUGE`):** Re-derived from first principles on the root-fixed maximal-tree gauge slice $\Sigma_{T_{\mathrm{per}}}$. While maximal-tree gauge fixing eliminates all $(L^d - 1)(N^2 - 1)$ local vertex gauge degrees of freedom with unit Haar Jacobian ($J_{\mathrm{tree}} = 1$), the remaining periodic zero-mode obstruction is proved to be **Category E (combination of all four structural mechanisms A, B, C, D)**:
  - **(A) Residual Global Conjugation:** Unfixed root gauge action $\mathcal{G}_{\mathrm{res}} = \operatorname{Ad}(SU(N))$ contributes $N(N - 1)$ orbit directions at generic torons;
  - **(B) Physical Flat-Connection Moduli:** The $d(N - 1)$-dimensional Cartan orbifold $\mathcal{M}_{\mathrm{flat}}(\Lambda_{\mathrm{per}}, SU(N)) \cong (T_{\mathrm{max}})^d / S_N$ ($T_{\mathrm{max}} \cong U(1)^{N-1}$) consists of gauge-inequivalent physical flat connections distinguished by noncontractible Polyakov loops;
  - **(C) Singular Stabilizer Structure:** $\operatorname{Stab}_{\operatorname{Ad}(SU(N))}(U)$ jumps from dimension $N - 1$ at regular torons to dimension $N^2 - 1$ ($\Delta \dim \operatorname{Stab} = N(N - 1)$) at the $N^d$ central torons $U_{\mathrm{cent}} \in Z(SU(N))^d$;
  - **(D) Quartic Commutator Directions:** At every central toron, the Hessian nullity in $\Sigma_{T_{\mathrm{per}}}$ jumps from $(d + N)(N - 1)$ to $d(N^2 - 1)$, releasing $(d - 1)N(N - 1)$ transverse off-diagonal modes with vanishing quadratic Hessian ($D^2 H = 0$) stabilized only at fourth order by $H_{\mathrm{quartic}}(X) = \frac{1}{2N}\sum_{\mu<\nu} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2$.

### NEG-YM-011-PLAQ-2: False Configuration-Wise Plaquette Energy Range $[0, 1]$ and Review Blind Spot (`YM-011-PLAQUETTE-EXP-R1`)
- **Discovery Date:** 2026-09-25
- **Epistemic Classification:** `[EXACT_MATHEMATICAL_COUNTEREXAMPLE_AND_GOVERNANCE_AUDIT]`
- **Hypothesis tested:** Whether the normalized plaquette defect $h_p(U) = 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p)$ and mean plaquette energy $e_{\mathrm{plaq}}(\beta, \Lambda_0)$ are bounded above by $1.0$ universally across $SU(N)$ ($N \ge 2$).
- **Result:** Falsified. For any even $N$, $-I_N \in SU(N)$ since $\det(-I_N) = (-1)^N = 1$. At $U_p = -I_N$, the normalized real trace is $q_N(-I_N) = -1.0$, which yields $h_p(-I_N) = 1.0 - (-1.0) = 2.0$. For example, in $SU(2)$, $U_p = -I_2 \in SU(2) \implies h_p(-I_2) = 2.0$ with $\|(-I_2) - I_2\|_{\mathrm{HS}}^2 = 8 = 2(2)(2.0)$. For odd $N$, $-I_N \notin SU(N)$, and the constrained minimum of $q_N(U)$ on $SU(N)$ is $-\cos(\pi/N) > -1$, giving $\max h_p = 1 + \cos(\pi/N) < 2$ (e.g. $1.5$ for $SU(3)$ at $U_p = e^{i 2\pi/3} I_3$). Thus the universally safe range is $h_p(U) \in [0, 2]$ and $e_{\mathrm{plaq}} \in [0, 2]$.
- **Root Cause of Independent Review Miss:** Subagent `7fa5a506-82bd-4978-820b-3106cc051995` verified symbolic algebra of Cauchy–Schwarz and the thermodynamic derivative but did not evaluate $h_p(U)$ at the extremal Lie group elements $U_p = -I_N$ or separate configuration-wise range from expectation properties under translation invariance.
- **Surviving resolution:** Repaired in `YM-011-PLAQUETTE-EXP-R1`: Theorem `T2` records the universally safe range $[0, 2]$ and group-theoretic bounds; Theorem `T1` ($C(d, N) = 4(d-1)\sqrt{N}$ and $C_{\mathrm{sharp}}(d, 2) = 4(d-1)$) was re-verified and proved strictly invariant (depending only on $\|U_p - I_N\|_{\mathrm{HS}}^2 = 2N h_p(U)$ and Cauchy–Schwarz); and `tests/test_ym_011_plaquette_exp.py` includes explicit regression tests on extremal group elements.

### NEG-YM-011-PLAQ-3: Group-Specific Plaquette Admissibility Inconsistency and Verification Separation (`YM-011-PLAQUETTE-EXP-R2`)
- **Discovery Date:** 2026-09-25
- **Epistemic Classification:** `[INTERNAL_SPECIFICATION_INCONSISTENCY_AND_VERIFICATION_REPAIR]`
- **Hypothesis tested:** Whether evaluating $e_{\mathrm{plaq}} = 2.0$ for $SU(3)$ in regression testing and test documentation is consistent with group-specific admissibility enforcement when $\max_{U \in SU(3)} h_p(U) = 1.5$.
- **Result:** Falsified as an internal inconsistency. While $h_p(U) \le 2.0$ holds universally across all $SU(N)$ ($N \ge 2$), for any fixed probability measure on $SU(3)$, $\langle h_p \rangle_\mu = \int h_p d\mu \le \sup_{U \in SU(3)} h_p(U) = 1.5$. An input expectation value of $e_{\mathrm{plaq}} = 2.0$ is physically and mathematically impossible for $SU(3)$. Testing universal $2.0$ on $SU(3)$ without distinguishing universal vs. group-specific validation created a specification conflict.
- **Lie-Laplacian Status Clarification:** The claim that Lie-Laplacian integration by parts implies $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr} U_p \rangle_{\mu_0} \ge 0 \implies e_{\mathrm{plaq}} \le 1.0$ was audited: it holds for the sum over plaquettes sharing a link $\sum_{p \ni \ell} \langle \operatorname{Re}\operatorname{Tr} U_p \rangle \ge 0$ under the bare Wilson Gibbs measure, and extends to single plaquettes only with hyperoctahedral transverse symmetry. It does NOT restrict configuration-wise $h_p(U)$ or non-symmetric states, nor is it required for $T1, T2, L1$ (since $e_{\mathrm{plaq}}(\beta) \le 1.0$ follows directly from Haar orthogonality $\langle \operatorname{Tr} U \rangle_{\beta=0} = 0$ and monotonicity $\partial_\beta e_{\mathrm{plaq}} \le 0$).
- **Surviving resolution:** Repaired in `YM-011-PLAQUETTE-EXP-R2`:
  1. Implemented strict 3-range separation: `CONFIGURATION_RANGE(N) = [0, h_max(N)]`, `EXPECTATION_RANGE(N) = [0, h_max(N)]`, and `UNIVERSAL_ALL_N_RANGE = [0, 2]`.
  2. Implemented `validate_group_plaquette_energy(mean_plaquette_energy, su_n)` enforcing $[0, h_{\max}(N)]$, and made it the default in `compute_unconditional_tangent_expectation_bound(..., enforce_group_admissibility=True)`.
  3. Added rigorous proof of the odd-$N$ constrained minimizer ($q_N^{\min} = -\cos(\pi/N)$) via Jensen's inequality on the concavity region of $\cos$.
  4. Decoupled candidate and closeout HEAD fields in `PROJECT_STATE.yaml`.

### NEG-YM-011-TREE-1: Failure of Unconstrained Co-Tree to Plaquette Bijection in $d \ge 3$ and on Periodic Tori (`YM-011-TREE-GAUGE`)
- **Discovery Date:** 2026-09-27
- **Epistemic Classification:** `[EXACT_COMBINATORIAL_AND_ALGEBRAIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether the tree-gauge co-tree link variables $\{\widetilde{U}_e\}_{e \in E_{\mathrm{co-tree}}}$ biject onto the set of all plaquette holonomies $\{U_p\}_{p \in P_+}$ in $d = 3$ and $d = 4$ (as they do on the $d = 2$ free-boundary lattice $\Lambda_{\mathrm{free}}(L, 2)$ where $|E_{\mathrm{co-tree}}| = |P_+| = (L - 1)^2$), thereby decoupling the $d \ge 3$ Wilson partition function into independent single-plaquette integrals.
- **Result:** Falsified for all $d \ge 3$ (both free and periodic boundaries) and for $d = 2$ periodic boundary:
  1. On $\Lambda_{\mathrm{free}}(L, 3)$, $|P_+| - |E_{\mathrm{co-tree}}| = 3L(L-1)^2 - (2L+1)(L-1)^2 = (L - 1)^3 = |C_3| > 0$.
  2. On $\Lambda_{\mathrm{free}}(L, 4)$, $|P_+| - |E_{\mathrm{co-tree}}| = 6L^2(L-1)^2 - (3L^2+2L+1)(L-1)^2 = 3L^4 - 8L^3 + 6L^2 - 1 = |C_3| - |C_4| > 0$.
  3. Around every 3-cube $c \in C_3$, the six base-point-transported boundary plaquette holonomies satisfy the exact non-Abelian Bianchi identity $\prod_{f=1}^6 \widehat{U}_{p_f(c)} = I_N$. Thus $|C_3| - |C_4|$ plaquettes are non-local non-Abelian products of the $|E_{\mathrm{co-tree}}|$ spanning plaquettes, preventing single-plaquette decoupling of $S_W$.
  4. Furthermore, on $\Lambda_{\mathrm{free}}(L, d)$, the smallest eigenvalue of the tree-gauge Hessian $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, d))$ degenerates to $0$ as $L \to \infty$ (e.g. $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, 2)) = 4\sin^2(\frac{\pi}{2(2L-1)}) \sim \frac{\pi^2}{4L^2}$), so finite-dimensional tree-gauge Laplace asymptotics proves **Claim A** (fixed finite volume $O(1/\beta)$ on $\Lambda_{\mathrm{free}}$) but does **not** establish **Claim B** (volume-uniform $O(1/\beta)$ in $d \ge 3$).

### NEG-YM-011-TORON-1: Failure of Global Brascamp–Lieb, Non-Self-Closure of Single-Plaquette Schwinger–Dyson, and Resolution of Fixed-Volume Periodic $O_L(1/\beta)$ (`YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB`)
- **Discovery Date:** 2026-09-28
- **Epistemic Classification:** `[EXACT_METHODOLOGICAL_BOUNDARY_AND_STRATIFIED_ASYMPTOTIC_RESOLUTION]`
- **Hypotheses tested:**
  1. Whether the quartic commutator functional $Q(X_1, \dots, X_d) = \sum_{\mu<\nu} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2$ satisfies a global coercive inequality $Q(X) \ge c\|X\|_{\mathrm{HS}}^4$ on $\mathfrak{su}(N)^d$;
  2. Whether global Brascamp–Lieb covariance bounds apply directly to the periodic Wilson Gibbs measure $\mu_{\mathrm{per}, \beta}$;
  3. Whether the single-plaquette link Schwinger–Dyson identity closes by itself to prove $\beta e_{\mathrm{plaq}} \le C(N, d)$;
  4. Whether toron flat moduli and central-toron quartic commutator zero modes obstruct fixed-volume periodic $O_L(1/\beta)$ (`P1`).
- **Results:**
  1. **Global Coercivity of $Q$ Falsified:** $Q(X) = 0 \iff [X_\mu, X_\nu] = 0 \;\forall \mu < \nu$. The zero locus $\mathcal{Z}(Q) = \mathfrak{C}_d(\mathfrak{su}(N))$ is a non-trivial real algebraic cone of dimension $(d + N)(N - 1)$ along which $\|X\|_{\mathrm{HS}}$ can be arbitrarily large while $Q(X) = 0$.
  2. **Global Brascamp–Lieb Falsified (`NOT_APPLICABLE`):** $V(A) = \beta H(\exp(A))$ is non-convex on the compact manifold $SU(N)^{|E_{\mathrm{co-tree}}|}$ and $\operatorname{Hess}(V)$ has vanishing eigenvalues on the flat moduli space $\mathcal{M}_{\mathrm{flat}}$ ($\sup \|(\operatorname{Hess} V)^{-1}\|_{\mathrm{op}} = +\infty$).
  3. **Schwinger–Dyson Self-Closure Falsified (`PARTIAL`):** The exact single-plaquette identity (`YM-011-TORON-SD1`) couples $\frac{N^2 - 1}{2N}\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr} U_{p_0} \rangle$ to $2d - 3$ neighboring 6-link domino loop mergers $\langle \operatorname{Re}\operatorname{Tr}(U_{p_0} U_p^\dagger) \rangle$ and 8-link figure-eight loops of indefinite sign.
  4. **Resolution of `NEG-YM-011-PLAQ-1` at Fixed Finite Volume $L$ (`P1 = PROVED`, `P2 = OPEN`):** While toron flat and quartic zero modes invalidate Gaussian Hessian inversion, each quartic mode ($\beta^{-1/4}$) contributes $\frac{1}{4\beta}$ and each flat mode ($\beta^0$) contributes $0$ to $-\partial_\beta \ln Z_{\mathrm{per}}(\beta)$ (strictly less than $\frac{1}{2\beta}$ for a quadratic mode), and any resonant $(\ln \beta)^{k_L}$ factor in $Z_{\mathrm{per}}(\beta)$ differentiates to $-\frac{k_L}{\beta \ln \beta} = o_L(1/\beta)$. Combined with the exact dyadic concavity bound $e_{\mathrm{plaq}}(\beta, \Lambda) \le \frac{2}{|P_+|\beta}\ln \frac{Z_\Lambda(\beta/2)}{Z_\Lambda(\beta)}$ (`YM-011-TORON-T1`) and real-analytic sublevel asymptotics (`YM-011-TORON-T2`), `P1` (`FIXED_VOLUME_PERIODIC_O_1_OVER_BETA`) is **PROVED** ($C_{\mathrm{per}}(L, 4, N) = \frac{(N^2 - 1)(3L^4 - 1)}{12 L^4} < \frac{N^2 - 1}{4}$), whereas `P2` (`VOLUME_UNIFORM_PERIODIC_O_1_OVER_BETA`) remains **`OPEN`** (`YM-011-DYADIC-FREE-ENERGY-UNIFORMITY`).

### NEG-YM-011-DYADIC-1: Thermodynamic Toron Irrelevance, Resolution of $P2$ (`VOLUME_UNIFORM_PERIODIC_O_1_OVER_BETA`), and Non-Sufficiency for Continuum Control ($P3$) (`YM-011-DYADIC-FREE-ENERGY-UNIFORMITY`)
- **Discovery Date:** 2026-09-30
- **Epistemic Classification:** `[THERMODYNAMIC_SCALING_RESOLUTION_AND_CONTINUUM_NON_SUFFICIENCY]`
- **Hypotheses tested:**
  1. Whether low-momentum infrared modes or toron zero modes accumulate intensive free-energy divergences as $L \to \infty$ at fixed $\beta$;
  2. Whether the periodic dyadic partition-ratio concavity bound establishes a volume-uniform $O(1/\beta)$ periodic plaquette bound (`P2`);
  3. Whether a volume-uniform lattice plaquette bound $e_{\mathrm{plaq}} \le C/\beta$ is mathematically sufficient to establish the continuum infinite-volume Wightman/OS spectral mass gap (`P3`).
- **Results:**
  1. **Thermodynamic Toron Irrelevance:** Because the flat toron moduli space $\mathcal{M}_{\mathrm{flat}} \cong \mathfrak{t}_{\max}^d / S_N$ has fixed dimension $d(N - 1)$ independent of volume, its specific free-energy density is suppressed as $O(L^{-d}) \to 0$ as $L \to \infty$. In $d = 4$, $C_{\mathrm{per}}(L, 4, N) = \frac{N^2 - 1}{4}(1 - \frac{1}{3L^4})$ strictly increases to $C_{\mathrm{bulk}}(4, N) = \frac{N^2 - 1}{4}$ without exceeding it.
  2. **Resolution of $P2$ at Weak Coupling:** In the dyadic ratio $Z_0(\beta/2) / Z_0(\beta)$, all non-zero Laplacian eigenvalues cancel identically, proving that the non-zero mode dyadic increment is bounded by the bulk limit for all $L \ge 2$. Combined with Kotecký–Preiss polymer tail suppression for $\beta \ge \beta_0(d, N)$, $e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{per}}(L, d)) \le \frac{C_{\mathrm{bulk}}(d, N)}{\beta}$ holds **uniformly in $L$** (`P2 = PROVED_AT_WEAK_COUPLING`).
  3. **Non-Sufficiency for Continuum Gap ($P3 = \text{OPEN}$):** A bare lattice weak-coupling plaquette bound establishes local field smoothness on fixed-cutoff lattices, but does **not** construct the continuum limit $a \to 0$, does not establish non-perturbative coupling renormalization $g^2(a) \to 0$, does not construct the continuum Schwinger functions, and does not establish a mass gap in physical units (`P3 = OPEN`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `GOAL_COMPLETE = FALSE`).

### NEG-YM-011-TRANSFER-1: Falsification of Unscaled Scale Transfer and Linear Tangent Drift (`YM-011`)
- **Discovery Date:** 2026-09-30
- **Epistemic Classification:** `[GEOMETRIC_DRIFT_AND_FLOW_MATCHING_FALSIFICATION]`
- **Hypothesis tested:** Whether a naive midpoint blocking map without flow matching or with an arbitrary flow parameter $\alpha \ne 2(d-1)t/a^2$ preserves $O(g_0^2)$ scale-transfer accuracy between lattice spacings $a$ and $2a$.
- **Result:** Falsified. If the flow matching condition $\alpha(t) = 2(d-1)t/a^2$ is not satisfied, the discrepancy between the blocked coarse observable and the fine observable retains an uncancelled linear drift $\sim |C_1| \left| \alpha - 2(d-1)\frac{t}{a^2} \right| \frac{1}{a}$, which produces an $O(1)$ discrepancy per link independent of coupling. Only the exact choice $\alpha(t) = 2(d-1)t/a^2$ eliminates the linear drift and reduces the tangent defect to the quadratic plaquette expectation $O(g_0^2)$.

### NEG-YM-011-TRANSFER-2: Insufficiency of Multiscale UV Scale Transfer for Intermediate Crossover and Continuum Mass Gap (`YM-011`)
- **Discovery Date:** 2026-09-30
- **Epistemic Classification:** `[CROSSOVER_BOUNDARY_OBSTRUCTION_AND_GAP_INSUFFICIENCY]`
- **Hypothesis tested:** Whether the geometric convergence of the multiscale UV transfer error $\sum_{j=0}^{n-1} 2^{-j} g_j^2 \le 2 g_0^2$ is sufficient to construct the infinite-volume continuum Yang-Mills theory and prove the mass gap $\Delta > 0$.
- **Result:** Falsified. The multiscale geometric series converges only within the perturbative domain $g_j \le g_* < 1$. At the intermediate crossover scale $a_{\mathrm{cross}} \sim 0.2\text{--}0.5\text{ fm}$ where $g_k \sim 1$, Bałaban's small-field Gaussian minimizer and polymer cluster expansion lose stability (`CrossoverBoundaryReached`). UV scale transfer alone cannot bridge the intermediate crossover window (`E-CROSSOVER = OPEN`), cannot construct the continuum Schwinger functions, and cannot establish the physical mass gap (`CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `GOAL_COMPLETE = FALSE`).

### NEG-YM-012-CROSSOVER-1: Falsification of Unconditional Flow-Mollified Crossover Continuation (`YM-012`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[NON_PERTURBATIVE_CROSSOVER_OBSTRUCTION_AND_TV_DIVERGENCE]`
- **Hypothesis tested:** Whether flow mollification and midpoint-exponential blocking can unconditionally continue the UV effective measure $\mu_{\mathrm{UV}}$ through the intermediate crossover window $g_k \sim 1$ into the strong-coupling polymer domain without measure-variation divergences.
- **Result:** Falsified. By Theorem `YM-012-T4`, the total variation distance $\mathcal{D}_{\mathrm{TV}}(\mu_{k+1}, (\mathcal{B}_\alpha^{\mathrm{mid}})_* \mu_k)$ between the interacting crossover measure and the pushed-forward measure is $\Omega(1)$ per scale step when $g_k \sim 1$ due to non-Gaussian effective action contributions of order $O(1)$. Summed over $K_{\mathrm{cross}} = \Omega(1/g_*^2 - 1/g_{\mathrm{strong}}^2)$ scale steps, the accumulated discrepancy is bounded away from zero and cannot be made arbitrarily small by flow matching alone. Edge `E-CROSSOVER` remains strictly `OPEN`.

### NEG-YM-012-CROSSOVER-2: Simultaneous Failure of Gaussian and Polymer Expansions in the Crossover Window (`YM-012`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[SIMULTANEOUS_EXPANSION_CONVERGENCE_BREAKDOWN]`
- **Hypothesis tested:** Whether either Bałaban's small-field Gaussian contractivity or the Osterwalder–Seiler character polymer expansion converges in the intermediate inverse coupling window $\beta \in (\beta_0, \beta_{\mathrm{UV}}^*)$ ($\beta \in (0.25, 6.25)$ for $SU(2)$).
- **Result:** Falsified. By Theorem `YM-012-T2`, for any $\beta \in (\beta_0, \beta_{\mathrm{UV}}^*)$:
  1. The Bałaban Gaussian contractivity parameter $\kappa_{\mathrm{BF}}(g) = C_{\mathrm{fluc}} g^2 \exp(c_1 g^2) \ge 1.0$ fails to contract, as non-Gaussian fluctuations exceed the Gaussian variance.
  2. The Kotecký–Preiss polymer criterion $\sum_{Y \sim X} |\zeta(Y)| e^{\mu |Y|} \le \mu |X|$ fails for the plaquette activity $\zeta(p) = \beta/(2N)$ on $\mathbb{Z}^4$ where coordination number $C_{\mathrm{geom}} \ge 6$.
  3. The Shen–Zhu–Zhu Langevin Ricci curvature lower bound degenerates to zero due to near-zero modes on the gauge orbit space.
  Thus, the crossover window is a genuine mathematical barrier unbridged by any known constructive expansion.

### NEG-YM-013-BOOTSTRAP-1: Finite-$N$ Multi-Trace Proliferation and Mandelstam Perimeter Explosion Obstruction (`YM-013`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[ALGEBRAIC_HIERARCHY_NON_CLOSURE_AND_PERIMETER_EXPLOSION]`
- **Hypothesis tested:** Whether finite-$N$ lattice loop equations (Schwinger–Dyson / Makeenko–Migdal) can self-close at a finite trace truncation degree $m < \infty$ or via Mandelstam trace reductions without generating infinite-degree or infinite-perimeter unknowns.
- **Result:** Falsified.
  1. By Theorem `YM-013-T1`, at any finite $N < \infty$, the absence of large-$N$ planar factorization ($\langle w(C_1) w(C_2) \rangle \ne \langle w(C_1) \rangle \langle w(C_2) \rangle$) causes the action variation $\sum_{p \ni \ell} \dots$ to couple $m$-loop correlators to $(m+1)$-loop correlators, producing an infinite, underdetermined BBGKY-type hierarchy.
  2. By Theorem `YM-013-T2`, while the $SU(2)$ Mandelstam identity $w(A)w(B) = \frac{1}{2}w(AB) + \frac{1}{2}w(AB^{-1})$ eliminates multi-trace operators, it sums loop perimeters: $|AB| = |A| + |B|$. This converts multi-trace proliferation into an exponential perimeter explosion $L \to \infty$, preventing closure at any finite loop cutoff $L_{\max} < \infty$.

### NEG-YM-013-BOOTSTRAP-2: Finite-Perimeter Truncation Barrier in the Continuum Limit (`YM-013`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[CONTINUUM_LIMIT_DECOUPLING_AND_TRUNCATION_BARRIER]`
- **Hypothesis tested:** Whether a finite-level semidefinite programming (SDP) loop bootstrap (at fixed truncation depth $L_{\max} < \infty$) can establish non-perturbative bounds on the intermediate coupling crossover window in the continuum limit $a \to 0$.
- **Result:** Falsified. By Theorem `YM-013-T4`, for any fixed $L_{\max} < \infty$, the physical perimeter of the bootstrap dictionary vanishes as $a \to 0$: $R_{\max}(a) = L_{\max} a \to 0$. Conversely, the physical crossover scale requires a fixed non-zero physical distance $R_{\mathrm{cross}} \sim \Lambda_{\mathrm{QCD}}^{-1} \approx 0.5\text{ fm}$, corresponding to lattice perimeter $L_{\mathrm{cross}}(a) = R_{\mathrm{cross}}/a \to \infty$. Thus, $\lim_{a \to 0} R_{\max}(a) / R_{\mathrm{cross}} = 0$. Any finite-level bootstrap is strictly blind to the non-perturbative crossover scale in the continuum limit. Edge `E-CROSSOVER` remains strictly `OPEN`, `P3 = OPEN`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, and `GOAL_COMPLETE = FALSE`.

### NEG-YM-014-SURFACE-1: Random-Surface Roughening and Entropy-Energy Divergence in the Crossover Regime (`YM-014`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[ENTROPY_ENERGY_DEFICIT_AND_ROUGHENING_DIVERGENCE]`
- **Hypothesis tested:** Whether the exact character-expansion random-surface representation converges and provides an un-inverted area-law lower bound throughout the intermediate crossover window $\beta \in [1.5, 2.5]$ ($g \sim 1$).
- **Result:** Falsified. By Theorem `YM-014-T1`, the 4D surface entropy connectivity constant satisfies $\mu_4 \ge 3.5$ ($\ln \mu_4 \ge 1.2528$, with physical hypercubic value $\mu_4 \approx 6.0$, $\ln \mu_4 \approx 1.7918$). The bare character-expansion surface tension $\tau_0(\beta) = -\ln a_{1/2}(\beta)$ satisfies $\tau_0(2.0) \approx 1.5298 < \ln \mu_4$. For all $\beta \ge \beta_c^{\mathrm{rough}} \approx 1.56$ (and even under the conservative lower bound $\mu_4 \ge 5.0$, for all $\beta \ge 1.88$), the growth factor $\mu_4 e^{-\tau_0(\beta)} > 1$. The random-surface partition sum $\sum_A N(A) e^{-\tau_0 A}$ undergoes a Hagedorn / roughening divergence, bare surfaces proliferate uncontrollably, and strong-coupling surface localization is destroyed.

### NEG-YM-014-SURFACE-2: Non-Abelian Dual Spin-Foam Sign Oscillation Barrier and Continuum Scaling Defect (`YM-014`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[NON_ABELIAN_SIGN_PROBLEM_AND_CONTINUUM_SCALING_DEFECT]`
- **Hypothesis tested:** Whether non-Abelian dual cell-complex / spin-foam representations or center-vortex decompositions can bypass the roughening divergence and provide an un-inverted confinement bound in the continuum limit.
- **Result:** Falsified.
  1. By Theorem `YM-014-T2`, 4D non-Abelian dual spin foams contain vertex weights formed by contractions of intertwiners (Wigner $6j$ / $15j$ symbols) that take indefinite signs (e.g. $\left\{\begin{matrix} 1 & 1 & 1 \\ 1/2 & 1/2 & 1/2 \end{matrix}\right\} = -1/3 < 0$). Dual weights are not strictly non-negative; the average sign decays exponentially with volume $\langle \operatorname{sign} \rangle \le e^{-c V}$, destroying probabilistic interpretation, Peierls contour percolation, and cluster expansions.
  2. By Theorem `YM-014-T3`, center-vortex decompositions $U_e = z_e V_e$ suffer from divergent non-local effective interactions when the $SO(3)$ coset degrees of freedom are integrated out at $\beta > \beta_0 \approx 0.35$.
  3. By Theorem `YM-014-T4`, physical continuum string tension requires $\tau(a) = \sigma_{\mathrm{phys}} a^2 \to 0$, which strictly forces $\tau(a) < \ln \mu_4$ into the rough phase as $a \to 0$. Fixed bare lattice surface models are structurally incompatible with continuum asymptotic freedom.
  Edge `E-CROSSOVER` remains strictly `OPEN`, `P3 = OPEN`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, and `GOAL_COMPLETE = FALSE`.



