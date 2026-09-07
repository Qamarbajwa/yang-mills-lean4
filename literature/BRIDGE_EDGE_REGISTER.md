# BRIDGE EDGE REGISTER (YM-003)

This ledger contains the authoritative, source-bound records for every edge in the Missing-Bridge Graph.

```yaml
EDGE_ID: E-UV-FREE
SOURCE_NODE: N-REG-LATTICE
TARGET_NODE: N-UV-FREE
MATHEMATICAL_PROPOSITION: >-
  Perturbative 1-loop and 2-loop beta function coefficients are strictly negative (beta_0 = 11N/3 > 0 for SU(N)),
  establishing asymptotic freedom where the effective coupling vanishes logarithmically at high energy scales.
PRIMARY_STATUS: PROVED
STATUS_QUALIFIERS:
  - perturbative
  - weak_coupling_only
  - ultraviolet_only
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: SU(N)
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: FINITE_OR_INFINITE
  CUTOFF_STATE: BARE_REGULATED
  COUPLING_REGIME: WEAK_COUPLING
EXPLICIT_HYPOTHESES:
  - Compact non-Abelian Lie group G
  - Renormalized perturbation theory expansion in powers of g
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: GaugeInvariance
    STATUS: PRESERVED
    DETAIL: Preserved by Wilson lattice action and Faddeev-Popov BRST formulation
  - ASSUMPTION: PerturbativeSmallness
    STATUS: NEW
    DETAIL: Effective coupling g_k must be sufficiently small to justify truncation
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Dimensional transmutation scale Lambda_QCD
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONLESS_COUPLING
  REFERENCE_PHYSICAL_SCALE: k >> Lambda_QCD
  CONTINUUM_SCALING_BEHAVIOR: g^2(k) ~ 1 / (2 beta_0 ln(k / Lambda_QCD))
OBSERVABLE_ALGEBRA: Local gauge-invariant field operators and plaquette Wilson loops
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0003
    CITATION: Gross & Wilczek, Phys. Rev. Lett. 30 (1973) 1343
  - THEOREM_ID: THM-YM-0004
    CITATION: Politzer, Phys. Rev. Lett. 30 (1973) 1346
WHAT_IS_PROVED: Negative sign of leading beta-function coefficient establishing weak-coupling ultraviolet flow.
WHAT_IS_NOT_PROVED: Nonperturbative existence or infrared behavior of the flow when g_k grows large.
BRIDGE_VARIABLES: Running effective coupling g_k and renormalization group scale parameter k.
FAILURE_LOCALITY: Infrared limit k -> Lambda_QCD where perturbation theory breaks down.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: ROUTE_REQUIRED
ROUTE_ID: ROUTE-ASYMPTOTIC-FREEDOM-RG
PROOF_DEPENDENCIES: []
REASON_FOR_STATUS: Proven rigorously within perturbative quantum field theory by Gross-Wilczek and Politzer.
```

```yaml
EDGE_ID: E-UV-FREE-CONT
SOURCE_NODE: N-REG-CUTOFF
TARGET_NODE: N-UV-FREE
MATHEMATICAL_PROPOSITION: >-
  Continuum regularized non-Abelian Yang-Mills with momentum cutoff Lambda exhibits asymptotic freedom
  governed by negative beta function in perturbative expansion.
PRIMARY_STATUS: PROVED
STATUS_QUALIFIERS:
  - perturbative
  - weak_coupling_only
  - continuum_cutoff
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: SU(N)
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: FINITE_OR_INFINITE
  CUTOFF_STATE: CONTINUUM_CUTOFF
  COUPLING_REGIME: WEAK_COUPLING
EXPLICIT_HYPOTHESES:
  - Smooth continuum cutoff Lambda
  - Gauge-fixing via Faddeev-Popov procedure
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: GaugeInvariance
    STATUS: STRENGTHENED
    DETAIL: Requires BRST Slavnov-Taylor identities in continuum gauge-fixed perturbation theory
  - ASSUMPTION: PerturbativeSmallness
    STATUS: PRESERVED
    DETAIL: Valid for g(Lambda) << 1
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Momentum cutoff scale Lambda
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONLESS_COUPLING
  REFERENCE_PHYSICAL_SCALE: Lambda >> Lambda_QCD
  CONTINUUM_SCALING_BEHAVIOR: g^2(Lambda) ~ 1 / (2 beta_0 ln(Lambda / Lambda_QCD))
OBSERVABLE_ALGEBRA: Gauge-invariant polynomials of curvature F_munu
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0002
    CITATION: Faddeev & Popov, Phys. Lett. B 25 (1967) 29
  - THEOREM_ID: THM-YM-0003
    CITATION: Gross & Wilczek (1973)
WHAT_IS_PROVED: Perturbative renormalizability and asymptotic freedom in continuum gauge theory.
WHAT_IS_NOT_PROVED: Nonperturbative continuum existence without cutoffs.
BRIDGE_VARIABLES: Momentum cutoff Lambda and bare coupling g(Lambda).
FAILURE_LOCALITY: Large-field configurations escaping perturbative gauge fixing.
OBSTRUCTION_CANDIDATE: OBS-CAND-002
NECESSITY_CLASS: ROUTE_REQUIRED
ROUTE_ID: ROUTE-CONTINUOUS-RG
PROOF_DEPENDENCIES: []
REASON_FOR_STATUS: Proved rigorously within perturbative continuum QFT.
```

