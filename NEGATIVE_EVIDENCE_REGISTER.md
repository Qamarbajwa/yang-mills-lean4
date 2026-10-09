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
- **Result:** Falsified for $N \ge 3$ (and under naive Mandelstam concatenation).
  1. By Theorem `YM-013-T1`, at finite $N \ge 3$, non-factorization couples $m$-loop correlators to $(m+1)$-loop correlators via non-vanishing $\operatorname{Tr}(U_p - U_p^\dagger) \ne 0$.
  2. By Theorem `YM-013-T2`, Mandelstam multiplication sums perimeters: $|AB| = |A| + |B|$.
- **Post-Reconciliation Amendment Note (`YM-014R`):**  
  *Correction:* For $SU(2)$, $\operatorname{Tr}(U_p - U_p^\dagger) \equiv 0$ identically as an operator identity; the loop-splitting term vanishes, and the single-trace loop equations are **linear and closed on single-trace loops** (Kazakov & Zheng 2025). Furthermore, Liu & Yang (2026) showed that indirect loop equations eliminate intermediate loops without perimeter explosion. Theorem `YM-013-T1` is **REFUTED for $SU(2)$** (`NEEDS_AMENDMENT`), and Theorem `YM-013-T2` is confirmed with narrower scope (`METHOD_SPECIFIC_OBSTRUCTION`).

### NEG-YM-013-BOOTSTRAP-2: Finite-Perimeter Truncation Barrier in the Continuum Limit (`YM-013`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[CONTINUUM_LIMIT_DECOUPLING_AND_TRUNCATION_BARRIER]`
- **Hypothesis tested:** Whether a finite-level semidefinite programming (SDP) loop bootstrap (at fixed truncation depth $L_{\max} < \infty$) can establish non-perturbative bounds on the intermediate coupling crossover window in the continuum limit $a \to 0$.
- **Result:** Falsified for fixed $L_{\max} < \infty$. By Theorem `YM-013-T4`, for any fixed $L_{\max} < \infty$, the physical perimeter of the bootstrap dictionary vanishes as $a \to 0$: $R_{\max}(a) = L_{\max} a \to 0$. Thus, $\lim_{a \to 0} R_{\max}(a) / R_{\mathrm{cross}} = 0$.
- **Post-Reconciliation Amendment Note (`YM-014R`):**  
  *Correction:* This proves a **method-specific fixed-truncation limitation** (`METHOD_SPECIFIC_OBSTRUCTION`), not an impossibility theorem for the bootstrap framework. An adaptive hierarchy $L_{\max}(a) \sim R_* / a \to \infty$ with fixed physical reach $R_* > 0$ remains open and is not ruled out by Theorem `YM-013-T4`. Classified as `CONFIRMED_WITH_NARROWER_SCOPE`.

### NEG-YM-014-SURFACE-1: Random-Surface Roughening and Entropy-Energy Divergence in the Crossover Regime (`YM-014`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[ENTROPY_ENERGY_DEFICIT_AND_ROUGHENING_DIVERGENCE]`
- **Hypothesis tested:** Whether the exact character-expansion random-surface representation converges and provides an un-inverted area-law lower bound throughout the intermediate crossover window $\beta \in [1.5, 2.5]$ ($g \sim 1$).
- **Result:** Falsified for bare non-interacting ribbon surfaces. The bare character-expansion surface tension $\tau_0(\beta) = -\ln a_{1/2}(\beta)$ satisfies $\tau_0(2.0) \approx 1.5298 < \ln \mu_4$ (with $\mu_4 \approx 6.0$, $\ln \mu_4 \approx 1.7918$).
- **Post-Reconciliation Amendment Note (`YM-014R`):**  
  *Correction:* The estimate $\tau_0 < \ln \mu_4$ is an unweighted single-surface heuristic. In the full non-Abelian gauge theory, self-avoidance, intertwiner contractions, representation multiplicities, and severe sign cancellations intervene. The threshold $\beta_c^{\mathrm{rough}} \approx 1.44\text{--}1.80$ is an internally derived heuristic threshold, NOT a mathematically proved divergence of interacting 4D Yang–Mills. Classified as `CONFIRMED_WITH_NARROWER_SCOPE` (`METHOD_SPECIFIC_OBSTRUCTION`).

### NEG-YM-014-SURFACE-2: Non-Abelian Dual Spin-Foam Sign Oscillation Barrier and Continuum Scaling Defect (`YM-014`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[NON_ABELIAN_SIGN_PROBLEM_AND_CONTINUUM_SCALING_DEFECT]`
- **Hypothesis tested:** Whether non-Abelian dual cell-complex / spin-foam representations or center-vortex decompositions can bypass the roughening divergence and provide an un-inverted confinement bound in the continuum limit.
- **Result:** Falsified for bare lattice models.
  1. Wigner $6j$ symbols take indefinite signs (e.g. $\left\{\begin{matrix} 1 & 1 & 1 \\ 1/2 & 1/2 & 1/2 \end{matrix}\right\} = -1/3 < 0$), establishing `SIGNED_WEIGHTS_EXIST`.
  2. Coset polymer expansion on $SO(3)$ diverges at $\beta > \beta_0 \approx 0.35$.
  3. Bare lattice string tension requires $\tau(a) \sim \sigma_{\mathrm{phys}} a^2 \to 0 < \ln \mu_4$, collapsing into the rough phase.
- **Post-Reconciliation Amendment Note (`YM-014R`):**  
  *Correction:* While signed weights exist, the claim of an exponential-in-volume average sign decay $\langle \operatorname{sign} \rangle \le e^{-c V}$ is an **unproved extrapolation** in 4D Yang–Mills (downgraded under `NEEDS_AMENDMENT`). Furthermore, failure of the bare lattice string model does not rule out renormalized continuum strings (Polyakov, Lüscher–Weisz). Classified as `CONFIRMED_WITH_NARROWER_SCOPE` (`METHOD_SPECIFIC_OBSTRUCTION`).

### NEG-YM-014R-RECON-1: False Universality of Multi-Trace Proliferation in $SU(2)$ Lattice Loop Equations and Review Blind Spot (`YM-014R`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[GOVERNANCE_AND_LITERATURE_RECONCILIATION_FINDING]`
- **Hypothesis tested:** Whether the accepted Theorem `YM-013-T1` accurately captured the mathematical structure of $SU(2)$ lattice Makeenko–Migdal loop equations.
- **Result:** Refuted for $SU(2)$. By the operator identity $\operatorname{Tr}(U_p - U_p^\dagger) \equiv 0$ on $SU(2)$, the trace-splitting term in the Makeenko–Migdal equation vanishes identically. The loop equations for single-trace Wilson loops on $SU(2)$ are strictly linear and closed within the single-trace sector (Kazakov & Zheng 2025). The previous project claim that multi-trace proliferation universally prevents closure at finite $N$ was an error arising from conflating $SU(2)$ with general $SU(N \ge 3)$. Theorem `YM-013-T1` is formally amended.

