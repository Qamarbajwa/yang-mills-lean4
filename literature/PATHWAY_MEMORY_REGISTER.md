# PATHWAY MEMORY REGISTER

## 1. Governance & Epistemic Taxonomy

Every pathway entry in this register documents a distinct mathematical or physical attempt to construct 4D Yang–Mills theory or prove the existence of a non-zero mass gap $\Delta > 0$.

### Epistemic Classification Prefixes
Every claim, result, and limitation recorded in this register is strictly tagged with one of the following epistemic classifications:
- `[PRIMARY_SOURCE_RESULT]`: A theorem, bound, or exact formula rigorously established within the primary paper itself.
- `[PRIMARY_SOURCE_LIMITATION]`: A scope restriction, failure, or open problem explicitly acknowledged by the original authors in the primary source text.
- `[LATER_LITERATURE_LIMITATION]`: An obstruction, divergence, or correction identified by subsequent peer-reviewed literature.
- `[PROJECT_SYNTHESIS]`: A comparative structural analysis, cross-pathway synthesis, or dimensional mapping developed within this research project.
- `[HYPOTHESIS]`: A testable conjecture formulated to bridge identified gaps between known results.
- `[UNKNOWN]`: An open mathematical question with no definitive resolution established in primary or secondary literature.

### Permanent Invariants
1. `FAILED_EXPERIMENT != FALSIFIED_PATHWAY` (A failed attempt or parameter breakdown does not prove the conceptual pathway is impossible).
2. `NO_KNOWN_EXTENSION != PROVED_NONEXTENDABILITY` (Absence of a known mathematical extension must never be promoted to an impossibility theorem without a rigorous no-go proof).
3. `SOURCE_STATED_LIMITATION != PROJECT_SYNTHESIS` (Authors' own scope caveats must be distinguished from later project interpretations).
4. `DORMANT_PATHWAY != SCIENTIFICALLY_DEAD_PATHWAY` (An active line of inquiry that ceased due to technical complexity remains dormant, not disproved).
5. `PROJECT_REGISTER != PRIMARY_LITERATURE_SOURCE` (Internal screening registers must not be classified as primary literature).
6. `OFFICIAL_STATUS != MATHEMATICAL_THEOREM` (Institutional governance status is an invariant, not a mathematical theorem).
7. `MARKOV_PROCESS_CONSTRUCTION != INVARIANT_MEASURE_PROOF` (Constructing the stochastic Markov dynamic is mathematically distinct from proving that a given measure is its unique invariant measure).
8. `2D_STOCHASTIC_YM != 3D_STOCHASTIC_YMH` (2D pure YM Langevin dynamics is distinct from 3D YMH singular flow).
9. `LOCAL_STOCHASTIC_FLOW != INVARIANT_QFT_MEASURE` (Local-in-time existence does not imply construction of an invariant Euclidean measure).
10. `LARGE_N_RESULT != FINITE_N_RESULT` (Planar $N=\infty$ bounds must not be conflated with finite-$N$ non-planar theorems).
11. `PREPRINT_YEAR != JOURNAL_PUBLICATION_YEAR` (Bibliographic metadata must distinguish preprint appearance from official journal publication).
12. `DISTINCT_PAPER != SAME_THEOREM_RECORD` (Separate independent papers must receive distinct primary literature records and theorem entries).
13. `LATTICE_STRONG_COUPLING_MASS_GAP != CONTINUUM_4D_CLAY_MASS_GAP` (A rigorous lattice mass gap at strong coupling $\beta < \beta_0$ does not equal the continuum weak-coupling Clay mass gap).
14. `AREA_LAW != CLAY_SPECTRAL_MASS_GAP` (Wilson area law and string tension on discrete lattices do not establish the continuum Hamiltonian spectral gap).
15. `UNIQUENESS_OF_GAUGE_COVARIANT_MASS_RENORMALISATION != UNQUALIFIED_RENORMALISATION_SCHEME_INDEPENDENCE` (Proving uniqueness of the mass counterterm required for gauge covariance does not constitute an unqualified renormalization scheme-independence for arbitrary non-local regularizations).

---

## 2. Program Pathways

### PATH-CONST-001: Göpfert–Mack 3D Abelian Confinement Program
- **PROGRAM_ID:** `PATH-CONST-001`
- **PRIMARY_PAPERS:** `PAPER-CONST-001` (Göpfert & Mack 1981, *Comm. Math. Phys.* 82, 545–590)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Static quark confinement and dynamical mass generation can be proved rigorously for all coupling values via exact monopole gas representation and Debye screening on a 3D lattice.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Non-perturbative duality transformation of 3D lattice $U(1)$ Villain action to integer-valued topological current configurations (Coulomb / sine-Gordon plasma).
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Complete mathematical proof that string tension $\sigma > 0$ for all $g^2$; controlled continuum limit with fixed physical Debye mass $m_D > 0$ converging to a free massive scalar field (*CMP* 82, pp. 545–590, Theorems 1–3).
- **WHAT_IS_DIFFERENT_IN_4D:** `[PROJECT_SYNTHESIS]`
  1. *Geometric / Topological Structure:* In 3D Euclidean spacetime, magnetic monopoles are localized point charges (0D events). In 4D Euclidean spacetime, magnetic monopoles are localized particles whose trajectories form 1D closed worldlines / current loops ($j_\mu = \frac{1}{2}\epsilon_{\mu\nu\rho\sigma}\partial_\nu F_{\rho\sigma}$), while Dirac strings form 2D surfaces / sheets (Dirac sheets) bounded by the monopole loops.
  2. *Algebraic Structure:* Abelian duality in 3D relies on Hodge star mapping of 2-form curvature $F$ to a 1-form dual field ($*F = d\chi$); in 4D non-Abelian Yang–Mills, the non-linear self-interaction $[A_\mu, A_\nu]$ obstructs a direct scalar dual transformation.
- **WHAT_IS_NOT_ESTABLISHED:** `[PROJECT_SYNTHESIS]` No mathematical impossibility theorem proves that monopole condensation cannot drive confinement in 4D; however, no rigorous continuum construction of 4D non-Abelian confinement from monopole current loops has been achieved.
- **CLOSURE_REASON:** `[PRIMARY_SOURCE_LIMITATION]` Solved completely for 2+1D $U(1)$ Villain lattice model; authors did not extend the method to 4D or non-Abelian groups.
- **BRIDGE_VARIABLES:** `lattice spacing a`, `coupling g`, `Debye mass m_D`, `string tension sigma`, `dimension d = 3`
- **FAILURE_LOCALITY:** `wrong dimension/theory (3D Abelian / Hodge star scalar duality)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Rigorous mathematical formulation of 4D non-Abelian dual Abelian projection or non-Abelian monopole current loop cluster expansions without uncontrolled truncations.
- **OUTCOME_FINGERPRINT:** `SOLVED_LOWER_DIMENSIONAL_ABELIAN_ANALOGUE_NO_DIRECT_EXTENSION_ESTABLISHED_TO_4D_NONABELIAN_YM`

---

### PATH-CONST-002: Bałaban Multiscale Constructive RG Program
- **PROGRAM_ID:** `PATH-CONST-002`
- **PRIMARY_PAPERS:** `PAPER-CONST-004`, `PAPER-CONST-005`, `PAPER-CONST-006` (Bałaban 1984–1989, *CMP* 95, 96, 98, 109, 114, 115, 116, 119)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` The continuum limit $a \to 0$ of 4D pure $SU(N)$ lattice Yang–Mills theory can be constructed constructively via an inductive sequence of block-spin renormalization group scale transformations controlling small-field quadratic fluctuations and large-field polymer deviations.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Multi-scale spatial averaging, axial/covariant gauge fixing on lattice blocks, inductive effective actions, and polymer expansions bounding non-perturbative large-field configurations by $e^{-c / g_k^2}$.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous mathematical proof of Ultraviolet Stability in 4D: uniform bounds on the partition function $Z(a, V)$ as lattice spacing $a \to 0$ in a fixed finite volume $V < \infty$ (*CMP* 116, pp. 1–22; *CMP* 119, pp. 243–285).
- **WHAT_FAILED_OR_REMAINED_OPEN:**
  - *Primary Source Fact:* `[PRIMARY_SOURCE_LIMITATION]` The small-field inductive condition ($|F_P| < \epsilon$) and asymptotically free coupling ($g_k \ll 1$) apply at high energies / ultraviolet scales. In a finite volume $V < \infty$, the number of RG steps is bounded, preserving small-field control (*CMP* 109, p. 250).
  - *Later Literature Assessment:* `[LATER_LITERATURE_LIMITATION]` In the infinite-volume limit ($V \to \infty$), the RG flow must continue indefinitely into the infrared where the running coupling grows large ($g_k \sim 1$), causing the small-field inductive series and large-field polymer estimates to lose convergence (Jaffe & Witten 2000, Section 3; Rivasseau 1991).
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Definitive mathematical technology for UV gauge-field block-spin RG; rigorous propagator decay bounds under block gauge fixing; polymer convergence criteria in constructive field theory.
- **CLOSURE_REASON:** `[PRIMARY_SOURCE_LIMITATION]` Stopped at the finite-volume ultraviolet boundary. The infinite-volume thermodynamic limit with a mass gap was not constructed.
- **BRIDGE_VARIABLES:** `lattice spacing a`, `volume V`, `running coupling g_k`, `small-field radius epsilon`, `correlation length xi`
- **FAILURE_LOCALITY:** `infinite volume / IR (strong-coupling transition g_k ~ 1)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Development of a non-perturbative infrared closure mechanism (e.g. geometric cluster expansion or dual condensation variable) that can match with Bałaban's small-field effective action at scale $g_k \sim 1$ and control the infrared flow.
- **OUTCOME_FINGERPRINT:** `RIGOROUS_UV_STABILITY_PROVED_BLOCKED_AT_INFRARED_BOUNDARY`

---

### PATH-CONST-003: Magnen–Rivasseau–Sénéor Constructive $YM_4$ Program
- **PROGRAM_ID:** `PATH-CONST-003`
- **PRIMARY_PAPERS:** `PAPER-CONST-008` (Magnen, Rivasseau, Sénéor 1993, *Comm. Math. Phys.* 155, 325–383)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` 4D Euclidean Yang–Mills Schwinger distributions can be constructed constructively using phase-space cluster expansions in the presence of an infrared cutoff.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Phase-space multi-scale cluster expansions, tree expansions, Slavnov–Taylor gauge Ward identities, and Borel summation of effective potentials (*CMP* 155, pp. 327–335).
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous constructive existence of 4D Yang–Mills Schwinger functions with an artificial infrared cutoff $\Lambda_{IR} > 0$ (such as finite volume or mass regulator) and proof of ultraviolet stability as $a \to 0$ (*CMP* 155, pp. 325–383, Theorems 1–4).
- **WHAT_FAILED_OR_REMAINED_OPEN:**
  - *Primary Source Statement:* `[PRIMARY_SOURCE_LIMITATION]` MRS explicitly state on p. 326: *"The removal of the infrared cutoff... is the main open problem of constructive gauge theories."* They do not claim to construct the limit $\Lambda_{IR} \to 0$.
  - *Literature / Project Assessment:* `[LATER_LITERATURE_LIMITATION]` / `[PROJECT_SYNTHESIS]` In constructive field theory literature (e.g., Rivasseau 1991, *From Perturbative to Constructive Renormalization*), removing an IR cutoff in non-Abelian gauge theory without an established mass gap is obstructed by infrared renormalon singularities and uncontrolled long-distance vacuum fluctuations.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Modern constructive phase-space multi-scale cluster expansions; rigorous integration of Slavnov–Taylor identities into constructive analytical bounds.
- **CLOSURE_REASON:** `[PRIMARY_SOURCE_LIMITATION]` Completed the construction with an IR cutoff; removal of the cutoff remains open.
- **BRIDGE_VARIABLES:** `lattice spacing a`, `IR cutoff Lambda_IR`, `spectral gap Delta`, `Borel parameter`
- **FAILURE_LOCALITY:** `IR (cutoff removal Lambda_IR -> 0 without mass gap)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Constructive proof of a uniform non-zero spectral gap $\Delta(\Lambda_{IR}) \ge \Delta_0 > 0$ that remains bounded away from zero uniformly as $\Lambda_{IR} \to 0$.
- **OUTCOME_FINGERPRINT:** `CONSTRUCTIVE_UV_EXISTENCE_ESTABLISHED_IR_CUTOFF_REMOVAL_OPEN`

---

### PATH-CONST-004: Federbush Constructive Gauge Phase-Cell Program
- **PROGRAM_ID:** `PATH-CONST-004`
- **PRIMARY_PAPERS:** `PAPER-CONST-007` (Federbush 1986–1988, *CMP* 107, 319–329; *CMP* 114, 317–343)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Yang–Mills lattice stability can be established via phase-cell cluster expansions and master inequalities for non-Abelian link variables.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Phase-cell spatial decomposition and multi-scale block inequalities.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Alternative rigorous derivation of local block stability and master inequalities for link variables on lattices (*CMP* 107, 319; *CMP* 114, 317).
- **WHAT_FAILED_OR_REMAINED_OPEN:** `[PRIMARY_SOURCE_LIMITATION]` Operates in bounded spatial domains; does not construct the 4D infinite-volume continuum limit with a mass gap.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Master inequalities for link variables and block localization techniques.
- **CLOSURE_REASON:** `[PRIMARY_SOURCE_LIMITATION]` Established block inequalities; did not pursue full infinite-volume infrared construction.
- **BRIDGE_VARIABLES:** `lattice spacing a`, `phase-cell size L`, `link variable bounds`, `volume V`
- **FAILURE_LOCALITY:** `infinite volume / IR`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Application of phase-cell master inequalities to non-perturbative infrared block measures.
- **OUTCOME_FINGERPRINT:** `ALTERNATIVE_UV_METHOD_CONVERGED_TO_COMMON_IR_BARRIER`

---

### PATH-MOD-001: 2D Stochastic Yang–Mills Dynamic & Invariant Measure Pathway
- **PROGRAM_ID:** `PATH-MOD-001`
- **PRIMARY_PAPERS:** `PAPER-MOD-001` (Chandra, Chevyrev, Hairer, Shen 2022, *Publ. Math. IHÉS* 136, 1–147), `PAPER-MOD-002` (Chevyrev & Shen 2026, *CPAM* 79, 1973–2102)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` The 2D Euclidean Yang–Mills measure can be dynamically realized as the unique invariant measure of a singular Langevin SPDE on the torus $\mathbb{T}^2$ for any connected compact Lie group $G$.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Distributional connection state space, regularity structures on 2D gauge orbits, Langevin Markov process construction, and Dirichlet form uniqueness analysis.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Complete mathematical proof of global existence of the Langevin dynamic (*IHÉS* 2022) and rigorous proof of the uniqueness of the 2D Yang–Mills invariant measure on $\mathbb{T}^2$ (*CPAM* 2026).
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]` Extension to higher dimensions (3D/4D) where gauge theories possess propagating transverse gluons and non-trivial scattering states.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` Specifically restricted to 2D spacetime where pure Yang–Mills has zero local propagating degrees of freedom.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` Solved completely in 2D; serves as a rigorous proof-of-concept for dynamic stochastic quantization on gauge orbits.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Gauge-orbit metric space construction and stochastic Langevin quantization formalism.
- **BRIDGE_VARIABLES:** `mollifier scale epsilon`, `gauge orbit metric d_orbit`, `dimension d = 2`, `invariant measure mu_YM`
- **FAILURE_LOCALITY:** `wrong dimension/theory (2D / no transverse gluons)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Extension of invariant measure techniques to subcritical 3D and critical 4D gauge systems.
- **OUTCOME_FINGERPRINT:** `SOLVED_2D_STOCHASTIC_LANGEVIN_INVARIANT_MEASURE`