```yaml
EDGE_ID: E-UV-RG
SOURCE_NODE: N-UV-FREE
TARGET_NODE: N-UV-RG-BOUNDS
MATHEMATICAL_PROPOSITION: >-
  Multiscale block-spin renormalization group transformations yield uniform bounds on effective actions
  and stability of the vacuum functional in finite volume for small initial bare coupling.
PRIMARY_STATUS: REGULATED_ONLY
STATUS_QUALIFIERS:
  - finite_volume_only
  - small_field_only
  - constructive_multiscale
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: SU(2), SU(3)
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: FINITE_VOLUME
  CUTOFF_STATE: BLOCK_SPIN_REGULATED
  COUPLING_REGIME: WEAK_COUPLING
EXPLICIT_HYPOTHESES:
  - Finite torus volume V = L^4
  - Small initial bare coupling g_0 < epsilon
  - Multiscale decomposition into small-field and large-field regions
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: FiniteVolume
    STATUS: NEW
    DETAIL: Bounds require periodic finite box V < infinity to control volume accumulation
  - ASSUMPTION: SmallFieldDominance
    STATUS: NEW
    DETAIL: Large-field deviations are bounded by exponential smallness estimates
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Block-spin scale L_k = L^k
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONLESS_ACTION_DENSITY
  REFERENCE_PHYSICAL_SCALE: Small distances x << 1/Lambda_QCD
  CONTINUUM_SCALING_BEHAVIOR: Stable propagation of effective action up to scale index k_max
OBSERVABLE_ALGEBRA: Block-averaged Wilson link variables and gauge-invariant link traces
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0016
    CITATION: Balaban, Commun. Math. Phys. 116 (1988) 1-22
  - THEOREM_ID: THM-YM-0017
    CITATION: Balaban, Commun. Math. Phys. 119 (1988) 243-285
  - THEOREM_ID: THM-YM-0018
    CITATION: Balaban, Commun. Math. Phys. 122 (1989) 175-202
  - THEOREM_ID: THM-YM-0019
    CITATION: Federbush, Commun. Math. Phys. 127 (1990) 433-457
WHAT_IS_PROVED: Rigorous constructive ultraviolet stability and partition function bounds in finite volume.
WHAT_IS_NOT_PROVED: Thermodynamic infinite volume limit or continuation past the crossover scale.
BRIDGE_VARIABLES: Effective coupling g_k at block scale k and multiscale polymer activity.
FAILURE_LOCALITY: Large block scales k where g_k grows of order unity.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: ROUTE_REQUIRED
ROUTE_ID: ROUTE-CONSTRUCTIVE-RG
PROOF_DEPENDENCIES:
  - E-UV-FREE
REASON_FOR_STATUS: Proved in peer-reviewed constructive literature (Balaban, Federbush), but strictly finite-volume and UV-regulated.
```

```yaml
EDGE_ID: E-CROSSOVER
SOURCE_NODE: N-UV-RG-BOUNDS
TARGET_NODE: N-INT-COUPLING
MATHEMATICAL_PROPOSITION: >-
  Uniform nonperturbative mathematical estimates controlling the effective action and correlation functions
  across the intermediate crossover window g_k ~ 1 into the infrared regime.
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - nonperturbative
  - intermediate_coupling
  - missing_uniform_bound
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: UNIFORM_VOLUME
  CUTOFF_STATE: CONTINUUM_OR_FINE_LATTICE
  COUPLING_REGIME: INTERMEDIATE_COUPLING
EXPLICIT_HYPOTHESES:
  - Nonperturbative measure exists across scale transition
  - Gauge invariance preserved without small-field approximation
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: SmallFieldDominance
    STATUS: WEAKENED
    DETAIL: Small-field expansion fails as g_k ~ 1; nonperturbative control required
  - ASSUMPTION: UniformCrossover
    STATUS: NEW
    DETAIL: Hypothesized existence of uniform nonperturbative bound across g_k ~ 1
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Physical mass scale m_phys ~ Lambda_QCD
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONLESS_TRANSFER_RATIO
  REFERENCE_PHYSICAL_SCALE: Intermediate distance x ~ 1 / Lambda_QCD
  CONTINUUM_SCALING_BEHAVIOR: Nonperturbative matching between UV and IR scaling regimes
OBSERVABLE_ALGEBRA: Gauge-invariant Wilson loops and smeared field-strength polymers
THEOREMS_OR_SOURCES: []
WHAT_IS_PROVED: Nothing proved in 4D continuum literature.
WHAT_IS_NOT_PROVED: Proving uniform bounds across this crossover is completely open.
BRIDGE_VARIABLES: Intermediate effective coupling g_k ~ 1 and nonperturbative cluster activities.
FAILURE_LOCALITY: Nonperturbative crossover region x ~ 1/Lambda_QCD.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: ROUTE_REQUIRED
ROUTE_ID: ROUTE-CONSTRUCTIVE-RG
PROOF_DEPENDENCIES:
  - E-UV-RG
REASON_FOR_STATUS: Open; no mathematical theorem bridges Balaban UV bounds across g_k ~ 1.
```

