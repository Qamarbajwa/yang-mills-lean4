# YM-004 STOPPING-POINT ANALYSIS

## Exact Mathematical Demarcation of the Ultraviolet Renormalization Group Boundary

This document identifies with mathematical precision where the rigorous 4D constructive RG machinery of Bałaban, Federbush, and Magnen–Rivasseau–Sénéor terminates, distinguishing proved failure modes from the absence of theorems.

---

## 1. Tripartite Regime Demarcation

### A. Last Proved Regime (`LAST_PROVED_REGIME`)
- **Mathematical Specification:**
  $$g_k^2 \le g_*^2 \ll 1, \quad a_k \le L_0, \quad V = L_0^4 < \infty$$
  where $g_* > 0$ is an explicit, computable numerical constant satisfying the polymer convergence condition:
  $$\sum_{m=1}^\infty (C_4 C_{\text{int}} e)^m \exp\left( - \frac{\kappa_1}{g_*^2} m \right) < \frac{1}{2}$$
- **Controlled Quantities:**
  1. Effective action $S_k(A_k)$ is strictly analytic in $\mathcal{D}_{\text{small}}(k)$.
  2. Running coupling obeys 1-loop Callan–Symanzik asymptotic freedom with bounded counterterm flow.
  3. Partition function $Z(\mathbb{T}^4, a_0, g_0)$ is uniformly bounded from above and below as $a_0 \to 0$.
  4. Local gauge invariance is preserved at every step.
- **Primary Citation:** Bałaban, *Commun. Math. Phys.* 116 (1988) 1–22; 119 (1988) 243–285 (`THM-YM-0018`).

---

### B. First Unproved Extension (`FIRST_UNPROVED_EXTENSION`)
- **Mathematical Specification:**
  $$g_k^2 > g_*^2, \quad \text{specifically the scale step } k = k_{\text{prov}} + 1 \text{ where } g_{k+1}^2 \approx g_*^2 + 2 b_0 g_*^4 \ln L$$
- **Uncontrolled Quantities:**
  1. Absolute convergence of the polymer activity sum $\sum_Y |\zeta_{k+1}(Y)| e^{|Y|}$ is lost.
  2. Remainder norm $\| R_{k+1} \|_{\kappa, \rho}$ is not established.
  3. Saddle-point expansion around $A_{\min}(B)$ is not provably dominated by the quadratic Hessian.
  4. Uniqueness of the background field minimizer $A_{\min}(B)$ is no longer guaranteed (potential Gribov ambiguities).

---

### C. Mathematical Cause of Machinery Termination

| Candidate Mechanism | Audited Status | Exact Mathematical Role | Supported by Source? |
|---|---|---|---|
| **Effective Coupling Growth** | **PRIMARY CAUSE** | Because $\beta_0 > 0$ (asymptotic freedom), $g_k$ increases monotonically under coarsening. The entire construction is perturbative in $g_k$; when $g_k > g_*$, the small parameter vanishes. | **YES** (CMP 116, p. 18; CMP 109, p. 251) |
| **Polymer Expansion Breakdown** | **CONSEQUENCE** | Polymer weights $e^{-\kappa_1 |Y| / g_k^2}$ lose exponential suppression when $g_k \sim 1$. The sum over polymer geometries diverges combinatorially. | **YES** (CMP 116, Lemma 3.2) |
| **Large-Field Proliferation** | **CONSEQUENCE** | Volume fraction occupied by large-field blocks $\chi_{\text{large}}(\Delta) = 1$ is no longer exponentially small. | **YES** (CMP 119, p. 260) |
| **Loss of Quadratic Dominance** | **CONSEQUENCE** | $g_k V_3(q) + g_k^2 V_4(q)$ becomes of the same order as $\langle q, \mathcal{H} q \rangle$, invalidating Gaussian saddle-point integration. | **YES** (CMP 109, p. 280) |
| **Finite-Volume Dependence ($L_0 < \infty$)** | **NOT THE CAUSE** | Volume estimates are extensive; boundary wrapping polymers vanish exponentially as $L_0 \to \infty$. Finite volume is an external constraint to keep $a_k \le L_0$ while $g_k \le g_*$. | **YES** (CMP 119, Section 4) |
| **Loss of Reflection Positivity** | **NOT THE CAUSE** | Wilson lattice action is reflection-positive on the lattice (`THM-YM-0009`). Bałaban's RG integration preserves reflection positivity for physical observables. | **NO** (reflection positivity intact) |
| **Infrared Renormalons** | **DISTINCT MECHANISM** | Perturbative factorial divergence in Borel plane ($\sim n!$). Bałaban's polymer divergence is spatial/combinatorial, not identified as a Borel-plane singularity. | **NOT IDENTIFIED IN BALABAN** (identified in MRS 1993) |

