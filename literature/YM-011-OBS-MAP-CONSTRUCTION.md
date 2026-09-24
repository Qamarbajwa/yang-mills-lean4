# Task `YM-011-OBS-MAP` — Construction and Verification of the First Observable-Transfer Map

- **TASK_ID:** `YM-011-OBS-MAP`
- **TASK_STATUS:** `SCIENTIFICALLY_VERIFIED_FINITE_LATTICE_OBSERVABLE_TRANSFER`
- **ORIGINAL_YM_011_CONTINUUM_PROPOSAL_STATUS:** `NOT_AUTHORIZED` (`PROPOSED / NOT AUTHORIZED FOR PROOF EXECUTION`)
- **YM_006_THROUGH_YM_010_STATUS:** `SCIENTIFIC_REVIEW_HOLD`
- **GOAL_COMPLETE:** `FALSE` (`CLAY_PROBLEM = OPEN_AND_UNSOLVED`)
- **GOVERNANCE_TIER:** `R2` (Autonomous Scientific Verification & Independent Adversarial Review under `YM-GOV-014` / `YM-GOV-015`)
- **PREREQUISITE_DEPENDENCIES:** `YM-004` (Bałaban Finite-Volume Multiscale Framework), `YM-005-R2` (Regulated Lattice Gap & Source-Scope Correspondence), `YM-011-PRE-R1` (Fixed-Lattice Gradient-Flow Loop Perturbation, $K = 2(d-1) = 6$)
- **VERIFICATION_MODULE:** `src/ymmg/observable_transfer.py` & `tests/test_ym_011_obs_map.py`

---

## 1. Explicit Two-Lattice Geometry, Configuration Spaces, Probability Measures, and Gauge Actions (Spacings $a$ and $2a$)

We work strictly on two finite periodic hypercubic lattices of spacings $a > 0$ and $2a > 0$ in dimension $d \ge 2$ (specifically $d = 4$) with compact gauge group $G = SU(N)$ ($N \ge 2$).

### 1.1 Finite Lattice Geometries $\Lambda_0$ and $\Lambda_1$
Fix an integer $L \in \mathbb{N}_{\ge 1}$:
1. **Fine Lattice $\Lambda_0$ (spacing $a$):**
   - Vertex set $V(\Lambda_0) := (a\mathbb{Z} / 2La\mathbb{Z})^d$ with $|V(\Lambda_0)| = (2L)^d$.
   - Oriented nearest-neighbor edge set $E(\Lambda_0) := \{ \ell = (x, x \pm a\hat{\mu}) : x \in V(\Lambda_0), \, \mu \in \{1, \dots, d\} \}$, partitioned into positively oriented edges $E_+(\Lambda_0) = \{ (x, x + a\hat{\mu}) \}$ ($|E_+(\Lambda_0)| = d(2L)^d$) and their reversals $\ell^{-1} = (x + a\hat{\mu}, x)$.
   - Positively oriented elementary $a \times a$ plaquettes $P_+(\Lambda_0)$ ($|P_+(\Lambda_0)| = \binom{d}{2}(2L)^d$).
2. **Coarse Sublattice $\Lambda_1$ (spacing $2a$):**
   - Vertex set $V(\Lambda_1) := (2a\mathbb{Z} / 2La\mathbb{Z})^d \subset V(\Lambda_0)$ with $|V(\Lambda_1)| = L^d$, embedded into $V(\Lambda_0)$ via the canonical inclusion $\iota_V : V(\Lambda_1) \hookrightarrow V(\Lambda_0)$, $\iota_V(y) = y$.
   - Oriented coarse nearest-neighbor edge set $E(\Lambda_1) := \{ e = (y, y \pm 2a\hat{\mu}) : y \in V(\Lambda_1), \, \mu \in \{1, \dots, d\} \}$, with positively oriented subset $E_+(\Lambda_1) = \{ (y, y + 2a\hat{\mu}) \}$ ($|E_+(\Lambda_1)| = d L^d$) and reversals $e^{-1} = (y + 2a\hat{\mu}, y)$.
   - Each coarse edge $e = (y, y + 2a\hat{\mu}) \in E(\Lambda_1)$ has a unique fine-lattice midpoint $m(e) := y + a\hat{\mu} \in V(\Lambda_0) \setminus \iota_V(V(\Lambda_1))$ and a canonical two-link coaxial path $\gamma_0(e) := (\ell_{e,1}, \ell_{e,2}) \subset E(\Lambda_0)$ where
     $$\ell_{e,1} := (y, \, y + a\hat{\mu}), \qquad \ell_{e,2} := (y + a\hat{\mu}, \, y + 2a\hat{\mu}), \qquad \gamma_0(e^{-1}) = (\ell_{e,2}^{-1}, \, \ell_{e,1}^{-1}).$$

### 1.2 Configuration Spaces and Probability Measures
1. **Fine Configuration Space $(\Omega_0, \mathcal{F}_0, \mu_0)$:**
   $$\Omega_0 := \left\{ U \in SU(N)^{E(\Lambda_0)} : U(\ell^{-1}) = U(\ell)^{-1} = U(\ell)^\dagger \;\;\forall \ell \in E(\Lambda_0) \right\} \cong SU(N)^{E_+(\Lambda_0)},$$
   equipped with the product Borel $\sigma$-algebra $\mathcal{F}_0 := \mathcal{B}(\Omega_0)$, the product normalized Haar measure $d\mu_{\mathrm{Haar},0}(U) := \prod_{\ell \in E_+(\Lambda_0)} dU(\ell)$, and the finite-volume Wilson Gibbs probability measure at bare coupling $\beta = \frac{2N}{g_0^2} > 0$:
   $$d\mu_0(U) := \frac{1}{Z_{\Lambda_0}(\beta)} \exp\!\left(-S_W(U)\right) d\mu_{\mathrm{Haar},0}(U), \qquad S_W(U) := \frac{\beta}{N} \sum_{p \in P_+(\Lambda_0)} \operatorname{Re}\operatorname{Tr}\!\left(I_N - U_p\right), \qquad Z_{\Lambda_0}(\beta) := \int_{\Omega_0} e^{-S_W(U)} d\mu_{\mathrm{Haar},0}(U) > 0.$$
   Since $\Omega_0$ is a compact connected smooth manifold and $S_W \in C^\infty(\Omega_0, \mathbb{R})$, $0 < e^{-2\beta |P_+(\Lambda_0)|} \le Z_{\Lambda_0}(\beta) \le 1$, so $\mu_0$ is a strictly positive Radon probability measure on $(\Omega_0, \mathcal{F}_0)$.
2. **Coarse Configuration Space $(\Omega_1, \mathcal{F}_1)$:**
   $$\Omega_1 := \left\{ V \in SU(N)^{E(\Lambda_1)} : V(e^{-1}) = V(e)^{-1} = V(e)^\dagger \;\;\forall e \in E(\Lambda_1) \right\} \cong SU(N)^{E_+(\Lambda_1)},$$
   equipped with the product Borel $\sigma$-algebra $\mathcal{F}_1 := \mathcal{B}(\Omega_1)$ and reference product Haar measure $d\mu_{\mathrm{Haar},1}(V) := \prod_{e \in E_+(\Lambda_1)} dV(e)$.

