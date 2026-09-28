# YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB — Periodic-Torus Uniform Plaquette Bound, Toron Quartic Commutator Variety, Brascamp–Lieb Applicability Audit, and Stratified Laplace Resolution of Fixed-Volume $O_L(1/\beta)$

**Task ID:** `YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB`  
**Date:** 2026-09-28  
**Baseline Commit SHA:** `9aec40b170415ba94fee65cb8d27df76ecd4aeaf`  
**Canonical Universal Baseline:** `UNIVERSAL_GOVERNANCE_MINIMAL_v4.0.4`  
**Project-Specific Strengthening:** `UNIVERSAL_GOVERNANCE_MINIMAL_v4.0.6-r3_ADOPTED_CONTROLS`  
**Global Invariants:** `GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`

---

## 1. Executive Summary and Implication Hierarchy (`P1`, `P2`, `P3`)

This document investigates whether the periodic Wilson lattice gauge Gibbs measure $\mu_{\mathrm{per}, \beta}$ on $\Lambda_{\mathrm{per}}(L, d) = (\mathbb{Z}/L\mathbb{Z})^d$ ($d \in \{2, 3, 4\}$, $SU(N)$ with $N \ge 2$) satisfies a weak-coupling plaquette-energy bound of the form $e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{per}}) \le C/\beta$, strictly separating the three-level hierarchy:

$$P3 \ (\text{Continuum-Useful Uniform Control}) \implies P2 \ (\text{Volume-Uniform Periodic } O(1/\beta)) \implies P1 \ (\text{Fixed-}L \text{ Periodic } O_L(1/\beta)).$$

### Central Mathematical Finding
We answer the core question of `YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB` rigorously:
> **Do toron flat moduli and central-toron quartic commutator degeneracies merely invalidate ordinary Gaussian Laplace analysis, or do they actually obstruct an $O(1/\beta)$ periodic plaquette-energy bound?**
>
> **Answer:**
> 1. **At fixed finite volume $L$ (`P1: FIXED_VOLUME_PERIODIC_O_1_OVER_BETA = PROVED`):**
>    Toron flat moduli and central-toron quartic commutator degeneracies **merely invalidate naive Gaussian / Morse–Bott Hessian inversion — they do NOT obstruct the $O_L(1/\beta)$ plaquette-energy bound.**
>    - Each quadratic mode contributes $\frac{1}{2\beta}$ to $-\partial_\beta \ln Z_{\mathrm{per}}(\beta)$;
>    - Each quartic commutator mode ($\int e^{-\beta y^4} dy \propto \beta^{-1/4}$) contributes $\frac{1}{4\beta} < \frac{1}{2\beta}$ to $-\partial_\beta \ln Z_{\mathrm{per}}(\beta)$;
>    - Each flat toron or conjugation mode ($\beta^0$) contributes $0 < \frac{1}{2\beta}$ to $-\partial_\beta \ln Z_{\mathrm{per}}(\beta)$;
>    - Any resonant logarithmic factor $(\ln \beta)^{k_L}$ in $Z_{\mathrm{per}}(\beta)$ contributes $-\frac{k_L}{\beta \ln \beta} = o_L(1/\beta)$ to $-\partial_\beta \ln Z_{\mathrm{per}}(\beta)$, **never** $\frac{\ln \beta}{\beta}$.
>    Thus, toron flat and quartic zero modes **strictly reduce** the weak-coupling equipartition coefficient $C_{\mathrm{per}}(L, d, N) = \frac{\alpha_L(d, N)}{|P_+|} < \frac{N^2 - 1}{d}$ relative to naive Gaussian equipartition!
>    Furthermore, via the **Exact Dyadic Partition-Ratio Inequality (`YM-011-TORON-T1`)**,
>    $$e_{\mathrm{plaq}}(\beta, \Lambda) \le \frac{2}{|P_+|\,\beta} \ln \frac{Z_\Lambda(\beta/2)}{Z_\Lambda(\beta)} \qquad \forall \beta > 0,$$
>    both $\beta^{-\alpha_L}$ and $(\ln \beta)^{k_L}$ cancel identically in the dyadic ratio $Z_{\mathrm{per}}(\beta/2)/Z_{\mathrm{per}}(\beta) \to 2^{\alpha_L}$, establishing `P1` (`PROVED`).
> 2. **At uniform infinite volume (`P2: VOLUME_UNIFORM_PERIODIC_O_1_OVER_BETA = OPEN`, `P3: CONTINUUM_UNIFORM_CONTROL = OPEN`):**
>    Although the asymptotic slope $\lim_{\beta \to \infty} \beta\, e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{per}}(L, d)) = \frac{\alpha_L(d, N)}{|P_+|} \le \frac{N^2 - 1}{d}$ is **uniformly bounded in $L$**, proving that the non-asymptotic dyadic ratio $\frac{1}{|P_+|} \ln \frac{Z_{\mathrm{per}}(\beta/2)}{Z_{\mathrm{per}}(\beta)}$ is bounded by $C(N, d)$ uniformly in $L$ at a fixed $\beta$ remains **`OPEN`** (`UNRESOLVED_DEPENDENCY: YM-011-DYADIC-FREE-ENERGY-UNIFORMITY`), because global Brascamp–Lieb is `NOT_APPLICABLE`, the single-plaquette Schwinger–Dyson hierarchy does not self-close (`PARTIAL`), and the $O(L^{-2})$ infrared curl-curl Laplacian modes and non-Abelian 3-cube Bianchi syzygies (`NEG-YM-011-TREE-1`) couple the finite-$\beta$ remainder across the lattice.

---

## 2. Toron Stratification and Local Action Expansion Across Regular, Levi-Singular, and Central Strata