```yaml
EDGE_ID: E-LATTICE-GAP
SOURCE_NODE: N-REG-LATTICE
TARGET_NODE: N-IR-CONFINEMENT
MATHEMATICAL_PROPOSITION: >-
  Rigorous proof of exponential correlation decay, strict positive spectral gap, and static quark confinement area law
  on fixed lattice at strong coupling beta = 2N/g^2 < beta_0.
PRIMARY_STATUS: REGULATED_ONLY
STATUS_QUALIFIERS:
  - fixed_lattice_spacing
  - strong_coupling_only
  - nonperturbative
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: SU(N)
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: FIXED_LATTICE_A
  COUPLING_REGIME: STRONG_COUPLING
EXPLICIT_HYPOTHESES:
  - Fixed lattice spacing a > 0
  - Strong coupling parameter beta = 2N/g^2 < beta_0
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: FixedLatticeSpacing
    STATUS: NEW
    DETAIL: Proof fundamentally relies on non-zero lattice spacing a > 0
  - ASSUMPTION: StrongCouplingConvergence
    STATUS: NEW
    DETAIL: Cluster expansion converges for small beta = 2N/g^2
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Lattice mass gap Delta_lattice(beta) > 0
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONLESS_LATTICE_MASS
  REFERENCE_PHYSICAL_SCALE: Lattice unit a
  CONTINUUM_SCALING_BEHAVIOR: Delta_lattice ~ -ln(beta / 2N) as beta -> 0
OBSERVABLE_ALGEBRA: Gauge-invariant Wilson loop operators on fixed lattice
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0008
    CITATION: Wilson, Phys. Rev. D 10 (1974) 2445
  - THEOREM_ID: THM-YM-0026
    CITATION: Shen, Zhu & Zhu, arXiv:2501.07720 (2025)
WHAT_IS_PROVED: Existence of infinite-volume Gibbs state, exponential clustering, and spectral gap on fixed lattice at strong coupling.
WHAT_IS_NOT_PROVED: Continuum limit a -> 0 or behavior as beta -> infinity.
BRIDGE_VARIABLES: Lattice spacing a, coupling parameter beta, and polymer cluster weights.
FAILURE_LOCALITY: Continuum limit beta -> infinity where cluster expansion radius beta_0 is exceeded.
OBSTRUCTION_CANDIDATE: OBS-CAND-003
NECESSITY_CLASS: ROUTE_REQUIRED
ROUTE_ID: ROUTE-LATTICE-CONTINUUM
PROOF_DEPENDENCIES: []
REASON_FOR_STATUS: Proved rigorously on fixed lattice (Wilson 1974, Shen-Zhu-Zhu 2025), but strictly regulated by a > 0.
```

```yaml
EDGE_ID: E-LATTICE-CONT
SOURCE_NODE: N-IR-CONFINEMENT
TARGET_NODE: N-INT-COUPLING
MATHEMATICAL_PROPOSITION: >-
  Continuation of exponential clustering and spectral gap estimates from strong coupling beta < beta_0
  along the weak-coupling continuum scaling trajectory beta -> infinity (a -> 0).
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - continuum_scaling
  - nonperturbative
  - diverging_cluster_expansion
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: SU(N)
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: SCALING_LATTICE
  COUPLING_REGIME: CROSSOVER_TO_WEAK
EXPLICIT_HYPOTHESES:
  - Lattice spacing a -> 0 scaling according to asymptotic freedom
  - Gap ratio Delta_lattice / a remains strictly positive and bounded
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: StrongCouplingConvergence
    STATUS: DISCHARGED
    DISCHARGED_BY: DiscardedAtWeakCoupling
    DISCHARGE_EVIDENCE: Cluster expansion invalid for beta > beta_0; replaced by nonperturbative scaling hypothesis
  - ASSUMPTION: UniformContinuumScaling
    STATUS: NEW
    DETAIL: Hypothesized nonperturbative scaling of physical mass m_phys = Delta(a)/a > 0
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Physical mass gap m_phys = lim_{a -> 0} Delta_lattice(a) / a
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONFUL_MASS
  REFERENCE_PHYSICAL_SCALE: Physical mass scale Delta > 0
  CONTINUUM_SCALING_BEHAVIOR: Delta_lattice(a) ~ a Lambda_QCD exp(-1 / (2 beta_0 g^2))
OBSERVABLE_ALGEBRA: Smeared Wilson loops and lattice field-strength correlators
THEOREMS_OR_SOURCES: []
WHAT_IS_PROVED: Nothing proved in mathematical physics for 4D non-Abelian continuum limit.
WHAT_IS_NOT_PROVED: Proving that the lattice mass gap survives the continuum limit beta -> infinity.
BRIDGE_VARIABLES: Lattice spacing a, coupling trajectory beta(a), and physical mass ratio Delta/a.
FAILURE_LOCALITY: Weak coupling limit beta -> infinity where non-trivial phase transitions or roughening could obstruct scaling.
OBSTRUCTION_CANDIDATE: OBS-CAND-003
NECESSITY_CLASS: ROUTE_REQUIRED
ROUTE_ID: ROUTE-LATTICE-CONTINUUM
PROOF_DEPENDENCIES:
  - E-LATTICE-GAP
REASON_FOR_STATUS: Open; core unsolved challenge of lattice gauge theory.
```

```yaml
EDGE_ID: E-THERMO
SOURCE_NODE: N-INT-COUPLING
TARGET_NODE: N-THERMO-LIMIT
MATHEMATICAL_PROPOSITION: >-
  Existence of the infinite volume thermodynamic limit V -> infinity for Schwinger functions with uniform volume-independent bounds.
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - thermodynamic_limit
  - infinite_volume
  - infrared_stability
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM_OR_REGULATED
  COUPLING_REGIME: FULL_COUPLING_RANGE
EXPLICIT_HYPOTHESES:
  - Finite volume Schwinger functions S_n^V exist
  - Uniform exponential cluster decay prevents boundary effects from accumulating
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: FiniteVolume
    STATUS: DISCHARGED
    DISCHARGED_BY: ThermodynamicLimitRemoval
    DISCHARGE_EVIDENCE: Hypothesized removal of boundary conditions as V -> infinity
  - ASSUMPTION: InfraredClusterBound
    STATUS: NEW
    DETAIL: Requires mass gap or exponential decay to establish thermodynamic limit
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Infinite volume vacuum energy density
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONLESS_CORRELATION_BOUND
  REFERENCE_PHYSICAL_SCALE: Spacetime volume V -> infinity
  CONTINUUM_SCALING_BEHAVIOR: Uniformity of correlators independent of box size L
OBSERVABLE_ALGEBRA: Local gauge-invariant operator algebra in infinite volume
THEOREMS_OR_SOURCES: []
WHAT_IS_PROVED: Proved for fixed lattice strong coupling (Shen-Zhu-Zhu 2025) and with IR cutoff (MRS 1993).
WHAT_IS_NOT_PROVED: Thermodynamic limit in 4D continuum without an explicit infrared mass cutoff.
BRIDGE_VARIABLES: Box volume V = L^4 and infrared correlation length xi = 1/m.
FAILURE_LOCALITY: Infrared volume accumulation without mass gap.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#WIGHTMAN-AXIOM-0
PROOF_DEPENDENCIES:
  - E-CROSSOVER
REASON_FOR_STATUS: Open; cannot be proved without infrared stability or mass gap.
```