### 1.3 Gauge-Group Actions and Restriction Homomorphism
1. **Fine Gauge Group $\mathcal{G}_0 := SU(N)^{V(\Lambda_0)}$:** Acts continuously from the left on $\Omega_0$ via
   $$(g_0 \cdot U)(x, x + a\hat{\mu}) := g_0(x) \, U(x, x + a\hat{\mu}) \, g_0(x + a\hat{\mu})^{-1} \qquad (\forall g_0 \in \mathcal{G}_0, \, U \in \Omega_0).$$
   Both $S_W(U)$ and $d\mu_{\mathrm{Haar},0}(U)$ are $\mathcal{G}_0$-invariant, so $\mu_0$ is $\mathcal{G}_0$-invariant: $(g_0)_\# \mu_0 = \mu_0$.
2. **Coarse Gauge Group $\mathcal{G}_1 := SU(N)^{V(\Lambda_1)}$:** Acts continuously from the left on $\Omega_1$ via
   $$(g_1 \cdot V)(y, y + 2a\hat{\mu}) := g_1(y) \, V(y, y + 2a\hat{\mu}) \, g_1(y + 2a\hat{\mu})^{-1} \qquad (\forall g_1 \in \mathcal{G}_1, \, V \in \Omega_1).$$
3. **Surjective Restriction Homomorphism $\pi_{\mathcal{G}} : \mathcal{G}_0 \twoheadrightarrow \mathcal{G}_1$:**
   $$(\pi_{\mathcal{G}}(g_0))(y) := g_0(\iota_V(y)) \qquad (\forall y \in V(\Lambda_1)).$$
   A blocking map $\mathcal{B} : \Omega_0 \to \Omega_1$ is **gauge-equivariant** if and only if $\mathcal{B}(g_0 \cdot U) = \pi_{\mathcal{G}}(g_0) \cdot \mathcal{B}(U)$ for all $g_0 \in \mathcal{G}_0$ and $U \in \Omega_0$. Notice that this requires $\mathcal{B}(U)(e)$ to be **strictly invariant** under all fine gauge transformations $g_0 \in \ker(\pi_{\mathcal{G}})$ supported on non-coarse vertices $V(\Lambda_0) \setminus \iota_V(V(\Lambda_1))$ (in particular, at the midpoint $m(e) = y + a\hat{\mu}$).

---

## 2. Concrete Blocking Maps and Normalized Markov Kernels

### 2.1 Negative Structural Result (`NEG-YM-011-OBS-1`): Why Naive Linear Staple Averaging Fails Globally on $\Omega_0$
In informal block-spin treatments (e.g. Swendsen 1981), one writes the linear matrix sum over the coaxial path $\gamma_0(e)$ and the $2(d-1)$ transverse $2a \times a$ staple paths $\Gamma_{\mathrm{staple}}(e)$:
$$M_\alpha^{\mathrm{lin}}(e)[U] := (1 - \alpha) \, U(\ell_{e,1}) U(\ell_{e,2}) + \frac{\alpha}{2(d - 1)} \sum_{\gamma \in \Gamma_{\mathrm{staple}}(e)} H_0(\gamma)[U] \in M_N(\mathbb{C}),$$
and attempts to project $M_\alpha^{\mathrm{lin}}(e)[U]$ onto $SU(N)$ via polar decomposition $\Pi_{SU(N)}(M) = M(M^\dagger M)^{-1/2}(\det(M(M^\dagger M)^{-1/2}))^{-1/N}$.
- **Explicit Counterexample (`NEG-YM-011-OBS-1`):** For $G = SU(2)$, $\alpha = 1/2$, $U(\ell_{e,1}) U(\ell_{e,2}) = I_2 \in SU(2)$, and $H_0(\gamma)[U] = -I_2 \in SU(2)$ ($\det(-I_2) = 1$), we have $M_{1/2}^{\mathrm{lin}}(e)[U] = \frac{1}{2}I_2 + \frac{1}{2}(-I_2) = 0_{2\times 2}$, so $\det M_{1/2}^{\mathrm{lin}}(e)[U] = 0$. The polar projection $\Pi_{SU(N)}$ is undefined on the non-empty singular locus $\Sigma_\alpha := \{ U \in \Omega_0 : \exists e \in E_+(\Lambda_1), \, \det M_\alpha^{\mathrm{lin}}(e)[U] = 0 \}$ and fails to define a globally smooth map $\Omega_0 \to \Omega_1$.

### 2.2 Globally Smooth, Everywhere $SU(N)$-Valued Deterministic Midpoint-Exponential Blocking Map $\mathcal{B}_\alpha^{\mathrm{mid}} : \Omega_0 \to \Omega_1$
To eliminate the singular locus $\Sigma_\alpha$ completely while maintaining exact $SU(N)$ values, exact orientation covariance, and exact $\mathcal{G}_0 \to \mathcal{G}_1$ gauge equivariance, we construct the **Midpoint-Exponential Blocking Map** $\mathcal{B}_\alpha^{\mathrm{mid}} : \Omega_0 \to \Omega_1$ ($\alpha \in \mathbb{R}$):

For each oriented coarse edge $e = (y, y + 2a\hat{\mu}) \in E(\Lambda_1)$ with coaxial fine links $\ell_{e,1} = (y, y+a\hat{\mu})$ and $\ell_{e,2} = (y+a\hat{\mu}, y+2a\hat{\mu})$, let $\Gamma_{\mathrm{staple}}(e) = \{ \gamma_{\nu,\sigma}(e) : \nu \ne \mu, \, \sigma \in \{+,-\} \}$ be the $2(d-1)$ oriented 4-link transverse rectangular paths in $E(\Lambda_0)$ joining $y$ to $y + 2a\hat{\mu}$:
$$\gamma_{\nu,\sigma}(e) := \left( (y, \, y + \sigma a\hat{\nu}), \; (y + \sigma a\hat{\nu}, \, y + \sigma a\hat{\nu} + a\hat{\mu}), \; (y + \sigma a\hat{\nu} + a\hat{\mu}, \, y + \sigma a\hat{\nu} + 2a\hat{\mu}), \; (y + \sigma a\hat{\nu} + 2a\hat{\mu}, \, y + 2a\hat{\mu}) \right),$$
with fine holonomy $H_0(\gamma_{\nu,\sigma}(e))[U] \in SU(N)$. Define the **midpoint-based closed loop** $L_{\nu,\sigma}(e)[U] \in SU(N)$ and **midpoint Lie-algebra generator** $X_{\mathrm{mid}}(e)[U] \in \mathfrak{su}(N)$ by:
$$L_{\nu,\sigma}(e)[U] := U(\ell_{e,1})^\dagger \, H_0(\gamma_{\nu,\sigma}(e))[U] \, U(\ell_{e,2})^\dagger \in SU(N),$$
$$X_{\mathrm{mid}}(e)[U] := \mathcal{P}_{\mathfrak{su}(N)}\!\left( \frac{1}{2(d - 1)} \sum_{\nu \ne \mu, \, \sigma \in \{+,-\}} L_{\nu,\sigma}(e)[U] \right) \in \mathfrak{su}(N),$$
and define the blocked coarse link $\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e)$ for $\alpha \in \mathbb{R}$ by:
$$\boxed{\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) := U(\ell_{e,1}) \, \exp\!\left( \alpha \, X_{\mathrm{mid}}(e)[U] \right) \, U(\ell_{e,2}) \in SU(N).}$$

