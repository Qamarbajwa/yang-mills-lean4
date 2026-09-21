# YM-005 Spectral Gap & Exponential Decay Audit

## 1. Dual Manifestations of the Mass Gap on the Lattice

In constructive quantum field theory and lattice statistical mechanics, the physical property of a "mass gap" manifests in two mathematically related but formally distinct ways:

### 1.1 Correlation Decay (Clustering Gap)
For a probability measure $\mu$ on configuration space $\Omega = G^{E(\mathbb{Z}^d)}$, the spatial/temporal correlation decay between two local gauge-invariant functionals $A, B$ supported on sets $\text{supp}(A), \text{supp}(B)$ separated by Euclidean distance $r = d(\text{supp}(A), \text{supp}(B))$ is defined as:
$$\text{Cov}_\mu(A, B) = \langle A B \rangle_\mu - \langle A \rangle_\mu \langle B \rangle_\mu$$
A theory exhibits **exponential clustering** if there exists a strictly positive mass $m_{\text{lat}} > 0$ such that:
$$|\text{Cov}_\mu(A, B)| \le C(A, B) \exp(-m_{\text{lat}} r) \quad \forall r \ge 0$$
The correlation length is defined as:
$$\xi_{\text{lat}} = \frac{1}{m_{\text{lat}}}$$

### 1.2 Transfer Matrix / Hamiltonian Spectral Gap
On a hypercubic lattice bisected by a time reflection hyperplane, reflection positivity constructs the physical Hilbert space $\mathcal{H}_{\text{phys}}$ and the self-adjoint transfer matrix $\mathbb{T} = e^{-a H_{\text{lat}}}$.
The **Hamiltonian spectral gap** is:
$$\Delta_{\text{lat}}(\beta, a) = \inf \left( \text{spec}(H_{\text{lat}}) \setminus \{0\} \right) = -\frac{1}{a} \ln \lambda_1(\beta)$$
where $\lambda_1 = \sup \{ (\psi, \mathbb{T} \psi)_{\mathcal{H}} : \|\psi\|=1, \psi \perp |\Omega\rangle \} < 1$.

### 1.3 Mathematical Equivalence on the Discrete Lattice
By the spectral theorem for self-adjoint operators (Osterwalder–Seiler 1978, Glimm–Jaffe 1987):
$$\langle \theta A, T_{na} B \rangle_\mu - \langle \theta A \rangle \langle B \rangle = (A, \mathbb{T}^n B)_{\mathcal{H}} - (A, \Omega)(\Omega, B) = \int_{\Delta_{\text{lat}}}^\infty e^{-t E} d\mu_{A,B}(E)$$
where $t = na$.
- If $\text{spec}(H_{\text{lat}}) \subseteq \{0\} \cup [\Delta_{\text{lat}}, \infty)$, then temporal correlations decay as $\exp(-t \Delta_{\text{lat}})$, yielding $m_{\text{lat}} = a \Delta_{\text{lat}}$.
- Conversely, if all gauge-invariant Euclidean correlation functions decay exponentially with rate $m_{\text{lat}} > 0$, the transfer matrix has an isolated eigenvalue at 1, and $\Delta_{\text{lat}} \ge m_{\text{lat}} / a > 0$.

---

## 2. Stochastic Analysis & Functional Inequalities (Shen–Zhu–Zhu 2023)

In 2023, H. Shen, R. Zhu, and X. Zhu developed a modern stochastic analysis framework for lattice Yang–Mills theories at strong coupling, establishing functional inequalities independent of volume.

### 2.1 The Lattice Langevin Diffusion Generator
Consider the lattice $\Lambda \subset \mathbb{Z}^d$ with link configuration $U \in G^{E(\Lambda)}$.
The Langevin dynamic is a diffusion process on the compact Riemannian manifold $\mathcal{M} = G^{E(\Lambda)}$ equipped with the product bi-invariant metric:
$$d U_\ell(t) = \nabla_{U_\ell} S_W(U) dt + \sqrt{2} d B_\ell(t) + \text{Stratonovich drift}$$
where $B_\ell$ is standard Brownian motion on Lie algebra $\mathfrak{g}$, and $\nabla_{U_\ell}$ is the Riemannian gradient.

The associated Markov diffusion generator is:
$$\mathcal{L} = \sum_{\ell \in E(\Lambda)} \left( \Delta_{G, \ell} - \nabla_{U_\ell} S_W(U) \cdot \nabla_{U_\ell} \right)$$
where $\Delta_{G, \ell}$ is the Laplace–Beltrami (Casimir) operator on $G$.

