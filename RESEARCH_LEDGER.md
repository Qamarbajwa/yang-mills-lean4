# RESEARCH LEDGER

## Entries

### YM-001-RES-001: Retrieval and Ingestion of Authoritative Primary Sources
- **Date:** 2026-08-24
- **Sources Ingested:**
  - Jaffe & Witten, *Quantum Yang–Mills Theory*, Clay Mathematics Institute (2000), 14 pages (`literature/primary/clay/jaffe_witten_yang_mills.pdf`, SHA-256: `3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09`).
  - Clay Mathematics Institute, *Yang–Mills & The Mass Gap* official page (`literature/primary/clay/CURRENT_CLAY_STATUS.md`).
- **Outcome:** Primary sources preserved and registered in `literature/primary/clay/SOURCE_MANIFEST.yaml`.

### YM-001-RES-002: Formal Semantic Reconstruction of the Millennium Problem Specification
- **Date:** 2026-08-24
- **Analysis:** Resolved questions SPEC-001 through SPEC-030 directly against the Jaffe–Witten text. Established the distinction between formal requirements (compact simple $G$, $\mathbb{R}^4$, axiomatic properties $\ge$ [45, 35], $\Delta > 0$, $m < \infty$, gauge-invariant operators, asymptotic freedom matching) and desirable extensions (confinement, isolated 1-particle state, chiral symmetry breaking, curved 4-manifolds).
- **Outcome:** Generated `OFFICIAL_PROBLEM_SPECIFICATION.md`, `DEFINITION_LEDGER.md`, and `CLAIM_EVIDENCE_MATRIX.md`.

### RES-YM-002A-001: What did Yang and Mills actually construct in 1954?
- **Date:** 2026-08-24
- **Question:** What was the mathematical and physical scope of the 1954 Yang–Mills paper?
- **Primary Source:** C. N. Yang & R. L. Mills, *Phys. Rev.* 96 (1954), 191–195 (`PAPER-FOUND-001`).
- **Findings:** Yang and Mills constructed the classical non-Abelian gauge theory for $SU(2)$ isotopic spin. They defined the non-Abelian connection $B_\mu$, the non-linear curvature $F_{\mu\nu}$, and the Euler–Lagrange wave equations. They recognized that classical non-Abelian waves are massless ($v=c$) and noted that the quantum mass spectrum remained an unsolved difficulty.
- **Outcome:** Recorded as `THM-YM-0001` (`RIGOROUS_THEOREM` for classical differential geometry; zero quantum existence).

### RES-YM-002A-002: What problem did Faddeev–Popov solve?
- **Date:** 2026-08-24
- **Question:** What is the exact mathematical contribution and limitation of Faddeev–Popov quantization?
- **Primary Source:** L. D. Faddeev & V. N. Popov, *Phys. Lett. B* 25 (1967), 29–30 (`PAPER-FOUND-002`).
- **Findings:** They solved the problem of overcounting gauge orbits in the formal Feynman path integral by introducing a gauge condition $f(A)=0$ and multiplying by the functional Jacobian $\Delta_f(A) = \det(\mathcal{M}_f)$, exponentiated via Grassmann ghost fields $c, \bar{c}$. This established unitary perturbative Feynman rules. It did not construct a non-perturbative measure, and Gribov (1978) later proved that $f(A)=0$ is not a global gauge slice (Gribov copies).
- **Outcome:** Recorded as `THM-YM-0002` (`PERTURBATIVE_THEOREM`).

### RES-YM-002A-003: What exactly was proved perturbatively renormalizable?
- **Date:** 2026-08-24
- **Question:** What is the precise scope of 't Hooft and Veltman's renormalization proof?
- **Primary Sources:** G. 't Hooft, *Nucl. Phys. B* 33 (1971), 173–199 (`PAPER-FOUND-003`); G. 't Hooft & M. Veltman, *Nucl. Phys. B* 44 (1972), 189–213 (`PAPER-FOUND-012`).
- **Findings:** They proved that order-by-order in perturbation theory, all ultraviolet divergences in massless and spontaneously broken non-Abelian gauge theories can be absorbed by local gauge-invariant counterterms using dimensional regularization to preserve Ward–Takahashi–Slavnov–Taylor identities. This does not prove convergence of the perturbation series or non-perturbative existence in 4D.
- **Outcome:** Recorded as `THM-YM-0003` and `THM-YM-0004` (`PERTURBATIVE_THEOREM`).