#### Verification of Structural Properties of $\mathcal{B}_\alpha^{\mathrm{mid}}$
1. **Global Smoothness, $SU(N)$ Membership, and Borel Measurability:**
   For all $U \in \Omega_0$ and $\alpha \in \mathbb{R}$, $X_{\mathrm{mid}}(e)[U] \in \mathfrak{su}(N)$ is anti-Hermitian and traceless, so $\exp(\alpha X_{\mathrm{mid}}(e)[U]) \in SU(N)$ and $\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) \in SU(N)$ as a product of three elements of $SU(N)$. Since matrix multiplication, $\mathcal{P}_{\mathfrak{su}(N)}$, and $\exp : \mathfrak{su}(N) \to SU(N)$ are $C^\infty$ maps on compact manifolds, $\mathcal{B}_\alpha^{\mathrm{mid}} \in C^\infty(\Omega_0, \Omega_1)$ and is $\mathcal{F}_0 / \mathcal{F}_1$-measurable. At $\alpha = 0$, $\mathcal{B}_0^{\mathrm{mid}} = \mathcal{B}^{\mathrm{dec}}_{0\to 1}$ is exact coaxial two-link decimation.
2. **Exact Orientation Covariance ($\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e^{-1}) = (\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e))^{-1}$):**
   Under edge reversal $e \mapsto e^{-1} = (y + 2a\hat{\mu}, y)$, the two coaxial links reverse and swap roles ($\ell_{e^{-1},1} = \ell_{e,2}^{-1}$, $\ell_{e^{-1},2} = \ell_{e,1}^{-1}$), and each staple path reverses to $\gamma_{\nu,\sigma}(e^{-1}) = \gamma_{\nu,\sigma}(e)^{-1}$ with $H_0(\gamma_{\nu,\sigma}(e^{-1}))[U] = H_0(\gamma_{\nu,\sigma}(e))[U]^\dagger$. Hence:
   $$L_{\nu,\sigma}(e^{-1})[U] = \left(U(\ell_{e,2})^\dagger\right)^\dagger H_0(\gamma_{\nu,\sigma}(e))[U]^\dagger \left(U(\ell_{e,1})^\dagger\right)^\dagger = U(\ell_{e,2}) \, H_0(\gamma_{\nu,\sigma}(e))[U]^\dagger \, U(\ell_{e,1}) = \left( L_{\nu,\sigma}(e)[U] \right)^\dagger.$$
   Because $\mathcal{P}_{\mathfrak{su}(N)}(M^\dagger) = -\mathcal{P}_{\mathfrak{su}(N)}(M)$ for all $M \in M_N(\mathbb{C})$, we have $X_{\mathrm{mid}}(e^{-1})[U] = -X_{\mathrm{mid}}(e)[U]$, and therefore:
   $$\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e^{-1}) = U(\ell_{e,2})^\dagger \, \exp\!\left(-\alpha \, X_{\mathrm{mid}}(e)[U]\right) \, U(\ell_{e,1})^\dagger = \left( U(\ell_{e,1}) \, \exp\!\left(\alpha \, X_{\mathrm{mid}}(e)[U]\right) \, U(\ell_{e,2}) \right)^{-1} = \left( \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) \right)^{-1}.$$
3. **Exact Gauge Equivariance ($\mathcal{B}_\alpha^{\mathrm{mid}}(g_0 \cdot U) = \pi_{\mathcal{G}}(g_0) \cdot \mathcal{B}_\alpha^{\mathrm{mid}}(U)$):**
   Let $g_0 \in \mathcal{G}_0$ and write $m = m(e) = y + a\hat{\mu}$, $y' = y + 2a\hat{\mu}$. Under $U \mapsto g_0 \cdot U$:
   $$U(\ell_{e,1}) \mapsto g_0(y) U(\ell_{e,1}) g_0(m)^{-1}, \qquad U(\ell_{e,2}) \mapsto g_0(m) U(\ell_{e,2}) g_0(y')^{-1}, \qquad H_0(\gamma_{\nu,\sigma}(e)) \mapsto g_0(y) H_0(\gamma_{\nu,\sigma}(e)) g_0(y')^{-1}.$$
   Therefore, $L_{\nu,\sigma}(e)$ transforms by adjoint conjugation at the midpoint $m$:
   $$L_{\nu,\sigma}(e)[g_0 \cdot U] = \left(g_0(m) U(\ell_{e,1})^\dagger g_0(y)^{-1}\right) \left(g_0(y) H_0(\gamma_{\nu,\sigma}(e))[U] g_0(y')^{-1}\right) \left(g_0(y') U(\ell_{e,2})^\dagger g_0(m)^{-1}\right) = g_0(m) \, L_{\nu,\sigma}(e)[U] \, g_0(m)^{-1}.$$
   Since $\mathcal{P}_{\mathfrak{su}(N)}$ and $\exp$ commute with unitary conjugation by $g_0(m) \in SU(N)$,
   $$\mathcal{B}_\alpha^{\mathrm{mid}}(g_0 \cdot U)(e) = \left(g_0(y) U(\ell_{e,1}) g_0(m)^{-1}\right) \left(g_0(m) \exp\!\left(\alpha X_{\mathrm{mid}}(e)[U]\right) g_0(m)^{-1}\right) \left(g_0(m) U(\ell_{e,2}) g_0(y')^{-1}\right) = g_0(y) \, \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) \, g_0(y')^{-1} = \left(\pi_{\mathcal{G}}(g_0) \cdot \mathcal{B}_\alpha^{\mathrm{mid}}(U)\right)(e).$$
   In particular, the midpoint gauge transformation $g_0(m)$ and all off-axis fine gauge transformations $g_0(y \pm a\hat{\nu}), g_0(m \pm a\hat{\nu})$ **cancel identically**.

### 2.3 Normalized Gauge-Covariant Markov Kernel $K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U)$
For any concentration parameter $\kappa \in [0, \infty)$, define the Markov transition kernel $K^{(\alpha,\kappa)}_{0\to 1} : \Omega_0 \times \mathcal{F}_1 \to [0, 1]$ by:
$$\boxed{K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U) := \prod_{e \in E_+(\Lambda_1)} \frac{\exp\!\left(\frac{\kappa}{N}\operatorname{Re}\operatorname{Tr}\!\left(V(e)^\dagger \, \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e)\right)\right)}{z_N(\kappa)} \, dV(e), \qquad z_N(\kappa) := \int_{SU(N)} \exp\!\left(\frac{\kappa}{N}\operatorname{Re}\operatorname{Tr}(W)\right) dW > 0.}$$
- **Exact Normalization:** Because $\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) \in SU(N)$ and $dV(e)$ is right-invariant Haar measure on $SU(N)$, changing variables to $W = V(e)^\dagger \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e) \in SU(N)$ gives $\int_{SU(N)} \exp(\frac{\kappa}{N}\operatorname{Re}\operatorname{Tr}(V(e)^\dagger \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e))) dV(e) = z_N(\kappa)$ identically (independent of $U$ and $e$). Thus $\int_{\Omega_1} K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U) = 1$ for every $U \in \Omega_0$.
- **Exact Gauge Equivariance:** For all $g_0 \in \mathcal{G}_0$ and $A \in \mathcal{F}_1$, $K^{(\alpha,\kappa)}_{0\to 1}(\pi_{\mathcal{G}}(g_0) \cdot A \mid g_0 \cdot U) = K^{(\alpha,\kappa)}_{0\to 1}(A \mid U)$ by bi-invariance of Haar measure and trace cyclicity $\operatorname{Re}\operatorname{Tr}((g_1(y) V(e) g_1(y')^{-1})^\dagger (g_1(y) B g_1(y')^{-1})) = \operatorname{Re}\operatorname{Tr}(V(e)^\dagger B)$.
- **Weak-Star Limit as $\kappa \to \infty$:** As $\kappa \to \infty$, $K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U) \rightharpoonup \delta_{\mathcal{B}_\alpha^{\mathrm{mid}}(U)}(dV)$ weakly as probability measures on $\Omega_1$.

