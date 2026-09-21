# Task YM-008: Scale-Interface Mathematical Matching Analysis

- **TASK_ID:** `YM-008`
- **GOVERNANCE_TIER:** `R2`
- **DATE:** 2026-09-22

---

## 1. Purpose and Interface Structure

In any multi-scale hybrid architecture, the primary mathematical danger is the **gluing error**—the breakdown of conservation laws, gauge invariance, or reflection positivity at the boundary separating different regimes.

Task **YM-008** defines explicit mathematical matching conditions across the two critical interfaces:
1. **Interface 1 ($\mathcal{I}_{\text{UV}\to\text{mid}}$):** Ultraviolet Bałaban/Flow $\longleftrightarrow$ Intermediate Loop Bootstrap ($x \approx x_{\text{UV}}^* \approx 0.15\text{ fm}$),
2. **Interface 2 ($\mathcal{I}_{\text{mid}\to\text{IR}}$):** Intermediate Loop Bootstrap $\longleftrightarrow$ Infrared Center-Vortex Cluster Expansion ($x \approx a_{\text{strong}}^* \approx 0.50\text{ fm}$).

---

## 2. Interface 1: Ultraviolet $\longleftrightarrow$ Intermediate Crossover Matching

### 2.1. Mathematical Formulation
At the ultraviolet boundary $x \approx x_{\text{UV}}^*$, the high-frequency fluctuations ($p > 1/x_{\text{UV}}^*$) have been integrated out by Bałaban's multiscale RG transformations. To interface these fields with the loop bootstrap, we define the **Flow-Regularized Wilson Loop**:

$$W_t(C) = \frac{1}{N} \text{Tr} \, \mathcal{P} \exp \left( i \oint_C B_\mu(t, x) \, dx^\mu \right)$$

where $B_\mu(t, x)$ is the solution of Lüscher's gradient flow equation at flow time $t$.

### 2.2. The Joint Scaling Theorem
To ensure that the continuum limit $a \to 0$ does not introduce unphysical smearing at the crossover scale, the flow time $t$ must scale quadratically with the lattice cutoff $a$:

$$\boxed{t(a) = c_0 \, a^2 \qquad (c_0 = \text{const} > 0)}$$

Under this joint scaling:
1. **UV Finiteness:** The root-mean-square smearing radius is $r_{\text{smooth}} = \sqrt{8t} = \sqrt{8c_0} \, a \to 0$ as $a \to 0$, ensuring that physical crossover correlations at distances $x \ge x_{\text{UV}}^* \gg a$ remain undistorted.
2. **Contact Singularity Elimination:** In the Makeenko–Migdal loop equation, the delta-function singularity $\delta^{(4)}(x - y)$ is smeared by the heat kernel:
   $$\delta^{(4)}(x - y) \mapsto K_t(x - y) = \frac{e^{-|x-y|^2 / 4t}}{(4\pi t)^2}$$
   This renders the continuum loop Laplacian $\Delta_{\text{loop}} W_t(C)$ strictly finite and well-defined for all $t > 0$, removing the contact-term divergence identified in `YM-007-LOOP-EQUATIONS-EVALUATION.md`.

### 2.3. Interface 1 Matching Condition
The moment matrix of the loop bootstrap $\mathcal{M}$ is constructed from flow-regularized loops:

$$\boxed{\mathcal{M}_{ij}(t) = \langle W_t(C_i)^\dagger \, W_t(C_j) \rangle \succeq 0}$$

Matching requires that as $t \to 0$ outside the flow boundary ($|x_i - x_j| \ge x_{\text{UV}}^*$), $\mathcal{M}_{ij}(t)$ converges uniformly to the gauge-invariant correlation matrix:
$$\lim_{t \to 0} \mathcal{M}_{ij}(t) = \mathcal{M}_{ij}^{\text{physical}} \qquad (\forall C_i, C_j \text{ with separation } \ge x_{\text{UV}}^*)$$

---

## 3. Interface 2: Intermediate Crossover $\longleftrightarrow$ Infrared Confinement Matching

### 3.1. Mathematical Formulation
At the infrared boundary $x \approx a_{\text{strong}}^* \approx 0.50\text{ fm}$, the non-perturbative SDP bootstrap bounds must transition into the convergent cluster expansion of the center-vortex ensemble.

For any closed rectangular loop $C = R \times T$ with $R, T \ge a_{\text{strong}}^*$, the SDP bootstrap provides rigorous non-perturbative upper and lower bounds:

$$\mathcal{B}_{\text{lower}}(R, T) \le \langle W(R \times T) \rangle \le \mathcal{B}_{\text{upper}}(R, T)$$

Simultaneously, the center-vortex polymer cluster expansion represents the Wilson loop as:

$$\langle W(R \times T) \rangle = e^{-\sigma_{\text{vortex}} R T - 2\mu (R + T)} \left( 1 + \sum_{P \text{ linked}} \zeta(P) \right)$$

where $\zeta(P)$ is the polymer activity bounded by $\| \zeta \| \le e^{-c / g^2} \le e^{-c \beta_0}$.

### 3.2. Interface 2 Matching Equation
The string tension $\sigma_{\text{bootstrap}}$ extracted from the asymptotic ratio of SDP bounds:
$$\sigma_{\text{bootstrap}} = -\lim_{R, T \to \infty} \frac{1}{R T} \ln \mathcal{B}_{\text{upper}}(R, T)$$
must match the topological vortex tension $\sigma_{\text{vortex}}$ derived from the Mack–Petkova free energy of vortex insertion:

$$\boxed{\left| \sigma_{\text{bootstrap}} - \sigma_{\text{vortex}} \right| \le \epsilon_{\text{matching}}(a_{\text{strong}}^*)}$$

where $\epsilon_{\text{matching}} \to 0$ exponentially as the cluster expansion order increases.

---

## 4. Preservation of Invariants Across Interfaces

1. **Gauge Invariance:**
   Both $W_t(C)$ (Interface 1) and center-vortex linking numbers $\text{Link}(C, \Sigma)$ (Interface 2) are **manifestly gauge-invariant**. No gauge fixing or Faddeev–Popov ghost determinant is required across either interface.
2. **Reflection Positivity (OS3):**
   - At Interface 1: Smearing is confined to $t \sim a^2$. In the continuum limit $a \to 0$, the smearing radius vanishes, restoring exact Osterwalder–Schrader reflection positivity for macroscopic observables.
   - At Interface 2: The transfer matrix $T$ on the lattice satisfies $T = T^\dagger \ge 0$ by the Osterwalder–Seiler construction, ensuring positive-definite physical Hilbert space $\mathcal{H}$.