### RES-YM-002A-004: What is the precise content of asymptotic freedom?
- **Date:** 2026-08-24
- **Question:** Does asymptotic freedom establish a mass gap or non-perturbative control?
- **Primary Sources:** D. J. Gross & F. Wilczek, *Phys. Rev. Lett.* 30 (1973), 1343–1346 (`PAPER-FOUND-006`); H. D. Politzer, *Phys. Rev. Lett.* 30 (1973), 1346–1349 (`PAPER-FOUND-007`).
- **Findings:** Asymptotic freedom proves that the 1-loop beta function is strictly negative ($\beta(g) = -\frac{b_0}{(4\pi)^2} g^3 < 0$), causing the running coupling $g(\mu) \to 0$ as $\mu \to \infty$. This gives complete perturbative control in the ultraviolet (short distances), but causes the coupling to grow large in the infrared (long distances), where perturbation theory breaks down and cannot determine the mass spectrum.
- **Outcome:** Recorded as `THM-YM-0006` (`PERTURBATIVE_THEOREM`).

### RES-YM-002A-005: What exactly does Wilson's strong-coupling expansion establish?
- **Date:** 2026-08-24
- **Question:** Does Wilson's lattice confinement prove continuum confinement or a mass gap?
- **Primary Source:** K. G. Wilson, *Phys. Rev. D* 10 (1974), 2445–2459 (`PAPER-FOUND-009`).
- **Findings:** Wilson defined gauge theory on a hypercubic lattice with link variables $U_{x,\mu} \in G$, preserving exact local gauge invariance. At strong coupling $g^2 \gg 1$, a high-temperature character expansion proves an area law $\langle W(C) \rangle \sim \exp(-\sigma \cdot \mathrm{Area}(C))$ with string tension $\sigma = \ln(g^2)/a^2$. However, taking the continuum limit requires $a \to 0$, which by asymptotic freedom forces $g \to 0$ (weak coupling), where the strong-coupling expansion fails.
- **Outcome:** Recorded as `THM-YM-0008` (`CONTROLLED_EXPANSION` on fixed lattice).

### RES-YM-002A-006: What does Osterwalder–Schrader reconstruction assume rather than construct?
- **Date:** 2026-08-24
- **Question:** Does the OS theorem solve the 4D Yang–Mills existence problem?
- **Primary Sources:** K. Osterwalder & R. Schrader, *Comm. Math. Phys.* 31 (1973), 83–112 (`PAPER-FOUND-004`); *ibid.* 42 (1975), 281–305 (`PAPER-FOUND-005`).
- **Findings:** The OS theorem proves that IF a family of Euclidean Schwinger functions satisfies OS-0 through OS-4 (including reflection positivity OS-2), THEN they uniquely reconstruct a relativistic Wightman QFT on Minkowski space with positive energy and a unique vacuum. The theorem does NOT construct the Schwinger functions for 4D Yang–Mills; that remains the core open challenge.
- **Outcome:** Recorded as `THM-YM-0005` (`RIGOROUS_THEOREM` for general QFT reconstruction).

### RES-YM-002A-007: What role do instantons rigorously establish?
- **Date:** 2026-08-24
- **Question:** Do BPST instantons prove a quantum mass gap?
- **Primary Source:** A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Yu. S. Tyupkin, *Phys. Lett. B* 59 (1975), 85–87 (`PAPER-FOUND-010`).
- **Findings:** BPST constructed exact finite-action self-dual classical solutions in 4D Euclidean space with topological charge $Q=1$. Instantons prove the existence of non-trivial topology and vacuum tunneling, but semiclassical dilute instanton gases in 4D suffer from infrared scale integration divergences and do not prove a quantum mass gap.
- **Outcome:** Recorded as `THM-YM-0010` (`RIGOROUS_THEOREM` for classical topology).