---

## 3. Coarse Loop Embedding, Observable Pullback, and Effective Action

### 3.1 Coarse Loop Subdivision Embedding $\iota_{\mathrm{loop}} : \mathcal{L}(\Lambda_1) \hookrightarrow \mathcal{L}(\Lambda_0)$
Let $C_1 = (e_1, e_2, \dots, e_m)$ be a closed oriented loop of $m = |C_1|_{\Lambda_1}$ coarse edges on $\Lambda_1$, with physical perimeter $L_{\mathrm{phys}}(C_1) := m \cdot (2a) = 2ma$. Its canonical subdivision embedding into $\Lambda_0$ is the concatenation of the coaxial two-link paths $\gamma_0(e_k) = (\ell_{e_k,1}, \ell_{e_k,2})$:
$$\iota_{\mathrm{loop}}(C_1) := \gamma_0(e_1) \star \gamma_0(e_2) \star \cdots \star \gamma_0(e_m) = \left( \ell_{e_1,1}, \, \ell_{e_1,2}, \, \ell_{e_2,1}, \, \ell_{e_2,2}, \, \dots, \, \ell_{e_m,1}, \, \ell_{e_m,2} \right) \in \mathcal{L}(\Lambda_0).$$
Then $\iota_{\mathrm{loop}}(C_1)$ is a closed oriented loop on $\Lambda_0$ consisting of $|\iota_{\mathrm{loop}}(C_1)|_{\Lambda_0} = 2m = 2|C_1|_{\Lambda_1}$ fine edges of length $a$, preserving physical perimeter:
$$L_{\mathrm{phys}}\!\left(\iota_{\mathrm{loop}}(C_1)\right) = (2m) \cdot a = 2ma = L_{\mathrm{phys}}(C_1).$$

### 3.2 Pullback of Coarse Wilson-Loop Observables
For $V \in \Omega_1$, let $H_1(C_1)[V] := \prod_{k=1}^m V(e_k) \in SU(N)$, and denote the coarse complex and real normalized Wilson traces by $W_{\Lambda_1}^{\mathbb{C}}(C_1)[V] := \frac{1}{N}\operatorname{Tr}(H_1(C_1)[V])$ and $W_{\Lambda_1}^{\mathbb{R}}(C_1)[V] := \frac{1}{N}\operatorname{Re}\operatorname{Tr}(H_1(C_1)[V])$.
1. **Deterministic Pullback $(\mathcal{B}_\alpha^{\mathrm{mid}})^* : C(\Omega_1) \to C(\Omega_0)$:**
   $$\left( (\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1) \right)[U] := W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1)\!\left[ \mathcal{B}_\alpha^{\mathrm{mid}}(U) \right] = \frac{1}{N} \operatorname{Re}/\operatorname{Tr}\!\left( \prod_{k=1}^m U(\ell_{e_k,1}) \exp\!\left(\alpha X_{\mathrm{mid}}(e_k)[U]\right) U(\ell_{e_k,2}) \right).$$
2. **Markov Kernel Pullback $(K^{(\alpha,\kappa)}_{0\to 1})^* : C(\Omega_1) \to C(\Omega_0)$:**
   $$\left( (K^{(\alpha,\kappa)}_{0\to 1})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1) \right)[U] := \int_{\Omega_1} W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1)[V] \, K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U).$$
Both pulled-back observables are **strictly $\mathcal{G}_0$-invariant** on $\Omega_0$: for all $g_0 \in \mathcal{G}_0$, $((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}(C_1))[g_0 \cdot U] = W_{\Lambda_1}(C_1)[\pi_{\mathcal{G}}(g_0) \cdot \mathcal{B}_\alpha^{\mathrm{mid}}(U)] = ((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}(C_1))[U]$.

### 3.3 Pushforward Measure $\mu_1$ and Effective Action $S_{\mathrm{eff}}^{(1)}(V)$ (Non-Wilson Structure)
Let $\mu_1^{(\alpha,\kappa)} := (K^{(\alpha,\kappa)}_{0\to 1})_\# \mu_0$ (and $\mu_1^{(\alpha,\infty)} := (\mathcal{B}_\alpha^{\mathrm{mid}})_\# \mu_0$).
1. **For $\kappa \in [0, \infty)$:** $\mu_1^{(\alpha,\kappa)}$ has a strictly positive $C^\infty$ Radon–Nikodym density with respect to $d\mu_{\mathrm{Haar},1}(V)$, defining the exact coarse effective action $S_{\mathrm{eff}}^{(1,\alpha,\kappa)} \in C^\infty(\Omega_1, \mathbb{R})$ (up to an additive constant):
   $$\frac{d\mu_1^{(\alpha,\kappa)}}{d\mu_{\mathrm{Haar},1}}(V) = \frac{1}{Z_{\Lambda_0}(\beta) \, z_N(\kappa)^{|E_+(\Lambda_1)|}} \int_{\Omega_0} \exp\!\left( -S_W(U) + \frac{\kappa}{N} \sum_{e \in E_+(\Lambda_1)} \operatorname{Re}\operatorname{Tr}\!\left(V(e)^\dagger \, \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e)\right) \right) d\mu_{\mathrm{Haar},0}(U) =: \frac{1}{Z_1(\beta)} \exp\!\left( -S_{\mathrm{eff}}^{(1,\alpha,\kappa)}(V) \right).$$