### NEG-YM-014R-CLAIM-1: Dimensional Scaling Defect and Lack of Rotational Invariance in Faizal–Shabir (2026) Claimed Proof (`YM-014R`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[EXTERNAL_CLAIM_FALSIFICATION]`
- **Hypothesis tested:** Whether the claimed construction of four-dimensional $SU(N)$ Yang–Mills theory with mass gap and confinement by Mir Faizal and Arshid Shabir (Fortschritte der Physik 74 (2026), e70097) provides a mathematically valid solution to the Clay Millennium problem.
- **Result:** Falsified. The claimed proof contains fatal mathematical defects:
  1. **Dimensional Scaling Defect:** The paper asserts a scale-independent lower bound on the dimensionless transfer matrix gap $\mu(a) \ge c_0 > 0$ as $a \to 0$. In physical units, this implies $M_{\mathrm{phys}} = \mu(a)/a \to +\infty$ (divergent physical mass, empty physical Hilbert space). A finite physical mass strictly requires $\mu(a) \sim a M_{\mathrm{phys}} \to 0$, which is a critical point where polymer expansions lose convergence.
  2. **Coupling Domain Conflation:** The authors assume the polymer expansion remains convergent as $a \to 0$, ignoring the fact that asymptotic freedom requires the bare coupling to run to weak coupling $\beta(a) \to \infty$, far outside the polymer convergence domain $\beta < \beta_0 \approx 0.35$.
  3. **Lack of Euclidean Rotational Invariance (OS1):** The authors do not prove that discrete hyperoctahedral lattice symmetry restores continuous $SO(4)$ rotational invariance in the continuum limit.
  - **Surviving Novel Lemmas:** ZERO SURVIVING NOVEL LOAD-BEARING LEMMAS CLOSING A MISSING-BRIDGE EDGE. Standard foundational facts (lattice reflection positivity OS2 on hypercubic lattice, and finite-volume transfer-matrix spectral gap at fixed cutoff $a > 0$) remain valid standard facts, but close no missing-bridge edge across crossover or the continuum limit. `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `goal_complete = false`, and `P3 = OPEN`.

### NEG-YM-015-KIRK-1: Cut-Locus Singularity in Global Karcher Riemannian Blocking on Large-Field Sectors (`YM-015`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[EXTERNAL_CLAIM_DEFECT]`
- **Hypothesis tested:** Whether Harold D. Kirk (Version 4, 2026, Lemma 1) establishes an everywhere smooth, non-singular right inverse for Karcher Riemannian center-of-mass blocking on $SU(N)$ lattice gauge configurations.
- **Result:** Refuted for large fields. The Karcher mean on compact Lie groups $SU(N)$ possesses a unique smooth minimizer strictly within the injectivity radius $r_{\mathrm{inj}} = \pi/\sqrt{2N}$. On large-field configurations where link eigenvalues approach $-1$, the Karcher energy functional hits cut loci, bifurcations, and caustic singularities. Asserting a globally smooth blocking right inverse without a Bałaban-style small/large-field partition of unity is mathematically invalid on the full non-perturbative configuration space.

### NEG-YM-015-RP-1: Reflection Positivity Violation for 4D Mollified Observables Without Support Buffer (`YM-015`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether 4D gradient flow or 4D block averaging automatically preserves Osterwalder–Schrader reflection positivity (OS2) across the Euclidean time hyperplane $x_4 = 0$.
- **Result:** Falsified without support buffer. 4D gradient flow is isotropic parabolic diffusion with physical radius $R_{\mathrm{diff}} = \sqrt{8 t_{\mathrm{phys}}}$. An observable placed within distance $\delta \le \sqrt{8 t_{\mathrm{phys}}}$ of $x_4 = 0$ diffuses links into the negative time half-space $x_4 < 0$, violating the strict positive-time algebra condition $A \in \mathcal{A}_+$. Reflection positivity is preserved if and only if test functions satisfy the strict support buffer $\operatorname{dist}(\operatorname{supp}(f), \{x_4 = 0\}) > \sqrt{8 t_{\mathrm{phys}}}$.
- **Post-Reconciliation Amendment Note (`YM-015R`):**  
  *Correction:* The assertion that reflection positivity is restored by the support buffer $\delta > \sqrt{8t}$ is **REFUTED**. The quantity $\sqrt{8t}$ is only the root-mean-square diffusion length, not a compact support boundary. Parabolic heat diffusion has non-compact support ($K_t(x-y) > 0$ strictly everywhere for any $t > 0$), so flowed observables at $x_4 > 0$ depend on bare links in $x_4 < 0$ for all finite $\delta < \infty$. The exact RP defect is $\Delta_{\mathrm{RP}} \sim O(e^{-\delta^2/(4t)}) > 0$. Exact reflection positivity fails for all 4D gradient-flowed observables at finite flow time. Exact OS2 can only be recovered via a two-stage limit $t \downarrow 0$ (Route C). Classified as `REFUTED_FOR_EXACT_RP_AT_FINITE_FLOW_TIME`.
- **Post-Reconciliation Amendment Note (`YM-015R2`):**  
  *Correction:* Heat-kernel leakage rigorously proves `NOT_IN_STANDARD_POSITIVE_TIME_ALGEBRA` and `STANDARD_HALF_SPACE_RP_INHERITANCE_FAILS_AS_A_PROOF_METHOD`. However, this does **NOT** prove that the Osterwalder–Schrader quadratic form is negative ($\langle \Theta F_t F_t \rangle_{\mu_a} < 0$). In the absence of an explicit counterexample observable, claiming that exact RP is mathematically false is a non-sequitur. Authoritative status amended to **`EXACT_RP_UNRESOLVED_FOR_FINITE_4D_FLOW_TIME`**. Furthermore, identifying scalar heat-kernel tails with an OS quadratic-form defect is an unproved heuristic extrapolation, classified as `CONJECTURAL_ERROR_MODEL`.

### NEG-YM-015-POWER-1: Ultraviolet Power Divergences of Unsmeared Lattice Curvature Jets (`YM-015`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether unsmeared higher lattice curvature jets $J^{(k)}(x) = \nabla^{k-2} F(x)$ (Kirk 2026, Lemma 3) possess uniform, cutoff-independent $L^2$ bounds on discrete lattices.
- **Result:** Falsified. Discrete finite differences $\nabla_\mu$ on unflowed lattice fields scale as $a^{-1}$, inducing severe ultraviolet power divergences $O(a^{-k})$ as $a \to 0$ without multiscale subtractions or continuous flow mollification. Pointwise curvature jets do not define distribution-valued fields without explicit smoothing.

