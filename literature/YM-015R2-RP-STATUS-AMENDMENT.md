# YM-015R2: REFLECTION POSITIVITY STATUS REPAIR AND EPISTEMIC AMENDMENT

## 1. Executive Summary & Epistemic Scope

Task `YM-015R2` provides the definitive, mathematically sound epistemic repair of the reflection positivity (OS2) status of gradient-flowed observables in four-dimensional lattice Yang–Mills theory.

In Revision 32 (Task `YM-015R`), the discovery of heat-kernel leakage across the Euclidean time reflection hyperplane $\{x_4 = 0\}$ was correctly proved. However, Revision 32 made an unwarranted logical jump: it equated the failure of standard half-space algebra membership ($\mathcal{O}_t(f) \notin \mathcal{A}_+$) with the strong assertion that exact reflection positivity is mathematically false ($\langle \Theta F_t F_t \rangle < 0$).

This document formally distinguishes four distinct mathematical statements, amends the status of Theorem `YM-015-L3`, excises unproved "RP defect" formulas, and establishes the precise status of reflection positivity in four-dimensional gradient flow.

---

## 2. Four-Tier Distinction in Reflection Positivity

Let $\Lambda = (a\mathbb{Z}/La\mathbb{Z})^4$ be a 4D periodic Euclidean lattice, $\mu_a$ the Wilson probability measure, and $\Theta$ the Euclidean time reflection operator $\Theta(x_1, x_2, x_3, x_4) = (x_1, x_2, x_3, -x_4)$.

Let $\mathcal{A}_+$ denote the standard positive-time local lattice algebra, consisting of all functions of link variables $U_\mu(x)$ whose support lies in the positive half-space $x_4 \ge 0$ (specifically, spatial links at $x_4 \ge 0$ and temporal links connecting $x_4 \ge 0$ to $x_4 + a$).

Standard lattice Osterwalder–Schrader reflection positivity (OS2) states:
$$\forall F \in \mathcal{A}_+, \quad \langle \Theta(F) F \rangle_{\mu_a} \ge 0.$$

When an observable $F_t = F[V_t(U)]$ is constructed via 4D gradient flow at flow time $t > 0$, we must strictly separate the following four propositions:

| Proposition | Statement | Logical Status in 4D Flow | Proof / Justification |
|---|---|---|---|
| **Tier 1** | `NOT_IN_STANDARD_POSITIVE_TIME_ALGEBRA` | **PROVED TRUE** | Parabolic heat diffusion $K_t(x-y) > 0$ everywhere implies flowed links at $x_4 > 0$ depend on bare links at $x_4 < 0$. Thus $F_t \notin \mathcal{A}_+$. |
| **Tier 2** | `STANDARD_RP_THEOREM_NOT_APPLICABLE` | **PROVED TRUE** | Because $F_t \notin \mathcal{A}_+$, the hypothesis of the standard OS reflection positivity theorem is unsatisfied. Standard inheritance cannot be invoked as a proof. |
| **Tier 3** | `RP_QUADRATIC_FORM_IS_NEGATIVE` | **UNPROVED / NO COUNTEREXAMPLE** | Heat-kernel leakage does NOT prove that $\langle \Theta(F_t) F_t \rangle_{\mu_a} < 0$. Whether there exists any gauge-invariant flowed observable with a negative quadratic form is mathematically open. |
| **Tier 4** | `EXACT_RP_IS_FALSE` | **UNPROVED / NO COUNTEREXAMPLE** | Falsification of a quadratic inequality $\langle \Theta F F \rangle \ge 0$ strictly requires an explicit counterexample. In the absence of an explicit $F_t$ with $\langle \Theta F_t F_t \rangle < 0$, claiming exact RP is false is a non-sequitur. |

---

## 3. Formal Reclassification of Theorem YM-015-L3

Based on the four-tier distinction:

```
[YM-015 Original Claim]
  "Exact RP proved for buffered observables delta > sqrt(8t)"
       │
       ▼ [YM-015R Stress Test]
  "Exact RP refuted for all finite flow times" (OVERSTATED)
       │
       ▼ [YM-015R2 Precise Scientific Repair]
  Status: EXACT_RP_UNRESOLVED_FOR_FINITE_4D_FLOW_TIME
  Sub-Result: STANDARD_HALF_SPACE_RP_INHERITANCE_FAILS_AS_A_PROOF_METHOD
```

### Authoritative Ledger Entry for YM-015-L3
- **Theorem ID:** `YM-015-L3`
- **Original Claim:** Reflection positivity inherited for $\operatorname{dist}(\operatorname{supp} f, \{x_4 = 0\}) > \sqrt{8t}$.
- **Established Mathematical Fact:** Standard half-space support inheritance fails identically for all finite $\delta < \infty$ due to infinite support of parabolic diffusion:
  $$P_{\mathrm{leak}}(t, \delta) = \frac{1}{2}\operatorname{erfc}\left(\frac{\delta}{\sqrt{4t}}\right) > 0.$$
