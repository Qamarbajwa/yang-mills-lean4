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
