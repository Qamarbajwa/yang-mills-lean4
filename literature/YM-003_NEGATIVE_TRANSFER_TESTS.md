# YM-003 NEGATIVE TRANSFER TESTS & COMPOSITION AUDIT

This document records the checked-in regression corpus and explanations of rejected compositions and invalid inferences.

## 1. Rejected Inferences and Epistemic Violations

### Case NEG-001: Volume-Uniform Estimate Promoted to Continuum Control
- **Description:** Attempting to infer weak-coupling continuum limit from an estimate that is uniform in volume at fixed lattice spacing.
- **Why Rejected:** A bound may be uniform in $V$ while completely blowing up as $a \to 0$. Uniformity in volume does not control ultraviolet scaling.
- **Epistemic Classification:** `INVALID_INFERENCE`
- **Governing Invariant:** `Uniformity inside a regime is not control across a regime transition.`

### Case NEG-002: Fixed-Lattice Gap Promoted to Continuum Mass Gap
- **Description:** Conflating the fixed-lattice spectral gap $\Delta_{\text{lattice}}(a) > 0$ with the continuum physical mass gap.
- **Why Rejected:** As $a \to 0$, $\Delta_{\text{lattice}}$ may scale as $O(a)$ or vanish, yielding $\Delta_{\text{phys}} = \lim \Delta/a = 0$ or undefined.
- **Epistemic Classification:** `LATTICE_CONTINUUM_CONFLATION`

### Case NEG-003: Semiclassical Instanton Gas Extrapolated to Infrared
- **Description:** Assuming dilute instanton gas approximations hold at scales $x \sim 1/\Lambda_{\text{QCD}}$.
- **Why Rejected:** Instanton action integral diverges in the infrared due to scale invariance of classical Yang-Mills; dilute gas assumption collapses.
- **Epistemic Classification:** `SEMICLASSICAL_IR_BREAKDOWN`

### Case NEG-004: Gauge-Variant Propagator Pole Promoted to Physical Mass Gap
- **Description:** Deducing a physical mass gap from gluon propagator poles in Landau or Feynman gauge.
- **Why Rejected:** Gluon propagator is gauge-dependent and not a physical observable; gauge-variant poles violate Osterwalder-Schrader reflection positivity.
- **Epistemic Classification:** `GAUGE_VARIANT_PROMOTION`

### Case NEG-005: Analogue Model Direct Transfer Without Barrier Removal
- **Description:** Exporting Seiberg-Witten $\mathcal{N}=2$ or Schwinger 2D mass mechanisms to pure 4D non-Abelian Yang-Mills.
- **Why Rejected:** Every analogue model possesses a documented `TRANSFER_OBSTRUCTION` (e.g. absence of transverse propagating gluons in 2D; requirement of fundamental scalar condensates in Higgs theories; requirement of holomorphy and extended SUSY in Seiberg-Witten).
- **Epistemic Classification:** `INVALID_ANALOGUE_TRANSFER`

### Case NEG-006: Ordinary Cyclic Proof Dependency
- **Description:** Edge A depends on Edge B, which depends on Edge A, without simultaneous fixed-point justification.
- **Why Rejected:** Proof dependencies must be strictly acyclic DAGs. Circular proof claims fail closed.
- **Epistemic Classification:** `CIRCULAR_PROOF_DEPENDENCY`

### Case NEG-007: Silent Assumption Disappearance
- **Description:** An entering assumption (e.g. $V < \infty$ or $a > 0$) is omitted from subsequent nodes without a formal discharge theorem.
- **Why Rejected:** Every assumption must be preserved, discharged with cited evidence, strengthened, weakened, or newly introduced. Silent disappearance fails closed.
- **Epistemic Classification:** `SILENT_ASSUMPTION_DISAPPEARANCE`