```yaml
EDGE_ID: E-CONT-SCHWINGER
SOURCE_NODE: N-INT-COUPLING
TARGET_NODE: N-CONTINUUM-LIMIT
MATHEMATICAL_PROPOSITION: >-
  Construction of non-trivial continuum Euclidean Schwinger functions S_n in S'((R^4)^n) by removing all ultraviolet and infrared cutoffs.
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - continuum_limit
  - constructive_qft
  - distribution_valued
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM_LIMIT
  COUPLING_REGIME: NONPERTURBATIVE
EXPLICIT_HYPOTHESES:
  - Removal of lattice cutoff a -> 0 or momentum cutoff Lambda -> infinity
  - Proper wavefunction and coupling renormalization constants Z(a), g(a)
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: LatticeDiscretization
    STATUS: DISCHARGED
    DISCHARGED_BY: ContinuumLimitProcess
    DISCHARGE_EVIDENCE: Hypothesized distributional convergence as a -> 0
  - ASSUMPTION: DistributionalTemperedness
    STATUS: NEW
    DETAIL: S_n must exist as tempered distributions in S'((R^4)^n)
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Renormalized physical mass scale Delta > 0
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONFUL_DISTRIBUTION
  REFERENCE_PHYSICAL_SCALE: Fixed physical distances |x_i - x_j| > 0
  CONTINUUM_SCALING_BEHAVIOR: Short distance singularity governed by asymptotic freedom
OBSERVABLE_ALGEBRA: Gauge-invariant Euclidean Schwinger functions <O(x_1) ... O(x_n)>
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0020
    CITATION: Magnen, Rivasseau & Seneor, Commun. Math. Phys. 155 (1993) 325-383
WHAT_IS_PROVED: Construction with explicit infrared cutoff mu > 0 (MRS 1993).
WHAT_IS_NOT_PROVED: Removal of the infrared cutoff without assuming a mass gap.
BRIDGE_VARIABLES: Cutoff parameter a -> 0 and infrared cutoff mu -> 0.
FAILURE_LOCALITY: Concurrently removing UV and IR cutoffs without nonperturbative stability.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#AXIOMATIC-EXISTENCE
PROOF_DEPENDENCIES:
  - E-CROSSOVER
  - E-THERMO
REASON_FOR_STATUS: Open; central unresolved problem of constructive 4D gauge theory.
```

```yaml
EDGE_ID: E-SCHWINGER-OS0
SOURCE_NODE: N-CONTINUUM-LIMIT
TARGET_NODE: N-OS-TEMPERED
MATHEMATICAL_PROPOSITION: >-
  Established continuum Schwinger functions S_n satisfy OS0 tempered distribution bounds in S'((R^4)^n).
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - axiomatic_requirement
  - tempered_distribution
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM_LIMIT
  COUPLING_REGIME: NONPERTURBATIVE
EXPLICIT_HYPOTHESES:
  - S_n exists as linear functional on Schwartz space S((R^4)^n)
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: DistributionalTemperedness
    STATUS: PRESERVED
    DETAIL: Explicit seminorm bounds must be proved for S_n
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Schwartz test function seminorms
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONFUL_DISTRIBUTION
  REFERENCE_PHYSICAL_SCALE: Arbitrary Schwartz test functions
  CONTINUUM_SCALING_BEHAVIOR: Power-law bounds at infinity and short distance
OBSERVABLE_ALGEBRA: Tempered smeared field operators
THEOREMS_OR_SOURCES: []
WHAT_IS_PROVED: Axiom definition only (Osterwalder & Schrader 1973/1975).
WHAT_IS_NOT_PROVED: Establishing OS0 for 4D non-Abelian gauge theory.
BRIDGE_VARIABLES: Schwartz seminorm constants C_n, p_n.
FAILURE_LOCALITY: Uncontrolled distributional singularities at coinciding points.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#OS-AXIOM-0
PROOF_DEPENDENCIES:
  - E-CONT-SCHWINGER
REASON_FOR_STATUS: Open; must be proved for constructed Schwinger functions.
```

