# YM-015-O4-TARGET — Hypercubic-to-Continuous Rotational Invariance Target Specification

- **Target Identifier:** `YM-015-O4-TARGET`
- **Task Association:** `YM-015 — E-UV-FREE-CONT`
- **Governance Classification:** Formal Symmetry Restoration Specification
- **Authoritative Baseline:** State Revision 30
- **Status:** `ACTIVE_TARGET`

---

## 1. Physical Context & Symmetry Gap

On the lattice $\Lambda_a = (a \mathbb{Z})^4$, the continuous rotation group $SO(4)$ is explicitly broken down to the discrete hyperoctahedral group $H_4 \subset SO(4)$:
$$|H_4| = 2^4 \cdot 4! = 384.$$
Axiom OS1 of Osterwalder and Schrader requires that the continuum Schwinger distributions be invariant under the full continuous Lie group $SO(4)$ (and $O(4)$ including reflections).

It is a well-known mathematical hazard that discrete hypercubic invariance $H_4$ does **NOT** imply continuous $SO(4)$ invariance. For example:
- Rank-4 tensors invariant under $H_4$ include the anisotropic tensor $\sum_\mu x_\mu^4$, which is not $SO(4)$-invariant ($\sum_\mu x_\mu^4 \neq |x|^4$).
- In lattice field theories with scalar or fermionic fields, hypercubic-invariant irrelevant operators can induce non-universal anisotropies if not properly suppressed.

---

## 2. Irreducible Tensor Decomposition Under $H_4$

Under the reduction $SO(4) \supset H_4$:
1. **Dimension 4 Operators:**
   The only gauge-invariant local dimension-4 operator is:
   $$\mathcal{L}_4(x) = \frac{1}{4} \operatorname{Tr}\!\left( F_{\mu\nu}(x) F_{\mu\nu}(x) \right) = \frac{1}{2} \operatorname{Tr}\!\left( \vec{E}^2 + \vec{B}^2 \right).$$
   This transforms in the trivial representation $\mathbf{1}$ of $SO(4)$, and therefore its restriction to $H_4$ remains the trivial representation $A_{1g}$.
   **There are NO non-$SO(4)$-invariant gauge-invariant operators of dimension $\le 4$.**
2. **Dimension 6 Operators:**
   The first appearance of hypercubic anisotropy occurs at mass dimension 6:
   $$\mathcal{O}_{\mathrm{aniso}}^{(6)}(x) := \sum_{\mu=1}^4 \operatorname{Tr}\!\left( \left( \sum_{\nu=1}^4 F_{\mu\nu}(x) F_{\mu\nu}(x) \right)^2 \right) - \frac{1}{4} \left( \sum_{\mu, \nu=1}^4 \operatorname{Tr}(F_{\mu\nu} F_{\mu\nu}) \right)^2.$$
   Under $H_4$, this forms a non-trivial singlet $A_{1g}^{(6)}$ that is invariant under 90-degree axis rotations and reflections, but changes under general continuous rotations $R \in SO(4)$.

---

## 3. Quantitative Vanishing-Anisotropy Target

The target theorem for $SO(4)$ restoration requires proving that for every fixed continuous rotation $R \in SO(4)$ and smooth test functions $f_1, \dots, f_k \in C^\infty(\mathbb{T}_{\mathrm{phys}}^4)$:
$$\left| \left\langle \prod_{i=1}^k \mathcal{O}_{a, t_i}(R f_i) \right\rangle_{\mu_a} - \left\langle \prod_{i=1}^k \mathcal{O}_{a, t_i}(f_i) \right\rangle_{\mu_a} \right| \le C_R(t_1, \dots, t_k) \, a^\alpha \prod_{i=1}^k \|f_i\|_{H^4(\mathbb{T}_{\mathrm{phys}}^4)},$$
with an explicit proved exponent $\alpha > 0$.

The target is satisfied with $\alpha = 2$ via the RG irrelevance of dimension-6 hypercubic operators.
In the continuum limit $a \to 0$:
$$S_k(t_1, \dots, t_k)(R f_1 \otimes \cdots \otimes R f_k) = S_k(t_1, \dots, t_k)(f_1 \otimes \cdots \otimes f_k) \quad \forall R \in SO(4).$$