---

## 2. Answers to Canonical Questions Q6–Q10

### Q6: At what precise step does the published proof stop?
The published proof stops at step $k_{\text{prov}}(g_0)$, defined by:
$$k_{\text{prov}}(g_0) = \max \left\{ k \in \mathbb{N} : g_k^2(g_0) \le g_*^2 \right\} \approx \frac{1}{2 b_0 \ln L} \left( \frac{1}{g_0^2} - \frac{1}{g_*^2} \right)$$
In physical distance units, this corresponds to:
$$a_{k_{\text{prov}}} \approx a_0 \exp\left( \frac{1}{2 b_0 g_0^2} \right) \cdot \exp\left( - \frac{1}{2 b_0 g_*^2} \right) \sim \frac{c_*}{\Lambda_{\text{QCD}}}$$
The proof stops at a fixed fraction of the confinement scale $\Lambda_{\text{QCD}}^{-1}$.

### Q7: Why does it stop?
It stops because every estimate in the induction (saddle-point Gaussian approximation, BPHZ counterterm bounds, polymer activity suppression) depends on negative powers of $g_k$ in the exponent and positive powers of $g_k$ in the remainder:
$$\| R_k \| \le C g_k^2, \quad |\zeta_k(Y)| \le e^{-\kappa_0 |Y| / g_k^2}$$
When $g_k$ exceeds $g_*$, these bounds cease to be contractive.

### Q8: What mechanism causes the stopping point?
$$\boxed{\textbf{Direct mechanism: Polymer/cluster expansion breakdown triggered by effective coupling growth } g_k \to g_*.}$$
It is **not** caused by boundary terms, nor by loss of reflection positivity, nor by finite-volume accumulation.

### Q9: Proved barrier vs limit of method?
- **PROVED:** Bałaban's specific functional norms ($\| \cdot \|_{\kappa, \rho}$) diverge for $g_k > g_*$. The small-field polymer expansion as formulated cannot be iterated further.
- **NOT PROVED:** There is **no theorem** proving that 4D Yang–Mills cannot be controlled at $g_k \sim 1$. The stopping point is an epistemic boundary of the weak-coupling constructive expansion, not a proved physical singularity of the theory.
- **Classification:**
  $$\boxed{\textbf{PROOF\_TERMINATES\_HERE / METHOD\_LIMITATION}}$$

### Q10: What would mathematically be required to extend control one scale further?
To advance from $k_{\text{prov}}$ to $k_{\text{prov}} + 1$ requires:
1. **Non-Gaussian Measure Parameterization:** Replacing the Gaussian saddle-point measure $d\mu_{A_{\min}}(q)$ with a non-perturbative measure capable of integrating fluctuations of order $g_k \sim 1$.
2. **Resummed Polymer Activities:** Reorganizing the polymer expansion so that large-field configurations are controlled by global topological or non-Abelian geometric properties (e.g. area-law suppression, vortex condensation, or center-symmetry domain walls) rather than local energy bounds $\propto 1/g_k^2$.
3. **Non-Perturbative Gauge-Fixing:** Controlling Gribov copies in the block averaging operator $Q$ when fluctuations are large.
