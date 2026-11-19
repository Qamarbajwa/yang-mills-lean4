# Why Nuclear Glue Has Weight While Light Flies Free: A Plain-English Guide to Our 4D Yang–Mills Measurements

**Author:** Qamar Munawer (Brandenburg University of Technology (BTU) Cottbus–Senftenberg)  
**Repository:** `Qamarbajwa/yang-mills-lean4` (`YM101`–`YM182`, Probes 1–6)  
**Status:** All `YM101`–`YM182` Lean 4 certificates compile with zero unexpected axioms; the full infinite-volume continuum Clay Millennium Problem ($L \to \infty, a \to 0$) remains **OPEN**.

---

## 1. The Everyday Question Behind the Million-Dollar Problem

Think about two invisible forces in our universe:
1. **Light (Electromagnetism, called $U(1)$):** A flashlight beam can travel across billions of light-years of empty space without slowing down or fading into heavy chunks, because photons have **zero mass**.
2. **Nuclear Glue (Strong Force, called $SU(2)$ / Yang–Mills):** Inside every proton and neutron in your body, force particles called **gluons** carry the nuclear force. Yet you never see a lone gluon flying across your room. They lock together at subatomic distances and behave as if there is a minimum energy cost—a **mass gap ($\Delta > 0$)**—needed to create even the lightest excitation.

The **Clay Yang–Mills Millennium Problem** asks for a complete mathematical proof that pure 4D non-Abelian gauge theory exists on continuous spacetime ($\mathbb{R}^4$) and always has a strictly positive mass gap $\Delta > 0$ for every compact simple gauge group $G$.

---

## 2. Three Real-World Analogies for How We Measure It

### Analogy A: The Tared Kitchen Scale ("Seeing Negatively")
Suppose you want to weigh a pinch of saffron inside a heavy iron bowl. If you put the bowl and saffron on a scale together and read `65.4505` grams, you haven't weighed the saffron—you weighed the iron bowl!

In 4D lattice physics, when you clamp the walls of a tiny $2 \times 2 \times 2 \times 2$ ($2^4$) spacetime box, **even massless light ($U(1)$)** shows a huge fake stiffness of **`65.4505`** (with minimum eigenvalue `4.0000`) because long light waves cannot fit inside a clamped box.
- **What it is called:** The **Dirichlet Cavity Mirage** (removed by **Abelian Subtraction** / the **Schur Complement**).
- **How we measure it:** We put the $U(1)$ baseline "bowl" on the scale at the exact neutral blocking weight $\alpha^* = 0.188$ and press **TARE / ZERO**. Once subtracted, the fake `65.4505` vanishes to **`0.000000000000000`** (`<= 1.5e-14`), leaving only the true non-Abelian difference.

### Analogy B: A Compass Needle vs. a 3D Spinning Top
Why does light ($U(1)$) stay massless while nuclear glue ($SU(2)$) locks up?
- A **compass needle** ($U(1)$) only rotates in one flat circle (1D). Moving 30 degrees clockwise and 20 degrees counterclockwise always commutes—walk around a square loop and the needle returns pointing the exact same way.
- A **3D spinning top or airplane** ($SU(2)$ or $SO(3)$) rotates in three dimensions. Pitching up and rolling right is *not* the same as rolling right and pitching up! Walk around a $2 \times 2$ spacetime loop and the orientation twists.
- **What it is called:** The **Adjoint Area Cocycle Dispersion ($\delta_{2\times 2}$)** (`0` = no twist; `1` = maximum directional scrambling).
- **What we observed:**
  - In **massless light $U(1)$**, $\delta_{2\times 2} = \mathbf{0.0000}$ everywhere.
  - In **non-Abelian $SU(2)$ and $SO(3)$**, $\delta_{2\times 2}$ jumps to **`0.4740`–`1.0023`**, locking directly to the negative magnetic pull.

