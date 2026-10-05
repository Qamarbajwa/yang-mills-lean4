# YM-015F-JET-002B — primary small-field map and conditional marked recurrence

Date: 2026-10-05. Candidate scientific artifact for independent review; no acceptance or governance change. Baseline: revision 35, HEAD `a632b7ce158d378af5b0e5ff7485cbce0f9b2b45`. Read: exact normalized transport 035, insertion/source audit reconciled in 034, source-jet reduction, and historical YM-004 RG architecture. Result: an actual **small-field** integration map was extracted; the complete normalized Wilson/source representation and its uniform marked estimates remain OPEN.

## Primary access record

CMP 109 (1987), 249–301: [Euclid article](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-2/Renormalization-group-approach-to-lattice-gauge-field-theories-I-Generation/cmp/1104116842.full), [normal download endpoint](https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104116842), [publisher](https://link.springer.com/article/10.1007/BF01215223). Ordinary PowerShell HTTP access supplied a 5,490,078-byte, 54-page PDF. Text extraction inspected PDF pages 1–10 and17–20 (printed249–258 and265–268); PDF page7/printed255 was additionally rendered in memory and visually inspected. Not every page or referenced predecessor was inspected. No PDF or image was saved. Later requests returned `Pardon Our Interruption`; Python urllib separately received a one-page `Request unsuccessful. Incapsula incident ID: 1228000030072153749-111078995500204229` PDF. These failures do not invalidate the earlier inspected full article; they limit further extraction.

Other access: publisher previews were directly inspected for [CMP116,1–22](https://link.springer.com/article/10.1007/BF01239022), [CMP119,243–285](https://link.springer.com/article/10.1007/BF01217741), and [CMP122,355–392](https://link.springer.com/article/10.1007/BF01238433). All state subscription preview. Euclid116 issue listing exposed article `cmp/1104161193`, but its full text was not inspected. Michigan discovery and the attempted author homepage returned403. Bounded searches did not identify an accessible Michigan full text for these four target articles. No assertion that legal copies do not exist follows.

## Source extraction: CMP109 (under 200 source-derived words, including notation)

Printed255, equation(0.19), visually verified:

\[
A_{k+1}(g_{k+1},V)=\log\!\left[N_k^{-1}\int dU
\prod_{c\in T^{(k+1)}}\delta(\bar U(c)V^{-1}(c))\,\chi_k
\exp\!\left\{-g_k^{-2}\!\sum_{y\in T^{(k+1)}}\sum_{x\in B(y),x\ne y}
[1-\operatorname{Re}\operatorname{tr}\bar U(y,x)]+A_k(g_k,U)\right\}\right].
\]

Here bar denotes the paper's averages: contour average(0.11), blocking average(0.12), printed253–254. The normalization is the same integral at `V=1` (printed256); this is a logarithmic weight convention. Equation(0.13) defines `T rho` by a gauge-invariant kernel. Equation(0.16) retains normalized exponential gauge-fixing and its restriction. Regular configurations and residual gauge transformations equal to1 at coarse sites are discussed on printed254. Section2 restricts backgrounds to those admitting regular minima; `chi_k` is defined in(2.9), printed266, with an alternative coupling-dependent cutoff. Those restrictions are retained here by reference, not replaced by unrestricted integration. Printed251 requires odd `L>11`; printed252 uses normalized trace `tr 1=1`. Printed256,(0.21), specifies a unique critical **orbit** in the regular space, not an unrestricted unique connection.

## Other primary summaries (each under 200 words)

CMP116: verified title is *Renormalization group approach to lattice gauge field theories. II. Cluster expansions*. Publisher abstract identifies exponentiation of the PartI fluctuation integral and completion of the effective-action construction in the small-field approximation. No exact cluster formula or activity norm was extracted here.

CMP119: verified title is *Convergent renormalization expansions for lattice gauge theories*. Publisher abstract describes complete densities including large-field domains, preserved by renormalization transformations; its stated completion and convergence concern superrenormalizable models. No full-density recurrence was extracted here.

CMP122: verified title is *Large field renormalization. II. Localization, exponentiation, and bounds for the R operation*. Publisher abstract locates completion of four-dimensional pure-gauge ultraviolet stability in Theorem1. Theorem1, the R-operation map, and its quantitative hypotheses were not inspected. No flowed-source conclusion is attributed to this abstract.

## Own conditional algebra on the extracted map

Everything below is our finite algebra, **not a theorem extracted from Bałaban**. Fix a permitted background `V`, a permitted cutoff, and real vacuum parameters. Let `I_k[V;F]` denote precisely the integral inside(0.19), inserting the scalar or finite-jet function `F(U)` and retaining every delta, gauge-fixing factor, cutoff, and vacuum factor displayed there. Keep the source-independent normalization `N_k=I_k[1;1]`.

Conditional hypothesis H: this constrained integral has its intended finite positive-measure interpretation, and `0<I_k[V;1]<infinity` on the chosen background domain; the inserted coefficients are integrable. Delta notation alone does not prove H or a disintegration dictionary. We do not replace group deltas by additive Lie-algebra deltas, omit gauge factors, or extend the domain. Define

    L_k[V;F] = I_k[V;F]/N_k,
    M_k[V;F] = I_k[V;F]/I_k[V;1].

Then `L_k[V;1]=exp(A_(k+1)(V))`. The quotient `M_k` is a probability expectation only under H. It is distinct from division by the global Wilson partition function and distinct from a source-dependent normalization at the identity background.

Use commuting labels `z_i^2=0` and a jet

    P_k(U;z)=sum_(S subset labels) z_S p_(k,S)(U),  p_(k,empty)=1.

Linearity gives the exact weight and coefficient recurrence

    L_k[V;P_k]=exp(A_(k+1)(V)) P_(k+1)(V;z),
    p_(k+1,S)(V)=M_k[V;p_(k,S)] .

Thus all subsets travel through the same unmodified vacuum map. Starting with `P_0=product_i(1+z_i X_i)` sends joint coefficients, rather than only singleton means. The `X_i` must be the selected physically normalized flowed observables to claim a relation to the target; no local-coordinate expression for them is constructed here.

For two labels write the fine jet as `1+z_1 p_1+z_2 p_2+z_1 z_2 p_12`. If `h_12=p_12-p_1 p_2` is its connected coefficient, the exact update is

    h'_12 = M_k[h_12]
            + M_k[p_1 p_2]-M_k[p_1]M_k[p_2].

The second term is the integration-created connected defect. For an initial product, `h_12=0`; the defect generally survives. The full recurrence automatically retains it. For arbitrary degree the finite logarithm supplies

    h'_S = sum_(partitions pi of S) (-1)^(|pi|-1)(|pi|-1)!
           product_(B in pi) M_k[p_B],  S nonempty.

This is the finite cumulant identity, obtained by expanding `log(1+u)` in the nilpotent ideal; it asserts no analytic cluster convergence. If a marked logarithmic action is used, define it as `A_(k+1)+log(P_(k+1))` with the same vacuum `N_k`.

Changing instead to `N_k(z)=I_k[1;P_k]` multiplies the marked result by `P_(k+1)(1;z)^(-1)`. That alters the source jet. An exact representation of the original physical jet must restore each such source normalization, as well as vacuum prefactors and terminal integration. A vacuum division at the identity is not global Gibbs normalization.

Conditional Jensen yields coefficientwise `|M_k[p_S]|<=M_k[|p_S|]` and the finite coefficient-norm contraction, under H. It gives no strict polymer contraction, source locality, cutoff-uniform input bound, or positivity of individual cluster activities. The signed-piece and factorization counterexamples in035 still apply.

## Audit of historical YM-004 architecture

The old formulas are not premises. Its `L=2 or3` convention conflicts with the explicitly extracted CMP109 setup (`L` odd and greater than11). Its additive path average of a Lie-algebra connection is not the group-valued average constrained in(0.19); this extraction does not rule out linearized approximations in other coordinates. Its proposed quadratic `G(A,B)` and an independently appended Faddeev–Popov determinant are not the extracted exponential gauge factor; no equivalence was established. Its `exp(-S_next)` schematic misses the paper's logarithmic action convention and identity-background normalization unless those changes are explicitly translated. Its unique minimizer assertion omits the regular-orbit qualification.

The old running-coupling remainder bound, mass-counterterm language, numerical activity suppression, extensivity claim, and stopping threshold were not verified in the inspected source portions. Classify them **UNEXTRACTED/UNSUPPORTED_AS_PREMISES**, not falsified merely by absent extraction. The earlier title assignments for116 and119 are bibliographically incorrect, as the directly inspected publisher records show. This audit does not rewrite historical files or revoke their governance statuses.

## Exact residual and disposition

Partial source progress: CMP109(0.19) supplies a specified small-field map and supports the conditional marked algebra above. OPEN: complete gauge/measure dictionary (including predecessors defining averages and constrained integration), visually checked cutoff formula(2.9), full fluctuation-coordinate Jacobians and constraints, all large-field/R sectors from119/122, relation of reconstructed density to the original normalized Wilson measure, physical Wilson-flow insertion coordinates and tails, source counterterms, uniform activity norms, and terminal integration. No equality between this restricted map alone and035's full Wilson disintegration is asserted. Source-extraction gaps are access/scope gaps, not structural impossibility theorems. JET-002 remains OPEN; no uniform insertion estimate, continuum Yang–Mills construction, or mass gap follows.
