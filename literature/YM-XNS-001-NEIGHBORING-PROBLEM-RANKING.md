# YM-XNS-001: Neighboring-Problem Ranking — The Yang–Mills Analogue of “Euler First”

## 1. The “Euler First” Precursor Principle

In the Navier–Stokes breakthrough, the decisive strategic milestone was not attacking 3D viscous Navier–Stokes directly, but first constructing blow-up for **3D incompressible Euler** (and simpler active scalar equations such as Boussinesq and IPM):
$$\underbrace{\partial_t u + (u \cdot \nabla)u + \nabla p = f}_{\text{Euler: Inviscid, Nonlinear Convection}} \quad \xrightarrow{\text{Transfer}} \quad \underbrace{\partial_t u + (u \cdot \nabla)u - \nu \Delta u + \nabla p = f}_{\text{Navier–Stokes: Convection + Viscous Dissipation}}$$

The Euler precursor achieved three vital objectives:
1. It eliminated the damping effect of viscosity ($\nu \Delta u$), isolating pure nonlinear vortex stretching.
2. It proved that smooth forcing $f$ could overcome geometric dispersion and pump energy into high frequencies.
3. It established the localized layer iteration architecture before introducing the balancing terms needed for diffusion.

**The Strategic Question for Yang–Mills:**  
What is the structural analogue of "Euler First" for the 4D Yang–Mills Millennium Problem? Which neighboring mathematical regime removes one primary obstruction while preserving the core mechanism necessary for the full Clay target?

---

## 2. Exhaustive Audit of Candidate Neighboring Regimes

### Candidate 1: Fixed Lattice Gauge Theory ($a > 0$, Compact $G$, $d = 4$)
- **Description:** Wilson lattice gauge theory on $a \mathbb{Z}^4$ with Haar measure on compact Lie group $G$.
- **Clay Obligation Made Easier:**
  - Ultraviolet divergence is completely eliminated by the lattice cutoff $a > 0$.
  - Gauge invariance is exact and non-perturbative on every link.
  - Spectral mass gap is rigorously proved at strong coupling ($\beta = 2N/g^2 \ll 1$, Wilson 1974, Shen–Zhu–Zhu 2023).
- **Clay Obligation Remaining Intact:**
  - Thermodynamic limit ($V \to \infty$) must still be controlled (solved at strong coupling via cluster expansion).
  - Reflection positivity (Osterwalder–Schrader OS3) holds on lattice hyperplanes.
- **Obstruction Removed:** Ultraviolet infinities; continuum renormalization.
- **Essential Structure Preserved:** Non-Abelian gauge symmetry, non-perturbative Wilson loops, confinement area law.
- **What Theorem Transfers Back:** Existence of an isolated strictly positive spectral gap $\Delta > 0$ on the lattice Hamiltonian.
- **Transfer Theorem Required:** **Continuum Scaling Limit ($a \to 0$, $\beta \to \infty$)**. Asymptotic freedom dictates $g(a) \to 0$ as $a \to 0$. Proving the mass gap survives the weak-coupling continuum limit without collapsing ($\Delta_{\text{phys}} = \lim_{a \to 0} \frac{\Delta(a)}{a} > 0$) is the entire Clay barrier!
- **Structural Closeness Score:** **HIGH (Tier 2)**. The lattice theory is an exact regularized discretization of the true theory, preserving OS3 and gauge invariance.

---

### Candidate 2: Constructive Euclidean YM with Infrared Mass Cutoff ($\mu > 0$, Continuum, $d = 4$)
- **Description:** 4D continuum Euclidean Yang–Mills with an artificial mass term or infrared cutoff (Magnen–Rivasseau–Sénéor 1993, `THM-YM-0020`).
- **Clay Obligation Made Easier:**
  - Infrared divergence and infinite-volume clustering are controlled because the gluon propagator has an effective mass $\mu > 0$.
  - UV stability is controlled via multiscale cluster expansion.
- **Clay Obligation Remaining Intact:**
  - 4D continuum spacetime; local field construction; OS reconstruction.
- **Obstruction Removed:** Infrared renormalons; infrared clustering breakdown.
- **Essential Structure Preserved:** Continuous Euclidean symmetry $SO(4)$, continuum spacetime, non-Abelian interaction.
- **What Theorem Transfers Back:** Existence of non-trivial 4D continuum Schwinger functions satisfying OS0, OS1, OS2.
- **Transfer Theorem Required:** **Removal of the Infrared Cutoff ($\mu \to 0$)**. One must prove that the theory develops a dynamical mass gap so that Schwinger functions remain non-singular as the bare cutoff $\mu$ is sent to zero.
- **Structural Closeness Score:** **HIGHEST (Tier 1 — Best Analogue)**. This is in the continuum in 4 dimensions, retains non-Abelian symmetry, and requires only removing the IR regulator.

---

### Candidate 3: Finite Volume Multiscale Continuum ($V < \infty$, Continuum, $d = 4$)
- **Description:** Bałaban's renormalization group program on a finite torus $\mathbb{T}^4$ or cube of size $L$ (`THM-YM-0016`–`THM-YM-0018`).
- **Clay Obligation Made Easier:**
  - Thermodynamic infrared divergences are absent due to finite volume $L < \infty$.
  - Ultraviolet stability is rigorously proved via multi-scale block-spin averaging.
- **Clay Obligation Remaining Intact:**
  - Continuum limit ($a \to 0$) is rigorously achieved in finite volume!
  - Local gauge invariance and Euclidean covariance are controlled.
