# MINIMAL SUFFICIENT ESTIMATE REGISTER (YM-003)

This register records candidate minimal sufficient estimates (E1–E8) that would strictly strengthen
the missing-bridge chain toward the Clay Millennium target.

## Status Summary: `NO_SINGLE_MINIMAL_ESTIMATE_IDENTIFIED`

Comparative mathematical analysis reveals that no single estimate in isolation suffices to bridge the gap.
The minimal unresolved requirement forms a **load-bearing cut-set pair**:
- Uniform crossover bound across $g_k \sim 1$ (`E-CROSSOVER` / `EST-E1`)
- Continuum thermodynamic limit without mass cutoff (`E-THERMO` / `EST-E3`)

---

### Candidate Estimates

#### `EST-E1: Connected Correlator Exponential Bound at Finite Separation`
- **Exact Proposition:** For renormalized gauge-invariant local observables $\\mathcal{O}_1, \\mathcal{O}_2$,
  $$\\big| \\langle \\mathcal{O}_1(x) \\mathcal{O}_2(0) \\rangle_{\\text{conn}} \\big| \\le C \\exp(-M |x|)$$
  uniformly as regulator $a \\to 0$ for $|x| \\ge x_0 > 0$.
- **Edge References:** `E-CROSSOVER`, `E-SCHWINGER-OS4`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#OS-AXIOM-4`
- **Minimality Class:** `LOAD_BEARING_CORE_ESTIMATE`
- **Comparison:** Weaker than full constructive existence; strictly stronger than perturbative bounds.
- **Epistemic Status:** `OPEN`

#### `EST-E2: Physical Energy Scale-Setting Ratio`
- **Exact Proposition:** Rigorous scale-setting ratio $m_{\\text{phys}} = \\lim_{a \\to 0} \\frac{\\Delta_{\\text{lattice}}(a)}{a} > 0$
  proved to be non-zero and finite along the asymptotic freedom trajectory.
- **Edge References:** `E-LATTICE-CONT`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#MASS-GAP-CONDITION`
- **Minimality Class:** `LATTICE_ROUTE_MINIMAL_ESTIMATE`
- **Epistemic Status:** `OPEN`

#### `EST-E3: Subsequential Tightness & Coincidence of Continuum Limits`
- **Exact Proposition:** Family of regularized Schwinger measures $\\{\\mu_a\\}_{a > 0}$ is tight in $\\mathcal{S}'$
  and all subsequential limits coincide.
- **Edge References:** `E-CONT-SCHWINGER`, `E-THERMO`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#AXIOMATIC-EXISTENCE`
- **Minimality Class:** `EXISTENCE_BRANCH_MINIMAL_ESTIMATE`
- **Epistemic Status:** `OPEN`

#### `EST-E4: Joint Directed Limit without Iterated-Limit Interchange`
- **Exact Proposition:** Joint thermodynamic and continuum limit $\\lim_{a \\to 0, V \\to \\infty}$ exists directly
  without requiring order-dependent limit interchange.
- **Edge References:** `E-THERMO`, `E-CONT-SCHWINGER`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#AXIOMATIC-EXISTENCE`
- **Minimality Class:** `TECHNICAL_REGIME_ESTIMATE`
- **Epistemic Status:** `OPEN`

#### `EST-E5: Non-Gaussian 4-Point Connected Interaction Witness`
- **Exact Proposition:** Truncated connected 4-point Schwinger function $S_4^c(x_1, x_2, x_3, x_4) \\ne 0$ in the continuum limit.
- **Edge References:** `E-NONTRIV-WITNESS`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#NON-TRIVIALITY`
- **Minimality Class:** `NON_TRIVIALITY_MINIMAL_WITNESS`
- **Epistemic Status:** `OPEN`

#### `EST-E6: Reflection-Positive Observable Algebra Density`
- **Exact Proposition:** Gauge-invariant positive-time local observables generate a dense domain in the reconstructed physical Hilbert space.
- **Edge References:** `E-OS-RECON`, `E-SCHWINGER-OS3`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#WIGHTMAN-RECONSTRUCTION`
- **Minimality Class:** `AXIOMATIC_CLOSURE_ESTIMATE`
- **Epistemic Status:** `CONDITIONAL`

#### `EST-E7: Nonperturbative Cluster Remainder Control`
- **Exact Proposition:** Cluster expansion truncation error bounded by $O(e^{-c L})$ uniformly in cutoff $a$.
- **Edge References:** `E-CROSSOVER`, `E-LATTICE-CONT`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#OS-AXIOM-4`
- **Minimality Class:** `CONSTRUCTIVE_EXPANSION_ESTIMATE`
- **Epistemic Status:** `OPEN`

#### `EST-E8: Uniform Lie Algebra Rank Bound`
- **Exact Proposition:** Bounds on constants $C(G), M(G)$ dependent only on Casimir invariants, uniform for all compact simple Lie algebras.
- **Edge References:** `E-GROUP-GEN`
- **Target / Route References:** `OFFICIAL_PROBLEM_SPECIFICATION.md#GROUP-REQUIREMENT`
- **Minimality Class:** `GROUP_GENERALITY_ESTIMATE`
- **Epistemic Status:** `OPEN`
