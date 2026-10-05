# YM-039 — attaining trees and degree-slack dictionary

Candidate audit, pending independent review. The partial 035/037/038 source findings remain bounded. This note identifies displayed trees but does not claim an exhaustive first-failure proof audit.

## Primary extraction (under 200 source-derived words)

Chandra–Chevyrev–Hairer–Shen, [Edinburgh manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/435998276/YangMills.pdf), printed59 and70 (PDF indices59 and70, including repository cover). Printed59 assigns deg(z)=2-kappa and deg(noise)=-5/2-kappa; its graphical legend uses circles for noise, thin kernel edges and thick differentiated kernel edges. Printed70, Lemma5.17's proof, displays a two-noise-leaf derivative tree for its minimum degree, printed -2-2kappa, and a three-noise-leaf tree for the first-criterion worst case, printed1-4kappa. Printed63, Lemma5.11,(5.12c), counts only noise slack -k_xi kappa; printed64 adds heat contributions2m in its proof. Printed73,(5.29), separately gives modelled-product exponents -2-4kappa. The tree drawings on printed70 were visually inspected from a direct full-PDF render. Printed67 already explains failure of naive integration in3D and its repair via LemmaA.4. Access: urllib403; ordinary PowerShell acquired the full PDF and supplied text/render inspection. No exhaustive intervening-definition or referenced-predecessor reconstruction is claimed.

## Independent arithmetic: two explicit assignments

Write b for assigned heat-edge degree, n=-5/2-kappa for noise degree, and a=b+n for a single heat-convolved noise branch. For the displayed unintegrated quadratic derivative form and cubic form, ordinary additive edge bookkeeping gives

    degree(quadratic derivative)=2a-1,
    third-criterion margin=(2a-1)+5/2,
    cubic first-criterion expression=3a+n+5.

These formulas concern the displayed branch forms under the specified additive assignment. They do not enumerate every relevant tree/subtree in Theorem2.15.

| Assignment | Single branch a | Quadratic degree | Third margin | Cubic first expression |
|---|---|---|---|---|
| Literal reduced b=2-kappa | -1/2-2kappa | -2-4kappa | 1/2-4kappa | 1-7kappa |
| Physical heat b=2 | -1/2-kappa | -2-2kappa | 1/2-2kappa | 1-4kappa |

The second assignment reproduces the two printed Lemma5.17 numbers. Lemma5.11 and its proof provide additional direct evidence of later heat-gain2 bookkeeping. This does not establish an explicit global assignment reset or identify the corresponding tree spaces and model topologies under a valid regrading theorem. The gap is a source-convention/transfer obligation, not a proof that the author theorem is false. The first row's positive margins for small kappa likewise do not independently certify all theorem hypotheses.

## Dimension diagnostic and its limits

For D spatial dimensions set n_D=-(D+2)/2-kappa. With b=2 the derivative third margin is2-D/2-2kappa and the cubic first expression is4-D-4kappa. With b=2-kappa they are2-D/2-4kappa and4-D-7kappa. Both assignments have positive displayed margins at D=3 and 0<kappa<=1/100; at D=4 both are negative. At kappa=0 both are zero in4D. These are our branch arithmetic, not a theorem prescribing a4D rule or proving nonconvergence.

Switching to b=2 therefore does not create a positive4D gain for these particular tests. A genuine regrading or endpoint argument must verify the complete/subcritical or replacement-rule prerequisites, all tree/subtree inequalities, covariance compatibility and the limit topology. It must also establish that the displayed candidate branches actually occur in the transferred construction. No such theorem is proved here.

## Disposition and next obligation

The visual attaining-tree locator is advanced; the exact relation of reduced source degrees, analytic kernel orders and the printed probabilistic proof remains unresolved. The source's initial-time integration failure already occurs in3D and cannot be mislabeled the earliest4D separator. First failing numbered statement of the entire proof remains UNESTABLISHED.

FA-001 stays a partial proof-local reconstruction. XFER-YM-BPHZ-GATE-038 remains conditional. Next atlas step is to inspect the tree-degree definitions and allowed homogeneity reassignments in the cited construction/BPHZ chain, then bind the two assignments to actual tree spaces and analytic model norms. No invariant measure, Wilson insertion estimate, local OS bridge, continuum edge or physical mass gap follows. STRUCTURAL_NO_GO_COUNT=0; goal_complete=false; Clay OPEN_AND_UNSOLVED; YM-016 BLOCKED.


## YM-041 candidate: numbered two-assignment model-norm gate

