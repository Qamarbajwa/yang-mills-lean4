# PAPER-MOD-003: Analytic Bootstrap for Lattice Yang-Mills Theory via Makeenko-Migdal Loop Equations and Positive Semidefinite Matrix Constraints

- **SOURCE_ID:** `PAPER-MOD-003`
- **TITLE:** Analytic Bootstrap for Lattice Yang-Mills Theory via Makeenko-Migdal Loop Equations and Positive Semidefinite Matrix Constraints
- **AUTHORS:** Vladimir Kazakov, Zechuan Zheng
- **JOURNAL:** Physical Review D
- **VOLUME:** 107
- **PAGES:** 034509
- **YEAR:** 2022
- **DOI:** `10.1103/PhysRevD.107.034509`
- **SOURCE_ACCESS:** `PRIMARY_FULL_TEXT`
- **STORAGE_FORMAT:** `AUTHORITATIVE_METADATA_AND_EXCERPTS`
- **BRIDGE_VARIABLES:** lattice coupling beta, Wilson loop size |C|, bootstrap truncation L_max, semidefinite matrix spectrum
- **FAILURE_LOCALITY:** `continuum limit (infinite loop truncation)`

## Executive Summary
Kazakov and Zheng developed a non-perturbative numerical/analytical bootstrap method for lattice gauge theories in 2D, 3D, and 4D. Combining the exact Schwinger-Dyson / Makeenko-Migdal loop equations on the lattice with reflection positivity and Gram matrix positive-semidefiniteness of Wilson loops, they obtained rigorous upper and lower bounds on plaquette expectation values and string tension at finite N and large N.

## Key Proven Results
- Derivation of rigorous bootstrap inequalities on Wilson loop expectation values from Makeenko-Migdal equations and positivity.
- Rigorous non-perturbative upper and lower bounds on lattice plaquette energy and string tension without Monte Carlo sampling.
- Formulation of semidefinite programming relaxation for non-Abelian lattice gauge theories.

## Limitations and Unresolved Boundaries
- Operates on a discrete lattice at fixed coupling beta = 2N/g^2 and lattice spacing a > 0.
- Continuum limit a -> 0 requires scaling infinite loops simultaneously, which is truncated in finite-size bootstrap relaxations.
- Does not prove the continuum mass gap Delta > 0 analytically in 4D.
