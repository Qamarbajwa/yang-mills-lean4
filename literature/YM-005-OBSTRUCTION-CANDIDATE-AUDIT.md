# YM-005 Obstruction Candidate Audit (IR Side)

## 1. Canonical Obstruction-ID Reconciliation

In strict adherence to repository invariants established in `YM-002F`, `YM-003`, and `YM-004-R1`, all obstruction analysis in Task `YM-005` maintains canonical definitions without semantic drift or local remapping:

| ID | Canonical Accepted Meaning | YM-005 Manifestation (IR / Lattice Side) | Consistent? | Authoritative Source |
|---|---|---|---|---|
| `OBS-CAND-001` | Non-Perturbative Intermediate Crossover Window ($g_k \sim 1$) / Infrared Running Breakdown / Continuum Thermodynamic Limit Failure | The unbridged intermediate-coupling transition $\beta \sim 1 - 2$ (or $g \sim 1$) separating the strong-coupling cluster expansion domain ($\beta < \beta_0$) from the weak-coupling asymptotic freedom domain ($\beta \gg 1$). | **YES** | `YM-002F`, `YM-003` (`BRIDGE_EDGE_REGISTER.md`) |
| `OBS-CAND-002` | Gauge-Fixing / Positivity Conflict (Gribov Copies & Reflection Positivity Breakdown under Gauge Fixing) | On the lattice, gauge fixing is unnecessary (compact Haar integration), preserving exact reflection positivity (OS3). However, attempting to gauge-fix to connect with continuum perturbative/RG flow introduces Gribov ambiguities or breaks manifest reflection positivity. | **YES** | `YM-002F` (`O8-OS`), `YM-003` (`E-SCHWINGER-OS3`) |
| `OBS-CAND-003` | Lattice Continuum Scaling / Diverging Cluster Expansion ($\beta \to \infty, a \to 0$) | Finite radius of convergence $\beta_0(d, G) \ll 1$ of the character cluster expansion; impossibility of directly extrapolating strong-coupling expansions to the continuum scaling limit $\beta \to \infty$. | **YES** | `YM-002F` (`O2-CONTINUUM`, `O4-CUTOFF`), `YM-003` (`E-LATTICE-CONT`) |

---

## 2. Granular Audit of `OBS-CAND-003` on the Infrared Lattice Boundary

### 2.1 The Nature of the Obstruction
`OBS-CAND-003` represents the foundational mathematical chokepoint of lattice gauge theory:
1. **Convergence on Discrete Lattice:**
   For $\beta < \beta_0(d, G)$, the polymer cluster expansion converges absolutely (Osterwalder–Seiler 1978, Gross 1979, Seiler 1982, Shen–Zhu–Zhu 2023). In this regime:
   - The infinite-volume Gibbs state $\mu_\infty$ exists and is unique.
   - The lattice Hamiltonian $H_{\text{lat}}$ has a strictly positive spectral gap $\Delta_{\text{lat}}(\beta, a) > 0$.
   - Wilson loops exhibit an area law $\langle W(C) \rangle \le C e^{-\sigma \cdot \text{Area}(C)}$.
2. **The Continuum Wall:**
   To take the continuum limit $a \to 0$, asymptotic freedom dictates that the bare coupling must scale according to the 1-loop/2-loop beta function:
   $$\beta(a) = \frac{2N}{g^2(a)} \approx \frac{2N b_0}{\ln(1 / (a \Lambda_{\text{QCD}}))} \xrightarrow{a \to 0} \infty$$
3. **The Divergence of the Expansion:**
   The character expansion parameter is $a_r(\beta) \sim \beta$. At $\beta \ge \beta_0$, the polymer activity bound:
   $$\sum_{Y \sim X} |\zeta(Y)| e^{\mu |Y|} < \mu |X|$$
   is violently violated. The expansion series for the free energy and correlation functions diverges.

### 2.2 Calibrated Epistemic Distinction
In compliance with **ROS v1.0 Law 2**:
- $\boxed{\textbf{Loss of Contractivity} \ne \textbf{Physical Phase Transition}}$
  In 4D pure $SU(N)$ lattice gauge theory, Monte Carlo evidence and asymptotic scaling analysis show that there is no thermodynamic singularity or phase transition separating the strong-coupling and weak-coupling regimes—it is a smooth crossover.
  The breakdown at $\beta_0$ is a **methodological stopping point** of the cluster expansion technique, not an intrinsic physical breakdown of the theory.

---

## 3. Contrast with `OBS-CAND-001` (The Non-Perturbative Crossover)

While `OBS-CAND-003` describes the breakdown of the strong-coupling series as $\beta$ increases toward unity, `OBS-CAND-001` describes the entire open gap between the two rigorous programs:
- **UV Side (YM-004):** Bałaban's multiscale RG controls $g_k \le g_* \ll 1$ (weak coupling, $\beta_k \gg 1$).
- **IR Side (YM-005):** Seiler / Shen–Zhu–Zhu controls $\beta \le \beta_0 \ll 1$ (strong coupling, $g \gg 1$).
- **The Gap (`OBS-CAND-001`):** The interval between $\beta_0$ and $\beta_{\text{UV}}^*$ constitutes the intermediate-coupling window where:
  - Perturbative asymptotic freedom and small-field Gaussian approximations fail ($g_k \sim 1$).
  - High-temperature character expansions fail ($\beta \ge \beta_0$).
  - Neither side's inductive contraction norms remain bounded.

---

## 4. Invariant Classification Under ROS v1.0 Law 7

$$\boxed{\textbf{No obstruction candidate is upgraded to a PROVED\_OBSTRUCTION\_THEOREM.}}$$

In accordance with ROS v1.0 Law 7:
1. `OBS-CAND-001`, `OBS-CAND-002`, and `OBS-CAND-003` remain strictly classified as `OBSTRUCTION_CANDIDATE`.
2. They document rigorous method boundaries of existing historical and modern techniques.
3. They do not assert mathematical impossibility of constructing the continuum theory via some genuinely novel non-perturbative framework.
