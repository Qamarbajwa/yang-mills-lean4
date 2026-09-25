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
