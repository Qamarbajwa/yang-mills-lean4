# YM-004 RG ARCHITECTURE

## Machine-Readable Renormalization Group Dependency Structure

This document details the functional-analytic architecture of the Bałaban multiscale block-spin renormalization group (RG) flow for 4D Euclidean $SU(N)$ Yang–Mills theory on a lattice.

---

## 1. Scale Sequence and Spatial Geometry

- **Base lattice:** $\Lambda^{(0)} = a_0 \mathbb{Z}^4 \cap \mathbb{T}^4$, with torus volume $V = L_0^4$.
- **Scale factor:** $L \in \mathbb{N}$, $L \ge 2$ (typically $L = 2$ or $L = 3$).
- **Scale hierarchy:**
  $$\Lambda^{(0)} \xrightarrow{Q} \Lambda^{(1)} \xrightarrow{Q} \Lambda^{(2)} \xrightarrow{Q} \cdots \xrightarrow{Q} \Lambda^{(k)} \xrightarrow{Q} \cdots \xrightarrow{Q} \Lambda^{(n)}$$
- **Lattice spacing at scale $k$:**
  $$a_k = L^k a_0$$
- **Number of cells at scale $k$:**
  $$|\Lambda^{(k)}| = \left( \frac{L_0}{a_k} \right)^4 = L^{-4k} |\Lambda^{(0)}|$$
- **Terminal scale index:**
  $$n = \left\lfloor \frac{\ln(L_0 / a_0)}{\ln L} \right\rfloor$$

---

## 2. The Multiscale Block-Spin Transformation $Q$

### Step Mapping
At step $k \to k+1$, the field configuration $A_k$ on links $\mathcal{B}(\Lambda^{(k)})$ is mapped to a coarsened connection $A_{k+1}$ on links $\mathcal{B}(\Lambda^{(k+1)})$:
$$A_{k+1}(b') = Q(A_k)(b'), \quad b' = \langle y, y + a_{k+1} \hat{\mu} \rangle \in \mathcal{B}(\Lambda^{(k+1)})$$

