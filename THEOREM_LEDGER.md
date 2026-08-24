# THEOREM LEDGER


## Foundational Yang–Mills Theorems and Results (1954–1980)

### THM-YM-0001: Classical Non-Abelian Gauge Field Invariance and Field Equations
- **THEOREM_ID:** `THM-YM-0001`
- **PAPER_ID:** `PAPER-FOUND-001`
- **TITLE:** Conservation of Isotopic Spin and Isotopic Gauge Invariance
- **AUTHORS:** C. N. Yang, R. L. Mills
- **YEAR:** 1954
- **DOMAIN:** `classical`
- **DIMENSION:** `4`
- **GAUGE_GROUP:** `SU(2)` (compact simple)
- **REGULARIZATION:** `none`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** `arbitrary`
- **LIMITS:** None (classical continuum)
- **ASSUMPTIONS:** Local $SU(2)$ isotopic gauge invariance, minimal coupling principle, spacetime Minkowski $M^4$.
- **EXACT_RESULT:** Explicit non-linear field strength tensor $F_{\\mu\\nu} = \\partial_\\mu B_\\nu - \\partial_\\nu B_\\mu - 2\\epsilon(B_\\mu \\times B_\\nu)$ and Euler–Lagrange variational wave equations $\\partial_\\mu F^{\\mu\\nu} + 2\\epsilon(B_\\mu \\times F^{\\mu\\nu}) + J^\\nu = 0$.
- **EVIDENCE_CLASS:** `RIGOROUS_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** Classical variational calculus and Lie-algebraic local gauge transformations.
- **UNIFORMITY_STATUS:** `NOT_APPLICABLE` (classical)
- **WHAT_IT_PROVES:** Classical geometric consistency of non-Abelian gauge fields and massless relativistic wave equations.
- **WHAT_IT_DOES_NOT_PROVE:** Quantum Hilbert space, quantum existence, renormalizability, asymptotic freedom, mass gap, confinement.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-001`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L182), [`YM-REQ-002`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L183)
- **RELEVANCE_TO_CLAY:** `BACKGROUND`
- **DEPENDENCIES:** None
- **KNOWN_LATER_CORRECTIONS:** Classical waves are massless; quantum theory exhibits mass gap.
- **SOURCE_LOCATOR:** *Phys. Rev.* 96 (1954), pp. 191–195, Eqs. (1)–(15).
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0002: Faddeev–Popov Gauge Fixing and Functional Determinant
- **THEOREM_ID:** `THM-YM-0002`
- **PAPER_ID:** `PAPER-FOUND-002`
- **TITLE:** Feynman Diagrams for the Yang–Mills Field
- **AUTHORS:** L. D. Faddeev, V. N. Popov
- **YEAR:** 1967
- **DOMAIN:** `quantum`
- **DIMENSION:** `4`
- **GAUGE_GROUP:** Compact Lie group $G$
- **REGULARIZATION:** `perturbative regulator`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** `weak` (perturbative)
- **LIMITS:** None (formal functional integral)
- **ASSUMPTIONS:** Functional integral over gauge equivalence classes (orbit space $\\mathcal{A}/\\mathcal{G}$) factorized by inserting identity $1 = \\Delta_f(A) \\int \\mathcal{D}g \\, \\delta(f(A^g))$.
- **EXACT_RESULT:** Integration over gauge group factors out orbit volume, yielding gauge-fixed effective action $S_{eff} = S_{YM} + S_{gf} + S_{ghost}$ with Grassmann ghost fields $c, \\bar{c}$ and ghost determinant $\\Delta_f(A) = \\det(\\mathcal{M}_f) = \\int \\mathcal{D}c \\mathcal{D}\\bar{c} \\exp(i \\int \\bar{c} \\mathcal{M}_f c)$.
- **EVIDENCE_CLASS:** `PERTURBATIVE_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** Formal transformation of variables on functional integrals and Lie group Haar measure.
- **UNIFORMITY_STATUS:** `NOT_APPLICABLE` (formal continuum path integral)
- **WHAT_IT_PROVES:** Unitary perturbative Feynman rules with ghost loops cancelling unphysical longitudinal/timelike gauge degrees of freedom.
- **WHAT_IT_DOES_NOT_PROVE:** Non-perturbative measure on $\\mathcal{A}/\\mathcal{G}$, Gribov ambiguity resolution (Gribov 1978 shows gauge condition $f(A)=0$ has multiple copies at large field amplitudes), non-perturbative mass gap.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-003`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L184), [`YM-REQ-009`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L190)
- **RELEVANCE_TO_CLAY:** `ENABLING`
- **DEPENDENCIES:** `THM-YM-0001`
- **KNOWN_LATER_CORRECTIONS:** Non-perturbatively subject to Gribov horizons and zero-mode obstructions.
- **SOURCE_LOCATOR:** *Phys. Lett. B* 25 (1967), pp. 29–30, Eqs. (1)–(10).
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0003: Perturbative Renormalizability of Massless Yang–Mills Fields
- **THEOREM_ID:** `THM-YM-0003`
- **PAPER_ID:** `PAPER-FOUND-003`
- **TITLE:** Renormalization of Massless Yang–Mills Fields
- **AUTHORS:** G. 't Hooft
- **YEAR:** 1971
- **DOMAIN:** `quantum`
- **DIMENSION:** `4`
- **GAUGE_GROUP:** Compact simple Lie group $G$
- **REGULARIZATION:** `perturbative regulator`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** `weak` (formal power series in $g$)
- **LIMITS:** $g \\to 0$ (perturbative expansion)
- **ASSUMPTIONS:** Order-by-order formal Feynman diagrammatic expansion and Slavnov–Taylor / Ward–Takahashi identities.
- **EXACT_RESULT:** All ultraviolet divergences occurring in the perturbative S-matrix and Green's functions of massless Yang–Mills theory can be canceled to all orders by a finite set of local gauge-invariant counterterms for gauge coupling $g$ and field normalizations.
- **EVIDENCE_CLASS:** `PERTURBATIVE_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** Combinatorial analysis of Feynman graphs, BPHZ subtractions, and gauge-symmetry Ward identities.
- **UNIFORMITY_STATUS:** `NOT_APPLICABLE` (formal power series)
- **WHAT_IT_PROVES:** Order-by-order ultraviolet renormalizability of perturbative Yang–Mills theory.
- **WHAT_IT_DOES_NOT_PROVE:** Non-perturbative mathematical existence of the quantum field theory, convergence or Borel summability of the perturbation series, existence of a non-perturbative mass gap $\\Delta > 0$.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-003`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L184), [`YM-REQ-011`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L192)
- **RELEVANCE_TO_CLAY:** `ENABLING`
- **DEPENDENCIES:** `THM-YM-0001`, `THM-YM-0002`
- **KNOWN_LATER_CORRECTIONS:** Perturbation series is divergent and not Borel-summable due to infrared renormalons (Gross & Neveu 1974, 't Hooft 1979).
- **SOURCE_LOCATOR:** *Nucl. Phys. B* 33 (1971), pp. 173–199, Sections 1–7.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0004: Dimensional Regularization and All-Orders Gauge Ward Identities
- **THEOREM_ID:** `THM-YM-0004`
- **PAPER_ID:** `PAPER-FOUND-012`
- **TITLE:** Regularization and Renormalization of Gauge Fields
- **AUTHORS:** G. 't Hooft, M. Veltman
- **YEAR:** 1972
- **DOMAIN:** `quantum`
- **DIMENSION:** $d = 4 - \\epsilon$
- **GAUGE_GROUP:** Compact Lie group $G$
- **REGULARIZATION:** `dimensional regularization`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** `weak` (perturbative)
- **LIMITS:** $\\epsilon \\to 0$ (pole subtraction)
- **ASSUMPTIONS:** Analytic continuation of loop momentum integrals in complex continuous dimension $d$.
- **EXACT_RESULT:** Dimensional regularization provides a mathematically consistent, Lorentz-invariant and local gauge-invariant regulator for non-Abelian gauge fields, preserving Ward–Takahashi–Slavnov–Taylor identities automatically at all loop orders.
- **EVIDENCE_CLASS:** `PERTURBATIVE_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** Analytic continuation of momentum-space Feynman parameter integrals.
- **UNIFORMITY_STATUS:** `NOT_APPLICABLE` (perturbative)
- **WHAT_IT_PROVES:** Systematic preservation of gauge invariance in perturbative multi-loop renormalization.
- **WHAT_IT_DOES_NOT_PROVE:** Non-perturbative measure or non-perturbative mass gap in $d=4$.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-003`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L184), [`YM-REQ-011`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L192)
- **RELEVANCE_TO_CLAY:** `ENABLING`
- **DEPENDENCIES:** `THM-YM-0002`, `THM-YM-0003`
- **KNOWN_LATER_CORRECTIONS:** Dimensional regularization does not provide a non-perturbative Hilbert space or reflection positivity (Osterwalder–Seiler 1978).
- **SOURCE_LOCATOR:** *Nucl. Phys. B* 44 (1972), pp. 189–213, Sections 1–6.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0005: Osterwalder–Schrader Euclidean Reconstruction Theorem
- **THEOREM_ID:** `THM-YM-0005`
- **PAPER_ID:** `PAPER-FOUND-004`, `PAPER-FOUND-005`
- **TITLE:** Axioms for Euclidean Green's Functions (I & II)
- **AUTHORS:** K. Osterwalder, R. Schrader
- **YEAR:** 1973, 1975
- **DOMAIN:** `axiomatic / constructive`
- **DIMENSION:** $d \\ge 2$ (including $d=4$)
- **GAUGE_GROUP:** General / unconstrained
- **REGULARIZATION:** `none` (tempered Euclidean distributions)
- **VOLUME:** `infinite` ($\\mathbb{R}^d$)
- **COUPLING_REGIME:** `arbitrary`
- **LIMITS:** None (exact continuum distributions)
- **ASSUMPTIONS:** OS-0 (Temperedness & Analyticity at non-coinciding points), OS-1 (Euclidean Invariance under $E(d)$), OS-2 (Reflection Positivity on $t > 0$), OS-3 (Symmetry under Bose permutation), OS-4 (Cluster Decomposition).
- **EXACT_RESULT:** A family of Euclidean Green's functions (Schwinger functions) satisfying OS-0 through OS-4 uniquely defines an analytic continuation to Wightman distributions on Minkowski spacetime satisfying the full Wightman axioms (W-1 through W-7), uniquely determining a separable Hilbert space $\\mathcal{H}$, a unitary representation of the Poincaré group $\\mathcal{P}_+^\\uparrow$, positive energy $H \\ge 0$, and a unique vacuum state $\\Omega$.
- **EVIDENCE_CLASS:** `RIGOROUS_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** Functional analysis, Hilbert space completion via reflection positivity, Laplace/Fourier transform analytic continuation in tube domains (Bargmann–Hall–Wightman theorem).
- **UNIFORMITY_STATUS:** `RIGOROUS_EXACT`
- **WHAT_IT_PROVES:** Complete mathematical equivalence between Euclidean reflection-positive Schwinger distributions and relativistic Wightman quantum field theories.
- **WHAT_IT_DOES_NOT_PROVE:** The construction of 4D Yang–Mills Schwinger functions satisfying OS-0 through OS-4. The OS theorem is an axiomatic reconstruction engine, not an existence proof for interacting Yang–Mills.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-003`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L184), [`YM-REQ-004`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L185), [`YM-REQ-005`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L186), [`YM-REQ-006`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L187), [`YM-REQ-015`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L196)
- **RELEVANCE_TO_CLAY:** `DIRECT`
- **DEPENDENCIES:** Streater & Wightman (1964) [45]
- **KNOWN_LATER_CORRECTIONS:** Initial paper OS I (1973) required refinement in growth/regularity conditions, resolved definitively in OS II (1975).
- **SOURCE_LOCATOR:** *Comm. Math. Phys.* 31 (1973), pp. 83–112; *Comm. Math. Phys.* 42 (1975), pp. 281–305, Theorems 1–3.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0006: Ultraviolet Asymptotic Freedom in Non-Abelian Gauge Theories
- **THEOREM_ID:** `THM-YM-0006`
- **PAPER_ID:** `PAPER-FOUND-006`, `PAPER-FOUND-007`
- **TITLE:** Ultraviolet Behavior of Non-Abelian Gauge Theories / Reliable Perturbative Results for Strong Interactions?
- **AUTHORS:** D. J. Gross, F. Wilczek; H. D. Politzer
- **YEAR:** 1973
- **DOMAIN:** `quantum`
- **DIMENSION:** `4`
- **GAUGE_GROUP:** Compact non-Abelian Lie group $G$ (e.g. $SU(N)$)
- **REGULARIZATION:** `1-loop perturbative RG`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** `asymptotically weak` at high energy ($g(\\mu) \\to 0$ as $\\mu \\to \\infty$)
- **LIMITS:** Energy scale $\\mu \\to \\infty$ (short distance $|x| \\to 0$)
- **ASSUMPTIONS:** 1-loop perturbation theory and Callan–Symanzik renormalization group equation.
- **EXACT_RESULT:** The 1-loop renormalization group beta function for pure non-Abelian gauge theory is strictly negative: $\\beta(g) = -\\frac{b_0}{(4\\pi)^2} g^3 + \\mathcal{O}(g^5)$ with $b_0 = \\frac{11}{3} C_2(G) > 0$ ($b_0 = \\frac{11}{3} N$ for $SU(N)$), causing the effective running coupling constant to vanish logarithmically at short distances: $g^2(\\mu) = \\frac{(4\\pi)^2}{2 b_0 \\ln(\\mu / \\Lambda_{QCD})}$.
- **EVIDENCE_CLASS:** `PERTURBATIVE_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** 1-loop Feynman diagram calculation of vertex and self-energy corrections in background/Feynman gauge.
- **UNIFORMITY_STATUS:** `NOT_APPLICABLE` (asymptotic expansion valid only as $\\mu \\to \\infty$)
- **WHAT_IT_PROVES:** Strict logarithmic ultraviolet weak coupling (asymptotic freedom) for 4D non-Abelian gauge fields.
- **WHAT_IT_DOES_NOT_PROVE:** Non-perturbative infrared behavior, existence of a spectral mass gap $\\Delta > 0$, or non-perturbative confinement. (As $\\mu \\to 0$, $g(\\mu) \\to \\infty$, rendering perturbative RG invalid).
- **RELATED_YM_REQ_IDS:** [`YM-REQ-011`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L192), [`YM-REQ-013`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L194)
- **RELEVANCE_TO_CLAY:** `DIRECT`
- **DEPENDENCIES:** `THM-YM-0002`, `THM-YM-0003`, `THM-YM-0004`
- **KNOWN_LATER_CORRECTIONS:** Perturbative Landau pole at $\\mu = \\Lambda_{QCD}$ is an artifact of truncation and does not determine non-perturbative infrared spectrum.
- **SOURCE_LOCATOR:** *Phys. Rev. Lett.* 30 (1973), pp. 1343–1346; *ibid.* pp. 1346–1349.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0007: Planar Diagram Dominance in the Large-N Limit
- **THEOREM_ID:** `THM-YM-0007`
- **PAPER_ID:** `PAPER-FOUND-008`
- **TITLE:** A Planar Diagram Theory for Strong Interactions
- **AUTHORS:** G. 't Hooft
- **YEAR:** 1974
- **DOMAIN:** `quantum`
- **DIMENSION:** `4` (and `1+1` in 't Hooft model)
- **GAUGE_GROUP:** $SU(N) / U(N)$ with $N \\to \\infty$
- **REGULARIZATION:** `topological 1/N expansion`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** Fixed 't Hooft coupling $\\lambda = g^2 N$
- **LIMITS:** $N \\to \\infty$ with $\\lambda = g^2 N$ fixed
- **ASSUMPTIONS:** Double-line index notation for gluon propagators and topological classification of Feynman graphs by Riemann surfaces of genus $h$.
- **EXACT_RESULT:** Perturbative vacuum diagrams scale as $N^{2 - 2h - L}$, where $h$ is the genus and $L$ the number of quark loops. In the limit $N \\to \\infty$, only planar diagrams ($h=0, L=0$) survive at leading order $\\mathcal{O}(N^2)$, establishing that $1/N$ acts as a topological string coupling constant.
- **EVIDENCE_CLASS:** `FORMAL_DERIVATION`
- **PROOF_OR_DERIVATION_METHOD:** Graph-theoretic Euler characteristic formula $\\chi = V - E + F = 2 - 2h$ on Feynman diagrams.
- **UNIFORMITY_STATUS:** `NOT_APPLICABLE` ($N \\to \\infty$ limit only)
- **WHAT_IT_PROVES:** Leading planar dominance and $1/N$ topological reorganization of gauge theory perturbation series.
- **WHAT_IT_DOES_NOT_PROVE:** Non-perturbative solution of 4D pure Yang–Mills for finite $N$ (e.g. $SU(2)$ or $SU(3)$), mass gap for finite $N$, convergence of planar series in $d=4$.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-001`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L182), [`YM-REQ-030`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L211)
- **RELEVANCE_TO_CLAY:** `ANALOGUE`
- **DEPENDENCIES:** `THM-YM-0001`, `THM-YM-0002`
- **KNOWN_LATER_CORRECTIONS:** Fully solvable in $1+1$ dimensions ('t Hooft model 1974), but 4D planar summation remains an open problem.
- **SOURCE_LOCATOR:** *Nucl. Phys. B* 72 (1974), pp. 461–473, Sections 1–5.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0008: Wilson Lattice Gauge Theory and Strong-Coupling Confinement
- **THEOREM_ID:** `THM-YM-0008`
- **PAPER_ID:** `PAPER-FOUND-009`
- **TITLE:** Confinement of Quarks
- **AUTHORS:** K. G. Wilson
- **YEAR:** 1974
- **DOMAIN:** `lattice`
- **DIMENSION:** `4` (Euclidean hypercubic lattice $\\mathbb{Z}^4$)
- **GAUGE_GROUP:** Compact Lie group $G$ (e.g. $SU(3)$)
- **REGULARIZATION:** `lattice spacing a > 0`
- **VOLUME:** `finite / infinite lattice`
- **COUPLING_REGIME:** `strong` ($g^2 \\gg 1$, $1/g^2 \\ll 1$)
- **LIMITS:** None in leading expansion (fixed lattice cutoff $a > 0$, fixed strong coupling $g$)
- **ASSUMPTIONS:** Gauge field represented by group-valued link variables $U_{x,\\mu} \\in G$; gauge-invariant Wilson plaquette action $S[U] = \\sum_P \\frac{1}{g^2} \\mathrm{Re}\\mathrm{Tr}(1 - U_P)$; invariant Haar measure $\\prod_{x,\\mu} dU_{x,\\mu}$.
- **EXACT_RESULT:** Exact gauge invariance preserved at finite lattice spacing $a > 0$. High-temperature / strong-coupling expansion of Wilson loop expectation value yields an exact area law: $\\langle W(C) \\rangle = \\langle \\mathrm{Tr} \\prod_{l \\in C} U_l \\rangle \\sim \\exp(-\\sigma \\cdot \\mathrm{Area}(C))$ with string tension $\\sigma = \\frac{\\ln(g^2)}{a^2} (1 + \\mathcal{O}(1/g^4))$, proving quark confinement on the strong-coupling lattice.
- **EVIDENCE_CLASS:** `CONTROLLED_EXPANSION`
- **PROOF_OR_DERIVATION_METHOD:** Character expansion of group integrals over compact Lie groups (Peter–Weyl theorem) and polymer/cluster graph summation on hypercubic lattice.
- **UNIFORMITY_STATUS:** `FIXED_LATTICE_ONLY` (expansion radius requires $g^2 \\gg 1$)
- **WHAT_IT_PROVES:** Exact gauge invariance on discrete lattice; quark confinement (Wilson loop area law) on a fixed lattice at strong coupling $g \\gg 1$.
- **WHAT_IT_DOES_NOT_PROVE:** Continuum limit $a \\to 0$, weak-coupling continuum confinement ($g \\to 0$ required by asymptotic freedom), non-perturbative mass gap in the continuum Hilbert space $\\mathcal{H}$.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-003`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L184), [`YM-REQ-018`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L199), [`YM-REQ-021`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L202), [`YM-REQ-022`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L203), [`YM-REQ-025`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L206)
- **RELEVANCE_TO_CLAY:** `DIRECT`
- **DEPENDENCIES:** `THM-YM-0001`
- **KNOWN_LATER_CORRECTIONS:** Strong-coupling lattice expansion has a finite radius of convergence in $1/g^2$ and cannot be directly extrapolated to the weak-coupling continuum limit $g \\to 0$ without non-perturbative control.
- **SOURCE_LOCATOR:** *Phys. Rev. D* 10 (1974), pp. 2445–2459, Sections I–VI.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0009: Lattice Reflection Positivity and Physical Transfer Matrix
- **THEOREM_ID:** `THM-YM-0009`
- **PAPER_ID:** `PAPER-FOUND-013`
- **TITLE:** Gauge Theories on the Lattice
- **AUTHORS:** K. Osterwalder, E. Seiler
- **YEAR:** 1978
- **DOMAIN:** `constructive / lattice`
- **DIMENSION:** $d = 2, 3, 4$
- **GAUGE_GROUP:** Compact Lie group $G$
- **REGULARIZATION:** `lattice spacing a > 0`
- **VOLUME:** `finite / infinite lattice`
- **COUPLING_REGIME:** `arbitrary` ($0 < g < \\infty$)
- **LIMITS:** None (exact on discrete lattice)
- **ASSUMPTIONS:** Wilson lattice action, hypercubic lattice partitioned across a hyperplane into positive and negative time halves.
- **EXACT_RESULT:** Wilson lattice gauge theory satisfies Osterwalder–Schrader reflection positivity $\\langle \\Theta F, F \\rangle \\ge 0$ for all functions $F$ supported on the positive-time half of the lattice. Consequently, the lattice transfer matrix $\\mathbb{T} = e^{-a H_a}$ is a positive self-adjoint contraction operator on a well-defined physical Hilbert space $\\mathcal{H}_a$.
- **EVIDENCE_CLASS:** `RIGOROUS_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** Slicing of compact group Haar measure along spatial hyperplanes, reflection anti-automorphism, and Cauchy–Schwarz inequality for positive measures.
- **UNIFORMITY_STATUS:** `RIGOROUS_EXACT_ON_LATTICE`
- **WHAT_IT_PROVES:** Exact existence of a quantum-mechanical Hilbert space $\\mathcal{H}_a$, positive energy $H_a \\ge 0$, and unitary transfer matrix on the discrete lattice for all couplings $g$.
- **WHAT_IT_DOES_NOT_PROVE:** Uniform lower bound on the spectral gap $\\Delta(a) \\ge \\Delta_0 > 0$ as $a \\to 0$, existence of the continuum limit as $a \\to 0$.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-003`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L184), [`YM-REQ-004`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L185), [`YM-REQ-006`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L187), [`YM-REQ-018`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L199)
- **RELEVANCE_TO_CLAY:** `DIRECT`
- **DEPENDENCIES:** `THM-YM-0005`, `THM-YM-0008`
- **KNOWN_LATER_CORRECTIONS:** None (foundational mathematical property of Wilson lattice action).
- **SOURCE_LOCATOR:** *Ann. Phys.* 110 (1978), pp. 440–471, Sections 1–5, Theorems 1–4.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0010: BPST Classical Instanton Solutions and Topological Charge
- **THEOREM_ID:** `THM-YM-0010`
- **PAPER_ID:** `PAPER-FOUND-010`
- **TITLE:** Pseudoparticle Solutions of the Yang–Mills Equations
- **AUTHORS:** A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Yu. S. Tyupkin
- **YEAR:** 1975
- **DOMAIN:** `classical / topological`
- **DIMENSION:** `4` (Euclidean $\\mathbb{R}^4$)
- **GAUGE_GROUP:** `SU(2)`
- **REGULARIZATION:** `none` (classical continuum)
- **VOLUME:** `infinite` ($\mathbb{R}^4$)
- **COUPLING_REGIME:** `classical`
- **LIMITS:** Boundary condition $F_{\\mu\\nu} \\to 0$ as $|x| \\to \\infty$
- **ASSUMPTIONS:** Self-duality equation $F_{\\mu\\nu} = \\tilde{F}_{\\mu\\nu} = \\frac{1}{2} \\epsilon_{\\mu\\nu\\rho\\sigma} F_{\\rho\\sigma}$.
- **EXACT_RESULT:** Explicit construction of finite-action classical solution in 4D Euclidean space: $A_\\mu^a(x) = \\frac{2 \\eta_{a\\mu\\nu} (x - x_0)_\\nu}{(x - x_0)^2 + \\rho^2}$, with integer topological Pontryagin charge $Q = \\frac{1}{32\\pi^2} \\int \\mathrm{Tr}(F \\wedge F) = 1$ and classical Euclidean action $S = \\frac{8\\pi^2}{g^2}$.
- **EVIDENCE_CLASS:** `RIGOROUS_THEOREM`
- **PROOF_OR_DERIVATION_METHOD:** Exact solution of non-linear first-order self-duality Bogomolny equations and homotopy classification $\\pi_3(SU(2)) \\cong \\mathbb{Z}$.
- **UNIFORMITY_STATUS:** `NOT_APPLICABLE` (classical solution)
- **WHAT_IT_PROVES:** Existence of non-trivial topological sectors, vacuum tunneling instantons, and finite-action localized classical configurations in 4D Euclidean Yang–Mills.
- **WHAT_IT_DOES_NOT_PROVE:** Quantum mass gap, quantum confinement, or non-perturbative quantum continuum measure.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-002`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L183), [`YM-REQ-009`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L190)
- **RELEVANCE_TO_CLAY:** `ANALOGUE`
- **DEPENDENCIES:** `THM-YM-0001`
- **KNOWN_LATER_CORRECTIONS:** Semiclassical instanton gas calculations in 4D suffer from scale-integration divergences over instanton size $\\rho$ in the infrared ($\int d\\rho / \\rho^5$).
- **SOURCE_LOCATOR:** *Phys. Lett. B* 59 (1975), pp. 85–87, Eqs. (1)–(8).
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0011: Monopole Debye Screening and Mass Gap in (2+1)-Dimensional Compact QED
- **THEOREM_ID:** `THM-YM-0011`
- **PAPER_ID:** `PAPER-FOUND-011`
- **TITLE:** Quark Confinement and Topology of Gauge Theories (Part A: 2+1D Compact QED)
- **AUTHORS:** A. M. Polyakov
- **YEAR:** 1977
- **DOMAIN:** `quantum / constructive`
- **DIMENSION:** `2+1` (3D Euclidean)
- **GAUGE_GROUP:** `U(1)` (compact Abelian)
- **REGULARIZATION:** `lattice / UV cutoff`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** `weak` ($e^2 \\ll 1$)
- **LIMITS:** $V \\to \\infty$
- **ASSUMPTIONS:** Compact $U(1)$ gauge theory on 3D lattice, compact gauge field admitting magnetic monopoles (instantons in $2+1$ dimensions) with action $S_{mono} \\sim \\text{const}/e^2$.
- **EXACT_RESULT:** Topological magnetic monopoles form a dilute gas equivalent to a 3D classical Coulomb plasma with Debye screening. The dual photon acquires a non-zero mass gap $\\Delta \\sim M \\exp(-S_{mono}/2) > 0$, generating an exact exponential decay of magnetic correlations and an exact linear confining potential (area law) for Wilson loops.
- **EVIDENCE_CLASS:** `RIGOROUS_THEOREM` (semiclassical plasma mapping made mathematically rigorous by Brydges, Fröhlich, Spencer 1980 / Göpfert & Mack 1981)
- **PROOF_OR_DERIVATION_METHOD:** Duality transformation mapping compact $U(1)$ lattice gauge field to a 3D sine-Gordon / Coulomb gas model, followed by Debye screening cluster expansion.
- **UNIFORMITY_STATUS:** `RIGOROUS_BOUND` in $2+1$ dimensions
- **WHAT_IT_PROVES:** Rigorous mechanism for dynamical mass gap generation and confinement from topological defects in (2+1)-dimensional compact $U(1)$ gauge theory.
- **WHAT_IT_DOES_NOT_PROVE:** Mass gap or confinement in (3+1)-dimensional pure non-Abelian Yang–Mills theory.
- **RELATED_YM_REQ_IDS:** [`YM-REQ-007`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L188), [`YM-REQ-020`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L201)
- **RELEVANCE_TO_CLAY:** `ANALOGUE`
- **DEPENDENCIES:** `THM-YM-0008`
- **KNOWN_LATER_CORRECTIONS:** Made completely rigorous by Göpfert & Mack (1981) and Brydges & Federbush (1980) as noted in Jaffe & Witten [6].
- **SOURCE_LOCATOR:** *Nucl. Phys. B* 120 (1977), pp. 429–458, Sections 1–4.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`

---

### THM-YM-0012: Semiclassical Instanton Gas Proposal for 4D Non-Abelian Gauge Theories
- **THEOREM_ID:** `THM-YM-0012`
- **PAPER_ID:** `PAPER-FOUND-011`
- **TITLE:** Quark Confinement and Topology of Gauge Theories (Part B: 4D Non-Abelian Proposal)
- **AUTHORS:** A. M. Polyakov
- **YEAR:** 1977
- **DOMAIN:** `quantum / semiclassical`
- **DIMENSION:** `4`
- **GAUGE_GROUP:** `SU(2)`
- **REGULARIZATION:** `cutoff instanton gas`
- **VOLUME:** `infinite`
- **COUPLING_REGIME:** `semiclassical / weak`
- **LIMITS:** Infrared cutoff required
- **ASSUMPTIONS:** Semiclassical approximation of 4D path integral by a gas of non-interacting instantons and anti-instantons.
- **EXACT_RESULT:** Polyakov proposed that instanton gas density fluctuations in 4D Euclidean Yang–Mills could produce confinement and a mass gap by analogy with the 2+1D monopole gas.
- **EVIDENCE_CLASS:** `CONJECTURE_OR_PROPOSAL`
- **PROOF_OR_DERIVATION_METHOD:** Heuristic analogy with 3D Coulomb gas and 1-loop instanton determinant.
- **UNIFORMITY_STATUS:** `UNCONTROLLED` (infrared divergent)
- **WHAT_IT_PROVES:** Physical heuristics motivating topological vacuum structure in 4D.
- **WHAT_IT_DOES_NOT_PROVE:** Mass gap, confinement, or mathematical existence of 4D Yang–Mills. (The 4D dilute instanton gas is uncontrolled due to the infrared divergence of large instantons $\\int d\\rho / \\rho^5$).
- **RELATED_YM_REQ_IDS:** [`YM-REQ-007`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L188), [`YM-REQ-025`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/OFFICIAL_PROBLEM_SPECIFICATION.md#L206)
- **RELEVANCE_TO_CLAY:** `BACKGROUND`
- **DEPENDENCIES:** `THM-YM-0010`, `THM-YM-0011`
- **KNOWN_LATER_CORRECTIONS:** Semiclassical dilute instanton gas is invalid in the infrared in 4D pure Yang–Mills due to strong coupling and large instanton overlap.
- **SOURCE_LOCATOR:** *Nucl. Phys. B* 120 (1977), pp. 429–458, Sections 5–6.
- **REPRODUCTION_STATUS:** `RECONSTRUCTED`
- **STATUS:** `VERIFIED_FROM_PRIMARY_SOURCE`