---

### PATH-MOD-002: 3D Singular Stochastic Yang–Mills–Higgs Flow Pathway
- **PROGRAM_ID:** `PATH-MOD-002`
- **PRIMARY_PAPERS:** `PAPER-MOD-003` (Chandra, Chevyrev, Hairer, Shen 2024, *Invent. Math.* 237, 85–236), `PAPER-MOD-004` (Chevyrev & Shen 2026, *ARMA* 250, art. 11)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Singular SPDEs can be renormalized in a gauge-covariant manner to yield a local-in-time Markov process on 3D gauge orbits.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` 3D regularity structures, gauge-covariant mollification, local-in-time flow, and unique gauge-covariant mass renormalization analysis.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous construction of local-in-time 3D stochastic Yang–Mills–Higgs flow, canonical Markov diffusion on gauge orbits (*Invent. Math.* 237, pp. 541–696), and proof of uniqueness of the gauge-covariant mass renormalization (*ARMA* 250, art. 11).
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]`
  - *Primary Source Fact:* `[PRIMARY_SOURCE_LIMITATION]` Authors explicitly state (*Invent. Math.* 237, p. 543) that the construction of an invariant measure in 3D remains an open problem.
  - *Dimensional Barrier:* `[PRIMARY_SOURCE_LIMITATION]` In 4D, stochastic Yang–Mills is critically singular and outside current parabolic SPDE theory.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` Construction is local in time; invariant measure existence in 3D is open.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` Establishes local dynamic stochastic quantization in 3D; stopping short of invariant equilibrium measures or 4D critical flow.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Regularity structure models for non-Abelian gauge-Higgs fields and gauge-covariant mass counterterm classification theorems.
