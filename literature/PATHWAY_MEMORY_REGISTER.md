# PATHWAY MEMORY REGISTER (CONSTRUCTIVE & RG ERA 1980–2000)

## 1. Epistemic Taxonomy & Governing Invariants

Every pathway-memory entry and claim in this register is categorized according to the following strict epistemic taxonomy:

- `[PRIMARY_SOURCE_RESULT]`: Direct mathematical theorem, equation, or bound proved in the cited primary paper.
- `[PRIMARY_SOURCE_LIMITATION]`: Exact boundary, unproved assumption, or scope limitation explicitly stated by the primary authors.
- `[LATER_LITERATURE_LIMITATION]`: Boundary, obstruction, or analysis established in subsequent peer-reviewed literature.
- `[PROJECT_SYNTHESIS]`: Deductive structural synthesis or comparative assessment derived within this project linking established results.
- `[HYPOTHESIS]`: Formally stated conjectural proposal requiring future mathematical proof or refutation.
- `[UNKNOWN]`: Question whose answer cannot be determined with certainty from current evidence.

### Permanent Epistemic Invariants:
1. `FAILED_EXPERIMENT != FALSIFIED_PATHWAY` (A failed attempt or parameter breakdown does not prove the conceptual pathway is impossible).
2. `NO_KNOWN_EXTENSION != PROVED_NONEXTENDABILITY` (Absence of a known mathematical extension must never be promoted to an impossibility theorem without a rigorous no-go proof).
3. `SOURCE_STATED_LIMITATION != PROJECT_SYNTHESIS` (Authors' own scope caveats must be distinguished from later project interpretations).
4. `DORMANT_PATHWAY != SCIENTIFICALLY_DEAD_PATHWAY` (An active line of inquiry that ceased due to technical complexity remains dormant, not disproved).

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

### PATH-MOD-001: Singular SPDE / Stochastic Quantization Pathway
- **PROGRAM_ID:** `PATH-MOD-001`
- **PRIMARY_PAPERS:** `PAPER-MOD-001` (Chandra, Chevyrev, Hairer, Shen 2024), `PAPER-MOD-002` (Chevyrev, Shen 2026)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Non-perturbative Euclidean Yang–Mills measures can be constructed as the unique invariant measures of gauge-covariant singular Langevin stochastic partial differential equations using regularity structures.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Regularity structures on gauge orbit space, gauge-covariant mollification, and stochastic dynamic renormalization.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous local existence, gauge-covariant counterterm uniqueness, and canonical Markov diffusion process on gauge orbit space leaving the Yang–Mills–Higgs measure invariant in 2D and 3D.
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]` Extension to 4D spacetime. In 4D, the Yang–Mills stochastic quantization SPDE is critically singular, where standard regularity structures and dynamic renormalization fail without non-perturbative control.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` Authors explicitly state that 4D pure Yang–Mills stochastic flow is critically singular and outside current parabolic SPDE theory.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` Stochastic quantization provides a rigorous alternative to functional integrals in subcritical dimensions (d < 4), but hits the identical dimensional barrier at d = 4.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Geometric framework of gauge orbit metric spaces, gauge-covariant counterterm classifications, and singular SPDE renormalization machinery.
- **BRIDGE_VARIABLES:** `lattice/mollifier cutoff epsilon`, `gauge orbit metric d_orbit`, `dimension d = 2, 3, 4`, `stochastic time t`
- **FAILURE_LOCALITY:** `wrong dimension/theory (3D / non-critical)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Development of critically singular non-perturbative SPDE techniques capable of controlling 4D gauge-covariant noise without catastrophic UV divergences.
- **OUTCOME_FINGERPRINT:** `SOLVED_LOWER_DIMENSIONAL_STOCHASTIC_GAUGE_FLOW_4D_CRITICAL_OPEN`

---

### PATH-MOD-002: Modern Analytic Lattice Bootstrap Pathway
- **PROGRAM_ID:** `PATH-MOD-002`
- **PRIMARY_PAPERS:** `PAPER-MOD-003` (Kazakov & Zheng 2022, *Phys. Rev. D* 107, 034509)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Non-perturbative lattice Yang–Mills observables and mass gaps can be rigorously bounded from above and below by combining Makeenko–Migdal loop equations with positive semidefiniteness of Wilson loop Gram matrices.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Exact loop equations, reflection positivity constraints, and semidefinite programming (SDP) relaxations at finite $N$ and large $N$.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Analytical and rigorous numerical bounds on plaquette expectation values and string tension on discrete lattices without Monte Carlo sign/statistical errors.
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]` Rigorous analytical continuum limit $a 	o 0$. In SDP bootstrap, taking $a 	o 0$ requires loops of arbitrarily large perimeter ($L_{max} 	o \infty$), causing the truncated bootstrap matrix constraints to lose rigorous closure.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` Results are obtained on a discrete lattice at fixed coupling $eta$; continuum scaling requires infinite loop size truncations.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` The bootstrap provides powerful rigorous inequalities on lattice correlation functions, offering rigorous non-perturbative lower bounds that could potentially bound the spectral gap away from zero if loop-space scaling is controlled.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Semidefinite matrix positivity constraints on Wilson loop spaces and exact Makeenko–Migdal lattice representations.
- **BRIDGE_VARIABLES:** `lattice coupling beta`, `Wilson loop size |C|`, `bootstrap truncation L_max`, `semidefinite matrix spectrum`
- **FAILURE_LOCALITY:** `continuum limit (infinite loop truncation)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Analytic proof of a uniform positive lower bound on string tension / spectral gap that survives the $L_{max} 	o \infty$ and $a 	o 0$ limits simultaneously.
- **OUTCOME_FINGERPRINT:** `RIGOROUS_LATTICE_BOUNDS_OBTAINED_CONTINUUM_BOOTSTRAP_LIMIT_UNRESOLVED`

