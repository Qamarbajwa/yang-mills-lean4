# YM-005 Strong-Coupling Cluster Expansion Ledger

## 1. The High-Temperature Character Expansion

The rigorous construction of non-trivial lattice gauge measures at strong coupling rests on high-temperature polymer and cluster expansions developed by Osterwalder & Seiler (1978), Gross (1979), and Seiler (1982).

### 1.1 Character Decomposition of the Plaquette Factor
Let $G$ be a compact Lie group (e.g. $SU(N)$) with irreducible unitary representations labeled by $r \in \hat{G}$, character $\chi_r(U) = \text{Tr}_r(U)$, and dimension $d_r = \chi_r(\mathbb{I})$.
By the Peter–Weyl theorem, class functions on $G$ expand into characters:
$$\exp\left(\frac{\beta}{2N} \text{Re} \text{Tr}_F(U_p)\right) = c_0(\beta) \left[ 1 + \sum_{r \ne 0} d_r a_r(\beta) \chi_r(U_p) \right]$$
where the Fourier–character coefficients are:
$$c_0(\beta) = \int_G \exp\left(\frac{\beta}{2N} \text{Re} \text{Tr}_F(U)\right) dU$$
$$a_r(\beta) = \frac{1}{d_r c_0(\beta)} \int_G \exp\left(\frac{\beta}{2N} \text{Re} \text{Tr}_F(U)\right) \chi_r(U)^* dU$$

### 1.2 Scaling of Character Coefficients at Strong Coupling ($\beta \to 0$)
For small $\beta$, the Taylor series expansion yields power-law scaling in $\beta$ determined by representation weight:
- For $SU(2)$, representations are labeled by spin $j \in \{0, \frac{1}{2}, 1, \dots\}$ with dimension $d_j = 2j+1$:
  $$a_j(\beta) = \frac{I_{2j+1}(\beta)}{I_1(\beta)} = \frac{\beta^{2j}}{(2j+1)! \, 2^{2j}} \left(1 + \mathcal{O}(\beta^2)\right)$$
- Specifically, for the fundamental representation ($j = 1/2$, $d_F = 2$):
  $$a_F(\beta) = \frac{I_2(\beta)}{I_1(\beta)} = \frac{\beta}{4} + \mathcal{O}(\beta^3)$$
- For the adjoint representation ($j = 1$, $d_{\text{adj}} = 3$):
  $$a_{\text{adj}}(\beta) = \frac{I_3(\beta)}{I_1(\beta)} = \frac{\beta^2}{24} + \mathcal{O}(\beta^4)$$
- In general for $SU(N)$, the fundamental representation scales as $a_F(\beta) \sim \mathcal{O}(\beta)$, and all non-trivial representations satisfy:
  $$|a_r(\beta)| \le C_r \beta^{|r|} \quad \text{for } \beta \le \beta_{\text{max}}$$

---

## 2. Abstract Polymer Representation

### 2.1 Definition of Polymers
The lattice partition function factors as:
$$Z_\Lambda = c_0(\beta)^{|P(\Lambda)|} \int_{\Omega_\Lambda} \prod_{p \in P(\Lambda)} \left( 1 + \sum_{r \ne 0} d_r a_r(\beta) \chi_r(U_p) \right) \prod_{\ell \in E(\Lambda)} dU_\ell$$
Expanding the product yields a sum over subsets of plaquettes $X \subset P(\Lambda)$ equipped with representation assignments $r: X \to \hat{G} \setminus \{0\}$.

A **polymer** $Y = (X, r)$ is a connected set of plaquettes (where connectedness means sharing at least one link), such that integrating the link Haar measures $\prod_{\ell} dU_\ell$ does not vanish:
$$\zeta(Y) = \int_{G^{E(Y)}} \prod_{p \in X} d_{r(p)} a_{r(p)}(\beta) \chi_{r(p)}(U_p) \prod_{\ell \in E(Y)} dU_\ell \ne 0$$
- **Link Integration Invariant:** By Schur's orthogonality relations, $\int_G \chi_r(U) dU = 0$ for $r \ne 0$. Therefore, for $\zeta(Y)$ to be non-zero, every link $\ell \in E(Y)$ must belong to at least two plaquettes in $Y$ (closed surfaces) or form a gauge-invariant singlet combination.
- **Minimal Polymer:** In pure gauge theory, the minimal closed polymer consists of the 6 faces of an elementary 3-cube on the lattice ($|Y_{\text{min}}| = 6$).