- **Obstruction Removed:** Infinite-volume infrared growth and cluster decomposition.
- **Essential Structure Preserved:** Full 4D continuum non-Abelian gauge fields, asymptotic freedom, running coupling constant.
- **What Theorem Transfers Back:** The Bałaban effective actions $S_k(A)$ and partition function bounds in the UV limit.
- **Transfer Theorem Required:** **Infinite-Volume Limit ($L \to \infty$) with Uniform Exponential Decay**. The thermodynamic limit requires controlling the large-field regions at large volume without letting the mass gap vanish.
- **Structural Closeness Score:** **HIGHEST (Tier 1 — Equal Best Analogue)**. Together with Candidate 2, this forms the natural continuum precursor.

---

### Candidate 4: Lower-Dimensional Gauge Theories ($d = 2, 3$)
- **Description:** 2D Yang–Mills (trivial, no propagating degrees of freedom) or 3D Yang–Mills / Georgi–Glashow model (Polyakov 1977, Göpfert–Mack 1981).
- **Clay Obligation Made Easier:**
  - 3D Yang–Mills is super-renormalizable (UV is soft; no running coupling in the UV).
  - In 3D compact $U(1)$ or broken $SU(2)$, instantons/monopoles form a dilute Coulomb gas with Debye screening, rigorously generating a mass gap (`THM-YM-0011`, `THM-YM-0013`).
- **Clay Obligation Remaining Intact:**
  - Continuum limit, confinement, spectral gap.
- **Obstruction Removed:** Marginal 4D ultraviolet renormalons; 4D scale anomaly.
- **Essential Structure Preserved:** Gauge invariance, non-perturbative mass generation.
- **What Theorem Transfers Back:** Mechanism of topological charge condensation / monopole screening.
- **Transfer Theorem Required:** **Dimensional Continuation $3D \to 4D$**. In 4D, instantons have zero engineering dimension and scale logarithmically; dilute gas approximations fail due to scale-invariant instanton size distribution (infrared instanton catastrophe).
- **Structural Closeness Score:** **MODERATE (Tier 3)**. Lower dimensions change the fundamental UV scaling character (super-renormalizable vs strictly renormalizable).

---

### Candidate 5: Classical Yang–Mills PDE (Cauchy Problem on $\mathbb{R}^{3+1}$)
- **Description:** Classical nonlinear hyperbolic PDE: $D^\mu F_{\mu\nu} = 0$.
- **Clay Obligation Made Easier:**
  - No path integrals, no Hilbert space, no quantum fluctuations, no operator-valued distributions.
- **Clay Obligation Remaining Intact:**
  - Nonlinear non-Abelian field equations.
- **Obstruction Removed:** Quantum measurement, operator positivity, renormalization.
- **Essential Structure Preserved:** Classical gauge symmetry.
- **What Theorem Transfers Back:** None.
- **Critical Discrepancy:** In 4D Minkowski spacetime, classical Yang–Mills has **global smooth solutions for all smooth initial data** (Eardley–Moncrief 1982). There is *no* finite-time blowup in classical 4D Yang–Mills! Furthermore, classical Yang–Mills is scale-invariant and has **no mass gap**.
- **Structural Closeness Score:** **LOWEST (Tier 4 — False Analogue)**. The mass gap is an exclusively quantum, non-perturbative phenomenon.

---

## 3. Structural Closeness Ranking Table

| Rank | Neighboring Problem Candidate | Dimension & Space | Primary Difficulty Removed | What Must Be Transferred Back | Structural Closeness to Clay Target |
|---|---|---|---|---|---|
| **1** | **Finite-Volume Continuum (Bałaban)** | $d=4$, $\mathbb{T}^4$ | Infinite volume / IR barrier | Thermodynamic limit $L \to \infty$ with uniform gap | **0.90 (Tier 1: Best Match)** |
| **2** | **Continuum YM with IR Mass Cutoff (MRS)** | $d=4$, $\mathbb{R}^4$, $\mu > 0$ | Infrared renormalons / mass generation | Removal of mass cutoff $\mu \to 0$ | **0.88 (Tier 1: Best Match)** |
| **3** | **Fixed-Lattice Gauge Theory (Wilson)** | $d=4$, $a \mathbb{Z}^4$ | UV divergence / renormalization | Continuum limit $a \to 0$ at weak coupling | **0.75 (Tier 2: Discretized)** |
| **4** | **3D Gauge Theories with Monopoles** | $d=3$, $\mathbb{R}^3$ | 4D marginal scaling / logarithmic running | 4D instanton size integration control | **0.50 (Tier 3: Dimensional Analogue)** |
| **5** | **Planar Large-$N$ Master Field** | $d=4$, $N = \infty$ | Non-planar Feynman topologies | Finite-$N$ $1/N$ corrections | **0.40 (Tier 3: Truncated Model)** |
| **6** | **Classical Yang–Mills PDE** | $d=3+1$, Classical | Quantum fluctuations / distributions | Entire quantum path integral & spectrum | **0.10 (Tier 4: Category Error)** |

---

## 4. Strategic Recommendation for the Yang–Mills Programme

The true Yang–Mills analogue of "Euler First" is:

$$\boxed{\textbf{Bałaban Finite-Volume UV Control} \quad + \quad \textbf{Magnen–Rivasseau–Sénéor IR Mass Regulator}}$$

**Strategic Insight:**  
Just as the fluid dynamics breakthrough first built the blow-up mechanism in Euler without viscosity, the Yang–Mills programme should formulate the mass-gap mechanism in the **4D continuum with an infrared regulator ($\mu > 0$ or finite $L$)**, where UV asymptotic freedom is rigorously proved, and isolate the exact transfer theorem required to take $\mu \to 0$ (or $L \to \infty$) while bounding the spectral gap strictly from below.