### RES-YM-002A-008: What lower-dimensional confinement mechanism did Polyakov establish?
- **Date:** 2026-08-24
- **Question:** Does Polyakov's 1977 paper prove 4D confinement?
- **Primary Source:** A. M. Polyakov, *Nucl. Phys. B* 120 (1977), 429–458 (`PAPER-FOUND-011`).
- **Findings:** In $2+1$ dimensions for compact $U(1)$ gauge theory, Polyakov established that magnetic monopoles (instantons in 3D Euclidean space) form a plasma with Debye screening, generating a dynamical mass gap for the photon and linear confinement for Wilson loops via a semiclassical duality mapping to a sine-Gordon model. In $3+1$ dimensions for non-Abelian theory, Polyakov proposed an instanton gas mechanism, which remained a heuristic conjecture due to infrared divergences.
- **Outcome:** Recorded as `THM-YM-0011` (`SEMICLASSICAL_DERIVATION` in 2+1D) and `THM-YM-0012` (`CONJECTURE_OR_PROPOSAL` in 4D).

### RES-YM-002AR1-001: What exactly does Faddeev–Popov 1967 establish?
- **Date:** 2026-08-24
- **Question:** What is the precise mathematical and perturbative scope of Faddeev and Popov's 1967 paper?
- **Primary Source:** L. D. Faddeev & V. N. Popov, *Phys. Lett. B* 25 (1967), 29–30 (`PAPER-FOUND-002`).
- **Findings:** The 1967 paper establishes the factorization of the gauge group volume in the formal functional integral by inserting $1 = \Delta_f(A) \int \mathcal{D}g \, \delta(f(A^g))$, yielding the ghost determinant $\det(\mathcal{M}_f)$ and Feynman rules in perturbation theory. It does not mention or discover Gribov copies.
- **Outcome:** Recorded as `THM-YM-0002` (`PERTURBATIVE_QFT_RESULT`).

### RES-YM-002AR1-002: What does Gribov 1978 add/change?
- **Date:** 2026-08-24
- **Question:** What is the exact historical and non-perturbative role of Gribov 1978?
- **Primary Source:** V. N. Gribov, *Nucl. Phys. B* 139 (1978), 1–19 (`PAPER-FOUND-014`).
- **Findings:** Gribov proved that local gauge conditions like Coulomb and Landau gauge do not uniquely fix the gauge for large field amplitudes: equivalent gauge configurations (Gribov copies) satisfy $f(A)=0$. This demonstrates that Faddeev–Popov gauge fixing is strictly a perturbative local device obstructed globally by Gribov horizons.
- **Outcome:** Admitted as `PAPER-FOUND-014` (`LATER_LIMITATION_OR_DEVELOPMENT`).

### RES-YM-002AR1-003: What is the evidentiary status of Polyakov's 2+1D confinement argument?
- **Date:** 2026-08-24
- **Question:** Is Polyakov 1977 Part A a rigorous mathematical theorem or a semiclassical derivation?
- **Primary Source:** A. M. Polyakov, *Nucl. Phys. B* 120 (1977), 429–458 (`PAPER-FOUND-011`).
- **Findings:** Polyakov uses a dilute monopole gas approximation and semiclassical duality to map 3D compact $U(1)$ / broken $SU(2)$ gauge theory to a Coulomb plasma with Debye screening mass $m_D$. While physically compelling, it was a semiclassical derivation, not an axiomatic constructive proof. Rigorous mathematical proof on the lattice was achieved later by Göpfert & Mack (1981) and Brydges et al. (1980).
- **Outcome:** Classified as `SEMICLASSICAL_DERIVATION` in `THM-YM-0011`.

