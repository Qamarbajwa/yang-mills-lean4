# YM-015R2: NONPERTURBATIVE FIXED-FLOW CONTINUUM TARGET (`YM-015F-TARGET`)

## 1. Specification of the Minimum Target

The primary scientific objective of Task `YM-015R2` is to establish the non-perturbative continuum compactness of gauge-invariant flowed observables at fixed flow time $t > 0$, formally designated:
$$\mathbf{YM\text{-}015F\text{-}TARGET — NONPERTURBATIVE\ FIXED\text{-}FLOW\ CONTINUUM\ COMPACTNESS}$$

This target closes the sub-edge **`E-UV-FLOWED`** without relying on the downstream $t \downarrow 0$ local limit or unproved reflection positivity.

### Mathematical Framework:
1. **Physical Spacetime:** Fix a finite physical Euclidean 4-torus $\mathbb{T}^4_{\mathrm{phys}} = (\mathbb{R}/L_{\mathrm{phys}}\mathbb{Z})^4$ of volume $V_{\mathrm{phys}} = L_{\mathrm{phys}}^4 < \infty$.
2. **Lattice Discretization:** Let $\Lambda_a = (a\mathbb{Z} / L_{\mathrm{phys}}\mathbb{Z})^4$ be hypercubic lattices with spacing $a_n \to 0$.
3. **Bare Coupling Trajectory:** Choose the two-loop asymptotically-free bare coupling trajectory $\beta(a) = 2N / g_0^2(a) \to \infty$ defined by:
   $$\frac{1}{g_0^2(a)} = 2 b_0 \ln\left(\frac{1}{a\Lambda_{\overline{\mathrm{MS}}}}\right) + \frac{b_1}{b_0} \ln\left(2\ln\left(\frac{1}{a\Lambda_{\overline{\mathrm{MS}}}}\right)\right) + O\left(\frac{\ln\ln}{\ln^2}\right).$$
4. **Gauge-Invariant Flowed Observables:** For each flow time $t \ge t_{\min} > 0$, let $V_t(U)$ be the Wilson gradient flow. Consider the flowed action density operator:
   $$\mathcal{E}_a(x; t) \equiv -\frac{1}{2} \operatorname{Tr}\left( G_{\mu\nu}^a(x; t) G_{\mu\nu}^a(x; t) \right),$$
   where $G_{\mu\nu}^a(x; t)$ is the symmetric cloverleaf lattice field-strength tensor built from flowed links $V_t(U)$.
5. **Smeared Approximants:** For smooth test functions $f \in C^\infty(\mathbb{T}^4_{\mathrm{phys}})$, define:
   $$\mathcal{O}_{a,t}(f) \equiv a^4 \sum_{x \in \Lambda_a} f(x) \mathcal{E}_a(x; t).$$

---

## 2. Formulation of Theorem YM-015F-L1: Uniform Smeared Schwinger Bound

The core load-bearing estimate required to establish precompactness is:

### Theorem YM-015F-L1 (Non-Perturbative Fixed-Flow Smeared Bound)
Let $N \ge 2$, $L_{\mathrm{phys}} < \infty$, and $t_{\min} > 0$. For any moment order $k \ge 1$ and flow times $t_1, \dots, t_k \ge t_{\min}$, there exists a constant $C_k(t_{\min}, L_{\mathrm{phys}}, N) < \infty$ independent of the lattice spacing $a$ such that along the asymptotically-free trajectory $\beta(a)$:
$$\sup_{0 < a < a_0} \left| \left\langle \prod_{j=1}^k \mathcal{O}_{a, t_j}(f_j) \right\rangle_{\mu_{a, \beta(a)}} \right| \le C_k(t_{\min}, L_{\mathrm{phys}}, N) \prod_{j=1}^k \|f_j\|_{H^3(\mathbb{T}^4_{\mathrm{phys}})}.$$

### Decomposition and Proof Strategy:
To prove this theorem non-perturbatively requires decomposing the lattice expectation over Bałaban's multiscale small-field and large-field sectors:
$$\langle \dots \rangle_{\mu_a} = \int_{\Omega_{\mathrm{small}}} \dots d\mu_a + \int_{\Omega_{\mathrm{large}}} \dots d\mu_a.$$