2. **For $\kappa = \infty$ at $\alpha = 0$ ($\mathcal{B}_0^{\mathrm{mid}} = \mathcal{B}^{\mathrm{dec}}_{0\to 1}$):** Partition $E_+(\Lambda_0)$ into the $d L^d$ first-half coaxial links $E_{\mathrm{half},1} = \{ \ell_{e,1} \}$, the $d L^d$ second-half coaxial links $E_{\mathrm{half},2} = \{ \ell_{e,2} \}$, and the remaining $d((2L)^d - 2L^d)$ fine internal links $E_{\mathrm{int}}$. Performing the Haar-measure-preserving change of variables $V(e) = U(\ell_{e,1}) U(\ell_{e,2})$ (with $U(\ell_{e,2}) = U(\ell_{e,1})^\dagger V(e)$) gives:
   $$\frac{d\mu_1^{(0,\infty)}}{d\mu_{\mathrm{Haar},1}}(V) = \frac{1}{Z_{\Lambda_0}(\beta)} \int_{SU(N)^{E_{\mathrm{half},1} \cup E_{\mathrm{int}}}} \exp\!\left( -\left.S_W(U)\right|_{U(\ell_{e,2}) = U(\ell_{e,1})^\dagger V(e)} \right) \prod_{\ell \in E_{\mathrm{half},1} \cup E_{\mathrm{int}}} dU(\ell) =: \frac{1}{Z_1(\beta)} \exp\!\left( -S_{\mathrm{eff}}^{(1,0,\infty)}(V) \right).$$
3. **Why $S_{\mathrm{eff}}^{(1)}(V)$ Does NOT Retain the Single-Plaquette Wilson Form:**
   In $d \ge 2$, each integrated link $U(\ell_{e,1})$ belongs to $2(d-1)$ elementary $a \times a$ plaquettes that share internal edges in $E_{\mathrm{int}}$. Integrating out $E_{\mathrm{half},1} \cup E_{\mathrm{int}}$ via character/cumulant expansion generates:
   - $2a \times 2a$ coarse plaquettes $\operatorname{Re}\operatorname{Tr}(I_N - V_{p_1})$ (at order $\beta^4$),
   - $2a \times 4a$ planar rectangular 6-link coarse loops and non-planar bent 6-link "chair" / "crown" coarse loops,
   - Higher-representation characters $\chi_R(V_{p_1})$ ($R \ne F$) and multi-trace interactions $[\operatorname{Tr}(V_{p_1})]^2$.
   Therefore, **no exact equality $S_{\mathrm{eff}}^{(1)}(V) = S_W(V; \beta_1)$ holds in $d=4$**, and we explicitly forbid assuming that $\mu_1$ is a single-plaquette Wilson measure.

---

## 4. Exact Separation Between Trivial Identities and Substantive Mathematical Theorems