### Analogy C: Two Magnets Inside a Box (Diamagnetic Push vs. Paramagnetic Pull)
Inside each $2^4$ spacetime box, the remaining non-Abelian energy splits into two competing pieces:
1. **Orbital Motion ($\Delta F_{\mathrm{diam}}/d$, Diamagnetic Screening):** Like electrons circling a wire, orbital motion pushes energy slightly *upward* (trying to weaken the force).
2. **Spin-1 Magnetic Pull ($F_{\mathrm{para}}/d$, Paramagnetic Schur Complement):** Because gluons themselves carry spin-1 color charge, they grab onto neighboring magnetic fields and pull energy *downward*.

- **What it is called:** **Paramagnetic Schur Dominance** ($C_{\mathrm{dom}} := |F_{\mathrm{para}}| / \Delta F_{\mathrm{diam}}$) and **Gribov-Horizon Clearance** ($\lambda_{\min}(I + K_{\mathrm{para}}) = 1 - \|K_{\mathrm{para}}\|_{\mathrm{op}} > 0$).
- **What we observed across all `720/720` non-Abelian $2^4$ blocks (Probes 4–5):**
  - Diamagnetic push: **`+0.0071` to `+0.0232`** (weak, positive).
  - Paramagnetic pull: **`-0.2011` to `-0.3774`** (strong, negative).
  - Dominance ratio: **$13.47\times$ minimum** (`16.2x` to `28.9x` mean).
  - Gribov clearance: $\|K_{\mathrm{para}}\|_{\mathrm{op}} \le \mathbf{0.4346} < 1$, so $\lambda_{\min}(I + K_{\mathrm{para}}) \ge \mathbf{0.5654} > 0$ (never hits a zero-mode singularity).

---

## 3. Dictionary of Measurements: What Each Metric Is Called, How It Is Measured & What We Observed

| Plain-English Name | Technical Name | How It Is Measured | Observed Value |
| --- | --- | --- | --- |
| **Neutral Zoom Weight** | $\alpha^* = 0.188$ (Scale-neutral blocking weight) | Tuned on massless 4D $U(1)$ ($\beta = 2.00$) until zooming out ($b = 2 \to 4$) gives zero fake running. | $\Delta\beta_{2\times}^{U(1)} = \mathbf{+0.001 \pm 0.025}$ |
| **Fake Wall Stiffness** | $F_{\mathrm{Ab}0}/d$ (Dirichlet cavity free energy) | Free energy of a clamped $2^4$ box in pure $U(1)$; subtracted as the "tare" bowl. | **`65.4505`** $\to$ **`0.0`** after subtraction |
| **Magnetic Pull vs. Push** | $F_{\mathrm{para}}/d$ vs. $\Delta F_{\mathrm{diam}}/d$ | Exact block-Schur determinant $\frac{1}{2d}\mathrm{Tr}\ln(I + K_{\mathrm{para}})$ (`SchurErr <= 1.5e-14`). | **`-0.3774..-0.2011`** vs. **`+0.0071..+0.0232`** ($C_{\mathrm{dom}} \ge 13.47\times$) |
| **Loop Twist Meter** | $\delta_{2\times 2}(X)$ (2D area cocycle dispersion) | Average rotational mismatch $1 - \hat{n}\cdot R(U_{2\times 2})\hat{n}$ around a $2\times 2$ spacetime loop. | $U(1)$: **`0.0000`**; $SU(2)$: **`0.868`–`1.002`** |
| **Running Coupling Shift** | $\Delta\beta_{\mathrm{rel}}$ (Matched-$3^4$ SD shift) | Change in effective coupling when zooming $b = 2 \to 4$ on matched $3^4$ grids minus $U(1)$. | $SU(2)(4.00)$: **`-0.269`** (Swendsen) / **`-0.8245`** (matched SD) |
| **Messy Higher-Loop Noise** | $\varepsilon_k = \|R^{(k)}\|$ (Multi-plaquette remainder) | Excess of $1\times 2$ rectangles and $2\times 2$ bent chairs over single-plaquette $\langle P\rangle^2$ minus $U(1)$. | **`0.014`–`0.058`**; ratio $\varepsilon_2/|\Delta\beta_{\mathrm{rel}}| \in \mathbf{[0.0163, 0.1202]} \ll 0.5654$ |
| **Safe Margin From Blow-Up** | $\lambda_{\min}(I + K_{\mathrm{para}})$ (Gribov clearance) | Smallest eigenvalue of $I + K_{\mathrm{para}}$ across all $720$ non-Abelian $2^4$ blocks. | $\ge \mathbf{0.5654} > 0$ ($\|K_{\mathrm{para}}\|_{\mathrm{op}} \le 0.4346$) |
| **Coarse Wave Contraction** | $\Gamma_{\ge 1}^{\mathrm{BLK}}$ (Block-transfer weight) | Decay of fattened $1^{+-}$ spatial block correlators at crossover. | $SU(2)(2.30)$: **`0.003`**; $SU(2)(4.00)$: `0.422` $\to$ **`0.302`** |