```yaml
EDGE_ID: E-SCHWINGER-OS1
SOURCE_NODE: N-CONTINUUM-LIMIT
TARGET_NODE: N-OS-EUCLIDEAN
MATHEMATICAL_PROPOSITION: >-
  Established continuum Schwinger functions are strictly invariant under Euclidean rotations and translations O(4) |><| R^4.
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - euclidean_invariance
  - symmetry_restoration
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM_LIMIT
  COUPLING_REGIME: NONPERTURBATIVE
EXPLICIT_HYPOTHESES:
  - Lattice hypercubic symmetry restores to continuous SO(4) rotation symmetry as a -> 0
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: HypercubicSymmetry
    STATUS: DISCHARGED
    DISCHARGED_BY: RotationalSymmetryRestoration
    DISCHARGE_EVIDENCE: Hypothesized restoration of continuous O(4) invariance as a -> 0
  - ASSUMPTION: FullEuclideanInvariance
    STATUS: NEW
    DETAIL: S_n(Rx + a) = S_n(x) for all R in O(4), a in R^4
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Rotational invariance of Euclidean metric
  DIMENSIONFUL_OR_DIMENSIONLESS: GEOMETRIC_INVARIANCE
  REFERENCE_PHYSICAL_SCALE: Spacetime coordinate space R^4
  CONTINUUM_SCALING_BEHAVIOR: Irrelevant lattice artifact operators vanish as a -> 0
OBSERVABLE_ALGEBRA: Gauge-invariant correlators of curvature tensors
THEOREMS_OR_SOURCES: []
WHAT_IS_PROVED: Axiom definition only; established in lower dimensions d=2,3 (Glimm-Jaffe, Chandra et al.).
WHAT_IS_NOT_PROVED: Proving O(4) restoration in 4D continuum non-Abelian theory.
BRIDGE_VARIABLES: Hypercubic breaking coefficients and irrelevant lattice operators.
FAILURE_LOCALITY: Anisotropic scaling or failure of rotational symmetry restoration.
OBSTRUCTION_CANDIDATE: OBS-CAND-003
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#OS-AXIOM-1
PROOF_DEPENDENCIES:
  - E-CONT-SCHWINGER
REASON_FOR_STATUS: Open; hypercubic lattice breaks O(4); restoration requires nonperturbative continuum limit proof.
```

```yaml
EDGE_ID: E-SCHWINGER-OS2
SOURCE_NODE: N-CONTINUUM-LIMIT
TARGET_NODE: N-OS-SYMMETRY
MATHEMATICAL_PROPOSITION: >-
  Continuum Schwinger functions are symmetric under permutations of Euclidean coordinates.
PRIMARY_STATUS: CONDITIONAL
STATUS_QUALIFIERS:
  - permutation_symmetry
  - path_integral_property
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM_LIMIT
  COUPLING_REGIME: NONPERTURBATIVE
EXPLICIT_HYPOTHESES:
  - S_n constructed as moments of a commutative Euclidean probability measure
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: PermutationSymmetry
    STATUS: PRESERVED
    DETAIL: Automatic from commutativity of functional integration variables
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Coordinate permutation
  DIMENSIONFUL_OR_DIMENSIONLESS: ALGEBRAIC_PROPERTY
  REFERENCE_PHYSICAL_SCALE: Permutation group S_n
  CONTINUUM_SCALING_BEHAVIOR: Preserved at all scales
OBSERVABLE_ALGEBRA: Bosonic Euclidean observables
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0009
    CITATION: Osterwalder & Schrader, Commun. Math. Phys. 31 (1973) 83-112
WHAT_IS_PROVED: Mathematical necessity and consistency of OS2.
WHAT_IS_NOT_PROVED: Unconditional existence of the continuum measure.
BRIDGE_VARIABLES: Bosonic field commutativity.
FAILURE_LOCALITY: None (algebraic property once measure exists).
OBSTRUCTION_CANDIDATE: null
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#OS-AXIOM-2
PROOF_DEPENDENCIES:
  - E-CONT-SCHWINGER
REASON_FOR_STATUS: Conditional; holds automatically if continuum limit is realized as a commutative probability measure.
```

```yaml
EDGE_ID: E-SCHWINGER-OS3
SOURCE_NODE: N-CONTINUUM-LIMIT
TARGET_NODE: N-OS-REFL-POS
MATHEMATICAL_PROPOSITION: >-
  Established continuum Schwinger functions satisfy Osterwalder-Schrader reflection positivity (Theta-positivity)
  with respect to Euclidean time reflection Theta(x_0, x_vec) = (-x_0, x_vec).
PRIMARY_STATUS: CONDITIONAL
STATUS_QUALIFIERS:
  - reflection_positivity
  - positive_hilbert_space
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM_LIMIT
  COUPLING_REGIME: NONPERTURBATIVE
EXPLICIT_HYPOTHESES:
  - Wilson lattice action reflection positivity survives the a -> 0 continuum limit
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: LatticeReflectionPositivity
    STATUS: PRESERVED
    DETAIL: Proved on Wilson lattice across planes of sites/links (Osterwalder-Seiler 1978)
  - ASSUMPTION: ContinuumReflectionPositivity
    STATUS: STRENGTHENED
    DETAIL: Preserved under pointwise or distributional limits of positive functionals
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Positive inner product on physical state space
  DIMENSIONFUL_OR_DIMENSIONLESS: POSITIVE_DEFINITE_METRIC
  REFERENCE_PHYSICAL_SCALE: Positive time half-space x_0 > 0
  CONTINUUM_SCALING_BEHAVIOR: Preserved identically under continuum scaling
OBSERVABLE_ALGEBRA: Algebra of observables localized in positive time half-space R^4_+
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0009
    CITATION: Osterwalder & Schrader (1973)
  - THEOREM_ID: THM-YM-0010
    CITATION: Osterwalder & Schrader, Commun. Math. Phys. 42 (1975) 281-305
WHAT_IS_PROVED: Reflection positivity is rigorously satisfied on the Wilson lattice (Osterwalder-Seiler 1978).
WHAT_IS_NOT_PROVED: Unconditional existence of the continuum limit.
BRIDGE_VARIABLES: Positive time reflection operator Theta and Euclidean transfer matrix.
FAILURE_LOCALITY: Gauge-fixing procedures that break reflection positivity (e.g. Faddeev-Popov ghost metric indefinite).
OBSTRUCTION_CANDIDATE: OBS-CAND-002
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#OS-AXIOM-3
PROOF_DEPENDENCIES:
  - E-CONT-SCHWINGER
REASON_FOR_STATUS: Conditional; reflection positivity is proved on the lattice and survives weak distributional limits, conditional on continuum limit existence.
```

