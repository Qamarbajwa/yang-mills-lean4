# YM-005 11-Dimensional Theorem Ledger

## 1. Governance Specification and Requirement

In strict adherence to human-owner instructions for Task `YM-005` and `INV-YM005-004`, every reconstructed infrared, lattice, and strong-coupling theorem must be explicitly audited across exactly 11 canonical parameters:

1. **`GAUGE_GROUP`** ($G$)
2. **`DIMENSION`** ($d$)
3. **`LATTICE_SPACING_SCOPE`** ($a$)
4. **`VOLUME_SCOPE`** ($V$ or $\Lambda$)
5. **`COUPLING_PARAMETER`** ($\beta$ or $g$)
6. **`OBSERVABLE_SCOPE`** (Wilson loop, plaquette, transfer matrix, correlation function)
7. **`GAP_OR_DECAY_PROPERTY`** (spectral gap $\Delta_{\text{lat}}$, string tension $\sigma$, decay mass $m_{\text{lat}}$, Poincaré constant $C_{\text{PI}}$)
8. **`UNIFORMITY_ESTABLISHED`** (uniform in volume, uniform in lattice size)
9. **`CONTINUUM_LIMIT_STATUS`** ($a \to 0, \beta \to \infty$ reached or blocked)
10. **`WHAT_IS_ACTUALLY_PROVED`** (exact mathematical scope)
11. **`WHAT_REMAINS_OPEN`** (precise terminal barrier)

---

## 2. Granular 11-Dimensional Theorem Entries

### Entry 1: THM-YM-0008 (Wilson 1974)
- **Theorem ID:** `THM-YM-0008`
- **Source Citation:** K. G. Wilson, *Phys. Rev. D* **10** (1974), pp. 2445–2459 (`PAPER-FOUND-008`).
1. **`GAUGE_GROUP`:** Any compact Lie group $G$ (explicitly $U(1)$, $SU(2)$, $SU(3)$).
2. **`DIMENSION`:** $d = 4$ Euclidean spacetime (and $d \ge 2$).
3. **`LATTICE_SPACING_SCOPE`:** Fixed lattice cutoff $a > 0$.
4. **`VOLUME_SCOPE`:** Finite box $\Lambda \subset a \mathbb{Z}^4$ and formal infinite volume.
5. **`COUPLING_PARAMETER`:** Extreme strong coupling: $g^2 \gg 1$ ($\beta = \frac{2N}{g^2} \ll 1$).
6. **`OBSERVABLE_SCOPE`:** Planar Wilson loop expectation $\langle W(C) \rangle = \frac{1}{N} \langle \text{Tr}_F \prod_{\ell \in C} U_\ell \rangle$.
7. **`GAP_OR_DECAY_PROPERTY`:** Area law decay: $\langle W(C) \rangle \sim \exp(-\sigma_{\text{lat}} \cdot \text{Area}(C) / a^2)$ with leading string tension $\sigma_{\text{lat}} = \ln(2N^2 / \beta) + \mathcal{O}(\beta^4)$.
8. **`UNIFORMITY_ESTABLISHED`:** Uniform in loop size for $\beta < \beta_0$.
9. **`CONTINUUM_LIMIT_STATUS`:** **BLOCKED.** Expansion parameter is $\beta \ll 1$; continuum limit requires $\beta \to \infty$.
10. **`WHAT_IS_ACTUALLY_PROVED`:** Leading-order strong-coupling expansion of character integrals yields an area law on fixed discrete lattices with non-zero string tension.
11. **`WHAT_REMAINS_OPEN`:** Continuum limit $a \to 0$; non-perturbative mass gap in continuum Hilbert space; preservation of confinement at weak coupling $\beta \to \infty$.

---

### Entry 2: THM-YM-0009 (Osterwalder & Seiler 1978; Lüscher 1977)
- **Theorem ID:** `THM-YM-0009`
- **Source Citation:** K. Osterwalder, E. Seiler, *Ann. Phys.* **110** (1978), pp. 440–471 (`PAPER-FOUND-013`); M. Lüscher, *Comm. Math. Phys.* **54** (1977), pp. 283–292.
1. **`GAUGE_GROUP`:** Compact Lie group $G$.
2. **`DIMENSION`:** $d = 2, 3, 4$ Euclidean spacetime.
3. **`LATTICE_SPACING_SCOPE`:** Fixed lattice cutoff $a > 0$.
4. **`VOLUME_SCOPE`:** Finite box with periodic/Dirichlet boundary conditions, bisected by reflection hyperplane $\Pi$.
5. **`COUPLING_PARAMETER`:** Arbitrary coupling $0 < \beta < \infty$.
6. **`OBSERVABLE_SCOPE`:** Cylinder functionals supported on positive-time lattice $\mathcal{A}_+$; transfer operator $\mathbb{T}$.
7. **`GAP_OR_DECAY_PROPERTY`:** Reflection positivity $\langle \theta F, F \rangle \ge 0$; existence of strictly positive self-adjoint transfer matrix $\mathbb{T} = e^{-a H_{\text{lat}}} > 0$; positive Hamiltonian $H_{\text{lat}} \ge 0$.
8. **`UNIFORMITY_ESTABLISHED`:** Exact operator inequality holding uniformly on the discrete lattice for all $\beta \in (0, \infty)$.
9. **`CONTINUUM_LIMIT_STATUS`:** **BLOCKED.** Does not establish uniform lower bound on the spectrum of $H_{\text{lat}}$ as $a \to 0$.
10. **`WHAT_IS_ACTUALLY_PROVED`:** Rigorous existence of physical Hilbert space $\mathcal{H}_{\text{phys}}$, self-adjoint positive transfer operator $\mathbb{T}$, and positive energy $H_{\text{lat}} \ge 0$ on discrete lattices for all $\beta$.
11. **`WHAT_REMAINS_OPEN`:** Uniform spectral gap $\Delta(a) \ge \Delta_0 > 0$ as $a \to 0$; recovery of continuous rotational/Poincaré invariance.

