# NEGATIVE EVIDENCE REGISTER

## Registered Negative Findings and Operational Disclosures

### NEG-001: Packaging and editable install failure during YM-000 bootstrap
- **Discovery Date:** 2026-08-24
- **Finding:** Editable installation (`pip install -e .`) failed in isolated environments without build tools.
- **Resolution:** Removed unnecessary editable-install dependency, switching to clean PYTHONPATH-based test execution.

### NEG-002: YM-001 Negative Disclosure and Inaccessible / Partial Definitions
- **Discovery Date:** 2026-08-24
- **Items Not Present or Partially Defined in Official Source:**
  1. *Operational Definition of "Non-trivial":* The official text uses the phrase "non-trivial quantum Yang–Mills theory" without providing a single closed algebraic equation. Marked `PARTIAL_SOURCE_DEFINITION` / `REQUIRES_FOLLOWUP`.
  2. *Full Reconstruction of OS / Wightman Axioms:* Detailed line-by-line reconstruction of the full Osterwalder–Schrader ([35]) and Wightman ([45]) axiom sets is bounded into follow-up tasks (YM-001A / YM-001B).
  3. *Unresolved Differences in Non-Gauge-Invariant Observables:* The Euclidean OS reconstruction specifically addresses gauge-invariant local observables; full gauge-dependent operator reconstruction is noted as mathematically open in the literature.

### NEG-003: Foundational Literature Scope Boundaries (1954–1980)
- **Discovery Date:** 2026-08-24
- **Scope Boundaries Established:**
  1. *Classical vs. Quantum:* The 1954 Yang–Mills classical equations (`THM-YM-0001`) describe massless waves; classical non-Abelian gauge invariance does not imply a quantum mass gap.
  2. *Perturbative Renormalizability vs. Non-Perturbative Existence:* 't Hooft's 1971 proof (`THM-YM-0003`) and 't Hooft–Veltman dimensional regularization (`THM-YM-0004`) establish order-by-order perturbative renormalizability, but the perturbation series is divergent (renormalons) and does not yield a non-perturbative measure.
  3. *UV Asymptotic Freedom vs. IR Mass Gap:* Asymptotic freedom (`THM-YM-0006`) provides logarithmic weak coupling at short distances, but leads to strong coupling in the infrared where perturbation theory fails to determine the mass spectrum.
  4. *Fixed-Lattice Strong-Coupling Confinement vs. Continuum Limit:* Wilson's 1974 lattice area law (`THM-YM-0008`) holds for $g^2 \gg 1$ at fixed $a > 0$, but the continuum limit requires $a \to 0$ ($g \to 0$), which cannot be reached via strong-coupling expansions alone.
  5. *Lower-Dimensional Monopole Gap vs. 4D Pure Yang–Mills:* Polyakov's 1977 mass gap result (`THM-YM-0011`) provides a semiclassical derivation in $2+1$ dimensions for compact $U(1)$ (elevated to a rigorous lattice theorem by Göpfert & Mack 1981 / Brydges et al. 1980), but cannot be transferred to $3+1$ dimensions where the 4D dilute instanton gas is infrared-divergent and uncontrolled (`THM-YM-0012`).
  6. *Reconstruction Machinery vs. Field Construction:* Osterwalder–Schrader reconstruction (`THM-YM-0005`) provides the necessary conditions to pass from Euclidean to Minkowski QFT (with OS II 1975 extending and correcting OS I 1973), but does not construct the 4D Yang–Mills measure.

### NEG-004: Gribov Ambiguity and Global Gauge Fixing Obstruction
- **Discovery Date:** 2026-08-24
- **Finding:** Faddeev–Popov gauge fixing (`THM-YM-0002`, 1967) relies on a local gauge condition $f(A)=0$. Gribov (1978, `PAPER-FOUND-014`) proved that for large field amplitudes, non-Abelian gauge orbits intersect the gauge condition multiple times (Gribov copies). Thus, Faddeev–Popov quantization is strictly a local perturbative tool and cannot be extended globally without resolving Gribov horizon boundaries.