- **BRIDGE_VARIABLES:** `mollifier scale epsilon`, `gauge orbit metric d_orbit`, `dimension d = 3`, `stochastic time t`, `blow-up time tau`
- **FAILURE_LOCALITY:** `wrong dimension/theory (3D / local flow only / invariant measure open)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Proof of global-in-time non-explosion and construction of 3D invariant Gibbs measure; developing critical SPDE methods for 4D.
- **OUTCOME_FINGERPRINT:** `SOLVED_3D_LOCAL_STOCHASTIC_FLOW_INVARIANT_MEASURE_OPEN_4D_CRITICAL_OPEN`

---

### PATH-MOD-003: Modern Non-Perturbative Lattice Bootstrap Pathway
- **PROGRAM_ID:** `PATH-MOD-003`
- **PRIMARY_PAPERS:** `PAPER-MOD-005` (Kazakov & Zheng 2023, *Phys. Rev. D* 107, L051501), `PAPER-MOD-006` (Kazakov & Zheng 2025, *JHEP* 2025, art. 99)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Combining Makeenko–Migdal loop equations with positive semidefiniteness of Wilson loop Gram matrices yields rigorous upper and lower bounds on lattice observables and string tension at large $N$ and finite $N$.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Exact lattice loop equations, reflection positivity, trace identities, and semidefinite programming (SDP) relaxations.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous numerical/analytical bounds on plaquette energies and string tensions on discrete lattices for $SU(\infty)$ and $SU(2)$ without Monte Carlo sampling errors.
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]` Rigorous analytical continuum limit $a \to 0$. In SDP bootstrap, taking $a \to 0$ requires loops of arbitrarily large perimeter ($L_{max} \to \infty$), where truncated SDP constraints lose closure.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` Results are obtained on a discrete lattice at fixed coupling $\beta$; continuum scaling requires infinite loop size truncations.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` The bootstrap provides powerful rigorous inequalities on lattice correlation functions, offering rigorous non-perturbative lower bounds that could potentially bound the spectral gap away from zero if loop-space scaling is controlled.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Semidefinite matrix positivity constraints on Wilson loop spaces and exact Makeenko–Migdal lattice representations.
- **BRIDGE_VARIABLES:** `lattice coupling beta`, `loop perimeter C`, `bootstrap truncation L_max`, `gauge group SU(N)`
- **FAILURE_LOCALITY:** `continuum limit (infinite loop truncation)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Analytic proof of a uniform positive lower bound on string tension / spectral gap that survives the $L_{max} \to \infty$ and $a \to 0$ limits simultaneously.
- **OUTCOME_FINGERPRINT:** `RIGOROUS_LATTICE_BOUNDS_OBTAINED_CONTINUUM_BOOTSTRAP_LIMIT_UNRESOLVED`

---

### PATH-MOD-004: Rigorous Infinite-Volume Lattice Strong-Coupling Mass Gap Pathway
- **PROGRAM_ID:** `PATH-MOD-004`
- **PRIMARY_PAPERS:** `PAPER-MOD-007` (Shen, Zhu, Zhu 2023, *CMP* 400, 805–851), `PAPER-MOD-008` (Cao, Nissim, Sheffield 2025, *arXiv:2505.16585*), `PAPER-MOD-009` (Cao, Nissim, Sheffield 2025, *arXiv:2509.04688*)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` In the infinite-volume lattice limit at strong coupling ($\beta < \beta_0$), Yang–Mills theory satisfies uniform Poincaré and log-Sobolev inequalities, yielding exponential correlation decay, a strictly positive lattice mass gap $\Delta_{lat}(\beta) > 0$, and area-law bounds in 't Hooft regimes.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Infinite-volume lattice Gibbs measures, Glauber/Langevin dynamic functional inequalities, and dynamical mass-gap bounds for Wilson loops.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous proof of infinite-volume Gibbs measure existence, uniform Poincaré/log-Sobolev inequalities, exponential correlation decay in 2D, 3D, and 4D at strong coupling ($\beta < \beta_0$), and area-law bounds in 't Hooft regimes for $U(N), SU(N), SO(2N)$.
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]`
  - *Coupling Barrier:* `[PRIMARY_SOURCE_LIMITATION]` The bounds are strictly restricted to strong coupling ($\beta < \beta_0$) or discrete lattice 't Hooft regimes.
  - *Continuum Transition:* `[PRIMARY_SOURCE_LIMITATION]` Asymptotic freedom requires taking the continuum limit along the weak-coupling trajectory ($\beta \to \infty, g \to 0, a \to 0$), where strong-coupling functional inequalities lose uniformity.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` Results hold on discrete lattices at fixed spacing $a > 0$; area law and lattice mass gap do not prove the continuum Clay mass gap.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` This provides a definitive modern benchmark for the lattice mass gap at strong coupling. The essential missing bridge for the Clay Millennium problem is connecting this strong-coupling mass gap to the weak-coupling continuum limit.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Infinite-volume functional inequality techniques on lattice gauge manifolds and dynamical area-law methods.
- **BRIDGE_VARIABLES:** `lattice coupling beta`, `strong-coupling threshold beta_0`, `lattice correlation length xi_lat`, `lattice mass gap Delta_lat`, `lattice spacing a`
- **FAILURE_LOCALITY:** `continuum/weak-coupling trajectory (blocked at beta -> infinity / g -> 0)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Establishing uniform functional inequalities or non-vanishing mass gap estimates along an analytical trajectory extending to the weak-coupling critical point $\beta \to \infty$.
- **OUTCOME_FINGERPRINT:** `RIGOROUS_INFINITE_VOLUME_LATTICE_MASS_GAP_AT_STRONG_COUPLING`