In maximal spanning-tree gauge $\Sigma_{T_{\mathrm{per}}} \cong SU(N)^{|E_{\mathrm{co-tree}}|}$ (`YM-011-TREE-T4`), the flat-connection zero locus $\mathcal{Z}(H|_{\Sigma_{T_{\mathrm{per}}}})$ sets all interior co-tree links to $I_N$ and all $L^{d-1}$ boundary-wrapping links in axis direction $\mu \in \{1, \dots, d\}$ to a common matrix $U_\mu \in SU(N)$ satisfying $[U_\mu, U_\nu] = I_N$, yielding the commuting variety $\mathcal{C}_d(SU(N)) \subset SU(N)^d$ and flat moduli space:
$$\mathcal{M}_{\mathrm{flat}}(\Lambda_{\mathrm{per}}, SU(N)) = \mathrm{Hom}(\mathbb{Z}^d, SU(N)) / \operatorname{Ad}(SU(N)) \cong (T_{\max})^d / S_N.$$

For any toron $U = (U_1, \dots, U_d) \in \mathcal{C}_d(SU(N))$, up to simultaneous $\operatorname{Ad}(SU(N))$ conjugation, $U_\mu \in T_{\max}$ are diagonal matrices whose common centralizer in $SU(N)$ is a Levi subgroup:
$$\operatorname{Stab}_{\operatorname{Ad}(SU(N))}(U) = L_{(n_1, \dots, n_k)} := S\big(U(n_1) \times \cdots \times U(n_k)\big), \qquad \sum_{r=1}^k n_r = N, \qquad S := \sum_{r=1}^k n_r^2 \in [N, N^2],$$
with stabilizer dimension $\dim \operatorname{Stab}(U) = S - 1$. The tangent space $T_U \Sigma_{T_{\mathrm{per}}} \cong \mathfrak{su}(N)^{|E_{\mathrm{co-tree}}|}$ of total dimension $(N^2 - 1)((d - 1)L^d + 1)$ decomposes orthogonally into:
1. **Non-harmonic co-tree quadratic modes:** $n_{\mathrm{non-harm}} = (N^2 - 1)(|E_{\mathrm{co-tree}}| - d) = (N^2 - 1)((d - 1)L^d + 1 - d)$ modes, which are **strictly quadratic** at every toron stratum with smallest positive eigenvalue $\lambda_{\min}^{\perp}(L, d) \asymp L^{-2} > 0$.
2. **Harmonic toron modes in $\mathfrak{su}(N)^d$ (dimension $d(N^2 - 1)$):**
   For a Levi stratum $L_{(n_1, \dots, n_k)}$ with $S = \sum_{r=1}^k n_r^2$, $\mathfrak{su}(N)^d$ splits into four exact orthogonal subspaces:
   - **Cartan / Levi-center flat directions ($\beta^0$):** $d(k - 1)$ directions in $\mathfrak{z}_L^d$ (for regular torons $k = N$, giving $d(N - 1)$ Cartan flat directions; for central torons $k = 1$, giving $0$);
   - **Global conjugation zero modes ($\beta^0$):** $N^2 - S$ directions tangent to the flag orbit $SU(N) / L_{(n_1, \dots, n_k)}$ (for regular torons $S = N$, giving $N(N - 1)$; for central torons $S = N^2$, giving $0$);
   - **Off-block transverse positive quadratic modes ($\beta^{-1/2}$):** $(d - 1)(N^2 - S)$ directions in the off-block root spaces $\Phi \setminus \Phi_L$, where $\sum_{\mu=1}^d |e^{i\alpha(H_\mu)} - 1|^2 = \delta_\alpha(U)^2 > 0$ provides a strictly positive quadratic restoring force;
   - **In-block quartic commutator modes ($\beta^{-1/4}$):** $d(S - k) = d\sum_{r=1}^k (n_r^2 - 1)$ directions in $\bigoplus_{r=1}^k \mathfrak{su}(n_r)^d$, where all $U_\mu$ act as scalars $z_{\mu, r} I_{n_r}$ on block $r$, so the quadratic Hessian vanishes identically and the leading action is the **quartic commutator functional**:
     $$H_4(X_1, \dots, X_d) = \frac{1}{2N} \sum_{1 \le \mu < \nu \le d} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2.$$

Notice the exact dimension conservation identity across every Levi stratum $(n_1, \dots, n_k) \vdash N$:
$$\underbrace{d(k - 1)}_{\text{Levi center flat}} + \underbrace{(N^2 - S)}_{\text{global conjugation}} + \underbrace{(d - 1)(N^2 - S)}_{\text{off-block quadratic}} + \underbrace{d(S - k)}_{\text{in-block quartic}} = d(k - 1) + d(N^2 - S) + d(S - k) = d(N^2 - 1).$$

---

## 3. Complete Characterization of the Quartic Commutator Model $Q(X_1, \dots, X_d)$

### Theorem `YM-011-TORON-Q1` (Zero Set, Dimension, and Transverse Coercivity of $Q$)
Let $Q : \mathfrak{su}(N)^d \to [0, \infty)$ be defined by $Q(X_1, \dots, X_d) = \sum_{1 \le \mu < \nu \le d} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2$.
1. **Exact Zero Set:** Since $\|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2 \ge 0$ for every pair $(\mu, \nu)$,
   $$\mathcal{Z}(Q) := \{X \in \mathfrak{su}(N)^d : Q(X) = 0\} = \mathfrak{C}_d(\mathfrak{su}(N)) := \{(X_1, \dots, X_d) \in \mathfrak{su}(N)^d : [X_\mu, X_\nu] = 0 \;\forall \mu < \nu\}.$$
   In particular, the global inequality $Q(X) \ge c \|X\|_{\mathrm{HS}}^4$ is **strictly false** on $\mathfrak{su}(N)^d$, because $Q(H_1, \dots, H_d) = 0$ for all non-zero Cartan tuples $(H_1, \dots, H_d) \in \mathfrak{t}_{\max}^d \setminus \{0\}$.