### RES-YM-002AR1-004: What status does Polyakov's 3+1D non-Abelian analysis have?
- **Date:** 2026-08-24
- **Question:** What is the mathematical status of Polyakov 1977 Part B in 4D?
- **Primary Source:** A. M. Polyakov, *Nucl. Phys. B* 120 (1977), 429–458 (`PAPER-FOUND-011`).
- **Findings:** Section 5–6 of Polyakov 1977 proposes that instantons in 4D non-Abelian gauge theory might induce confinement and mass gap by analogy with 3D monopoles. However, the 4D dilute instanton gas is plagued by infrared logarithmic divergence $\int d\rho / \rho^5$ from large instantons, making the proposal uncontrolled in pure 4D Yang–Mills.
- **Outcome:** Classified as `CONJECTURE_OR_PROPOSAL` in `THM-YM-0012`.

### RES-YM-002AR1-005: What exactly is established in Wilson's strong-coupling limit?
- **Date:** 2026-08-24
- **Question:** What are the exact assumptions and limitations of Wilson's 1974 lattice confinement?
- **Primary Source:** K. G. Wilson, *Phys. Rev. D* 10 (1974), 2445–2459 (`PAPER-FOUND-009`).
- **Findings:** Wilson proved that at fixed lattice cutoff $a > 0$ and strong coupling $g^2 \gg 1$, the character expansion of the Wilson loop produces an area law with string tension $\sigma = \ln(g^2)/a^2$. In this regime, continuous Euclidean/Lorentz invariance is explicitly broken. Crucially, the continuum limit $a \to 0$ requires $g \to 0$ (weak coupling) due to asymptotic freedom, where the strong-coupling expansion is invalid.
- **Outcome:** Classified as `CONTROLLED_STRONG_COUPLING_EXPANSION` in `THM-YM-0008`.

### RES-YM-002AR1-006: What is classical versus quantum in BPST?
- **Date:** 2026-08-24
- **Question:** Does the BPST instanton establish a quantum mass gap?
- **Primary Source:** A. A. Belavin et al., *Phys. Lett. B* 59 (1975), 85–87 (`PAPER-FOUND-010`).
- **Findings:** BPST discovered an exact classical non-singular self-dual solution in Euclidean $\mathbb{R}^4$ with topological Pontryagin charge $Q=1$ and finite action $S = 8\pi^2/g^2$. This is a classical field solution and does not construct the quantum Hilbert space, quantum measure, or quantum mass gap.
- **Outcome:** Classified as `CLASSICAL_EXACT_SOLUTION` in `THM-YM-0010`.

### RES-YM-002AR1-007: What does OS II correct/extend relative to OS I?
- **Date:** 2026-08-24
- **Question:** Why did Osterwalder and Schrader publish OS II in 1975?
- **Primary Sources:** K. Osterwalder & R. Schrader, *Comm. Math. Phys.* 31 (1973), 83–112 (`PAPER-FOUND-004`); *ibid.* 42 (1975), 281–305 (`PAPER-FOUND-005`).
- **Findings:** OS I (1973) introduced the Euclidean axioms (reflection positivity, Euclidean invariance, cluster decomposition) but had technical subtleties in the linear growth condition for reconstructing Wightman distributions. OS II (1975) established the definitive, corrected, and extended theorem with linear growth condition OS-0 and proved the equivalence with Wightman axioms W-1 through W-7.
- **Outcome:** Recorded as `THM-YM-0005` (`RIGOROUS_MATHEMATICAL_THEOREM`).