### NEG-YM-015-THERMO-1: Non-Sufficiency of Finite-Volume Continuum Limits for the Physical Mass Gap (`YM-015`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[STRUCTURAL_EDGE_SEPARATION]`
- **Hypothesis tested:** Whether constructing continuum Schwinger distributions and proving $SO(4)$ restoration in a fixed finite physical volume $V = L_{\mathrm{phys}}^4 < \infty$ suffices to establish the infinite-volume Yang–Mills mass gap.
- **Result:** Falsified (order of limits separation). In a finite physical volume $V < \infty$, the Hamiltonian spectrum is discrete and isolated by finite-size box quantization, producing an apparent discrete gap $\sim 1/L_{\mathrm{phys}}$ even in free massless gauge theories. Proving the true physical mass gap strictly requires taking the thermodynamic limit $L_{\mathrm{phys}} \to \infty$ across the non-perturbative crossover window ($g \sim 1$) and proving that the spectral gap remains strictly positive ($\lim_{L \to \infty} \Delta(L) \ge m > 0$). Task `YM-015` remains strictly upstream of the thermodynamic limit. `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `goal_complete = false`, and `P3 = OPEN`.

### NEG-YM-015R-RP-1: Parabolic Heat-Kernel Support Non-Compactness and Proof Method Breakdown (`YM-015R` / `YM-015R2`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether 4D gradient flow with support buffer $\delta > \sqrt{8t}$ satisfies exact Osterwalder–Schrader reflection positivity (OS2) at finite flow time $t > 0$ via standard half-space algebra inheritance.
- **Result:** Refuted as a proof method. Parabolic heat diffusion has non-compact support ($K_t(x-y) \propto e^{-|x-y|^2/(4t)} > 0$ strictly everywhere for any $t > 0$). Flowed fields at positive Euclidean time receive analytic contributions from bare links at negative Euclidean time. The positive-time algebra condition $\mathcal{O}_t(f) \in \mathcal{A}_+$ fails identically for all finite $\delta < \infty$. Standard half-space reflection positivity inheritance fails as a proof method.
- **Post-Reconciliation Amendment Note (`YM-015R2`):**  
  *Correction:* While standard half-space inheritance fails, no explicit gauge-invariant observable with $\langle \Theta F_t F_t \rangle < 0$ has been demonstrated. Exact reflection positivity at finite flow time is **`EXACT_RP_UNRESOLVED_FOR_FINITE_4D_FLOW_TIME`**, NOT definitively falsified.

### NEG-YM-015R-SO4-1: Insufficiency of Perturbative Symanzik Expansion for Non-Perturbative SO(4) Restoration (`YM-015R`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether representation-theoretic classification of dimension-6 hypercubic operators and perturbative Symanzik effective field theory rigorously prove non-perturbative continuous $SO(4)$ rotational covariance on the lattice path integral.
- **Result:** Falsified as a non-perturbative theorem. Symanzik improvement is an asymptotic expansion in powers of $g_0^2$. Proving that the non-perturbative lattice functional integral restores continuous $SO(4)$ rotational covariance requires uniform non-perturbative control over rough/large-field configurations, which is unproved. Classified as `PERTURBATIVE_SUPPORT_ONLY`.

### NEG-YM-015R-TOPOLOGY-1: Topological Non-Equivalence of Multilinear Dual Space with Product Sobolev Space (`YM-015R`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether a multilinear bound $|\Phi(f_1, \dots, f_k)| \le C \prod \|f_i\|_{H^3}$ places the functional in the product Sobolev space $H^{-3}((\mathbb{T}^4)^k)$.
- **Result:** Falsified. The tensor product $H^s \otimes_2 H^s \cong H^{s, s}_{\mathrm{mix}}$ has strictly dominating mixed derivatives and is strictly contained in $H^s(M \times M)$. A bounded multilinear functional belongs to the dual of the projective Banach tensor product $(H^3)^{\hat{\otimes}_\pi k}$, not to $H^{-3}((\mathbb{T}^4)^k)$. By the Schwartz kernel theorem on the nuclear space $C^\infty(\mathbb{T}^4)$, it defines a distribution in $\mathcal{D}'((\mathbb{T}^4)^k)$, but weak-* compactness of multilinear forms does not automatically constitute a physical Schwinger function system.

### NEG-YM-015R-NONTRIVIALITY-1: Non-Inference of Continuum Non-Degeneracy from Finite-Cutoff Variance (`YM-015R`)
- **Discovery Date:** 2026-10-02
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether strictly positive variance $\operatorname{Var}_{\mu_a}(\mathcal{O}_a(f)) > 0$ at finite lattice spacing $a > 0$ guarantees a non-zero lower bound $\inf_a \operatorname{Var}_{\mu_a}(\mathcal{O}_a(f)) > 0$ surviving the continuum limit.
- **Result:** Falsified. Finite-cutoff non-degeneracy $\operatorname{Var}_a > 0$ is a trivial consequence of Haar measure support on compact $SU(N)$. Proving that the variance does not vanish in the continuum limit requires non-perturbative remainder bounds. Lüscher's perturbative formula $\operatorname{Var} \sim g^4(t)/t^4$ is perturbative and presupposes the continuum limit. Non-triviality is proved only as `FINITE_CUTOFF_NONDEGENERACY_ONLY`.

### NEG-YM-015R2-RP-DEFECT-1: Unproved Equivalence of Scalar Heat-Kernel Leakage with OS Quadratic-Form Defect (`YM-015R2`)
- **Discovery Date:** 2026-10-03
- **Epistemic Classification:** `[CONJECTURAL_ERROR_MODEL]`
- **Hypothesis tested:** Whether the linear heat-kernel tail probability $\frac{1}{2}\operatorname{erfc}(\delta/\sqrt{4t}) \sim e^{-\delta^2/(4t)}$ rigorously bounds the reflection-positivity quadratic-form defect $\Delta_{\mathrm{OS}}(F_t) \equiv \max(0, -\langle \Theta(F_t) F_t \rangle_{\mu_a} / \|F_t\|^2)$ on the full non-linear lattice Yang–Mills functional integral.
- **Result:** Falsified as a proved mathematical theorem. Connecting linear scalar diffusion tails to non-linear Wilson flow requires controlling non-Abelian Lie algebra derivatives, non-Gaussian measure correlations, large-field polymer sectors, and thermodynamic uniformity. In the absence of an independent mathematical proof, the estimate $\Delta_{\mathrm{RP}} \lesssim e^{-\delta^2/(4t)}$ is an unproved conjectural extrapolation and is formally excised from all theorem-level proofs.

### NEG-YM-015R2-SPATIAL-FLOW-1: Explicit Hypercubic Symmetry Breaking and Temporal Contact Singularities in Spatial Gradient Flow (`YM-015R2`)
- **Discovery Date:** 2026-10-03
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether purely spatial gradient flow $\partial_t B_i = \sum_{j=1}^3 D_j G_{ji}$ provides a complete replacement for 4D gradient flow that simultaneously preserves exact reflection positivity (OS2), 4D Euclidean rotational invariance (OS1), and universal ultraviolet finiteness ($Z \equiv 1$).
- **Result:** Falsified for simultaneous closure. Spatial gradient flow strictly preserves exact reflection positivity on time slices (Criterion A, `SPATIAL_FLOW_RP_COMPATIBILITY_PROVED`), but:
  1. Explicitly breaks the 4D hypercubic lattice symmetry $H_4$ down to cubic $H_3 \times \mathbb{Z}_2$, leaving non-perturbative $SO(4)$ restoration as an unsolved downstream challenge;
  2. Leaves the Euclidean time direction $x_4$ unsmoothed, resulting in surviving temporal contact divergences and requiring non-trivial operator renormalization ($Z \ne 1$).

### NEG-YM-015R2-FIXED-T-BOUND-1: Absence of Published Non-Perturbative Multiscale Observable Insertion Bounds (`YM-015R2`)
- **Discovery Date:** 2026-10-03
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]`
- **Hypothesis tested:** Whether Bałaban's published constructive renormalization group programme (CMP 1984–1989) directly provides cutoff-independent uniform bounds on correlation functions of gradient-flowed field-strength operators $\mathcal{O}_{a,t}(f)$.
- **Result:** Falsified as an off-the-shelf citation. Bałaban's published theorems establish ultraviolet stability of the partition function and free energy density, but do not construct or bound local flowed observable insertions. Extending Bałaban's polymer expansions to include flowed field-strength insertions requires controlling the non-local flow Jacobian $\delta V_t / \delta U$ across multiscale block-spin transformations, which is mathematically plausible but remains unproved in the literature. Theorem `YM-015F-L1` is classified as `PARTIAL_PROGRESS — CONDITIONAL_ON_BALABAN_OBSERVABLE_FLOW`.




## YM-034 / 2026-10-04: insertion shortcut reconciliation