### 4.1 Exact Identities (Zero Inter-Scale Error Content by Themselves)
1. **Identity `ID-OBS-1` (Measure-Theoretic Pushforward–Pullback Duality):**
   For any bounded Borel function $O : \Omega_1 \to \mathbb{C}$,
   $$\langle O \rangle_{\mu_1^{(\alpha,\kappa)}} := \int_{\Omega_1} O(V) \, d\mu_1^{(\alpha,\kappa)}(V) \equiv \int_{\Omega_0} \left( (K^{(\alpha,\kappa)}_{0\to 1})^* O \right)[U] \, d\mu_0(U) =: \left\langle (K^{(\alpha,\kappa)}_{0\to 1})^* O \right\rangle_{\mu_0},$$
   and in the deterministic limit $\kappa = \infty$, $\langle O \rangle_{(\mathcal{B}_\alpha^{\mathrm{mid}})_\# \mu_0} \equiv \langle (\mathcal{B}_\alpha^{\mathrm{mid}})^* O \rangle_{\mu_0}$. This follows directly from the definition of pushforward measure / Fubini's theorem on compact spaces and **is not a Yang–Mills scale-transfer estimate**.
2. **Identity `ID-OBS-2` (Coaxial Associativity Identity at $\alpha = 0$):**
   Because matrix multiplication in $SU(N)$ is associative, $\prod_{k=1}^m (U(\ell_{e_k,1}) U(\ell_{e_k,2})) = \prod_{j=1}^{2m} U(\ell_j)$, so at $\alpha = 0$:
   $$\left( (\mathcal{B}_0^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1) \right)[U] \equiv W_{\Lambda_0,0}^{\mathbb{R}/\mathbb{C}}\!\left(\iota_{\mathrm{loop}}(C_1)\right)[U] \qquad (\forall U \in \Omega_0).$$
3. **Identity `ID-OBS-3` (Exact Midpoint Staple Factorization Into Adjacent $1\times 1$ Plaquettes):**
   For every coarse edge $e = (y, y+2a\hat{\mu})$ and every transverse staple channel $(\nu \ne \mu, \sigma \in \{+,-\})$, let $s_{1,\nu,\sigma}, s_{2,\nu,\sigma} \in SU(N)$ be the $1\times 1$ fine staples around $\ell_{e,1}$ and $\ell_{e,2}$, and let $P_{1,\nu,\sigma} := s_{1,\nu,\sigma}^\dagger U(\ell_{e,1}) \in SU(N)$ and $P_{2,\nu,\sigma} := U(\ell_{e,2}) s_{2,\nu,\sigma}^\dagger \in SU(N)$ be the two $1\times 1$ fine plaquettes based at the midpoint $m(e) = y + a\hat{\mu}$. Because the shared interior transverse link $U(y+a\hat{\mu}, y+a\hat{\mu}+\sigma a\hat{\nu})$ appears as $U_{\mathrm{mid}}^\dagger U_{\mathrm{mid}} = I_N$ in the product $s_{1,\nu,\sigma} s_{2,\nu,\sigma}$, we have the exact configuration-space identities:
   $$s_{1,\nu,\sigma}[U] \, s_{2,\nu,\sigma}[U] \equiv H_0(\gamma_{\nu,\sigma}(e))[U], \qquad L_{\nu,\sigma}(e)[U] = U(\ell_{e,1})^\dagger H_0(\gamma_{\nu,\sigma}(e))[U] U(\ell_{e,2})^\dagger \equiv P_{1,\nu,\sigma}[U]^\dagger \, P_{2,\nu,\sigma}[U]^\dagger.$$

---

### 4.2 Substantive Finite-Lattice Comparison Theorems (`YM-011-OBS-T1`, `YM-011-OBS-T2`, `YM-011-OBS-T3`)

#### Theorem `YM-011-OBS-T1` (Unconditional Pointwise & $L^1(\mu_0)$ Observable-Transfer Bounds on $(\Lambda_0, \Lambda_1)$)
**Statement:** Let $C_1 = (e_1, \dots, e_m)$ be any closed coarse loop of $m = |C_1|_{\Lambda_1}$ coarse edges on $\Lambda_1$ (fine subdivision length $|\iota_{\mathrm{loop}}(C_1)|_{\Lambda_0} = 2m$, physical perimeter $L_{\mathrm{phys}}(C_1) = 2ma$). Then for all $U \in \Omega_0$, all $\alpha \in \mathbb{R}$, and all gradient-flow times $t \ge 0$, both the complex and real normalized Wilson traces satisfy:
1. **Block-Smearing to Unflowed Fine Loop Bound:**
   $$\boxed{\left| \left((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{R}}(C_1)\right)[U] - W_{\Lambda_0,0}^{\mathbb{R}}(\iota_{\mathrm{loop}}(C_1))[U] \right| \le \left| \left((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{C}}(C_1)\right)[U] - W_{\Lambda_0,0}^{\mathbb{C}}(\iota_{\mathrm{loop}}(C_1))[U] \right| \le |\alpha| \, |C_1|_{\Lambda_1} = \frac{|\alpha|}{2} \frac{L_{\mathrm{phys}}(C_1)}{a}.}$$
2. **Block-Smearing to Gradient-Flowed Fine Loop Bound:**
   $$\boxed{\left| \left((\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1)\right)[U] - W_{\Lambda_0,t}^{\mathbb{R}/\mathbb{C}}(\iota_{\mathrm{loop}}(C_1))[U] \right| \le |C_1|_{\Lambda_1} \!\left( |\alpha| + 4(d - 1)\frac{t}{a^2} \right) = \frac{L_{\mathrm{phys}}(C_1)}{2a} \!\left( |\alpha| + 4(d - 1)\frac{t}{a^2} \right),}$$
   and the identical bound holds for the expectations $\left| \langle W_{\Lambda_1}(C_1) \rangle_{(\mathcal{B}_\alpha^{\mathrm{mid}})_\# \mu_0} - \langle W_{\Lambda_0,t}(\iota_{\mathrm{loop}}(C_1)) \rangle_{\mu_0} \right|$ under $\mu_0$.

**Proof:**
Since each $L_{\nu,\sigma}(e_k)[U] \in SU(N)$ has Hilbert–Schmidt norm $\|L_{\nu,\sigma}(e_k)[U]\|_{\mathrm{HS}} = \sqrt{N}$ and $\mathcal{P}_{\mathfrak{su}(N)}$ is the $\mathbb{R}$-orthogonal projection onto $\mathfrak{su}(N)$ with $\|\mathcal{P}_{\mathfrak{su}(N)}\|_{\mathrm{HS}} = 1$, the triangle inequality yields $\|X_{\mathrm{mid}}(e_k)[U]\|_{\mathrm{HS}} \le \frac{1}{2(d-1)} \sum_{\nu,\sigma} \sqrt{N} = \sqrt{N}$.
Differentiating $s \mapsto \mathcal{B}_s^{\mathrm{mid}}(U)(e_k) = U(\ell_{e_k,1}) \exp(s X_{\mathrm{mid}}(e_k)[U]) U(\ell_{e_k,2})$ along $s \in [0, \alpha]$ gives $\frac{d}{ds} \mathcal{B}_s^{\mathrm{mid}}(U)(e_k) = U(\ell_{e_k,1}) X_{\mathrm{mid}}(e_k)[U] \exp(s X_{\mathrm{mid}}(e_k)[U]) U(\ell_{e_k,2})$. Along the $m$-edge coarse holonomy $H_s(C_1) := \prod_{k=1}^m \mathcal{B}_s^{\mathrm{mid}}(U)(e_k)$, the Leibniz rule and Hilbert–Schmidt Cauchy–Schwarz inequality $|\frac{1}{N}\operatorname{Tr}(A B)| \le \frac{1}{N}\|A\|_{\mathrm{HS}}\|B\|_{\mathrm{HS}}$ with $\|\tilde{H}_s^{(k)}\|_{\mathrm{HS}} = \sqrt{N}$ yield:
$$\left| \frac{d}{ds} \left((\mathcal{B}_s^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{C}}(C_1)\right)[U] \right| \le \frac{1}{N} \sum_{k=1}^m \|X_{\mathrm{mid}}(e_k)[U]\|_{\mathrm{HS}} \, \|\tilde{H}_s^{(k)}\|_{\mathrm{HS}} \le \frac{1}{N} m (\sqrt{N})(\sqrt{N}) = m = |C_1|_{\Lambda_1}.$$
Integrating from $s = 0$ (where $(\mathcal{B}_0^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{C}}(C_1) = W_{\Lambda_0,0}^{\mathbb{C}}(\iota_{\mathrm{loop}}(C_1))$ by Identity `ID-OBS-2`) to $s = \alpha$ proves (1). Combining (1) with Theorem `YM-011-PRE-R1` applied to $\iota_{\mathrm{loop}}(C_1)$ of fine link length $n_0 = 2m$ ($|W_{\Lambda_0,t}(\iota_{\mathrm{loop}}(C_1)) - W_{\Lambda_0,0}(\iota_{\mathrm{loop}}(C_1))| \le 2(d-1)(2m)\frac{t}{a^2} = 4(d-1)m\frac{t}{a^2}$) via the triangle inequality proves (2). $\blacksquare$

---

#### Theorem `YM-011-OBS-T2` (Exact Quadratic Plaquette Defect Identity & Small-Field Tangent Cancellation)
**Statement:** Set the scale-matching relation $\alpha(t) := 2(d - 1)\frac{t}{a^2}$ between the transverse block-smearing parameter $\alpha$ and the fine gradient-flow time $t$. For any coarse edge $e = (\ell_{e,1}, \ell_{e,2}) \in E(\Lambda_1)$ in direction $\hat{\mu}$, let
$$Y_{\mathrm{flow}}(e)[U] := \left. a^2 \, U(\ell_{e,1})^\dagger \left( \frac{d}{dt} \left( V_t(\ell_{e,1}) V_t(\ell_{e,2}) \right) \right)\right|_{t=0} U(\ell_{e,2})^\dagger = \sum_{\nu \ne \mu, \, \sigma \in \{+,-\}} \left( \mathcal{P}_{\mathfrak{su}(N)}\!\left(P_{1,\nu,\sigma}[U]^\dagger\right) + \mathcal{P}_{\mathfrak{su}(N)}\!\left(P_{2,\nu,\sigma}[U]^\dagger\right) \right) \in \mathfrak{su}(N)$$
be the midpoint-transported tangent drift of the two-link fine gradient flow at $t = 0$, and let
$$\left. a^2 \, U(\ell_{e,1})^\dagger \left( \frac{d}{dt} \mathcal{B}_{\alpha(t)}^{\mathrm{mid}}(U)(e) \right)\right|_{t=0} U(\ell_{e,2})^\dagger = 2(d - 1) \, X_{\mathrm{mid}}(e)[U] = \sum_{\nu \ne \mu, \, \sigma \in \{+,-\}} \mathcal{P}_{\mathfrak{su}(N)}\!\left( P_{1,\nu,\sigma}[U]^\dagger \, P_{2,\nu,\sigma}[U]^\dagger \right) \in \mathfrak{su}(N)$$
be the midpoint-transported tangent drift of the blocked coarse link at $t = 0$. Then:
1. **Exact Non-Abelian Quadratic Plaquette Defect Identity:** For all $N \ge 2$ and every configuration $U \in \Omega_0$, the linear plaquette excitations cancel identically and the generator difference is given **exactly** by:
   $$\boxed{2(d - 1) \, X_{\mathrm{mid}}(e)[U] - Y_{\mathrm{flow}}(e)[U] \equiv \sum_{\nu \ne \mu, \, \sigma \in \{+,-\}} \mathcal{P}_{\mathfrak{su}(N)}\!\left( \left(P_{1,\nu,\sigma}[U]^\dagger - I_N\right) \left(P_{2,\nu,\sigma}[U]^\dagger - I_N\right) \right).}$$
2. **Quadratic Small-Field Tangent Discrepancy Bound:** For any closed coarse loop $C_1 = (e_1, \dots, e_m)$, the initial tangent discrepancy rate
   $$\Delta_{\mathrm{tan}}(C_1)[U] := \left. a^2 \frac{d}{dt} \right|_{t=0} \left( \left((\mathcal{B}_{\alpha(t)}^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{C}}(C_1)\right)[U] - W_{\Lambda_0,t}^{\mathbb{C}}(\iota_{\mathrm{loop}}(C_1))[U] \right)$$
   satisfies the exact pointwise bound:
   $$\boxed{\left|\Delta_{\mathrm{tan}}(C_1)[U]\right| \le \frac{1}{\sqrt{N}} \sum_{k=1}^m \sum_{\nu \ne \mu_k, \, \sigma \in \{+,-\}} \left\| P_{1,\nu,\sigma}^{(k)}[U] - I_N \right\|_{\mathrm{op}} \, \left\| P_{2,\nu,\sigma}^{(k)}[U] - I_N \right\|_{\mathrm{HS}}.}$$
   In particular, on the Bałaban small-field domain $\Omega_0(\epsilon_{\mathrm{plaq}}) := \left\{ U \in \Omega_0 : \max_{p \in P_+(\Lambda_0)} \|U_p - I_N\|_{\mathrm{op}} \le \epsilon_{\mathrm{plaq}} \right\}$, since $\|U_p - I_N\|_{\mathrm{HS}} \le \sqrt{N}\,\|U_p - I_N\|_{\mathrm{op}} \le \sqrt{N}\,\epsilon_{\mathrm{plaq}}$, we have:
   $$\boxed{\left|\Delta_{\mathrm{tan}}(C_1)[U]\right| \le 2(d - 1) \, |C_1|_{\Lambda_1} \, \epsilon_{\mathrm{plaq}}^2 \qquad \left(\forall U \in \Omega_0(\epsilon_{\mathrm{plaq}})\right),}$$
   exhibiting a strict **quadratic small-field gain $O(\epsilon_{\mathrm{plaq}}^2)$** over the $O(1)$ global worst-case bound $4(d-1)|C_1|_{\Lambda_1}$.

**Proof:**
1. Because $\ell_{e,1}$ and $\ell_{e,2}$ are collinear in direction $\hat{\mu}$, all $2(d-1)$ elementary plaquettes containing $\ell_{e,1}$ lie in planes $(\mu, \nu)$ with $\nu \ne \mu$ and have holonomies $P_{1,\nu,\sigma} = s_{1,\nu,\sigma}^\dagger U(\ell_{e,1})$ based at $m(e)$; similarly all $2(d-1)$ elementary plaquettes containing $\ell_{e,2}$ have holonomies $P_{2,\nu,\sigma} = U(\ell_{e,2}) s_{2,\nu,\sigma}^\dagger$ based at $m(e)$. Under Lüscher's gradient flow $a^2 \partial_t V_t(\ell) = -\mathcal{P}_{\mathfrak{su}(N)}(V_t(\ell) S_\ell(V_t)^\dagger) V_t(\ell)$, transporting $\left.a^2 \partial_t V_t(\ell_{e,1})\right|_{t=0}$ to the right of $U(\ell_{e,1})$ gives $U(\ell_{e,1})^\dagger (-\mathcal{P}_{\mathfrak{su}(N)}(U(\ell_{e,1}) S_{\ell_{e,1}}^\dagger) U(\ell_{e,1})) = -\mathcal{P}_{\mathfrak{su}(N)}(S_{\ell_{e,1}}^\dagger U(\ell_{e,1})) = -\sum_{\nu,\sigma} \mathcal{P}_{\mathfrak{su}(N)}(P_{1,\nu,\sigma}) = +\sum_{\nu,\sigma} \mathcal{P}_{\mathfrak{su}(N)}(P_{1,\nu,\sigma}^\dagger)$. Similarly $\left.a^2 (\partial_t V_t(\ell_{e,2}))\right|_{t=0} U(\ell_{e,2})^\dagger = +\sum_{\nu,\sigma} \mathcal{P}_{\mathfrak{su}(N)}(P_{2,\nu,\sigma}^\dagger)$, proving the formula for $Y_{\mathrm{flow}}(e)[U]$.
2. By Identity `ID-OBS-3`, $L_{\nu,\sigma}(e)[U] = P_{1,\nu,\sigma}^\dagger P_{2,\nu,\sigma}^\dagger$. For any two matrices $A, B \in M_N(\mathbb{C})$, $(A - I_N)(B - I_N) \equiv AB - A - B + I_N$. Since $\mathcal{P}_{\mathfrak{su}(N)}$ is $\mathbb{R}$-linear and $\mathcal{P}_{\mathfrak{su}(N)}(I_N) = 0$, applying $\mathcal{P}_{\mathfrak{su}(N)}$ to $A = P_{1,\nu,\sigma}^\dagger$ and $B = P_{2,\nu,\sigma}^\dagger$ gives:
   $$\mathcal{P}_{\mathfrak{su}(N)}\!\left(P_{1,\nu,\sigma}^\dagger P_{2,\nu,\sigma}^\dagger\right) - \mathcal{P}_{\mathfrak{su}(N)}\!\left(P_{1,\nu,\sigma}^\dagger\right) - \mathcal{P}_{\mathfrak{su}(N)}\!\left(P_{2,\nu,\sigma}^\dagger\right) = \mathcal{P}_{\mathfrak{su}(N)}\!\left(\left(P_{1,\nu,\sigma}^\dagger - I_N\right)\left(P_{2,\nu,\sigma}^\dagger - I_N\right)\right).$$
   Summing over all $2(d-1)$ channels $(\nu \ne \mu, \sigma \in \{+,-\})$ proves (1).
3. Using $\|\mathcal{P}_{\mathfrak{su}(N)}(M)\|_{\mathrm{HS}} \le \|M\|_{\mathrm{HS}}$ and $\|XY\|_{\mathrm{HS}} \le \|X\|_{\mathrm{op}}\|Y\|_{\mathrm{HS}}$, each channel satisfies $\|\mathcal{P}_{\mathfrak{su}(N)}((P_1^\dagger - I_N)(P_2^\dagger - I_N))\|_{\mathrm{HS}} \le \|P_1 - I_N\|_{\mathrm{op}}\|P_2 - I_N\|_{\mathrm{HS}}$. Applying Cauchy–Schwarz along the $m$ coarse edges of $C_1$ with $\frac{1}{N}\|\tilde{H}_0^{(k)}\|_{\mathrm{HS}} = \frac{\sqrt{N}}{N} = \frac{1}{\sqrt{N}}$ yields (2). $\blacksquare$

---

#### Theorem `YM-011-OBS-T3` (Exact Schur Character Factorization & Perimeter Attenuation for Normalized Markov Kernels)
**Statement:** Let $K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U)$ ($\kappa \in [0, \infty)$) be the normalized gauge-covariant Markov transition kernel of Section 2.3, and define the fundamental character coefficient
$$c_F(\kappa) := \frac{1}{N \, z_N(\kappa)} \int_{SU(N)} \operatorname{Re}\operatorname{Tr}(W) \, \exp\!\left(\frac{\kappa}{N}\operatorname{Re}\operatorname{Tr}(W)\right) dW = \frac{d}{d\kappa} \ln z_N(\kappa) \in [0, 1).$$
For any **simple** (edge-self-avoiding) closed coarse loop $C_1 = (e_1, \dots, e_m)$ of length $m = |C_1|_{\Lambda_1}$ on $\Lambda_1$, the Markov kernel pullback satisfies the **exact representation-theoretic factorization**:
$$\boxed{\left( (K^{(\alpha,\kappa)}_{0\to 1})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1) \right)[U] \equiv \left( c_F(\kappa) \right)^{|C_1|_{\Lambda_1}} \left( (\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1) \right)[U] \qquad (\forall U \in \Omega_0),}$$
and consequently:
$$\left| \left( (K^{(\alpha,\kappa)}_{0\to 1})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1) \right)[U] - \left( (\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}^{\mathbb{R}/\mathbb{C}}(C_1) \right)[U] \right| \le 1 - c_F(\kappa)^m \le m \left( 1 - c_F(\kappa) \right).$$
*(For $G = SU(2)$, $z_2(\kappa) = \frac{2 I_1(\kappa)}{\kappa}$ and $c_F(\kappa) = \frac{I_2(\kappa)}{I_1(\kappa)} \in [0, 1)$, where $I_\nu$ are the modified Bessel functions of the first kind.)*