---

### Entry 3: THM-YM-0015 (Seiler 1982; Gross 1979)
- **Theorem ID:** `THM-YM-0015`
- **Source Citation:** E. Seiler, *Lecture Notes in Physics* **159** (1982), pp. 1–192 (`PAPER-CONST-003`); L. Gross, *Comm. Math. Phys.* **68** (1979), pp. 9–27.
1. **`GAUGE_GROUP`:** General compact Lie group $G$.
2. **`DIMENSION`:** $d \ge 2$ ($d = 4$ specifically).
3. **`LATTICE_SPACING_SCOPE`:** Fixed lattice cutoff $a > 0$.
4. **`VOLUME_SCOPE`:** Infinite-volume thermodynamic limit $\Lambda \to \mathbb{Z}^d$.
5. **`COUPLING_PARAMETER`:** Strong coupling: $0 \le \beta < \beta_0(d, G)$.
6. **`OBSERVABLE_SCOPE`:** Free energy density $f(\beta)$; truncated correlation functions $\langle A B \rangle_T$ of gauge-invariant observables.
7. **`GAP_OR_DECAY_PROPERTY`:** Exponential correlation decay $m_{\text{lat}}(\beta) \sim \ln(1/\beta) > 0$; strictly positive transfer matrix spectral gap $\Delta_{\text{lat}}(\beta, a) \ge m_{\text{lat}} / a > 0$.
8. **`UNIFORMITY_ESTABLISHED`:** Uniform in volume $\Lambda \to \mathbb{Z}^d$; analyticity of free energy in complex disc $|\beta| < \beta_0$.
9. **`CONTINUUM_LIMIT_STATUS`:** **BLOCKED.** Convergence radius $\beta_0(d, G) \ll 1$ does not reach continuum limit $\beta \to \infty$.
10. **`WHAT_IS_ACTUALLY_PROVED`:** Absolute convergence of polymer cluster expansion, uniqueness of infinite-volume Gibbs measure, and strictly positive spectral gap on discrete lattice for $\beta < \beta_0$.
11. **`WHAT_REMAINS_OPEN`:** Any control for $\beta \ge \beta_0$; crossing the intermediate-coupling window $\beta \sim 1$; continuum limit $a \to 0$.

---

### Entry 4: THM-YM-0027 (Shen, Zhu, Zhu 2023)
- **Theorem ID:** `THM-YM-0027`
- **Source Citation:** H. Shen, R. Zhu, X. Zhu, *Comm. Math. Phys.* **400** (2023), pp. 805–851 (`PAPER-MOD-007`).
1. **`GAUGE_GROUP`:** Compact Lie group $G$ (specifically $SU(N)$).
2. **`DIMENSION`:** $d \ge 2$ ($d = 4$ included).
3. **`LATTICE_SPACING_SCOPE`:** Fixed lattice cutoff $a > 0$.
4. **`VOLUME_SCOPE`:** Infinite volume $\mathbb{Z}^d$.
5. **`COUPLING_PARAMETER`:** Strong coupling: $\beta < \beta_0(d, G)$.
6. **`OBSERVABLE_SCOPE`:** Smooth cylinder functions on configuration space $G^{E(\mathbb{Z}^d)}$; Dirichlet form $\mathcal{E}(f, f)$.
7. **`GAP_OR_DECAY_PROPERTY`:** Uniform Poincaré inequality $\text{Var}_{\mu_\infty}(f) \le C_{\text{PI}}(\beta) \mathcal{E}(f, f)$; strictly positive spectral gap $\text{gap}(-\mathcal{L}) \ge C_{\text{PI}}(\beta)^{-1} > 0$; exponential decay of gauge-invariant correlations.
8. **`UNIFORMITY_ESTABLISHED`:** Uniform in volume $\Lambda \to \mathbb{Z}^d$ for $\beta < \beta_0$.
9. **`CONTINUUM_LIMIT_STATUS`:** **BLOCKED.** Bakry–Émery Ricci curvature bound degenerates as $\beta \to \beta_0$; completely inapplicable to $\beta \to \infty$.
10. **`WHAT_IS_ACTUALLY_PROVED`:** Existence and uniqueness of infinite-volume Gibbs measure via Langevin diffusion, uniform Poincaré/log-Sobolev inequalities, and strictly positive spectral gap on the lattice at strong coupling.
11. **`WHAT_REMAINS_OPEN`:** Extension beyond $\beta_0$; non-perturbative scaling toward the continuum limit $\beta \to \infty$.