```yaml
EDGE_ID: E-SCHWINGER-OS4
SOURCE_NODE: N-CONTINUUM-LIMIT
TARGET_NODE: N-OS-CLUSTER
MATHEMATICAL_PROPOSITION: >-
  Established continuum Schwinger functions satisfy exponential cluster decomposition with uniform rate Delta > 0.
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - cluster_decomposition
  - exponential_decay
  - spectral_gap_witness
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM_LIMIT
  COUPLING_REGIME: NONPERTURBATIVE
EXPLICIT_HYPOTHESES:
  - Spatial separation |x - y| -> infinity yields |<O(x) O(y)> - <O>^2| <= C exp(-Delta |x - y|)
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: ExponentialClustering
    STATUS: NEW
    DETAIL: Equivalent to existence of positive mass gap in Euclidean framework
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Exponential decay rate Delta > 0
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONFUL_MASS
  REFERENCE_PHYSICAL_SCALE: Long distance asymptotic separation |x| >> 1/Delta
  CONTINUUM_SCALING_BEHAVIOR: Uniform exponential decay rate in continuum limit
OBSERVABLE_ALGEBRA: Connected gauge-invariant correlators
THEOREMS_OR_SOURCES: []
WHAT_IS_PROVED: Proved on fixed lattice at strong coupling (Wilson 1974, Shen-Zhu-Zhu 2025).
WHAT_IS_NOT_PROVED: Proving exponential clustering in 4D continuum non-Abelian theory.
BRIDGE_VARIABLES: Exponential decay rate Delta and cluster truncation bounds.
FAILURE_LOCALITY: Infrared long-distance clustering without mass gap.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#OS-AXIOM-4
PROOF_DEPENDENCIES:
  - E-CONT-SCHWINGER
  - E-THERMO
REASON_FOR_STATUS: Open; directly equivalent to proving mass gap in the continuum.
```

```yaml
EDGE_ID: E-OS-RECON
SOURCE_NODE: N-OS-REFL-POS
TARGET_NODE: N-WIGHTMAN-RECON
MATHEMATICAL_PROPOSITION: >-
  Osterwalder-Schrader Reconstruction Theorem: Any collection of Euclidean Schwinger functions satisfying OS0, OS1, OS2, OS3
  uniquely reconstructs a relativistic Wightman quantum field theory on physical Hilbert space H with unitary Poincare representation U(a, Lambda).
PRIMARY_STATUS: PROVED
STATUS_QUALIFIERS:
  - axiomatic_theorem
  - hilbert_space_reconstruction
  - general_qft_framework
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: ARBITRARY
  MATTER_CONTENT: ARBITRARY
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM
  COUPLING_REGIME: GENERAL
EXPLICIT_HYPOTHESES:
  - OS0 (Temperedness)
  - OS1 (Euclidean invariance)
  - OS2 (Symmetry)
  - OS3 (Reflection positivity)
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: OS0_Temperedness
    STATUS: PRESERVED
    DETAIL: Essential hypothesis for operator domain density
  - ASSUMPTION: OS1_EuclideanInvariance
    STATUS: PRESERVED
    DETAIL: Essential hypothesis for Poincare group reconstruction
  - ASSUMPTION: OS3_ReflectionPositivity
    STATUS: DISCHARGED
    DISCHARGED_BY: HilbertSpaceQuotientConstruction
    DISCHARGE_EVIDENCE: Discharged by quotienting null vectors and completing under positive inner product <A, B>_H = S(Theta A * B)
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Self-adjoint Hamiltonian generator H = -i d/dt U(t)
  DIMENSIONFUL_OR_DIMENSIONLESS: OPERATOR_ALGEBRA
  REFERENCE_PHYSICAL_SCALE: Forward light cone V_bar_+
  CONTINUUM_SCALING_BEHAVIOR: Exact relativistic dispersion relation H^2 - P^2 = M^2
OBSERVABLE_ALGEBRA: Wightman operator-valued distributions on physical Hilbert space H
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0009
    CITATION: Osterwalder & Schrader, Commun. Math. Phys. 31 (1973) 83-112
  - THEOREM_ID: THM-YM-0010
    CITATION: Osterwalder & Schrader, Commun. Math. Phys. 42 (1975) 281-305
WHAT_IS_PROVED: Complete, rigorous mathematical theorem proving relativistic QFT reconstruction from Euclidean OS axioms.
WHAT_IS_NOT_PROVED: Existence of the 4D Yang-Mills Schwinger functions satisfying the input OS hypotheses.
BRIDGE_VARIABLES: Euclidean time transfer matrix e^{-t H} and physical Hilbert space completion.
FAILURE_LOCALITY: None (general mathematical theorem).
OBSTRUCTION_CANDIDATE: null
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#WIGHTMAN-RECONSTRUCTION
PROOF_DEPENDENCIES:
  - E-SCHWINGER-OS0
  - E-SCHWINGER-OS1
  - E-SCHWINGER-OS2
  - E-SCHWINGER-OS3
REASON_FOR_STATUS: Proved as a general mathematical theorem by Osterwalder and Schrader (1973, 1975).
```

