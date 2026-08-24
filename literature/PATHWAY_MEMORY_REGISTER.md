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
- **REOPEN_CONDITIONS:** `[PROJECT_SYNTHESIS]` Application of phase-cell master inequalities to non-perturbative infrared block measures.
- **OUTCOME_FINGERPRINT:** `ALTERNATIVE_UV_METHOD_CONVERGED_TO_COMMON_IR_BARRIER`