- METHOD_SPECIFIC_OBSTRUCTION: per-polymer bad-field suppression does not imply a probability exp(-c beta V/a^4) for occurrence of any bad polymer. Independent Bernoulli countermodel and exact scope: research/YM_015F_INSERTION_SOURCE_AUDIT.md. No counterexample to the physical Wilson measure asserted.
- METHOD_SPECIFIC_OBSTRUCTION: linear heat smoothing alone does not prove nonlinear gauge-flow curvature bounds or conversion of lattice coordinates to physical norms. Required estimate remains OPEN.
- METHOD_SPECIFIC_OBSTRUCTION: uniform zero-source partition values do not imply uniform source derivatives; exp(s/a) is an elementary countermodel. Finite cutoff analyticity gives no uniform radius or bound.
- All-moment finiteness need not imply exponential integrability (lognormal countermodel); finite nilpotent source jets avoid an unnecessary hypothesis.
- Critical SPDE homogeneity gains vanish under d=3 to d=4 substitution. This is an algebraic method diagnostic; first numbered proof-local failure remains pending.
- Bałaban source labels require correction: CMP102 is 3D; final 4D stability publisher abstract is CMP122. Exact source activity estimates remain unverified.
- No structural no-go or scientific edge closure follows. STRUCTURAL_NO_GO_COUNT=0. Candidate mathematical reconciliation is pending independent review.


## YM-035: exact source transport and method-specific limitations
- Signed mass-one pieces need not contract norms; the exact finite 2delta_u-delta_v countermodel is recorded in research/YM_015F_EXACT_SOURCE_TRANSPORT_035.md.
- Positive conditional integration preserves existing integrability with constant one; it supplies no cutoff-uniform input or strict RG contraction. Dropping conditional connected source coefficients can erase mixed moments (Rademacher countermodel).
- The plaquette-source field is scaled and unflowed; SU(N), quadratic normalization and flow/smearing hypotheses remain unmatched. Literal source constants require PDF/proof extraction; no theorem is falsified by an upper-bound discrepancy.
- Correction: the source boundary factor tends to one on the fixed-physical-volume AF diagonal; fixed-site weak-coupling nonuniformity is not an obstruction to that diagonal.
- Atlas source rule(5.6) and its subcritical-completion assertion have now been located. A first failing numbered lemma and a critical 4D replacement theorem remain unproved.
- All entries METHOD_SPECIFIC_OBSTRUCTION; STRUCTURAL_NO_GO_COUNT=0. No continuum edge closes. Candidate artifacts require fresh review.


## YM-036: marked recurrence and quadratic-source limitations
- Dropping conditional covariance sectors loses the full third connected coefficient in the exact rational 9/8 countermodel. Source-dependent factors require disjoint-subset convolution, not source-free transport.
- Compact group single-matrix quadratic domination is uniform on its stated finite source disk. It does not identify an interacting plaquette marginal or prove a flowed clover bound; reflected lattice factorization, support growth, denominators and signed activity norms remain open.
- Literal PDF normalization, absolute-sine equality and constants discrepancies remain recorded without silently repairing or declaring the physical theorem false.
- A verified small-field map is not an all-sector map. Unknown source extraction is not falsification. All findings are METHOD_SPECIFIC_OBSTRUCTION; no continuum edge closes and STRUCTURAL_NO_GO_COUNT=0.


## YM-037: terminal and all-sector normalization defects
- A vanishing bad-sector probability does not control marked moments: epsilon^2 probability with epsilon^-3 insertion has expectation epsilon^-1. Finite probability countermodel only, not a physical Wilson counterexample.
- Terminal reweighting changes the coarse measure and incurs the explicit normalized density-ratio/Holder cost. Constant-one conditional transport in the prior measure does not remove it.
- Extracted scalar source jets must be restored by subset convolution. Vacuum-only equalities do not establish marked terminal functional identities. Signed activities require total variation and the actual reconstructed denominator.
- All estimates for actual physically normalized flowed sources, all-sector RG and terminal law remain open. METHOD_SPECIFIC_OBSTRUCTION; STRUCTURAL_NO_GO_COUNT=0; no continuum edge closure.
- Atlas037 locates Lemma5.17 model convergence and a strict sufficient criterion; a physical-degree4D diagnostic loses margin, but exact source-tree/convention transfer and earliest failure remain unresolved. Sufficient-criterion failure does not prove convergence impossible.


## YM-038: source gates and constrained coordinates
- A minimum-degree margin alone does not verify Theorem2.15: every quantified subtree/leaf test, complete-subcritical rule and uniformly compatible Gaussian inputs are required. Formal4D branch diagnostics do not identify an admissible tree in a verified4D rule.
- Extracted small-field coordinate cutoffs, Haar/constraint factors and normalization must remain in the marked representation; no all-sector Wilson disintegration or uniform flowed-source estimate is inferred.
- Missing source/coordinate dictionaries are pending obligations, not falsified theorems. METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0 and all continuum edges remain open.


## YM-039: basic R-step and degree convention limitations
- R-I printed177 explicitly qualifies introductory(0.3): actual denominators use localized parts rather than full densities. Extracted(1.100) quotient is one factor of basic R-prime, not a reconstructed all-sector operator. Vacuum equality(1.102) does not establish marked coefficient equality.
- Literal initial heat degree2-kappa and later heat-gain2 tree counting give different slack coefficients. Both displayed3D margins remain positive; full assignment/regrading dictionary is pending, not an author-theorem counterexample. Neither scheme produces a positive displayed4D gain.
- All actual uniform source/terminal estimates and earliest proof-local4Dfailure remain open. METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0; no continuum edge closure.

## YM-040: localized source-denominator compensation

- A normalized local quotient jet integrates to zero in every nonempty degree; it therefore cannot replace the raw conditional marked jet without the denominator jet. Exact two-point example L=1+zx, x in {0,1} equiprobable, F=x gives raw marked coefficient1/2 versus quotient coefficient1/4; restoration recovers1/2. Finite shortcut countermodel only, not a physical Wilson or author-theorem counterexample.
- Exterior-dependent local normalizations must remain inside exterior integration; source-dependent gauges, maps and cutoff measures require their own coefficient rules. Vacuum R-prime equality does not identify these rules.
- A finite algebraic inverse has no smallness requirement, but its norm cost and marked input norms can grow with cutoff and scale count. No uniform-flow estimate, operator reconstruction, atlas earliest failure or continuum edge closes. METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0.


YM-040 pre-acceptance covariance-premise repair: both individual factors and their products must be absolutely integrable. Product integrability alone does not define separate means; C=1/y,T=0 on uniform(0,1) is a countermodel to that shortcut. Initial candidate challenged and retained in Git/raw receipt; no accepted state relied on it. METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0.

## YM-041: retained branch and changed density marked gates

- Numbered basic R-prime predecessors distinguish successive selected-class reductions from complementary operations, and density-preserving preliminary representation changes from later equal-integral replacements. Omitting rejected branches or assuming marked equality from vacuum equivalence is unsupported.
- Own finite reference probabilities1/2 on x=0,1, density(0,2), averaged density1: both vacuum integrals1; unchanged test x gives1 versus1/2. Proper transported conditional test1 restores the mark. This falsifies only an unchanged-observable shortcut, not Bałaban's construction.
- Complete all-sector marked/source/terminal dictionary and uniform bounds remain OPEN. No atlas failure or continuum edge closes. METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0.

YM-041 parallel atlas limitation (root source audit): CH16 Theorem2.33 requires strict two-assignment degree gap for every negative tree. Conditional heat-only regrading gives no gap to a bare-noise tree with zero heat edges if that tree belongs to the quantified negative family. Actual rule/tree/norm and Definition2.32 typography remain OPEN. This is a hypothesis gate, not earliest4Dfailure, an author counterexample or no-go; structural no-go count0.