### Parallel-Transported Path Average
The discrete link $b'$ on the coarsened lattice spans $L$ elementary links of $\Lambda^{(k)}$. The operator $Q$ is defined via path-ordered averaging:
$$Q(A_k)(b') = \sum_{p \in \mathcal{P}(b')} w(p) \, \Omega(y, x_p; A_k) \, A_k(b_p) \, \Omega(x_p, y; A_k)$$
where:
- $\mathcal{P}(b')$ is a symmetric family of paths connecting the endpoints of $b'$.
- $w(p)$ are normalized geometric weights satisfying $\sum_p w(p) = 1$.
- $\Omega(y, x; A_k) = \mathcal{P} \exp\left( i \int_x^y A_k \right)$ is the parallel transporter along a fixed minimal tree, preserving gauge covariance up to local gauge transformations.

---

## 3. The Conditional Functional Integration

Given a background / coarse connection $B$ on $\Lambda^{(k+1)}$, the step from partition function $Z_k$ to $Z_{k+1}$ is governed by the conditional expectation:
$$\exp\left( - S_{k+1}(B) \right) = \int \mathcal{D} A_k \, \delta\left( Q(A_k) - B \right) \, \exp\left( - S_k(A_k) - G(A_k, B) \right)$$

### Gauge-Fixing Functional $G(A_k, B)$
To eliminate the gauge zero modes inside the blocks of size $L^4$, Bałaban introduces a block gauge-fixing term:
$$G(A_k, B) = \frac{1}{2\alpha} \| Q(A_k) - B \|_{L^2(\Lambda^{(k+1)})}^2 + \frac{1}{2\beta} \sum_{X \in \text{blocks}} \| d_{\Lambda^{(k)}}^* A_k \|_{L^2(X)}^2$$
with corresponding Faddeev–Popov determinant $\Delta_{\text{FP}}(A_k)$.

### Background Field Saddle-Point Splitting
For a given $B \in \mathcal{D}_{\text{small}}(k+1)$, there exists a unique classical minimizer $A_{\min}(B)$ on $\Lambda^{(k)}$ solving:
$$D_{A_{\min}}^* F(A_{\min}) + \alpha^{-1} Q^* (Q(A_{\min}) - B) = 0$$
The fluctuation field $q$ is defined by:
$$A_k = A_{\min}(B) + g_k q$$
The conditional functional integral then takes the form of a perturbative Gaussian expansion around $A_{\min}(B)$ plus non-Gaussian cluster corrections.

---

## 4. Scale-Step Effective Action Decomposition

At each scale $k$, the total effective weight factorizes into three distinct mathematical components:

$$Z_k(A_k) = \exp\left( - E_k(V) \right) \cdot \exp\left( - S_k(A_k) \right) \cdot \Xi_k(A_k)$$

### Component 1: Vacuum Energy Constant $E_k(V)$
- Represents accumulated vacuum energy density:
  $$E_k(V) = \sum_{j=0}^{k-1} e_j \cdot L^{-4j} V$$
- Proved to be strictly extensive: $E_k(V) = \mathcal{E}_k \cdot \mathrm{Vol}(\mathbb{T}^4)$.

### Component 2: Small-Field Effective Action $S_k(A_k)$
Valid in the small-field domain $\mathcal{D}_{\text{small}}(k) = \{ A_k : \sup_{p} \| F_p(A_k) \| \le \epsilon_0 g_k^{-\gamma} \}$:
$$S_k(A_k) = \frac{1}{4 g_k^2} \| F(A_k) \|_{L^2}^2 + \sum_{j} c_{j,k} \mathcal{O}_{j,\text{local}}(A_k) + R_k(A_k)$$
- **Running coupling recurrence:**
  $$\frac{1}{g_{k+1}^2} = \frac{1}{g_k^2} - 2 b_0 \ln L + r_k, \quad |r_k| \le C g_k^0$$
  with $b_0 = \frac{11 N}{48 \pi^2} > 0$.
- **Local counterterms:** $\mathcal{O}_{j,\text{local}}$ include quadratic mass/curvature counterterms required by lattice symmetry breaking (restoring continuous gauge covariance in the limit).
- **Remainder functional:** $R_k(A_k)$ is analytic, satisfying:
  $$\| R_k \|_{\kappa, \rho} \le C_R g_k^2 \cdot |\Lambda^{(k)}|$$

### Component 3: Large-Field Polymer Gas $\Xi_k(A_k)$
Controls regions where the small-field condition fails ($\|F_p\| > \epsilon_0 g_k^{-\gamma}$):
$$\Xi_k(A_k) = 1 + \sum_{m=1}^{\infty} \frac{1}{m!} \sum_{Y_1, \dots, Y_m \text{ disjoint}} \prod_{i=1}^m \zeta_k(Y_i, A_k)$$
- Each polymer $Y_i$ is a connected union of unit blocks on $\Lambda^{(k)}$.
- Polymer activity $\zeta_k(Y)$ satisfies the uniform exponential suppression bound:
  $$|\zeta_k(Y)| \le \exp\left( - \frac{\kappa_0}{g_k^2} |Y| \right)$$
  where $|Y|$ is the number of elementary blocks in $Y$, and $\kappa_0 > 0$ is a geometric constant independent of $k$ and $a_0$.

---

## 5. Summary Dependency Graph

```
[Scale 0: a_0, g_0] (Wilson Lattice Action)
         │
         ▼ (Q_0 integration: small/large field partition)
[Scale 1: a_1 = L a_0, g_1] (S_1 + Polymer Gas Xi_1)
         │
         ▼ (Q_1 integration)
[Scale 2: a_2 = L^2 a_0, g_2] (S_2 + Polymer Gas Xi_2)
         │
         ▼
        ...
         │
         ▼ (Q_{k-1} integration)
[Scale k: a_k = L^k a_0, g_k]  <-- STABLE while g_k <= g_* << 1
         │
         ▼
[Scale k_max: g_{k_max} >= g_*]   <-- METHOD BOUNDARY (Polymer cluster expansion loses contractivity)
```