**Proof:**
Since $W \mapsto \exp(\frac{\kappa}{N}\operatorname{Re}\operatorname{Tr}(W))$ is a central class function on the irreducible fundamental representation of $SU(N)$, Schur's Lemma implies $\int_{SU(N)} W \frac{e^{\frac{\kappa}{N}\operatorname{Re}\operatorname{Tr}(W)}}{z_N(\kappa)} dW = c I_N$, and taking $\frac{1}{N}\operatorname{Re}\operatorname{Tr}$ gives $c = c_F(\kappa)$. Changing variables to $V(e_k) = \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e_k) W^\dagger$ gives $\int_{SU(N)} V(e_k) K_e(dV(e_k) \mid U) = c_F(\kappa)\,\mathcal{B}_\alpha^{\mathrm{mid}}(U)(e_k)$. Because $C_1$ is simple, the $m$ coarse edges $\{e_1, \dots, e_m\}$ lie in distinct undirected edge factors of $E_+(\Lambda_1)$, so the integral of $\prod_{k=1}^m V(e_k)$ under the product measure $K^{(\alpha,\kappa)}_{0\to 1}(dV \mid U)$ factors into the product of the single-edge expectations, yielding $c_F(\kappa)^m \prod_{k=1}^m \mathcal{B}_\alpha^{\mathrm{mid}}(U)(e_k)$. $\blacksquare$