---

### PATH-MOD-005: Nearby Gauge-Higgs Scaling Limits Pathway
- **PROGRAM_ID:** `PATH-MOD-005`
- **PRIMARY_PAPERS:** `PAPER-MOD-010` (Chatterjee 2026, *Probab. Math. Phys.* 7, 339–381)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Rigorous 4D continuum limits with a mass gap can be constructed by studying nearby gauge-scalar models (Yang–Mills–Higgs) under joint parameter scaling.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Lattice $SU(2)$ Yang–Mills–Higgs, unitary gauge transformations, and correlation inequality expansions.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous proof that 4D $SU(2)$ Yang–Mills–Higgs has a continuum scaling limit converging to a massive Gaussian generalized field with an explicit non-zero mass gap.
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]` Constructing pure 4D Yang–Mills without Higgs scalar fields. In the Chatterjee limit, the massive scalar field dominates the measure, forcing Gaussianity (triviality) of the continuum limit.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` The author explicitly states (pp. 339–342) that pure 4D Euclidean Yang–Mills construction is still open and the non-Gaussian interacting limit remains unsolved.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` Nearby theories with Higgs condensation provide massive continuum QFTs, but they achieve mass gaps via the Higgs mechanism (yielding trivial Gaussian limits), bypassing rather than solving non-Abelian confinement.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Rigorous techniques for controlling joint scaling of lattice parameters in 4D gauge-scalar systems.
- **BRIDGE_VARIABLES:** `gauge coupling g`, `Higgs parameter gamma`, `lattice spacing a`, `correlation length xi`
- **FAILURE_LOCALITY:** `nontriviality (Gaussian limit / Higgs-dominated)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Scaling trajectories in parameter space that do not condense the scalar field and preserve non-Gaussian non-Abelian interaction vertices in the limit $a \to 0$.
- **OUTCOME_FINGERPRINT:** `RIGOROUS_MASSIVE_SCALING_LIMIT_ESTABLISHED_LIMIT_IS_GAUSSIAN`
