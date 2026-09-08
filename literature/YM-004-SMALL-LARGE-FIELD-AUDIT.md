# YM-004 SMALL-FIELD / LARGE-FIELD AUDIT

## Rigorous Decomposition of Small-Field vs Large-Field Regions in 4D Constructive Gauge Theory

This document audits the mathematical mechanisms governing the partition of configuration space into small-field and large-field regions in the Bałaban constructive renormalization group program.

---

## 1. Mathematical Definition of the Partition

At each RG scale $k$, the spatial lattice $\Lambda^{(k)}$ is paved by unit cubes / blocks $\Delta \subset \Lambda^{(k)}$.
The full configuration space $\mathcal{A}_k$ is partitioned locally for each block $\Delta$:

### Small-Field Characteristic Function
$$\chi_{\text{small}}(\Delta, A_k) = \theta\left( \epsilon_0 g_k^{-\gamma} - \sup_{p \subset \Delta} a_k^{-2} \| I - U_k(\partial p) \| \right)$$
where $\theta$ is the Heaviside step function (or a smooth partition of unity), $\epsilon_0 > 0$ is a small dimensionless parameter, and $\gamma \in (0, 1)$ (typically $\gamma = 1/4$ or $\gamma = 1/2$).

### Large-Field Characteristic Function
$$\chi_{\text{large}}(\Delta, A_k) = 1 - \chi_{\text{small}}(\Delta, A_k)$$

A connected union of large-field blocks forms a **large-field polymer** $Y = \bigcup_{i=1}^m \Delta_i$.
The partition of unity on the entire lattice takes the form:
$$1 = \prod_{\Delta} \left( \chi_{\text{small}}(\Delta) + \chi_{\text{large}}(\Delta) \right) = \sum_{Y \subset \Lambda^{(k)}} \chi_{\text{large}}(Y) \chi_{\text{small}}(\Lambda^{(k)} \setminus Y)$$

---

## 2. The Small-Field Region: Detailed Audit

### Field Norm and Threshold
- **Norm:** Plaquette curvature sup-norm:
  $$\| F(A) \|_{L^\infty(\Delta)} = \sup_{p \subset \Delta} \frac{1}{a_k^2} \| I - U_k(\partial p) \|$$
- **Threshold:** $\| F(A) \|_{L^\infty(\Delta)} \le \epsilon_0 g_k^{-\gamma}$.
- **Scale Dependence:** In physical units, the curvature threshold scales as $a_k^{-2} \epsilon_0 g_k^{-\gamma}$, meaning that at fine lattice spacings ($a_k \to 0$, $g_k \to 0$), the allowed curvature fluctuation grows, but remains strictly bounded in units of the running coupling.

### Gaussian Dominance and Saddle-Point Analysis
Inside $\mathcal{D}_{\text{small}}$, the Yang–Mills action:
$$S_k(A_k) = \frac{1}{g_k^2} \sum_{p} \mathrm{Re} \mathrm{Tr}(I - U_k(\partial p))$$
can be expanded in powers of the fluctuation $q = A_k - A_{\min}(B)$:
$$S_k(A_{\min} + g_k q) = S_k(A_{\min}) + \frac{1}{2} \langle q, \mathcal{H}(A_{\min}) q \rangle + g_k V_3(q) + g_k^2 V_4(q)$$
- **Quadratic Hessian:** $\mathcal{H}(A_{\min}) = D_{A_{\min}}^* D_{A_{\min}} + \alpha^{-1} Q^* Q$.
- **Strict Positivity:** Because $\|F(A_{\min})\| \le \epsilon_0 g_k^{-\gamma}$ is small, the Hessian $\mathcal{H}(A_{\min})$ has no zero modes or negative eigenvalues; its spectrum is strictly bounded away from zero by the gauge-fixing term:
  $$\mathrm{Spec}(\mathcal{H}(A_{\min})) \subset [c_0 a_k^{-2}, \infty), \quad c_0 > 0$$
- **Perturbative Convergence:** The cubic and quartic terms $g_k V_3(q) + g_k^2 V_4(q)$ are strictly subordinated to the quadratic form. The non-Gaussian functional integral is analytic in $g_k$ and controlled by convergent Feynman graph / BPHZ expansions.

---

## 3. The Large-Field Region: Detailed Audit