## YM-042: first changed-density integration premise gap

- R-I (1.76) integrates disjoint regions; its first integral stays unchanged, delta constraints are already eliminated there, and tree gauge is introduced later. A source lift that merges these stages or drops the first integral/complement is not supported by the numbered chain.
- Positive Wilson disintegration does not verify positivity or probability-reference normalization of individual effective-action histories. The conditional degree-one ratio needs nonnegative vacuum density, absolutely integrable marked coefficient absolutely continuous with respect to it, and the actual reference/domain dictionary. For signed terms, zero vacuum integral can coexist with nonzero marked integral; coefficient integration remains available but division/Jensen need separate proof.
- History-dependent supports, source-decorated maps, all complementary-sector sums and terminal estimates remain unmatched. METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0; no continuum closure.


YM-042 parallel root atlas limitation: finite noise-slack regrading requires q>=1, half-integer baseline degrees, finite counted family and kappa<1/(2M). The supplied-family floor/sign/gap certificate does not exhaust the actual generated family or verify R-consistency/theorem/model-norm correspondence. Zero-noise case q=0,r=0,m=1 violates floor/sign matching; separate treatment is required. Alternative analytic-degree branch margins2-D/2-kappa and4-D-2kappa remain negative at D=4 for positivekappa, so this certificate is no critical repair, earliest4Dfailure or structural no-go.


## YM-043: inherited-reference normalization gate

- The actual predecessor fluctuation representation keeps Gaussian integrations, normalization and interaction/background factors. A Gaussian-looking integrand cannot silently be promoted to a probability reference; constrained-variable removal and coupling scaling require their inherited constants/Jacobians.
- H042 is conditional: physical Wilson positivity and later gauge invariance do not establish positivity or unit reference mass of each effective-action history. Full R-I text terminology search did not identify the needed explicit Haar convention; this is a bounded audit limitation, not an assertion of source absence.
- Source-decorated all-sector/terminal mapping and uniform estimates remain OPEN. METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0; no continuum closure.


YM-043 root atlas limitation:207-template enumeration exhausts only the expressly defined full-arity ordered scalar syntax, not the authors' normal extension/completion, decorations, type labels or all required subtrees. Under the stated4D comparison, binary chains have degrees-3-(3q-2)kappa and are unbounded below; this is a method-specific power-counting diagnostic, not a universal4D obstruction or earliest proof-local numbered failure. Actual completion/model mapping remains open; structural no-go0.


## YM-044 — inherited integral is not yet a probability reference

Primary [III] inherited operator dictionary places conditional Lambda integration separately from residual T integration and retains constants/bond factors. This defeats the inference that merely calling an integral conditional establishes the positive unit-mass history reference H042. No source theorem is falsified. Exact measures/Jacobians, component supports, source decorations, history positivity, normalization and terminal control remain OPEN. Initial publisher PDF URL returned3038 bytes HTML; guessed Euclid identifier was inaccessible; successful public issue-derived Euclid PDF supplied the evidence. Source access limits are not mathematical negative results. No typography from043 is retrospectively certified. Classification METHOD_SPECIFIC_OBSTRUCTION; structural no-go count0; no continuum edge closes.


YM-044 root atlas boundary: slot pruning extends only the own scalar comparison. Empty roots have degree0 and strict assignment gap0; excluded from negative certificate, not ignored. Admissible full-arity4D binary chains persist and remain unbounded below under the stipulated assignment; pruning does not restore a positive margin. No actual author completion or earliest numbered4Dfailure established. METHOD_SPECIFIC_OBSTRUCTION; structural no-go0.


## YM-045 — normalized Gaussian does not identify the all-sector history reference

Primary [I] small-field normalization and Jacobian placement are audited in research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md. Own inference: a normalized reference Gaussian does not make its cutoff/interaction-weighted integral unit mass; a unit-background normalization does not establish fiber normalization at every exterior background. Exact history/domain/boundary matching to [III]/R-I, positivity or signed absolute control, source mapping and terminal uniformity remain unverified. This is a missing-premise record, not a source theorem counterexample. Web-tool PDF retrieval failed; ordinary public PowerShell acquisition succeeded, and no denial content was used as evidence. Full formulas and the tentative043 prefactor glyph remain uncertified. METHOD_SPECIFIC_OBSTRUCTION; structural no-go0; no continuum edge closure.


YM-045 root parity-only transfer limit: the necessary odd-noise/odd-decoration exclusion in numberedLemma5.5 is not a finiteness theorem. Own pruned evenq/even-derivative chains remain negative in4D with unbounded-below degrees for positivekappa. Passing the filter does not assert nonzero BPHZ value or actual author membership. No source theorem falsified; earliest numbered4Dfailure remains unestablished. Fixed root gain cannot repair this comparison; a quantified per-noise gain still needs actual analytic proof. METHOD_SPECIFIC_OBSTRUCTION; structural no-go0.


## YM-046 — history identification remains incomplete

Primary [III]257(2.18) suppresses S-sequence/action dependencies;267 before(3.15) retains a resummed zeta at fixed Omega and states that reused formulas act on different domain-dependent operators. Therefore identifying a history from Omega alone or equating C measures by symbol reuse is unverified. Complete admissibility/weights and mapping to R-I transformed supports are missing; no arbitrary empty/full history was invented. This is a bounded source-dictionary gap, not a source contradiction or impossibility theorem. Local normalized Gaussian evidence045 does not close H042 or all-sector marked transport. PrimaryPDF reuse and visual/text scope recorded in audit039. All continuum statuses retained, structural no-go0.


YM-046 root numbered proof-local limit: source5.12 uses a positive order coefficient to exclude n>=6. Own stipulated4D heat2 comparison has coefficient0 and even-order necessary-count witnesses of unbounded negative degree, including marginal cubic external patterns. These counts need not be realizable symbols or nonzero characters. No source3Dlemma falsified; earliest global4Dfailure remains unestablished. Grading-specific gains are not interchangeable across unresolved initial/later assignments. METHOD_SPECIFIC_OBSTRUCTION; structural no-go0.


## YM-047 source support limitation

[III]265(3.2)–(3.3) supplies strict/complementary local cube indicators with a P-dependent Q universe. Treating P/Q as independent subsets of a common domain or treating zeta as an unweighted probability history is unsupported. Gauge-fixing factors and remaining admissibility conditions have not been reconstructed in full. R-I source dependence of these vacuum cutoff supports is unverified, not asserted. Classification METHOD_SPECIFIC_OBSTRUCTION; full marked history and continuum edges remain OPEN; structural no-go count0.


YM-047 root mark-omission countermodels: moving sharp support has no ordinary L1 source coefficient despite pointwise a.e. derivative0; endpoint and complementary sector-weight marks are essential in the stated interval example. Vacuum parity alone does not annihilate a first source mark; a positive Gaussian insertion has L0(G)=0,L1(G)=1. These falsify only unrestricted omission rules, not source theorems. ActualRGcutoff motion/observableparity are not asserted. METHOD_SPECIFIC_OBSTRUCTION; structural no-go0; no continuum closure.


## YM-048 candidate: gauge/support and vacuum-equivalence limitations

Primary-source locators and provenance: research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md, YM-048. Host-Python extraction succeeded after repository-venv fitz absence; no new network acquisition or complete prefactor typography claimed. The exact S/R boundary/complement formulas remain unaudited as formulas despite the certified prose restrictions. No complete nontrivial admissible R-I history is instantiated.

