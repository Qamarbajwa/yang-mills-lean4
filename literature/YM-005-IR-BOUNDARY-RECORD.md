# YM-005 Canonical IR Boundary Record

## 1. Canonical Boundary Identification

- **Record Identifier:** `IR-BND-YM005-001`
- **Domain:** Infrared / Strong-Coupling Lattice Gauge Theory
- **Governance Context:** Universal Governance v4.0.3 / ROS v1.0
- **Parent Task:** `YM-005` (Rigorous IR / Lattice Gap Machinery Reproduction)
- **Status:** `AUTHORITATIVE_IR_BOUNDARY_RECORD`

---

## 2. Canonical IR Boundary Record Specification

```yaml
canonical_ir_boundary_record:
  record_id: "IR-BND-YM005-001"
  theory: "4D Pure Euclidean Yang–Mills Theory on Hypercubic Lattice a Z^4"
  gauge_group: "Compact simple Lie group G (specifically SU(N), N >= 2)"
  regularization: "Wilson lattice plaquette action with lattice spacing a > 0"

  last_proved_strong_coupling_regime:
    symbolic_bound: "beta <= beta_* << 1  (equivalently g^2 >= g_IR*^2 >> 1)"
    mathematical_character: "Uniformly convergent polymer / high-temperature character cluster expansion"
    governing_norm: "Lattice polymer tree-norm with Kotecký–Preiss activity bound sum_{Y ~ X} |zeta(Y)| e^{mu |Y|} <= mu |X|"

  beta_range:
    symbolic: "0 <= beta <= beta_0(d, G)"
    formal_definition: "Radius of absolute convergence of the multi-plaquette character cluster expansion"

  lattice_spacing_scope:
    scope: "Fixed discrete lattice cutoff a > 0"
    continuum_status: "Lattice spacing a CANNOT be taken to 0 within this regime without violating beta <= beta_*"

  volume_scope:
    scope: "Infinite-volume thermodynamic limit Lambda -> Z^4"
    uniformity: "Thermodynamic limit exists, is unique, and is independent of boundary conditions (Gross 1979, Seiler 1982, Shen–Zhu–Zhu 2023)"

  gap_or_decay_property:
    hamiltonian_spectral_gap: "Delta_lat(beta, a) = -a^{-1} ln(lambda_1(beta) / lambda_0(beta)) = -a^{-1} ln(lambda_hat_1(beta)) >= m_lat(beta) / a > 0 on H_phys with T_hat = T / lambda_0(beta) (Osterwalder–Seiler 1978, Seiler 1982)"
    markov_generator_gap: "gap_{L^2(mu_infty)}(-L) >= 1 / C_PI(beta) > 0 on L^2(G^{E(Z^d)}, mu_infty) (Shen–Zhu–Zhu 2023)"
    exponential_clustering: "|<A B> - <A><B>| <= C(A, B) exp(-m_lat(beta) d(A, B)) with m_lat(beta) ~ ln(1/beta) > 0 (Gross 1979, Osterwalder–Seiler 1978, Seiler 1982, Shen–Zhu–Zhu 2023)"
    functional_inequality: "Uniform Poincaré inequality on Z^d: Var_{mu_infty}(f) <= C_PI(beta) E(f, f) with C_PI(beta) < infty (Shen–Zhu–Zhu 2023)"
    wilson_area_law: "Wilson loop area law <W(C)> <= C exp(-sigma_lat Area(C) / a^2) with sigma_lat(beta) ~ ln(1/beta) > 0 (Wilson 1974, Osterwalder–Seiler 1978, Cao–Nissim–Sheffield 2025)"
    non_conflation_invariant: "gap(-L) != Delta_lat(beta, a) != sigma_lat(beta); Markov generator gap on L^2(mu_infty) is never equated with Hamiltonian gap on H_phys"

  uniformity_established:
    spatial_volume: "Uniform across all finite sub-boxes Lambda subset Z^4"
    transfer_operator: "Self-adjoint positive contraction 0 < T <= I on physical Hilbert space H_phys"

  first_unproved_extension:
    mathematical_boundary: "The intermediate-coupling crossover window beta ~ 1 (equivalently g_k ~ 1)"
    continuum_trajectory: "Scaling trajectory beta(a) -> infty (a -> 0, g -> 0) dictated by asymptotic freedom"
    failure_mode: "Loss of sufficient contractivity of polymer cluster expansions and collapse of Bakry–Émery positive curvature"

  source:
    primary_theorems:
      - "THM-YM-0008 (Wilson 1974, Phys. Rev. D 10, 2445)"
      - "THM-YM-0009 (Osterwalder & Seiler 1978, Ann. Phys. 110, 440; Lüscher 1977, CMP 54, 283)"
      - "THM-YM-0015 (Seiler 1982, Lecture Notes in Physics 159; Gross 1979, CMP 68, 9)"
      - "THM-YM-0027 (Shen, Zhu, Zhu 2023, Comm. Math. Phys. 400, 805)"
      - "THM-YM-0028 (Cao, Nissim, Sheffield 2025, arXiv:2505.16585)"

  epistemic_status: "RIGOROUS_PROVED_AT_STRONG_COUPLING_FIXED_LATTICE (SCIENTIFICALLY_ACCEPTED_WITH_REGULATED_SCOPE)"
```