### 2.2 Compatibility Relation
Two polymers $Y_1, Y_2$ are **compatible** (denoted $Y_1 \nsim Y_2$) if they do not share any common links ($E(Y_1) \cap E(Y_2) = \emptyset$).
They are **incompatible** (denoted $Y_1 \sim Y_2$) if they share at least one link ($E(Y_1) \cap E(Y_2) \ne \emptyset$).

The partition function assumes the canonical polymer form:
$$\Xi_\Lambda = \frac{Z_\Lambda}{c_0(\beta)^{|P(\Lambda)|}} = \sum_{n=0}^\infty \frac{1}{n!} \sum_{\substack{Y_1, \dots, Y_n \\ Y_i \nsim Y_j \, (i \ne j)}} \prod_{i=1}^n \zeta(Y_i)$$

---

## 3. The Kotecký–Preiss Convergence Criterion

To establish absolute convergence of the cluster expansion for $\ln \Xi_\Lambda$, the polymer system must satisfy the Kotecký–Preiss criterion (1986) or the Dobrushin criterion (1996).

### 3.1 Polymer Activity Bound
For any polymer $Y = (X, r)$ with size $|Y| = |X|$ plaquettes:
$$|\zeta(Y)| \le \prod_{p \in X} (d_{r(p)} |a_{r(p)}(\beta)|) \le (K_0 \beta)^{|Y|}$$
where $K_0 = K_0(d, G) < \infty$ is a geometric combinatorial constant bounding the Haar integral trace contractions.