METHOD_SPECIFIC_OBSTRUCTION: vacuum-integral equivalence after term-dependent Lambda integration does not itself establish an arbitrary observable insertion identity. An inserted or adjoint transport must be derived with the actual measures, domains and retained T/zeta components. This is a missing premise, not falsification of the source's vacuum equivalence, a proof of actual flowed parity, or a structural Yang-Mills no-go. Likewise gauge-averaging normalization does not identify every effective-history fiber with a probability measure, and one cutoff's invariance under an excluded-coordinate linearization does not establish invariance of all cutoffs or source insertions.

All-sector/source/normalization/terminal uniform obligations remain OPEN; no continuum edge closes; structural no-go count0.


## YM-048 bounded negative evidence
Own positive linear maps T=(1,1),A=(2,0) agree on vacuum(1/2,1/2), but on marked(1/2,-1/2) give0 and1. Equality of one vacuum integral therefore does not establish the marked adjoint identity; source R-I vacuum formulas are not falsified. Own full finite-jet covariance needs combined source/observable parity, not a vacuum-only filter: centered Gaussian q=1 with one odd mark has coefficient1. For q=2/two repeated odd marks the fixed-vacuum mixed coefficient3 becomes2 under source normalization, despite identical parity selection. No author model/flowed observable is identified with these witnesses. Classification METHOD_SPECIFIC_OBSTRUCTION; no structural no-go, dimensional gain or scientific edge closure. Actual all-sector, normalization, terminal and cutoff-uniform source estimates remain OPEN.


## YM-049 candidate: disjoint-domain and gauge-orbit marking limitations

Primary inspection provenance and locators: research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md, YM-049. Initial PDF page-offset guess returned printed headers two pages earlier; corrected by verified headers before attribution. No new HTTP access or exact full formula transcription is claimed.

METHOD_SPECIFIC_OBSTRUCTION: disjoint integration regions in R-I(1.76) do not imply independent normalized fibers. The unchanged Zh integral cannot be discarded when treating the fluctuation integral. Unmarked gauge invariance and Faddeev-Popov insertion do not identify the original flowed observable's coordinate pullback; an actual inserted gauge-orbit identity with retained boundary conventions is required. The supported cutoff replacement(1.89) cannot replace complementary branches or normalize every effective-history term. These are missing premises, not source theorem falsifications or proof of an actual Yang-Mills obstruction.

No actual nontrivial history, termwise marked adjoint or cutoff-uniform terminal bound has been identified. All-sector/source/normalization/continuum obligations remain OPEN; structural no-go count0.


## YM-049 own observability and orbit-normalization limits
Positive T_epsilon fixes normalized vacuum but a contrast target recovered from unmarked reduced data has unique adjoint norm1/epsilon; at epsilon0 kernel loss forbids that particular descent. The same column-stochastic map exactly preserves masses of preinserted marked coefficients, so this is not an obstruction to the selected full source-jet route or Yang–Mills. Toy even projection preserves vacuum yet loses odd-source/odd-probe pairing1; no BPHZ lemma is identified with that projection. Signed orbit kernel2 delta_identity-delta_swap fixes invariant marks but amplifies noninvariant contrast by3, so massone does not imply probability contraction. Actual Faddeev-Popov measure/original physical gauge pullback are unverified; abstract invariance does not close them. Classification METHOD_SPECIFIC_OBSTRUCTION; structural no-go0, no cutoff-uniform gain or scientific edge closure.


