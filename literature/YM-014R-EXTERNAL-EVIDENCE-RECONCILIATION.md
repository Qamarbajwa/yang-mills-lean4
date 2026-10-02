# YM-014R-EXTERNAL-EVIDENCE-RECONCILIATION: Re-Audit of Finite-N Loop Bootstrap and Random-Surface Obstructions Against Primary Literature

- **TASK_ID:** `YM-014R`
- **OBJECTIVE:** External-Evidence Reconciliation and Obstruction-Theorem Repair
- **MISSING_BRIDGE_EDGE:** `E-CROSSOVER`
- **GOVERNANCE_STATUS:** Authoritative Reconciliation Artifact (Post-Acceptance Amendment)
- **DATE:** 2026-10-02
- **PRECURSOR_REVISION:** 29 (HEAD `25278d6`)

---

## 1. Executive Summary

This document executes the mandatory scientific reconciliation mandated by governance after comparing the internal obstruction theorems proved in Tasks `YM-013` and `YM-014` against primary literature:
1. Vladimir Kazakov and Zechuan Zheng, *"Bootstrap for finite N lattice Yang-Mills theory,"* JHEP 03 (2025) 099 (arXiv:2404.16925).
2. Xizhe Liu and Gang Yang, *"Direct and indirect loop equations in lattice Yang-Mills theory,"* JHEP 04 (2026) 107.
3. Robert Oeckl and Hendryk Pfeiffer, *"The dual of pure non-Abelian lattice gauge theory as a spin foam model,"* Nucl. Phys. B 598 (2001) 400.
4. G. Mack and V. B. Petkova, *"Sufficient condition for confinement of static quarks by a lattice gauge field,"* Ann. Phys. 123 (1979) 442; E. T. Tomboulis, *"Permanence of confinement in SU(2) gauge theory,"* Phys. Rev. D 23 (1981) 2371.

### Key Reconciliation Findings
1. **The $SU(2)$ Multi-Trace Contradiction (Repair of Theorem `YM-013-T1`):**  
   In `YM-013-T1`, the project claimed that finite-$N$ non-factorization produces an infinite, non-closing BBGKY-type multi-trace hierarchy for all finite $N$.  
   *Correction:* In $SU(2)$, the trace identity $\operatorname{Tr}(U) = \operatorname{Tr}(U^\dagger) \in \mathbb{R}$ forces the loop-splitting term $\operatorname{Tr}(U_p - U_p^\dagger) \equiv 0$ identically at the operator level. Consequently, the lattice Makeenko–Migdal loop equations for $SU(2)$ are **linear and close strictly within the space of single-trace Wilson loops**. The multi-trace proliferation obstruction does NOT apply to $SU(2)$ single-trace loop equations. Theorem `YM-013-T1` is **REFUTED for $SU(2)$** and classified as **`NEEDS_AMENDMENT`**.
2. **Perimeter Explosion vs. Indirect Loop Equations (Repair of Theorem `YM-013-T2`):**  
   In `YM-013-T2`, the project claimed that Mandelstam reduction converts multi-trace proliferation into an exponential perimeter explosion.  
   *Correction:* As established by Liu & Yang (2026), one can formulate *indirect loop equations* using a vertex-filtering strategy that eliminates higher-length intermediate loops, generating closed linear constraints without intermediate perimeter explosions. Theorem `YM-013-T2` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (applies to naive loop concatenation, but indirect equations bypass intermediate perimeter blow-ups).
