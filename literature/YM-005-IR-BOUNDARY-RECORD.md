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
    spectral_gap: "Delta_lat(beta, a) = -a^{-1} ln lambda_1(beta) >= m_lat(beta) / a > 0"
    exponential_clustering: "|<A B> - <A><B>| <= C(A, B) exp(-m_lat(beta) d(A, B)) with m_lat(beta) ~ ln(1/beta) > 0"
    functional_inequality: "Uniform Poincaré inequality on Z^d: Var_{mu_infty}(f) <= C_PI(beta) E(f, f) with C_PI(beta) < infty"
    area_law: "Wilson loop area law <W(C)> <= C exp(-sigma_lat Area(C) / a^2) with sigma_lat(beta) ~ ln(1/beta) > 0"

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

  epistemic_status: "RIGOROUS_PROVED_AT_STRONG_COUPLING_FIXED_LATTICE"
```

---

## 3. Quantitative Parameter Provenance Audit Table

In accordance with **`INV-YM005-003`** and **ROS v1.0 Law 1**, all numerical parameters associated with the infrared boundary are classified with explicit mathematical provenance:

| Parameter / Symbol | Numerical Value / Range | Provenance Classification | Authoritative Source & Mathematical Basis | Rigorous Constructive Status |
|---|---|---|---|---|
| Strong-Coupling Radius ($\beta_0$) | $\sim 0.05 - 0.25$ for $SU(2)$ | `PROJECT_ESTIMATE` | Kotecký–Preiss condition $\beta < (C_{\text{geom}} K_0 e^{\mu+1})^{-1}$ on hypercubic lattice polymers (Seiler 1982, Section 3). | **Heuristic mathematical estimate.** Primary source proves $\exists \beta_0 > 0$ strictly positive; exact numerical radius depends on tree-embedding bounds. |
| Expanded Area Law Bound ($\beta_1$) | $\sim 0.3 - 0.8$ for $SU(2)$ | `PROJECT_ESTIMATE` | Random surface percolation and stochastic coupling thresholds (Cao, Nissim, Sheffield 2025). | **Heuristic mathematical estimate.** Bounded rigorously on discrete lattice, but non-uniform as $\beta \to \infty$. |
| Coarse Lattice Spacing ($a_{\text{strong}}$) | $\ge 0.4 - 0.6\text{ fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Phenomenological conversion equating dimensionless lattice mass $m_{\text{lat}} \sim 1$ with physical glueball scale $M \sim 1.5 - 1.7\text{ GeV}$ ($a = m_{\text{lat}} / M$). | **Physical phenomenology only.** Primary constructive lattice theorems contain no physical units or $\text{fm}$ constants. |
| Physical String Tension ($\sigma_{\text{phys}}$) | $\sim (420\text{ MeV})^2 \approx 0.18\text{ GeV}^2 \approx 0.9\text{ GeV/fm}$ | `HEURISTIC_PHYSICAL_TRANSLATION` | Regge trajectory slope $\alpha' \approx 0.9\text{ GeV}^{-2}$ from hadronic string phenomenology ($\sigma = 1 / (2\pi \alpha')$). | **Empirical QCD phenomenology.** Pure mathematical theorems prove only dimensionless area law decay $\sigma_{\text{lat}}(\beta) > 0$. |
| Intermediate Crossover ($\beta_{\text{crossover}}$) | $\approx 2.0 - 2.5$ for $SU(2)$ ($\approx 5.7 - 6.0$ for $SU(3)$) | `HEURISTIC_PHYSICAL_TRANSLATION` | Monte Carlo lattice simulations identifying the peak of the specific heat / plaquette susceptibility separating strong and weak coupling. | **Numerical simulation benchmark.** Unestablished within rigorous analytical constructive theorems. |

---

## 4. Fundamental Boundary Invariants

1. **Symbolic Bounds Enforced:**
   Canonical theorems operate strictly under symbolic bounds:
   $$\boxed{\beta \le \beta_* \ll 1, \quad a \ge a_{\text{strong}}^* \sim \frac{c_{\text{IR}}}{\Lambda_{\text{QCD}}}}$$
   Specific numerical numbers are restricted to heuristic comparisons.

2. **Lattice Spectral Gap $\ne$ Continuum Mass Gap:**
   $$\boxed{\Delta_{\text{lat}}(\beta, a) > 0 \;\; \centernot\implies \;\; \Delta_{\text{continuum}} > 0}$$
   The non-zero spectral gap established by Shen–Zhu–Zhu (2023) and Seiler (1982) is an exact property of the discrete lattice at fixed $a > 0$ and $\beta < \beta_0$. It does not establish the existence of a continuum quantum field theory in $\mathbb{R}^4$.

3. **Wilson Area Law $\ne$ Spectral Mass Gap:**
   $$\boxed{\langle W(C) \rangle \le C e^{-\sigma \cdot \text{Area}(C)} \;\; \centernot\implies \;\; \text{spec}(H) \subseteq \{0\} \cup [\Delta, \infty)}$$
   Confinement of static fundamental quarks (Cao–Nissim–Sheffield 2025; Wilson 1974) is independent of the local glueball spectral mass gap.