```yaml
EDGE_ID: E-WIGHTMAN-VAC
SOURCE_NODE: N-WIGHTMAN-RECON
TARGET_NODE: N-VACUUM-UNIQUE
MATHEMATICAL_PROPOSITION: >-
  Physical Hilbert space contains a unique, Poincare-invariant vacuum state Omega with H Omega = 0,
  which is cyclic for the field algebra.
PRIMARY_STATUS: PROVED
STATUS_QUALIFIERS:
  - axiomatic_consequence
  - vacuum_uniqueness
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: ARBITRARY
  MATTER_CONTENT: ARBITRARY
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM
  COUPLING_REGIME: GENERAL
EXPLICIT_HYPOTHESES:
  - Wightman reconstructed QFT with OS4 cluster decomposition
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: ClusterDecomposition
    STATUS: DISCHARGED
    DISCHARGED_BY: ErgodicProjectionTheorem
    DISCHARGE_EVIDENCE: Discharges vacuum degeneracy via ergodic theorem on translation group
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Vacuum state normalization <Omega, Omega> = 1, H Omega = 0
  DIMENSIONFUL_OR_DIMENSIONLESS: STATE_NORMALIZATION
  REFERENCE_PHYSICAL_SCALE: Ground state energy E_0 = 0
  CONTINUUM_SCALING_BEHAVIOR: Exact scale-independent normalization
OBSERVABLE_ALGEBRA: Cyclic field algebra acting on vacuum Omega
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0009
    CITATION: Osterwalder & Schrader (1973)
WHAT_IS_PROVED: Unique cyclic vacuum state follows rigorously from OS reconstruction when cluster decomposition holds.
WHAT_IS_NOT_PROVED: Constructing 4D Yang-Mills theory satisfying the premise.
BRIDGE_VARIABLES: Projection operator P_0 = |Omega><Omega| onto translation-invariant subspace.
FAILURE_LOCALITY: None (mathematical consequence of clustering).
OBSTRUCTION_CANDIDATE: null
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#VACUUM-SECTOR
PROOF_DEPENDENCIES:
  - E-OS-RECON
  - E-SCHWINGER-OS4
REASON_FOR_STATUS: Proved rigorously within axiomatic QFT as a consequence of reconstruction and cluster decomposition.
```

```yaml
EDGE_ID: E-WIGHTMAN-SPEC
SOURCE_NODE: N-WIGHTMAN-RECON
TARGET_NODE: N-SPECTRAL-REP
MATHEMATICAL_PROPOSITION: >-
  Energy-momentum operators H, P_vec form a self-adjoint representation of R^4 translations with joint spectrum
  confined to the closed forward light cone Spec(H, P) in V_bar_+ = { (E, p) : E >= |p| >= 0 }.
PRIMARY_STATUS: PROVED
STATUS_QUALIFIERS:
  - spectral_condition
  - relativistic_stability
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: ARBITRARY
  MATTER_CONTENT: ARBITRARY
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM
  COUPLING_REGIME: GENERAL
EXPLICIT_HYPOTHESES:
  - Wightman reconstructed QFT from reflection-positive Schwinger functions
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: RelativisticStability
    STATUS: DISCHARGED
    DISCHARGED_BY: SemigroupSelfAdjointGenerator
    DISCHARGE_EVIDENCE: Generated by contractive Euclidean time semigroup T(t) = e^{-t H}, t >= 0
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Positive self-adjoint generator H >= 0
  DIMENSIONFUL_OR_DIMENSIONLESS: OPERATOR_SPECTRUM
  REFERENCE_PHYSICAL_SCALE: Mass hyperboloid M^2 >= 0
  CONTINUUM_SCALING_BEHAVIOR: Relativistic Lorentz covariance
OBSERVABLE_ALGEBRA: Energy-momentum spectral projections E(Delta)
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0009
    CITATION: Osterwalder & Schrader (1973)
  - THEOREM_ID: THM-YM-0010
    CITATION: Osterwalder & Schrader (1975)
WHAT_IS_PROVED: Relativistic spectrum condition Spec(P_mu) in forward light cone follows rigorously from OS reconstruction.
WHAT_IS_NOT_PROVED: Existence of 4D Yang-Mills Wightman fields.
BRIDGE_VARIABLES: Joint spectral measure of (H, P_vec).
FAILURE_LOCALITY: None (general mathematical theorem).
OBSTRUCTION_CANDIDATE: null
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#SPECTRAL-CONDITION
PROOF_DEPENDENCIES:
  - E-OS-RECON
REASON_FOR_STATUS: Proved rigorously as a core component of Osterwalder-Schrader reconstruction.
```

```yaml
EDGE_ID: E-GAP-CLUSTER
SOURCE_NODE: N-OS-CLUSTER
TARGET_NODE: N-MASS-GAP
MATHEMATICAL_PROPOSITION: >-
  Exponential decay of Euclidean connected correlation functions at rate m > 0 implies an isolated spectral mass gap
  Delta = m > 0 in the reconstructed physical Hamiltonian: Spec(H|_{H_0^perp}) subset [Delta, infinity).
PRIMARY_STATUS: PROVED
STATUS_QUALIFIERS:
  - spectral_theorem
  - mass_gap_equivalence
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: ARBITRARY
  MATTER_CONTENT: ARBITRARY
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM
  COUPLING_REGIME: GENERAL
EXPLICIT_HYPOTHESES:
  - OS reconstructed QFT with uniform exponential cluster decay rate m > 0
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: ExponentialClustering
    STATUS: DISCHARGED
    DISCHARGED_BY: SpectralLaplaceTransformTheorem
    DISCHARGE_EVIDENCE: Discharged by Laplace-Stieltjes transform relating correlator time-decay to Hamiltonian resolvent spectrum
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: "Isolated spectral threshold Delta = inf { E > 0 : E in Spec(H|_{H_0^perp}) }"
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONFUL_MASS_GAP
  REFERENCE_PHYSICAL_SCALE: Fundamental mass gap Delta > 0
  CONTINUUM_SCALING_BEHAVIOR: Exact identity between Euclidean decay rate and physical mass gap
OBSERVABLE_ALGEBRA: Gauge-invariant states generated on vacuum H_0^perp
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0009
    CITATION: Osterwalder & Schrader (1973)
WHAT_IS_PROVED: Exact mathematical equivalence between Euclidean exponential clustering and physical Hamiltonian spectral gap.
WHAT_IS_NOT_PROVED: Proving that 4D Yang-Mills exhibits exponential clustering in the continuum limit.
BRIDGE_VARIABLES: Spectral resolvent (H - z)^{-1} and Euclidean time correlation rate.
FAILURE_LOCALITY: None (general functional analysis theorem).
OBSTRUCTION_CANDIDATE: null
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#MASS-GAP-CONDITION
PROOF_DEPENDENCIES:
  - E-SCHWINGER-OS4
  - E-WIGHTMAN-SPEC
REASON_FOR_STATUS: Proved as a general mathematical theorem connecting Euclidean decay to Hamiltonian spectrum (Glimm-Jaffe, OS).
```