### RES-YM-002B-001: What did Göpfert and Mack rigorously prove in 3D?
- **Date:** 2026-08-24
- **Question:** What was the mathematical scope and limitation of the 1981 Göpfert–Mack confinement proof?
- **Primary Source:** M. Göpfert & G. Mack, *Comm. Math. Phys.* 82 (1981), 545–590 (`PAPER-CONST-001`).
- **Epistemic Classification:** `[PRIMARY_SOURCE_RESULT]` (Theorems 1–3) / `[PRIMARY_SOURCE_LIMITATION]`
- **Findings:** They rigorously proved static quark confinement (non-zero string tension $\sigma > 0$) for all values of coupling $g^2$ in 3D $U(1)$ lattice gauge theory with Villain action. In the continuum limit with physical Debye mass $m_D > 0$ held fixed, the dual field theory converges to a free massive scalar field. Monopoles in 3D Euclidean spacetime are 0D point events. The method does not generalize directly to 4D where monopoles are 1D closed current loops, nor to non-Abelian gauge groups.
- **Outcome:** Recorded as `THM-YM-0013` and `PATH-CONST-001`.

### RES-YM-002B-002: What is the exact mathematical scope of Bałaban's RG program?
- **Date:** 2026-08-24
- **Question:** What did Bałaban prove in 4D Yang–Mills, and where did the program stop?
- **Primary Sources:** T. Bałaban, *Comm. Math. Phys.* 95 (1984), 419; *ibid.* 109 (1987), 249; *ibid.* 116 (1988), 1; *ibid.* 119 (1988), 243 (`PAPER-CONST-004`, `PAPER-CONST-005`, `PAPER-CONST-006`).
- **Epistemic Classification:** `[PRIMARY_SOURCE_RESULT]` (UV stability) / `[PRIMARY_SOURCE_LIMITATION]` (finite volume $V < \infty$) / `[LATER_LITERATURE_LIMITATION]`
- **Findings:** Bałaban proved 4D Ultraviolet Stability in a fixed finite volume $V < \infty$: uniform upper and lower bounds on the partition function $Z(a, V)$ as $a \to 0$. In the infinite volume limit ($V \to \infty$), the RG trajectory enters the strong-coupling infrared regime ($g_k \sim 1$), where small-field inductive series and large-field polymer expansions lose convergence without an independent infrared closure mechanism.
- **Outcome:** Recorded as `THM-YM-0016`, `THM-YM-0017`, `THM-YM-0018`, and `PATH-CONST-002`.

### RES-YM-002B-003: What did Magnen, Rivasseau, and Sénéor achieve in 1993?
- **Date:** 2026-08-24
- **Question:** What was constructed in the 1993 MRS paper on $YM_4$?
- **Primary Source:** J. Magnen, V. Rivasseau, R. Sénéor, *Comm. Math. Phys.* 155 (1993), 325–383 (`PAPER-CONST-008`).
- **Epistemic Classification:** `[PRIMARY_SOURCE_RESULT]` (Theorems 1–4) / `[PRIMARY_SOURCE_LIMITATION]` (p. 326) / `[PROJECT_SYNTHESIS]`
- **Findings:** They constructively proved the existence of 4D Euclidean Yang–Mills Schwinger distributions with an artificial infrared cutoff $\Lambda_{IR} > 0$ (such as finite volume or mass regulator), proving UV Borel summability. The authors explicitly stated (p. 326) that the removal of the infrared cutoff ($\Lambda_{IR} \to 0$) remains open. In constructive field theory literature, removing $\Lambda_{IR}$ without a prior mass gap is obstructed by infrared renormalons.
- **Outcome:** Recorded as `THM-YM-0020` and `PATH-CONST-003`.

### RES-YM-002CR2-001: Separation of 2D Markov Process vs. Invariant Measure Proof
- **Date:** 2026-08-25
- **Question:** What is the precise division of labor between Chandra et al. (2022) and Chevyrev & Shen (2026)?
- **Primary Sources:** A. Chandra et al., *Publ. Math. IHÉS* 136 (2022), 1–147 (`PAPER-MOD-001`); I. Chevyrev & H. Shen, *CPAM* 79 (2026), 1973–2102 (`PAPER-MOD-002`).
- **Epistemic Classification:** `[PRIMARY_SOURCE_RESULT]` / `[PRIMARY_SOURCE_LIMITATION]`
- **Findings:** Chandra et al. (2022) constructed the distributional connection state space, gauge-orbit metric state space, and stochastic Markov process on the torus $\mathbb{T}^2$. Chevyrev & Shen (2026) proved that the 2D Euclidean Yang–Mills measure is the unique invariant measure of this Langevin dynamic for any connected compact Lie group $G$, and established universality of the continuum dynamic.
- **Outcome:** Recorded as separate theorems `THM-YM-0021` and `THM-YM-0022`.