1. **Large-Field Sector Bound:**
   On rough/large-field configurations, cloverleaf field-strengths are bounded deterministically by compact Lie group geometry:
   $$\|\mathcal{E}_a(x; t)\|_\infty \le \frac{8N}{a^4}.$$
   Therefore:
   $$\left| \int_{\Omega_{\mathrm{large}}} \prod_{j=1}^k \mathcal{O}_{a, t_j}(f_j) d\mu_a \right| \le \left(\frac{8N L_{\mathrm{phys}}^4}{a^4}\right)^k \left(\prod_{j=1}^k \|f_j\|_\infty\right) \mu_a(\Omega_{\mathrm{large}}).$$
   By Bałaban's large-field polymer estimates (CMP 109, 116), the probability of large-field polymer configurations decays exponentially with the action:
   $$\mu_a(\Omega_{\mathrm{large}}) \le \exp\left(- c_0 \beta(a) \frac{L_{\mathrm{phys}}^4}{a^4}\right).$$
   Because asymptotic freedom forces $\beta(a) \sim \ln(1/a) \to \infty$, the factor $\exp(-c_0 \beta(a)/a^4)$ dominates any power $a^{-4k}$. Thus:
   $$\lim_{a \to 0} \left| \int_{\Omega_{\mathrm{large}}} \prod_{j=1}^k \mathcal{O}_{a, t_j}(f_j) d\mu_a \right| = 0.$$
   The large-field sector contributes zero divergence in the continuum limit!

2. **Small-Field Sector Bound:**
   On the small-field sector $\Omega_{\mathrm{small}}$, the gauge field satisfies $\|A_\mu\|_\infty \le \chi(a) \ll 1$. Under the gradient flow:
   $$\partial_t B_\mu = D_\nu G_{\nu\mu} = \Delta B_\mu + [B_\nu, \partial_\nu B_\mu] + \dots$$
   Parabolic contractivity of the linear Laplacian yields:
   $$\|G_{\mu\nu}(t)\|_\infty \le \frac{C}{\sqrt{t}} \|B(0)\|_\infty \implies \|\mathcal{E}(t)\|_\infty \le \frac{C}{t}.$$
   Sobolev embedding $H^3(\mathbb{T}^4) \hookrightarrow C^0(\mathbb{T}^4)$ gives:
   $$\left| \sum_x a^4 f(x) \mathcal{E}(x; t) \right| \le \|f\|_\infty L_{\mathrm{phys}}^4 \frac{C}{t} \le C_S \|f\|_{H^3} L_{\mathrm{phys}}^4 \frac{C}{t}.$$

### Current Epistemic Status & Smallest Missing Estimate:
- **Small-Field Step:** Rigorous for continuum parabolic PDEs, but multiscale integration against Bałaban's effective Gaussian measures with non-local gauge-fixing requires observable-flow stability bounds.
- **Large-Field Step:** Rigorous Peierls bounds exist for the partition function, but the insertion of local operator prefactors into polymer cluster expansions is not explicitly documented in Bałaban's papers.
- **Classification:** **`PARTIAL_PROGRESS — CONDITIONAL_ON_BALABAN_OBSERVABLE_FLOW`**.
- **Smallest Missing Estimate:** A rigorous bound controlling the insertion of a flowed field-strength observable $\mathcal{E}_t(x)$ into Bałaban's multiscale polymer representation at the crossover scale $k \sim k_{\mathrm{cross}}$.

---

## 3. Theorem YM-015F-L2: Subsequential Multilinear Continuum Limit

Given Theorem `YM-015F-L1`, we construct the subsequential continuum limit in the corrected functional analysis topology established in `YM-015R`.

### Functional Analysis Setting:
1. Let $\mathcal{H} = H^3(\mathbb{T}^4_{\mathrm{phys}})$. For each $k \ge 1$, consider the projective Banach tensor product:
   $$\mathcal{H}_\pi^{(k)} \equiv \underbrace{H^3(\mathbb{T}^4_{\mathrm{phys}}) \hat{\otimes}_\pi \dots \hat{\otimes}_\pi H^3(\mathbb{T}^4_{\mathrm{phys}})}_{k\text{ factors}}.$$