```yaml
EDGE_ID: E-NONTRIV-WITNESS
SOURCE_NODE: N-WIGHTMAN-RECON
TARGET_NODE: N-NONTRIV-DEF
MATHEMATICAL_PROPOSITION: >-
  Reconstructed 4D quantum field theory is non-trivial in the sense that its truncated 4-point connected correlator
  is non-vanishing (non-Gaussian) and does not collapse to a generalized free field.
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - non_triviality
  - non_gaussianity
  - interaction_witness
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM
  COUPLING_REGIME: INTERACTING
EXPLICIT_HYPOTHESES:
  - Connected 4-point truncated Schwinger function S_4^c is non-zero
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: NonTrivialityCriterion
    STATUS: NEW
    DETAIL: Official Clay non-triviality requirement must be established
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Truncated 4-point connected coupling lambda_phys > 0
  DIMENSIONFUL_OR_DIMENSIONLESS: DIMENSIONLESS_COUPLING
  REFERENCE_PHYSICAL_SCALE: Low-energy scattering scale
  CONTINUUM_SCALING_BEHAVIOR: Non-zero physical interaction in continuum limit
OBSERVABLE_ALGEBRA: Gauge-invariant Wilson loop connected correlators
THEOREMS_OR_SOURCES:
  - THEOREM_ID: THM-YM-0027
    CITATION: Chatterjee, Invent. Math. (2024)
WHAT_IS_PROVED: Chatterjee proved that certain naive 4D SU(2) lattice scaling limits collapse to generalized free fields (triviality warning).
WHAT_IS_NOT_PROVED: Constructing an interacting, non-trivial continuum Yang-Mills theory.
BRIDGE_VARIABLES: Truncated connected 4-point correlator S_4^c(x_1, x_2, x_3, x_4).
FAILURE_LOCALITY: Triviality collapse to Gaussian free field under continuum limit.
OBSTRUCTION_CANDIDATE: OBS-CAND-001
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#NON-TRIVIALITY
PROOF_DEPENDENCIES:
  - E-OS-RECON
REASON_FOR_STATUS: Open; non-triviality cannot be assumed; triviality collapse is an active mathematical threat (Chatterjee 2024).
```

```yaml
EDGE_ID: E-GROUP-GEN
SOURCE_NODE: N-MASS-GAP
TARGET_NODE: N-COMPACT-SIMPLE-G
MATHEMATICAL_PROPOSITION: >-
  The existence of quantum Yang-Mills theory and positive spectral mass gap Delta > 0 holds for every compact simple Lie group G.
PRIMARY_STATUS: OPEN
STATUS_QUALIFIERS:
  - group_universality
  - compact_simple_lie_group
SCOPE:
  DIMENSION: 4
  GAUGE_GROUP: ARBITRARY_COMPACT_SIMPLE_G
  MATTER_CONTENT: PURE_GAUGE
  VOLUME_REGIME: INFINITE_VOLUME
  CUTOFF_STATE: CONTINUUM
  COUPLING_REGIME: GENERAL
EXPLICIT_HYPOTHESES:
  - Compact simple Lie group G (SU(N), SO(N), Sp(N), G_2, F_4, E_6, E_7, E_8)
ASSUMPTION_TRANSFERS:
  - ASSUMPTION: ArbitraryGroupUniversality
    STATUS: NEW
    DETAIL: Clay target explicitly requires proof for arbitrary compact simple G
PHYSICAL_SCALE:
  ENERGY_NORMALIZATION: Casimir invariants C_2(G)
  DIMENSIONFUL_OR_DIMENSIONLESS: LIE_ALGEBRA_STRUCTURE
  REFERENCE_PHYSICAL_SCALE: Mass gap Delta(G) > 0
  CONTINUUM_SCALING_BEHAVIOR: Uniformity of bounds in group rank
OBSERVABLE_ALGEBRA: Adjoint and fundamental representations of Lie algebra g
THEOREMS_OR_SOURCES: []
WHAT_IS_PROVED: Nothing proved uniformly across all compact simple G.
WHAT_IS_NOT_PROVED: Proving mass gap for arbitrary G.
BRIDGE_VARIABLES: Group rank, dual Coxeter number c_2(G), and center Z(G).
FAILURE_LOCALITY: Center-dependent topological defects and group-specific representation subtleties.
OBSTRUCTION_CANDIDATE: null
NECESSITY_CLASS: TARGET_REQUIRED
TARGET_OBLIGATION_REF: OFFICIAL_PROBLEM_SPECIFICATION.md#GROUP-REQUIREMENT
PROOF_DEPENDENCIES:
  - E-GAP-CLUSTER
REASON_FOR_STATUS: Open; Clay problem requires universal proof for any compact simple G.
```