---

## 5. Unresolved Mathematical Obstacles and Next Smallest Research Task (`YM-011-PLAQUETTE-EXP`)

### 5.1 Explicitly Preserved Mathematical Obstacles (What `YM-011-OBS-MAP` Does NOT Prove)
1. **Effective-Action Discrepancy (`YM-011-ACT-DEFECT`):**
   While `YM-011-OBS-T1` and `YM-011-OBS-T2` bound the difference between the pulled-back coarse observable $(\mathcal{B}_\alpha^{\mathrm{mid}})^* W_{\Lambda_1}(C_1)$ and the fine observable $W_{\Lambda_0,t}(\iota_{\mathrm{loop}}(C_1))$ **inside the same fine measure $\mu_0$** (which by `ID-OBS-1` equals $\langle W_{\Lambda_1}(C_1) \rangle_{\mu_1^{(\alpha,\infty)}} - \langle W_{\Lambda_0,t}(\iota_{\mathrm{loop}}(C_1)) \rangle_{\mu_0}$), they do **not** bound $\langle W_{\Lambda_1}(C_1) \rangle_{\mu_1^{(\alpha,\infty)}} - \langle W_{\Lambda_1}(C_1) \rangle_{\mu_{\mathrm{Wilson}}(\beta_1)}$ against a single-plaquette Wilson measure on $\Lambda_1$, because $S_{\mathrm{eff}}^{(1)}(V) \ne S_W(V; \beta_1)$.
2. **Expectation of the Quadratic Plaquette Defect Over All of $\Omega_0$:**
   Theorem `YM-011-OBS-T2` proves that $\Delta_{\mathrm{tan}}(C_1)[U]$ is bounded by $\frac{1}{\sqrt{N}} \sum_{k,\nu,\sigma} \|P_{1,\nu,\sigma}^{(k)} - I_N\|_{\mathrm{op}} \|P_{2,\nu,\sigma}^{(k)} - I_N\|_{\mathrm{HS}}$. Converting this pointwise quadratic bound into a quantitative expectation bound in terms of $\beta = 2N/g_0^2$ under $\mu_0$ requires bounding $\langle \|P_1 - I_N\|_{\mathrm{op}} \|P_2 - I_N\|_{\mathrm{HS}} \rangle_{\mu_0}$ via the finite-lattice Wilson plaquette expectation $\langle \frac{1}{N}\operatorname{Re}\operatorname{Tr}(I_N - U_p) \rangle_{\mu_0}$.
3. **No Continuum Limit or Physical Mass Gap Implied:**
   All results in `YM-011-OBS-MAP` hold on finite lattices $(\Lambda_0, \Lambda_1)$ of fixed spacings $a$ and $2a$. They do not establish a continuum limit $a \to 0$, do not identify Markov generator gaps with physical Hamiltonian gaps, and do not establish a physical mass gap (`GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`).

### 5.2 Next Smallest Authorized Research Task (`YM-011-PLAQUETTE-EXP`)
- **Task ID:** `YM-011-PLAQUETTE-EXP` (`Finite-Lattice Gibbs Expectation Bound for the Quadratic Plaquette Tangent Defect`)
- **Objective:** Using the exact Hilbert–Schmidt identity $\|U_p - I_N\|_{\mathrm{HS}}^2 = 2N\left(1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p)\right)$ for $U_p \in SU(N)$ and the Cauchy–Schwarz / translation-invariance properties of the finite-lattice Wilson Gibbs measure $\mu_0$ on $\Lambda_0$, derive and verify an explicit upper bound on $\left\langle \left|\Delta_{\mathrm{tan}}(C_1)\right| \right\rangle_{\mu_0}$ in terms of the mean plaquette energy $e_{\mathrm{plaq}}(\beta, \Lambda_0) := \left\langle 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \right\rangle_{\mu_0}$ and the finite-lattice Schwinger–Dyson / Brascamp–Lieb plaquette bound.