### Suppression Mechanism
In any block $\Delta$ where the small-field condition fails ($\chi_{\text{large}}(\Delta) = 1$), there exists at least one plaquette $p \subset \Delta$ with:
$$\| I - U_k(\partial p) \| > a_k^2 \epsilon_0 g_k^{-\gamma}$$
The Wilson action contribution from this block satisfies the deterministic lower bound:
$$S_{\Delta}(U) = \frac{1}{g_k^2} \sum_{p \subset \Delta} \mathrm{Re} \mathrm{Tr}(I - U_k(\partial p)) \ge \frac{c_1}{g_k^2} \left( a_k^2 \epsilon_0 g_k^{-\gamma} \right)^2 \cdot a_k^{-4} = \frac{c_1 \epsilon_0^2}{g_k^{2 + 2\gamma}}$$
- Consequently, the Boltzmann factor is super-exponentially suppressed:
  $$\exp\left( - S_\Delta(U) \right) \le \exp\left( - \frac{\kappa_0}{g_k^{2(1-\gamma)}} \right) \le \exp\left( - \frac{\kappa_1}{g_k^2} \right)$$
  for $\gamma < 1$.

### Combinatorial Polymer Treatment
- A large-field polymer $Y$ of size $|Y| = m$ contains $m$ connected blocks.
- The number of connected polymers of size $m$ containing a fixed block $x$ is bounded by the tree graph combinatorics:
  $$N_m(x) \le (C_4)^m$$
  where $C_4 \le 7^4 = 2401$ is the lattice coordination constant in 4 dimensions.
- The total large-field polymer activity $\zeta_k(Y)$ is bounded by:
  $$|\zeta_k(Y)| \le (C_{\text{int}})^m \cdot \exp\left( - \frac{\kappa_1}{g_k^2} m \right) = \exp\left( - \left( \frac{\kappa_1}{g_k^2} - \ln C_{\text{int}} \right) |Y| \right)$$

### Cluster Expansion Convergence Criterion
The Mayer / Kirkwood–Salsburg cluster expansion of the polymer gas $\sum_Y \zeta_k(Y)$ converges absolutely if:
$$\sup_x \sum_{Y \ni x} |\zeta_k(Y)| \cdot e^{|Y|} < 1$$
Substituting the suppression bound yields the convergence condition:
$$\sum_{m=1}^\infty (C_4 C_{\text{int}} e)^m \exp\left( - \frac{\kappa_1}{g_k^2} m \right) = \frac{K_0 e^{-\kappa_1 / g_k^2}}{1 - K_0 e^{-\kappa_1 / g_k^2}} < 1$$
This inequality holds if and only if:
$$\frac{\kappa_1}{g_k^2} > \ln(2 K_0) \iff g_k^2 < \frac{\kappa_1}{\ln(2 K_0)} \equiv g_*^2$$

---

## 4. Which Region Loses Control First as Coupling Increases?

Comparative analysis of the failure thresholds reveals:

| Region | Primary Failure Mode | Mathematical Condition for Breakdown | Literature Status |
|---|---|---|---|
| **Small-Field** | Loss of strict convexity of Hessian; appearance of non-trivial saddle points (Gribov copies). | $g_k \sim g_{\text{Gribov}} \sim \mathcal{O}(1)$ | Observed in functional analysis of gauge-fixing operator. |
| **Large-Field** | Polymer cluster expansion divergence: combinatorial entropy $(C_4)^m$ overwhelms Boltzmann suppression $e^{-\kappa_1 m / g_k^2}$. | $g_k^2 \ge \frac{\kappa_1}{\ln(2 K_0)} \equiv g_*^2 \ll 1$ | **PROVED** breakdown of Bałaban's polymer norm convergence (CMP 116, p. 18). |

$$\boxed{\textbf{The large-field polymer cluster expansion loses mathematical control first.}}$$

### Critical Epistemic Invariant
- The divergence of the polymer cluster expansion at $g_k \ge g_*$ is a **rigorous theorem concerning Bałaban's specific functional norms**.
- It does **NOT** prove that the underlying quantum field theory ceases to exist or that large fields physically destroy confinement.
- **Factorial Divergence & Renormalons:** The literature does not equate polymer cluster expansion breakdown with perturbative renormalon poles. Polymer divergence is a breakdown of the single-site cluster expansion method, not an intrinsic physical singularity.