### NEG-CONST-001: The 4D Infinite-Volume Infrared Boundary in Bałaban's RG Program
- **Discovery Date:** 2026-08-24
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[LATER_LITERATURE_LIMITATION]`
- **Finding:** Bałaban's multi-scale block-spin RG program achieves complete mathematical control over the ultraviolet limit ($a \to 0$) in any finite volume $V < \infty$, but was bounded at the finite-volume boundary. In 4D, as the RG scale descends toward the infrared ($V \to \infty$), asymptotic freedom causes the effective coupling to grow ($g_k \sim 1$), preventing small-field inductive bounds and large-field polymer expansions from controlling the thermodynamic infinite-volume limit without a separate non-perturbative infrared closure mechanism.

### NEG-CONST-002: Infrared Cutoff Removal Obstruction in Constructive $YM_4$
- **Discovery Date:** 2026-08-24
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[LATER_LITERATURE_LIMITATION]`
- **Finding:** Magnen, Rivasseau, and Sénéor (1993, *CMP* 155, 325) proved that 4D Euclidean Yang–Mills exists constructively in the presence of an artificial infrared cutoff $\Lambda_{IR} > 0$, explicitly stating that the removal of the infrared cutoff ($\Lambda_{IR} \to 0$) remains open. In constructive field theory literature, removing $\Lambda_{IR}$ without an established isolated vacuum and positive mass gap $\Delta > 0$ encounters infrared renormalon divergences and unbounded long-distance fluctuations.

### NEG-CONST-003: Dimensional and Non-Abelian Boundaries in Monopole Confinement
- **Discovery Date:** 2026-08-24
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** Göpfert & Mack (1981) rigorously proved confinement and mass gap for 3D $U(1)$ lattice gauge theory via monopole Coulomb gas duality. In 4D Euclidean spacetime, magnetic monopoles form 1D closed worldlines / current loops rather than 0D point events (with Dirac strings forming 2D Dirac sheets bounded by the loops), and the non-Abelian field self-interaction $[A_\mu, A_\nu]$ obstructs direct Hodge-star scalar duality. No direct mathematical extension from 3D Abelian duality to 4D non-Abelian Yang–Mills has been established, though no impossibility theorem rules out confinement via dual superconductor mechanisms.


### NEG-MOD-001: Dimensional Criticality Barrier in 4D Stochastic Yang–Mills Quantization
- **Discovery Date:** 2026-08-25
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** Chandra, Chevyrev, Hairer, and Shen (2024) established rigorous stochastic quantization for Yang–Mills–Higgs in 2D and 3D. However, in 4D spacetime, stochastic Yang–Mills is critically singular, meaning that standard local polynomial counterterms and regularity structures are insufficient to control UV fluctuations, leaving 4D stochastic quantization open.

### NEG-MOD-002: Infinite-Loop Truncation Barrier in Continuum Lattice Bootstrap
- **Discovery Date:** 2026-08-25
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** The Makeenko–Migdal loop equation bootstrap (Kazakov & Zheng 2022) provides rigorous upper and lower bounds on lattice observables at fixed lattice spacing $a > 0$. However, taking the continuum limit $a 	o 0$ requires loops of arbitrarily large perimeter ($L_{max} 	o \infty$), causing truncated semidefinite bootstrap matrices to lose rigorous closure without independent non-perturbative continuum bounds.

### NEG-MOD-003: Triviality of the Massive Continuum Scaling Limit in Gauge-Higgs Systems
- **Discovery Date:** 2026-08-25
- **Epistemic Classification:** `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Finding:** Chatterjee (2024) proved that 4D $SU(2)$ Yang–Mills–Higgs under joint parameter scaling produces a continuum field with a strictly positive mass gap $m > 0$. However, because the mass generation is driven by Higgs condensation, the resulting continuum field is a free Gaussian field (trivial $S$-matrix), which does not solve the interacting non-Abelian pure Yang–Mills problem.