2. **Simultaneous Diagonalization and Quotient Dimension:** Every commuting tuple $(X_1, \dots, X_d) \in \mathfrak{C}_d(\mathfrak{su}(N))$ of skew-Hermitian matrices is simultaneously unitarily diagonalizable by $g \in SU(N)$ into $\mathfrak{t}_{\max}^d$. Hence the adjoint sweep map $\Psi : (SU(N)/T_{\max}) \times \mathfrak{t}_{\max}^d \to \mathfrak{C}_d(\mathfrak{su}(N))$ is surjective and a $W$-fold covering ($W = S_N$) over the open dense regular stratum $\mathfrak{C}_d^{\mathrm{reg}}(\mathfrak{su}(N))$. Therefore:
   $$\dim_{\mathbb{R}} \mathfrak{C}_d(\mathfrak{su}(N)) = \dim(SU(N)/T_{\max}) + d \dim \mathfrak{t}_{\max} = N(N - 1) + d(N - 1) = (d + N)(N - 1),$$
   $$\mathfrak{C}_d(\mathfrak{su}(N)) / \operatorname{Ad}(SU(N)) \cong \mathfrak{t}_{\max}^d / S_N, \qquad \dim_{\mathbb{R}}\!\left(\mathfrak{C}_d(\mathfrak{su}(N)) / \operatorname{Ad}(SU(N))\right) = d(N - 1),$$
   and the transverse codimension of $\mathfrak{C}_d(\mathfrak{su}(N))$ in $\mathfrak{su}(N)^d$ is:
   $$\operatorname{codim}_{\mathfrak{su}(N)^d} \mathfrak{C}_d(\mathfrak{su}(N)) = d(N^2 - 1) - (d + N)(N - 1) = (d - 1)N(N - 1).$$
3. **Transverse Lower Bound Near Regular Stratum vs. Central Origin:**
   For any regular commuting tuple $H = (H_1, \dots, H_d) \in \mathfrak{t}_{\max}^d \cap \mathfrak{C}_d^{\mathrm{reg}}(\mathfrak{su}(N))$ and any normal perturbation $Y^\perp \in N_H \mathfrak{C}_d(\mathfrak{su}(N)) \cong \mathbb{R}^{(d-1)N(N-1)}$ orthogonal to the flag tangent space $\{( [Z, H_1], \dots, [Z, H_d] ) : Z \in \mathfrak{t}_{\max}^\perp\}$, we have $\sum_{\mu=1}^d \alpha(H_\mu) Y_{\mu,\alpha}^\perp = 0$ for each root $\alpha \in \Phi_+$, so:
   $$\sum_{1 \le \mu < \nu \le d} \|[H_\mu, Y_\nu^\perp] - [H_\nu, Y_\mu^\perp]\|_{\mathrm{HS}}^2 = \sum_{\alpha \in \Phi_+} \left(\sum_{\mu=1}^d \alpha(H_\mu)^2\right) \sum_{\nu=1}^d |Y_{\nu,\alpha}^\perp|^2 \ge \delta_{\mathrm{sing}}(H)^2 \|Y^\perp\|_{\mathrm{HS}}^2,$$
   where $\delta_{\mathrm{sing}}(H) := \min_{\alpha \in \Phi_+} \left(\sum_{\mu=1}^d \alpha(H_\mu)^2\right)^{1/2} > 0$ is the distance to the singular Levi hyperplanes. Thus $Q(H + Y^\perp)$ is quadratically coercive normal to $\mathfrak{C}_d^{\mathrm{reg}}$ with constant degenerating as $\delta_{\mathrm{sing}}(H)^2 \to 0$ toward singular strata, and purely quartic ($Q(\lambda Y^\perp) = \lambda^4 Q(Y^\perp)$) at $H = 0$.

---

## 4. Audit of Brascamp–Lieb Applicability and Small-Field Localization (Sections 4 & 5)

We audit all 11 required hypothesis fields for the Brascamp–Lieb inequality ($\operatorname{Var}_\mu(f) \le \langle \nabla f, (\operatorname{Hess} V)^{-1} \nabla f \rangle_\mu$, Brascamp–Lieb 1976; Helffer–Sjöstrand 1994; Bakry–Émery 1985):

| Brascamp–Lieb Audit Field | Periodic Lattice Yang–Mills Evaluation on $\Lambda_{\mathrm{per}}(L, d)$ |
| :--- | :--- |
| **1. Measure** | $d\mu_{\mathrm{per}, \beta}(U) = Z_{\mathrm{per}}(\beta)^{-1} e^{-\beta H(U)} \prod_{e \in E_+} d\mu_{\mathrm{Haar}}(U_e)$ |
| **2. Coordinate Chart** | Maximal-tree co-tree exponential chart $\widetilde{U}_e = \exp(A_e)$, $A_e \in \mathfrak{su}(N)$ |
| **3. Potential $V$** | $V(A) = \beta \sum_{p \in P_+} \left(1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p(A))\right) - \sum_{e \in E_{\mathrm{co-tree}}} \ln J_{\mathrm{Haar}}(A_e)$ |
| **4. Domain** | Compact non-Euclidean manifold $\Sigma_{T_{\mathrm{per}}} = SU(N)^{(d-1)L^d + 1}$ |
| **5. Hessian of $V$** | $\beta D^2 H(A) - D^2 \ln J_{\mathrm{Haar}}(A)$; non-positive outside small-field region and degenerate along $\mathcal{M}_{\mathrm{flat}}$ |
| **6. Convexity Region** | Strictly restricted to small-field tubular slice $\mathcal{G}_\epsilon \cap N_\perp(\mathcal{C}_d^{\mathrm{reg}})$ away from singular torons |
| **7. Lower Hessian Bound** | $\lambda_{\min}(\operatorname{Hess}_\perp H(T)) \asymp \min(\delta_{\mathrm{sing}}(T)^2, 4\sin^2(\pi/L)) \to 0$ as $T \to \mathcal{C}_d^{\mathrm{sing}}$ and as $L \to \infty$ |
| **8. Boundary Conditions** | Periodic torus $\Lambda_{\mathrm{per}}(L, d) = (\mathbb{Z}/L\mathbb{Z})^d$ with $b_1(\mathbb{T}^d) = d > 0$ |
| **9. Zero Modes Removed** | Tree gauge removes $(L^d - 1)(N^2 - 1)$ vertex modes; retains $(d+N)(N-1)$ regular toron and $d(N^2 - 1)$ central toron zero modes |
| **10. Constants** | $\sup_{U} \|(\operatorname{Hess} V)^{-1}\|_{\mathrm{op}} = +\infty$ globally and on $\mathcal{M}_{\mathrm{flat}}$ |
| **11. Volume Dependence** | Transverse Poincaré / curl-curl eigenvalue decays as $O(L^{-2}) \to 0$ in $d \ge 3$ |