## YM-050: OpenAI Family 215 unverified candidate and criticality mismatch

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]` / `[UNVERIFIED_CANDIDATE_PREPRINT]`
- **Hypothesis tested:** Whether OpenAI Family 215 provides a verified, mathematically transferable technique for controlling the missing M1 source insertion term in 4D Yang–Mills constructive RG.
- **Result:** Falsified as a verified transfer.
  1. Primary-source audit of `openai/math` (Problem 215 / Family 215, upstream public release October 6, 2026, `math/lean/docs/215.md`, `formalization.yaml`) establishes that its inspectable Lean 4 formalization is strictly limited to declaration head `lattice_spin_decay_2d` (classical lattice spin correlation decay for $O(n)$, $n \ge 3$, on finite 2D periodic lattices under nearest-neighbor ferromagnetic action). Exhaustive search across declaration heads reveals that zero Lean declarations exist for continuum QFT construction, Osterwalder–Schrader axioms, non-Gaussianity, or the one-particle mass gap pole. The claimed full continuum construction remains an unreviewed candidate preprint (`UNVERIFIED_CANDIDATE_PREPRINT`).
  2. The 2D $O(3)$ sigma model is strictly critical / renormalizable (dimensionless coupling), not super-renormalizable.
  3. The spin source term $J \cdot q = J_\pi \cdot \pi + J_\sigma \sqrt{1 - \|\pi\|^2}$ is strictly non-linear in local fluctuation coordinates $\pi$ on $S^2$, refuting the claim that source coupling is a simple linear Gaussian shift.
  4. Local $L^1$ integrability of the 2D Green's kernel does not establish cutoff-uniform source analyticity for a non-linear field theory.
  5. The transfer proposal is classified as `UNVERIFIED_CANDIDATE_PREPRINT` and `METHOD_SPECIFIC_OBSTRUCTION`; no accepted transfer is promoted, and zero DAG edges close.
  6. **[CHALLENGED_AND_SUPERSEDED IN YM-050R2]:** The path `math/lean/docs/215.md`, periodic boundary condition, and declaration head `lattice_spin_decay_2d` cited in this historical entry are superseded by exact upstream commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, path `lean/docs/215.md`, free-boundary condition, comparator `OAI.ClassicalON.main : ExponentialDecay := by sorry`, and candidate solution module `lean/OAI/Probability/ClassicalON/Main.lean` (see entry `NEG-YM-050R2-FAMILY215-PROVENANCE`).


## YM-050: physical observable non-factorization across disjoint regions and trace-only omission

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether disjoint integration regions in R-I (1.76) allow independent factorization of the physical flowed observable insertion, and whether the nilpotent determinant trace $\frac{1}{2} \operatorname{Tr}(Q^{-1} B)$ captures the complete first moment.
- **Result:** Falsified.
  1. Gradient flow over positive flow time $t > 0$ generates non-compact diffusion across physical distance $\sim \sqrt{8 t_{\mathrm{phys}}}$. For test functions whose diffusion envelope intersects both $Z_h$ and $\Omega \setminus Z_h$, the physical clover energy density $\mathcal{O}_{a,t}(f)[V e^{g A}]$ couples link variables across both $Z_h$ and active fluctuation regions. This demonstrates a generic failure of spatial factorization across disjoint vacuum integration domains in (1.76), precluding the universal assumption of observable factorization, while leaving open trivial factorization in uncoupled/degenerate limits.
  2. In the nilpotent algebra $\eta^2 = 0$, $\det(Q - \eta B)^{-1/2}$ linearizes exactly to $1 + \frac{1}{2} \eta \operatorname{Tr}(Q^{-1} B)$. However, replacing the full physical insertion by this trace alone drops linear fluctuation terms $DX[V] \cdot A$ that contract with cubic/quartic interaction vertices in the non-Gaussian effective action, producing an exact strictly non-zero moment defect in interacting models.
  3. Classification: `METHOD_SPECIFIC_OBSTRUCTION`; structural no-go count remains 0; no continuum edge closes.


## YM-050R: Faddeev–Popov orbit vs configuration slice conflation and endpoint coordinate action

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether the single-orbit Faddeev–Popov resolution of unity on a maximal tree directly produces the gauge-slice delta distribution on the initial configuration, and whether holding background $V$ fixed under site gauge transformations yields simple endpoint adjoint action on fluctuation $A$.
- **Result:** Falsified.
  1. The single-orbit Faddeev–Popov identity on a maximal tree evaluates to $\int_{G_T} dg \prod_{b \in T} \delta((A^g)(b)) = \Delta_{\mathrm{FP}}(V, A)^{-1}$. On any single configuration orbit this is a scalar ($1/\Delta_{\mathrm{FP}}$), NOT the distribution $\prod_{b \in T} \delta(A(b))$. Equating them yields an exact mismatch (exposed by setting $\mathcal{O} = 1$, where $1/\Delta_{\mathrm{FP}} \ne \prod_b \delta(A(b))$). The gauge-slice delta $\prod_{b \in T} \delta(A(b))$ arises strictly under the full configuration-space functional integral $\int d\mu(A)$ after a functional change of variables using gauge invariance of the measure.
  2. For composite link $U_{xy} = V_{xy} \exp(g A_{xy})$, site gauge transformations $h \in \mathcal{G}$ act at both endpoints: $U_{xy}^h = h_x U_{xy} h_y^{-1}$. Holding background $V$ fixed does not commute with this action: $V_{xy}^{-1} h_x V_{xy} \exp(g A_{xy}) h_y^{-1} \ne \exp(g h_y A_{xy} h_y^{-1})$ unless $h_x = V_{xy} h_y V_{xy}^{-1}$. Bałaban's compensating transformations (R-I (1.85)–(1.88)) require joint transformation of both background $V \mapsto V^h$ and fluctuation $A \mapsto h^{-1} A h$.
  3. Consequently, asserting an uncoupled tree-gauge identity on fluctuation $A$ with fixed background $V$ is mathematically defective. The actual-model Bałaban coordinate pullback and tree-gauge orbit identity are reclassified as `CONDITIONAL_AND_OPEN` (`ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_ORBIT_IDENTITY_OPEN`).
  4. Classification: `METHOD_SPECIFIC_OBSTRUCTION`; structural no-go count remains 0; no continuum edge closes.


## YM-050R2: OpenAI Family 215 primary-source provenance and proof status repair

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]` / `[UNVERIFIED_CANDIDATE_PREPRINT]`
- **Hypothesis tested:** Whether OpenAI Family 215 at commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` provides a verified, kernel-checked, transferable technique for 4D Yang–Mills source control.
- **Result:** Falsified and source provenance repaired.
  1. **Upstream Locators & Hashes:** Repository `https://github.com/openai/math.git` at commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Scope doc: `lean/docs/215.md` (LEN 1,031 bytes, SHA-256 `41ed31b3d5b0f9c0ce5df3604527f17b26eec23b225a7a2184f5a9c2d936ac30`). Comparator challenge: `lean/ComparatorChallenges/ClassicalON.lean` (LEN 1,961 bytes, SHA-256 `c2f5f88455b811eb6b56c1ae80ff91f4e398e18e7c7fbeee6daca8da4122d696`). Manifest: `lean/ComparatorChallenges/ClassicalON.json` (LEN 308 bytes, SHA-256 `47cb3623915c8cfcc35099fabd0c44173afa72b706eb0526c4b8d3855e789252`). Solution module: `lean/OAI/Probability/ClassicalON/Main.lean` (LEN 2,050 bytes, SHA-256 `0e4bca8c6b8fe89ffec32eda5d3222af85062a2e3e685729f41578076b528c8a`).
  2. **Boundary Conditions & Model:** The model specifies classical $O(n)$ ($n \ge 3$) spin correlation decay on finite square-lattice subgraphs with **FREE boundary conditions**, NOT periodic boundaries. Infinite-volume limit and $O(4)$ spectral gap are explicitly disclaimed in `lean/docs/215.md`.
  3. **Declaration Heads & Proof Status:** The phantom declaration head `lattice_spin_decay_2d` does not exist. The comparator challenge specifies `def ExponentialDecay : Prop` and `theorem main : ExponentialDecay := by sorry`. The candidate solution `Main.lean` contains proof script text `theorem main : ExponentialDecay := by ...`. However, because downloaded code is untrusted and no reproducible kernel-checked build receipt is verified, proof status is strictly `UNVERIFIED_UPSTREAM_PROOF_CODE`.
  4. **Inspected Scope vs. Nonexistence Theorem:** Direct inspection of the scope doc, comparator challenge, manifest, and solution main module establishes a search-negative finding: zero declarations exist for continuum QFT construction, Osterwalder–Schrader axioms, non-Gaussianity, or 4D Yang–Mills. This search-negative finding across inspected primary files is distinguished from an unproved universal assertion of repo-wide nonexistence.
  5. **Transfer Status:** Classification remains `UNVERIFIED_CANDIDATE_PREPRINT` and `METHOD_SPECIFIC_OBSTRUCTION`; allowed transfer conclusion is strictly None; zero DAG edges close.


## NEG-YM-051-ONE-TERM-REPRESENTATION: Single-Term Admissible Pullback Insufficiency for Multiscale Cluster Expansion and Continuum Limit (`YM-051`)

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether instantiating the exact coordinate pullback, tree-gauge resolution, and compensating transformation for ONE admissible history term $\alpha$ from Bałaban R-I (1.76) suffices to establish multiscale marked polymer activity summability or the continuum limit of flowed correlation functions.
- **Result:** Falsified.
  1. The single-term admissible representation $\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)]$ establishes the exact finite coordinate, gauge-orbit, and compensating transformation identities on active bonds $\mathbb{B}_0$, but does not prove uniform summability $\sum_\alpha \mathcal{I}_\alpha$ over the infinite family of polymer histories under the multiscale cluster expansion.
  2. The bound $\|K_j^{(1)}\|_{B_j} \le C_j$ across all RG scales $j = 0, \dots, n$ remains the first unresolved bridge lemma (`MULTISCALE_MARKED_POLYMER_ACTIVITY_SUMMABILITY_OPEN`).
  3. Classification: `METHOD_SPECIFIC_OBSTRUCTION`; structural no-go count remains 0; no continuum edge closes.


## NEG-YM-051R-TREE-CHART-AND-ADJOINT-CONFLATION: Conflation of Adjoint Background Covariance with Tree-Gauge Fixing and Unconditioned Chart Delta (`YM-051R`)

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether adjoint conjugation $B^\prime \mapsto u_0 B^\prime u_0^{-1}$ can zero out tree fluctuations, whether group Haar tree-gauge integration directly yields an unconditioned Lie-algebra delta on restricted coordinates, and whether the single-term representation closes without conditional chart and cutoff bounds.
- **Result:** Falsified.
  1. Adjoint conjugation is an inner automorphism preserving Frobenius norm: $\|u_0 B^\prime u_0^{-1}\|_F = \|B^\prime\|_F$. For non-zero $B^\prime \ne 0$, $\|u_0 B^\prime u_0^{-1} - 0\|_F = \|B^\prime\|_F > 0$; it can NEVER zero out a fluctuation. Adjoint covariance governs background AL mixture transformation, whereas tree-gauge fixing requires solving the affine parallel transport equation $h_y = V_0(b)^{-1} h_x \exp(i B^\prime(b)) V_0(b)$ along tree edges. Conflating the two was a defect that must be decoupled.
  2. Group Haar measure on tree bonds integrates over compact $SU(2)^{T_0}$ with volume 1 and no boundaries. The Lie algebra delta $\prod_{b \in T_0} \delta(B^\prime(b))$ is defined on an open coordinate chart with cutoff $\chi^\prime$. Replacing group tree gauge by Lie algebra delta on restricted coordinates is strictly conditional on the orbit remaining within chart boundaries $\|B^\prime\| < \delta_k^\prime$.
  3. The actual-model Bałaban coordinate pullback and tree-gauge representation are formally reclassified as `CONDITIONAL_AND_OPEN` (`ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_TREE_GAUGE_CONDITIONAL_AND_OPEN`).
  4. Classification: `METHOD_SPECIFIC_OBSTRUCTION`; structural no-go count remains 0; no continuum edge closes.