3. **Fixed Truncation vs. Adaptive Hierarchy (Repair of Theorem `YM-013-T4`):**  
   Theorem `YM-013-T4` proved that for *fixed* $L_{\max} < \infty$, the physical reach vanishes as $a \to 0$ ($R_{\max}(a) = L_{\max} a \to 0$).  
   *Correction:* This establishes a **method-specific fixed-truncation limitation**, NOT an impossibility theorem for the bootstrap framework. An adaptive hierarchy $L_{\max}(a) \sim R_* / a \to \infty$ maintains non-zero physical reach $R_* > 0$. Theorem `YM-013-T4` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`).
4. **Bare Ribbon Entropy vs. Full Interacting Surface Partition Sum (Repair of Theorem `YM-014-T1`):**  
   Theorem `YM-014-T1` claimed that $\tau_0(\beta) < \ln \mu_4$ proves a roughening divergence in 4D lattice Yang–Mills.  
   *Correction:* $\tau_0(\beta) < \ln \mu_4$ is an elementary single-surface heuristic that omits self-avoidance, non-trivial vertex intertwiners, representation multiplicities, and severe sign cancellations. The threshold $\beta_c^{\mathrm{rough}} \approx 1.44\text{--}1.80$ is an **internally derived heuristic threshold** / strong-coupling estimate, NOT a mathematically proved divergence of interacting 4D Yang–Mills. Theorem `YM-014-T1` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`**.
5. **Indefinite Wigner $6j$ Signs vs. Extensive Sign Decay (Repair of Theorem `YM-014-T2`):**  
   Theorem `YM-014-T2` claimed that the average dual sign decays exponentially with volume: $\langle \operatorname{sign} \rangle \le e^{-c V}$.  
   *Correction:* The existence of negative $6j$ coefficients proves `SIGNED_WEIGHTS_EXIST`. However, an extensive sign decay bound $\langle \operatorname{sign} \rangle \le e^{-c V}$ is an **unproved extrapolation** for 4D Yang–Mills. Regrouping into tensor networks or contracting local hypercubes can alter or alleviate the sign structure. Theorem `YM-014-T2` is classified as **`NEEDS_AMENDMENT`**.
6. **Coset Polymer Radius vs. General Center-Vortex Variables (Repair of Theorem `YM-014-T3`):**  
   The threshold $\beta_0 \approx 0.35$ is the convergence radius of the specific bare polymer expansion on $SO(3)$, NOT a general obstruction to center-vortex descriptions (Mack–Petkova, Tomboulis). Theorem `YM-014-T3` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`).
7. **Bare Surface Tension Scaling vs. Renormalized Continuum Strings (Repair of Theorem `YM-014-T4`):**  
   The scaling $\tau(a) \sim \sigma_{\mathrm{phys}} a^2 \to 0$ applies strictly to the **bare** lattice surface tension. It does NOT imply an "empty Hilbert space" or the impossibility of a renormalized continuum string description. Theorem `YM-014-T4` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`).

---

## 2. Re-Audit of Task `YM-013` (Finite-$N$ Loop Bootstrap)

