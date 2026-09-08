# YM-004 FINITE-VOLUME BOUNDARY TERM AUDIT

## Rigorous Audit of Finite-Volume Dependence in Constructive Renormalization Group Estimates

This document audits the exact mathematical role of the spatial volume $V = L_0^4$ and boundary conditions in Bałaban's ultraviolet stability proof for 4D Euclidean Yang–Mills theory.

---

## 1. Boundary Setup and Geometric Formulation

In Bałaban's primary papers (CMP 109, 116, 119), the spatial domain is formulated on a four-dimensional flat torus:
$$\mathbb{T}^4 = (\mathbb{R} / L_0 \mathbb{Z})^4$$
with periodic boundary conditions:
$$A_\mu(x + L_0 \hat{\nu}) = A_\mu(x)$$

### Torus Holonomy Zero Modes
Because the torus is topologically non-trivial ($\pi_1(\mathbb{T}^4) = \mathbb{Z}^4$), gauge connections admit global topological degrees of freedom that cannot be gauged away:
- **Polyakov loops:**
  $$P_\mu(x_\perp) = \mathcal{P} \exp\left( i \int_0^{L_0} A_\mu(x_\mu, x_\perp) \, dx_\mu \right) \in G$$
- **Flat connection moduli space:**
  $$\mathcal{M}_{\text{flat}}(\mathbb{T}^4) = \left( T \times T \times T \times T \right) / W$$
  where $T \subset G$ is the maximal torus (e.g. $U(1)^{N-1}$ for $SU(N)$) and $W$ is the Weyl group.
- **Laplacian spectrum on the torus:**
  $$\mathrm{Spec}(-\Delta_{\mathbb{T}^4}) = \left\{ \sum_{\mu=1}^4 \left( \frac{2\pi n_\mu}{L_0} \right)^2 : n_\mu \in \mathbb{Z} \right\}$$
  The lowest non-zero eigenvalue has a discrete infrared gap:
  $$\lambda_1(L_0) = \left( \frac{2\pi}{L_0} \right)^2 > 0$$
  which provides an automatic infrared regulator for all fluctuating modes orthogonal to the constant harmonic modes ($n = 0$).

---

## 2. Finite-Volume Boundary Term Audit Table

| Bound ID | Quantity / Functional | Published Estimate | Depends on $L_0$? | Uniform in $L_0$? | Reason & Mechanism | Primary Source | Potential Importance for $L_0 \to \infty$ |
|---|---|---|---|---|---|---|---|
| `BND-VOL-01` | Propagator decay constant $m_0$ | $\|\Delta_Q^{-1}(x,y)\| \le C a_k^{-2} e^{-m_0 |x-y|/a_k}$ | **NO** | **PROVED** | Local block operator with Dirichlet/axial block boundary conditions; decay rate depends only on block factor $L$, not total box $L_0$. | Bałaban CMP 95, p. 428 | Preserved in thermodynamic limit. |
| `BND-VOL-02` | Small-field curvature bound | $\sup_{p \subset \Delta} \|F_p\| \le \epsilon_0 g_k^{-\gamma}$ | **NO** | **PROVED** | Local criterion defined block-by-block. | Bałaban CMP 109, p. 256 | Local estimate; independent of volume. |
| `BND-VOL-03` | Remainder functional $R_k(A_k)$ | $\|R_k\|_{\kappa,\rho} \le C g_k^2 |\Lambda^{(k)}|$ | **YES** | **PROVED EXTENSIVE** | Extensive in volume ($|\Lambda^{(k)}| = L_0^4 / a_k^4$); remainder density $R_k / V$ is strictly uniform in $L_0$. | Bałaban CMP 114, p. 640 | Extensive density survives $L_0 \to \infty$. |
| `BND-VOL-04` | Polymer activity suppression | $|\zeta_k(Y)| \le e^{-\kappa_0 |Y| / g_k^2}$ | **NO** | **PROVED** | Decay factor depends on polymer volume $|Y|$, not total box size $L_0$. | Bałaban CMP 116, p. 12 | Uniform in $L_0$ for localized polymers. |
| `BND-VOL-05` | Polymer cluster expansion convergence | $\sum_{Y \ni x} |\zeta_k(Y)| e^{|Y|} < 1$ | **NO** | **PROVED** | Pinned sum at point $x$ bounded by translation invariance; independent of $L_0$. | Bałaban CMP 116, p. 15 | Local convergence holds for any volume. |
| `BND-VOL-06` | Torus-wrapping polymers | $|Y| \ge L_0 / a_k$ | **YES** | **PROVED** ($\to 0$) | Polymers wrapping around torus cycles are exponentially suppressed by $e^{-\kappa_0 L_0 / (a_k g_k^2)} \to 0$ as $L_0 \to \infty$. | Bałaban CMP 119, p. 250 | Non-local topological boundary terms vanish as $L_0 \to \infty$. |
| `BND-VOL-07` | Vacuum energy density $\mathcal{E}_k$ | $E_k(L_0) = \mathcal{E}_k L_0^4 + \mathcal{O}(L_0^3)$ | **YES** | **PROVED EXTENSIVE** | Thermodynamic limit of free energy density exists in small-field regime. | Bałaban CMP 119, p. 278 | Well-defined extensive limit. |
| `BND-VOL-08` | Torus zero-mode Haar integration | $\int_{\mathcal{M}_{\text{flat}}} d\mu_{\text{Haar}}(\theta) \, J(\theta)$ | **YES** | **NOT PROVED UNIFORM** | At terminal scale $a_k \sim L_0$, zero-mode measure integration cannot be factored into local cluster weights. | Bałaban CMP 119, p. 281 | Critical global obstacle at terminal scale. |
| `BND-VOL-09` | Infrared correlation decay / Mass gap | $\langle \mathcal{O}(x) \mathcal{O}(y) \rangle_{\text{conn}} \le C e^{-m |x-y|}$ | **YES** | **NOT PROVED** | No exponential decay proved in 4D continuum without an infrared cutoff; cluster bounds stop at $g_k \sim 1$. | **UNPROVED IN 4D** | **LOAD-BEARING OBSTACLE** to $L_0 \to \infty$. |

