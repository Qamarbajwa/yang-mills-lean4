# LIMIT AND REGIME MATRIX (YM-003)

This matrix tracks dimension, gauge group, volume, cutoff status, coupling regime, and limit trajectories
for every edge, enforcing that uniformity within a regime is never conflated with control across a transition.

| Edge ID | Dimension | Gauge Group | Volume Regime | Cutoff State | Coupling Regime | Limit Trajectory | Crossover Control | Physical Scale Setting |
|---|---|---|---|---|---|---|---|---|
| `E-UV-FREE` | 4 | SU(N) | FINITE_OR_INFINITE | BARE_REGULATED | WEAK_COUPLING | - | - | Dimensional transmutation scale Lambda_QCD |
| `E-UV-FREE-CONT` | 4 | SU(N) | FINITE_OR_INFINITE | CONTINUUM_CUTOFF | WEAK_COUPLING | - | - | Momentum cutoff scale Lambda |
| `E-UV-RG` | 4 | SU(2), SU(3) | FINITE_VOLUME | BLOCK_SPIN_REGULATED | WEAK_COUPLING | - | - | Block-spin scale L_k = L^k |
| `E-CROSSOVER` | 4 | COMPACT_SIMPLE_G | UNIFORM_VOLUME | CONTINUUM_OR_FINE_LATTICE | INTERMEDIATE_COUPLING | - | - | Physical mass scale m_phys ~ Lambda_QCD |
| `E-LATTICE-GAP` | 4 | SU(N) | INFINITE_VOLUME | FIXED_LATTICE_A | STRONG_COUPLING | - | - | Lattice mass gap Delta_lattice(beta) > 0 |
| `E-LATTICE-CONT` | 4 | SU(N) | INFINITE_VOLUME | SCALING_LATTICE | CROSSOVER_TO_WEAK | - | - | Physical mass gap m_phys = lim_{a -> 0} Delta_lattice(a) / a |
| `E-THERMO` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM_OR_REGULATED | FULL_COUPLING_RANGE | - | - | Infinite volume vacuum energy density |
| `E-CONT-SCHWINGER` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM_LIMIT | NONPERTURBATIVE | - | - | Renormalized physical mass scale Delta > 0 |
| `E-SCHWINGER-OS0` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM_LIMIT | NONPERTURBATIVE | - | - | Schwartz test function seminorms |
| `E-SCHWINGER-OS1` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM_LIMIT | NONPERTURBATIVE | - | - | Rotational invariance of Euclidean metric |
| `E-SCHWINGER-OS2` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM_LIMIT | NONPERTURBATIVE | - | - | Coordinate permutation |
| `E-SCHWINGER-OS3` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM_LIMIT | NONPERTURBATIVE | - | - | Positive inner product on physical state space |
| `E-SCHWINGER-OS4` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM_LIMIT | NONPERTURBATIVE | - | - | Exponential decay rate Delta > 0 |
| `E-OS-RECON` | 4 | ARBITRARY | INFINITE_VOLUME | CONTINUUM | GENERAL | - | - | Self-adjoint Hamiltonian generator H = -i d/dt U(t) |
| `E-WIGHTMAN-VAC` | 4 | ARBITRARY | INFINITE_VOLUME | CONTINUUM | GENERAL | - | - | Vacuum state normalization <Omega, Omega> = 1, H Omega = 0 |
| `E-WIGHTMAN-SPEC` | 4 | ARBITRARY | INFINITE_VOLUME | CONTINUUM | GENERAL | - | - | Positive self-adjoint generator H >= 0 |
| `E-GAP-CLUSTER` | 4 | ARBITRARY | INFINITE_VOLUME | CONTINUUM | GENERAL | - | - | Isolated spectral threshold Delta = inf { E > 0 : E in Spec(H|_{H_0^perp}) } |
| `E-NONTRIV-WITNESS` | 4 | COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM | INTERACTING | - | - | Truncated 4-point connected coupling lambda_phys > 0 |
| `E-GROUP-GEN` | 4 | ARBITRARY_COMPACT_SIMPLE_G | INFINITE_VOLUME | CONTINUUM | GENERAL | - | - | Casimir invariants C_2(G) |