- **`GLOBAL_BRASCAMP_LIEB: NOT_APPLICABLE`.** Global uniform convexity fails both macroscopically (compactness of $SU(N)$ where $\cos\theta$ becomes concave for $|\theta| > \pi/2$) and microscopically at $H = 0$ (vanishing Hessian on the $(d+N)(N-1)$-dimensional commuting variety $\mathcal{C}_d(SU(N))$ and jumping nullity at central torons).
- **`LOCAL_BRASCAMP_LIEB: CONDITIONAL`.** Splitting $\langle h_p \rangle_{\mu_{\mathrm{per},\beta}} = \langle h_p \mathbf{1}_{\mathcal{G}_\epsilon} \rangle + \langle h_p \mathbf{1}_{\mathcal{G}_\epsilon^c} \rangle$ on $\mathcal{G}_\epsilon = \{\max_p \|U_p - I_N\|_{\mathrm{op}} \le \epsilon\}$ still confronts two independent obstacles: (i) within $\mathcal{G}_\epsilon$, $\delta_{\mathrm{sing}}(T)^2 \to 0$ as $T \to \mathcal{C}_d^{\mathrm{cent}}$ and $\lambda_{\min}^{\perp}(L) = O(L^{-2}) \to 0$; and (ii) bounding $\langle h_p \mathbf{1}_{\mathcal{G}_\epsilon^c} \rangle \le h_{\max}(N) \mu_{\mathrm{per},\beta}(\mathcal{G}_\epsilon^c)$ uniformly in $L$ requires a volume-uniform Peierls / large-field polymer tail bound $\mu_{\mathrm{per},\beta}(\mathcal{G}_\epsilon^c) \le C e^{-c\beta}$ (`Conditional`).

---

## 5. Exact Finite-Lattice Schwinger–Dyson / Makeenko–Migdal Identity and Non-Closure (Sections 6 & 7)

### Theorem `YM-011-TORON-SD1` (Exact Link Schwinger–Dyson Identity on $SU(N)$)
Let $\{T^a\}_{a=1}^{N^2 - 1}$ be an anti-Hermitian basis of $\mathfrak{su}(N)$ with $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$ and quadratic Casimir $\sum_{a=1}^{N^2 - 1} (T^a)^2 = -\frac{N^2 - 1}{2N} I_N$. Fix a link $\ell \in E_+(\Lambda)$ and a plaquette $p_0 \ni \ell$, and set $F_{\ell, p_0}^a(U) := \frac{1}{2N}\operatorname{Tr}\!\left(T^a (U_{p_0} - U_{p_0}^\dagger)\right)$. Then Haar integration by parts $\int_\Omega \sum_{a=1}^{N^2 - 1} \partial_\ell^a \big(F_{\ell, p_0}^a(U) e^{-\beta H(U)}\big) d\mu_{\mathrm{Haar}}(U) = 0$ yields the exact finite-lattice identity:
$$\frac{N^2 - 1}{2N} \left\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_{p_0}) \right\rangle_{\mu_\beta} = \frac{\beta}{4N^2} \Big\langle \underbrace{\operatorname{Tr}\!\left(I_N - \frac{U_{p_0}^2 + (U_{p_0}^\dagger)^2}{2}\right) - \frac{2}{N}(\operatorname{Im}\operatorname{Tr} U_{p_0})^2}_{\text{Single-plaquette self-term } (p = p_0) = \frac{1}{2}\|P_{\mathfrak{su}(N)}(U_{p_0} - U_{p_0}^\dagger)\|_{\mathrm{HS}}^2 \ge 0} + \underbrace{\sum_{\substack{p \ni \ell \\ p \neq p_0}} \left[ \operatorname{Re}\operatorname{Tr}(U_{p_0} U_p^\dagger - U_{p_0} U_p) - \frac{2}{N}(\operatorname{Im}\operatorname{Tr} U_{p_0})(\operatorname{Im}\operatorname{Tr} U_p) \right]}_{2d - 3 \text{ Neighboring plaquette loop-merger \& } 1/N \text{ loop-splitting terms}} \Big\rangle_{\mu_\beta}.$$

