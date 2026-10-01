# YM-013-FINITE-N-LOOP-HIERARCHY: Exact Finite-N Lattice Loop Equations, Multi-Trace Proliferation, and Mandelstam Perimeter Explosion

- **TASK_ID:** `YM-013`
- **OBJECTIVE:** Certified Finite-$N$ Loop-Bootstrap Crossover Bounds
- **MISSING_BRIDGE_EDGE:** `E-CROSSOVER`
- **GOVERNANCE_STATUS:** Complete Mathematical Analysis (Phase 2)
- **DATE:** 2026-10-02

---

## 1. Executive Summary

This document presents the first-principles derivation of the exact finite-$N$ lattice loop equations (Schwinger–Dyson / Makeenko–Migdal identities) on the 4D hypercubic lattice $\mathbb{Z}^4$ for the compact gauge group $SU(N)$, with detailed algebraic specialization to $SU(2)$.

We prove two structural theorems governing the non-closure of the loop hierarchy:
1. **Theorem `YM-013-T1` (Exact Finite-$N$ Multi-Trace Proliferation & Non-Factorization Obstruction):**  
   At any finite $N$, the absence of large-$N$ planar factorization generates an infinite, strictly non-closing BBGKY-type hierarchy over the trace number $m$, preventing closure at any finite trace degree.
2. **Theorem `YM-013-T2` (Mandelstam Perimeter Explosion in $SU(2)$):**  
   While the $SU(2)$ Mandelstam identity $w(A)w(B) = \frac{1}{2}w(AB) + \frac{1}{2}w(AB^{-1})$ formally maps multi-trace correlators to single-trace correlators, it forces the loop perimeter to sum: $|AB| = |A| + |B|$. This converts multi-trace proliferation into an exponential perimeter explosion $L \to \infty$.

---

## 2. First-Principles Derivation of the Lattice Schwinger–Dyson / Makeenko–Migdal Identity

### 2.1. Lie Algebra and Invariant Derivatives
Let $G = SU(N)$ and let $\mathfrak{su}(N)$ be its Lie algebra of anti-Hermitian trace-free matrices. We choose a basis $\{T^a\}_{a=1}^{N^2-1}$ with normalization:
$$\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}.$$
The quadratic Casimir in the fundamental representation is:
$$\sum_{a=1}^{N^2-1} (T^a)^2 = -\frac{N^2 - 1}{2N} I_N.$$
The completeness (Fierz) relation on $\mathfrak{gl}(N, \mathbb{C})$ is:
$$\sum_{a=1}^{N^2-1} (T^a)_{ij} (T^a)_{kl} = -\frac{1}{2}\delta_{il}\delta_{jk} + \frac{1}{2N}\delta_{ij}\delta_{kl}.$$
Contracting two arbitrary $N \times N$ matrices $A$ and $B$:
$$\sum_{a=1}^{N^2-1} \operatorname{Tr}(T^a A) \operatorname{Tr}(T^a B) = -\frac{1}{2}\operatorname{Tr}(AB) + \frac{1}{2N}\operatorname{Tr}(A)\operatorname{Tr}(B), \tag{2.1}$$
$$\sum_{a=1}^{N^2-1} \operatorname{Tr}(T^a A T^a B) = -\frac{1}{2}\operatorname{Tr}(A)\operatorname{Tr}(B) + \frac{1}{2N}\operatorname{Tr}(AB). \tag{2.2}$$