### 2.1. First-Principles Analysis of the Master Loop Equation on $SU(2)$
Recall the exact master Schwinger–Dyson / Makeenko–Migdal identity for a single closed loop $C$ passing through link $\ell$ on the 4D hypercubic lattice for gauge group $SU(N)$ ([`literature/YM-013-FINITE-N-LOOP-HIERARCHY.md`](file:///d:/Comfy%20UI/yang%20mills%20and%20the%20mass%20gap/literature/YM-013-FINITE-N-LOOP-HIERARCHY.md), eq. 2.9):
$$\frac{N^2 - 1}{2N} \langle \operatorname{Tr}(U(C)) \rangle = \frac{\beta}{4N} \sum_{p \ni \ell} \left\langle \operatorname{Tr}(U(C) U_p) - \operatorname{Tr}(U(C) U_p^\dagger) \right\rangle - \frac{\beta}{4N^2} \sum_{p \ni \ell} \left\langle \operatorname{Tr}(U(C)) \operatorname{Tr}(U_p - U_p^\dagger) \right\rangle.$$

Now examine the second sum on the right-hand side:
$$\mathcal{S}_{\mathrm{split}} \equiv -\frac{\beta}{4N^2} \sum_{p \ni \ell} \left\langle \operatorname{Tr}(U(C)) \operatorname{Tr}(U_p - U_p^\dagger) \right\rangle.$$

For general $SU(N)$ ($N \ge 3$):
$$\operatorname{Tr}(U_p - U_p^\dagger) = \operatorname{Tr}(U_p) - \overline{\operatorname{Tr}(U_p)} = 2 i \operatorname{Im}\operatorname{Tr}(U_p) \ne 0.$$
Therefore, for $N \ge 3$, this term couples the single-trace observable $\operatorname{Tr}(U(C))$ to the two-trace operator $\operatorname{Tr}(U(C)) \operatorname{Im}\operatorname{Tr}(U_p)$. In the large-$N$ limit, planar factorization $\langle \mathcal{O}_1 \mathcal{O}_2 \rangle = \langle \mathcal{O}_1 \rangle \langle \mathcal{O}_2 \rangle + O(1/N^2)$ and $\langle \operatorname{Im}\operatorname{Tr} U_p \rangle = 0$ cause this term to decouple at leading order $N = \infty$.

**HOWEVER, FOR $SU(2)$ ($N = 2$):**
Every element $U \in SU(2)$ has eigenvalues $\{e^{i\theta}, e^{-i\theta}\}$, so its trace is real:
$$\operatorname{Tr}(U) = 2\cos\theta \in \mathbb{R} \implies \operatorname{Tr}(U^\dagger) = \operatorname{Tr}(U).$$
Therefore:
$$\boxed{\operatorname{Tr}(U_p - U_p^\dagger) \equiv 0 \quad \text{identically as an operator on } SU(2).}$$
Thus, for $SU(2)$:
$$\mathcal{S}_{\mathrm{split}} \equiv 0.$$
The loop equation on $SU(2)$ reduces strictly to:
$$\frac{3}{4} \langle \operatorname{Tr}(U(C)) \rangle = \frac{\beta}{8} \sum_{p \ni \ell} \langle \operatorname{Tr}(U(C) U_p) - \operatorname{Tr}(U(C) U_p^\dagger) \rangle.$$
Dividing by $2$ and using $w(C) = \frac{1}{2}\operatorname{Tr}(U(C))$:
$$\boxed{3 \langle w(C) \rangle = \frac{\beta}{2} \sum_{p \ni \ell} \left( \langle w(C \cdot p) \rangle - \langle w(C \cdot p^\dagger) \rangle \right).}$$

This equation is:
1. **Strictly linear** in the Wilson loop expectations;
2. **Closed entirely within the space of single-trace Wilson loops**;
3. Contains **zero multi-trace operators**.

### 2.2. Diagnosis of the Project Error in Theorem `YM-013-T1`
In `YM-013-T1`, the project asserted:
> *"At any finite $N < \infty$, the absence of large-$N$ planar factorization generates an infinite, strictly non-closing BBGKY-type hierarchy over the trace number $m$, preventing closure at any finite trace degree."*

**Root Cause of Error:**
The project erroneously equated "finite $N$" with "multi-trace proliferation". While multi-trace coupling is generic for $N \ge 3$, $SU(2)$ is exceptional:
- In $SU(2)$, the Fierz identity trace-splitting term vanishes identically because $\operatorname{Tr}(U - U^\dagger) = 0$.
- In $SU(2)$, the Mandelstam relation $w(A)w(B) = \frac{1}{2}w(AB) + \frac{1}{2}w(AB^{-1})$ is an **algebraic operator identity** mapping any product of two traces to a sum of single traces.
- Kazakov & Zheng (JHEP 03 (2025) 099) explicitly built their finite-$N$ lattice bootstrap on this exact fact: in $SU(2)$, the Makeenko–Migdal equations are linear and closed on single-trace loops!

**Formal Amendment:**
Theorem `YM-013-T1` is **REFUTED** as a universal finite-$N$ theorem. Its valid scope is restricted to $SU(N)$ with $N \ge 3$ where Mandelstam reduction is nonlinear and trace splitting does not vanish.

---

### 2.3. Re-Audit of Theorem `YM-013-T2` (Mandelstam Perimeter Explosion)
Theorem `YM-013-T2` asserted that applying Mandelstam reduction $w(A)w(B) = \frac{1}{2}w(AB) + \frac{1}{2}w(AB^{-1})$ creates an exponential perimeter explosion $|AB| = |A| + |B|$ that prevents closing the equations.

**Literature Reconciliation (Liu & Yang 2026):**
Liu & Yang (*"Direct and indirect loop equations in lattice Yang-Mills theory,"* JHEP 04 (2026) 107) proved:
1. When generating Makeenko–Migdal identities by link variations on small loops, higher-length intermediate loops appear on the RHS.
2. However, by taking linear combinations of loop equations sharing intermediate loops, one can systematically **eliminate intermediate loops of length $L > L_{\mathrm{target}}$**, obtaining **indirect loop equations** involving only loops of length $\le L_{\mathrm{target}}$.
3. Using their **vertex-filtering strategy**, the number of independent equations matches the number of independent Wilson loops up to length $L \le 16$, with no intermediate perimeter explosion required to constrain the target dictionary.

**Formal Amendment:**
Theorem `YM-013-T2` is **CONFIRMED_WITH_NARROWER_SCOPE**: while naive multiplication of independent loops sums perimeters ($|AB| = |A| + |B|$), indirect loop equations eliminate intermediate loops and prevent perimeter blow-up in the constraint generation.

---

### 2.4. Re-Audit of Theorem `YM-013-T4` (Continuum Truncation Barrier)
Theorem `YM-013-T4` asserted:
> *"It is mathematically impossible for a finite-level SDP bootstrap ($L_{\max} < \infty$) to bound or close the intermediate coupling crossover edge $E\text{-}CROSSOVER$ in the continuum limit $a \to 0$."*

**Reconciliation:**
The mathematical derivation in `YM-013-T4` proved:
$$\text{For fixed } L_{\max} < \infty: \quad R_{\max}(a) = L_{\max} a \xrightarrow{a \to 0} 0.$$
This is a mathematically correct statement: a fixed-truncation dictionary probe cannot reach physical distance $R_{\mathrm{cross}} \sim 0.5\text{ fm}$ if $L_{\max}$ is held constant while $a \to 0$.

However, promoting this fixed-truncation limitation to an impossibility claim for the *entire loop-bootstrap program* was an over-claim:
- One can define an **adaptive hierarchy**:
  $$L_{\max}(a) = \left\lceil \frac{R_*}{a} \right\rceil \xrightarrow{a \to 0} \infty,$$
  where $R_* > 0$ is a fixed physical probing distance (e.g. $R_* = 0.5\text{ fm}$).
- As $a \to 0$, $L_{\max}(a)$ grows, but the physical scale probed remains constant.
- Whether the certified SDP bounds converge uniformly under $L_{\max}(a) \to \infty$ is currently **open**, but it is NOT mathematically ruled out by Theorem `YM-013-T4`.

**Formal Amendment:**
Theorem `YM-013-T4` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION` for fixed $L_{\max} < \infty$, not a structural no-go for adaptive bootstrap).

---

## 3. Re-Audit of Task `YM-014` (Random-Surface and Duality Representations)

### 3.1. Re-Audit of Theorem `YM-014-T1` (Random-Surface Roughening)
Theorem `YM-014-T1` asserted that because $\tau_0(\beta) = -\ln a_{1/2}(\beta) < \ln \mu_4$ for $\beta \ge 1.44\text{--}1.80$, the random-surface partition sum undergoes a Hagedorn / roughening divergence, proving that character-expansion surface representations diverge in the crossover regime.

**Literature Reconciliation:**
1. The density of states $N(A) \asymp \mu_4^A$ counts *isolated, non-interacting, self-avoiding ribbon surfaces* embedded in $\mathbb{Z}^4$.
2. In the full non-Abelian lattice gauge theory, surfaces are NOT independent ribbons:
   - Multiple plaquettes sharing edges contract via Clebsch–Gordan coefficients and Wigner $6j$ symbols.
   - Distinct representations $j = 1/2, 1, 3/2, \dots$ compete and interfere.
   - Significant sign and phase cancellations occur between different surface topologies.
3. Therefore, the single-surface estimate $\tau_0(\beta) < \ln \mu_4$ is an **internally derived heuristic threshold** / strong-coupling estimate. It proves the divergence of the *naive non-interacting ribbon model*, but does NOT constitute a rigorous mathematical proof that the full interacting 4D Yang–Mills partition function diverges at $\beta_c^{\mathrm{rough}} \approx 1.44$.

**Formal Amendment:**
Theorem `YM-014-T1` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION` for bare non-interacting ribbon surfaces; heuristic/unproved for full interacting non-Abelian theory).

---

### 3.2. Re-Audit of Theorem `YM-014-T2` (Non-Abelian Duality Sign Problem)
Theorem `YM-014-T2` asserted:
$$\langle \operatorname{sign} \rangle = \frac{\sum_\sigma W(\sigma)}{\sum_\sigma |W(\sigma)|} \le e^{-c_{\mathrm{sign}} V}.$$

**Literature Reconciliation (Oeckl & Pfeiffer 2001):**
1. Step 2 of `YM-014-T2` correctly proved:
   $$\left\{\begin{matrix} 1 & 1 & 1 \\ 1/2 & 1/2 & 1/2 \end{matrix}\right\} = -\frac{1}{3} < 0.$$
   Therefore, vertex amplitudes are NOT pointwise positive: `SIGNED_WEIGHTS_EXIST` is a **proved mathematical theorem**.
2. However, Step 3 asserted:
   $$\Delta f = f - f_{\mathrm{abs}} = c_{\mathrm{sign}} > 0 \implies \langle \operatorname{sign} \rangle \le e^{-c_{\mathrm{sign}} V}.$$
   This step assumed that negative vertex amplitudes cannot be reorganized or cancelled locally.
3. In constructive field theory and tensor-network physics (Oeckl & Pfeiffer 2001; Denbleyker et al. 2014):
   - Local block contractions (e.g. contracting all 24 faces inside a 4-hypercube) can produce effective weights that are strictly positive or have significantly reduced sign oscillation.
   - The assertion of strict exponential sign decay $\langle \operatorname{sign} \rangle \le e^{-c V}$ for 4D Yang–Mills requires an explicit analytical lower bound on the absolute free energy relative to the physical free energy, which was NOT proved.

**Formal Amendment:**
Theorem `YM-014-T2` is classified as **`NEEDS_AMENDMENT`**:
- `SIGNED_WEIGHTS_EXIST`: **CONFIRMED** (proved from Racah formula).
- `EXPONENTIALLY_VANISHING_AVERAGE_SIGN`: **UNPROVED EXTRAPOLATION** (downgraded to unproved hypothesis).

---

### 3.3. Re-Audit of Theorem `YM-014-T3` (Center-Vortex / Coset Polymer Expansion)
Theorem `YM-014-T3` asserted that center-vortex representations fail in the crossover regime because the coset polymer expansion diverges for $\beta > \beta_0 \approx 0.35$.

**Literature Reconciliation (Mack–Petkova 1979, Tomboulis 1981):**
1. $\beta_0 \approx 0.35$ is the radius of convergence of the standard Osterwalder–Seiler polymer expansion on $SO(3)$. The failure of this specific series is a known mathematical fact.
2. However, Tomboulis (1981) and Mack & Petkova (1979) established rigorous lower bounds on 't Hooft electric flux free energy using vortex sheet variables and correlation inequalities that do not rely on naive bare polymer expansions.
3. Failure of the bare coset polymer expansion does NOT imply that all center-vortex formulations are impossible.

**Formal Amendment:**
Theorem `YM-014-T3` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION` for bare coset polymer expansion; does not rule out vortex-sheet correlation inequalities).

---

### 3.4. Re-Audit of Theorem `YM-014-T4` (Continuum Surface-Tension Asymptotic Scaling Defect)
Theorem `YM-014-T4` asserted:
$$\tau(a) = \sigma_{\mathrm{phys}} a^2 \to 0 \implies \tau(a) < \ln \mu_4 \implies \text{empty Hilbert space}.$$

**Literature Reconciliation:**
1. The mathematical scaling $\tau(a) \sim \sigma_{\mathrm{phys}} a^2 \to 0$ correctly describes the **bare lattice surface tension** required for finite physical string tension.
2. However, asserting an "empty Hilbert space" and "impossibility of all surface representations" confuses a **bare** lattice model with a **renormalized** continuum string description:
   - In continuum effective string theory (Lüscher, Weisz, Polyakov), the physical string tension is a renormalized quantity where the bare tension is counterbalanced by worldsheet quantum fluctuations.
   - The failure of bare lattice surfaces to localize does not preclude a continuum string or duality description.

**Formal Amendment:**
Theorem `YM-014-T4` is classified as **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION` for bare lattice surface models; renormalized continuum surface descriptions remain open).