### Audit of Closure (`SCHWINGER_DYSON_CLOSURE: PARTIAL / NOT_SELF_CLOSING`)
1. Summing over all $2(d - 1)$ plaquettes $p_0 \ni \ell$ gives the exact Lie-Laplacian positivity identity (`YM-011-PLAQUETTE-EXP-R2`):
   $$\frac{N^2 - 1}{2N} \big(1 - e_{\mathrm{plaq}}(\beta)\big) = \frac{\beta}{2(d - 1)} \sum_{a=1}^{N^2 - 1} \left\langle (\partial_\ell^a H(U))^2 \right\rangle_{\mu_\beta} \ge 0 \implies e_{\mathrm{plaq}}(\beta) \le 1.$$
   Because $\langle (\partial_\ell^a H)^2 \rangle_{\mu_\beta} \ge 0$ appears with a **positive** sign on the right-hand side against $1 - e_{\mathrm{plaq}}(\beta)$ on the left-hand side, this identity bounds $1 - e_{\mathrm{plaq}}(\beta)$ from **below** by $0$ ($e_{\mathrm{plaq}} \le 1$), **not** from above by $C/\beta$.
2. In the single-plaquette identity `YM-011-TORON-SD1`, isolating the quadratic fluctuation $\operatorname{Tr}(I_N - \operatorname{Re}(U_{p_0}^2)) \approx 4 N h_{p_0}(U)$ requires controlling the $2d - 3$ neighboring loop-merger correlations $\langle \operatorname{Re}\operatorname{Tr}(U_{p_0} U_p^\dagger - U_{p_0} U_p) \rangle_{\mu_\beta}$ (which couple 4-link plaquettes to 6-link domino loops $W_{2\times 1}$ and 8-link figure-eight loops of **indefinite sign**). Applying Cauchy–Schwarz bounds $|\langle \operatorname{Tr}((U_{p_0}-U_{p_0}^\dagger)(U_p^\dagger - U_p)) \rangle| \le \langle \|U_{p_0} - U_{p_0}^\dagger\|_{\mathrm{HS}}^2 \rangle$, which cancels the positive self-term with factor $(2d - 3) > 1$ for $d \ge 3$ ($2d - 3 = 3$ in $d=3$ and $5$ in $d=4$). Thus the local Schwinger–Dyson hierarchy does **not** self-close (`PARTIAL`).

---

## 6. Reflection Positivity / Chessboard and Character-Expansion Routes (Sections 8 & 9)

1. **Reflection Positivity and Chessboard Route (`REFLECTION_POSITIVITY_ROUTE: PARTIAL`):**
   - On the even periodic torus $\Lambda_{\mathrm{per}}(2L, d)$, the Wilson Gibbs measure $\mu_{\mathrm{per},\beta}$ is reflection positive across link-bisecting and site-containing hyperplanes $\Pi$ (`Osterwalder–Seiler 1978`, `Fröhlich–Israel–Lieb–Simon 1978`).
   - However, for a single plaquette observable $h_p(U) = 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p)$, the chessboard seminorm $\|h_p\|_{\mathrm{chess}} := \langle \prod_{x \in \Lambda_{\mathrm{hom}}} h_{p_x} \rangle_{\mu_{\mathrm{per},\beta}}^{1/|\Lambda_{\mathrm{hom}}|}$ satisfies $\langle h_p \rangle_{\mu_{\mathrm{per},\beta}} \le \|h_p\|_{\mathrm{chess}}$, where the disseminated observable $\prod_{x} h_{p_x}$ is still coupled across all $d$ dimensions via the non-Abelian 3-cube Bianchi identities in $d \ge 3$ rather than factoring into independent 1-plaquette integrals.
2. **Character-Expansion Route (`CHARACTER_EXPANSION_STATUS: PARTIAL`):**
   - The $SU(N)$ heat-kernel / character expansion $\exp\!\big(\frac{\beta}{N}\operatorname{Re}\operatorname{Tr} U_p\big) = \sum_{r \in \widehat{SU(N)}} d_r c_r(\beta) \chi_r(U_p)$ has strictly positive coefficients $c_r(\beta) > 0$ for all $\beta > 0$, yielding exact finite-volume positivity of Wilson loop expectations and convergent strong-coupling expansions for $\beta \le \beta_0 \ll 1$ (`Osterwalder–Seiler 1978`).
   - At weak coupling $\beta \gg 1$, representations up to Casimir scale $C_2(r) \sim \beta$ contribute constructively across all closed 2-surfaces in $\Lambda_{\mathrm{per}}(L, d)$ ($d \ge 3$), so strong-coupling character truncation cannot be applied at $\beta \gg 1$.

---

## 7. Toron Integration, Levi-Stratum Power Counting, Dyadic Concavity, and Proof of Fixed-Volume Periodic $O_L(1/\beta)$ (Sections 10–14)

### Theorem `YM-011-TORON-T1` (Universal Dyadic Partition-Ratio & Concavity Inequality)
For any finite lattice $\Lambda$ (free or periodic, any $L \ge 2, d \ge 2, N \ge 2$) and every $\beta > 0$, the log-partition function $\beta \mapsto \ln Z_\Lambda(\beta)$ is convex ($\partial_\beta^2 \ln Z_\Lambda(\beta) = \operatorname{Var}_{\mu_\beta}(H) \ge 0$), so $t \mapsto \langle H \rangle_{\mu_t} = -\partial_t \ln Z_\Lambda(t)$ is monotonically non-increasing on $(0, \infty)$. Integrating over the dyadic interval $[\beta/2, \beta]$ yields:
$$\frac{\beta}{2}\, \langle H \rangle_{\mu_\beta} \le \int_{\beta/2}^{\beta} \langle H \rangle_{\mu_t}\, dt = \ln Z_\Lambda(\beta/2) - \ln Z_\Lambda(\beta) = \ln \frac{Z_\Lambda(\beta/2)}{Z_\Lambda(\beta)},$$
and therefore:
$$e_{\mathrm{plaq}}(\beta, \Lambda) \le \frac{2}{|P_+|\,\beta} \ln \frac{Z_\Lambda(\beta/2)}{Z_\Lambda(\beta)} \qquad \forall \beta > 0.$$

