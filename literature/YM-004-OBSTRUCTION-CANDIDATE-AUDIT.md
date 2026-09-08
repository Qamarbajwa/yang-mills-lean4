# YM-004 OBSTRUCTION-CANDIDATE AUDIT

## Alignment of Constructive UV Renormalization Group Literature with Repository Obstruction Candidates

This document audits the relationship between the 4D ultraviolet constructive renormalization group machinery (Bałaban, Federbush, Magnen–Rivasseau–Sénéor) and the three canonical common obstruction candidates established in `YM-002F` and `YM-003`.

---

## 1. Candidate Alignment Matrix

| Candidate ID | Candidate Obstruction Name | UV Literature Alignment Status | Specific Evidence in Reconstructed Literature | Mathematical Verdict |
|---|---|---|---|---|
| **`OBS-CAND-001`** | **Non-Perturbative Intermediate Crossover Window ($g_k \sim 1$)** | **DIRECTLY SUPPORTS** | Bałaban's polymer cluster expansion norm $\| \zeta_k \|_{\kappa, \rho} \le C g_k^2$ strictly diverges as $g_k \to g_*$. The proof explicitly terminates at the boundary of weak-coupling perturbation theory ($g_k \le g_* \ll 1$). Magnen–Rivasseau–Sénéor explicitly require an artificial IR cutoff $\Lambda_{\text{IR}} > 0$ because crossover control is absent. | **CONFIRMED CANDIDATE** (remains `METHOD_LIMITATION`, not proved impossible) |
| **`OBS-CAND-002`** | **Gauge-Fixing / Positivity Conflict (Gribov Copies)** | **PARTIALLY SUPPORTS** | Bałaban circumvents global Gribov copies by using local block-gauge fixing at each scale step with Dirichlet-type boundary conditions, ensuring local invertibility of the block Faddeev–Popov operator. However, this local gauge fixing generates boundary counterterms and cannot be extended globally when fluctuations grow of order unity. | **CONFIRMED CANDIDATE** (local circumvention proved; global obstruction survives in IR) |
| **`OBS-CAND-003`** | **Lattice Continuum Scaling / Diverging Cluster Expansion** | **DOES NOT ADDRESS (UV SIDE)** | `OBS-CAND-003` describes the strong-coupling lattice perspective ($\beta \to \infty$, $a \to 0$), where the high-temperature cluster expansion radius is exceeded. Bałaban starts directly from the weak-coupling continuum end ($a \to 0$, $g_0 \to 0$); hence Bałaban's theorems neither support nor contradict lattice strong-coupling cluster behavior, but rather confirm that the weak-coupling side cannot reach the strong-coupling domain. | **INDEPENDENT COMPLEMENT** (serves as the opposite side of the bridge) |

---

## 2. Granular Analysis per Candidate

### OBS-CAND-001: The Intermediate Crossover Window
- **Candidate Hypothesis:** The failure of both weak-coupling UV expansions and strong-coupling IR expansions to overlap in 4D continuum spacetime represents a fundamental structural chokepoint ($g_k \sim 1$).
- **Reconstruction Findings:**
  - Bałaban's proof proves that the small-field effective action is stable for all $k$ such that $g_k \le g_*$.
  - It demonstrates that large-field configurations are controlled by Boltzmann suppression $e^{-\kappa / g_k^2}$.
  - When $g_k \sim 1$, both small-field Gaussian dominance and large-field exponential suppression fail simultaneously.
  - MRS 1993 confirms that even with Borel summability, the infrared renormalon singularity obstructs the removal of the IR cutoff at the crossover scale.
- **Epistemic Invariant Preserved:** `OBS-CAND-001` remains an unproved candidate obstruction. The literature establishes that *known constructive RG methods stop at $g_k \sim 1$*, not that the Yang–Mills continuum measure cannot exist across the transition.

### OBS-CAND-002: Gribov Copies and Local Block Gauge Fixing
- **Candidate Hypothesis:** Non-perturbative gauge fixing on compact manifolds develops Gribov copies, introducing sign changes into the Faddeev–Popov determinant that conflict with reflection positivity.
- **Reconstruction Findings:**
  - Bałaban solves the gauge-fixing problem locally: by restricting the integration at each step to fluctuations inside blocks of size $L$, and fixing gauge only relative to the coarse background field $Q(A) = B$, the Faddeev–Popov operator is strictly positive-definite on the small-field domain.
  - Global gauge fixing is never performed; gauge invariance is maintained at the level of the block effective actions.
  - Therefore, Gribov copies do **not** obstruct the UV flow in the small-field regime.
  - However, when fluctuations reach $g_k \sim 1$, the background field equation $D_A^* F(A) + \alpha^{-1} Q^* (Q(A) - B) = 0$ admits multiple non-unique solutions, re-introducing Gribov ambiguities.

### OBS-CAND-003: Lattice Strong-Coupling vs Continuum Scaling
- **Candidate Hypothesis:** The strong-coupling mass gap established by Wilson and Shen–Zhu–Zhu cannot be scaled to $a \to 0$ because the cluster expansion radius $\beta_0$ is finite.
- **Reconstruction Findings:**
  - Bałaban's results provide the exact dual perspective: starting at $a_0 \to 0$ with $\beta_0 = 2N/g_0^2 \to \infty$, the theory is controlled downwards toward the infrared until $g_k$ grows.
  - This confirms that the two programs are working from opposite sides of the coupling axis without overlap:
    $$\underbrace{[0, g_*]}_{\text{Bałaban UV Proved}} \quad \ll \quad \underbrace{[g_*, g_{\text{lattice}}]}_{\text{Unbridged Gap}} \quad \ll \quad \underbrace{[g_{\text{lattice}}, \infty)}_{\text{Lattice Strong-Coupling Proved}}$$
  - The audit confirms that YM-004 provides the exact left boundary ($g_*$) of the unbridged gap.

---

## 3. Governance Status Invariant

Under ROS v1.0 Law 7 (Obstruction State Machine):
$$\boxed{\textbf{No obstruction candidate is upgraded to a PROVED\_OBSTRUCTION\_THEOREM.}}$$
All three entries remain strictly classified as `OBSTRUCTION_CANDIDATE`.
