# YM-005 Lattice Formalism & Transfer Matrix Audit

## 1. Geometric and Measure-Theoretic Foundation

Lattice gauge theory provides a mathematically non-perturbative regularization of non-Abelian gauge fields on a hypercubic Euclidean lattice $\Lambda \subset a \mathbb{Z}^4$ with lattice spacing $a > 0$.

### 1.1 Lattice Geometry and Variables
- **Lattice Sites:** Vertices $x \in \Lambda = (a \mathbb{Z})^4 \cap [-L, L]^4$.
- **Oriented Links:** Directed bonds $\ell = (x, \mu)$ from $x$ to $x + a \hat{\mu}$, with $\mu \in \{0, 1, 2, 3\}$. The reversed link is denoted $\ell^{-1} = (x + a \hat{\mu}, -\mu)$.
- **Plaquettes:** Elementary oriented 2-cells $p = (x, \mu, \nu)$ with $\mu < \nu$, bounded by four links:
  $$\partial p = (x, \mu) \circ (x + a \hat{\mu}, \nu) \circ (x + a \hat{\mu} + a \hat{\nu}, -\mu) \circ (x + a \hat{\nu}, -\nu)$$
- **Gauge Group:** Compact Lie group $G$ (for pure Yang–Mills, $G = SU(N)$, typically $SU(2)$ or $SU(3)$), endowed with normalized invariant Haar measure $dU$:
  $$\int_G dU = 1, \quad \int_G f(g U) dU = \int_G f(U g) dU = \int_G f(U) dU \quad \forall g \in G$$
- **Configuration Space:** $\Omega_\Lambda = G^{E(\Lambda)}$, where $E(\Lambda)$ is the set of unoriented links. Each configuration is an assignment $U: \ell \mapsto U_\ell \in G$, with the convention $U_{\ell^{-1}} = U_\ell^\dagger = U_\ell^{-1}$.
- **Plaquette Holonomy:** The path-ordered product of link variables around $p$:
  $$U_p = U_{x,\mu} U_{x+a\hat{\mu},\nu} U_{x+a\hat{\nu},\mu}^\dagger U_{x,\nu}^\dagger \in G$$

### 1.2 Gauge Invariance on the Lattice
A gauge transformation is an arbitrary map $g: \Lambda \to G$, acting on link variables as:
$$U_{x,\mu} \longmapsto U_{x,\mu}^g = g(x) U_{x,\mu} g(x + a \hat{\mu})^{-1}$$
Under this transformation, the plaquette holonomy transforms by local conjugation at the basepoint $x$:
$$U_p \longmapsto g(x) U_p g(x)^{-1}$$
Consequently, the class functions $\chi_r(U_p) = \text{Tr}_r(U_p)$ for any representation $r$ of $G$ are strictly gauge-invariant.

### 1.3 Wilson Plaquette Action
The canonical Wilson lattice action $S_W(U)$ is defined as:
$$S_W(U) = \frac{\beta}{2N} \sum_{p \in P(\Lambda)} \text{Re} \text{Tr}_F (\mathbb{I} - U_p)$$
where:
- $\beta = \frac{2N}{g^2}$ is the bare lattice coupling parameter (for $SU(N)$).
- $\text{Tr}_F$ is the trace in the fundamental defining representation of $G$.
- In the classical formal continuum limit $a \to 0$, expanding link variables via the exponential map $U_{x,\mu} = \exp(i a g A_\mu(x))$ yields:
  $$U_p = \exp\left(i a^2 g F_{\mu\nu}(x) + \mathcal{O}(a^3)\right)$$
  $$\text{Re} \text{Tr}_F (\mathbb{I} - U_p) = \frac{1}{2} a^4 g^2 \text{Tr}_F(F_{\mu\nu}^2) + \mathcal{O}(a^6)$$
  $$S_W(U) = \frac{a^4}{4} \sum_x \sum_{\mu,\nu} \text{Tr}_F(F_{\mu\nu}(x)^2) + \mathcal{O}(a^2) \xrightarrow{a \to 0} \frac{1}{4} \int d^4x F_{\mu\nu}^a F^{\mu\nu}_a$$
This proves formal classical consistency, but does **not** imply quantum measure convergence.