### Theorem `YM-011-TORON-T2` (Levi-Stratum Power Counting and Proof of Fixed-Volume Periodic $O_L(1/\beta)$ — Resolution of `P1`)
On the periodic torus $\Lambda_{\mathrm{per}}(L, d)$, let $H : \Sigma_{T_{\mathrm{per}}} \to [0, \infty)$ be the tree-gauge Wilson Hamiltonian.
1. **Exact Harmonic Exponent Across Levi Strata:**
   Around each Levi stratum $L_{(n_1, \dots, n_k)} = S(U(n_1) \times \cdots \times U(n_k))$ ($S = \sum_{r=1}^k n_r^2$), integrating the $(d - 1)(N^2 - S)$ quadratic off-block modes ($\beta^{-1/2}$ each), the $d(S - k)$ quartic in-block modes ($\beta^{-1/4}$ each), and the $d(k - 1) + (N^2 - S)$ flat/conjugation modes ($\beta^0$ each) gives the local harmonic $\beta$-exponent:
   $$\alpha_{\mathrm{harm}}(n_1, \dots, n_k) = \frac{d - 1}{2}(N^2 - S) + \frac{d}{4}(S - k) = \frac{(d - 1)N(N - 1)}{2} + \frac{1}{4}\sum_{r=1}^k (n_r - 1)\big[ d - (d - 2) n_r \big].$$
   - In $d = 2$: $d - (d - 2)n_r = 2 > 0$, so the **regular toron stratum** $(1, \dots, 1)$ strictly minimizes $\alpha_{\mathrm{harm}}$ with $\alpha_{\mathrm{harm}}^{\min}(2, N) = \frac{N(N - 1)}{2}$.
   - In $d = 3$: $d - (d - 2)n_r = 3 - n_r$, so $\alpha_{\mathrm{harm}}^{\min}(3, 2) = 2$ (regular toron), $\alpha_{\mathrm{harm}}^{\min}(3, 3) = 6$ (marginal resonance between regular and central toron, producing $\ln \beta$ in $Z_{\mathrm{per}}(\beta)$), and $\alpha_{\mathrm{harm}}^{\min}(3, N) = \frac{3}{4}(N^2 - 1)$ for $N \ge 4$ (central toron).
   - In $d = 4$: $d - (d - 2)n_r = 4 - 2n_r = 2(2 - n_r) \le 0$ for all $n_r \ge 2$, so the **central toron stratum** $(N)$ minimizes $\alpha_{\mathrm{harm}}$ for all $N \ge 2$ (with marginal resonance at $n_r = 2$), yielding:
     $$\alpha_{\mathrm{harm}}^{\min}(4, N) = \frac{4(N^2 - 1)}{4} = N^2 - 1 \qquad \forall N \ge 2.$$
2. **Total Scaling Exponent $\alpha_L(d, N)$ and Sublevel Asymptotics:**
   Combining the $(N^2 - 1)(|E_{\mathrm{co-tree}}| - d)$ non-harmonic quadratic co-tree modes with $\alpha_{\mathrm{harm}}^{\min}(d, N)$ yields:
   $$\alpha_L(d, N) = \frac{1}{2}(N^2 - 1)\big(|E_{\mathrm{co-tree}}| - d\big) + \alpha_{\mathrm{harm}}^{\min}(d, N).$$
   By the real-analytic sublevel-set theorem (Łojasiewicz 1965; Varchenko 1976) on the compact real-analytic manifold $\Sigma_{T_{\mathrm{per}}}$, $V_L(s) = \mu_{\mathrm{Haar}}(\{H \le s\}) = c_0(L) s^{\alpha_L} (\ln(1/s))^{k_L} (1 + o_L(1))$ as $s \to 0^+$ and $Z_{\mathrm{per}}(\beta) = C_0(L) \beta^{-\alpha_L} (\ln \beta)^{k_L} (1 + O_L(1/\ln\beta))$ as $\beta \to \infty$.
3. **Resolution of `P1` (`FIXED_VOLUME_PERIODIC_O_1_OVER_BETA = PROVED`):**
   Both by direct differentiation of $\ln Z_{\mathrm{per}}(\beta)$ and by the dyadic ratio bound `YM-011-TORON-T1` (in which $\frac{Z_{\mathrm{per}}(\beta/2)}{Z_{\mathrm{per}}(\beta)} = 2^{\alpha_L} (1 + O_L(1/\ln\beta))$ cancels both $\beta^{-\alpha_L}$ and $(\ln \beta)^{k_L}$), the periodic plaquette expectation satisfies:
   $$e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{per}}(L, d)) = \frac{C_{\mathrm{per}}(L, d, N)}{\beta} - \frac{k_L}{|P_+|\,\beta \ln \beta} + o_L\!\left(\frac{1}{\beta \ln \beta}\right) = O_L\!\left(\frac{1}{\beta}\right),$$
   where the exact leading asymptotic coefficient is:
   $$C_{\mathrm{per}}(L, d, N) = \frac{\alpha_L(d, N)}{|P_+|} = \frac{(N^2 - 1)\big((d - 1)L^d + 1 - d\big) + 2\alpha_{\mathrm{harm}}^{\min}(d, N)}{d(d - 1) L^d} < \frac{N^2 - 1}{d}.$$
   In $d = 4$, for every $SU(N)$ ($N \ge 2$), this simplifies to the exact closed form:
   $$C_{\mathrm{per}}(L, 4, N) = \frac{(N^2 - 1)(3L^4 - 1)}{12 L^4} = \frac{N^2 - 1}{4}\left(1 - \frac{1}{3L^4}\right) < \frac{N^2 - 1}{4}.$$