### 3.2 Inductive Tree Bound
Let $\mu: Y \mapsto \mu |Y|$ be a size-proportional weight with $\mu > 0$.
The Kotecký–Preiss condition requires:
$$\sum_{Y' \sim Y} |\zeta(Y')| e^{\mu |Y'|} \le \mu |Y| \quad \forall Y$$
Summing over all lattice polymers $Y'$ incident to a fixed link $\ell \in E(Y)$ on a $d$-dimensional hypercubic lattice:
- Each link is shared by $2(d-1)$ plaquettes.
- The number of connected polymers of size $n$ containing $\ell$ is bounded by $(C_{\text{geom}}(d))^n$.
- Therefore:
  $$\sum_{Y' \sim Y} |\zeta(Y')| e^{\mu |Y'|} \le |Y| \sum_{n=n_{\text{min}}}^\infty (C_{\text{geom}}(d))^n (K_0 \beta)^n e^{\mu n} = |Y| \frac{(C_{\text{geom}} K_0 e^\mu \beta)^{n_{\text{min}}}}{1 - C_{\text{geom}} K_0 e^\mu \beta}$$

### 3.3 Convergence Threshold $\beta_0(d, G)$
Sufficient contractivity holds whenever:
$$\beta < \beta_0(d, G) \equiv \frac{1}{C_{\text{geom}}(d) K_0(d, G) e^{\mu + 1}}$$
For $d = 4$ and $G = SU(2)$:
- $C_{\text{geom}}(4) \approx 12 - 20$ (polymer embedding constant on hypercubic lattice).
- $\beta_0(4, SU(2)) \sim 0.05 - 0.25$ (`PROJECT_ESTIMATE`).

---

## 4. Rigorous Mathematical Consequences of Convergence

For all $\beta \in [0, \beta_0(d, G))$, the Kotecký–Preiss theorem yields four definitive mathematical results (`PROVED_BY_SOURCE`, Seiler 1982, Gross 1979):

### 4.1 Thermodynamic Free Energy Analyticity
The infinite-volume pressure / free energy density exists:
$$f(\beta) = \lim_{\Lambda \to \mathbb{Z}^4} \frac{1}{|\Lambda|} \ln Z_\Lambda = \ln c_0(\beta) + \sum_{n=1}^\infty \sum_{\substack{(Y_1, \dots, Y_n) \\ \text{connected cluster}}} \frac{a(Y_1, \dots, Y_n)}{n!} \prod_{i=1}^n \zeta(Y_i)$$
The series converges uniformly and absolutely, proving that $f(\beta)$ is real-analytic in $\beta \in [0, \beta_0)$. There are **no phase transitions** in the strong-coupling domain $\beta < \beta_0$.

### 4.2 Uniqueness of the Infinite-Volume Gibbs Measure
The thermodynamic limit $\Lambda \to \mathbb{Z}^4$ is independent of boundary conditions (free, periodic, or Dirichlet). The infinite-volume Gibbs measure $\mu_\infty$ on $G^{E(\mathbb{Z}^4)}$ exists, is unique, and is invariant under lattice translations and hypercubic rotations $O(4, \mathbb{Z})$.

### 4.3 Exponential Correlation Decay (Mass Gap on the Lattice)
For any two gauge-invariant local observables $A, B$ supported on disjoint subsets $\text{supp}(A), \text{supp}(B) \subset \mathbb{Z}^4$:
$$|\langle A B \rangle_\infty - \langle A \rangle_\infty \langle B \rangle_\infty| \le C(A, B) \exp\left( - m_{\text{lat}}(\beta) \, d(\text{supp}(A), \text{supp}(B)) \right)$$
where the dimensionless lattice mass gap satisfies the asymptotic bound:
$$m_{\text{lat}}(\beta) \ge n_{\text{min}} \ln(1 / \beta) - \mathcal{O}(1) > 0 \quad \text{as } \beta \to 0$$
For minimal glueball operators ($n_{\text{min}} = 4$ plaquettes around a temporal loop):
$$m_{\text{lat}}(\beta) = 4 \ln(1/\beta) + \mathcal{O}(1)$$

### 4.4 Transfer Matrix Spectral Gap
By the Osterwalder–Seiler reconstruction theorem, exponential decay in temporal distance implies that the lattice transfer matrix $\mathbb{T} = e^{-a H_{\text{lat}}}$ has an isolated vacuum eigenvalue at 1, with physical spectral gap:
$$\Delta_{\text{lat}}(\beta, a) = -\frac{1}{a} \ln \lambda_1(\beta) \ge \frac{m_{\text{lat}}(\beta)}{a} > 0$$

---

## 5. Audit of Failure Language: Stopping Point at $\beta_0$

In compliance with **ROS v1.0 Law 2**, failure language must be strictly calibrated:

| Mathematical Statement | Epistemic Classification | Justification & Precise Meaning |
|---|---|---|
| *"For $\beta \ge \beta_0$, the polymer expansion Kotecký–Preiss criterion is no longer satisfied"* | `PROVED_BY_SOURCE` | Exact mathematical fact: the activity series bound $\sum |\zeta| e^{\mu |Y|} < \mu |Y|$ fails for $\beta \ge \beta_0$. |
| *"The method of high-temperature cluster expansions ceases to prove exponential clustering for $\beta \ge \beta_0$"* | `PROVED_BY_SOURCE` | Methodological stopping point: the specific bounding technique loses contractivity. |
| *"Lattice Yang–Mills undergoes a physical phase transition at $\beta_0$"* | `FALSE / REFUTED` | For 4D pure non-Abelian $SU(N)$ lattice gauge theory, numerical simulations and analytic arguments establish that there is **no non-analyticity or phase transition** at $\beta_0$; it is an analytic crossover. (In contrast, 4D $U(1)$ has a genuine phase transition at $\beta_c \approx 1.01$). |
| *"The lattice mass gap $\Delta_{\text{lat}}$ vanishes at $\beta_0$"* | `NOT_ESTABLISHED / UNPROVED` | No primary source establishes that the spectral gap closes at $\beta_0$. It is an unbridged boundary of the cluster expansion machinery. |
| *"Cluster expansions cannot reach the continuum limit $\beta \to \infty$"* | `PROVED_BY_SOURCE` | The continuum limit requires $\beta \to \infty$, which lies infinitely far outside the convergence radius $\beta < \beta_0$. |
