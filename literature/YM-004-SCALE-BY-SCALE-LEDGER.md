# YM-004 SCALE-BY-SCALE LEDGER

## Granular Multiscale Evolution and Parameter Tracking

This ledger provides a step-by-step mathematical inspection of the Bałaban renormalization group progression from the bare ultraviolet cutoff scale $k=0$ down to the infrared stopping scale $k_{\max}$.

---

## 1. Multiscale Step Ledger

| Scale $k$ | Lattice Spacing $a_k$ | Effective Coupling $g_k^2$ | Small-Field Domain $\mathcal{D}_{\text{small}}(k)$ | Large-Field Suppression $e^{-S_{\text{large}}}$ | Remainder Bound $\|R_k\|$ | Volume Dependence | Status & Source |
|---|---|---|---|---|---|---|---|
| **$k = 0$** | $a_0$ (bare UV cutoff) | $g_0^2 \ll 1$ | $\|F_p\| \le \epsilon_0 g_0^{-\gamma}$ | $\le e^{-c / g_0^2}$ | $0$ (exact Wilson action) | $\mathrm{Vol} = L_0^4 = N_0 a_0^4$ | `PROVED` (Wilson 1974) |
| **$k = 1$** | $a_1 = L a_0$ | $g_1^2 = \frac{g_0^2}{1 - 2b_0 g_0^2 \ln L}$ | $\|F_p\| \le \epsilon_0 g_1^{-\gamma}$ | $\le e^{-c / g_1^2}$ | $\le C g_1^2 \cdot |\Lambda^{(1)}|$ | $N_1 = L^{-4} N_0$ cells | `PROVED` (Bałaban CMP 95/109) |
| **$k = 2$** | $a_2 = L^2 a_0$ | $g_2^2 = \frac{g_0^2}{1 - 4b_0 g_0^2 \ln L}$ | $\|F_p\| \le \epsilon_0 g_2^{-\gamma}$ | $\le e^{-c / g_2^2}$ | $\le C g_2^2 \cdot |\Lambda^{(2)}|$ | $N_2 = L^{-8} N_0$ cells | `PROVED` (Bałaban CMP 109/114) |
| **$k$** | $a_k = L^k a_0$ | $g_k^2 \approx \frac{g_0^2}{1 - 2b_0 k g_0^2 \ln L}$ | $\|F_p\| \le \epsilon_0 g_k^{-\gamma}$ | $\le \exp\left(-\frac{\kappa_0}{g_k^2} \|Y\|\right)$ | $\le C g_k^2 \cdot L^{-4k} N_0$ | $N_k = L^{-4k} N_0$ cells | `PROVED` (Bałaban CMP 116/119) |
| **$k_{\text{prov}}$** | $a_{k_{\text{prov}}} \approx \frac{1}{\Lambda_{\text{prov}}}$ | $g_{k_{\text{prov}}}^2 = g_*^2 \ll 1$ | Upper limit of small-field perturbation theory | Threshold of polymer convergence | $\le C g_*^2 \cdot |\Lambda^{(k_{\text{prov}})}|$ | Extensively bounded | `LAST_PROVED_SCALE` (CMP 119) |
| **$k_{\text{prov}} + 1$** | $a_{k_{\text{prov}}+1} > a_{k_{\text{prov}}}$ | $g_{k_{\text{prov}}+1}^2 > g_*^2$ | Small-field expansion radius exceeded | $\sum_{Y} e^{-\kappa_0 |Y| / g^2}$ ceases to converge | Uncontrolled | Uncontrolled | `FIRST_UNPROVED_SCALE` |
| **$k_{\text{crossover}}$** | $a_{\text{cross}} \sim \frac{1}{\Lambda_{\text{QCD}}}$ | $g_k^2 \sim 1$ | Small-field concept invalid ($\|F_p\| \sim 1$) | No exponential suppression ($e^{-c/1} \sim \mathcal{O}(1)$) | Order unity fluctuations | Global volume accumulation | `UNCONTROLLED_REGIME` |
| **$k \to \infty$** | $a_k \to \infty$ ($L_0 \to \infty$) | Perturbative $g_k^2 \to \infty$ (Landau pole) | Completely outside Gaussian domain | Non-perturbative confinement regime | Unbounded | Infinite volume limit | `OPEN` (Clay Problem) |

---

## 2. Functional Norm Specifications

At each scale $k$, the mathematical stability is audited under three distinct functional norms:

### 1. Gauge Connection Sobolev Norm
$$\| A_k \|_{\mathcal{H}_k^1}^2 = a_k^4 \sum_{x \in \Lambda^{(k)}} \left( |A_k(x)|^2 + \sum_{\mu} |\nabla_\mu A_k(x)|^2 \right)$$
- Measures the kinetic regularity of the gauge connection.
- Uniformly bounded under the block averaging operator: $\| Q(A_k) \|_{\mathcal{H}_{k+1}^1} \le C_Q \| A_k \|_{\mathcal{H}_k^1}$.

### 2. Curvature Sup-Norm (Small-Field Criterion)
$$\| F(A_k) \|_{\infty} = \sup_{p \in \mathcal{P}(\Lambda^{(k)})} a_k^{-2} \| I - U_k(\partial p) \|$$
- Governs the small-field vs large-field partition:
  $$\mathcal{D}_{\text{small}}(k) = \left\{ A_k : \| F(A_k) \|_{\infty} \le \epsilon_0 g_k^{-\gamma} \right\}, \quad 0 < \gamma < 1$$
- Within $\mathcal{D}_{\text{small}}$, the Yang–Mills action is strictly convex around the classical minimizer.

### 3. Polymer Activity Norm (Cluster Expansion Convergence)
$$\| \zeta_k \|_{\kappa, \rho} = \sup_{x \in \Lambda^{(k)}} \sum_{Y \subset \Lambda^{(k)}, Y \ni x} |\zeta_k(Y)| \cdot \exp\left( \frac{\kappa}{g_k^2} |Y| \right) \cdot \rho^{|Y|}$$
- Controls the convergence of the Kirkwood–Salsburg / Mayer equations for the polymer gas $\Xi_k$.
- **Convergence Theorem (Bałaban CMP 116):** For $g_k \le g_*$ sufficiently small and $\rho > 1$:
  $$\| \zeta_k \|_{\kappa, \rho} \le C_0 g_k^2$$
  guaranteeing that $\ln \Xi_k$ is an absolutely convergent, contractive cluster expansion. For $g_k \ge g_*$, contractivity is no longer established.

---

## 3. Step-by-Step Inductive Transition Hypotheses

For the induction $k \implies k+1$ to succeed, Bałaban requires four simultaneous mathematical conditions:

1. **Coupling Smallness:** $g_k < g_*$, ensuring that asymptotic freedom continues to provide an effective expansion parameter.
2. **Spectral Gap of Block Hessian:** The second-variation operator $D_{A_{\min}}^* D_{A_{\min}} + \alpha^{-1} Q^* Q$ on the block must satisfy a strictly positive lower bound independent of the volume $V$:
   $$\lambda_{\min} \ge c_0 a_k^{-2} > 0$$
3. **Gauge Invariance of Counterterms:** The local counterterms generated at step $k$ must belong to the finite-dimensional space of gauge-invariant polynomials of degree $\le 4$.
4. **Polymer Localization:** The activity $\zeta_k(Y)$ must be exponentially localized in the polymer support $Y$:
   $$\mathrm{dist}(Y_1, Y_2) \ge 1 \implies \zeta_k(Y_1 \cup Y_2) = \zeta_k(Y_1) \zeta_k(Y_2)$$