2. By Theorem `YM-015F-L1`, for each lattice spacing $a_n$, the $k$-point correlation defines a continuous multilinear functional:
   $$S_{k, a_n}(f_1, \dots, f_k) \equiv \left\langle \prod_{j=1}^k \mathcal{O}_{a_n, t_j}(f_j) \right\rangle_{\mu_{a_n}}.$$
   By the universal property of the projective tensor product, $S_{k, a_n}$ extends to a unique continuous linear functional:
   $$S_{k, a_n} \in \left( \mathcal{H}_\pi^{(k)} \right)^* \quad \text{with norm} \quad \|S_{k, a_n}\|_{(\mathcal{H}_\pi^{(k)})^*} \le C_k(t_{\min}, L_{\mathrm{phys}}, N).$$

### Theorem YM-015F-L2 (Subsequential Multilinear Distribution Extraction)
Under the uniform bound of Theorem `YM-015F-L1`:
1. **Weak-* Compactness:** By the Banach–Alaoglu theorem on the separable Banach space $\mathcal{H}_\pi^{(k)}$, the unit ball of $(\mathcal{H}_\pi^{(k)})^*$ is compact and metrizable in the weak-* topology.
2. **Diagonal Subsequence:** There exists a subsequence $a_{n_m} \to 0$ such that for all $k \ge 1$ simultaneously, the functionals converge in the weak-* topology:
   $$S_{k, a_{n_m}} \xrightarrow{w^*} S_k \in \left( \mathcal{H}_\pi^{(k)} \right)^*.$$
3. **Schwartz Kernel Representation:** Restricting to the dense nuclear subspace $C^\infty((\mathbb{T}^4_{\mathrm{phys}})^k) \subset \mathcal{H}_\pi^{(k)}$, the Schwartz Kernel Theorem guarantees that each $S_k$ is represented by a unique tempered distribution:
   $$S_k \in \mathcal{D}'\left((\mathbb{T}^4_{\mathrm{phys}})^k\right).$$
4. **Permutation Symmetry & Reality:** The limiting distributions inherit permutation symmetry and reality from the finite-lattice observables:
   $$S_k(f_{\sigma(1)}, \dots, f_{\sigma(k)}) = S_k(f_1, \dots, f_k), \quad S_k(\bar{f}_1, \dots, \bar{f}_k) = \overline{S_k(f_1, \dots, f_k)}.$$

### Epistemic Scope of L2:
The limiting system $(S_k)_{k=1}^\infty$ constitutes an **infinite family of Euclidean multilinear correlation distributions on flowed fields**.
It does **NOT** yet constitute an Osterwalder–Schrader physical Schwinger system, because:
- Exact reflection positivity (OS2) is unresolved at finite $t > 0$;
- Continuous $SO(4)$ rotational covariance (OS1) has only perturbative support;
- Cluster decomposition (OS4) requires the infinite-volume limit $L_{\mathrm{phys}} \to \infty$.

---

## 4. Upstream / Downstream Logical Boundary

```
[YM-011: Regulated UV Scale Transfer]
                 │
                 ▼
[YM-015F: Nonperturbative Fixed-Flow Continuum Compactness]
   - YM-015F-L1: Uniform Smeared Bound (Conditional)
   - YM-015F-L2: Subsequential Multilinear Limit in (H^3_pi)^k
                 │
        ┌────────┴────────┐
        ▼                 ▼
[YM-015L: Local Limit]  [YM-015-SP: Spatial Flow RP]
   t -> 0 OS2 Recovery    Exact RP on Time Slices
        │                 │
        └────────┬────────┘
                 ▼
[E-CROSSOVER / YM-012: Intermediate Coupling]
                 │
                 ▼
[YM-016: Thermodynamic Limit V -> infty & Mass Gap]
```

The construction of `YM-015F` is strictly upstream of the crossover window, the thermodynamic limit, and the physical mass gap.