---

### Entry 5: THM-YM-0028 (Cao, Nissim, Sheffield 2025)
- **Theorem ID:** `THM-YM-0028`
- **Source Citation:** Y. Cao, E. Nissim, S. Sheffield, *arXiv:2505.16585* (2025) (`PAPER-MOD-008`).
1. **`GAUGE_GROUP`:** Classical Lie groups: $SU(N)$, $SO(N)$, $Sp(N)$.
2. **`DIMENSION`:** $d \ge 2$ ($d = 4$ included).
3. **`LATTICE_SPACING_SCOPE`:** Fixed lattice cutoff $a > 0$.
4. **`VOLUME_SCOPE`:** Infinite lattice $\mathbb{Z}^d$.
5. **`COUPLING_PARAMETER`:** Expanded strong-coupling regime: $0 \le \beta < \beta_1(d, G)$ (where $\beta_1 > \beta_0$).
6. **`OBSERVABLE_SCOPE`:** Wilson loop expectation $\langle W(C) \rangle$.
7. **`GAP_OR_DECAY_PROPERTY`:** Area law decay: $\langle W(C) \rangle \le C \exp(-\sigma(\beta) \text{Area}(C))$ with strictly positive string tension bound $\sigma(\beta) \ge \sigma_0 > 0$.
8. **`UNIFORMITY_ESTABLISHED`:** Uniform in loop size over expanded coupling regime $\beta \in [0, \beta_1)$.
9. **`CONTINUUM_LIMIT_STATUS`:** **BLOCKED.** Restricted to fixed lattice $a > 0$; does not establish physical string tension scaling $\sigma_{\text{phys}} = \sigma / a^2$.
10. **`WHAT_IS_ACTUALLY_PROVED`:** Rigorous expansion of the coupling range exhibiting Wilson loop area law using random surface representations and stochastic couplings.
11. **`WHAT_REMAINS_OPEN`:** Continuum limit $a \to 0$; spectral mass gap for local glueball operators; scaling through intermediate crossover window.

---

## 3. Comparative 11-Dimensional Synthesis Table

| Theorem ID | Gauge Group | $d$ | Lattice $a$ | Volume | Coupling $\beta$ | Primary Observable | Gap / Decay Property | Uniformity Scope | Continuum Status | Epistemic Status |
|---|---|---|---|---|---|---|---|---|---|---|
| **`THM-YM-0008`** | Compact $G$ | 4 | Fixed $a > 0$ | Finite / $\infty$ | $\beta \ll 1$ | Wilson loop $W(C)$ | Area law: $\sigma > 0$ | Uniform in loop size | **BLOCKED** ($\beta \to \infty$) | `PROVED_BY_SOURCE` |
| **`THM-YM-0009`** | Compact $G$ | 2–4 | Fixed $a > 0$ | Bisected $\Lambda$ | $\forall \beta \in (0, \infty)$ | Transfer matrix $\mathbb{T}$ | $\mathbb{T} = e^{-a H} > 0$, $H \ge 0$ | Exact for all $\beta$ | **BLOCKED** ($\Delta(a) \text{ as } a \to 0$) | `PROVED_BY_SOURCE` |
| **`THM-YM-0015`** | Compact $G$ | 2–4 | Fixed $a > 0$ | Infinite $\mathbb{Z}^d$ | $\beta < \beta_0(d, G)$ | Correlations $\langle A B \rangle_T$ | $\Delta_{\text{lat}} > 0$, $m_{\text{lat}} > 0$ | Uniform in volume | **BLOCKED** ($\beta \ge \beta_0$) | `PROVED_BY_SOURCE` |
| **`THM-YM-0027`** | $SU(N)$ | 2–4 | Fixed $a > 0$ | Infinite $\mathbb{Z}^d$ | $\beta < \beta_0(d, G)$ | Dirichlet form $\mathcal{E}(f, f)$ | Poincaré gap: $C_{\text{PI}} < \infty$ | Uniform in volume | **BLOCKED** ($\beta \ge \beta_0$) | `PROVED_BY_SOURCE` |
| **`THM-YM-0028`** | $SU, SO, Sp$ | 2–4 | Fixed $a > 0$ | Infinite $\mathbb{Z}^d$ | $\beta < \beta_1(d, G)$ | Wilson loop $W(C)$ | Area law: $\sigma(\beta) > 0$ | Uniform in loop size | **BLOCKED** ($a \to 0$) | `PROVED_BY_SOURCE` |
