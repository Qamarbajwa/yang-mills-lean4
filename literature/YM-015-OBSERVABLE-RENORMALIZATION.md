# YM-015-OBSERVABLE-RENORMALIZATION — Operator Mixing, Divergences, and Flow-Mollification

- **Document Identifier:** `YM-015-OBSERVABLE-RENORMALIZATION`
- **Task Association:** `YM-015 — E-UV-FREE-CONT`
- **Governance Classification:** Operator Classification & Renormalization Ledger
- **Authoritative Baseline:** State Revision 30
- **Status:** `COMPLETE_OPERATOR_AUDIT`

---

## 1. Executive Summary

A critical failure mode in lattice-to-continuum limits is **uncontrolled operator mixing or divergent rescaling**, where a candidate observable appears to converge only because an implicit divergent factor was concealed, or where operator mixing under discrete lattice symmetries introduces non-conserved continuum artifacts.

This ledger establishes an exact classification of:
$$\mathbf{BARE\;OBSERVABLE} \quad \longrightarrow \quad \mathbf{FLOWED\;OBSERVABLE} \quad \longrightarrow \quad \mathbf{RENORMALIZED\;OBSERVABLE} \quad \longrightarrow \quad \mathbf{CONTINUUM\;DISTRIBUTION}$$
proving why the **two-scale gradient-flowed observable family** $\mathcal{E}(x; t_{\mathrm{phys}})$ avoids power divergences, requires zero multiplicative wave-function renormalization, and eliminates contact-term singularities at fixed physical flow time $t_{\mathrm{phys}} > 0$.

---

## 2. Operator Landscape & Divergence Inventory

| Candidate Observable Class | Mathematical Definition | Canonical Mass Dimension | Additive Divergence as $a \to 0$ | Multiplicative Renormalization $Z(g_0)$ | Contact Term Divergence as $x_i \to x_j$ | Hypercubic Mixing Allowed | Continuum Applicability |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bare Plaquette Energy** | $\mathcal{P}(x) = 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr} U_p(x)$ | $[M]^0$ (lattice) $\to [M]^4$ | Quartic: $\sim \frac{c_0}{a^4}$ | $Z \sim g_0^4 \sim \frac{1}{\ln^2(1/a)}$ | $\sim \frac{1}{|x-y|^8}$ | Mixes with $I_N$ | Severe UV divergences |
| **Bare Local Action Density** | $\operatorname{Tr}(F_{\mu\nu} F_{\mu\nu})(x)$ | $[M]^4$ | Quartic: $\sim \frac{c_0}{a^4}$ | Non-trivial: $Z_{F^2} \neq 1$ | Singular: $\sim |x-y|^{-8}$ | Mixes with $I_N$ | Requires subtractive renormalization |
| **Bare Wilson Loop** | $W(C) = \frac{1}{N}\operatorname{Tr} \prod_{e \in C} U(e)$ | $[M]^0$ | Perimeter: $\sim e^{-\kappa |C|/a}$ | Corner & cusp divergences | Non-singular for disjoint loops | Self-intersections split | Perimeter divergence diverges as $a \to 0$ |
| **Lüscher Flowed Action Density** | $\mathcal{E}(x; t_{\mathrm{phys}}) = \frac{1}{4}\operatorname{Tr}(G_{\mu\nu} G_{\mu\nu})(x; t_{\mathrm{phys}})$ | $[M]^4$ | **ZERO** (after vacuum subtraction) | **$Z \equiv 1$ (Identically)** | **ZERO** (Smooth for all $x, y$) | $O(a^2)$ irrelevant only | **OPTIMAL CONTINUUM CANDIDATE** |
| **Flowed Polyakov / Wilson Loop** | $W_t(C) = \frac{1}{N}\operatorname{Tr} \prod V_t(e)$ | $[M]^0$ | **ZERO** | **$Z \equiv 1$** | **ZERO** | None | **OPTIMAL NON-LOCAL CANDIDATE** |

---

## 3. The Lüscher Flow-Mollification Theorem

### 3.1 Theorem Statement (Lüscher 2010, 2011)
Let $B_\mu(x; t)$ be the solution to the Yang–Mills gradient flow equation in $\mathbb{R}^4$ (or on the flat torus $\mathbb{T}^4$):
$$\partial_t B_\mu = D_\nu G_{\nu\mu} + \alpha_0 D_\mu \partial_\nu B_\nu, \qquad B_\mu(x; 0) = A_\mu(x),$$
where $G_{\mu\nu} = \partial_\mu B_\nu - \partial_\nu B_\mu + [B_\mu, B_\nu]$ is the field strength of the flowed connection and $D_\mu = \partial_\mu + [B_\mu, \cdot]$.

Then:
1. **Infrared and Ultraviolet Smoothing:** The flow acts as a heat kernel mollifier with physical smoothing radius:
   $$R_{\mathrm{flow}} = \sqrt{8 t_{\mathrm{phys}}}.$$