### 2.2 The Dirichlet Form and Poincaré Inequality
The Gibbs measure $d\mu_\Lambda(U) = Z_\Lambda^{-1} e^{-S_W(U)} \prod dU_\ell$ is the unique reversible stationary measure for $\mathcal{L}$.
The associated Dirichlet form is:
$$\mathcal{E}(f, f) = -\int_{\Omega_\Lambda} f (\mathcal{L} f) d\mu_\Lambda = \int_{\Omega_\Lambda} \sum_{\ell \in E(\Lambda)} \|\nabla_{U_\ell} f(U)\|^2 d\mu_\Lambda(U)$$
The measure $\mu_\Lambda$ satisfies a **Poincaré inequality** with constant $C_{\text{PI}}$ if for all smooth cylinder functions $f$:
$$\text{Var}_{\mu_\Lambda}(f) \equiv \int f^2 d\mu_\Lambda - \left(\int f d\mu_\Lambda\right)^2 \le C_{\text{PI}} \, \mathcal{E}(f, f)$$

### 2.3 The Log-Sobolev Inequality
The measure satisfies a **logarithmic Sobolev inequality** with constant $C_{\text{LSI}}$ if for all smooth positive functions $f$:
$$\text{Ent}_{\mu_\Lambda}(f^2) \equiv \int f^2 \ln\left(\frac{f^2}{\int f^2 d\mu_\Lambda}\right) d\mu_\Lambda \le 2 C_{\text{LSI}} \, \mathcal{E}(f, f)$$
By the Rothaus–Herbst theorem, $C_{\text{PI}} \le C_{\text{LSI}}$, and log-Sobolev implies hypercontractivity of the semigroup $P_t = e^{t \mathcal{L}}$.

### 2.4 The Shen–Zhu–Zhu Theorem (CMP 400, 2023)

> **Theorem (Shen, Zhu, Zhu 2023, Theorems 1.1–1.5):**
> Let $d \ge 2$, and let $G$ be a compact Lie group. There exists a strictly positive threshold $\beta_0 = \beta_0(d, G) > 0$ such that for all bare couplings $\beta \in [0, \beta_0)$:
> 1. **Uniform Poincaré Inequality:**
>    $$\sup_{\Lambda \subset \mathbb{Z}^d} C_{\text{PI}}(\beta, \Lambda) = C_{\text{PI}}(\beta) < \infty$$
>    The Poincaré constant is uniformly bounded independently of lattice volume $\Lambda$.
> 2. **Infinite-Volume Gibbs Measure:**
>    The thermodynamic limit $\mu_\infty = \lim_{\Lambda \to \mathbb{Z}^d} \mu_\Lambda$ exists, is unique on $G^{E(\mathbb{Z}^d)}$, and satisfies the infinite-volume Poincaré inequality with constant $C_{\text{PI}}(\beta)$.
> 3. **Lattice Spectral Gap:**
>    The generator $-\mathcal{L}$ has a strictly positive spectral gap on $L^2(\mu_\infty)$:
>    $$\text{gap}(-\mathcal{L}) \ge \frac{1}{C_{\text{PI}}(\beta)} > 0$$
> 4. **Exponential Correlation Decay:**
>    For any local gauge-invariant functionals $F, G$:
>    $$|\text{Cov}_{\mu_\infty}(F, G)| \le C(F, G) \exp\left( - m_{\text{lat}}(\beta) d(\text{supp}(F), \text{supp}(G)) \right)$$
>    with $m_{\text{lat}}(\beta) > 0$.

---

## 3. Terminal Obstruction of Stochastic Analysis

The mathematical mechanism behind Shen–Zhu–Zhu's proof is based on Bakry–Émery Ricci curvature bounds on Riemannian manifolds combined with spatial cluster estimates:

### 3.1 Bakry–Émery Curvature on Compact Lie Groups
On the Lie group $G$ with bi-invariant metric, the Ricci curvature tensor is positive: $\text{Ric}_G \ge \kappa_G \mathbb{I} > 0$ (for $SU(2)$, $G \cong S^3$, $\kappa_G = 1/2$).
When the Wilson action is coupled across plaquettes, the Hessian of the action perturbs the Ricci curvature:
$$\text{Ric}_{\mathcal{M}} + \nabla^2 S_W \ge \left( \kappa_G - C_{\text{action}} \beta \right) \mathbb{I}$$

### 3.2 Curvature Collapse at Strong-Coupling Threshold
- For $\beta < \beta_0$, the positive Ricci curvature of the compact group dominates the interaction Hessian, providing a uniform drift driving the system toward the unique equilibrium measure.
- As $\beta \to \beta_0$, the Bakry–Émery curvature $\kappa(\beta) = \kappa_G - C \beta \to 0$.
- For $\beta \ge \beta_0$, the curvature becomes negative. While the compact group Haar measure still provides a crude local Poincaré inequality on single links, the inter-link coupling destroys the uniform spatial contractivity.
- In the continuum limit $\beta \to \infty$ ($g \to 0$), the interaction term completely dominates the single-site Ricci curvature ($\kappa(\beta) \sim -C \beta \to -\infty$). The stochastic quantization method of Shen–Zhu–Zhu is **strictly incapable of reaching the continuum limit**.

```text
Stochastic / Curvature Contraction
[0 ─────────────── beta_0]  ───────── ? ───────── [beta -> infinity]
  PROVED LATTICE GAP       UNBRIDGED CROSSOVER       CONTINUUM LIMIT
 (Shen–Zhu–Zhu 2023)       (Curvature Lost)         (Clay Target)
```