---

## 8. Comparison with Bałaban's Weak-Coupling Machinery and Primary-Source Audit (Sections 15 & 16)

### 8.1 Comparison with Bałaban (`CMP 95, 96, 98, 109, 116, 119, 122`)
Bałaban's multiscale renormalization-group program controls single-step block averaging on a finite periodic torus by decomposing the configuration space into a small-field domain $\mathcal{S}_k$ (where covalent axial/Landau gauge fixing eliminates local gauge degrees of freedom and bounds the local fluctuation propagator) and a large-field polymer domain $\mathcal{L}_k$ (controlled by Peierls stability and Kotecký–Preiss polymer cluster expansions). However, Bałaban does **not** prove a standalone unconditional theorem $e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{per}}) \le C(N, d)/\beta$ on the un-gauge-fixed periodic torus without the full multiscale large-field polymer expansion.

### 8.2 Primary-Source Audit Table (12 Mandatory Fields)

| SOURCE | YEAR | THEOREM / PAGE | EXACT STATEMENT USED | GAUGE GROUP | DIMENSION | FINITE / PERIODIC / FREE | BETA REGIME | VOLUME DEPENDENCE | ZERO-MODE ASSUMPTIONS | CONCLUSION | PROJECT USE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Brascamp & Lieb**, *J. Funct. Anal.* 22, 366–389 | 1976 | Theorem 4.1, pp. 376–379 | $\operatorname{Var}_\mu(f) \le \langle \nabla f, (\operatorname{Hess} V)^{-1} \nabla f \rangle_\mu$ for log-concave $e^{-V(x)} dx$ | Euclidean $\mathbb{R}^M$ (adapted to Lie algebras) | Any $M \ge 1$ | Convex domain $D \subseteq \mathbb{R}^M$ | Requires $\operatorname{Hess} V > 0$ globally on $D$ | Depends on $\lambda_{\min}(\operatorname{Hess} V)^{-1}$ | Requires zero modes absent ($\ker \operatorname{Hess} V = \{0\}$) | Covariance bounded by inverse Hessian | Proves why `GLOBAL_BRASCAMP_LIEB = NOT_APPLICABLE` on $SU(N)$ & $\mathcal{M}_{\mathrm{flat}}$ |
| **Osterwalder & Seiler**, *Ann. Phys.* 110, 440–471 | 1978 | Section 2 (Reflection Positivity) & Section 3 (Cluster Expansion), pp. 444–460 | Link reflection positivity of Wilson action and convergent character-polymer expansion at $\beta \ll 1$ | Compact $G \subseteq U(N)$ | $d \ge 2$ | Finite periodic / even torus & infinite volume | $\beta > 0$ for RP; $\beta \le \beta_0 \ll 1$ for convergence | Uniform in $L$ for RP and strong coupling | None | Establishes RP on even periodic torus & strong-coupling area law | Used in Sections 8 & 9 for RP and character positivity audit |
| **Fröhlich, Israel, Lieb & Simon**, *Commun. Math. Phys.* 62, 1–34 | 1978 | Theorem 2.2 (Chessboard Estimate), pp. 8–12 | $\lvert\langle \prod_{x \in B} A_x \rangle\rvert \le \prod_{x \in B} \langle \prod_{y} \theta_{y}(A_x) \rangle^{1/\lvert\Lambda\rvert}$ | General reflection-positive lattice systems | $d \ge 1$ | Even periodic torus $(\mathbb{Z}/2L\mathbb{Z})^d$ | All $\beta > 0$ | Homogeneous periodic disseminated product | None | Bounds inhomogeneous correlations by periodic homogeneous product | Shows chessboard dissemination of a single plaquette reproduces homogeneous periodic torus (`PARTIAL`) |
| **Makeenko & Migdal**, *Phys. Lett. B* 88, 135–137 (and *Nucl. Phys. B* 188, 269) | 1979 / 1981 | Master Loop Equation, pp. 135–137 | Invariant link variation of Wilson loop equates Casimir self-term to loop-merger and $1/N$ loop-splitting terms | $SU(N)$ and $U(N)$ | $d \ge 2$ | Finite or infinite lattice | All $\beta > 0$ | Exact local identity at each link $\ell$ | None | Exact Schwinger–Dyson identity coupling 1-plaquette to 6-link domino loops | Verified at finite $N$ in Theorem `YM-011-TORON-SD1` (`PARTIAL / NOT_SELF_CLOSING`) |
| **Lüscher**, *Nucl. Phys. B* 219, 233–261 | 1983 | Section 2 (Toron Zero Modes & Quartic Action), pp. 235–244 | Zero-momentum gauge modes on $\mathbb{T}^d$ have quartic commutator action $\frac{1}{4}\operatorname{Tr}[A_\mu, A_\nu]^2$ and scale as $g^{1/2} \sim \beta^{-1/4}$ | $SU(N)$, $N \ge 2$ | $d = 4$ (and $d=3$) | Periodic torus $\mathbb{T}^d$ | Weak coupling $\beta \gg 1$ | Fixed torus volume | Analyzes expansion around $A_\mu = 0$ central toron | Quartic zero modes contribute fractional powers $\beta^{-1/4}$ per mode | Grounds central-toron quartic scaling in Sections 2, 3, 11 |
| **Varchenko**, *Invent. Math.* 37, 253–262 (and **Arnol'd, Gusein-Zade, Varchenko**, Vol. II) | 1976 / 1988 | Theorem 1.1 & Ch. 7 (Asymptotics of Real-Analytic Oscillatory & Laplace Integrals) | For real-analytic $H \ge 0$ with $H^{-1}(0) \neq \emptyset$ on compact $\Omega$, $\int_\Omega e^{-\beta H} d\mu \sim C_0 \beta^{-\alpha_L} (\ln \beta)^{k_L}$ as $\beta \to \infty$ | Compact real-analytic manifold $\Omega = SU(N)^{\lvert E_+\rvert}$ | Any finite dimension $M$ | Compact manifold (periodic or free lattice at fixed $L$) | $\beta \to \infty$ at fixed $L$ | Fixed finite dimension $M(L)$ | Resolves arbitrary algebraic singularities of $H^{-1}(0)$ | Differentiating $\ln Z(\beta)$ yields $-\partial_\beta \ln Z(\beta) = \alpha_L / \beta + O_L(1/(\beta \ln \beta))$ | Rigorously establishes `P1` (`FIXED_VOLUME_PERIODIC_O_1_OVER_BETA = PROVED`) in Theorem `YM-011-TORON-T2` |
| **Bałaban**, *Commun. Math. Phys.* 95, 17–40 & *CMP* 109, 249–301 | 1984 / 1987 | Prop. 2.1–3.4 (Axial Gauge Fixing & Small/Large-Field Split) | Propagator and polymer bounds on small-field domain $\mathcal{S}_k$ with block gauge fixing | $SU(N)$ | $d = 3, 4$ | Finite periodic torus $\mathbb{T}_L^d$ | Weak coupling $\beta \gg 1$ | Multiscale RG block steps | Restricts to small-field neighborhood away from toron singularities | Controls block effective action via small/large-field split | Confirms `P2` requires uniform large-field / dyadic free-energy control |

---

## 9. Required Scientific Dispositions (Section 18)

| Required Disposition Item | Assigned Status | Mathematical Justification |
| :--- | :--- | :--- |
| **`TORON_QUARTIC_GEOMETRY`** | **`PROVED`** | Exact commuting variety $\mathcal{Z}(Q) = \mathfrak{C}_d(\mathfrak{su}(N))$ of dimension $(d+N)(N-1)$, quotient $\mathfrak{t}_{\max}^d/S_N$ of dimension $d(N-1)$, transverse codimension $(d-1)N(N-1)$, and complete Levi-stratum dimension partition $d(k-1) + (N^2-S) + (d-1)(N^2-S) + d(S-k) = d(N^2-1)$ (`YM-011-TORON-Q1`, `YM-011-TORON-T2`). |
| **`BRASCAMP_LIEB_APPLICABILITY`** | **`NOT_APPLICABLE` (Global) / `CONDITIONAL` (Local)** | Global Brascamp–Lieb fails due to non-convexity of $H(U)$ on $SU(N)$ and vanishing Hessian on $\mathcal{M}_{\mathrm{flat}}$ (`sup ||(Hess V)^{-1}|| = +infty`). Local Brascamp–Lieb on $\mathcal{G}_\epsilon$ is conditional on transverse toron cutoff and large-field tail $\mu_{\mathrm{per},\beta}(\mathcal{G}_\epsilon^c)$. |
| **`SCHWINGER_DYSON_CLOSURE`** | **`PARTIAL`** | Exact link identity `YM-011-TORON-SD1` proved with all Casimir and $1/N$ factors; single-plaquette expectation couples to $2d-3$ neighboring 6-link domino loops $W_{2\times 1}$ of indefinite sign and does not self-close. |
| **`REFLECTION_POSITIVITY_ROUTE`** | **`PARTIAL`** | Wilson measure on $\Lambda_{\mathrm{per}}(2L, d)$ is reflection positive across link/site hyperplanes, but chessboard dissemination of $h_p$ reproduces the homogeneous 3D/4D periodic torus without decoupling 3-cube Bianchi constraints. |
| **`STRATIFIED_LAPLACE_ROUTE`** | **`PROVED` (at fixed $L$)** | Real-analytic sublevel asymptotics $V_L(s) \sim c_0(L) s^{\alpha_L}(\ln(1/s))^{k_L}$ and Levi-stratum power counting prove $\alpha_L(d, N) = \frac{1}{2}(N^2-1)(|E_{\mathrm{co-tree}}|-d) + \alpha_{\mathrm{harm}}^{\min}(d, N)$ and $e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{per}}(L, d)) = \frac{\alpha_L}{|P_+|\beta} + O_L\!\left(\frac{1}{\beta \ln\beta}\right)$ (`YM-011-TORON-T2`). |
| **`FIXED_VOLUME_PERIODIC_O_1_OVER_BETA` (`P1`)** | **`PROVED`** | Proved via Theorem `YM-011-TORON-T1` (dyadic concavity bound $e_{\mathrm{plaq}} \le \frac{2}{|P_+|\beta} \ln \frac{Z(\beta/2)}{Z(\beta)}$) and Theorem `YM-011-TORON-T2` (stratified real-analytic sublevel asymptotics), with leading coefficient $C_{\mathrm{per}}(L, 4, N) = \frac{(N^2-1)(3L^4-1)}{12 L^4} < \frac{N^2-1}{4}$. |
| **`VOLUME_UNIFORM_PERIODIC_O_1_OVER_BETA` (`P2`)** | **`OPEN`** | While the asymptotic slope $\frac{\alpha_L(d, N)}{|P_+|} \le \frac{N^2-1}{d}$ is bounded uniformly in $L$, bounding the non-asymptotic dyadic increment $\frac{1}{|P_+|} \ln \frac{Z_{\mathrm{per}}(\beta/2)}{Z_{\mathrm{per}}(\beta)}$ uniformly in $L$ at fixed $\beta$ remains `OPEN` (`YM-011-DYADIC-FREE-ENERGY-UNIFORMITY`). |
| **`CONTINUUM_UNIFORM_CONTROL` (`P3`)** | **`OPEN`** | Not established (`CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `GOAL_COMPLETE = FALSE`). |