---

## 4. Formal Post-Acceptance Amendment Registry

| Original Theorem ID | Original Epistemic Claim | Audited Literature Baseline | Reconciliation Finding | Amended Epistemic Classification |
| :--- | :--- | :--- | :--- | :--- |
| **`YM-013-T1`** | Universal finite-$N$ multi-trace proliferation obstruction | Kazakov & Zheng (JHEP 2025 099) | For $SU(2)$, $\operatorname{Tr}(U_p - U_p^\dagger) \equiv 0$; equations are strictly linear on single-trace loops. | **`NEEDS_AMENDMENT`** (Refuted for $SU(2)$; confirmed for $SU(N \ge 3)$) |
| **`YM-013-T2`** | Mandelstam reduction forces exponential perimeter explosion | Liu & Yang (JHEP 2026 107) | Indirect loop equations with vertex filtering eliminate intermediate loops without perimeter explosion. | **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`) |
| **`YM-013-T3`** | Certified SDP bounds on Wilson loops at fixed lattice spacing | Kazakov & Zheng (2025) | Dual interval Cholesky certificates verify valid SDP relaxations on discrete lattices. | **`CONFIRMED`** (`CODE_VERIFIED` + `MATHEMATICALLY_PROVED`) |
| **`YM-013-T4`** | Finite-level bootstrap cannot close continuum crossover | Standard constructive scaling | Proves fixed-truncation limitation ($L_{\max} < \infty$); adaptive hierarchy ($L_{\max}(a) \sim R_*/a$) is unruled out. | **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`) |
| **`YM-014-T1`** | $\tau_0 < \ln \mu_4$ proves roughening divergence of 4D Yang–Mills | Ambjørn (1997), Durhuus (1984) | Single-surface heuristic; does not prove divergence of full interacting non-Abelian partition sum. | **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`) |
| **`YM-014-T2`** | Average dual sign decays exponentially: $\langle \operatorname{sign} \rangle \le e^{-c V}$ | Oeckl & Pfeiffer (Nucl. Phys. B 2001) | Indefinite signs confirmed ($6j < 0$ exists); extensive sign decay is an unproved extrapolation. | **`NEEDS_AMENDMENT`** (Downgraded to signed weights existence) |
| **`YM-014-T3`** | Center-vortex polymer expansion divergence rules out vortex route | Mack & Petkova (1979), Tomboulis (1981) | Bare coset polymer expansion fails at $\beta \approx 0.35$; vortex-sheet flux inequalities remain viable. | **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`) |
| **`YM-014-T4`** | Bare string tension scaling $\tau(a) \to 0$ forces empty Hilbert space | Lüscher & Weisz (2002), Polyakov (1981) | Applies strictly to bare lattice models; does not rule out renormalized continuum string descriptions. | **`CONFIRMED_WITH_NARROWER_SCOPE`** (`METHOD_SPECIFIC_OBSTRUCTION`) |

---

## 5. Summary and Invariant Governance Preservation

Throughout this reconciliation:
- `goal_complete = false`
- `clay_problem = OPEN_AND_UNSOLVED`
- `P3 = OPEN`
- `E-CROSSOVER = OPEN`
- Historical Revision 29 artifacts remain preserved without mutation.
- All amended theorems are tracked via explicit post-acceptance amendment objects.