---

### PATH-MOD-003: Nearby Theory Scaling Limits Pathway
- **PROGRAM_ID:** `PATH-MOD-003`
- **PRIMARY_PAPERS:** `PAPER-MOD-004` (Chatterjee 2024, *arXiv:2401.10507*)
- **CENTRAL_THESIS:** `[PRIMARY_SOURCE_RESULT]` Rigorous 4D continuum limits with a mass gap can be constructed by studying nearby gauge-scalar models (Yang–Mills–Higgs) under joint parameter scaling.
- **DIRECTION:** `[PRIMARY_SOURCE_RESULT]` Lattice $SU(2)$ Yang–Mills–Higgs, unitary gauge transformations, and correlation inequality expansions.
- **WHAT_SUCCEEDED:** `[PRIMARY_SOURCE_RESULT]` Rigorous proof that 4D $SU(2)$ Yang–Mills–Higgs has a continuum scaling limit converging to a massive Gaussian generalized field with an explicit non-zero mass gap.
- **WHAT_REMAINS_OPEN:** `[PRIMARY_SOURCE_LIMITATION]` Constructing pure 4D Yang–Mills without Higgs scalar fields. In the Chatterjee limit, the massive scalar field dominates the measure, forcing Gaussianity (triviality) of the continuum limit.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` The author explicitly states (pp. 1–3) that pure 4D Euclidean Yang–Mills construction is still open and the non-Gaussian interacting limit remains unsolved.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` Nearby theories with Higgs condensation provide massive continuum QFTs, but they achieve mass gaps via the Higgs mechanism (yielding trivial Gaussian limits), bypassing rather than solving non-Abelian confinement.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Rigorous techniques for controlling joint scaling of lattice parameters in 4D gauge-scalar systems.
- **BRIDGE_VARIABLES:** `gauge coupling g`, `Higgs parameter gamma`, `lattice spacing a`, `correlation length xi`
- **FAILURE_LOCALITY:** `nontriviality (Gaussian limit / Higgs-dominated)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Scaling trajectories in parameter space that do not condense the scalar field and preserve non-Gaussian non-Abelian interaction vertices in the limit $a 	o 0$.
- **OUTCOME_FINGERPRINT:** `RIGOROUS_MASSIVE_SCALING_LIMIT_ESTABLISHED_LIMIT_IS_GAUSSIAN`

---

### PATH-MOD-004: Adversarial Claim Audit Pathway (2024–2026 Preprints)
- **PROGRAM_ID:** `PATH-MOD-004`
- **PRIMARY_PAPERS:** `PAPER-MOD-005` (Clay Millennium Invariant 2026), `PAPER-MOD-006` (Adversarial Boundary Register)
- **CENTRAL_THESIS:** `[PROJECT_SYNTHESIS]` External claims asserting full continuum mass gap solutions must be quarantined and subjected to adversarial mathematical audit against Jaffe–Witten requirements.
- **DIRECTION:** `[PROJECT_SYNTHESIS]` Adversarial verification of compactness, non-triviality, Lorentz invariance, and Wightman axioms.
- **WHAT_SUCCEEDED:** `[PROJECT_SYNTHESIS]` Preservation of project integrity against unverified external announcements and strict adherence to Clay Mathematics Institute official standards.
- **WHAT_REMAINS_OPEN:** `[PROJECT_SYNTHESIS]` Execution of systematic adversarial audits on claimed-solution families in task `YM-002E`.
- **SOURCE_STATED_LIMITATION:** `[PRIMARY_SOURCE_LIMITATION]` Clay Mathematics Institute confirms the Millennium Problem remains officially open and unsolved in 2026.
- **PROJECT_SYNTHESIS:** `[PROJECT_SYNTHESIS]` No unrefereed preprint has survived rigorous mathematical scrutiny without identifying unproved compactness assumptions or heuristic truncations.
- **WHAT_SURVIVED:** `[PROJECT_SYNTHESIS]` Formal adversarial audit protocol and negative evidence recording.
- **BRIDGE_VARIABLES:** `claimed continuum mass gap Delta > 0`, `audit criteria`
- **FAILURE_LOCALITY:** `quarantined (external unverified claims)`
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Official peer review acceptance by Clay Mathematics Institute advisory committee.
- **OUTCOME_FINGERPRINT:** `EXTERNAL_CLAIMS_QUARANTINED_SUBJECT_TO_ADVERSARIAL_AUDIT`