### RES-YM-002CR2-002: Shen–Zhu–Zhu Strong Coupling Lattice Mass Gap Publication
- **Date:** 2026-08-25
- **Question:** What is the authoritative publication metadata and scope of Shen–Zhu–Zhu?
- **Primary Source:** H. Shen, R. Zhu, X. Zhu, *Comm. Math. Phys.* 400 (2023), 805–851 (`PAPER-MOD-007`).
- **Epistemic Classification:** `[PRIMARY_SOURCE_RESULT]` / `[PRIMARY_SOURCE_LIMITATION]` / `[PROJECT_SYNTHESIS]`
- **Findings:** Published in *Communications in Mathematical Physics* (2023), proving infinite-volume Gibbs measure existence, uniform Poincaré and log-Sobolev inequalities, and exponential correlation decay (strictly positive lattice mass gap $\Delta_{lat}(\beta) > 0$) at strong coupling ($\beta < \beta_0$). Confined to $\beta < \beta_0$; does not establish the weak-coupling continuum limit $\beta \to \infty$.
- **Outcome:** Recorded as `THM-YM-0027`.

### RES-YM-002CR2-003: Cao–Nissim–Sheffield Area Law Advances
- **Date:** 2026-08-25
- **Question:** How do the two Cao–Nissim–Sheffield 2025 papers differ?
- **Primary Sources:** Y. Cao, E. Nissim, S. Sheffield, *arXiv:2505.16585* (`PAPER-MOD-008`); *arXiv:2509.04688* (`PAPER-MOD-009`).
- **Epistemic Classification:** `[PRIMARY_SOURCE_RESULT]` / `[PRIMARY_SOURCE_LIMITATION]`
- **Findings:** *arXiv:2505.16585* expands the rigorous parameter regimes for the Wilson loop area law. *arXiv:2509.04688* develops a dynamical approach building on Shen–Zhu–Zhu inequalities, deriving area law from spectral gap conditions in 't Hooft regimes for $U(N), SU(N), SO(2N)$.
- **Outcome:** Recorded as separate theorems `THM-YM-0028` and `THM-YM-0029`.

### RES-YM-002CR2A-001: Modern-Source Locator and Theorem-Wording Erratum
- **Date:** 2026-08-25
- **Question:** What is the precise page range for CCHS (2024) 3D YMH and the exact theorem scope of Chevyrev & Shen (2026)?
- **Primary Sources:** A. Chandra, I. Chevyrev, M. Hairer, H. Shen, *Inventiones Mathematicae* 237 (2024), 541–696 (`PAPER-MOD-003`); I. Chevyrev & H. Shen, *Archive for Rational Mechanics and Analysis* 250 (2026), article 11, 1–55 (`PAPER-MOD-004`).
- **Epistemic Classification:** `[PRIMARY_SOURCE_RESULT]` / `[PRIMARY_SOURCE_LIMITATION]`
- **Findings:**
  1. *CCHS 2024 Locator:* Published in *Inventiones Mathematicae* 237 (2024), pp. 541–696 (replacing any erroneous 85–236 range). Invariant measure existence remains an open problem (cited on p. 543).
  2. *Chevyrev–Shen 2026 Theorem Scope:* Rigorously establishes uniqueness of the mass renormalisation that leads to gauge-covariant solutions of the stochastic 3D Yang–Mills–Higgs equations. The phrase 'scheme-independence' is not an unqualified source claim and is restricted to the canonical uniqueness of the gauge-covariant mass counterterm.
- **Outcome:** Recorded in `THM-YM-0023` and `THM-YM-0024`.