---

## Appendix A (NON-AUTHORITATIVE HEURISTIC APPENDIX): Parameter Provenance Quarantine

In accordance with **`INV-YM005-003`**, **ROS v1.0 Law 1**, and **`YM-GOV-014` (`YM-005-R1`)**, canonical lattice theorems are strictly dimensionless ($a > 0$, $\beta \in (0, \beta_0)$) and contain **no physical QCD unit guarantees**. Any numerical or phenomenological parameter translations are strictly non-authoritative and quarantined below:

| Parameter / Symbol | Symbolic / Dimensionless Scope | Provenance Classification | Authoritative Source & Mathematical Basis | Rigorous Constructive Status |
|---|---|---|---|---|
| Strong-Coupling Radius ($\beta_0$) | $0 < \beta_0(d, G) \ll 1$ | `PROJECT_ESTIMATE` | Kotecký–Preiss condition $\beta < (C_{\text{geom}} K_0 e^{\mu+1})^{-1}$ on hypercubic lattice polymers (Seiler 1982, Section 3). | **Symbolic existence theorem.** Primary source proves $\exists \beta_0 > 0$ strictly positive; exact numerical radius depends on tree-embedding bounds. |
| Expanded Area Law Bound ($\beta_1$) | $0 < \beta_0 < \beta_1(d, G)$ | `PROJECT_ESTIMATE` | Random surface percolation and stochastic coupling thresholds (Cao, Nissim, Sheffield 2025). | **Bounded on discrete lattice.** Non-uniform as $\beta \to \infty$. |
| Coarse Lattice Spacing ($a_{\text{strong}}$) | Fixed discrete spacing $a > 0$ (dimensionless lattice units) | `HEURISTIC_PHYSICAL_TRANSLATION` | Phenomenological conversion equating dimensionless lattice mass $m_{\text{lat}} \sim 1$ with external reference scale $M_{\text{ref}}$ ($a = m_{\text{lat}} / M_{\text{ref}}$). | **Physical phenomenology only (NOT A THEOREM).** Primary constructive lattice theorems contain no physical length units. |
| Dimensionless vs. Phenomenological String Tension ($\sigma_{\text{lat}}$) | $\sigma_{\text{lat}}(\beta) \sim \ln(1/\beta) > 0$ (dimensionless per plaquette) | `HEURISTIC_PHYSICAL_TRANSLATION` | Pure mathematical theorems prove only dimensionless area-law decay $\sigma_{\text{lat}}(\beta) > 0$ on fixed lattices. | **Dimensionless lattice bound only.** Physical continuum string tension $\lim_{a\to 0} \sigma_{\text{lat}}(a)/a^2$ is unproved (`OPEN`). |
| Intermediate Crossover ($\beta_{\text{crossover}}$) | $\beta \sim \mathcal{O}(1)$ outside polymer radius $\beta_0$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Monte Carlo lattice simulations identifying the peak of plaquette susceptibility separating strong and weak coupling. | **Numerical simulation benchmark.** Unestablished within rigorous analytical constructive theorems. |

---

## 4. Fundamental Boundary Invariants

1. **Symbolic Bounds Enforced:**
   Canonical theorems operate strictly under dimensionless symbolic bounds:
   $$\boxed{\beta \le \beta_0(d, G) \ll 1, \quad a > 0 \text{ (fixed discrete lattice)}}$$
   Specific numerical numbers are restricted to heuristic comparisons.

2. **Lattice Spectral Gap $\ne$ Continuum Mass Gap:**
   $$\boxed{\Delta_{\text{lat}}(\beta, a) > 0 \;\; \centernot\implies \;\; \Delta_{\text{continuum}} > 0}$$
   The non-zero spectral gap established by Shen–Zhu–Zhu (2023) and Seiler (1982) is an exact property of the discrete lattice at fixed $a > 0$ and $\beta < \beta_0$. It does not establish the existence of a continuum quantum field theory in $\mathbb{R}^4$.

3. **Wilson Area Law $\ne$ Spectral Mass Gap:**
   $$\boxed{\langle W(C) \rangle \le C e^{-\sigma \cdot \text{Area}(C)} \;\; \centernot\implies \;\; \text{spec}(H) \subseteq \{0\} \cup [\Delta, \infty)}$$
   Confinement of static fundamental quarks (Cao–Nissim–Sheffield 2025; Wilson 1974) is independent of the local glueball spectral mass gap.