---

## 4. What We Proved in Lean 4 (`YM101`–`YM182`) vs. What Remains Open

Every mathematical lemma we built is checked by the **Lean 4 proof assistant** (`3,012` build jobs, zero `sorry`, zero `admit`, zero custom axioms—strictly `[propext, Classical.choice, Quot.sound]`):

1. **Completed in Lean 4 (`YM101`–`YM182`):**
   - `YM101`–`YM175`: UV polymer contraction, Killing–Cartan / Weyl–Coxeter closure for all compact simple Lie groups (including centerless $G_2, F_4, E_8$), Kotecky–Preiss collar decoupling, Lieb–Loss bathtub floors, and reflection-positive `OSHilbert` space.
   - `YM176`: Trace-zero identity $\mathrm{Tr}(K_{\mathrm{para}}) = 0$, 4th-order rational sandwich, $C_{\mathrm{dom}} \ge 13.47$, and cocycle floor $\ge 1.3407\,\delta_{2\times 2}$.
   - `YM177`: Two-variable inductive RG contraction showing that whenever remainder damping $\theta_{\mathrm{Schur}} < 1$ holds, any UV trajectory starting at arbitrarily large $\beta_0$ enters the crossover basin in $\mathcal{O}(\beta_0)$ steps with uniformly bounded remainder $\varepsilon_k \le \varepsilon_{\max}$.
   - `YM178`: Exact calculus proof (`HasDerivAt`) of the 4th-order `Real.log (1 + λ)` Taylor sandwich and deterministic small-field Gribov clearance.
   - `YM179`–`YM182`: Small/large-field Peierls Gibbs split, $\mathcal{O}(1/\beta_k)$ cocycle descent, and end-to-end wiring into `YM151` (`OSHilbert`), `YM-REQ-001` (universal simple Lie groups), and `YM127` (short-distance OPE non-triviality).

2. **What Remains Open (The Honest Clay Frontier — Hypothesis 4.1):**
   Proving **unconditionally on the true infinite-volume continuum ($a \to 0, L \to \infty$) 4D Wilson Gibbs measure** across the crossover ($g_{\mathrm{eff}}^2 \sim 1$) that:
   - large-field Peierls probabilities stay exponentially suppressed down to $\beta_{\mathrm{basin}} = \mathcal{O}(1)$,
   - the renormalized cocycle expectation obeys $\mathbb{E}[\delta_{2\times 2}^{(k)}] \ge c_{\mathrm{coc}}/\beta_k$ uniformly in $L$, and
   - coarse-slice contraction $\Gamma_{\mathrm{blk}} < 1$ survives the joint $(a \to 0, L \to \infty)$ limit.

That final analytic bridge is the **unsolved Clay Millennium Problem** itself—isolated cleanly and honestly inside Hypothesis 4.1.