- **Counterexample Search:** A systematic search of the literature and explicit test observables (such as flowed plaquette loops, flowed Polyakov loops, and flowed field-strength polynomials) reveals **zero known instances** where $\langle \Theta(F_t) F_t \rangle_{\mu_a} < 0$. Evaluating $\langle \Theta F_t F_t \rangle$ requires non-perturbative correlation functions of the full non-linear flow.
- **Formal Status:** **`EXACT_RP_UNRESOLVED_FOR_FINITE_4D_FLOW_TIME`**
- **Established Sub-Result:** **`STANDARD_HALF_SPACE_RP_INHERITANCE_FAILS_AS_A_PROOF_METHOD`**

---

## 4. Deconstruction of the Unproved "RP Defect" Theorem

In Revision 32, the quantity:
$$\Delta_{\mathrm{RP}}(t, \delta) \lesssim e^{-\delta^2/(4t)}$$
was cited as the "exact reflection positivity defect."

### Rigorous Audit:
1. The expression $\frac{1}{2}\operatorname{erfc}(\delta/\sqrt{4t}) \sim \frac{\sqrt{t}}{\delta\sqrt{\pi}} e^{-\delta^2/(4t)}$ is the **scalar tail probability of the linear Euclidean heat kernel** in $\mathbb{R}^4$.
2. The Yang–Mills gradient flow on the lattice is a **coupled, non-linear, Lie-algebra-valued dynamical system**:
   $$\partial_t V_t(x, \mu) = - g_0^2 \left( \sum_{\nu \ne \mu} (V_t(x, \mu\nu) - V_t(x, \mu\nu)^\dagger) \right) V_t(x, \mu).$$
3. Connecting the scalar heat-kernel tail to an expectation value defect:
   $$\Delta_{\mathrm{OS}}(F_t) \equiv \max\left(0, -\frac{\langle \Theta(F_t) F_t \rangle_{\mu_a}}{\|F_t\|^2}\right)$$
   requires controlling:
   - The non-linear Jacobian $\frac{\delta V_t(x, \mu)}{\delta U_\rho(y)}$ across the reflection plane;
   - The non-Abelian ordering of Lie algebra exponentials along the flow trajectory;
   - Integration with respect to the correlated, non-Gaussian Wilson lattice measure $\mu_a$, rather than a free Gaussian product measure;
   - Uniform bounds over the entire configuration manifold $\Omega_a = SU(N)^{4|\Lambda_a|}$, including large-field configurations;
   - Thermodynamic and continuum scaling limits.
4. None of these mathematical bounds exist in the published literature.
5. In particular, any claim that $\Delta_{\mathrm{OS}} \le C e^{-\delta^2/(4t)}$ holds for the full Wilson measure is a **heuristic extrapolation** from free field theory.

### Epistemic Ruling:
The formula $\Delta_{\mathrm{RP}} \lesssim e^{-\delta^2/(4t)}$ is formally classified as a:
$$\mathbf{CONJECTURAL\_ERROR\_MODEL}$$
It is hereby **excised from all theorem-level reasoning** and proof graphs in this project.

---

## 5. Epistemic Correction to Route C (Two-Stage Limit)

In Revision 32, Route C was described as:
`ROUTE C = EXACT RP RECOVERED AS t -> 0`.

This phrasing is premature and conflates an architectural program with a proved theorem.

### Corrected Status:
$$\mathbf{ROUTE\ C = CANDIDATE\ LOCALITY-RECOVERY\ ARCHITECTURE}$$

To promote Route C to a proved mathematical theorem requires establishing two separate, non-trivial load-bearing lemmas:
1. **Lemma C.1 (Fixed-$t$ Continuum Object):** Existence of a well-defined continuum multilinear distribution system at fixed $t > 0$ along the asymptotically free trajectory (the target of `E-UV-FLOWED`).
2. **Lemma C.2 (Controlled $t \downarrow 0$ OS Form Convergence):** Existence of a local observable algebra $\mathcal{A}_0$ and an OS-form continuity theorem:
   $$\lim_{t \downarrow 0} \lim_{a \to 0} \langle \Theta(\mathcal{O}_{a,t}(f)) \mathcal{O}_{a,t}(f) \rangle_a = \langle \Theta(\mathcal{O}_0(f)) \mathcal{O}_0(f) \rangle \ge 0.$$

Neither Lemma C.1 nor Lemma C.2 may be assumed. Both remain open research targets.