Primary text inspected: [Chandra-Hairer arXiv1612.08138v5](https://arxiv.org/pdf/1612.08138v5), printed12 equation(2.3), printed24 Definition2.32/Theorem2.33. This is a bounded locator audit; no visual verification of typography is claimed. Equation(2.3) adds type degrees and decoration contributions. Definition2.32 requires agreement of generated negative trees and their integer floors. Theorem2.33 additionally requires super-regularity and a strictly positive assignment gap for every negative tree, under its complete/subcritical-rule and cumulant assumptions, to obtain a model-distance moment estimate. The precise typeset repeated-assignment bullet in Definition2.32 remains unaudited; no silently corrected reading is imported.

Our conditional diagnostic: with unchanged decorations, raising only heat degree by kappa changes a tree degree by m*kappa, where m counts heat edges. A permitted bare-noise tree has m=0, hence gap0 and fails this particular strict-gap hypothesis. Thus heat-only reassignment cannot automatically invoke Theorem2.33 when such a tree is included. This does not refute other convergence routes or the authors' theorem. Actual tree inclusion, noise-slack adjustment, consistency, covariance norms and topology mapping remain OPEN; earliest numbered4Dfailure remains UNESTABLISHED.


## YM-042 candidate: finite noise-slack grading certificate

Own conditional lemma, using the source gate located in041; not a theorem about the authors' complete rule or an actual4D construction. Supply a finite nonempty family F of trees with unchanged decorations, heat-edge counts m>=0, noise-edge counts q>=1, and unpenalized degrees r in (1/2)Z. Set M=max_F(m+q). Choose 0<kappa<1/(2M). Compare book degree a=r-(m+q)kappa to analytic degree b=r-q*kappa/2, corresponding formally to restored heat order and reduced noise penalty. Then for each supplied tree:

    floor(a)=floor(b),
    a<0 if and only if b<0,
    b-a=(m+q/2)kappa >= kappa/2.

Proof: both shifts are positive and less than1/2. If r is an integer, both degrees lie strictly between r-1 and r and have floor r-1; their signs agree, including r=0 where both are negative. If r is a strict half-integer, both lie strictly between floor(r) and r and have floor floor(r); neither can cross zero. Subtracting gives the gap, including m=0 because q>=1. Thus adding noise slack can repair the bare-noise gap diagnosed in041 on this supplied finite family.

This certificate does not prove that F contains every tree generated by either assignment, that the rules generate the same family, or any complete/subcritical-rule, super-regularity, cumulant/kernel-norm or topology hypothesis. Positive-degree trees outside F can cross zero if their counts are unbounded. A q=0 tree at r=0,m=1 instead has a=-kappa<0 and b=0, so the noise-count premise cannot be omitted. This is a finite mapping certificate, not full Definition2.32 consistency or application of Theorem2.33.

Independent branch diagnostic with analytic heat2 and noise n_D=-(D+2)/2-kappa/2 gives derivative third margin2-D/2-kappa and cubic first expression4-D-2kappa. In4D they are -kappa and -2kappa, still strictly negative; at kappa=0 they are zero. A repaired finite assignment gap supplies no positive critical4D analytic margin. These are branch calculations, not all-subtree tests or a prescribed4D rule. Actual source/tree/model-norm correspondence and earliest numbered4Dfailure remain OPEN; no continuum or uniform-flow edge closes.


## YM-043 candidate: restricted equation-tree enumeration

Primary text reacquired at [Edinburgh YMH manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/435998276/YangMills.pdf), printed59 rule(5.6): the unextended production patterns are noise, a quadratic one-derivative interaction, and a cubic interaction. The source separately passes to a normal extension and completion. This audit uses text, not a new visual tree inspection. The following is our ordered scalar comparison grammar, not an enumeration of that completed rule.

Define solution templates H=I(N), I(H D H), or I(H H H); an equation template E is N, H D H, or H H H. Treat child positions as ordered, ignore component/derivative-direction labels, and include only these full-arity productions. D differentiates the specified child kernel once. If q counts noise leaves and v2,v3 count binary/ternary vertices including the equation root, then

    q=1+v2+2v3,
    m=q+v2+v3-1,
    derivative count=v2,
    r_D=2m-(D+2)q/2-v2=(2-D/2)q-3.

Proof: rooted-tree leaf counting; each solution child carries its outer heat edge, while the equation root has none. Each binary production adds exactly one derivative. Substitution gives the degree. These count identities concern exactly the stated syntax.

For book heat2-kappa and noise-(D+2)/2-kappa, a_D=r_D-(m+q)kappa. In3D choose 0<kappa<1/38. For q<=6, r_3<=0 and a_3<0. For q>=7, m+q<=3q-2 and

    a_3 >= (1/2-3kappa)q-3+2kappa
        >= 1/2-19kappa >0.

Thus negative membership in this restricted grammar is exactly q=1,...,6. The alternative analytic degree b_3=r_3-q*kappa/2 has the same negative membership under this bound. The number f_q of ordered templates satisfies f_1=1 and, for q>=2, f_q=sum_(i+j=q) f_i f_j +sum_(i+j+l=q) f_i f_j f_l, with positive indices. Counts for q1..6 are1,1,3,10,38,154:207 templates. Exhaustive syntax enumeration and exact rational degree checks at kappa1/100 confirm these counts. Their maximum M=m+q is16. Hence the supplied-family certificate042 applies because kappa<1/38<1/32=1/(2M). This is exhaustive for our defined ordered syntax only.

At D=4 the same comparison gives r_4=-3 for every q; each binary-chain template exists for arbitrary q and has m=2q-2, a_4=-3-(3q-2)kappa. Under this stipulated grammar and assignment the degrees are unbounded below for kappa>0. This records loss of finite negative-template power counting, not a theorem forbidding4D Yang-Mills or a prescribed completed4D regularity structure.

Normal-extension lower-arity terms, completion, decorated subtrees, polynomial nodes, type/component labels, gauge cancellations and actual model-norm/cumulant hypotheses are not audited by this207-template list. No claim of exhausting either authors' generated family, applying Theorem2.33, or locating the first numbered failure of the complete4D proof follows. Those source/completion mappings remain OPEN. Classification METHOD_SPECIFIC_OBSTRUCTION; structural no-go0; all continuum edges remain open.


## YM-044: slot-pruned comparison grammar and noise-free exclusion

Primary [Edinburgh manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/435998276/YangMills.pdf), printed59 rule(5.6), explicitly separates its initial multisets from the smallest normal extension and subsequent completion. This motivates the following OWN pruning comparison; it does not identify either author's extension/completion. Source text checked through public PDF; no new visual inspection claimed.

Retain any subset of ordered slots of a binary B or ternary C vertex, including none; at B its one differentiated slot contributes one derivative exactly when retained. Each retained slot has a child solution template and one heat edge, differentiated if that slot requires it. Equation roots have no extra heat edge. Noise N is a distinct leaf. Nullary B/C vertices stand for constants within THIS syntax; they are not asserted to be author symbols. No polynomial/decorated nodes, component labels, extra productions or derivative orders are included.

Let q count noises, v2,v3 all B/C vertices, d retained differentiated B slots, and delta=sum_B(2-retained_slots)+sum_C(3-retained_slots). Counting retained edges m gives

    m=q+v2+v3-1,
    q=1+v2+2v3-delta,
    e=v2-d>=0,
    r_D=2m-(D+2)q/2-d=(2-D/2)q-3+delta+e.

The tree is connected and every derivative is on a retained heat edge, hence d<=m. Assign a_D=r_D-(m+q)kappa and b_D=r_D-q*kappa/2. For q=0, r_D=2m-d>=m; consequently a_D>=m(1-kappa)>=0 and b_D=r_D>=0 when0<kappa<1. The nullary root has m=d=0 and both degrees zero. Thus this grammar's noise-free trees are never negative; the positive strict-gap certificate cannot apply to the zero tree (gap0), and we do not include it in the negative family.

For D=3 and q>=1, put r=q/2-3+delta+e and choose0<kappa<1/38. Since v2+2v3=q-1+delta, m+q<=3q-2+delta. For q>=7,

    a_3 >= (1/2-3kappa)q-3+2kappa+(1-kappa)delta+e >0,
    b_3 >= (1/2-kappa/2)q-3 >0.

For1<=q<=6 with r>0, half-integrality gives r>=1/2. Since delta<=r+3-q/2, m+q<=5q/2+1+r<=16+r. Therefore a_3>=r(1-kappa)-16kappa>=1/2-33kappa/2>0; b_3>=1/2-3kappa>0. When r<=0, both a_3,b_3 are strictly negative. This proves equality of negative membership throughout the stipulated pruned grammar: q>=1 and r<=0.

For that family, q<=6 and delta+e<=3-q/2. In particular delta<=2 forq1/2, <=1 forq3/4, and0 forq5/6; v2+v3<=q-1+delta. Total vertices q+v2+v3<=11 and M=m+q<=16. Each vertex has finitely many labels/retained-slot choices, so this is a finite family WITHOUT claiming its cardinality. The supplied-family042 certificate applies: q>=1, r half-integral and kappa<1/38<1/32=1/(2M), yielding equal floors, negative signs and b-a=(m+q/2)kappa>=kappa/2. Root deterministic checks exhaust all algebraically admissible count tuples with q<=6,v2+v3<=5, all retained derivative counts and pruning counts; those tuples are a superset, not an AST enumeration.

At4D r_4=-3+delta+e. The full-arity differentiated binary chains (delta=e=0) remain admissible for arbitraryq and retain a_4=-3-(3q-2)kappa. Adding slot pruning therefore cannot remove the unbounded-below diagnostic for THIS stipulated assignment. This is METHOD_SPECIFIC_OBSTRUCTION only; no universal no-go, actual4D model result or earliest numbered author proof failure follows.

This advances the lower-arity arithmetic boundary beyond043 but leaves actual normal-extension/completion correspondence, decorated subtrees, polynomial nodes, type labels, gauge cancellations and analytic/cumulant/kernel hypotheses OPEN. No continuum edge closes; structural no-go0.
