# YM-005 Visual Intuition Data: Dual-Boundary Structure

> **DISCLAIMER:** This artifact is non-authoritative and intended solely for intuitive visualization in external chat interfaces (e.g., ChatGPT / Claude / Antigravity). It synthesizes the rigorous mathematical results of `YM-004` (UV side) and `YM-005` (IR side). It does not replace or supersede canonical theorem statements in `THEOREM_LEDGER.md` or boundary records.

---

## 1. Dual-Boundary Structural Map

```text
====================================================================================================
               RIGOROUS BOUNDARY STRUCTURE OF 4D YANG–MILLS (UV vs. IR)
====================================================================================================

      ULTRAVIOLET REGIME (YM-004)                   INFRARED REGIME (YM-005)
      Weak Coupling: g_k <= g_* << 1               Strong Coupling: beta <= beta_0 << 1
      Small Distance: x -> 0 (Continuum)            Coarse Lattice: a >= a_strong (Discrete)
      
+---------------------------------------+     +---------------------------------------+
|  BAŁABAN MULTISCALE RG (1984–1989)    |     |  OSTERWALDER–SEILER / GROSS (1978–82) |
|  - Asymptotic freedom inductive flow  |     |  - High-temp character cluster exp.   |
|  - Small-field effective actions      |     |  - Transfer matrix T = e^{-a H} > 0   |
|  - Large-field polymer suppression    |     |  - Exponential clustering m_lat > 0   |
|  - Finite-volume UV stability a -> 0  |     |  - Thermodynamic limit on Z^4         |
+---------------------------------------+     +---------------------------------------+
|  MAGNEN–RIVASSEAU–SÉNÉOR (1993)       |     |  SHEN–ZHU–ZHU (2023)                  |
|  - R^4 infinite volume with IR cutoff |     |  - Uniform Poincaré inequality        |
|  - Renormalon / BPHZ control          |     |  - Strictly positive gap Delta_lat > 0|
+---------------------------------------+     +---------------------------------------+
                    │                                             ▲
                    ▼                                             │
      [Contractivity Lost at g_*]                   [Contractivity Lost at beta_0]
                    │                                             │
                    └─────────────────────┬───────────────────────┘
                                          │
                                          ▼
                =====================================================
                      UNBRIDGED NON-PERTURBATIVE CROSSOVER WINDOW
                                 (E-CROSSOVER / OBS-CAND-001)
                                      g_k ~ 1, beta ~ 1 - 2
                               x ~ 0.2 - 1.0 fm (phenomenological)
                =====================================================
                - Asymptotic freedom ceases; g_k grows beyond contractivity
                - Polymer cluster expansion activity sum diverges
                - Bakry–Émery Ricci curvature collapses to negative
                - Neither UV small-field nor IR character methods apply
                - Thermodynamic infinite-volume removal unestablished
                =====================================================
```

---

## 2. Scale-by-Scale Mathematical Control Ledger

| Physical Scale / Regime | Coupling Representation | Rigorous Status | Governing Program | Mathematical Mechanism | Status of Mass Gap |
|---|---|---|---|---|---|
| **Deep UV** ($x \to 0, a \to 0$) | $g_k \to 0, \beta \to \infty$ | `RIGOROUS_PROVED` (Finite Volume) | Bałaban (1984–1989) | Asymptotic freedom, saddle-point small-field flow | Unproved ($\Delta$ requires IR) |
| **Perturbative UV** ($x \le x_{\text{UV}}^*$) | $g_k \le g_* \ll 1$ | `RIGOROUS_PROVED` (Finite Volume) | Bałaban / MRS (1993) | Inductive multiscale small/large field partition | Unproved (UV stability only) |
| **UV Stopping Point** | $g_k \to g_* \ll 1$ | `METHOD_BOUNDARY` | YM-004 Boundary Record | Polymer tree contraction bound $\sum |\zeta| e^{|Y|} < 1/2$ fails | Boundary of UV method |
| **Intermediate Crossover** | $g_k \sim 1, \beta \sim 1 - 2$ | **`COMPLETELY_UNBRIDGED`** | `OPEN` (`E-CROSSOVER`) | No known convergent series or contractive inductive norm | **OPEN CHOKEPOINT** |
| **IR Starting Point** | $\beta \to \beta_0 \ll 1$ | `METHOD_BOUNDARY` | YM-005 Boundary Record | High-temperature polymer activity condition fails | Boundary of IR method |
| **Strong-Coupling Lattice** | $\beta \le \beta_0 \ll 1$ ($g \gg 1$) | `RIGOROUS_PROVED` (Fixed Lattice) | Osterwalder–Seiler / Shen–Zhu–Zhu | Character expansion, uniform Poincaré inequality | $\Delta_{\text{lat}} > 0$ (on lattice only) |
| **Deep Strong Coupling** ($\beta \to 0$) | $\beta \to 0, g \to \infty$ | `RIGOROUS_PROVED` (Fixed Lattice) | Wilson (1974) | Leading-order character integration, area law | $m_{\text{lat}} \sim \ln(1/\beta) \to \infty$ |

---

## 3. Rendering Instructions for External Visualizers

To render this dual-boundary architecture in ChatGPT or external Markdown renderers:
1. Copy Section 1 directly into ChatGPT with prompt:
   *"Render the dual-boundary structure of 4D Yang–Mills theory, highlighting why the central crossover window g_k ~ 1 prevents connecting Bałaban's UV constructive results with the lattice strong-coupling spectral gap."*
2. Emphasize that the horizontal line dividing UV and IR is not an infinitesimal point, but an extensive, non-perturbative regime spanning the entire order-one coupling window.