### 1.4 Finite-Volume Lattice Gibbs Measure
For a finite lattice volume $\Lambda$, the Euclidean probability measure is:
$$d\mu_\Lambda(U) = \frac{1}{Z_\Lambda} \exp\left(-S_W(U)\right) \prod_{\ell \in E(\Lambda)} dU_\ell$$
where the partition function $Z_\Lambda$ is strictly positive and finite by compactness of $G$:
$$Z_\Lambda = \int_{\Omega_\Lambda} \exp\left(-S_W(U)\right) \prod_{\ell \in E(\Lambda)} dU_\ell \in (0, \infty)$$

---

## 2. Reflection Positivity and the Transfer Matrix

The foundational breakthrough enabling a quantum-mechanical Hilbert space interpretation of Euclidean lattice gauge theories was the proof of reflection positivity by Osterwalder and Seiler (1978) and Lüscher (1977).

### 2.1 Reflection Operation
Consider the hypercubic lattice $\Lambda$. Choose the Euclidean time coordinate $x_0 \in a \mathbb{Z}$.
Define a spatial reflection hyperplane $\Pi$ bisecting the lattice orthogonal to the $x_0$ axis:
- **Case 1 (Site-centered hyperplane):** $\Pi = \{x : x_0 = 0\}$.
- **Case 2 (Link-centered hyperplane):** $\Pi = \{x : x_0 = a/2\}$, passing through temporal links.

Let $\theta$ be the Euclidean time reflection:
$$\theta(x_0, \mathbf{x}) = (-x_0, \mathbf{x}) \quad (\text{site-centered}), \quad \text{or} \quad \theta(x_0, \mathbf{x}) = (a - x_0, \mathbf{x}) \quad (\text{link-centered})$$
The reflection acts on link variables $\ell = (x, \mu)$ as:
$$\theta(U_{(x, \mu)}) = U_{(\theta x, \theta \mu)}^*$$
where $\theta \mu = \mu$ for spatial indices $\mu \in \{1, 2, 3\}$, and $\theta \mu = -\mu$ for the temporal index $\mu = 0$.

### 2.2 Reflection Positivity Theorem (Osterwalder & Seiler 1978)
Partition the lattice into positive-time $\Lambda_+ = \{x : x_0 > 0\}$, negative-time $\Lambda_- = \{x : x_0 < 0\}$, and boundary $\Lambda_0$.
Let $\mathcal{A}_+$ denote the algebra of cylinder functions $F(U)$ depending exclusively on links lying entirely in $\Lambda_+ \cup \Lambda_0$.

> **Theorem (Lattice Reflection Positivity):**
> For the Wilson lattice gauge theory with compact Lie group $G$ and bare coupling $\beta > 0$, the Gibbs expectation satisfies:
> $$\langle \theta F, F \rangle_\Lambda = \int_{\Omega_\Lambda} (\theta F(U))^* F(U) d\mu_\Lambda(U) \ge 0 \quad \forall F \in \mathcal{A}_+$$

**Proof Architecture:**
1. The Wilson action decouples across $\Pi$ into positive, negative, and crossing terms:
   $$S_W(U) = S_+(U) + \theta S_+(U) + S_0(U)$$
   where $S_+(U)$ contains plaquettes in $\Lambda_+$, and $S_0(U)$ contains plaquettes intersecting $\Pi$.
2. In temporal gauge or via character expansion of crossing plaquettes, $e^{-S_0}$ admits a sum of factored positive terms $\sum_k c_k \theta A_k A_k$ with $c_k \ge 0$.
3. Integration over positive-time and negative-time variables factors independently over the Haar product measure:
   $$\int (\theta F) F e^{-S_W} \prod dU = \sum_k c_k \left| \int F A_k e^{-S_+} \prod_{\ell \in \Lambda_+} dU_\ell \right|^2 \ge 0$$

### 2.3 Physical Lattice Hilbert Space $\mathcal{H}_{\text{lat}}$
Reflection positivity endows $\mathcal{A}_+$ with a positive semi-definite sesquilinear form:
$$(F, G)_{\mathcal{H}} = \langle \theta F, G \rangle_\Lambda$$
Define the null ideal $\mathcal{N} = \{F \in \mathcal{A}_+ : (F, F)_{\mathcal{H}} = 0\}$.
The physical lattice Hilbert space is the completion:
$$\mathcal{H}_{\text{lat}} = \overline{\mathcal{A}_+ / \mathcal{N}}$$
Restricting to gauge-invariant functionals yields the physical color-singlet Hilbert space:
$$\mathcal{H}_{\text{phys}} = \mathcal{H}_{\text{lat}}^{\text{gauge-invariant}}$$

