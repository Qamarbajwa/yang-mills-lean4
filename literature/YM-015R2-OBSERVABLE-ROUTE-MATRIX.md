# YM-015R2: OBSERVABLE FAMILY EVALUATION & ROUTE DECISION MATRIX

## 1. Executive Summary & Design Scope

Task `YM-015R2` establishes a comprehensive, mathematically rigorous comparison of candidate observable families and architectural routes for constructing the continuum limit of four-dimensional Yang–Mills theory upstream of the crossover and thermodynamic limits.

Temporal locality is treated as an explicit, non-negotiable **design constraint** for Osterwalder–Schrader reconstruction, rather than an afterthought sacrificed for ultraviolet smoothing convenience.

---

## 2. Observable Family Comparison & Temporal Locality Taxonomy

Every candidate observable family is assigned one of four strict temporal locality states:
1. **`STRICT_TIME_SLICE_LOCAL`:** The observable depends exclusively on bare field variables on a single discrete Euclidean time slice $x_4$.
2. **`FINITE_TIME_SUPPORT`:** The observable depends on bare fields within a compact, finite time interval $x_4 \in [t_a, t_b]$.
3. **`EXPONENTIALLY_TIME_NONLOCAL`:** The observable depends on bare fields across all Euclidean times, with analytic influence decaying exponentially as $e^{-|x_4 - y_4|^2/(4t)}$ or $e^{-m|x_4 - y_4|}$.
4. **`GLOBALLY_TIME_NONLOCAL`:** The observable has power-law or non-decaying dependence across all Euclidean times (e.g. global gauge-fixed fields, global Polyakov loops).

### Family Comparison Table:

| Family ID | Description | Definition | Temporal Locality State | Exact Lattice RP | 4D UV Finiteness ($Z \equiv 1$) | $O(4)$ Symmetry |
|---|---|---|---|---|---|---|
| **Family 1** | 4D Gradient-Flow Field Strength | $\mathcal{E}(x; t) = -\frac{1}{2}\operatorname{Tr}(G_{\mu\nu}^2(x; t))$ via 4D flow $\partial_t B_\mu = D_\nu G_{\nu\mu}$ | **`EXPONENTIALLY_TIME_NONLOCAL`** | **UNRESOLVED** (Standard inheritance fails) | **YES** (Lüscher–Weisz all-orders finiteness) | **YES** (Preserves hypercubic $H_4 \to SO(4)$) |
| **Family 2** | Spatial-Gradient-Flow Observables | $\mathcal{E}_{\mathrm{sp}}(\vec{x}, x_4; t) = -\frac{1}{2}\operatorname{Tr}(G_{ij}^2)$ via spatial flow $\partial_t B_i = D_j G_{ji}$ | **`STRICT_TIME_SLICE_LOCAL`** | **EXACT** ($\mathcal{O} \in \mathcal{A}_+$ identically) | **NO** (Temporal loops unsmoothed; $Z \ne 1$) | **NO** (Explicitly broken to $SO(3) \times \mathbb{Z}_2$) |
| **Family 3** | Time-Slice Spatially Smeared Loops | Smeared spatial loops $W(C_{\vec{x}})$ via stout / midpoint-exponential blocking on slice $x_4$ | **`STRICT_TIME_SLICE_LOCAL`** | **EXACT** ($\mathcal{O} \in \mathcal{A}_+$ identically) | **NO** (Requires perimeter / loop renormalization) | **NO** (Explicitly broken to $SO(3) \times \mathbb{Z}_2$) |
| **Family 4** | Unsmeared Bare Local Curvature | Bare lattice plaquette $1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_{\mu\nu}(x))$ at $t=0$ | **`STRICT_TIME_SLICE_LOCAL`** | **EXACT** ($\mathcal{O} \in \mathcal{A}_+$ identically) | **NO** (Severe $a^{-4}$ power divergences & mixing) | **YES** (Hypercubic $H_4$) |

---

## 3. Comprehensive Mathematical Decision Matrix Across Architectural Routes

