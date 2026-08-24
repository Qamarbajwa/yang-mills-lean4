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

