# YM-005 Area Law vs. Mass Gap Audit

## 1. Executive Invariant Identification

$$\boxed{\textbf{INV-YM005-002: } \text{WILSON_AREA_LAW } \langle W(C) \rangle \le C e^{-\sigma \cdot \text{Area}(C)} \ne \text{SPECTRAL_MASS_GAP } \Delta > 0}$$

In mathematical gauge theory, the confinement of static quarks (probed by the Wilson loop area law) and the existence of a spectral mass gap (probed by the Hamiltonian transfer matrix or exponential decay of local gauge-invariant operators) are frequently conflated in informal physical discourse. Under **ROS v1.0**, they represent distinct mathematical propositions that require independent proof.

---

## 2. Mathematical Definitions of the Two Phenomena

### 2.1 The Wilson Loop and the Area Law
Let $C$ be a simple closed rectifiable planar loop on the lattice $\Lambda \subset a \mathbb{Z}^4$ bounding a planar surface $S$ of minimal area $\text{Area}(C)$.
The normalized Wilson loop functional in representation $r$ is:
$$W_r(C) = \frac{1}{d_r} \text{Tr}_r \left( \prod_{\ell \in C} U_\ell \right)$$
A gauge theory exhibits an **area law** for representation $r$ if there exist constants $C > 0$ and $\sigma_r > 0$ (the **string tension**) such that:
$$\langle W_r(C) \rangle_\mu \le C \exp\left( - \sigma_r \cdot \text{Area}(C) \right) \quad \forall C$$
The static quark–antiquark potential is extracted as the large-time limit of a rectangular loop $R \times T$:
$$V_r(R) = \lim_{T \to \infty} -\frac{1}{T} \ln \langle W_r(R \times T) \rangle_\mu \ge \sigma_r R - \text{const}$$
Thus, an area law implies a strictly linear confining potential at large distances ($V(R) \sim \sigma R$).

### 2.2 The Spectral Mass Gap
Let $H$ be the physical Hamiltonian operating on the physical Hilbert space $\mathcal{H}_{\text{phys}}$ with unique vacuum $|\Omega\rangle$ ($H |\Omega\rangle = 0$).
The theory possesses a **spectral mass gap** $\Delta > 0$ if:
$$\text{spec}(H) \subseteq \{0\} \cup [\Delta, \infty)$$
Equivalently, in Euclidean space, for every local gauge-invariant field operator $O(x)$ (e.g. plaquette actions, $F_{\mu\nu}^2(x)$, or glueball interpolators) satisfying $\langle \Omega, O \Omega \rangle = 0$:
$$|\langle O(x) O(y) \rangle| \le C_O \exp(-\Delta |x - y|) \quad \forall x, y$$

---

## 3. Mathematical Decoupling: Non-Implication in Both Directions

The area law and the spectral mass gap are mathematically independent:

```text
               Area Law: <W(C)> <= e^{-sigma Area(C)}
                      /                 \
        (does NOT imply)               (does NOT imply)
                    /                     \
                   v                       v
      Spectral Mass Gap: spec(H) in {0} U [Delta, infty)
```

### 3.1 Counterexample 1: Area Law Without Continuum Dynamical Mass Gap (2D Yang–Mills)
- In $d = 2$ spacetime dimensions, pure Yang–Mills theory has an exact, rigorously proved area law for all Wilson loops:
  $$\langle W_F(C) \rangle = \exp\left( - \frac{1}{2} g^2 C_F \cdot \text{Area}(C) \right)$$
  for any compact gauge group $G$ (Migdal 1975, Witten 1991, Fine 1990).
- However, 2D Yang–Mills has **zero propagating local degrees of freedom**: the field strength tensor $F_{01}$ has no transverse components ($d-2 = 0$). The local glueball Hilbert space is trivial, and there are no local dynamical particles in the continuum.
- Thus, an exact area law exists with non-zero string tension ($\sigma = \frac{1}{2} g^2 C_F > 0$), yet there is no non-trivial 4D-type particle spectrum or non-trivial local Wightman field theory.