---

## 3. Which Exact Bound Fails or Prevents $L_0 \to \infty$?

### Synthesis of Findings

1. **Local Estimates are Uniform in $L_0$:**
   All local small-field estimates, Green's function decay rates, polymer activities, and cluster expansion convergence bounds (`BND-VOL-01` through `BND-VOL-05`) are **strictly uniform in the volume $L_0$**. The spatial volume enters strictly as an extensive counting factor ($V = L_0^4$).

2. **Topological Boundary Corrections Vanish:**
   Polymers that wrap around the non-trivial homology cycles of the torus (`BND-VOL-06`) carry action proportional to $L_0$ and therefore vanish exponentially as $L_0 \to \infty$. Boundary wrapping is **not** the obstacle to the thermodynamic limit.

3. **The True Obstacle is the Scale-Step Stopping Point:**
   The failure to establish the thermodynamic limit $L_0 \to \infty$ in the continuum is **not** caused by a breakdown of volume estimates at fixed scale $k$. Rather:
   $$\boxed{\text{To send } L_0 \to \infty \text{ at fixed physical scale, the number of RG steps } n = \frac{\ln(L_0 / a_0)}{\ln L} \text{ must grow arbitrarily large.}}$$
   Because the effective coupling runs according to asymptotic freedom:
   $$\frac{1}{g_k^2} = \frac{1}{g_0^2} - 2 b_0 k \ln L$$
   the coupling $g_k$ inevitably exceeds the polymer convergence radius $g_*$ after a finite number of steps $k_{\max} \approx \frac{1}{2 b_0 g_0^2 \ln L} \sim \frac{1}{\Lambda_{\text{QCD}}}$.

### Definite Conclusion
$$\boxed{\textbf{No single volume-dependent boundary term prevents } L_0 \to \infty.}$$
$$\boxed{\textbf{The thermodynamic limit is obstructed because the RG flow exits the weak-coupling regime } g_k < g_* \textbf{ before the infinite-volume limit can be taken.}}$$
In Bałaban's finite-volume theorem, $L_0$ is constrained so that $a_k$ reaches $L_0$ while $g_k$ is still small. If $L_0 \gg 1/\Lambda_{\text{QCD}}$, the flow hits $g_k \sim 1$ at an intermediate scale $a_k \ll L_0$, where the multiscale machinery halts.