## NEG-YM-051R2-UNIT-QUATERNION-AND-OBSERVABLE-DEFECT: Non-Unit Quaternion Approximations, Single-Edge Tree Inadequacy, Scalar Heuristics, and Premature Summability Scope (`YM-051R2`)

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether non-unit quaternion approximations, single-edge parallel transport, scalar plaquette values, or unconditioned continuum heuristics can certify SU(2) lattice gauge invariance, tree gauge on rooted trees, and physical observable non-factorization; and whether uniform polymer activity summability can be pursued before resolving the conditional chart-admissibility lemma for actual Bałaban histories.
- **Result:** Falsified.
  1. Non-unit quaternions such as $(1, 0, 1/3, 0)$ (norm squared 10/9) and second-order Taylor truncations $(1 - 1/8, 1/2, 0, 0)$ (norm squared 65/64) do not belong to $SU(2)$. Inversion algebra in non-zero quaternions cannot certify an allowed site gauge transformation. Certification requires exact rational unit quaternions ($\|q\|^2 = 1$) via Pythagorean quadruples.
  2. Single-link parallel transport fails to certify tree-gauge fixing across a multi-edge tree; tree-gauge fixing must be sequentially resolved across a non-trivial rooted multi-edge tree $T_0$, proving that all tree links simultaneously fix to background transporters $V_0(b)$, while non-tree cycle bonds retain non-trivial holonomy and naive uncoupled transformations fail.
  3. A scalar plaquette value $\ne 1$ or hardcoded heuristic (e.g. 135/1000) does not prove observable non-factorization across spatial boundaries; non-factorization requires demonstrating a non-zero cross-variation determinant $\Delta_{\mathrm{fact}} \ne 0$ for an explicit observable coupling regions $Z_h$ and $\Lambda_0$, and establishing discrete lattice gradient-flow mixing.
  4. Hermitian vs. anti-Hermitian Lie algebra conventions must be rigorously reconciled: Hermitian generators ($B^\prime$, $\operatorname{Tr}((B^\prime)^2) \ge 0$, $\exp(i B^\prime)$) versus anti-Hermitian generators ($X$, $\operatorname{Tr}(X^2) \le 0$, $\exp(X)$), and signed determinant $\det(D_{V_0}) = +1$ versus absolute Jacobian $|\det(D_{V_0})| = 1$.
  5. The actual R-I pullback remains `CONDITIONAL_AND_OPEN`. Uniform multiscale polymer activity summability is conditionally blocked by Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` (Small-Field Chart Stability and Remainder Activity Bound) and cannot be claimed as the immediate next dependency-satisfied obligation.
  6. Classification: `METHOD_SPECIFIC_OBSTRUCTION`; structural no-go count remains 0; no continuum edge closes.


## NEG-YM-051R3-SOURCE-LOCATOR-AND-ILL-POSED-CHART-LEMMA: Source Citation Conflation, Domain Equality Failure, Signed Orientation Determinant, and Ill-Posed Probabilistic Chart Lemma (`YM-051R3`)

- **Discovery Date:** 2026-10-09
- **Epistemic Classification:** `[METHOD_SPECIFIC_OBSTRUCTION]`
- **Hypothesis tested:** Whether Bałaban R-I is cited from CMP 109 (1987); whether $\Lambda_0$ equals $\Lambda \setminus Z_h$; whether the 4-site graph in Test 11 represents an admissible hypercubic lattice history; whether directional derivative determinant $\det(D_{V_0}) = +1$ is universally orientation-independent; whether Euler flow staple dependence proves exact physical flowed observable non-factorization at finite flow time; and whether a Haar measure probability estimate $\mathcal{O}(e^{-c/g^2})$ for gauge orbit chart exit is well-posed as the first source-required bridge lemma.
- **Result:** Falsified.
  1. Primary-Source Citation: Bałaban R-I is *Large Field Renormalization. I. The Basic Step of the Renormalization Group*, Communications in Mathematical Physics 122, 175–202 (1989), NOT CMP 109 (1987) pp. 193–198. The citation in YM-051R2 was erroneous and is formally superseded. Direct page/equation locators are in CMP 122 Section 1 (pp. 180–202).
  2. Domain Equality: $\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c$ (CMP 122 p. 195). Because $Z_h^{\prime \sim}$ is an enlarged regularized neighborhood of $Z_h$, $\Lambda_0 \subsetneq \Lambda \setminus Z_h$. The collar region $Z_h^{\prime \sim} \setminus Z_h$ carries constraints and boundary fields; assuming $\Lambda_0 = \Lambda \setminus Z_h$ is false.
  3. Scoping of Finite Graph: The 4-site unit quaternion graph in Test 11 contains non-tree cycle edge $((2, 0), (0, 1))$ of length $\sqrt{5}$, which is a diagonal non-hypercubic jump. It is strictly scoped as a toy finite graph certificate, NOT an admissible hypercubic lattice history.
  4. Orientation Sign: Directional derivative operator on child site along parent-to-child edge is $- \operatorname{Ad}_{V_0(b)}$. On 3-dimensional $\mathfrak{su}(2)$, $\det(-\operatorname{Ad}_{V_0}) = (-1)^3 (+1) = -1$. The signed determinant $\det(D_{V_0}) = (-1)^k$ depends on edge orientation and variable ordering; claiming $\det(D_{V_0}) = +1$ universally is false. In contrast, the absolute Jacobian $|\det(D_{V_0})| = 1$ is universally robust.
  5. Flowed Observable Scoping: Euler staple mixing does not prove non-factorization for the non-perturbative physical flowed observable at finite $t_{\mathrm{phys}} > 0$. The toy cross-defect $\Delta_{\mathrm{fact}} = -16/25 \ne 0$ is strictly a toy algebraic certificate on open links. Physical flowed observable non-factorization across spatial boundaries remains `PHYSICAL_FLOWED_OBSERVABLE_NON_FACTORIZATION_OPEN`.
  6. Ill-Posed Chart Lemma Refutation: Haar measure on $SU(2)$ has no $g$-dependence; an $\mathcal{O}(e^{-c/g^2})$ tail cannot be acquired under Haar measure without the Wilson action. Original cutoff $(1 - \chi^\prime)$ and tree-gauge chart exit are not identical events. Constants and norms were undefined. Speculative probabilistic lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` is formally refuted and replaced by the purely deterministic lemma **LEMMA `YM-051F-DETERMINISTIC-CHART-OVERLAP`** (Deterministic Small-Field Chart Overlap and Remainder Decomposition). Any weighted-measure tail estimate is a distinct subsequent obligation conditionally blocked by deterministic chart overlap.
  7. Classification: `METHOD_SPECIFIC_OBSTRUCTION`; structural no-go count remains 0; no continuum edge closes.