The four candidate routes are evaluated below across eight purely factual mathematical properties:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                    MATHEMATICAL ROUTE DECISION MATRIX (YM-015R2)                       │
├──────────────────────────┬──────────────┬──────────────┬───────────────┬───────────────┤
│ Property                 │ Route 1      │ Route 2      │ Route 3       │ Route 4       │
│                          │ 4D Flow +    │ Spatial-Only │ Time-Slice    │ Unsmeared     │
│                          │ Two-Stage    │ Flow         │ Smeared Loops │ Bare Local    │
├──────────────────────────┼──────────────┼──────────────┼───────────────┼───────────────┤
│ 1. Temporal Locality     │ Exp. Nonlocal│ Strict Slice │ Strict Slice  │ Strict Slice  │
│ 2. Gauge Invariance      │ Exact        │ Exact        │ Exact         │ Exact         │
│ 3. Renormalization       │ Zero (Z=1)   │ Medium-High  │ High          │ Extreme       │
│    Burden                │ at t > 0     │ (temporal div│ (perimeter law│ (a^-4 div)    │
│ 4. Nonperturbative      │ High (Bałaban│ Medium       │ High (YM-011  │ Blocked       │
│    Bound Availability    │ polymer RG)  │ (3D flow)    │ scale transfer│               │
│ 5. Compatibility with RP │ Unresolved   │ EXACT        │ EXACT         │ EXACT         │
│    at Finite Smoothing   │ at t > 0     │ (all t >= 0) │ (all R >= 0)  │ (at a > 0)    │
│ 6. Continuum Compactness │ Proved in    │ Spatial only;│ Distributional│ Fails without │
│    Topology              │ (H^3_pi)^k*  │ needs time f │ in time       │ subtraction   │
│ 7. Smoothing Removal     │ HIGH         │ N/A for RP;  │ N/A for RP;   │ N/A           │
│    (t -> 0) Difficulty   │ (small-t OPE)│ needed for 4D│ needed for 4D │ (already t=0) │
│ 8. O(4) Restoration      │ LOW          │ VERY HIGH    │ VERY HIGH     │ MEDIUM        │
│    Burden                │ (Symanzik a^2│ (broken H_4) │ (broken H_4)  │ (Symanzik a^2)│
└──────────────────────────┴──────────────┴──────────────┴───────────────┴───────────────┘
```

### Synthesis of the Route Dichotomy:
- **The Locality vs. Symmetry Trade-Off:**
  - **Routes 2 & 3 (Spatial Flow / Spatial Smearing):** Unconditionally solve Reflection Positivity (OS2) on the lattice and preserve it through the continuum limit. However, they destroy four-dimensional Euclidean rotational invariance ($SO(4)$) at the regulated level, creating an enormous downstream burden to prove isotropy restoration.
  - **Route 1 (4D Gradient Flow + Two-Stage Limit):** Unconditionally preserves hypercubic symmetry $H_4 \to SO(4)$ and provides universal UV finiteness ($Z \equiv 1$), but leaves exact reflection positivity open at finite flow time $t > 0$, requiring an eventual $t \downarrow 0$ limit.
  - **Route 4 (Unsmeared Bare Observables):** Constructively blocked due to severe $a^{-4}$ ultraviolet divergences.

---

## 4. Exact Reflection Positivity Recovery Criteria

To avoid premature acceptance of reflection positivity, the project adopts three mutually exclusive, rigorous criteria.
Exact Osterwalder–Schrader reflection positivity (OS2) may be declared recovered if and only if at least one of the following criteria is mathematically proved:

### Criterion A (Direct Lattice Inheritance on Time Slices)
A local or time-slice continuum observable algebra $\mathcal{A}_{\mathrm{cont}}$ is constructed directly such that every generator $A \in \mathcal{A}_{\mathrm{cont}}$ with support in $x_4 > 0$ is the strong or weak limit of lattice observables $A_a \in \mathcal{A}_+$:
$$\forall A \in \mathcal{A}_{\mathrm{cont}, +}, \quad \langle \Theta(A) A \rangle_{\mathrm{cont}} = \lim_{a \to 0} \langle \Theta(A_a) A_a \rangle_{\mu_a} \ge 0.$$
*(Satisfied by Spatial Gradient Flow Route 2 and Spatial Smearing Route 3).*

### Criterion B (Two-Stage OS Form Limit)
There exists a sequence of flowed observables $A_t$ at flow time $t > 0$ such that as $t \downarrow 0$, $A_t$ converges to a local continuum observable $A_0 \in \mathcal{A}_{\mathrm{cont}, +}$ in a topology strong enough to guarantee convergence of the reflection-positive quadratic form:
$$\lim_{t \downarrow 0} \langle \Theta(A_t) A_t \rangle_{\mathrm{cont}} = \langle \Theta(A_0) A_0 \rangle_{\mathrm{cont}} \ge 0.$$
*(The target of Route C / Route 1).*

### Criterion C (Exact Non-Local Positivity Theorem)
A novel mathematical theorem is established proving that the non-local flowed observable algebra $\mathcal{A}_t$ at finite flow time $t > 0$ satisfies:
$$\langle \Theta(F_t) F_t \rangle_{\mathrm{cont}} \ge 0 \quad \forall F_t \in \mathcal{A}_{t, +},$$
despite the fact that $F_t$ receives non-zero support from bare links in the negative-time half-space.

---

## 5. Specification of Downstream Flowed-to-Local Target (`YM-015L-TARGET`)

If and only if the fixed-flow continuum limit `E-UV-FLOWED` is established, the project defines:
$$\mathbf{YM\text{-}015L\text{-}TARGET — FLOWED\text{-}TO\text{-}LOCAL\ LIMIT}$$

### Formal Target Statement:
Construct a local, unsmeared continuum operator family $\mathcal{O}_0(x)$ such that for test functions $f \in C_0^\infty(\mathbb{T}^4_{\mathrm{phys}})$ with $\operatorname{supp} f \subset \{x_4 > 0\}$:
1. **OPE Convergence:**
   $$\lim_{t \downarrow 0} \mathcal{O}_t(f) = \mathcal{O}_0(f) \quad \text{in } \mathcal{D}'(\mathbb{T}^4_{\mathrm{phys}}).$$
2. **Contact Subtractions:**
   All short-distance singularities of the form $t^{-k}$ and $|x - y|^{-2k}$ are absorbed by a finite number of local counterterms determined by the small-flow-time expansion:
   $$\mathcal{E}(x; t) \sim c_0(t) \mathbf{1} + c_1(t) \mathcal{O}_0(x) + O(t).$$
3. **OS Form Non-Negativity (Criterion B):**
   $$\langle \Theta(\mathcal{O}_0(f)) \mathcal{O}_0(f) \rangle \ge 0.$$

---

## 6. Smallest Missing Load-Bearing Theorem Identified

Comparing all routes and criteria, the project identifies the **smallest currently unproved load-bearing theorem**:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                 SMALLEST UNPROVED LOAD-BEARING THEOREM                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Title: Non-Perturbative Multiscale Insertion Bound for Flowed Field Strength    │
│ Target ID: THM-YM-015F-L1                                                       │
│ Statement: sup_{0 < a < a_0} |< O_{a,t}(f) >| <= C(t, L, N) ||f||_{H^3}         │
│ Core Obstruction: Inserting the non-local cloverleaf flowed observable          │
│ into Bałaban's multiscale polymer expansion requires proving that the flow      │
│ derivative ||delta V_t / delta U|| does not spoil polymer cluster convergence.  │
└─────────────────────────────────────────────────────────────────────────────────┘
```
This confirms that the primary bottleneck of `E-UV-FREE-CONT` is **not** the functional-analysis topology (which was solved in `YM-015R`), but the **non-perturbative observable flow bound across Bałaban's multiscale effective measures**.
