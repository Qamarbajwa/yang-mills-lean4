# YM-004 VISUAL INTUITION DATA

> [!WARNING]
> **STATUS: INTUITION ONLY — NOT MATHEMATICAL EVIDENCE**
>
> This document provides structured ASCII diagrams and visual schematics to aid human intuition. It does not constitute mathematical proof or evidence and carries no formal epistemic authority. The mathematical ledgers and source theorems remain the sole authoritative reference.

---

## 1. The Renormalization Group Scale Flow

```text
========================================================================================
             4D YANG-MILLS RENORMALIZATION GROUP SCALE PROGRESSION
========================================================================================

  ULTRAVIOLET (UV)                                                        INFRARED (IR)
  Lattice Cutoff a_0                                                      Confinement Scale
  Bare Coupling g_0 << 1                                                  g_k ~ 1

  Scale 0         Scale 1         Scale 2         Scale k_prov      Scale k_prov + 1
  a_0             a_1 = L*a_0     a_2 = L^2*a_0   a_k ~ c_*/Lambda  a > a_k
  g_0 << 1  ───>  g_1 > g_0 ───>  g_2 > g_1 ───>  g_* << 1    ───X  g > g_* (CONTRACTIVITY LOST)
  [   CONTROLLED BY BAŁABAN UV RG MACHINERY   ]   [LAST PROVED]     [UNBRIDGED CROSSOVER]
                                                  
  ─────────────────────────────────────────────   ───────────       ─────────────────────
  - Plaquette curvature ||F_p|| <= eps * g^-gamma  Boundary of       - Small-field fails
  - Quadratic Hessian strictly positive           Polymer Cluster   - Large fields unsuppressed
  - Large fields suppressed by exp(-c/g_k^2)      Contractivity     - Non-perturbative gap
  - Counterterms strictly local & bounded         (||zeta|| bound)  - Clay target open
========================================================================================
```

---

## 2. Scale-by-Scale Status Table (Intuition Format)

```text
+----------+--------------------+---------------------+-------------------------------+
| Scale k  | Lattice Spacing    | Effective Coupling  | Mathematical Status           |
+----------+--------------------+---------------------+-------------------------------+
| k = 0    | a_0                | g_0 << 1            | [PASS] Proved (Wilson lattice)|
| k = 1    | a_1 = L * a_0      | g_1 > g_0           | [PASS] Proved (Bałaban step)  |
| k = 2    | a_2 = L^2 * a_0    | g_2 > g_1           | [PASS] Proved (Bałaban step)  |
| ...      | ...                | ...                 | [PASS] Inductively stable     |
| k_prov   | a_* ~ c_*/Lambda   | g_* << 1 (symbolic) | [PASS] Last mathematically    |
|          |                    |                     |        proved scale (CMP 119) |
+----------+--------------------+---------------------+-------------------------------+
| k_prov+1 | a > a_*            | g > g_*             | [FAIL] Sufficient polymer     |
|          |                    |                     |        contractivity lost     |
| k_cross  | 1 / Lambda_QCD     | g ~ 1.0             | [OPEN] Intermediate crossover |
| k -> inf | L_0 -> infty       | g_eff(phys)         | [OPEN] Continuum Mass Gap     |
+----------+--------------------+---------------------+-------------------------------+
```

---

## 3. Finite-Volume vs Thermodynamic Limit Intuition

```text
+---------------------------------------------------------------------------------------+
| SCENARIO A: FINITE VOLUME (L_0 < infty) -- RIGOROUSLY SOLVED BY BAŁABAN               |
|                                                                                       |
|   +---------------------------------------+                                           |
|   | Torus T^4 = (R / L_0 Z)^4             |  - Box size L_0 is fixed.                 |
|   |                                       |  - UV cutoff a_0 -> 0 is removed cleanly. |
|   |        [ a_0 -> 0 ]                   |  - Effective coupling at scale L_0 is     |
|   |                                       |    kept small: g(L_0) <= g_*.             |
|   |   Partition function Z is uniformly   |  - Result: 4D UV Stability in finite      |
|   |   bounded from above and below!       |    volume is a PROVED THEOREM!            |
|   +---------------------------------------+                                           |
+---------------------------------------------------------------------------------------+
                                           │
                                           ▼ (Take L_0 -> infinity?)
+---------------------------------------------------------------------------------------+
| SCENARIO B: THERMODYNAMIC LIMIT (L_0 -> infty) -- THE UNBRIDGED CHOKEPOINT            |
|                                                                                       |
|   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+   |
|   :  Infinite Spacetime R^4                                                       :   |
|   :                                                                               :   |
|   :    To make L_0 -> infty at fixed physical scale:                             :   |
|   :    The number of RG scale steps n = ln(L_0 / a_0) must grow to infinity!      :   |
|   :                                                                               :   |
|   :    Because beta_0 > 0, the coupling MUST grow:                                :   |
|   :    g_k^2 ~ 1 / (2 b_0 ln(1 / a_k Lambda))                                     :   |
|   :                                                                               :   |
|   :    At scale a_k ~ 1/Lambda_QCD, the coupling hits g_k ~ 1 BEFORE reaching     :   |
|   :    the outer volume boundary L_0!                                             :   |
|   :                                                                               :   |
|   :    [ MISSING ESTIMATE: Non-perturbative cluster bound across g_k ~ 1 ]        :   |
|   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+   |
+---------------------------------------------------------------------------------------+
```

---

## 4. Small-Field vs Large-Field Phase Plane

```text
Field Strength ||F_p||
   ▲
   │
   │  LARGE-FIELD REGION (Polymer Gas Xi_k)
   │  - Non-Gaussian, non-perturbative link fluctuations
   │  - Suppressed by Wilson action: exp(-c * ||F_p||^2 / g_k^2)
   │  - Combinatorial entropy: (C_4)^|Y|
   │  - When g_k << 1: Suppression DOMINATES entropy (convergent)
   │  - When g_k ~ 1:  Entropy DEFEATS suppression (DIVERGENT!)
   │
───┼───────────────────────────────────────────────────────────── Threshold: eps * g_k^-gamma
   │
   │  SMALL-FIELD REGION (Effective Action S_k)
   │  - Plaquettes close to identity: U(p) ~ exp(i a^2 F_p)
   │  - Strict quadratic convexity: Spec(Hessian) >= c_0 / a^2
   │  - Gaussian integration + BPHZ perturbative counterterms
   │  - Asymptotic freedom flow: 1/g_{k+1}^2 = 1/g_k^2 - 2 b_0 ln L
   │  - Stable for all g_k <= g_*
   │
   └─────────────────────────────────────────────────────────────► Coupling g_k
                          g = 0               g = g_*         g ~ 1
```

> [!NOTE]
> **End of Visual Intuition Artifact.** Consult `literature/YM-004-STOPPING-POINT-ANALYSIS.md` for formal mathematical formulations and theorem locators.