### 3.2 Counterexample 2: Spectral Mass Gap Without Area Law (Higgs Phase / Screening)
- Consider $SU(2)$ or compact $U(1)$ gauge theory coupled to fundamental scalar matter (the Fradkin–Shenker model, 1979):
  $$\mathcal{L} = \frac{1}{4} F_{\mu\nu}^2 + |D_\mu \phi|^2 + V(|\phi|)$$
- In the Higgs / strong-screening regime, the theory possesses a rigorously proved strictly positive spectral mass gap ($\Delta > 0$): both vector bosons and Higgs scalars are massive (Osterwalder–Seiler 1978, Fradkin–Shenker 1979).
- However, the Wilson loop exhibits a **perimeter law**:
  $$\langle W_F(C) \rangle \sim \exp\left( - \mu \cdot \text{Perimeter}(C) \right)$$
  because the dynamical fundamental matter fields screen the external test charges, causing the confining flux tube to break once the energy exceeds $2 M_{\text{meson}}$ ($V(R) \to \text{const}$ as $R \to \infty$).
- Thus, a strictly positive spectral mass gap $\Delta > 0$ exists, yet the area law is strictly **false**.

---

## 4. Rigorous Audit of Cao–Nissim–Sheffield (2025)

In 2025, Y. Cao, E. Nissim, and S. Sheffield posted two major mathematical preprints on lattice Yang–Mills:
1. *"Expanded Regimes of Area Law for Lattice Yang-Mills Theories"* (`arXiv:2505.16585`, `PAPER-MOD-008` / `THM-YM-0028`)
2. *"A Dynamical Approach to Lattice Yang-Mills in the 't Hooft Limit"* (`arXiv:2505.16586`, `PAPER-MOD-009` / `THM-YM-0029`)

### 4.1 Reconstructed Mathematical Achievements
- **Technique:** Random surface representations and stochastic couplings on discrete lattices. A Wilson loop expectation is represented as a partition function over random branched surfaces bounded by $C$.
- **Theorem (arXiv:2505.16585, Theorems 1.1–1.4):**
  For classical Lie groups $G = SU(N), SO(N), Sp(N)$ on a fixed hypercubic lattice $\Lambda = a \mathbb{Z}^d$ ($d \ge 2$), there exists an explicit parameter threshold $\beta_1(d, G) > \beta_0(d, G)$ such that for all bare couplings $\beta \in [0, \beta_1)$:
  $$\langle W(C) \rangle \le C \exp(-\sigma(\beta) \cdot \text{Area}(C))$$
  with an explicit positive lower bound on the string tension:
  $$\sigma(\beta) \ge \sigma_0(\beta) > 0$$
- **Advancement:** Extends the rigorous parameter domain of the Wilson loop area law significantly beyond the standard convergence radius $\beta_0$ of character cluster expansions.

### 4.2 Epistemic Limitations and Clay Non-Sufficiency
In accordance with `INV-YM005-002`, the Cao–Nissim–Sheffield theorems are subject to strict mathematical boundaries:
1. **Discrete Lattice Only:** The results are strictly confined to a fixed lattice spacing $a > 0$. They do not control the continuum limit $a \to 0$.
2. **Dimensionless String Tension:** The string tension $\sigma(\beta)$ is dimensionless. In physical units, the physical string tension is:
   $$\sigma_{\text{phys}} = \frac{\sigma(\beta(a))}{a^2}$$
   Taking $a \to 0$ requires establishing the non-perturbative scaling $\sigma(\beta(a)) \sim a^2 \Lambda_{\text{QCD}}^2 \sim \exp(-1 / (b_0 g^2))$. Cao–Nissim–Sheffield does **not** prove this scaling trajectory.
3. **Area Law $\ne$ Continuum Mass Gap:** The theorems establish upper bounds on loop expectations $\langle W(C) \rangle$. They do **not** construct the physical Hilbert space $\mathcal{H}$, do not bound the spectrum of the local Hamiltonian $H_{\text{lat}}$ in the glueball sector, and do not prove that $\Delta_{\text{continuum}} > 0$ in 4D Minkowski spacetime.

```text
Cao–Nissim–Sheffield (2025)
[0 ─────────────── beta_1]  ───────── ? ───────── [beta -> infinity]
  EXPANDED AREA LAW        UNBRIDGED CROSSOVER       CONTINUUM LIMIT
   (Wilson Loops)          (Scaling Unknown)        (Clay Target)
```