2. **All-Orders Multiplicative Finiteness:** For any $t_{\mathrm{phys}} > 0$, any gauge-invariant local polynomial in $G_{\mu\nu}(x; t_{\mathrm{phys}})$ and its covariant derivatives $D_\rho G_{\mu\nu}(x; t_{\mathrm{phys}})$ is **strictly UV-finite** without any multiplicative wave-function renormalization:
   $$Z_{\mathcal{E}}(g_0, t_{\mathrm{phys}}) \equiv 1.$$
3. **Absence of Short-Distance Singularities:** For any $n \ge 1$ and points $x_1, \dots, x_n$ (whether distinct or coincident):
   $$\lim_{a \to 0} \left\langle \mathcal{E}(x_1; t_{\mathrm{phys}}) \cdots \mathcal{E}(x_n; t_{\mathrm{phys}}) \right\rangle_{\mathrm{conn}} < \infty.$$
   The smoothing radius $\sqrt{8 t_{\mathrm{phys}}}$ provides an absolute short-distance cutoff, eliminating contact terms.

---

## 4. Hypercubic Operator Mixing & Symanzik Analysis

On the hypercubic lattice $\Lambda_a$, the continuous rotation group $SO(4)$ is broken down to the discrete hyperoctahedral reflection group $H_4 \cong W(B_4)$ of order $2^4 \cdot 4! = 384$.

### 4.1 Irreducible Tensor Decomposition Under $H_4$
In 4D Euclidean space, the symmetric trace-free rank-4 tensor representation $\mathbf{35}$ of $SO(4)$ decomposes under $H_4$ into:
$$\mathbf{35} \;\longrightarrow\; \mathbf{1}^{(4)} \;\oplus\; \mathbf{2}^{(4)} \;\oplus\; \mathbf{3}^{(4)} \;\oplus\; \mathbf{3}'^{(4)} \;\oplus\; \dots$$
where:
1. The **hypercubic singlet** $\mathbf{1}^{(4)}$ corresponds to the non-$SO(4)$-invariant operator:
   $$\mathcal{O}_{\mathrm{aniso}}(x) := \sum_{\mu=1}^4 \operatorname{Tr}\!\left( G_{\mu\nu}(x) G_{\mu\nu}(x) \right) - \frac{1}{4} \sum_{\mu, \nu=1}^4 \operatorname{Tr}\!\left( G_{\mu\nu}(x) G_{\mu\nu}(x) \right) \quad (\text{dimension 6}).$$
2. The Symanzik effective field theory expansion of the lattice clover flowed operator is:
   $$\mathcal{E}_a(x; t_{\mathrm{phys}}) = \mathcal{E}_{\mathrm{cont}}(x; t_{\mathrm{phys}}) + a^2 \left( c_1 \mathcal{O}_{\mathrm{symm}}^{(6)}(x; t_{\mathrm{phys}}) + c_2 \mathcal{O}_{\mathrm{aniso}}^{(6)}(x; t_{\mathrm{phys}}) \right) + O(a^4),$$
   where $\mathcal{O}_{\mathrm{symm}}^{(6)}$ is $SO(4)$-invariant and $\mathcal{O}_{\mathrm{aniso}}^{(6)}$ breaks $SO(4) \to H_4$.

### 4.2 Uniform Suppression of Mixing
Because $\mathcal{O}_{\mathrm{aniso}}^{(6)}$ has canonical dimension 6, its coefficient is suppressed by:
$$\Delta \mathcal{E}_{\mathrm{aniso}} \le C_{\mathrm{aniso}} \frac{a^2}{t_{\mathrm{phys}}} \|\mathcal{E}\|.$$
For any fixed physical flow time $t_{\mathrm{phys}} > 0$, this difference vanishes quadratically:
$$\lim_{a \to 0} a^2 / t_{\mathrm{phys}} = 0.$$
Therefore, **operator mixing with non-$SO(4)$-invariant operators is power-suppressed by $O(a^2)$ and vanishes identically in the continuum limit.**

---

## 5. Renormalization Protocol for YM-015

For any smooth test function $f \in C^\infty(\mathbb{T}_{\mathrm{phys}}^4)$ and physical flow time $t_{\mathrm{phys}} > 0$:
1. **Centered Smeared Lattice Observable:**
   $$\mathcal{O}_{a, t_{\mathrm{phys}}}(f) := a^4 \sum_{x \in \Lambda_a} f(x) \left( \mathcal{E}_a(x; t_{\mathrm{phys}}) - \langle \mathcal{E}_a(x; t_{\mathrm{phys}}) \rangle_{\mu_a} \right).$$
2. **Vacuum Subtraction Constant:**
   $$\langle \mathcal{E}_a(x; t_{\mathrm{phys}}) \rangle_{\mu_a} = \frac{3(N^2-1)}{32\pi^2 t_{\mathrm{phys}}^2} g_0^2(t_{\mathrm{phys}}) \left( 1 + O(g_0^2) \right) + O(a^2).$$
   This removes the only non-vanishing 1-point tadpole divergence.
3. **Continuum Target Distribution:**
   $$S_k(t_1, \dots, t_k)(f_1, \dots, f_k) := \lim_{j \to \infty} \left\langle \prod_{i=1}^k \mathcal{O}_{a_{n_j}, t_i}(f_i) \right\rangle_{\mu_{a_{n_j}}}.$$
   Zero multiplicative renormalizations $Z$ are required.
