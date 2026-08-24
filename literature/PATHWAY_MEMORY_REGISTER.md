# PATHWAY MEMORY REGISTER (CONSTRUCTIVE & RG ERA 1980–2000)

## Overview
This register records the historical trajectory, central theses, proven boundaries, failure points, surviving machinery, closure reasons, and reopen conditions for each major constructive program attempting 4D Yang–Mills existence and mass gap generation.

---

### PATH-CONST-001: Göpfert–Mack 3D Abelian Confinement Program
- **PROGRAM_ID:** `PATH-CONST-001`
- **PRIMARY_PAPERS:** `PAPER-CONST-001` (Göpfert & Mack 1981)
- **CENTRAL_THESIS:** Static quark confinement and dynamical mass generation can be proved rigorously for all coupling values via exact monopole gas representation and Debye screening on a 3D lattice.
- **DIRECTION:** Non-perturbative duality transformation of 3D lattice $U(1)$ Villain action to integer-valued topological current configurations (Coulomb / sine-Gordon plasma).
- **WHAT_SUCCEEDED:** Complete mathematical proof that string tension $\sigma > 0$ for all $g^2$; controlled continuum limit with fixed physical Debye mass $m_D > 0$ converging to a massive scalar field.
- **WHAT_FAILED:** Extension to 4D spacetime and non-Abelian gauge groups. In 4D, monopoles are string-like worldsheets rather than localized point particles, and the dual Abelian representation does not capture non-Abelian self-interactions.
- **WHAT_SURVIVED:** Rigorous polymer expansion techniques for Coulomb plasmas, sine-Gordon duality maps, and benchmark proof that topology can generate a mass gap in lower dimensions.
- **CLOSURE_REASON:** Solved completely for 2+1D $U(1)$; fundamentally exhausted regarding 4D non-Abelian Yang–Mills due to dimensional and group-theoretic barriers.
- **REOPEN_CONDITIONS:** Only if a non-Abelian 4D gauge theory can be rigorously reduced to an effective 3D topological monopole condensation without uncontrolled approximations.
- **OUTCOME_FINGERPRINT:** `SOLVED_LOWER_DIMENSIONAL_ANALOGUE_UNEXTENDABLE_TO_4D`

---

### PATH-CONST-002: Bałaban Multiscale Constructive RG Program
- **PROGRAM_ID:** `PATH-CONST-002`
- **PRIMARY_PAPERS:** `PAPER-CONST-004`, `PAPER-CONST-005`, `PAPER-CONST-006` (Bałaban 1984–1989)
- **CENTRAL_THESIS:** The continuum limit $a 	o 0$ of 4D pure $SU(N)$ lattice Yang–Mills theory can be constructed constructively via an inductive sequence of block-spin renormalization group scale transformations controlling small-field quadratic fluctuations and large-field polymer deviations.
- **DIRECTION:** Multi-scale spatial averaging, axial/covariant gauge fixing on lattice blocks, inductive effective actions, and polymer expansion bounding non-perturbative large-field configurations by $e^{-c / g_k^2}$.
- **WHAT_SUCCEEDED:** Rigorous mathematical proof of Ultraviolet Stability in 4D: uniform bounds on the partition function $Z(a, V)$ as lattice spacing $a 	o 0$ in a fixed finite volume $V < \infty$.
- **WHAT_FAILED:** Infinite-volume thermodynamic limit ($V 	o \infty$) and spectral gap generation in the continuum. As the RG flow descends into the infrared, the running coupling $g_k$ grows large ($g_k \sim 1$), destroying the convergence of both the small-field expansion and the large-field polymer estimates.
- **WHAT_SURVIVED:** The most complete and powerful rigorous mathematical framework for UV gauge-field block-spin RG ever built; rigorous propagator decay bounds under block gauge fixing; polymer convergence criteria.
- **CLOSURE_REASON:** Stopped at the infrared boundary. The program proved UV stability but could not cross the strong-coupling infrared transition to establish infinite-volume clustering and a mass gap.
- **REOPEN_CONDITIONS:** Requires a non-perturbative infrared closure mechanism (e.g. geometric cluster expansion or dual condensation variable) that can take over at the scale where $g_k \sim 1$ and carry the RG flow to $k 	o \infty$.
- **OUTCOME_FINGERPRINT:** `RIGOROUS_UV_STABILITY_PROVED_BLOCKED_AT_INFRARED_BOUNDARY`

---

### PATH-CONST-003: Magnen–Rivasseau–Sénéor Constructive $YM_4$ Program
- **PROGRAM_ID:** `PATH-CONST-003`
- **PRIMARY_PAPERS:** `PAPER-CONST-008` (Magnen, Rivasseau, Sénéor 1993)
- **CENTRAL_THESIS:** 4D Euclidean Yang–Mills Schwinger distributions can be constructed constructively using phase-space cluster expansions with an explicit infrared mass regulator.
- **DIRECTION:** Phase-space multi-scale cluster expansions, tree expansions, Slavnov–Taylor gauge Ward identities, and Borel summation of effective potentials.
- **WHAT_SUCCEEDED:** Rigorous constructive existence of 4D Yang–Mills Schwinger functions with an artificial infrared cutoff $\Lambda_{IR} > 0$ and proof of ultraviolet stability ($a 	o 0$).
- **WHAT_FAILED:** Removal of the infrared cutoff ($\Lambda_{IR} 	o 0$). In the absence of an a priori proved mass gap $\Delta > 0$, the removal of $\Lambda_{IR}$ generates infrared renormalon divergences and unbounded long-distance fluctuations.
- **WHAT_SURVIVED:** Modern constructive phase-space multi-scale cluster expansions; rigorous integration of Slavnov–Taylor identities into constructive bounds.
- **CLOSURE_REASON:** Circularity barrier: removing the IR cutoff requires knowing the theory has an isolated vacuum and a mass gap $\Delta > 0$, but the mass gap cannot be established without controlling the non-perturbative infrared measure.
- **REOPEN_CONDITIONS:** Development of a non-perturbative mechanism that establishes a uniform spectral gap $\Delta(\Lambda_{IR}) \ge \Delta_0 > 0$ uniformly as $\Lambda_{IR} 	o 0$.
- **OUTCOME_FINGERPRINT:** `CONSTRUCTIVE_UV_EXISTENCE_ESTABLISHED_BLOCKED_BY_IR_RENORMALONS`

---

### PATH-CONST-004: Federbush Constructive Gauge Phase-Cell Program
- **PROGRAM_ID:** `PATH-CONST-004`
- **PRIMARY_PAPERS:** `PAPER-CONST-007` (Federbush 1986–1988)
- **CENTRAL_THESIS:** Yang–Mills lattice stability can be streamlined via phase-cell cluster expansions and master inequalities for non-Abelian link variables.
- **DIRECTION:** Phase-cell spatial decomposition and multi-scale block inequalities.
- **WHAT_SUCCEEDED:** Alternative derivation of local block stability and master inequalities for link variables.
- **WHAT_FAILED:** Did not overcome the fundamental infrared barrier in 4D infinite volume.
- **WHAT_SURVIVED:** Elegant master inequalities for link variables and gauge cluster techniques.
- **CLOSURE_REASON:** Merged conceptually into the broader Bałaban/Magnen–Rivasseau constructive consensus without providing a breakthrough in the infrared.
- **REOPEN_CONDITIONS:** N/A (subsumed by phase-space constructive RG).
- **OUTCOME_FINGERPRINT:** `ALTERNATIVE_UV_METHOD_CONVERGED_TO_COMMON_IR_BARRIER`