### 2.4 Self-Adjoint Strictly Positive Transfer Matrix (Lüscher 1977)
Time translation by one lattice unit $a$ in the positive $x_0$ direction defines the transfer operator $\mathbb{T}: \mathcal{H}_{\text{phys}} \to \mathcal{H}_{\text{phys}}$.

> **Theorem (Lüscher 1977; Osterwalder–Seiler 1978):**
> The lattice transfer operator $\mathbb{T}$ satisfies:
> 1. $\mathbb{T}$ is a bounded, self-adjoint contraction on $\mathcal{H}_{\text{phys}}$:
>    $$\mathbb{T} = \mathbb{T}^\dagger, \quad 0 < \mathbb{T} \le \mathbb{I}$$
> 2. $\mathbb{T}$ is strictly positive: $\ker(\mathbb{T}) = \{0\}$.
> 3. The lattice Hamiltonian $H_{\text{lat}}$ is uniquely defined as a self-adjoint, positive operator:
>    $$H_{\text{lat}} = -\frac{1}{a} \ln \mathbb{T} \ge 0$$
> 4. The Euclidean correlation function of temporal displacements corresponds to quantum Hamiltonian evolution:
>    $$\langle \theta F, T_t G \rangle_\Lambda = (F, \mathbb{T}^{t/a} G)_{\mathcal{H}} = (F, e^{-t H_{\text{lat}}} G)_{\mathcal{H}} \quad \forall t = n a \ge 0$$

---

## 3. Lattice Spectral Gap vs. Continuum Mass Gap

The existence of a self-adjoint lattice Hamiltonian $H_{\text{lat}} \ge 0$ allows an exact definition of the lattice spectral gap:

### 3.1 Lattice Spectral Gap Definition
Let $|\Omega\rangle \in \mathcal{H}_{\text{phys}}$ be the normalized vacuum state corresponding to the constant function $F = \mathbb{I}$, satisfying $H_{\text{lat}} |\Omega\rangle = 0$ ($\mathbb{T} |\Omega\rangle = |\Omega\rangle$).
The lattice spectral gap $\Delta_{\text{lat}}$ is the distance between the vacuum eigenvalue 0 and the rest of the spectrum of $H_{\text{lat}}$:
$$\Delta_{\text{lat}}(\beta, a) = \inf \left\{ \text{spec}(H_{\text{lat}}) \setminus \{0\} \right\} = -\frac{1}{a} \ln \lambda_1(\beta)$$
where $\lambda_1(\beta) = \sup_{\psi \perp \Omega, \|\psi\|=1} (\psi, \mathbb{T} \psi) \in (0, 1)$.

### 3.2 Epistemic Invariant: Lattice Gap $\ne$ Continuum Clay Mass Gap
Under **`INV-YM005-001`**, establishing $\Delta_{\text{lat}}(\beta, a) > 0$ on a fixed lattice does **not** solve the Clay Millennium problem:
1. **Lattice Units:** At fixed $a > 0$, the lattice Hamiltonian has dimension of energy ($\Delta_{\text{lat}} = m_{\text{lat}} / a$). A non-zero dimensionless mass $m_{\text{lat}}(\beta) > 0$ means that correlations decay across a finite number of lattice sites.
2. **The Continuum Scaling Limit:** The continuum Clay mass gap $\Delta_{\text{continuum}}$ is defined as:
   $$\Delta_{\text{continuum}} = \lim_{\substack{a \to 0 \\ \beta \to \infty}} \frac{m_{\text{lat}}(\beta(a))}{a}$$
3. **The Scaling Failure Mode:** If $m_{\text{lat}}(\beta)$ remains non-zero as $a \to 0$ without scaling as $a \sim \exp(-1 / (2 b_0 g^2))$, then either:
   - $\Delta_{\text{continuum}} \to \infty$ (infinite physical mass, zero correlation length in physical units), or
   - The scaling trajectory cannot be tracked through the intermediate coupling crossover $\beta \sim 1$.
4. **Rotational Invariance Restoration:** The lattice Hamiltonian $H_{\text{lat}}$ generates discrete translations. Continuous $SO(4)$ Euclidean / $SO(1,3)$ Lorentz invariance is recovered only if the continuum limit exists and satisfies Osterwalder–Schrader axioms OS0–OS4.