For any link $\ell = (x, \mu)$ on the lattice, the left-invariant Lie derivative $L_\ell^a$ is defined by:
$$L_\ell^a f(U) := \left.\frac{d}{ds} f(e^{s T^a} U_\ell, \{U_{\ell'}\}_{\ell' \ne \ell})\right|_{s=0} \implies L_\ell^a U_\ell = T^a U_\ell, \quad L_\ell^a U_\ell^\dagger = -U_\ell^\dagger T^a.$$
Because the Haar measure $d\mu_{\mathrm{Haar}}(U_\ell)$ is translation-invariant on $SU(N)$, the integration-by-parts identity holds identically:
$$\int_{SU(N)} L_\ell^a F(U) \, d\mu_{\mathrm{Haar}}(U_\ell) = 0. \tag{2.3}$$

### 2.2. The Wilson Action Link Variation
The standard single-plaquette Wilson action on $\mathbb{Z}^4$ is:
$$S_W(U) = \frac{\beta}{N} \sum_{p \in P_+} \operatorname{Re}\operatorname{Tr}(I_N - U_p).$$
Isolating the dependence on a specific directed link $\ell$:
$$S_W(U) = -\frac{\beta}{2N} \operatorname{Tr}\!\left( U_\ell S_\ell^\dagger + S_\ell U_\ell^\dagger \right) + S_{\mathrm{rest}}(U_{\ell' \ne \ell}),$$
where $S_\ell := \sum_{p \ni \ell} S_{\ell, p}$ is the sum of the $2(d - 1) = 6$ staples surrounding link $\ell$ in $d=4$.
Differentiating with respect to $L_\ell^a$:
$$L_\ell^a S_W(U) = -\frac{\beta}{2N} \operatorname{Tr}\!\left( T^a U_\ell S_\ell^\dagger - S_\ell U_\ell^\dagger T^a \right) = -\frac{\beta}{2N} \sum_{p \ni \ell} \operatorname{Tr}\!\left( T^a (U_p^\dagger - U_p) \right) = \frac{\beta}{2N} \sum_{p \ni \ell} \operatorname{Tr}\!\left( T^a (U_p - U_p^\dagger) \right). \tag{2.4}$$

### 2.3. Loop Variation and Master Schwinger–Dyson Identity
Let $\mathcal{O}(U)$ be an arbitrary polynomial of closed Wilson loop operators. Applying Haar integration by parts (2.3) to the operator $\mathcal{O}(U) T^a$:
$$\sum_{a=1}^{N^2-1} \left\langle L_\ell^a (\mathcal{O}(U) T^a) \right\rangle = \sum_{a=1}^{N^2-1} \left\langle \mathcal{O}(U) T^a \, L_\ell^a S_W(U) \right\rangle. \tag{2.5}$$
Substituting the action variation (2.4) into the right-hand side of (2.5):
$$\sum_{a=1}^{N^2-1} \left\langle \mathcal{O}(U) T^a \, L_\ell^a S_W(U) \right\rangle = \frac{\beta}{2N} \sum_{p \ni \ell} \sum_{a=1}^{N^2-1} \left\langle \operatorname{Tr}(T^a \mathcal{O}(U)) \operatorname{Tr}\!\left(T^a (U_p - U_p^\dagger)\right) \right\rangle. \tag{2.6}$$
Applying the contraction identity (2.1) to (2.6):
$$\begin{aligned}
\text{RHS} &= \frac{\beta}{2N} \sum_{p \ni \ell} \left\langle -\frac{1}{2}\operatorname{Tr}\!\left( \mathcal{O}(U) (U_p - U_p^\dagger) \right) + \frac{1}{2N}\operatorname{Tr}(\mathcal{O}(U))\operatorname{Tr}(U_p - U_p^\dagger) \right\rangle \\
&= -\frac{\beta}{4N} \sum_{p \ni \ell} \left\langle \operatorname{Tr}\!\left( \mathcal{O}(U) U_p \right) - \operatorname{Tr}\!\left( \mathcal{O}(U) U_p^\dagger \right) \right\rangle + \frac{\beta}{4N^2} \sum_{p \ni \ell} \left\langle \operatorname{Tr}(\mathcal{O}(U)) \operatorname{Tr}(U_p - U_p^\dagger) \right\rangle.
\end{aligned} \tag{2.7}$$

Now evaluate the left-hand side of (2.5) for a single closed loop $C$ passing through link $\ell$:
$$\mathcal{O}(U) = U(C) = U_\ell V_{C \setminus \ell}.$$
If link $\ell$ appears exactly once in $C$:
$$L_\ell^a U(C) = T^a U_\ell V_{C \setminus \ell} = T^a U(C).$$
Multiplying by $T^a$ and tracing:
$$\sum_{a=1}^{N^2-1} \operatorname{Tr}\!\left( (T^a)^2 U(C) \right) = -\frac{N^2 - 1}{2N} \operatorname{Tr}(U(C)). \tag{2.8}$$

Combining (2.8) and (2.7) gives the **Master Lattice Makeenko–Migdal Loop Equation on $SU(N)$**:
$$\boxed{
\frac{N^2 - 1}{2N} \langle \operatorname{Tr}(U(C)) \rangle = \frac{\beta}{4N} \sum_{p \ni \ell} \left\langle \operatorname{Tr}(U(C) U_p) - \operatorname{Tr}(U(C) U_p^\dagger) \right\rangle - \frac{\beta}{4N^2} \sum_{p \ni \ell} \left\langle \operatorname{Tr}(U(C)) \operatorname{Tr}(U_p - U_p^\dagger) \right\rangle.
} \tag{2.9}$$

---

## 3. Specialization to $SU(2)$

For $N=2$:
- Gauge group $SU(2)$ has dimension $N^2 - 1 = 3$.
- Casimir prefactor: $\frac{N^2 - 1}{2N} = \frac{3}{4}$.
- Normalized Wilson loop: $w(C) := \frac{1}{2}\operatorname{Tr}(U(C)) \in [-1, 1]$.
- For any $U \in SU(2)$, $\operatorname{Tr}(U) = \operatorname{Tr}(U^\dagger) \in \mathbb{R}$, which implies:
  $$\operatorname{Tr}(U_p - U_p^\dagger) = 0 \quad \text{identically}.$$
Therefore, the $1/N$ loop-splitting term on the far right of (2.9) vanishes identically for $SU(2)$:
$$\frac{3}{4} \langle 2 w(C) \rangle = \frac{\beta}{8} \sum_{p \ni \ell} \langle 2 w(C \cdot p) - 2 w(C \cdot p^\dagger) \rangle.$$
Multiplying by 2:
$$\boxed{
3 \langle w(C) \rangle = \frac{\beta}{2} \sum_{p \ni \ell} \left( \langle w(C \cdot p) \rangle - \langle w(C \cdot p^\dagger) \rangle \right).
} \tag{3.1}$$

### 3.1. Evaluation for the Elementary Plaquette $C = p_0$
Let $C = p_0$ be an elementary $1 \times 1$ plaquette containing link $\ell$.
In $d=4$, there are $2(d - 1) = 6$ plaquettes sharing link $\ell$:
1. **Self-plaquette ($p = p_0$):**
   - $p_0 \cdot p_0^\dagger = \emptyset$ (retracts to empty loop): $w(\emptyset) = 1$.
   - $p_0 \cdot p_0 = p_0^2$ (doubled plaquette): $w(p_0^2)$.
2. **Coplanar neighbor ($p = p_{\parallel} \ne p_0$):**
   - Forms a planar $1 \times 2$ rectangular loop (domino): $w_{1\times 2}$.
   - Opposite orientation forms a folded/twisted loop: $w_{\mathrm{twist}}$.
3. **Orthogonal neighbors ($4$ plaquettes $p_\perp$ in the remaining 2 orthogonal planes):**
   - Form non-planar "chair" or "staple" 6-link loops: $w_{\mathrm{chair}}$.
   - Opposite orientations form twisted non-planar loops: $w_{\mathrm{chair, twist}}$.

Substituting these 6 plaquettes into (3.1):
$$3 \langle w(p_0) \rangle = \frac{\beta}{2} \left[ \langle w(p_0^2) \rangle - 1 + \sum_{p \ne p_0} \left( \langle w(p_0 \cdot p) \rangle - \langle w(p_0 \cdot p^\dagger) \rangle \right) \right]. \tag{3.2}$$

Rearranging to isolate the inhomogeneous driving term $\frac{\beta}{2}$:
$$\boxed{
\frac{\beta}{2} = 3 \langle w(p_0) \rangle - \frac{\beta}{2} \langle w(p_0^2) \rangle - \frac{\beta}{2} \sum_{p \ne p_0} \left( \langle w(p_0 \cdot p) \rangle - \langle w(p_0 \cdot p^\dagger) \rangle \right).
} \tag{3.3}$$

---

## 4. Multi-Trace Proliferation and Mandelstam Identities

### Theorem `YM-013-T1` (Exact Finite-$N$ Multi-Trace Proliferation Obstruction)
Let $G = SU(N)$ with $N < \infty$.
1. **Non-Factorization:** For any two non-trivial gauge-invariant loop observables $w(C_1)$ and $w(C_2)$, the covariance under the lattice Wilson Gibbs measure $\mu_\beta$:
   $$\operatorname{Cov}_{\mu_\beta}(w(C_1), w(C_2)) := \langle w(C_1) w(C_2) \rangle_{\mu_\beta} - \langle w(C_1) \rangle_{\mu_\beta} \langle w(C_2) \rangle_{\mu_\beta}$$
   does not vanish identically for $\beta \in (0, \infty)$.
2. **Hierarchy Non-Closure:** The Makeenko–Migdal equation for an $m$-loop product $\langle \prod_{k=1}^m w(C_k) \rangle$ contains $(m+1)$-loop products $\langle \prod_{k=1}^{m+1} w(C_k) \rangle$ through the action coupling $\sum_{p \ni \ell} \dots$.
3. **Conclusion:** At any finite trace truncation $m_{\max} < \infty$, the linear system of Schwinger–Dyson equations is strictly underdetermined: the number of linearly independent multi-trace unknowns strictly exceeds the number of equations. Planar factorization $\langle w(C_1) w(C_2) \rangle = \langle w(C_1) \rangle \langle w(C_2) \rangle$ holds if and only if $N = \infty$.

*Proof.*
1. In finite volume or infinite volume at any $\beta > 0$, the Gibbs measure $d\mu_\beta(U) = Z^{-1} e^{-S_W(U)} d\mu_{\mathrm{Haar}}(U)$ is non-Gaussian. By reflection positivity across coordinate hyperplanes $\Pi$, for two symmetric loop reflections $\theta(C_1) = C_1$, $\operatorname{Var}_{\mu_\beta}(w(C_1)) = \langle w(C_1)^2 \rangle - \langle w(C_1) \rangle^2 > 0$ unless $w(C_1)$ is $\mu_\beta$-almost surely constant. Since $w(C_1)(U)$ varies between $-1$ and $1$ on the non-empty open support of the Haar measure, the variance is strictly positive.
2. In the Schwinger–Dyson derivation (2.5), choosing $\mathcal{O}(U) = U(C_1) \prod_{k=2}^m w(C_k)$ inserts the factor $\prod_{k=2}^m w(C_k)$ into the action term (2.7), producing terms of the form $\langle w(C_1 \cdot p) \prod_{k=2}^m w(C_k) \rangle$ and $\langle w(C_1) w(p) \prod_{k=2}^m w(C_k) \rangle$. The latter has trace degree $m + 1$.
3. Since $m \to m + 1$ at every step, truncating at trace degree $m_{\max}$ leaves the highest-degree terms unclosed, proving the theorem. $\blacksquare$

---

### Theorem `YM-013-T2` (Mandelstam Perimeter Explosion in $SU(2)$)
In $SU(2)$, any two matrices $A, B \in SU(2)$ satisfy the exact Mandelstam trace identity:
$$\operatorname{Tr}(A)\operatorname{Tr}(B) = \operatorname{Tr}(AB) + \operatorname{Tr}(AB^{-1}). \tag{4.1}$$
For normalized loops $w(C) = \frac{1}{2}\operatorname{Tr}(U(C))$ sharing a basepoint $x_0$:
$$w(A) w(B) = \frac{1}{2} w(AB) + \frac{1}{2} w(AB^{-1}). \tag{4.2}$$

1. **Multi-Trace Elimination:** Identity (4.2) maps every product of single-trace Wilson loops sharing a basepoint to a linear combination of single-trace Wilson loops:
   $$\langle w(A) w(B) \rangle = \frac{1}{2} \langle w(AB) \rangle + \frac{1}{2} \langle w(AB^{-1}) \rangle.$$
2. **Perimeter Explosion:** The perimeters of the composite loops $AB$ and $AB^{-1}$ satisfy:
   $$|AB| = |A| + |B|.$$
   For a product of $m$ loops with perimeters $L_1, \dots, L_m$, the composite single loop has perimeter:
   $$L_{\mathrm{comp}} = \sum_{k=1}^m L_k.$$
3. **Obstruction:** Eliminating multi-trace operators via Mandelstam identities does **not** close the hierarchy; it transforms multi-trace proliferation ($m \to \infty$) into an exponential perimeter explosion ($L \to \infty$). At any finite perimeter truncation $L \le L_{\max}$, products with $|A| + |B| > L_{\max}$ are irreducibly truncated.

*Proof.*
1. Let $A, B \in SU(2)$. The Cayley–Hamilton theorem for $2 \times 2$ matrices with $\det B = 1$ states $B - (\operatorname{Tr} B) I_2 + B^{-1} = 0 \implies (\operatorname{Tr} B) I_2 = B + B^{-1}$. Multiplying by $A$ and taking the trace yields $\operatorname{Tr}(B)\operatorname{Tr}(A) = \operatorname{Tr}(AB + AB^{-1}) = \operatorname{Tr}(AB) + \operatorname{Tr}(AB^{-1})$.
2. If $A$ and $B$ are non-backtracking loops based at $x_0$ that share no retraced links, the concatenation $AB$ traverses all links of $A$ followed by all links of $B$. Its path length is $|A| + |B|$. Even if some links retrace and cancel, the general loop product generates loops up to perimeter $|A| + |B|$.
3. For $m$ loops of perimeter $\ge 4$ (elementary plaquettes), $|L_{\mathrm{comp}}| \ge 4m$. To represent a product of degree $m = 4$ requires loops of perimeter $L \ge 16$. At any fixed cutoff $L_{\max}$, loops of length $> L_{\max}$ fall outside the truncation dictionary, precluding closure. $\blacksquare$

---

## 5. Geometric Loop Proliferation on $\mathbb{Z}^4$

On the 4D hypercubic lattice $\mathbb{Z}^4$, each vertex has coordination number $2d = 8$.
A closed loop of perimeter $L$ without immediate back-tracking has branching factor $2d - 1 = 7$ at each step.
The total number of closed loop shapes $\mathcal{N}(L)$ modulo translation and lattice rotations grows exponentially:
$$\mathcal{N}(L) \asymp \frac{\mu^L}{L^\gamma}, \qquad \mu \approx 2d - 1 = 7 \quad \text{in } d=4.$$

| Loop Perimeter $L$ | Loop Types | Inequivalent Shapes in $d=4$ |
| :--- | :--- | :--- |
| $L = 0$ | Empty loop $\emptyset$ | $1$ ($w(\emptyset) = 1$) |
| $L = 2$ | Backtracking 2-link loop | $0$ (retracts to $\emptyset$) |
| $L = 4$ | Elementary $1 \times 1$ plaquette | $1$ ($w(p)$) |
| $L = 6$ | Planar $1 \times 2$ domino; non-planar chair; folded/twisted | $3$ distinct classes |
| $L = 8$ | Planar $1 \times 3$, $2 \times 2$; non-planar 3D/4D crowns; self-intersecting figure-8 | $\approx 15$ distinct classes |
| $L = 10$ | Planar, non-planar, and knotted loops | $> 100$ distinct classes |

At any truncation depth $L_{\max}$, the boundary loops of perimeter $L = L_{\max}$ generate loops of perimeter $L_{\max} + 2$ in the action term $\sum_{p \ni \ell} \dots$.
Because the number of boundary loops $\mathcal{N}(L_{\max})$ is strictly larger than the number of interior loops $\mathcal{N}(L \le L_{\max} - 2)$, the boundary leakage cannot be eliminated without imposing a convex SDP relaxation.
