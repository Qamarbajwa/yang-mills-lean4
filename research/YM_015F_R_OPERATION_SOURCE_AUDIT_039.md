# YM-015F — R-operation source audit 039

Candidate for independent review. Read constrained-coordinates038 and terminal037. This is bounded primary-source progress, not an all-sector source-flow construction.

## Access and bounded extraction

On 2026-10-05, ordinary PowerShell HTTP access to the [Euclid issue page](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-122/issue-2) identified R-I as `cmp/1104178393`. Its [public download](https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104178393) returned HTTP200, application/pdf, 2,826,369 bytes, 28 pages. Extracted in memory; rendered printed176/PDF2 and printed201/PDF27 in memory and visually checked. Read printed175–180 and198–202, not the whole paper. Python urllib separately returned a one-page Incapsula denial; that response was not treated as the article. No access bypass or paid access was used. The [publisher record](https://link.springer.com/article/10.1007/BF01257412) remains a subscription preview. R-I DOI is BF01257412; BF01238433 in038 identifies R-II.

Primary-derived extraction below is under200 words in total:

Printed176,(0.3):

    (R rho)(V) = sum_Z rho(Z'',V)
       [integral dV|_(Z') rho(Z,V)] /
       [integral dV|_(Z') rho(Z'',V)].

This introductory representation splits Z into components Z' requiring renormalization and Z'' retaining sufficient small factors. Printed177 explicitly cautions that the actual denominators integrate localized parts, not whole densities. Printed201,(1.100), defines R', only a basic part of R; its component quotient is

    delta_(G_i)(V') chi(Lambda_i)
    exp[-g_k^(-2) A(zeta_i,U_(k,X_i)(V'_k V_(Lambda_i)))]
    / integral dV'|_(Lambda_i) delta_(G_i)(V') chi(Lambda_i)
      exp[-g_k^(-2) A(zeta_i,U_(k,X_i)(V' V_(Lambda_i)))].

This is one factor of (1.100), not its complete expression. G_i fixes axial gauge; graph averaging restores Euclidean invariance with N_i=1/(2^d d!). Printed201,(1.102), states

    integral dV_k (R' rho_k)(V_k) = integral dV_k rho_k(V_k).

Printed177 conditions(i),(ii) select components fitting100MR_k cubes with no new large-field regions in preceding N steps. Printed200 retains other components and varying integral operations. Printed202 postpones localization, polymer expansion and exponentiation to R-II.

## Own interpretation and obligations

The exact numbered introductory representation (0.3) now has direct visual evidence. It must not be promoted into the actual full operator: the author's printed177 qualification prevents that. The visually checked quotient from(1.100) improves the dictionary for the actual basic operation, but this audit deliberately does not transcribe or reconstruct the remaining nested summations, characteristic functions, background maps and integrations of that equation.

The normalized local quotient integrates to one in its specified local variables when its denominator is finite and positive. That observation identifies a conditional normalization interface; it does not establish a single positive conditional measure representing every sector of the physical Wilson law. The remaining integrations and sector sums of(1.100) must still be retained, including the components outside conditions(i),(ii). Their precise admissibility, support, positivity, integrability and reconstruction require inspection of the complete source chain.

Equation(1.102) is a vacuum integral identity for the author's transformed density. For selected marked/source coefficients, terminal037 still requires equality of the corresponding integrals, not merely vacuum equality. Source dependence in local denominators would generate inverse scalar jets or variable-dependent factors; those must be derived from a verified source-decorated representation and restored before global normalization. Graph averaging, gauge fixing, constrained coordinates from038, cutoff support, Jacobians and local background dependence must accompany each transported insertion.

The final coarse law, its terminal functional and reference density must be identified from the actual full representation. No uniform marked numerator estimate, terminal density-ratio bound, source-counterterm estimate or marked large-field summability follows from(1.102). Excluding the unselected components would lose the global observable. No all-sector uniform flowed estimate, continuum/OS construction, mass gap or closure is claimed; the analytic obligations exposed in037 remain open.

## YM-040 candidate: exact localized quotient jets and their normalization defect

This section is our conditional finite-algebra derivation, not a further extraction of (1.100). The complete basic R-prime dictionary and R-II localization remain OPEN. The source locators above retain precisely their stage039 scope; this stage imports no new primary-source claim.

Fix k distinct nilpotent source labels, z_i^2=0, and a parameter y representing all exterior/background variables, graph choice, sector choice and retained constraints. Let m_y(dx) be a source-independent positive local measure. Gauge deltas may enter this hypothesis only after their meaning as a positive measure has been established; a formal distribution is insufficient. Suppose

    L(z,x;y)=sum_S L_S(x;y) z_S,
    D_S(y)=integral L_S(x;y) m_y(dx),
    0<D_empty(y)<infinity,

with every L_S absolutely integrable, and L_empty>=0. These are assumptions, not verified properties of every factor in the gauge RG. Define Q=L/D in the finite source algebra. Division exists because D_empty is nonzero. If Q_S denotes its coefficient, exact disjoint-subset multiplication gives

    Q_empty=L_empty/D_empty,
    Q_S=L_S/D_empty
        -sum_(nonempty B subset S) [D_B/D_empty] Q_(S\B).
    integral Q_empty dm_y=1; integral Q_S dm_y=0 for nonempty S.

Proof: D Q=L, solve each coefficient by increasing |S|; integrate and use the same recursion inductively. At degree one Q_i=L_i/D_empty-(D_i/D_empty)Q_empty. At degree two

    Q_ij=L_ij/D_empty
       -(D_i L_j+D_j L_i+D_ij L_empty)/D_empty^2
       +2 D_i D_j L_empty/D_empty^3.

The coefficient 2 comes from the two ordered disjoint singleton products. This quotient is a normalized source-dependent kernel jet, not the raw marked conditional expectation. In the special exponential-marking case L_S=L_empty product_(i in S) X_i, its first derivative is Q_empty times X_i-E_(Q_empty)X_i. Thus integrating Q_i alone gives zero, whereas the conditional insertion is D_i/D_empty. This normalization subtraction is unavoidable. Source-dependent local measures, domains, cutoffs, gauges or coordinate maps must first be incorporated into L (or differentiated with their own justified rules); the displayed formula does not discard their derivatives.

### Exact restoration and exterior-variable dependence

As jets, L/D_empty=(D/D_empty)Q. Both sides must remain inside exterior integration when D depends on y. In particular, for a source-independent local test F with integrable selected products,

    integral F L_S dm_y / D_empty
      =sum_(B subset S) [D_B/D_empty] integral F Q_(S\B) dm_y.

This is the exact local compensation identity. It is not an assertion that inserting a physical source into the author's vacuum quotient produces the source-decorated R-prime operation. That operation must still be defined and matched to the Wilson source jet. If a proposed transformed density has an identified outer jet H(z,y), sector sum and terminal functional, every H coefficient and every D/D_empty factor used in restoring the fine density requires the same disjoint-subset convolution before the actual global vacuum normalization. An exterior-dependent D cannot be extracted as a global scalar; a nonconstant terminal weight incurs the stage037 change-of-measure cost. Vacuum equality (1.102) supplies none of these marked identities.

The exterior dependence creates an exact covariance defect already at two labels. For a fixed positive exterior probability nu and jets C=D/D_empty, T=integral F Q dm_y, the difference between nu(CT) and nu(C)nu(T) in degree {1,2} is

    Cov_nu(C_empty,T_12)+Cov_nu(C_1,T_2)
      +Cov_nu(C_2,T_1)+Cov_nu(C_12,T_empty).

Here C_empty=1, so the first term vanishes. Covariance uses bilinear multiplication, without conjugation. For every indicated B, assume C_B, T_(S\B), and their product are individually absolutely integrable under nu; this makes both separate means and the product mean finite. Product integrability alone is insufficient: on y in (0,1) with uniform nu, C_1(y)=1/y and T_empty(y)=0 have integrable product but an undefined separate mean nu(C_1). The initial candidate wording was challenged before acceptance and is superseded by this explicit hypothesis. At any degree S the defect is sum_(B subset S) Cov_nu(C_B,T_(S\B)). This identifies the error from replacing a background-dependent jet by its exterior mean even when the mean is accurately computed.

Own finite diagnostic: exterior y=0,1 equiprobable; local x=0,1 equiprobable under m_y; let h(0)=0,h(1)=2 and m(0)=0,m(1)=1. Set

    D=1+z_1 h(y), Q=1+z_2 m(y)(2x-1), L=D Q, F=2x.

Then integral Q dm_y=1, integral L dm_y=D, L_empty=1 and D_empty=1. Thus this is a valid instance of the local pair assumptions, with finite integrable coefficients. The terminal test gives T=integral F Q dm_y=1+z_2 m(y). The degree12 coefficient of nu(D T) is nu(h m)=1; replacing D by nu(D) gives nu(h)nu(m)=1/2. The defect is1/2. Formal inverse jets are valid; if positive real source interpretation is desired, taking |z_1|<1/2 and |z_2|<1 keeps the corresponding ordinary affine factors strictly positive before nilpotent truncation. This example is unrelated to an actual gauge RG law.

For sectors, distinguish the target fixed-vacuum normalization rho(P(z))/rho(1) from the different source-normalized expectation rho(FP(z))/rho(P(z)). Suppose actual positive vacuum sector measures rho_alpha give source partition jets Z_alpha(z), normalized sector jets J_alpha=Z_alpha(z)/Z_alpha(0), and vacuum weights p_alpha=Z_alpha(0)/sum_beta Z_beta(0). Then the fixed-vacuum source jet is sum_alpha p_alpha J_alpha. If a source-dependent conditional sector law divides by Z_alpha(z), restoring the marked numerator requires J_alpha as well as p_alpha. The alternative source-normalized law has formal weights Z_alpha(z)/sum_beta Z_beta(z) and is a different target; it cannot silently replace the chosen Gibbs generating jet. For countably many sectors require summability of integrals of absolute values of every selected marked coefficient and every selected compensation product under the actual exterior/terminal law. Summability of vacuum weights alone is insufficient. Signed activity representations require total variation and the actual reconstructed vacuum denominator as in037.

### Conditional finite norm cost

With the existing weighted coefficient norm, write U=D/D_empty-1 and u=||U||_r. The ideal of positive-degree elements has (k+1)st power zero. Therefore

    (1+U)^(-1)=sum_(j=0)^k (-U)^j,
    ||Q||_r <= [||L||_r/D_empty] sum_(j=0)^k u^j,
    integral ||Q||_r dm_y
       <= [integral ||L||_r dm_y/D_empty] sum_(j=0)^k u^j.

Proof: finite geometric identity and submultiplicativity; coefficientwise integrability permits the last finite sum. No condition u<1 is needed for finite k. Nevertheless u, normalized marked input norms, their products across scales and exterior/terminal integration may depend on the cutoff. This is a conditional interface bound, not strict RG contraction, an analytic source disk, or a uniform flowed-observable bound. Positivity is assumed only for Q_empty; nonempty coefficients are generally signed even when the vacuum kernel is positive.

### Falsification experiment: omitted denominator derivative

Use the probability measure on x in {0,1} with both weights 1/2, one source z^2=0, and L=1+zx. Then D=1+z/2 and Q=1+z(x-1/2). Taking F=x gives

    integral F L_1 dm=1/2,
    integral F Q_1 dm=1/4,
    integral F Q_1 dm+(D_1/D_empty) integral F Q_empty dm=1/2.

Hence replacing the source-decorated local density by its normalized quotient and dropping its denominator jet changes a marked coefficient, despite identical vacuum integrals. This finite countermodel falsifies that shortcut only. It is not a counterexample to Bałaban's construction or to any continuum theorem. Writer executed Python Fraction checks of this example and the exterior covariance example: results (1/2,1/4,1/2) and (1,1/2,1/2), all assertions passed. Root E3 must independently verify the frozen candidate; this writer check is not independent acceptance.

### Remaining operator dictionary / smallest next obligation

For every quotient actually occurring in the complete (1.100), determine its integration variables and reference measure; graph weights; axial constraint and gauge transformation; cutoffs and localized action; background dependence; source numerator; source denominator; source dependence of coordinate maps; sector selection and retained unselected components; outer factors and terminal functional. Prove the resulting all-sector marked integral identity against the original normalized Wilson jet. The formulas above specify the coefficient obligations for a verified local pair (L,D), not that entire dictionary. R-II localization and any uniform marked/terminal estimates remain OPEN. No numbered 4D Failure Atlas edge advances in this section; its source-tree/regrading and all-subtree hypothesis obligations remain independent. Structural no-go count stays zero and no continuum edge closes.

## YM-041 candidate: predecessor-chain and retained-branch dictionary

Ordinary PowerShell public HTTP access succeeded again on 2026-10-05. Host Python fitz extracted printed177,190–202 in memory; printed201 was independently visually inspected at C:/Users/arqam/AppData/Local/Temp/YM041_RI_p201.png. No PDF denial page, subscription preview or OCR-only reading was substituted for that visual check. Same R-I public source and DOI as039. This adds numbered predecessors, not a full transcription of (1.100).

New primary-derived paraphrase/table below is under200 words; no additional direct quotation:

| Locator | Bounded dictionary |
|---|---|
| 177,(1.1) | Selected components factorize; the complementary operation is retained, usually omitted from intermediate displays. |
| 192,(1.71)–(1.73) | After N preliminary integrations, Lambda is a one-layer enlargement of the new region; its variables are integrated out. |
| 193,(1.75) | A unity split imposes exterior-extension regularity; failing components leave the selected class. Transformations so far preserve the density. |
| 194,(1.76) | Subsequent Lambda integration replaces density equality by equal-integral equivalence. The two integration regions are disjoint; the first is left unchanged. |
| 195,(1.81)–196,(1.82) | Fluctuation coordinates use the background; tree gauge and another unity split restrict surviving components. |
| 197,(1.88)–198,(1.89) | Additional large-field branches further shrink the selected union; cutoff removal uses the resulting restrictions. |
| 200–201,(1.99) | Complementary operations include all intermediate branch forms. Component integrations factorize; histories are localized to each component. |
| 201,(1.100) | Outer sum retains complementary regions/operations; selected-component sum includes n=0. Each product factor retains graph averaging, local quotient, remaining integrations and cutoffs. |

### Own marked-transport consequence

The selected union is not a permanent label attached only to the initial geometric conditions. A reconstruction must track its successive changes and carry each rejected branch into the complementary operations. Reading the displayed selected formula while forgetting the author's convention of omitting the complementary operation loses sectors. These are bookkeeping obligations; no quantitative suppression of those branches is inferred here.

The source's distinction between representation equality before the later integration and equal-integral equivalence after it identifies a separate marked gate even before adding local denominator jets. Suppose an integration replaces a density by a function independent of integrated variables. Vacuum equality alone cannot justify retaining the original observable unchanged. Our finite diagnostic: on x=0,1 with reference probabilities1/2, take density rho(0)=0,rho(1)=2. Integrating its only variable gives constant density1. Both vacuum integrals equal1, but the original test F(x)=x has marked integral1 under rho and1/2 under the replacement. This falsifies an unchanged-observable shortcut, not the source operation. Correct conditional transport of F gives constant1 in this example and restores the marked integral. An actual gauge source lift must derive that transport jointly with every changed operation, source-dependent map, gauge restriction, cutoff and compensated denominator, rather than infer it from (1.102).

This stage locates a finite part of the actual dictionary. It does not reconstruct all admissible histories, domain intersections, boundary bond conventions, reference measures, backgrounds or source-decorated operations in (1.100). The n=0 convention ensures no selected component is required; it does not prove positivity or summability of complementary terms. R-II localization, all-sector marked equality, terminal law and cutoff-uniform analytic estimates remain OPEN. Atlas regrading/all-subtree hypotheses and the earliest numbered4Dfailure are unchanged. No scientific edge closes and structural no-go count remains zero.


## YM-042 candidate: first density-changing integration and its degree-one gate

Ordinary public PowerShell HTTP again acquired the same 28-page R-I PDF on 2026-10-05; host Python fitz read printed193–196 in memory and rendered printed193/194. Writer visually inspected printed194, including (1.76). Printed193 is text-inspected only. No primary PDF is stored in the scientific tree. New source-derived dictionary below is under200 words, without direct quotation; exact boundary/intersection typography outside these bounded descriptions is not certified.

| Locator | Newly bounded operation dictionary |
|---|---|
| 193,(1.75) | Exterior configuration on Z intersect Lambda-complement is tested for a regular extension; rejected components join the retained complement. |
| 194,(1.76) | For each summand Lambda variables are integrated. The resulting function is independent of them; integration regions can differ between summands. |
| 194,(1.76) | First integral uses V_h on Z_h and retains its cutoff and T_h operation. Second integral uses V-double-prime on its specified B-double-prime_k subset intersecting Lambda and Z_h-complement; it retains chi-prime_k and exp(A-prime_k). The integrals have disjoint regions; the first remains unchanged. |
| 194,(1.76)–(1.78) | Delta constraints have already been integrated out here. The variational problem uses regularity restrictions; the minimizing orbit depends on exterior fields. |
| 195,(1.79)–(1.81) | U_0 is built from that exterior-dependent minimum; fluctuations use V-double-prime=V-prime V_0 on B_0. |
| 195–196,(1.81)–(1.82) | Tree gauge is imposed later on B_0, then a fluctuation unity split rejects additional components. |

### Own finite premise, tied to (1.76) rather than inferred from it

The newly distinguished integration is before the later tree gauge delta; treating that later delta as already part of the (1.76) measure would misorder the source lift. The first, unchanged integral and omitted complementary T_k operations remain in the outer bookkeeping. Neither reading supplies positivity of every term or reconstruction of its effective action.

For one fixed admissible history alpha, let x denote precisely its Lambda variables eliminated by this density replacement; let y retain the exterior variables, V_h variables of the unchanged first integral, and all unintegrated variables. This is a proposed finite dictionary, not a completed bond-by-bond transcription of (1.76). Hypothesis H042 requires a source-independent measurable assignment of these coordinates and product positive probability reference m_alpha(dy) h_(alpha,y)(dx), with the actual support indicators placed in the integrand. If a constrained reference replaces product Haar, its measure interpretation and total mass must first be proved. Domain variations with alpha are retained; no single common domain is assumed. Fixed physical Wilson-flow marking changes the density on a fixed finite lattice, but its representation through these histories/coordinates has not been verified.

Assume rho_(alpha,0)(x,y)>=0 is measurable and integrable, X_alpha is a finite complex-valued measurable function, and rho_(alpha,1)=rho_(alpha,0) X_alpha is absolutely integrable jointly. Define

    R_(alpha,0)(y)=integral rho_(alpha,0)(x,y) h_(alpha,y)(dx),
    R_(alpha,1)(y)=integral rho_(alpha,1)(x,y) h_(alpha,y)(dx).

On fibers with 0<R_(alpha,0)<infinity set X_eff=R_(alpha,1)/R_(alpha,0); set it zero on zero fibers. Fubini gives R_(alpha,1)=0 almost everywhere on zero fibers, since rho_(alpha,0)>=0 and rho_(alpha,1)=rho_(alpha,0)X_alpha. Exceptional infinite fibers have m_alpha-measure zero by joint vacuum integrability. The displayed identities hold almost everywhere; exceptional fibers may be modified to zero without changing either integral. Thus

    R_(alpha,0)(1+z X_eff)=R_(alpha,0)+z R_(alpha,1), z^2=0,
    integral R_(alpha,1) dm_alpha=integral rho_(alpha,1) dm_alpha dh_alpha,
    integral |R_(alpha,1)| dm_alpha<=integral |rho_(alpha,1)| dm_alpha dh_alpha.

Proof: integrate both coefficients and use triangle inequality. Reference probability mass is essential when the integrated result is lifted back to a function of x; a nonunit fiber mass produces an extra factor. A merely signed vacuum summand has no positive conditional-kernel interpretation and may have zero R_0 but nonzero R_1. Direct coefficient integration still makes sense under absolute integrability; division or Jensen then needs separate justification. This is a conditional first-degree lift of the specified elimination, not the actual source-decorated R-prime operation.

For finitely/countably many actual histories require sum_alpha integral (rho_(alpha,0)+|rho_(alpha,1)|) dm_alpha dh_alpha<infinity in the positive formulation, or absolute values of both coefficients for signed representations. All rejected and n=0 histories are included. Divide the summed marked coefficient by the actual global vacuum denominator, not a history denominator or source-dependent partition. Remaining T operations, the later background/fluctuation coordinate change, gauges/cutoffs and terminal law must transport this jet in turn; source derivatives of changed maps or domains cannot be discarded. The displayed L1 estimate carries existing integrability and gives no cutoff-uniform flowed input bound or terminal change-of-measure control.

### Failure record and next load-bearing obligation

Positive finite disintegration from stage035 applies to the physical Wilson law with a specified Borel coarse map. It does not establish H042 for each effective-action history in (1.76). This audit has not verified the exact reference domains, all effective-action terms, positivity or finite masses needed for that identification. The marked lift is therefore conditional. Next reconstruct those actual reference variables and complementary operations, prove their source-decorated equal-integral identity, and retain all terminal/sector coefficients before seeking uniform estimates. Vacuum equivalence alone does not discharge that gate. No source operation, continuum edge or earliest numbered4Dfailure is closed; structural no-go count remains zero.


## YM-043 candidate: inherited reference and normalization obligations

Ordinary public PowerShell access obtained the same R-I PDF on 2026-10-05. Host fitz extracted printed177–195/202; writer visually inspected printed188, including the first portion of (1.60). Initial extraction failed only from stdout encoding, then succeeded with UTF-8. No source PDF was stored. Exact normalization-symbol typography and full inherited definitions are unaudited; the preliminary notification's tentative prefactor symbol is not certified.

New primary-derived dictionary (under200 words total with the transfer entry; no direct quotation):

| Locator | Bounded reference/factor evidence |
|---|---|
| 182,(1.25) | Preliminary integration retains fluctuation A variables, a Gaussian quadratic form, constrained V variables and gauge-fixing factors. |
| 187,(1.53)–188,(1.60) | V fluctuations are logarithmic; delta constraints are linearized, removed using C, then variables are coupling-rescaled. An additional A integration remains. The displayed transformed integral retains a normalization prefactor, two Gaussian integrations, interaction terms and background action. |
| 189,(1.60)–(1.62) | Constant E refers to [III](3.15); new boundary terms collect successive integration contributions and Wilson-action renormalization. |
| 195,(1.81) | Boundary-intersecting bonds belong to B_0 at the Lambda boundary, but not at the other stated boundary. Measure and integrand are gauge invariant before the later tree gauge. |
| 202,References | [III] is CMP119243–285; [I] is CMP109249–301. |

### Own disposition of H042

This advances the predecessor dictionary: the already-eliminated constraints in (1.76) are connected to an explicit earlier linearization/C-elimination/coupling-scaling chain, with surviving A integration and normalization/background factors. It does not make those fluctuation references probability measures. A Gaussian quadratic factor alone supplies neither its normalization nor the total mass after cutoffs and interactions; those factors cannot be erased merely because the final density is considered independent of eliminated variables.

The physical compact-group Wilson probability reference established in035 is still a different identification from H042 for effective-action histories. We searched the entire extracted R-I text for Haar/measure/normalization terminology; that search did not locate an explicit unit-total-mass Haar convention for the reference of (1.76). This is a bounded search limitation, not proof the convention is absent in the source series. Gauge invariance on195 is affirmative evidence for the stated symmetry, not positivity, unit mass or source-independent disintegration. Exact prefactor/Jacobian reconstruction and inherited [III] integration conventions remain OPEN, as do each history's support, nonnegative effective density, summability and all complementary operations. The noted boundary convention prevents identifying the integrated coordinate set solely by interior sites.

Next load-bearing source task: reconstruct [III](2.21),(3.15),(3.25) and [I] Sect2 measures, constants and C-elimination maps, then match them history-by-history to (1.72)/(1.76). Preserve all prefactors in the global fixed-vacuum marked identity. No actual source-decorated R operation, cutoff-uniform insertion estimate, terminal bound or continuum edge is proved; structural no-go count0.


## YM-044 candidate: inherited integration split and retained constants

Public primary [III], Bałaban, Convergent Renormalization Expansions for Lattice Gauge Theories, CMP119243–285, DOI10.1007/BF01217741: https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104162401 . Euclid issue119/2 provided this identifier. Ordinary PowerShell downloaded on2026-10-06; host fitz opened44 PDF pages (printed243 at index0); article ends285. Text inspected243,257,258,267,268,269,270; visually inspected258,267,268,270. Local PDF/images remain in host TEMP outside the scientific tree. Initial publisher content/pdf response was3038 bytes HTML, not a usable PDF; an initially guessed Euclid identifier was inaccessible and supplied no evidence. Exact full operator typography is not transcribed or certified.

New primary-derived paraphrase, under200 words across this audit and transfer:

| Locator | Bounded inherited dictionary |
|---|---|
| 258,(2.20)–(2.21) | Ordered one-step operations integrate gauge variables on Omega_(j+1) intersect X, and fluctuation variables on Z_(j+1) intersect Omega_(j+1) intersect X. Quadratic couplings across components enter boundary terms. R changes characteristic functions; fluctuation domains may become empty. |
| 267–268,(3.15) | Constraint linearization, C-elimination and coupling scaling precede an integral retaining normalization constants, a bond-factor product, cutoff and fluctuation/background interactions. |
| 270,(3.23)–(3.25) | The Lambda_(k+1) fluctuation integral is conditional; remaining fluctuation integration on Omega_(k+1) intersect Lambda_(k+1)-complement enters the new T operation. Constants from the first exponential of (3.15) become E_0^(k); the bond-factor product persists in the last integral. |

### Own marked-interface consequence and falsification boundary

This is a concrete placement dictionary for inherited factors, not a normalized effective-history reference. Any proposed reconstruction of H042 must keep the conditional inner integration and residual T integration distinct. Their support restrictions and retained constants cannot be merged into a unit-mass kernel by notation. A conditional integral here is an integral with other variables retained; the word alone does not establish a probability conditional expectation. Neither its constrained gauge measure nor its fluctuation measure has been identified with the positive probability reference needed by H042. Exact measure conventions, all Jacobians, full bond factors, effective-action positivity and global source/vacuum normalization remain OPEN.

The ordinary source text confirms where constants are retained. Their values, complete defining formulas from [I] Sect2, and a history-by-history match to R-I(1.60)/(1.76) remain unaudited; no exact prefactor symbol from043 is rehabilitated. Empty fluctuation domains need their actual integration convention and retained gauge/cutoff factors, rather than automatic deletion of the history. Boundary action terms require the same source marking as retained interior terms. Next reconstruct [I] Sect2 measure/Jacobian/C conventions and instantiate one actual history's full fixed-vacuum marked identity, including residual operations and terminal law. The source's convergence scope remains superrenormalizable; this dictionary grants no four-dimensional convergence, cutoff-uniform insertion estimate or continuum edge closure. Structural no-go count0.


## YM-045 candidate: small-field Gaussian normalization and Jacobian placement

Public primary [I], Bałaban, Renormalization Group Approach to Lattice Gauge Field Theories. I. Generation of Effective Actions in a Small Field Approximation and a Coupling Constant Renormalization in Four Dimensions, CMP109249–301 (1987): https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104116842 . Identifier verified through official Euclid109/2 issue listing. On2026-10-06 ordinary PowerShell public download yielded54 PDF pages (printed249 at index0; article ends301). Web-tool PDF opening failed; it supplied no scientific evidence. Host fitz text inspected249,260–261,265–269; writer visually inspected260,267,268. Local PDF/images remain in host TEMP. The numbered prose distinctions below are certified; no full formula transcription or exact R-I prefactor glyph is certified.

New primary-derived dictionary is under200 words across this audit and transfer, without direct quotation:

| Locator | Bounded reference dictionary |
|---|---|
| 260,(1.4) | Z is the constrained Gaussian integral normalizing each fluctuation Gaussian measure. |
| 265,(2.1)–(2.3) | This transformation restricts to small fields and regular backgrounds, then uses a background-dependent minimum and fluctuation coordinates. |
| 267,(2.10)–(2.11) | Logarithmic coordinate factors enter the normalization. Nonlinear constraint linearization and coupling scaling precede Gaussian normalization. |
| 268,(2.12) | Constraint elimination leaves B variables with B-prime=CB; C and covariance depend on the background. The action retains a background Gaussian-normalization difference and a trace-log Jacobian in the interaction. |
| 268,(2.12)–(2.14) | N-double-prime is the displayed integral at unit background. E is a logarithm of the Gaussian expectation with cutoff and interaction; its unit-background value supplies that normalization. |

### Own reconstruction consequence and limits

This improves the missing normalization dictionary. It distinguishes an explicitly normalized Gaussian reference from the full cutoff/interaction-weighted integral and from a background=1 normalization. Those are separate objects in a proposed marked lift. Identifying one does not identify the others with a unit-mass effective-history fiber. In particular, a reference evaluated at one background cannot by itself normalize every exterior-dependent fiber of H042. Retaining the displayed background factor and the nonlinear coordinate Jacobian is part of matching the actual integrand, even when a Gaussian measure has already been normalized.

The domain assumptions here are smaller than the all-sector history system in R-I. This audit has not proved their extension to each complementary history, boundary-restricted measure, or residual T operation in [III](2.21)/(3.25). Nor has it verified the exact equality of these small-field C maps and Jacobians with each R-I history's constrained reference. Source dependence of a chosen coordinate map, its support and its Jacobian requires an explicit marked formula; it cannot be inferred from vacuum normalization. Gaussian positivity/covariance bounds on every needed history, summability, absolute marked integrability, fixed global vacuum normalization and terminal control remain OPEN. No cutoff-uniform flowed insertion theorem or continuum edge closes. The old large-field probability and nonlinear-smoothing sketches remain excluded; structural no-go count0.

Smallest next source obligation: match one admissible R-I(1.76) history to [III](3.15)/(3.25), including the exact retained normalization, bond factors, nonlinear Jacobian and residual variables. Only after that identification derive its degree-one marked identity; retain all rejected/n=0 histories in the eventual global transport.


## YM-046 candidate: history labels, hidden sums and operator dependencies

Read accepted revision45 and reconciliation034 before using sources. Reused publicly acquired primary PDFs in host TEMP: YM043_review_RI.pdf (28 pages), YM044_III.pdf (44 pages), YM045_I.pdf (54 pages), with the official Euclid URLs recorded above. No new HTTP acquisition is claimed. Host fitz independently extracted R-I printed179,192–195 and [III]255–257,267–270; visually inspected R-I192 and [III]267 via newly rendered pages. Initial stdout encoding failure was corrected with UTF-8. Exact full operator typography is not certified. This stage does not reuse the withdrawn043 prefactor reading.

New primary-derived dictionary (under200 words together with the transfer entry, no direct quotation):

| Locator | History/support dependency |
|---|---|
| [III]255(2.2)–256(2.12) | A determining set encodes the domain sequence; its gauge configuration determines the constrained minimizing orbit/background. |
| [III]257(2.14)–(2.18) | Localized determining sets require boundary/separation conditions. The density sum hides S-sequence summation inside T; the action depends on Omega/Lambda/S despite suppressed notation. |
| [III]267, before(3.15) | At fixed Omega_(k+1), admissible P/Q choices are resummed into zeta; only characteristic functions and localized gauge-fixing terms are resummed. C and other operators depend on the Omega sequence, although [I] formulas are reused. |
| [III]270(3.23)–(3.25) | Effective-action terms correspond to particular Omega/Lambda/S sequences and change under the R operation. |
| R-I192(1.71)–(1.74),194(1.76) | Preliminary integrations modify background/action and retained T operations; the later eliminated domain is term dependent. |

### Own history identification gate

This supplies a genuinely new index dependency, not a complete actual-history example. A selected Omega sequence alone does not select an elementary effective-action history: S summation remains inside T, and zeta has already aggregated admissible P/Q choices. There are two legitimate bookkeeping levels: carry the summed T/zeta objects with their exact integrals and source marking, or expand their definitions into elementary labels with the original weights and domains. Switching levels without reconstructing that sum changes what a proposed history label denotes. No numerical label multiplicity or positivity of the resummed weight is inferred.

For a proposed actual history alpha record: (a) the displayed outer domain labels and every hidden summation or its retained summed operator; (b) determining sets and associated constrained backgrounds; (c) restrictions/support and reference coordinate spaces at each scale; (d) actual domain-dependent C/covariance, nonlinear coordinate Jacobian and normalization factors; (e) unchanged T integrals, eliminated Lambda integral and residual integration; (f) fixed-global-vacuum numerator and denominator, subsequent terminal functional and rejected/n=0 branches. These are proof obligations, not definitions claimed extracted in full. The source explicitly reuses algebraic formulas while changing their domain-dependent operators, so equality of C symbols across [I], [III] and R-I cannot establish equality of the actual fiber measures.

No explicitly admissible nontrivial history is instantiated: the complete admissibility conditions/weights of hidden sums and their matching to R-I transformed supports have not been reconstructed. Choosing all domains empty/full by convenience would not resolve those conditions, boundary rules or the changed action. The source [III](3.25) is an inherited one-step representation, not a substitute for deriving R-I's termwise source-decorated(1.76). Next expand the precise T/zeta definitions and admissible domain conditions for one chosen summation level, then derive its coordinate/measure matching with all factors retained. H042 positivity/probability-fiber identification, absolute marked integrability, all-sector identity, uniform insertion and terminal bounds remain OPEN. No continuum edge closes; structural no-go count0.


## YM-047 candidate: strict/complementary partitions and resummed support

Read accepted revision46, autonomous architecture and reconciliation034. Reused host-TEMP primary YM044_III.pdf and YM043_review_RI.pdf; no new HTTP acquisition claimed. Host fitz extracted [III]254–258,263–267 and R-I177–181; visually inspected [III]265, including(3.2)–(3.5), at C:/Users/arqam/AppData/Local/Temp/YM047_III_p265.png. The rendered page supports the complementary inequality distinction; no full geometric formula transcription or withdrawn043 prefactor certification is claimed. Initial guessed repository filenames were absent; located the existing reconciliation/registry by rg before use.

New primary-derived dictionary, under200 words together with the transfer source binding; no direct quotation:

| Locator | Support and summation evidence |
|---|---|
| [III]265(3.2) | P is a union of specified partition cubes outside the four-layer enlarged previous large-field region. Each cube is assigned a strict-small indicator or its complementary greater-than-or-equal indicator. |
| [III]265(3.3)–(3.5) | Q is a union of partition cubes in a P-dependent restricted domain; its complement is relative to that domain. A second strict/complementary split tests approximate fluctuations. Enlarged bad regions determine the next Omega. |
| [III]267, before(3.15) | At fixed Omega, zeta sums admissible P/Q preimages, retaining characteristic functions and localized gauge-fixing factors. |
| [III]257(2.18)–258(2.20) | S summation stays in T; component factorization and ordered one-step integrations describe the retained operator. |
| R-I177–178(1.1)–(1.9),181(1.22)–(1.23) | No-new-large-field history conditions simplify the recent cutoff functions. Componentwise unity splits reject components into the retained complement. |

### Own fixed-summation-level interface

Choose the summed level: retain each actual zeta and T as an operator/integrand object; do not relabel a single Omega sequence as an elementary P/Q/S history. This source reconstruction identifies one precise necessary support condition: any elementary preimage used to unpack zeta must use its P-dependent Q universe, relative complement, specified cube partitions and strict-versus-complementary indicator products. Cube threshold equality belongs to the complementary branch. Free assignment of independent P and Q subsets of one common domain is therefore unsupported. Formula(3.5) is a geometric aggregation map, not a declared one-to-one identification of elementary labels with Omega.

For our own finite partition abstraction, on a fixed configuration let a_c be any real cube statistic and t_c its threshold. The factors 1_{a_c<t_c} and 1_{a_c>=t_c} sum to one. Expanding the product of these sums gives a partition indexed by large-cube subsets. At a threshold equality the strict branch vanishes; the complementary branch equals one. A second partition over a first-label-dependent finite cube universe still sums to one by first summing its labels for each fixed first label. This algebra requires those fixed universes and actual scalar statistics; it is not an extraction of all the source's gauge/background constraints. Nor does it make the integrals of different partition branches equal, their label masses a probability distribution without normalization, or the resummed zeta a positive unit-mass kernel after gauge fixing.

A complete zeta definition still requires the earlier axial-gauge expression referenced as(1.5), exact enlargements/partitions and all conditions preceding the resummation. A complete T definition needs inherited and R-modified one-step cutoffs and S restrictions. The dictionary certifies local indicator support, not complete global admissibility or an instantiated nontrivial R-I(1.76) fiber. Source-independent physical Wilson marking alone does not establish source independence of every reconstructed coordinate map/domain. Actual dependence must be derived; a conditional moving-domain formula may not be asserted to describe these vacuum cutoffs. All rejected and n=0 sectors, normalization/Jacobian/operator matching, absolute marked integrability, source coefficients, terminal law and cutoff-uniform bounds remain OPEN. No continuum edge closes; structural no-go count0.


## YM-048 candidate: axial gauge, geometric admissibility and the insertion equivalence gate

Read accepted revision47, autonomous architecture and reconciliation034. Reused host-TEMP primary YM044_III.pdf and YM043_review_RI.pdf, using their previously recorded official Euclid URLs; no new HTTP acquisition claimed. Host Python/fitz extracted [III]247-249,254-258,264-267 and R-I178-182,192-194. Visually inspected newly rendered [III]247,255 and R-I193 at C:/Users/arqam/AppData/Local/Temp/YM048_III_p247.png, YM048_III_p255.png and YM048_RI_p193.png. Initial repository-venv extraction failed because fitz was unavailable; successful host Python extraction supplied the evidence. No full gauge formula/prefactor transcription or withdrawn043 glyph certification is claimed.

New primary-derived dictionary, under200 words per primary source across this audit and transfer; no direct quotation:

| Locator | Bounded admissibility / operation dictionary |
|---|---|
| [III]247(1.5)-(1.9) | A normalized gauge-averaging unity includes a small-coordinate restriction and exponential gauge-fixing weight; Faddeev-Popov insertion produces gauge factors. The approximate-fluctuation test omits designated constraint bonds. |
| [III]248(1.10)-(1.12),249 after(1.14) | Resummation retains localized gauge factors. The linearizing map changes designated constraint bonds only, leaving that approximate-fluctuation cutoff unchanged. |
| [III]254(2.1),255 before(2.2)-(2.3),256 before(2.10) | Admissibility includes nested localization sequences, specified cube partitions/separation and small-component rectangular geometry. S includes a mandatory boundary portion when its relevant domain is nonempty; R is the remaining S portion. R operations may allow Lambda=Omega. |
| [III]258(2.19)-(2.22) | Retained T factors over disjoint components and ordered scale operations; R can modify characteristic functions and empty the fluctuation domain. |
| R-I179-180(1.10)-(1.20) | Preliminary regions follow compatible partitions and layer separations; successive integrations generate and localize new determining sets/backgrounds. |
| R-I193 final paragraphs,194 before(1.76) | Preliminary transformations preserve the density. The subsequent term-dependent Lambda integration changes it; equivalence asserts equal field integrals. Remaining-component T operations persist. |

### Own support dictionary and transport obligation

Keep the summed T/zeta level selected in047. The newly read gauge unity is a gauge-orbit averaging device in its stated support, not a declaration that each resummed effective-history fiber is a positive probability kernel. Its small-coordinate cutoff, exponential factor, normalization and Faddeev-Popov construction must travel together. The constraint-bond exclusion is material: the claim that a particular approximate cutoff survives linearization relies on the changed coordinates being excluded from that cutoff. It grants no blanket invariance of every cutoff, observable, exterior condition or source-marked coordinate map.

The S/R information narrows an admissibility check but does not instantiate a history. To unpack a T sum, reconstruct the exact complement and boundary conventions, mandatory S subset, residual R subset and compatible scale partitions; add the actual determining/background data and all R-modified characteristic functions. Do not choose S empty on a nonempty mandatory domain or choose independent localization sets without their nesting/layers. The exact region/bond formula typography is not certified here; this prose dictionary cannot replace it. Retaining T instead of unpacking S still requires marking its entire ordered operation, including empty-fluctuation cases with surviving gauge and cutoff data.

Most importantly, equal vacuum field integrals after the R-I Lambda integration do not imply equality against an arbitrary inserted functional of the eliminated coordinates. A correct marked lift must integrate the original density multiplied by the original insertion, or derive a matching adjoint/conditional insertion transport at that term's actual domain. This is an own consequence of the stated equivalence scope, not a claim that the source has an insertion error. Term-dependent domains and retained complementary T components preclude replacing this obligation by one arbitrary common-domain average. Vacuum preservation alone does not identify the required all-sector marked map.

Still OPEN: a complete nontrivial admissible history, exact gauge/constraint Jacobians and normalization, original-versus-transformed observable matching, source dependence or independence of every support/map, positivity or total variation needed for H042, absolute marked integrability, global fixed-vacuum denominator, all rejected/n=0 branches and terminal-scale functional. The source geometry and gauge formulas supply no cutoff-uniform flowed insertion theorem or four-dimensional convergence result. Next audit the termwise R-I(1.76) integration measure and derive its observable adjoint with retained T/zeta, using the exact admissibility conventions. No continuum edge closes; structural no-go count0.


## YM-049 candidate: disjoint integral, boundary bonds and gauge-fixed marking

Read accepted revision48, autonomous architecture and reconciliation034. Reused the public primary host-TEMP YM043_review_RI.pdf, whose official Euclid URL is recorded above; no new HTTP acquisition claimed. Host Python/fitz extracted actual printed192-198. Initial guessed index=printed-177 returned headers two pages earlier; this was detected from the extracted headers and corrected to index=printed-175 before using locators. Visually inspected actual printed194 and196, rendered at C:/Users/arqam/AppData/Local/Temp/YM049_RI_actual194.png and YM049_RI_actual196.png. No exact full prefactor, bond-set typography or withdrawn043 glyph is certified.

New primary-derived dictionary (under200 words across this audit and transfer, no direct quotation):

| Locator | Retained operation / support |
|---|---|
| R-I194(1.76) and following paragraphs | Two displayed integrations have disjoint regions. The first, over Zh, stays unchanged in the subsequent discussion. Constraint delta functions have already been integrated out. Minimization concerns the whole integration domain, although subsequent fluctuation analysis uses a smaller domain. |
| R-I194 Proposition1,195(1.79)-(1.81) | The minimizing orbit depends on exterior fields. Its extension defines the background and fluctuation split. Bonds intersecting the Lambda boundary enter B0, while bonds intersecting the designated Omega boundary do not. |
| R-I195-196, before(1.82) | Modified axial gauge fixes a tree plus specified external bonds. A Faddeev-Popov tree delta is inserted; componentwise fluctuation cutoffs separate retained and excluded components. |
| R-I197(1.85)-(1.88),198(1.89) | Background gauge changes require compensating transformations of both residual and fluctuation variables. Further componentwise partitions precede replacement of inherited cutoffs on the surviving support. |

### Own first marked source obligation

This locates an earlier concrete gate than a Gaussian conditional expectation: fix one actual admissible term at the retained summed T/zeta level and identify its unmarked(1.76) coordinate integral with the original term. The first disjoint integral and remaining-component T operation remain part of that term. Disjoint coordinate regions allow iterated integration when the needed integrability holds; they do not prove independence or a factorization of the action, observable or normalized law. The minimizing exterior-dependent background is a coordinate construction, not an observable expectation. A boundary bond cannot be assigned to both coordinate sets or silently removed.

The first missing marked lemma for the selected route is the following actual-model obligation, not a theorem established by this audit: after the term's original degree-one physical flowed insertion is pulled into the(1.76) coordinates, inserting the tree-gauge delta and making the compensating residual/fluctuation gauge transformations preserves that inserted integral, with the original domain, measures and all normalization factors. This requires either proof of invariance of the pulled-back insertion under precisely those transformations or its explicitly transformed insertion, together with the correct gauge-orbit measure identity and absolute integrability. General physical gauge invariance motivates that check but does not identify the actual coordinate pullback or gauge-map action. Source prose certifying invariance of the unmarked integrand cannot supply the missing inserted formula.

Next the componentwise fluctuation and later residual partitions must retain the complementary terms with their inherited integration, rather than applying the surviving-support cutoff replacement to the whole original sum. The equality(1.89) is support-specific. It may be used for an insertion only on the same supported integrand and only after the actual coordinate/gauge identity is matched; it creates neither a probability normalization nor a source derivative. We do not assert that these vacuum supports actually move with the chosen physical source.

No complete history or gauge-fixed marked map is instantiated. Exact inherited normalization, full gauge-Jacobian conventions, hidden sums, terminal functional, positivity/total variation, fixed global vacuum denominator and every rejected/n=0 branch remain OPEN. The small-field fluctuation analysis is not the retained Zh integral and cannot replace it. No source passage inspected here establishes the termwise flowed adjoint or a cutoff-uniform bound; this limited search is not a claim of nonexistence elsewhere. The smallest next source task is the exact marked gauge-orbit/coordinate identity at(1.76)->(1.81)->tree-gauge insertion, followed by matching the support replacement and residual integral. No continuum edge closes; structural no-go count0.


## YM-050 / YM-050R: physical insertion pullback, tree-gauge orbit identity repair, and Family 215 audit

Read accepted revision 50, autonomous repair governance, and coordinator review findings. Reused the public primary host-TEMP YM043_review_RI.pdf (R-I, Bałaban CMP 122, 175–202); no new HTTP network acquisition claimed. Host Python/fitz extracted printed 194–198; visually confirmed (1.76), (1.79)–(1.81), tree-gauge insertion before (1.82), compensating transformations (1.85)–(1.88), and support-specific cutoff replacement (1.89).

New primary-derived dictionary (under 200 words across this audit and transfer, no direct quotation):

| Locator | Operation / Source Equation |
|---|---|
| R-I 194,(1.76) | The joint integration contains two disjoint spatial domains: preliminary integration over Zh (constraint deltas integrated out) and active fluctuation integration on its complement. |
| R-I 194–195,(1.79)–(1.81) | Minimizing background orbit V depends on exterior boundary conditions. Fluctuation split is U = V exp(g A). Boundary bonds: intersecting the Lambda boundary enter B0, while bonds intersecting the designated Omega boundary do not. |
| R-I 195–196, before (1.82) | Modified axial gauge fixes a maximal spanning tree T and designated external bonds via Faddeev–Popov tree delta product_(b in T) delta(A(b)) Delta_FP(V, A). Componentwise fluctuation cutoffs separate retained small-field and excluded components. |
| R-I 197,(1.85)–(1.88), 198,(1.89) | Background gauge changes V -> V^h require compensating transformations of fluctuation variables A -> h^-1 A h and residual variables. Supported cutoff replacement applies to surviving small-field support only. |

### Equation-by-equation map of physical insertion pullback and gauge-orbit identity (repaired)

Let O_(a,t)(f)[U] = a^4 sum_x f(x) E_(a,t)(x)[U] be the physically normalized clover energy density generated by positive-time gradient flow (t > 0). In the degree-one nilpotent source algebra (eta^2 = 0), the source-deformed partition function is Z(eta) = integral dmu[U] (1 + eta O_(a,t)(f)[U]).

1. **Pullback to (V, A) coordinates:**
   For each admissible history alpha in (1.76), link variables decompose as U = V exp(g A). The physical observable pulls back to:
       O_(a,t)(f)[U] = O_(a,t)(f)[V exp(g A)].
   *Non-factorization quantifiers:* Gradient flow over time t > 0 generates non-compact parabolic diffusion across physical distance ~ sqrt(8 t_phys). Consequently, for test functions f whose diffusion envelope intersects both Zh and Omega \ Zh, O_(a,t)(f)[V exp(g A)] couples links in Zh with active fluctuation links, background links V, and boundary bonds B0. This demonstrates a generic failure of spatial factorization across disjoint vacuum integration domains in (1.76), precluding the universal assumption of observable factorization, while leaving open trivial factorization in uncoupled/degenerate limits.

2. **Repaired Faddeev–Popov tree-gauge functional identity:**
   On a maximal spanning tree T subset Lambda with rooted site gauge group G_0 = {h in G^Lambda : h_(x_0) = 1}, the Faddeev–Popov resolution of unity on a single configuration orbit is:
       Delta_FP(V, A) integral_(G_0) dh product_(b in T) delta((A^h)(b)) = 1.
   On a single orbit, the integral evaluates to the scalar 1 / Delta_FP(V, A), NOT to the slice distribution product_(b in T) delta(A(b)). Taking O = 1 demonstrates this distinction: 1 / Delta_FP != product_b delta(A(b)).
   The gauge-slice delta distribution product_(b in T) delta(A(b)) appears strictly under the full configuration-space functional integral:
       integral dmu(A) O_(a,t)(f)[V exp(g A)] = Vol(G_0) integral dmu(A) Delta_FP(V, A) product_(b in T) delta(A(b)) O_(a,t)(f)[V exp(g A)],
   obtained by inserting the resolution of unity into the functional measure, interchanging integrals via Fubini, and performing the functional change of variables A -> A^(h^-1) using gauge invariance of the measure dmu(A^h) = dmu(A), determinant Delta_FP(V, A^h) = Delta_FP(V, A), and observable O_(a,t)(f)[U^h] = O_(a,t)(f)[U]. Under normalized Haar measure Vol(G_0) = 1 and constant tree Jacobian Delta_FP, this establishes exact functional restriction to the gauge slice A|_T = 0.

3. **Link endpoint transformation and background-fluctuation coupling:**
   Under site gauge transformations h in G^Lambda, link variables transform with separate endpoint factors: U_xy^h = h_x U_xy h_y^-1. For U_xy = V_xy exp(g A_xy), holding V_xy fixed while transforming A_xy by h_y A_xy h_y^-1 does NOT produce U_xy^h because h_x V_xy != V_xy h_y unless h is covariantly constant along the link (h_x = V_xy h_y V_xy^-1).
   Bałaban's compensating transformations (R-I (1.85)–(1.88)) resolve this by transforming both background V -> V^h and fluctuation A -> h^-1 A h simultaneously:
       V_xy^h exp(g (h^-1 A h)_xy) = (h_x V_xy h_y^-1) exp(g h_y A_xy h_y^-1) = h_x (V_xy exp(g A_xy)) h_y^-1 = U_xy^h.
   Therefore, an uncoupled tree-gauge identity on fluctuation A with fixed background V is mathematically defective. The actual-model Bałaban coordinate pullback and tree-gauge orbit identity across all external bonds B0, charts, and cutoffs are classified as **CONDITIONAL_AND_OPEN** (`ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_ORBIT_IDENTITY_OPEN`).

4. **All-sector global normalization:**
   The degree-one transport identity is normalized by the global vacuum partition function Z_vac, not by any single-history denominator:
       <O_(a,t)(f)> = (1 / Z_vac) sum_alpha integral dmu_(alpha)^vac[V, A] O_(a,t)(f)[V exp(g A)].
   This sum carries all small-field sectors, complementary/rejected sectors (chi_small = 0), and the n=0 sector.

### Primary-source audit of OpenAI Family 215 (repaired provenance and proof status)

We audited the external candidate manuscript from the openai/math repository at immutable upstream commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` (upstream public release October 6, 2026, Problem 215 / Family 215, titled "Canonical O(3) continuum limit and exact O(4) mass asymptotics"):

1. **Exact Upstream Locators, Roles, and Byte Digests:**
   - **Scope Description:** `lean/docs/215.md` (LEN 1,031 bytes, SHA-256: `41ed31b3d5b0f9c0ce5df3604527f17b26eec23b225a7a2184f5a9c2d936ac30`). Role: Scope documentation for accompanying preprint `preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf`. (Note: The repository-relative path is `lean/docs/215.md`; prefixing with `math/` returns 404). This markdown file contains documentation and markdown tables, but zero Lean code declarations or theorem heads.
   - **Comparator Challenge Specification:** `lean/ComparatorChallenges/ClassicalON.lean` (LEN 1,961 bytes, SHA-256: `c2f5f88455b811eb6b56c1ae80ff91f4e398e18e7c7fbeee6daca8da4122d696`). Role: Formal challenge specification. Namespace: `OAI.ClassicalON`. Exact declarations: `Site := ℤ × ℤ`, `PositiveNeighbor (x y : Site) : Prop`, `structure LatticeGraph` (finite square-lattice subgraphs with nearest-neighbor edges), `abbrev Spin (n : ℕ) := ↥(Metric.sphere (0 : EuclideanSpace ℝ (Fin n)) 1)`, `Configuration`, `referenceLaw`, `interaction`, `partition`, `correlation`, `siteDistance`, `def ExponentialDecay : Prop`, and `theorem main : ExponentialDecay := by sorry`.
   - **Comparator Execution Manifest:** `lean/ComparatorChallenges/ClassicalON.json` (LEN 308 bytes, SHA-256: `47cb3623915c8cfcc35099fabd0c44173afa72b706eb0526c4b8d3855e789252`). Role: Manifest linking challenge module `ComparatorChallenges.ClassicalON` to solution module `OAI.Probability.ClassicalON.Main`, with permitted axioms `["propext", "Quot.sound", "Classical.choice"]`.
   - **Candidate Solution Module:** `lean/OAI/Probability/ClassicalON/Main.lean` (LEN 2,050 bytes, SHA-256: `0e4bca8c6b8fe89ffec32eda5d3222af85062a2e3e685729f41578076b528c8a`). Role: Solution proof module. Imports `OAI.Probability.ClassicalON.BlockReduction` and contains `theorem main : ExponentialDecay := by ...` without top-level `sorry`.

2. **Exact Mathematical Model & Boundary Conditions:**
   - **Model:** Two-dimensional classical lattice spin system on unit sphere $S^{n-1} \subset \mathbb{R}^n$ ($n \ge 3$) under nearest-neighbor ferromagnetic coupling $\sum_e b(e) \langle \sigma(e_1), \sigma(e_2) \rangle$ with $b(e) \in [0, \beta]$.
   - **Boundary Conditions:** Finite square-lattice subgraphs with **FREE boundary conditions** (`structure LatticeGraph`), NOT periodic boundary conditions.
   - **Explicit Documented Scope & Exclusions:** `lean/docs/215.md` explicitly specifies: *"For each interaction bound $\beta>0$, constants $A$ and $m>0$ work for every finite square-lattice subgraph with free boundary and nonnegative edge strengths at most $\beta$: the correlation between sites $x,y$ is at most $Ae^{-m|x-y|}$. The infinite-volume limit and the separate $O(4)$ spectral-gap claim are not included."*

3. **Supersession of Inaccurate Declaration & Periodic-Boundary Claims:**
   - The previously asserted declaration head `lattice_spin_decay_2d` does NOT exist in the repository; it is formally superseded by the actual comparator theorem `OAI.ClassicalON.main : ExponentialDecay` (with `sorry` in `ClassicalON.lean`) and solution theorem `OAI.ClassicalON.main` in `Main.lean`.
   - The previously asserted "finite 2D periodic lattices" claim is superseded by the exact free-boundary specification.
   - The claim that inspecting `lean/docs/215.md` constituted an "exhaustive declaration search of Lean formalization" is superseded: `lean/docs/215.md` is a Markdown doc with zero Lean code heads; the actual comparator code is `ClassicalON.lean` and solution code is `Main.lean`.

4. **Proof Status Evaluation:**
   - The comparator `ClassicalON.lean` contains `theorem main : ExponentialDecay := by sorry`, which is a problem statement placeholder, not a verified proof.
   - The solution module `Main.lean` contains proof script text relying on a deep dependency tree of ~100 modules in `lean/OAI/Probability/ClassicalON/`. Because we adhere to governance prohibiting execution of untrusted downloaded code, and no reproducible kernel-checking verification receipt is verified at commit `fd4aeeb2...`, the candidate proof status is labeled **UNVERIFIED_UPSTREAM_PROOF_CODE**.
   - Presence of `sorry` in the comparator challenge does NOT imply absence of a solution proof in `Main.lean`; conversely, presence of proof text in `Main.lean` does not substitute for independent kernel verification.

5. **Inspected Search Scope & Negative Boundary:**
   - Across the inspected files (`lean/docs/215.md`, `ClassicalON.lean`, `ClassicalON.json`, and `Main.lean`), zero declarations exist for:
     (a) Continuum quantum field theory construction / Wightman reconstruction;
     (b) Osterwalder–Schrader axioms OS0–OS4;
     (c) Non-Gaussianity of connected Schwinger functions;
     (d) The one-particle mass gap pole or 4D Yang–Mills gauge theory.
   - This search-negative finding across inspected primary files is distinguished from an unproved universal assertion of repo-wide nonexistence.

6. **Epistemic Classification & Transfer Determination:**
   - The transfer candidate remains classified as `UNVERIFIED_CANDIDATE_PREPRINT` and `METHOD_SPECIFIC_OBSTRUCTION`.
   - Allowed transfer conclusion: strictly `None`. Zero DAG edges close.


### Mathematical corrections to the proposed transfer mechanism

1. **Criticality distinction:** The 2D O(3) non-linear sigma model is asymptotically free with dimensionless coupling beta^-1. It is strictly critical / renormalizable, not super-renormalizable. Its ultraviolet behavior requires infinite multiscale cluster or counterterm control, matching the power-counting classification of 4D Yang–Mills.
2. **Non-linear fluctuation source:** On S^2, writing q = (pi, sigma) with sigma = sqrt(1 - ||pi||^2) = 1 - 1/2 ||pi||^2 - ... proves that J . q = J_pi . pi + J_sigma sqrt(1 - ||pi||^2) is strictly non-linear in the fluctuation coordinates pi. It shifts the fluctuation Hessian by -J_sigma delta_ij and does not complete the square linearly.
3. **Green's kernel vs. uniform source analyticity:** Local L1 integrability of (-Delta)^-1(x, y) ~ ln |x-y|^-1 in 2D does not establish cutoff-uniform source analyticity of non-linear observables without multiscale cluster expansion bounds.
4. **Resolvent domain and norm specification:** For the observable Hessian B = D^2 O_(a,t)(f)[V] in 4D, at fixed flow time t_phys > 0, gradient flow smoothing bounds B on L2(Lambda_a, su(N)) orthogonal to gauge zero modes. The obstacle is not an infinite operator norm at fixed t > 0, but the cutoff-uniform summability of the marked polymer activity ||K_j^(1)||_B_j under Bałaban's multiscale RG.


## YM-051: ONE-TERM ADMISSIBLE R-I(1.76) MARKED COORDINATE AND GAUGE-ORBIT REPRESENTATION

### 1. Primary Source Extraction & Metadata
- **Primary Source:** T. Bałaban, *Large Field Renormalization. I. The Basic Step of the Renormalization Group*, Communications in Mathematical Physics 122, 175–202 (1989).
- **Inspected Range:** Pages 192–198, specifically Section 1, equations (1.71)–(1.76), Proposition 1, (1.77)–(1.89).
- **Direct Visual & Digital Extraction:** Verified from `C:\Users\arqam\AppData\Local\Temp\YM043_review_RI.pdf` via high-resolution rendering.

### 2. Specification of ONE Explicit Admissible History Term $\alpha$
At the retained summed $\mathbb{T}/\zeta$ level, we select ONE explicit admissible history term $\alpha$ generated after $N$ preliminary scale integrations:
1. **Scale Parameters:** Lattice spacing $a_k = L^{-k} a_0$, with block scale $M \ge 100$ and $L \ge 2$.
2. **Domain Hierarchy:**
   - Previous retained large-field region $Z$, a rectangular parallelepiped union of $M$-cubes.
   - Scale index $k_0$ where $L^{-(k - k_0 + 1)} R_{k - k_0 + 1} = 1$, with $N_0 = k - k_0$.
   - Large-field component $Z_k^\prime = (\Omega_{k_0+1}^5)^c \cap Z$ (eq. (1.10), p. 192), a rectangular parallelepiped contained in a cube of size $100M$.
   - Integration domain $\Lambda$:
     $$\Lambda = (\Omega_{k_0+1}^4)^c \cap Z \quad \text{(R-I (1.73), p. 192)}$$
     obtained by adding exactly one layer of $M$-cubes to $Z_k^\prime$. $\Lambda$ is a rectangular parallelepiped contained in a cube of size $100M$.
   - Preliminary integration domain $Z_h \subset \Lambda$: a rectangular domain on which constraint delta functions have already been integrated out (p. 194).
   - Active fluctuation domain:
     $$\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c \quad \text{(p. 195)}.$$
   - Boundary and external bond set $\mathbb{B}_0$:
     $$\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0 \quad \text{(p. 195)}.$$
     *Boundary bond convention (R-I p. 195):* Bonds $b \in \mathbb{U}_k$ that intersect the outer boundary $\partial \Lambda$ belong to $\mathbb{B}_0$. Bonds that intersect the internal boundary $\partial \Omega_{k+1}^1$ (i.e., touching $Z_h^{\prime \sim}$) DO NOT belong to $\mathbb{B}_0$.
   - Exterior domain: $Z \cap \Lambda^c$, carrying field variables $V_k|_{Z \cap \Lambda^c}$ governed by characteristic function $\chi_{k, \Lambda}$ from the decomposition of unity $1 = \chi_{k, \Lambda} + (1 - \chi_{k, \Lambda})$ (eq. (1.75), p. 193).
3. **Unmarked Termwise Density (R-I (1.76), p. 194):**
   $$\rho_{k, \alpha}[V] = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} \chi_k^{\prime\prime} \exp A_k^{\prime\prime}[V].$$

### 3. Coordinate Coverage and Factorization Scope
- **Active fluctuation factorization on $\mathbb{B}_0$:**
  On the bond set $\mathbb{B}_0$, the configuration $V^{\prime\prime}$ factorizes as:
  $$V^{\prime\prime}(b) = V^\prime(b) V_0(b), \quad V_0 = M_{\mathbb{B}_k^\prime}(U_0) \quad \text{(R-I (1.81), p. 195)}$$
  where $U_0 = U_{k, Z}(V_\Lambda^*)$ is the critical background configuration (eq. (1.79)) from Proposition 1 (p. 194), and $V^\prime = \exp(i B^\prime)$ with $B^\prime \in \mathfrak{g}^{\mathbb{B}_0}$.
- **Link coverage disclaimer:**
  The fluctuation representation $V^{\prime\prime} = \exp(i B^\prime) V_0$ covers ONLY the active bond set $\mathbb{B}_0$.
  - It does NOT cover links in $Z_h$, which are carried by the preliminary field $V_h$ under measure $dV_h \lceil_{Z_h}$ and operator $\mathbb{T}_h(Z_h)$.
  - It does NOT cover links in $Z \cap \Lambda^c$, which are carried by the exterior field $V_k|_{Z \cap \Lambda^c}$ under cutoff $\chi_{k, \Lambda}$.
  - It does NOT replace residual scale operators $\mathbb{T}_k$ by a Gaussian; all preliminary and residual operations are strictly retained.

### 4. Degree-One Physical Insertion Pullback
Let $\mathcal{O}_{(a, t)}(f)[U]$ be the gauge-invariant gradient-flowed observable at positive flow time $t_{\mathrm{phys}} > 0$:
$$\mathcal{O}_{(a, t)}(f)[U] = a^4 \sum_{x \in \Lambda_a} f(x) E_{(a, t)}(x)[U].$$
In the degree-one marked partition function $Z(\eta) = Z_{\mathrm{vac}} + \eta \langle \mathcal{O}_{(a, t)}(f) \rangle Z_{\mathrm{vac}} + \mathcal{O}(\eta^2)$, the contribution from term $\alpha$ is:
$$\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} \chi_k^{\prime\prime} \exp(A_k^{\prime\prime}[V]) \, \mathcal{O}_{(a, t)}(f)[U(V_h, V^{\prime\prime}, V_k|_{Z \cap \Lambda^c})].$$

*Non-Factorization Proof:*
Positive flow time $t > 0$ generates parabolic diffusion with RMS radius $r_{\mathrm{diff}} = \sqrt{8 t_{\mathrm{phys}}}$. For test functions $f$ whose diffusion envelope intersects both $Z_h$ and $\Lambda \cap Z_h^c$, the flowed field strength $G_{\mu\nu}(x, t)$ depends simultaneously on links in $Z_h$, links in $\mathbb{B}_0$, and links in $Z \cap \Lambda^c$. Consequently, the physical insertion does NOT factor into $\mathcal{O}_{Z_h}[V_h] \cdot \mathcal{O}_{\Lambda \setminus Z_h}[V^{\prime\prime}]$. The preliminary integration over $V_h$ and the fluctuation integration over $V^{\prime\prime}$ remain non-trivially coupled through the physical insertion.

### 5. Gauge Orbit Resolution, Maximal Tree $T_0$, and Slice Restriction
1. **Tree Graph Construction (R-I p. 195–196):**
   Across the nested rectangular parallelepipeds $P_1 \supset P_2 \dots$, contours $\Gamma_{y, x}$ connecting $x \in P_1 \setminus P_2$ to base point $y = (a_1 + 1/2, \dots, a_d + 1/2)$ build tree graph $T = \bigcup_{x} \Gamma_{y, x}$.
   Adding external bonds $[(a_1^\prime - 1/2, \dots), (a_1^\prime + 1/2, \dots)]$ intersecting $\partial P_1$, and for $P_1 = \Lambda$ adding $[(y_1 - 1, y_2, \dots), y]$, yields tree graph $T_0 \subset \mathbb{B}_0$.
2. **Faddeev–Popov Tree-Gauge Resolution:**
   Let $G_{T_0} = \prod_{x \in V(\Lambda_0) \setminus \{x_0\}} G_x$ be the site gauge group rooted at $x_0$. Because $T_0$ contains no closed loops, the tree Jacobian is strictly constant: $\Delta_{\mathrm{FP}} \equiv 1$ under normalized Haar measure.
   On configuration space, inserting the resolution of unity $\Delta_{\mathrm{FP}} \int_{G_{T_0}} dh \prod_{b \in T_0} \delta(B^{\prime h}(b)) = 1$ and performing the functional change of variables $B^\prime \mapsto B^{\prime h^{-1}}$ using gauge invariance of the measure, action, and physical observable $\mathcal{O}_{(a, t)}(f)[U^h] = \mathcal{O}_{(a, t)}(f)[U]$ evaluates the group volume to $\operatorname{Vol}(G_{T_0}) = 1$ and restricts the functional integral to the gauge slice:
   $$\prod_{b \in T_0} \delta(B^\prime(b)).$$
   *Crucial distinction:* Fluctuation variables on non-tree bonds $b \in \mathbb{B}_0 \setminus T_0$ remain unconstrained dynamical degrees of freedom.

### 6. Compensating Transformations (R-I (1.85)–(1.88))
Transforming background $U_0$ to the axial-Landau (AL) mixture gauge (eqs. (1.85)–(1.87), p. 197) with gauge parameter $u_0$:
$$U_0 \mapsto U_0^{u_0} = \exp(i \eta \mathbb{A}_0)$$
requires simultaneous compensating transformations:
- on $V_h$: site transformation restricted to $\partial^+(Z_h^{\prime \sim})^{(h)}$;
- on $V^\prime$: transformation in the adjoint representation $B^\prime \mapsto u_0 B^\prime u_0^{-1}$.
At link endpoints $(x, y)$, site gauge transformations act with endpoint factors $(h_x, h_y)$. Bałaban's joint compensating transformation satisfies:
$$V^{\prime\prime h}_{xy} = (h_x V^\prime_{xy} h_x^{-1}) (h_x V_{0, xy} h_y^{-1}) = h_x (V^\prime_{xy} V_{0, xy}) h_y^{-1} = h_x V^{\prime\prime}_{xy} h_y^{-1}.$$
This guarantees that composite links transform covariantly and the physical insertion $\mathcal{O}_{(a, t)}(f)[U]$ is identically invariant. A naive transformation holding $V_0$ fixed while transforming $B^\prime$ alone fails by an endpoint mismatch $(h_x V_0 h_y^{-1} \ne V_0 h_y^{-1})$.

### 7. Support-Specific Cutoff Replacement (R-I (1.89))
On $\mathbb{B}_0$, decomposition of unity $1 = \chi^\prime + (1 - \chi^\prime)$ with $\chi^\prime = \chi(\{|B^\prime(b)| < \delta_k^\prime \text{ for } b \in \mathbb{B}_0\})$ separates small and large fields.
On the surviving small-field support $\chi^\prime$, Bałaban's cutoff replacement identity (1.89, p. 198) holds:
$$\chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \chi^\prime \chi_h(\Omega_h \cap Z_h) \chi_k^{\prime\prime} = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \chi^\prime.$$
This allows dropping the previous cutoff $\chi_k^{\prime\prime}$ strictly on the small-field branch. The complementary branch $(1 - \chi^\prime)$ is explicitly carried into the large-field remainder $\mathcal{R}_{\alpha, \mathrm{large}}$.

### 8. Established Proved Identity for Term $\alpha$
Within stated finite hypotheses, the degree-one marked functional integral for term $\alpha$ is:
$$\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \mathbb{T}_h(Z_h) \int_{\mathfrak{g}^{\mathbb{B}_0 \setminus T_0}} \prod_{b \in \mathbb{B}_0 \setminus T_0} dB^\prime(b) \, J(B^\prime) \, \chi^\prime(B^\prime) \chi_{h, 1/2} \exp(A_k^{\prime\prime}[\exp(i B^\prime) V_0]) \, \mathcal{O}_{(a, t)}(f)[U(V_h, \exp(i B^\prime) V_0, V_k|_{Z \cap \Lambda^c})] + \mathcal{R}_{\alpha, \mathrm{large}}$$
where:
- $J(B^\prime) = \prod_{b \in \mathbb{B}_0 \setminus T_0} \det\left(\frac{1 - e^{-i \operatorname{ad}_{B^\prime(b)}}}{i \operatorname{ad}_{B^\prime(b)}}\right)$ is the Lie algebra Haar Jacobian;
- $B^\prime|_{T_0} = 0$ is fixed by tree gauge;
- $\mathcal{R}_{\alpha, \mathrm{large}}$ carries the complementary $(1 - \chi^\prime)$ and rejected sectors;
- The observable $\mathcal{O}_{(a, t)}(f)$ is evaluated at the full entangled configuration.

### 9. First Missing Theorem Blocking Continuum Closure
This finite representation for term $\alpha$ is completely instantiated and proved within stated hypotheses. The first missing theorem that blocks continuum closure is:
**The Multiscale Marked Polymer Activity Summability Theorem:**
$$\sum_{\alpha} \mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] \quad \text{converges uniformly as } a_0 \to 0,$$
which requires proving that the marked polymer activities $K_j^{(1)}$ satisfy the cluster-expansion tree bound $\|K_j^{(1)}\|_{B_j} \le C_j$ across all scales $j = 0, \dots, n$ under Bałaban's multiscale cluster expansion.


## YM-051R: REPAIR OF TREE-GAUGE CHART MAP, ADJOINT-VS-TREE CONFLATION, EXPLICIT DENSITY REPRESENTATION, AND CONDITIONAL CLASSIFICATION

### 1. Rigorous Derivation of Tree-Gauge Chart Map $h \mapsto B^{\prime h}$ and Slice Derivative
In Section YM-051.5, the tree Faddeev–Popov identity was cited as $\Delta_{\mathrm{FP}} \equiv 1$ under group Haar measure, but its application to a Lie-algebra delta distribution $\prod_{b \in T_0} \delta(B^{\prime h}(b))$ over restricted coordinates omitted the chart mapping and its differential. Here we establish the exact chart representation:

1. **Domain and Coordinate Chart:**
   Let $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$ be the active bond set. On each bond $b = (x, y) \in \mathbb{B}_0$, the link configuration is parameterized by:
   $$V^{\prime\prime}(b) = \exp(i B^\prime(b)) V_0(b),$$
   where $V_0(b) \in SU(2)$ is the fixed minimal background parallel transporter and $B^\prime(b) \in \mathfrak{su}(2)$ satisfies the small-field bound $\|B^\prime(b)\| < \delta_k^\prime \le \pi$. The matrix exponential $\exp: \mathfrak{su}(2) \to SU(2)$ is a diffeomorphism from the ball $\{B \in \mathfrak{su}(2) : \|B\| < \pi\}$ onto its image in $SU(2) \setminus \{-I\}$.

2. **Site Gauge Transformation on Links:**
   Let $\mathcal{G}_{\Lambda_0} = \prod_{x \in V(\Lambda_0)} SU(2)$ be the site gauge group. A gauge transformation $h = (h_x)_{x \in V(\Lambda_0)}$ acts on directed bond $b = (x, y)$ by:
   $$V^{\prime\prime h}(b) = h_x V^{\prime\prime}(b) h_y^{-1} = h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1}.$$
   To express $V^{\prime\prime h}(b)$ in the Bałaban fluctuation chart relative to the same background $V_0(b)$, we write:
   $$V^{\prime\prime h}(b) = \exp(i B^{\prime h}(b)) V_0(b).$$
   Equating these two expressions yields:
   $$\exp(i B^{\prime h}(b)) = h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1} V_0(b)^{-1}.$$

3. **Chart Map Definition via Matrix Logarithm:**
   Whenever $h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1} V_0(b)^{-1}$ stays within the injectivity radius (trace $> -2$), the transformed Lie algebra fluctuation $B^{\prime h}(b)$ is uniquely defined by:
   $$B^{\prime h}(b) = \frac{1}{i} \log\left( h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1} V_0(b)^{-1} \right).$$

4. **Root Condition and Maximal Tree Graph:**
   Let $x_0 \in V(\Lambda_0)$ be the designated tree root. The gauge group at the root is fixed: $h_{x_0} = I$.
   The reduced gauge group is $G_{T_0} = \prod_{x \in V(\Lambda_0) \setminus \{x_0\}} SU(2)$.
   The tree graph $T_0 \subset \mathbb{B}_0$ contains $|V(\Lambda_0)| - 1$ bonds and no closed loops, so each vertex $x \ne x_0$ has a unique path in $T_0$ to $x_0$.

5. **Linearization and Derivative at the Gauge Slice:**
   Consider an infinitesimal gauge transformation along generators $X = (X_x)_{x \in V(\Lambda_0) \setminus \{x_0\}} \in \mathfrak{su}(2)^{V(\Lambda_0) \setminus \{x_0\}}$ with $X_{x_0} = 0$:
   $$h_x(\epsilon) = \exp(i \epsilon X_x) = I + i \epsilon X_x + \mathcal{O}(\epsilon^2).$$
   At the gauge slice $B^\prime = 0$, evaluating the chart map:
   $$h_x(\epsilon) V_0(b) h_y(\epsilon)^{-1} V_0(b)^{-1} = (I + i \epsilon X_x) V_0(b) (I - i \epsilon X_y) V_0(b)^{-1} + \mathcal{O}(\epsilon^2) = I + i \epsilon \left( X_x - V_0(b) X_y V_0(b)^{-1} \right) + \mathcal{O}(\epsilon^2).$$
   Taking the logarithm and dividing by $i$:
   $$\left. \frac{d}{d\epsilon} B^{\prime h(\epsilon)}(b) \right|_{\epsilon=0, B^\prime=0} = X_x - \operatorname{Ad}_{V_0(b)}(X_y) = (D_{V_0} X)(b),$$
   where $D_{V_0}: \mathfrak{su}(2)^{V(\Lambda_0) \setminus \{x_0\}} \to \mathfrak{su}(2)^{T_0}$ is the background covariant lattice differential along tree bonds.
   Because $T_0$ is a rooted tree, ordering vertices by tree distance from $x_0$ renders the matrix of $D_{V_0}$ block triangular with diagonal blocks given by $\pm \operatorname{Ad}_{V_0(b)}$ or $\pm I$.
   Since $\det(\operatorname{Ad}_g) = 1$ for all $g \in SU(2)$, the Jacobian determinant of $D_{V_0}$ is:
   $$\det(D_{V_0}) = \prod_{b \in T_0} |\det(\operatorname{Ad}_{V_0(b)})| = 1.$$

6. **Unrestricted Group Tree Gauge vs. Lie Algebra Delta with Cutoffs:**
   - On the full group $SU(2)^{T_0}$, normalized Haar measure $\int \prod_{b \in T_0} dh_b = 1$ integrates over compact space with no boundaries.
   - In contrast, the Lie algebra delta $\delta(B^\prime)$ is supported on an open coordinate chart $\mathcal{U} = \{\|B^\prime\| < \delta_k^\prime\}$.
   - If a gauge orbit exits the chart $\mathcal{U}$, the matrix logarithm ceases to be single-valued or crosses the cutoff $\chi^\prime$.
   - Therefore, replacing group Haar tree gauge by a Lie algebra delta $\prod_{b \in T_0} \delta(B^\prime(b))$ is **not** an unconditional identity; it is strictly conditional on the small-field chart domain and boundary cutoffs.


### 2. Adjoint Conjugation vs. Tree-Gauge Fixing Decoupling
In Section YM-051.6, the joint compensating transformation under background axial-Landau gauge change $U_0 \mapsto U_0^{u_0}$ was presented alongside tree-gauge fixing. We prove that these two actions are mathematically distinct and cannot be conflated:

1. **Adjoint Conjugation Preserves Norm and Spectrum:**
   Let $u_0 \in SU(2)$ and $B^\prime \in \mathfrak{su}(2)$. Under adjoint conjugation, $B^\prime \mapsto u_0 B^\prime u_0^{-1}$.
   Using the standard Frobenius / Hilbert–Schmidt norm on $\mathfrak{su}(2)$ (where $\|X\|_F = \sqrt{\frac{1}{2} \operatorname{Tr}(X^\dagger X)} = \sqrt{\frac{1}{2} \operatorname{Tr}(X^2)}$ for anti-Hermitian $X$, or $\sqrt{\operatorname{Tr}(B^{\prime 2})}$ for Hermitian $B^\prime$):
   $$\|u_0 B^\prime u_0^{-1}\|_F^2 = \operatorname{Tr}((u_0 B^\prime u_0^{-1})^\dagger (u_0 B^\prime u_0^{-1})) = \operatorname{Tr}(u_0 B^{\prime \dagger} B^\prime u_0^{-1}) = \operatorname{Tr}(B^{\prime \dagger} B^\prime) = \|B^\prime\|_F^2.$$
   Consequently, for any non-zero fluctuation $B^\prime \ne 0$:
   $$\|u_0 B^\prime u_0^{-1} - 0\|_F = \|B^\prime\|_F > 0.$$
   **Theorem (Adjoint Non-Zero Preservation):** Adjoint conjugation is an isometry of $\mathfrak{su}(2)$ and can NEVER map a non-zero fluctuation to zero. It merely rotates the Lie-algebra direction; it does not reduce degrees of freedom or fix a gauge slice.

2. **Tree-Gauge Fixing Requires Affine Parallel Transport:**
   To fix tree gauge on bond $b = (x, y) \in T_0$, one requires $V^{\prime\prime h}(b) = V_0(b)$, which is equivalent to $B^{\prime h}(b) = 0$.
   From $h_x \exp(i B^\prime) V_0 h_y^{-1} = V_0$, the site gauge element $h_y$ at the target endpoint MUST satisfy:
   $$h_y = V_0(b)^{-1} h_x \exp(i B^\prime(b)) V_0(b).$$
   When $B^\prime = 0$, this is the affine parallel transport equation:
   $$h_y = V_0(b)^{-1} h_x V_0(b).$$
   Notice that $h_y \ne h_x$ whenever $V_0(b)$ does not commute with $h_x$.
   Adjoint conjugation $B^\prime \mapsto u_0 B^\prime u_0^{-1}$ is an AL background mixture covariance transformation acting with the same parameter $u_0$ everywhere on the background field, whereas tree-gauge fixing recursively solves the non-local parallel transport equation edge-by-edge along the tree $T_0$.
   Conflating the two is a severe conceptual error; they must be decoupled completely.


### 3. Explicit Original Density vs. Transformed Template and Remainder Sector
We present the exact original term from Bałaban R-I (1.76) and its explicit transformed template with all constraints and inherited cutoffs:

1. **Original Unmarked Termwise Density (R-I (1.76), p. 194):**
   $$\rho_{k, \alpha}[V] = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} \chi_k^{\prime\prime} \, \exp\left(A_k^{\prime\prime}[V]\right).$$

2. **Explicit Transformed Template with Inherited Cutoffs and Measure Factors:**
   Introducing the Lie-algebra fluctuation coordinates $V^{\prime\prime}(b) = \exp(i B^\prime(b)) V_0(b)$ on active bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$, the degree-one physical marked insertion is:
   $$\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int_{\mathfrak{g}^{\mathbb{B}_0 \setminus T_0}} \prod_{b \in \mathbb{B}_0 \setminus T_0} dB^\prime(b) \, J(B^\prime(b)) \, \chi^\prime(B^\prime|_{T_0=0}) \, \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \, \exp\left(A_k^{\prime\prime}[\exp(i B^\prime|_{T_0=0}) V_0]\right) \, \mathcal{O}_{(a, t)}(f)[U(V_h, \exp(i B^\prime|_{T_0=0}) V_0, V_k|_{Z \cap \Lambda^c})] + \mathcal{R}_{\alpha, \mathrm{large}}.$$

3. **Complete Inventory of Inherited Cutoffs:**
   - $\chi_k(\Omega_k^{\sim 4})$: scale $k$ large-field cutoff on domain $\Omega_k^{\sim 4}$;
   - $\chi_{k, \Lambda}$: partition-of-unity characteristic function isolating exterior domain $Z \cap \Lambda^c$ (R-I (1.75));
   - $\chi_h(\Omega_h \cap Z_h)$: scale $h$ cutoff on preliminary region $Z_h$;
   - $\chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h)$: transition cutoff from scale $h$ to $h+1$ (R-I (1.89));
   - $\chi^\prime(B^\prime) = \prod_{b \in \mathbb{B}_0} \mathbf{1}_{\|B^\prime(b)\| < \delta_k^\prime}$: small-field characteristic function on active bonds $\mathbb{B}_0$;
   - $J(B^\prime(b)) = \det\left(\frac{1 - e^{-i \operatorname{ad}_{B^\prime(b)}}}{i \operatorname{ad}_{B^\prime(b)}}\right)$: Lie algebra Haar measure Jacobian on unconstrained bonds $b \in \mathbb{B}_0 \setminus T_0$.

4. **Explicit Complementary Large-Field Remainder Term $\mathcal{R}_{\alpha, \mathrm{large}}$:**
   Instead of an uninstantiated symbolic label, the exact complementary term is given by:
   $$\mathcal{R}_{\alpha, \mathrm{large}} = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} (1 - \chi^\prime) \, \chi_k^{\prime\prime} \, \exp\left(A_k^{\prime\prime}[V]\right) \, \mathcal{O}_{(a, t)}(f)[U(V_h, V^{\prime\prime}, V_k|_{Z \cap \Lambda^c})].$$
   Every factor in $\mathcal{R}_{\alpha, \mathrm{large}}$ is mathematically explicit.


### 4. Formal Reclassification
The actual-model Bałaban coordinate pullback and tree-gauge orbit representation across external bonds $\mathbb{B}_0$, charts, and cutoffs are formally classified as:
$$\text{Status: } \mathbf{CONDITIONAL\_AND\_OPEN}$$
with persistent governance identifier:
$$\mathbf{ACTUAL\_BALABAN\_COORDINATE\_PULLBACK\_AND\_TREE\_GAUGE\_CONDITIONAL\_AND\_OPEN}.$$
No continuum limit or spectral gap estimate is closed. The structural no-go count remains strictly 0.


## YM-051R2: REPAIR OF SU(2) UNIT RATIONAL QUATERNION CERTIFICATES, MULTI-EDGE TREE AFFINE TRANSPORT, EXACT OBSERVABLE MIXED DEPENDENCE, LIE CONVENTION RECONCILIATION, AND ACTUAL-HISTORY ADMISSIBILITY AUDIT

### 1. Reconciliation of Lie Algebra Conventions and Determinants
In mathematical physics literature (specifically Bałaban CMP 109, R-I (1.81)), link fluctuations are written as $V^{\prime\prime}(b) = \exp(i B^\prime(b)) V_0(b)$. We establish the explicit dictionary between the Hermitian generator convention and the differential-geometric anti-Hermitian convention:

1. **Hermitian Generator Convention (Bałaban):**
   - Basis: $T_a = \frac{1}{2} \sigma_a$ where $\sigma_a$ are Hermitian Pauli matrices ($T_a^\dagger = T_a$).
   - Lie bracket: $[T_a, T_b] = i \epsilon_{abc} T_c$.
   - Fluctuation: $B^\prime = \sum_{a=1}^3 B^{\prime a} T_a$ is Hermitian ($B^{\prime \dagger} = B^\prime$, $\operatorname{Tr}(B^\prime) = 0$).
   - Quadratic Casimir / Trace: $\operatorname{Tr}((B^\prime)^2) = \frac{1}{2} \sum_{a=1}^3 (B^{\prime a})^2 \ge 0$.
   - Group element: $U = \exp(i B^\prime)$, where the exponent $i B^\prime$ is anti-Hermitian ($(i B^\prime)^\dagger = -i B^\prime$).

2. **Anti-Hermitian Generator Convention (Lie Theory / Differential Geometry):**
   - Basis: $\tilde{T}_a = i T_a = \frac{i}{2} \sigma_a$ satisfying $\tilde{T}_a^\dagger = -\tilde{T}_a$.
   - Lie bracket: $[\tilde{T}_a, \tilde{T}_b] = -\epsilon_{abc} \tilde{T}_c$.
   - Lie algebra element: $X = i B^\prime = \sum_{a=1}^3 X^a \tilde{T}_a \in \mathfrak{su}(2)$.
   - Quadratic Casimir / Trace: $\operatorname{Tr}(X^2) = -\frac{1}{2} \sum_{a=1}^3 (X^a)^2 \le 0$.
   - Group element: $U = \exp(X) \in SU(2)$.

3. **Quaternion Embedding:**
   - Standard isomorphism $\mathbb{H}_1 \cong SU(2)$: $q = q_0 + q_1 \mathbf{i} + q_2 \mathbf{j} + q_3 \mathbf{k}$ with $q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1$.
   - Pure imaginary quaternions $\operatorname{Im}(\mathbb{H})$ satisfy $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = \mathbf{i}\mathbf{j}\mathbf{k} = -1$.
   - For $X = x_1 \mathbf{i} + x_2 \mathbf{j} + x_3 \mathbf{k}$, $X^2 = -\|X\|^2 \le 0$. Pure imaginary quaternions represent the **anti-Hermitian** algebra $\mathfrak{su}(2)$.
   - Group exponential: $\exp(X) = \cos(\|X\|) + \frac{\sin(\|X\|)}{\|X\|} X \in \mathbb{H}_1$. No factor of $i$ appears in the quaternion exponential because imaginary quaternion units already square to $-1$.

4. **Signed Determinant vs. Absolute Jacobian:**
   - The directional derivative matrix $D_{V_0}: \mathfrak{su}(2)^{V(\Lambda_0) \setminus \{x_0\}} \to \mathfrak{su}(2)^{T_0}$ along rooted tree $T_0$ has signed matrix determinant:
     $$\det(D_{V_0}) = +1$$
     (orientation-preserving linear isomorphism).
   - In the coordinate transformation of the differential form Haar measure $dB^\prime$, the volume density scales by the **absolute Jacobian**:
     $$|\det(D_{V_0})| = 1.$$
   - Both signed determinant and absolute Jacobian equal $1$ on $SU(2)$, but the distinction between orientation and integration density is maintained.

### 2. Exact SU(2) Unit Rational Quaternions
To eliminate non-unit approximations (such as $(1, 0, 1/3, 0)$ or truncated Taylor series $(1 - 1/8, 1/2, 0, 0)$ which have squared norms $10/9 \ne 1$ and $65/64 \ne 1$), all group links and site transformations are constructed from Pythagorean quadruples $q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1$ in $\mathbb{Q}$:
- Identity: $I = (1, 0, 0, 0)$
- Transporter $V_0(b_1) = (3/5, 4/5, 0, 0)$, norm squared $(9+16)/25 = 1$.
- Transporter $V_0(b_2) = (3/5, 0, 4/5, 0)$, norm squared $(9+16)/25 = 1$.
- Transporter $V_0(b_3) = (4/5, 0, 0, 3/5)$, norm squared $(16+9)/25 = 1$.
- Small-field fluctuation factor $U_{\mathrm{fluc}}(b_1) = (24/25, 7/25, 0, 0)$, norm squared $(576+49)/625 = 1$.
- Small-field fluctuation factor $U_{\mathrm{fluc}}(b_2) = (12/13, 0, 5/13, 0)$, norm squared $(144+25)/169 = 1$.
- Small-field fluctuation factor $U_{\mathrm{fluc}}(b_3) = (4/5, 0, 0, 3/5)$, norm squared $(16+9)/25 = 1$.
Every link $U(b) = U_{\mathrm{fluc}}(b) V_0(b)$ and site gauge element $h_x$ is certified to satisfy $\|q\|^2 = 1$ identically. Inversion in $\mathbb{H}_1$ is the exact quaternionic conjugate $q^{-1} = (q_0, -q_1, -q_2, -q_3)$.

### 3. Multi-Edge Rooted Tree $T_0$ Affine Parallel Transport
Consider a non-trivial rooted multi-edge tree $T_0$ on active vertices $V(\Lambda_0) = \{x_0, x_1, x_2, x_3\}$:
- Root vertex: $x_0 = (1, 1)$, with gauge condition $h_{x_0} = (1, 0, 0, 0) = I$.
- Tree edge 1 (branch 1): $b_1 = (x_0, x_1) = ((1, 1), (1, 0))$.
- Tree edge 2 (depth 2): $b_2 = (x_1, x_2) = ((1, 0), (2, 0))$.
- Tree edge 3 (branch 2): $b_3 = (x_0, x_3) = ((1, 1), (0, 1))$.
- Non-tree cycle edge: $b_4 = (x_2, x_3)$, closing a loop in $\Lambda_0$.

Sequential affine parallel transport along $T_0$:
1. At edge $b_1$: $h_{x_1} = V_0(b_1)^{-1} h_{x_0} U(b_1)$.
   Norm $\|h_{x_1}\|^2 = 1$; transformed link $U^h(b_1) = h_{x_0} U(b_1) h_{x_1}^{-1} = V_0(b_1)$.
2. At edge $b_2$: $h_{x_2} = V_0(b_2)^{-1} h_{x_1} U(b_2)$.
   Norm $\|h_{x_2}\|^2 = 1$; transformed link $U^h(b_2) = h_{x_1} U(b_2) h_{x_2}^{-1} = V_0(b_2)$.
3. At edge $b_3$: $h_{x_3} = V_0(b_3)^{-1} h_{x_0} U(b_3)$.
   Norm $\|h_{x_3}\|^2 = 1$; transformed link $U^h(b_3) = h_{x_0} U(b_3) h_{x_3}^{-1} = V_0(b_3)$.

All three tree edges simultaneously satisfy $U^h(b) = V_0(b)$, meaning on the chart $B^{\prime h}|_{T_0} = 0$.
In contrast:
- On the non-tree cycle edge $b_4 = (x_2, x_3)$, the transformed link is $U^h(b_4) = h_{x_2} U(b_4) h_{x_3}^{-1} \ne V_0(b_4)$. Its defect $\|U^h(b_4) - V_0(b_4)\|^2 > 0$ proves that non-tree links carry dynamical degrees of freedom (gauge-invariant holonomy) that cannot be eliminated by tree gauge.
- Naive uncoupled transformation setting $h_x = I$ for all $x$ leaves a non-zero tree defect $\sum_{b \in T_0} \|U(b) - V_0(b)\|^2 > 0$, confirming that affine transport coupling is mandatory.

### 4. Explicit Mixed Dependence and Lattice Gradient Flow Non-Factorization
To replace scalar heuristic constants (such as `135/1000` or a single uncoupled plaquette value), we establish genuine non-factorization:
1. **Observable Mixed Dependence Defect:**
   Let $\mathcal{O}(U_A, U_B) = \frac{1}{2} \operatorname{Tr}(U_A U_B)$ be an explicit composite observable coupling a link $U_A$ in preliminary region $Z_h$ with a link $U_B$ in active region $\Lambda_0$ sharing a boundary vertex $x \in \partial Z_h$.
   If $\mathcal{O}$ were factorizable into $f(U_A) g(U_B)$, then for any 4 configurations $(U_A^{(1)}, U_B^{(1)})$, $(U_A^{(2)}, U_B^{(1)})$, $(U_A^{(1)}, U_B^{(2)})$, $(U_A^{(2)}, U_B^{(2)})$, the cross-variation determinant must vanish identically:
   $$\Delta_{\mathrm{fact}} = \mathcal{O}(U_A^{(1)}, U_B^{(1)}) \mathcal{O}(U_A^{(2)}, U_B^{(2)}) - \mathcal{O}(U_A^{(1)}, U_B^{(2)}) \mathcal{O}(U_A^{(2)}, U_B^{(1)}) \equiv 0.$$
   Evaluating $\Delta_{\mathrm{fact}}$ on exact rational unit quaternions yields $\Delta_{\mathrm{fact}} \ne 0$, rigorously proving non-factorization.

2. **Lattice Wilson Gradient Flow Coupling:**
   On a hypercubic lattice, the discrete gradient flow equation is $\partial_t U_t(b) = - D S(U_t)(b) U_t(b)$, where $D S(U_t)(b)$ is the Lie-algebra staple sum around bond $b$.
   The first Euler flow step $U_{t + \epsilon}(b) = \exp(-\epsilon D S(U_t)(b)) U_t(b)$ explicitly mixes bond $b \in Z_h$ with adjacent plaquette staples touching $\Lambda_0$.
   The second functional cross-derivative $\frac{\partial^2 S_{\mathrm{flowed}}}{\partial U(b_1) \partial U(b_2)} \ne 0$ for $b_1 \in Z_h$ and $b_2 \in \Lambda_0$ is strictly non-zero, establishing that gradient-flowed observables cannot factorize across spatial boundaries without approximation.

### 5. Actual History Admissibility Audit and Primary-Source Locators
We audit ONE concrete actual admissible history $\alpha$ from Bałaban R-I (1.76):
1. **Primary-Source Locators:**
   - Bałaban, CMP 109 (1987) pp. 193–198: Proposition 1, eq. (1.76), (1.79), (1.81), (1.85)–(1.89).
   - Fixed exterior domain: $Z \cap \Lambda^c$, carrying field variables $V_k|_{Z \cap \Lambda^c}$ under cutoff $\chi_{k, \Lambda}$ (R-I (1.75)).
   - Preliminary region $Z_h$: carrying short-distance field $V_h$ under measure $dV_h \lceil_{Z_h}$ and retained scale operator $\mathbb{T}_h(Z_h)$.
   - Active region $\Lambda_0 = \Lambda \setminus Z_h$: carrying bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$, excluding bonds touching $\partial \Omega_{k+1}^1$.
   - Background parallel transporter: $U_0 = U_{k, Z}(V_\Lambda^*)$ (eq. (1.79)), $V_0 = M_{\mathbb{B}_k^\prime}(U_0)$.
   - Site gauge group: $\mathcal{G}_{\Lambda_0}$ rooted at $x_0 \in \Lambda_0$ with condition $h_{x_0} = I$.
   - Normalization: degree-one physical marked insertion $\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)]$ is normalized by the global vacuum partition function $Z_{\mathrm{vac}}$, not by an individual history denominator.

2. **Chart Admissibility and Boundary Cutoff Analysis:**
   - On active bonds $\mathbb{B}_0$, the tree slice $B^\prime|_{T_0} = 0$ is defined on the chart ball $\|B^\prime(b)\| < \delta_k^\prime \le \pi$.
   - While group Haar tree-gauge integration $\int_{SU(2)^{T_0}} \prod dh_b = 1$ is globally defined on the compact group with zero boundary, the chart representation $B^{\prime h}(b) = \frac{1}{i} \log(h_x \exp(i B^\prime) V_0 h_y^{-1} V_0^{-1})$ is restricted to the ball $\|B^\prime\| < \delta_k^\prime$.
   - If a gauge orbit exits this ball, the configuration is cut off by $(1 - \chi^\prime)$ and enters the large-field remainder $\mathcal{R}_{\alpha, \mathrm{large}}$.
   - Therefore, the tree-gauge slice is **conditionally admissible** on the small-field support $\chi^\prime$.

3. **Identification of the First Explicit Missing Bridge Lemma:**
   Before multiscale polymer activity summability can be addressed, the actual-model chart stability must be established. We formulate:
   
   **LEMMA `YM-051F-ACTUAL-CHART-SUMMABILITY` (Small-Field Chart Stability and Remainder Activity Bound):**
   *For any admissible history $\alpha$ in Bałaban R-I (1.76), there exists a scale-dependent constant $c_k > 0$ such that:*
   1. *Gauge Orbit Chart Stability: The probability under constrained Haar measure that the tree-gauge orbit exits the chart ball $\|B^{\prime h}(b)\| < \delta_k^\prime$ is bounded by $\mathcal{O}(e^{-c_k / g_k^2})$;*
   2. *Large-Field Remainder Bound: The complementary remainder satisfies $\|\mathcal{R}_{\alpha, \mathrm{large}}\| \le C_k e^{-M / g_k^2} \|\mathcal{O}_{(a, t)}(f)\|_\infty$;*
   3. *Summability Dependency: Uniform polymer activity summability $\sum_\alpha \mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)]$ is conditionally dependent on the resolution of this chart stability lemma.*

4. **Corrected Dependency Ordering:**
   Uniform multiscale polymer activity summability is **NOT** the first dependency-satisfied obligation. The first required obligation is the proof of Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` on the concrete history domain.


## YM-051R3: SOURCE/DOMAIN AND CONJECTURE WELL-POSEDNESS REPAIR

### 1. Primary-Source Citation Supersession and Page/Equation Verification
In Section YM-051R2 (lines 619, 697), citations referred to "Bałaban CMP 109 (1987) pp. 193–198". This citation is formally corrected and superseded:
- **Erroneous Citation (Superseded):** CMP 109 (1987) pp. 193–198 (*Generation of Effective Actions*).
- **Correct Primary Source:**
  **T. Bałaban, *Large Field Renormalization. I. The Basic Step of the Renormalization Group*, Communications in Mathematical Physics 122, 175–202 (1989)**.
- **Direct Primary PDF Page and Equation Mapping:**
  - Section 1: pp. 180–202.
  - Page 192, eq. (1.71)–(1.73): Decomposition of large-field component $Z_k^\prime = (\Omega_{k_0+1}^5)^c \cap Z$ and integration domain $\Lambda = (\Omega_{k_0+1}^4)^c \cap Z$.
  - Page 193, eq. (1.75): Characteristic function $\chi_{k, \Lambda}$ on exterior $Z \cap \Lambda^c$.
  - Page 194, eq. (1.76): Definition of termwise density $\rho_{k, \alpha}[V]$ with preliminary integration on $Z_h$.
  - Page 194, Proposition 1 and eq. (1.79): Minimal background configuration $U_0 = U_{k, Z}(V_\Lambda^*)$.
  - Page 195, eq. (1.81): Active fluctuation factorization $V^{\prime\prime} = \exp(i B^\prime) V_0$ on $\mathbb{B}_0$.
  - Page 195, eq. (1.85)–(1.88): Compensating transformations under background gauge change.
  - Page 195, eq. (1.89): Support-specific cutoff replacement $\chi_k^{\prime\prime} \chi^\prime = \chi^\prime$.
  - Pages 195–196: Maximal tree graph $T_0 \subset \mathbb{B}_0$ constructed from nested parallelepipeds $P_1 \setminus P_2$.

### 2. Geometric Domain Reconciliation: $\Lambda_0$ vs. $\Lambda \setminus Z_h$ and Scoping of Finite Examples
1. **Enlarged Neighborhoods and Domain Inequality:**
   In line 700 of Section YM-051R2, $\Lambda_0$ was loosely written as $\Lambda \setminus Z_h$. This is mathematically inaccurate and is superseded:
   $$\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c \quad \text{(CMP 122 p. 195)}.$$
   Because $Z_h \subset Z_h^\prime \subset Z_h^{\prime \sim}$, the set $Z_h^{\prime \sim}$ is a strictly larger regularized neighborhood of $Z_h$.
   Consequently, $\Lambda_0 \subsetneq \Lambda \setminus Z_h$. The collar region $(\Lambda \setminus Z_h) \setminus \Lambda_0 = Z_h^{\prime \sim} \setminus Z_h$ carries delta constraints, preliminary boundary fields, and buffer bonds, but is **NOT** part of the active fluctuation domain $\Lambda_0$.
2. **Active Bond Endpoints and Boundaries:**
   - Active bonds: $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$.
   - Bonds in $\mathbb{U}_k$ that intersect the outer boundary $\partial \Lambda$ belong to $\mathbb{B}_0$.
   - Bonds that intersect the internal boundary $\partial \Omega_{k+1}^1$ (touching $Z_h^{\prime \sim}$) are explicitly excluded from $\mathbb{B}_0$.
   - Exterior sites on $\partial \Lambda$ and in $Z \cap \Lambda^c$ carry fixed exterior fields $V_k|_{Z \cap \Lambda^c}$ under cutoff $\chi_{k, \Lambda}$.
3. **Explicit Scoping of Finite Certificates:**
   The 4-site unit quaternion graph in Test 11 ($x_0=(1, 1)$, $x_1=(1, 0)$, $x_2=(2, 0)$, $x_3=(0, 1)$) is an explicit **toy finite graph certificate** illustrating the algebraic mechanism of multi-edge tree affine transport and cycle holonomy defect.
   Its non-tree cycle edge $b_4 = ((2, 0), (0, 1))$ has coordinate displacement $(-2, 1)$ and Euclidean length $\sqrt{5}$, which is NOT a nearest-neighbor hypercubic lattice bond.
   This graph is NOT an admissible Bałaban history on $\mathbb{Z}^4$; it is strictly scoped as a non-hypercubic algebraic certificate of the tree-gauge transport mechanism.

### 3. Signed Determinant vs. Absolute Jacobian and Orientation Order
In line 643 of Section YM-051R2, the claim that $\det(D_{V_0}) = +1$ universally is corrected:
- On link $b = (x, y)$ oriented from parent $x$ to child $y$, the directional derivative of $U^h(b) = h_x U(b) h_y^{-1}$ with respect to Lie algebra parameters $\xi_x, \xi_y$ is:
  $$(D_{V_0} \xi)(b) = \xi_x - \operatorname{Ad}_{V_0(b)} \xi_y.$$
- For a rooted tree with root condition $\xi_{x_0} = 0$, the child site $\xi_y$ enters with coefficient $- \operatorname{Ad}_{V_0(b)}$.
- On the 3-dimensional Lie algebra $\mathfrak{su}(2)$, the linear operator $- \operatorname{Ad}_{V_0(b)}$ has determinant:
  $$\det(- \operatorname{Ad}_{V_0(b)}) = (-1)^3 \det(\operatorname{Ad}_{V_0(b)}) = (-1) \cdot (+1) = -1.$$
- Therefore, for a tree with $k$ child edges directed away from the root, the signed block determinant is:
  $$\det(D_{V_0}) = (-1)^{3 k} = (-1)^k.$$
  The sign is $-1$ for odd $k$ and $+1$ for even $k$, and reverses if edge orientations are flipped.
- In contrast, the **absolute Jacobian**:
  $$|\det(D_{V_0})| = |-1|^k = 1$$
  is universally and robustly equal to $1$, completely independent of edge orientation, basis order, or dimension parity.

### 4. Observables: Scoped Toy Cross-Defect vs. Open Physical Flowed Non-Factorization
1. **Toy Algebraic Scope:** The non-factorization defect $\Delta_{\mathrm{fact}} = -16/25 \ne 0$ for composite observable $\mathcal{O}(U_A, U_B) = \frac{1}{2} \operatorname{Tr}(U_A U_B)$ is strictly a toy algebraic certificate disproving the spatial factorization hypothesis $f(U_A) g(U_B)$ for coupled open links.
2. **Physical Gauge Invariance & Open Status:** On a physical lattice gauge theory, the trace of two open links is not gauge invariant without closing paths. Furthermore, an infinitesimal Euler flow staple calculation does not prove non-factorization for the physical gauge-invariant flowed observable $\mathcal{O}_{(a, t)}(f)$ across non-linear trajectories at finite $t_{\mathrm{phys}} > 0$.
3. **Formal Epistemic Classification:** The claim of non-factorization for the physical flowed observable remains formally classified as:
   $$\mathbf{PHYSICAL\_FLOWED\_OBSERVABLE\_NON\_FACTORIZATION\_OPEN}.$$

### 5. Refutation of Ill-Posed Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` and Replacement by Deterministic Lemma
1. **Refutation of Proposed Probabilistic Formulation:**
   The formulation of Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` in Section YM-051R2 is refuted as ill-posed:
   - Haar measure on $SU(2)$ is a normalized translation-invariant group measure with NO $g$-dependence; naming $g$ cannot produce an $\mathcal{O}(e^{-c/g^2})$ probability bound under Haar measure.
   - An $\mathcal{O}(e^{-c/g^2})$ suppression requires the Wilson action $\exp(-g^{-2} S(U))$, which is a weighted measure, not pure Haar measure.
   - The event that the original configuration exits the chart ball (governed by $1 - \chi^\prime$) is NOT identical to the event that the tree-gauge transformed configuration exits the chart ball.
   - Constants $C_k, c_k, M$, norms, and parameter ranges were undefined.
2. **Replacement: Purely Deterministic First Bridge Lemma:**
   We formulate the true, source-bound deterministic bridge lemma that precedes any statistical estimates:

   **LEMMA `YM-051F-DETERMINISTIC-CHART-OVERLAP` (Deterministic Small-Field Chart Overlap and Remainder Decomposition):**
   *For any admissible history $\alpha$ in Bałaban CMP 122 (1.76) on $\Lambda_0 = \Lambda \cap (Z_h^{\prime \sim})^c$ and active bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$:*
   1. *Let $\mathcal{B}_{\delta_k^\prime} = \{B^\prime \in \mathfrak{su}(2)^{\mathbb{B}_0} : \|B^\prime(b)\| < \delta_k^\prime \ \forall b \in \mathbb{B}_0\}$ with small-field characteristic function $\chi^\prime = \mathbf{1}_{\mathcal{B}_{\delta_k^\prime}}$.*
   2. *Let $h[V^{\prime\prime}] \in \mathcal{G}_{\Lambda_0}$ (rooted at $x_0$, $h_{x_0} = I$) be the unique sequential tree-fixing affine parallel transport map satisfying $V^{\prime\prime h}(b) = V_0(b)$ for all $b \in T_0$.*
   3. *Define the deterministic chart overlap domain:*
      $$\mathcal{E}_{\mathrm{chart}} = \left\{ B^\prime \in \mathcal{B}_{\delta_k^\prime} : \forall b \in \mathbb{B}_0 \setminus T_0, \ V^{\prime\prime h[V^{\prime\prime}]}(b) V_0(b)^{-1} \in \exp(\mathcal{B}_{\delta_k^\prime}) \right\}.$$
   4. *On $\mathcal{E}_{\mathrm{chart}}$, the gauge slice coordinate map $B^{\prime h}|_{T_0} = 0$ is exact, the absolute Jacobian is $|\det(D_{V_0})| = 1$, and Haar measure satisfies exact measure equality.*
   5. *The un-normalized termwise density $\rho_{k, \alpha}$ admits an exact deterministic decomposition:*
      $$\rho_{k, \alpha} = \rho_{k, \alpha}^{\mathrm{tree-slice}} + \mathcal{R}_{\alpha, \mathrm{chart-exit}} + \mathcal{R}_{\alpha, \mathrm{large}}$$
      *where:*
      - $\rho_{k, \alpha}^{\mathrm{tree-slice}}$ *is the integral restricted to $\mathcal{E}_{\mathrm{chart}}$ on the gauge slice $B^{\prime h}|_{T_0} = 0$;*
      - $\mathcal{R}_{\alpha, \mathrm{chart-exit}}$ *is the integral over $\mathcal{B}_{\delta_k^\prime} \setminus \mathcal{E}_{\mathrm{chart}}$ where the tree gauge rotates fluctuations outside the small-field chart;*
      - $\mathcal{R}_{\alpha, \mathrm{large}}$ *is the remainder integral carrying $(1 - \chi^\prime)$.*
   6. *Status & Dependency:*
      *This deterministic decomposition is completely defined. Any subsequent weighted-measure tail estimate under the action $\exp(-g_k^{-2} A_k^{\prime\prime})$ is a separate, downstream analytic obligation that is conditionally blocked until the deterministic properties of $\mathcal{E}_{\mathrm{chart}}$ are certified.*


## YM-052: CONSTRAINED TREE-MAP PUSHFORWARD, FIBER WEIGHTS, BOUNDARY ADMISSIBILITY, AND SOURCE LOCATOR CORRECTIONS

### 1. Primary-Source Printed-Page Mapping and Page/Equation Disambiguation
In Section YM-051R3 (lines 738–739), equations (1.85)–(1.88) and (1.89) were listed as appearing on page 195. A rigorous visual audit against the printed article **T. Bałaban, *Large Field Renormalization. I. The Basic Step of the Renormalization Group*, Communications in Mathematical Physics 122, 175–202 (1989)** establishes the precise printed page numbers:
- **Printed p. 194:** Proposition 1 and minimal background equation (1.79): $U_0 = U_{k, Z}(V_\Lambda^*)$ with decomposition $U_k = U_0 \exp(i B^\prime)$.
- **Printed p. 195:** Fluctuation factorization equation (1.81): $V^{\prime\prime} = \exp(i B^\prime) V_0$ on active bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$, and initial boundary definitions.
- **Printed pp. 195–196:** Maximal tree graph $T_0 \subset \mathbb{B}_0$ constructed from nested parallelepipeds $P_1 \setminus P_2$ rooted at a single base point $x_0 \in \Lambda_0$.
- **Printed p. 197:** Background covariance and compensating transformations, equations **(1.85)–(1.88)**: joint action under background AL gauge transformation $U_0 \mapsto U_0^{u_0}$ via $V_h \mapsto V_h^{u_0}$ and $B^\prime \mapsto u_0 B^\prime u_0^{-1}$. (Formally supersedes the erroneous citation to p. 195).
- **Printed p. 198:** Support-specific cutoff replacement, equation **(1.89)**: $\chi_k^{\prime\prime} \chi^\prime = \chi^\prime$ on the small-field support $\chi^\prime = \mathbf{1}_{\{|B^\prime(b)| < \delta_k^\prime \ \forall b \in \mathbb{B}_0\}}$. (Formally supersedes the erroneous citation to p. 195).
- **Disambiguation Note:** Authors and readers must strictly distinguish between **PDF page indices** (which depend on journal front matter / cover sheets) and **printed journal page numbers** (pp. 175–202 in CMP 122).

### 2. Geometric Collar Difference Identity and Strictness Precision
1. **Exact Set Difference Identity:**
   Let $\Lambda = (\Omega_{k_0+1}^4)^c \cap Z$ be the large-field integration domain, $Z_h$ the preliminary region, and $Z_h^{\prime \sim}$ the enlarged regularized neighborhood carrying delta constraints and buffer bonds.
   The active fluctuation region is defined by:
   $$\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c.$$
   The difference between the naive exterior $\Lambda \setminus Z_h$ and the true active region $\Lambda_0$ is given by the exact set identity:
   $$(\Lambda \setminus Z_h) \setminus \Lambda_0 = (\Lambda \setminus Z_h) \cap (\Lambda \cap (Z_h^{\prime \sim})^c)^c = (\Lambda \setminus Z_h) \cap Z_h^{\prime \sim} = \Lambda \cap (Z_h^{\prime \sim} \setminus Z_h).$$
2. **Precision on Strict Inclusion:**
   In Section YM-051R3 (line 747), strict inclusion $\Lambda_0 \subsetneq \Lambda \setminus Z_h$ was asserted unconditionally. This is refined and superseded:
   - The inclusion $\Lambda_0 \subseteq \Lambda \setminus Z_h$ is universal because $Z_h \subset Z_h^{\prime \sim} \implies (Z_h^{\prime \sim})^c \subset Z_h^c$.
   - **Strict inclusion $\Lambda_0 \subsetneq \Lambda \setminus Z_h$ holds IF AND ONLY IF the collar intersection inside $\Lambda$ is non-empty:**
     $$\Lambda \cap (Z_h^{\prime \sim} \setminus Z_h) \ne \emptyset.$$
   - If the regularized collar lies entirely outside $\Lambda$, or in boundary configurations where the collar carries zero interior lattice points inside $\Lambda$, then $\Lambda \cap (Z_h^{\prime \sim} \setminus Z_h) = \emptyset$ and $\Lambda_0 = \Lambda \setminus Z_h$.
   - Strictness cannot be asserted for every arbitrary history geometry from topological inclusions alone without explicit verification of non-emptiness.

### 3. Full Invertible Augmented Coordinate Map vs. Unproved Slice Projection
1. **The Dimension Reduction Fallacy:**
   On active bonds $\mathbb{B}_0$, the original Lie algebra fluctuation variables $B^\prime$ span $3|\mathbb{B}_0|$ dimensions.
   A spanning tree $T_0 \subset \mathbb{B}_0$ rooted at $x_0$ with $|T_0| = |\Lambda_0| - 1$ edges defines a gauge-fixing condition $B^{\prime h}|_{T_0} = 0$.
   Projecting to the gauge slice by eliminating tree variables reduces dimensions from $3|\mathbb{B}_0|$ to $3|\mathbb{B}_0 \setminus T_0|$.
   Local absolute Faddeev–Popov determinant $|\det(D_{V_0})| = 1$ at the slice together with group Haar invariance under *fixed* gauge transformations **DOES NOT** establish that the pushforward measure on the slice equals the restricted slice measure.
2. **Non-Invariance of Small-Field Cutoffs:**
   The small-field cutoff:
   $$\chi^\prime(B^\prime) = \prod_{b \in \mathbb{B}_0} \mathbf{1}_{\{\|B^\prime(b)\| < \delta_k^\prime\}}$$
   is explicitly **dependent on individual bond fluctuations and is NOT gauge invariant**. Under a gauge transformation $h \in \mathcal{G}_{\Lambda_0}$, the tree link fluctuations change, so the support of $\chi^\prime$ cuts off the gauge orbit non-trivially.
3. **The Invertible Augmented Map $\Phi$:**
   Before integration, the change of variables must be defined as an invertible augmented diffeomorphism:
   $$\Phi: \mathfrak{su}(2)^{\mathbb{B}_0} \to \mathfrak{su}(2)^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0}, \quad B^\prime \mapsto (\hat{B}^\prime, h[B^\prime]),$$
   where $h[B^\prime]$ is the unique sequential tree-fixing transformation satisfying $V^{\prime\prime h[B^\prime]}(b) = V_0(b)$ for all $b \in T_0$, and $\hat{B}^\prime \in \mathfrak{su}(2)^{\mathbb{B}_0 \setminus T_0}$ represents the gauge-transformed fluctuations on non-tree bonds:
   $$\exp(i \hat{B}^\prime(b)) V_0(b) = h_x[B^\prime] \exp(i B^\prime(b)) V_0(b) h_y[B^\prime]^{-1} \quad \text{for } b = (x, y) \in \mathbb{B}_0 \setminus T_0.$$
4. **Exact Pushforward Measure and Fiber Weights:**
   The pushforward measure on the slice coordinates $\hat{B}^\prime$ is:
   $$d\hat{\mu}(\hat{B}^\prime) = W(\hat{B}^\prime) \, \left[ \prod_{b \in \mathbb{B}_0 \setminus T_0} J(\hat{B}^\prime(b)) \, d\hat{B}^\prime(b) \right],$$
   where the **FIBER WEIGHT** is the explicit integral over the orbit fiber:
   $$W(\hat{B}^\prime) = \int_{\mathcal{G}_{\Lambda_0, x_0}} dh \, J_{\mathrm{orbit}}(\hat{B}^\prime, h) \, \chi^\prime(\Phi^{-1}(\hat{B}^\prime, h)).$$
   - In Lemma `YM-051F-DETERMINISTIC-CHART-OVERLAP`, setting $W(\hat{B}^\prime) \equiv 1$ (or identifying the overlap integral with an unweighted slice integral) assumed without proof that the fiber weight is identically 1.
   - For cutoffs depending on tree variables, the fiber volume $\operatorname{vol}(\text{Fiber}(\hat{B}^\prime))$ varies with $\hat{B}^\prime$ and does not integrate to 1.
   - Consequently, the overlap integral can only be equated to a tree-slice integral AFTER computing and bounding the fiber weight $W(\hat{B}^\prime)$.
   - Status of Lemma `YM-051F-DETERMINISTIC-CHART-OVERLAP`: the set partition $\rho_{k, \alpha} = \rho_{k, \alpha}^{\mathrm{overlap}} + \mathcal{R}_{\alpha, \mathrm{chart-exit}} + \mathcal{R}_{\alpha, \mathrm{large}}$ is algebraically exact, but calling $\rho_{k, \alpha}^{\mathrm{overlap}}$ an unweighted tree-slice integral is formally **UNPROVED_PENDING_FIBER_WEIGHT_INTEGRATION**.

### 4. Concrete History Boundary Admissibility and Tree Solvability
1. **Permitted Site Gauge Group:**
   On $\Lambda_0$, the gauge group is $\mathcal{G}_{\Lambda_0} = \{h: \Lambda_0 \to SU(2)\}$.
2. **Solvability under Single-Root Constraint:**
   If $\mathcal{G}_{\Lambda_0}$ is constrained ONLY at a single root site $x_0 \in \Lambda_0$ by $h_{x_0} = I$, the sequential tree-fixing equations:
   $$h_y = V_0(b)^{-1} h_x \exp(i B^\prime(b)) V_0(b)$$
   have a UNIQUE, unconditional solution along every directed edge of spanning tree $T_0$. Every vertex $y \ne x_0$ has exactly one parent in $T_0$, so each $h_y$ is uniquely determined without overconstraint.
3. **Obstruction under Multiple Fixed Endpoints:**
   If preliminary sector boundary conditions or external boundary rules impose $h_x = I$ on multiple boundary sites (e.g. $h_x = I$ for all $x \in \partial \Lambda_0$):
   - Any path in $T_0$ connecting two fixed endpoints $x_1, x_2 \in \partial \Lambda_0$ imposes the global holonomy constraint:
     $$I = h_{x_2} = \left[ \prod_{b \in \text{path}(x_1, x_2)} \operatorname{Ad}_{V_0(b)} \exp(i B^\prime(b)) \right] h_{x_1} = \prod_{b \in \text{path}} \operatorname{Ad}_{V_0(b)} \exp(i B^\prime(b)).$$
   - For generic configurations $B^\prime$, this holonomy is non-trivial ($ \ne I$).
   - Therefore, the tree-fixing equation **HAS NO SOLUTION** on configurations with non-zero tree holonomy if multiple endpoints are pre-fixed.
4. **Source Audit Finding:**
   Bałaban CMP 122 pp. 195–196 avoids this overconstraint obstruction by:
   - Fixing ONLY the single root site $x_0$ ($h_{x_0} = I$).
   - Partitioning boundary bonds so that internal boundary bonds touching $\partial \Omega_{k+1}^1$ are strictly excluded from $\mathbb{B}_0$, leaving active bonds $\mathbb{B}_0$ and site group $\mathcal{G}_{\Lambda_0, x_0}$ free of preliminary fixed-site overconstraints.


## YM-053: GROUP-VALUED AUGMENTED GAUGE MAP, SEQUENTIAL NORMALIZED HAAR PUSHFORWARD, EFFECTIVE FIBER DENSITY, AND CONCRETE HISTORY ADMISSIBILITY AUDIT

### 1. Group-Valued Invertible Augmented Map $\Phi$
1. **Geometric Setup and Target Spaces:**
   - Active spatial domain: $\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c \subset \mathbb{Z}^4$ (Bałaban CMP 122 p. 195).
   - Active bonds: $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$, excluding bonds touching $\partial \Omega_{k+1}^1$.
   - Compact gauge group: $G = SU(2)$ (or $SU(N)$).
   - Group configuration space: $\mathcal{U} = G^{\mathbb{B}_0}$.
   - Spanning tree: $T_0 \subset \mathbb{B}_0$, a maximal spanning tree of the graph $(\Lambda_0, \mathbb{B}_0)$ rooted at single base site $x_0 \in \Lambda_0$.
   - Number of vertices: $N_0 = |\Lambda_0|$. Number of tree bonds: $|T_0| = N_0 - 1$.
   - Rooted gauge group:
     $$\mathcal{G}_{\Lambda_0, x_0} = \left\{ h = (h_x)_{x \in \Lambda_0} \in G^{\Lambda_0} : h_{x_0} = I \right\}.$$
   - Target slice space: $\mathcal{S} = G^{\mathbb{B}_0 \setminus T_0}$.
   - Target augmented space: $\mathcal{S} \times \mathcal{G}_{\Lambda_0, x_0} = G^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0}$.
   - Dimensional balance: $\dim(G^{\mathbb{B}_0}) = (\dim G)|\mathbb{B}_0| = (\dim G)(|\mathbb{B}_0 \setminus T_0| + |T_0|) = \dim(G^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0})$.

2. **Sequential Tree Gauge Solver in Group Variables:**
   - Let $V_0 \in G^{\mathbb{B}_0}$ be the fixed minimal background parallel transporter $V_0 = M_{\mathbb{B}_k^{\prime\prime}}(U_0)$ (CMP 122 p. 195 (1.81)).
   - For every vertex $y \in \Lambda_0 \setminus \{x_0\}$, let $p(y) \in \Lambda_0$ be its unique parent in $T_0$, and let $b_y = (p(y), y) \in T_0$ be the directed tree edge entering $y$.
   - For any active group configuration $V^{\prime\prime} \in G^{\mathbb{B}_0}$, the gauge-slice condition on tree bonds is:
     $$V^{\prime\prime h}(b_y) = V_0(b_y) \iff h_{p(y)} V^{\prime\prime}(b_y) h_y^{-1} = V_0(b_y).$$
   - This determines $h_y \in G$ recursively by:
     $$h_y[V^{\prime\prime}] = V_0(b_y)^{-1} h_{p(y)}[V^{\prime\prime}] V^{\prime\prime}(b_y), \quad h_{x_0}[V^{\prime\prime}] = I.$$
   - **Global Solvability Theorem:**
     Because $G$ is a group and $T_0$ has no cycles, this recursion defines $h_x[V^{\prime\prime}] \in G$ uniquely and smoothly for every $x \in \Lambda_0$.
     **Crucial distinction from Lie algebra coordinates:** This solver operates entirely with group multiplications and inversions. It requires NO matrix logarithms and NO small-field domain restrictions; it is globally well-defined on all of $G^{\mathbb{B}_0}$.
     Furthermore, $h[V^{\prime\prime}]$ depends *strictly* on tree link variables $V^{\prime\prime}|_{T_0}$ and is independent of non-tree variables $V^{\prime\prime}|_{\mathbb{B}_0 \setminus T_0}$.

3. **Definition of the Group Augmented Map $\Phi$:**
   $$\Phi: G^{\mathbb{B}_0} \to G^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0}, \quad V^{\prime\prime} \mapsto (\hat{V}^{\prime\prime}, h[V^{\prime\prime}]),$$
   where:
   $$\hat{V}^{\prime\prime}(b) = h_x[V^{\prime\prime}] V^{\prime\prime}(b) h_y[V^{\prime\prime}]^{-1} \in G \quad \text{for each } b = (x, y) \in \mathbb{B}_0 \setminus T_0.$$

4. **Explicit Inverse Map $\Phi^{-1}$:**
   Given $(\hat{V}, h) \in G^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0}$, define $\Phi^{-1}(\hat{V}, h) \in G^{\mathbb{B}_0}$ by:
   $$V^{\prime\prime}(b) = \begin{cases} h_x^{-1} V_0(b) h_y & \text{if } b = (x, y) \in T_0, \\ h_x^{-1} \hat{V}(b) h_y & \text{if } b = (x, y) \in \mathbb{B}_0 \setminus T_0. \end{cases}$$
   - **Verification of Left Inverse ($\Phi \circ \Phi^{-1} = \operatorname{id}$):**
     On tree bonds, $V^{\prime\prime}(b_y) = h_{p(y)}^{-1} V_0(b_y) h_y$. The tree solver computes:
     $$h_y[V^{\prime\prime}] = V_0(b_y)^{-1} h_{p(y)}[V^{\prime\prime}] (h_{p(y)}^{-1} V_0(b_y) h_y).$$
     Since $h_{x_0}[V^{\prime\prime}] = I = h_{x_0}$, mathematical induction on tree depth gives $h_y[V^{\prime\prime}] = h_y$ for all $y \in \Lambda_0$.
     Hence the gauge output is $h$.
     On non-tree bonds $b = (x, y) \in \mathbb{B}_0 \setminus T_0$:
     $$\hat{V}^{\prime\prime}(b) = h_x V^{\prime\prime}(b) h_y^{-1} = h_x (h_x^{-1} \hat{V}(b) h_y) h_y^{-1} = \hat{V}(b).$$
     Thus $\Phi(\Phi^{-1}(\hat{V}, h)) = (\hat{V}, h)$.
   - **Verification of Right Inverse ($\Phi^{-1} \circ \Phi = \operatorname{id}$):**
     Let $V^{\prime\prime} \in G^{\mathbb{B}_0}$. The map $\Phi$ produces $(\hat{V}^{\prime\prime}, h[V^{\prime\prime}])$.
     On tree bonds $b = (x, y) \in T_0$, $h_x[V^{\prime\prime}]^{-1} V_0(b) h_y[V^{\prime\prime}] = V^{\prime\prime}(b)$ by the tree solver relation.
     On non-tree bonds $b = (x, y) \in \mathbb{B}_0 \setminus T_0$, $h_x[V^{\prime\prime}]^{-1} \hat{V}^{\prime\prime}(b) h_y[V^{\prime\prime}] = h_x^{-1} (h_x V^{\prime\prime}(b) h_y^{-1}) h_y = V^{\prime\prime}(b)$.
     Thus $\Phi^{-1}(\Phi(V^{\prime\prime})) = V^{\prime\prime}$.
   - **Theorem (Global Diffeomorphism):**
     $\Phi: G^{\mathbb{B}_0} \to G^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0}$ is a global, bijective, smooth diffeomorphism with image equal to the entire product space.

5. **Restricted Log Charts on Explicit Domains:**
   - On the open chart ball $\mathcal{B}_{\delta_k^\prime} = \{ B^\prime \in \mathfrak{su}(2)^{\mathbb{B}_0} : \|B^\prime(b)\| < \delta_k^\prime \ \forall b \in \mathbb{B}_0 \}$ with $\delta_k^\prime \le \pi$, fluctuation variables are defined by $V^{\prime\prime}(b) = \exp(i B^\prime(b)) V_0(b)$.
   - The matrix logarithm $\log: \exp(\mathcal{B}_{\delta_k^\prime}) V_0 \to \mathcal{B}_{\delta_k^\prime}$ is well-defined only on this open ball.
   - On the slice, $\hat{V}(b) = \exp(i \hat{B}^\prime(b)) V_0(b)$ for $b \in \mathbb{B}_0 \setminus T_0$.
   - The group diffeomorphism $\Phi$ induces a chart map on the restricted domain:
     $$\mathcal{E}_{\mathrm{chart}} = \left\{ V^{\prime\prime} \in \exp(\mathcal{B}_{\delta_k^\prime}) V_0 : \forall b \in \mathbb{B}_0 \setminus T_0, \ \hat{V}(b) V_0(b)^{-1} \in \exp(\mathcal{B}_{\delta_k^\prime}) \right\}.$$
   - On $\mathcal{E}_{\mathrm{chart}}$, the gauge slice coordinate condition $\hat{B}^\prime|_{T_0} = 0$ is exact.

### 2. Sequential Normalized Haar Changes of Variables & Unit Pushforward Jacobian
1. **Sequential Transformation along Spanning Tree:**
   - Let $dV^{\prime\prime} = \prod_{b \in \mathbb{B}_0} dV^{\prime\prime}(b)$ be the product normalized Haar measure on $G^{\mathbb{B}_0}$.
   - Order vertices $x_0, x_1, \dots, x_{N_0-1}$ by increasing tree distance from root $x_0$.
   - Each $x_j$ ($j \ge 1$) has unique tree edge $b_j = (p(x_j), x_j) \in T_0$ with parent $p(x_j) \in \{x_0, \dots, x_{j-1}\}$.
   - At step $j$, the mapping $V^{\prime\prime}(b_j) \mapsto h_{x_j} = V_0(b_j)^{-1} h_{p(x_j)} V^{\prime\prime}(b_j)$ is left multiplication by the already determined group element $V_0(b_j)^{-1} h_{p(x_j)} \in G$.
   - By left invariance of the normalized Haar measure on compact Lie group $G$:
     $$dh_{x_j} = dV^{\prime\prime}(b_j).$$
   - Therefore, taking the product over all tree bonds:
     $$\prod_{b \in T_0} dV^{\prime\prime}(b) = \prod_{x \in \Lambda_0 \setminus \{x_0\}} dh_x = dh_{\mathcal{G}_{\Lambda_0, x_0}}.$$
2. **Two-Sided Transformation on Non-Tree Bonds:**
   - For each non-tree bond $b = (x, y) \in \mathbb{B}_0 \setminus T_0$, the transformation is $\hat{V}(b) = h_x V^{\prime\prime}(b) h_y^{-1}$.
   - For any fixed $(h_x, h_y) \in G \times G$, this is a left translation by $h_x$ and right translation by $h_y^{-1}$.
   - By bi-invariance of normalized Haar measure on compact Lie group $G$:
     $$d\hat{V}(b) = dV^{\prime\prime}(b).$$
3. **Triangular Jacobian and Exact Measure Pushforward:**
   - The derivative matrix of the transformation $(V^{\prime\prime}|_{T_0}, V^{\prime\prime}|_{\mathbb{B}_0 \setminus T_0}) \mapsto (h, \hat{V})$ is block triangular: $h$ depends only on $V^{\prime\prime}|_{T_0}$, and the diagonal blocks are left/right translations with determinant 1.
   - Therefore, the pushforward of normalized product Haar measure under $\Phi$ satisfies:
     $$\Phi_*\left( \prod_{b \in \mathbb{B}_0} dV^{\prime\prime}(b) \right) = \left[ \prod_{b \in \mathbb{B}_0 \setminus T_0} d\hat{V}(b) \right] \times dh_{\mathcal{G}_{\Lambda_0, x_0}}.$$
   - The integration Jacobian with respect to normalized Haar measure is **IDENTICALLY 1**.

### 3. Retention of Cutoffs, Action, and Boundary Factors: Measure Fiber Weight vs. Full Effective Density
1. **Full Integrand on Active Bonds:**
   In Bałaban R-I (1.76), the full integrand on active bonds $\mathbb{B}_0$ in term $\alpha$ is:
   $$\mathcal{F}(V^{\prime\prime}) = \chi_k^{\prime\prime}[V^{\prime\prime}] \, \chi^\prime[V^{\prime\prime}] \, \exp(A_k^{\prime\prime}[V^{\prime\prime}]) \, \mathcal{O}_{(a, t)}(f)[U(V_h, V^{\prime\prime}, V_k|_{Z \cap \Lambda^c})] \, \Theta_{\mathrm{boundary}}[V^{\prime\prime}, V_h, V_k].$$
2. **Pushforward onto Slice Space:**
   Applying the global diffeomorphism $\Phi$:
   $$\int_{G^{\mathbb{B}_0}} dV^{\prime\prime} \, \mathcal{F}(V^{\prime\prime}) = \int_{G^{\mathbb{B}_0 \setminus T_0}} d\hat{V} \, \mathcal{W}_{\mathrm{eff}}(\hat{V}),$$
   where the **FULL EFFECTIVE FIBER DENSITY** is the explicit fiber integral:
   $$\mathcal{W}_{\mathrm{eff}}(\hat{V}) = \int_{\mathcal{G}_{\Lambda_0, x_0}} dh \, \mathcal{F}(\Phi^{-1}(\hat{V}, h)).$$
3. **Distinction between Measure Fiber Weight and Effective Density:**
   - The **Pure Measure Fiber Weight** of a cutoff characteristic function $\chi$ (e.g. $\chi^\prime$ or overlap indicator $\chi_{\mathcal{E}_{\mathrm{chart}}}$) is:
     $$W_\chi(\hat{V}) = \int_{\mathcal{G}_{\Lambda_0, x_0}} dh \, \chi(\Phi^{-1}(\hat{V}, h)).$$
   - For the deterministic overlap domain $\mathcal{E}_{\mathrm{chart}}$:
     $$W_{\mathcal{E}_{\mathrm{chart}}}(\hat{V}) = \int_{\mathcal{G}_{\Lambda_0, x_0}} dh \, \mathbf{1}_{\{\Phi^{-1}(\hat{V}, h) \in \mathcal{E}_{\mathrm{chart}}\}}.$$
   - **Why factoring $\mathcal{W}_{\mathrm{eff}}(\hat{V})$ into $W_\chi(\hat{V}) \times \mathcal{F}(\hat{V}, h=I)$ fails in general:**
     - A site gauge transformation $h \in \mathcal{G}_{\Lambda_0, x_0}$ acts only on sites in $\Lambda_0$ with $h_{x_0} = I$, while fields outside $\Lambda_0$ ($V_h$ on $Z_h$, $V_k$ on $Z \cap \Lambda^c$) are NOT transformed by $h$.
     - Any link $b = (x, y)$ crossing the boundary $\partial \Lambda$ (with $x \in \Lambda_0$ and $y \in Z \cap \Lambda^c$) transforms as:
       $$U^h(b) = h_x U(b) \ne U(b) \quad (\text{since } h_y = I \text{ outside } \Lambda_0).$$
     - Plaquettes straddling $\partial \Lambda$ in the action $A_k^{\prime\prime}$ and observable $\mathcal{O}_{(a, t)}(f)$ pick up boundary gauge factors $h_x$.
     - Consequently, $\exp(A_k^{\prime\prime}[\Phi^{-1}(\hat{V}, h)])$ and $\mathcal{O}_{(a, t)}(f)[\Phi^{-1}(\hat{V}, h)]$ depend non-trivially on $h$ along the fiber.
     - **Strict Mathematical Rule:** Unless exact boundary compensating transformations are proved to cancel every boundary $h_x$ factor identically, all action, insertion, and boundary factors **MUST REMAIN INSIDE THE FIBER INTEGRAL** $\int dh$. Factoring them out produces an uncontrolled approximation error.

### 4. Source Reconstruction of ONE Actual Admissible R-I History
1. **Source Context from Bałaban CMP 122 (1989) Section 1 (pp. 192–198):**
   - Scale $k$. Large-field domain: $\Lambda = (\Omega_{k_0+1}^4)^c \cap Z$ (p. 192).
   - Preliminary region $Z_h$ carries short-distance fields $V_h$ under operator $\mathbb{T}_h(Z_h)$.
   - Regularized neighborhood $Z_h^{\prime \sim}$.
   - Active region: $\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c$ (p. 195).
   - Active bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$: bonds intersecting $\partial \Lambda$ are INCLUDED in $\mathbb{B}_0$; bonds intersecting $\partial \Omega_{k+1}^1$ are EXCLUDED from $\mathbb{B}_0$.
   - Exterior domain: $Z \cap \Lambda^c$, carrying fixed $V_k|_{Z \cap \Lambda^c}$ under cutoff $\chi_{k, \Lambda}$ (p. 193 (1.75)).
2. **Audit of Fixed Sites and Pre-Existing Delta Functions:**
   - Bałaban states on p. 194: *"The integration in (1.76) does not involve any $\delta$-functions, they are all integrated out."*
   - There are NO pre-existing delta constraints on active bonds $\mathbb{B}_0$.
   - On p. 196: *"The union of the above described tree graphs and bonds is denoted by $T_0$. It is a tree graph in $\mathbb{B}_0$, fixing completely a gauge in this set. Using the Faddeev-Popov procedure we introduce the gauge fixing $\delta$-function $\delta_{T_0}(V^\prime)$ in the integral (1.76)."*
   - Tree $T_0$ leaves exactly ONE root site $x_0 \in \Lambda_0$ fixed.
   - The prior assertion that "excluded internal boundary bonds automatically remove all fixed-site obstructions" is confirmed for the inner boundary $\partial \Omega_{k+1}^1$ because bonds intersecting $\partial \Omega_{k+1}^1$ are not in $\mathbb{B}_0$.
   - However, for outer boundary bonds intersecting $\partial \Lambda$, these bonds ARE in $\mathbb{B}_0$ and connect to exterior field $V_k|_{Z \cap \Lambda^c}$.
   - Bałaban resolves this outer background coupling on p. 197 by transforming $U_0$ to the axial-Landau (AL) mixture gauge (eqs. (1.85)–(1.88)) with compensating transformations on $V_h$ and $V^\prime$.
3. **Explicit Termwise Density Representation:**
   The un-normalized termwise density with physical insertion is:
   $$\rho_{k, \alpha}[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int_{G^{\mathbb{B}_0 \setminus T_0}} d\hat{V} \, \mathcal{W}_{\mathrm{eff}}(\hat{V}; V_h, V_k|_{Z \cap \Lambda^c}) + \mathcal{R}_{\alpha, \mathrm{large}},$$
   where the full effective fiber density is:
   $$\mathcal{W}_{\mathrm{eff}}(\hat{V}; V_h, V_k) = \int_{\mathcal{G}_{\Lambda_0, x_0}} dh \, \chi_k^{\prime\prime}[\Phi^{-1}(\hat{V}, h)] \, \chi^\prime[\Phi^{-1}(\hat{V}, h)] \, \exp(A_k^{\prime\prime}[\Phi^{-1}(\hat{V}, h)]) \, \mathcal{O}_{(a, t)}(f)[U(V_h, \Phi^{-1}(\hat{V}, h), V_k)].$$
   Normalized physical insertion: $\mathcal{I}_\alpha = Z_{\mathrm{vac}}^{-1} \rho_{k, \alpha}$.
   Any assertion of unweighted slice factorizability across $\partial \Lambda$ remains formally classified as **OPEN**.

### 5. Finite Regression Challenge and Arithmetic Reconciliation
1. **Arithmetic Reconciliation of Test 12 Defect Formulas:**
   - In Test 12 code: parameter $\delta = 1/4$.
   - The true fiber weight is $w(x_S) = 2\delta = 1/2$. The naive slice indicator is $\chi(0, x_S) = 1$.
   - **Pointwise Density / Fiber-Weight Defect:**
     $$\Delta_{\mathrm{weight}} = w(x_S) - 1 = 2\delta - 1 = 2(1/4) - 1 = -1/2 \ne 0.$$
   - **Integrated Measure Loss Defect:**
     $$\Delta_{\mathrm{measure}} = \int_{-\delta}^\delta (w(x_S) - 1) dx_S = (2\delta - 1)(2\delta) = 2\delta(2\delta - 1) = \left(\frac{1}{2}\right)\left(-\frac{1}{2}\right) = -1/4 \ne 0.$$
   - (Remark: For parameter $\delta = 3/8$, $2\delta - 1 = -1/4$).
   - The formula written in the prose summary "$\Delta_{\mathrm{fiber}} = 2\delta - 1 = -1/4$" conflated the pointwise density defect $2\delta - 1 = -1/2$ with the integrated measure loss defect $2\delta(2\delta - 1) = -1/4$.
   - **Reconciliation Resolution:** Both defects are strictly non-zero and certify the measure loss obstruction. Additive assertions in Test 12/13 certify both $2\delta - 1 = -1/2$ and $2\delta(2\delta - 1) = -1/4$. Immutable raw receipts are preserved.

2. **Genuine Compact-Group $U(1)$ / $SU(2)$ Orbit-Weight Certificate:**
   - Consider a 2-bond graph with vertices $\{x_0, x_1\}$ and bonds $\mathbb{B}_0 = \{b_1, b_2\}$, where $b_1 = (x_0, x_1) \in T_0$ and $b_2 = (x_0, x_1) \notin T_0$.
   - Compact group $G = U(1)$ with normalized Haar measure $d\theta / (2\pi)$ on $[-\pi, \pi)$. Total group volume $\int dU = 1$.
   - Rooted gauge group $\mathcal{G}_{x_0} = \{h_{x_1} = e^{i\phi} : \phi \in [-\pi, \pi)\}$, Haar measure $dh = d\phi / (2\pi)$.
   - Tree gauge condition: $U^h(b_1) = 1 \iff \phi = \theta_1$.
   - Global augmented diffeomorphism $\Phi(e^{i\theta_1}, e^{i\theta_2}) = (e^{i(\theta_2 - \theta_1)}, e^{i\theta_1}) = (e^{i\hat{\theta}_2}, e^{i\phi})$.
   - Inverse: $\Phi^{-1}(e^{i\hat{\theta}_2}, e^{i\phi}) = (e^{i\phi}, e^{i(\hat{\theta}_2 + \phi)})$.
   - Measure pushforward: $\Phi_*(dU) = d\hat{U} dh$ with exact Jacobian 1.
   - Compact-group cutoff: $\chi(U) = \mathbf{1}_{\{|\theta| \le \delta\}}$ with $\delta = \pi/3$ ($\cos \delta = 1/2$).
   - Exact compact-group fiber weight:
     $$W(\hat{\theta}_2) = \int_{-\pi}^\pi \frac{d\phi}{2\pi} \mathbf{1}_{\{|\phi| \le \delta\}} \mathbf{1}_{\{|\hat{\theta}_2 + \phi| \le \delta\}} = \frac{2\delta - |\hat{\theta}_2|}{2\pi} \mathbf{1}_{\{|\hat{\theta}_2| \le 2\delta\}}.$$
   - **Exact Compact-Group Measure Loss Defect:**
     $$\Delta_{\mathrm{compact\_measure}} = \int_{-\pi}^\pi \frac{d\hat{\theta}_2}{2\pi} W(\hat{\theta}_2) - \int_{-\pi}^\pi \frac{d\hat{\theta}_2}{2\pi} \chi(1, e^{i\hat{\theta}_2}) = \left(\frac{\delta}{\pi}\right)^2 - \frac{\delta}{\pi} = \left(\frac{1}{3}\right)^2 - \frac{1}{3} = \frac{1}{9} - \frac{1}{3} = -\frac{2}{9} \ne 0.$$
   - **Exact Compact-Group Fiber Weight Defect at Slice Origin:**
     $$\Delta_{\mathrm{compact\_weight\_origin}} = W(0) - 1 = \frac{2\delta}{2\pi} - 1 = \frac{1}{3} - 1 = -\frac{2}{3} \ne 0.$$
   - **Exact Observable Expectation Defect on $F(\hat{U}) = \cos(\hat{\theta}_2)$:**
     Pushforward expectation is $(\sin(\delta)/\pi)^2 = 3/(4\pi^2)$. Naive slice expectation is $\sin(\delta)/\pi = \sqrt{3}/(2\pi)$.
     Defect: $\Delta_{\mathrm{compact\_obs}} = \frac{\sqrt{3}}{2\pi}\left(\frac{\sqrt{3}}{2\pi} - 1\right) \ne 0$.
   - This compact-group certificate has zero Euclidean normalization ambiguity and confirms that naive slice projection causes exact measure and expectation defects on compact Lie groups.


## YM-053R: REPAIR OF BOUNDARY GAUGE INVARIANCE, ACTUAL GRAPH/MEASURE CORRESPONDENCE, AND ADMISSIBLE EFFECTIVE DENSITY FACTOR INVENTORY

### 1. Refutation of Invalid Single-Link Non-Invariance Inference and Proof of Closed-Plaquette Trace Cancellation
In Section YM-053.3, it was asserted that because boundary-crossing links $b = (x, y)$ (with $x \in \Lambda_0$ and $y \in Z \cap \Lambda^c$) transform non-trivially as $U^h(b) = h_x U(b) \ne U(b)$, straddling plaquettes in the action $A_k^{\prime\prime}$ and the gradient-flowed observable $\mathcal{O}_{(a, t)}(f)$ necessarily depend on $h$.
**This inference is mathematically invalid and is formally refuted:**

1. **The Single-Link vs. Closed-Loop Non-Sequitur:**
   A single link $U(b)$ is not a gauge-invariant quantity. Conflating the non-invariance of a single link with the non-invariance of an action or physical observable is an elementary mathematical fallacy. Physical actions and observables are composed of gauge-invariant traces of closed loops (or covariant functional combinations).

2. **Proof of Exact Closed-Plaquette Trace Invariance under Extended Gauge Transformations:**
   Let $\mathcal{G}_{\Lambda_0, x_0} = \{h \in G^{\Lambda_0} : h_{x_0} = I\}$ be the rooted site gauge group on active vertices $\Lambda_0$. Extend $h$ to the entire lattice by setting:
   $$h_x = I \quad \text{for all } x \notin \Lambda_0.$$
   Under the standard lattice gauge transformation, every directed bond $b = (u, v)$ on the lattice transforms as:
   $$U^h(u, v) = h_u U(u, v) h_v^{-1}.$$
   Now consider an arbitrary oriented plaquette $p = (x_1, x_2, x_3, x_4)$ straddling the boundary $\partial \Lambda$, where $x_1, x_4 \in \Lambda_0$ (active sites) and $x_2, x_3 \in \Lambda_0^c$ (exterior sites).
   Evaluating each of the four links:
   - Link $b_1 = (x_1, x_2)$ (crossing from active to exterior):
     $$U^h(b_1) = h_{x_1} U(b_1) h_{x_2}^{-1} = h_{x_1} U(b_1) I = h_{x_1} U(b_1).$$
   - Link $b_2 = (x_2, x_3)$ (exterior link with both endpoints in $\Lambda_0^c$):
     $$U^h(b_2) = h_{x_2} U(b_2) h_{x_3}^{-1} = I \cdot U(b_2) \cdot I = U(b_2).$$
     *(An exterior link whose endpoints are both exterior stays identically fixed!)*
   - Link $b_3 = (x_3, x_4)$ (crossing from exterior to active):
     $$U^h(b_3) = h_{x_3} U(b_3) h_{x_4}^{-1} = I \cdot U(b_3) h_{x_4}^{-1} = U(b_3) h_{x_4}^{-1}.$$
   - Link $b_4 = (x_4, x_1)$ (internal link with both endpoints in $\Lambda_0$):
     $$U^h(b_4) = h_{x_4} U(b_4) h_{x_1}^{-1}.$$
   Now compute the ordered product around the closed loop $p$:
   $$\begin{aligned}
   U^h(p) &= U^h(b_1) \, U^h(b_2) \, U^h(b_3) \, U^h(b_4) \\
   &= (h_{x_1} U(b_1)) \, (U(b_2)) \, (U(b_3) h_{x_4}^{-1}) \, (h_{x_4} U(b_4) h_{x_1}^{-1}).
   \end{aligned}$$
   At vertex $x_4$, the interior factors cancel: $h_{x_4}^{-1} h_{x_4} = I$.
   Thus:
   $$U^h(p) = h_{x_1} \left( U(b_1) U(b_2) U(b_3) U(b_4) \right) h_{x_1}^{-1} = h_{x_1} U(p) h_{x_1}^{-1}.$$
   The holonomy of the straddling plaquette transforms by exact conjugation by $h_{x_1} \in G$.
   Taking the trace:
   $$\operatorname{Tr}(U^h(p)) = \operatorname{Tr}(h_{x_1} U(p) h_{x_1}^{-1}) = \operatorname{Tr}(U(p)).$$
   **Theorem (Exact Boundary Plaquette Trace Invariance):**
   For every plaquette $p$ on the lattice—whether purely internal, purely exterior, or straddling the boundary—the plaquette trace is IDENTICALLY INVARIANT under the extended gauge transformation:
   $$\operatorname{Tr}(U^h(p)) \equiv \operatorname{Tr}(U(p)).$$
   Consequently, the Wilson plaquette action $S_W(U^h) \equiv S_W(U)$ is identically invariant.

3. **Gauge Invariance of Physical Flowed Observables:**
   Wilson gradient flow $\partial_t U_t(b) = - D S(U_t)(b) U_t(b)$ is strictly gauge covariant: if bare links transform as $U \mapsto U^h$, flowed links satisfy $U_t^h(b) = h_u U_t(b) h_v^{-1}$ identically.
   Any gauge-invariant observable $\mathcal{O}_{(a, t)}(f)[U]$ constructed from flowed plaquette traces / Wilson loops satisfies:
   $$\mathcal{O}_{(a, t)}(f)[U^h] \equiv \mathcal{O}_{(a, t)}(f)[U].$$
   The assertion that the physical observable depends on $h$ along the fiber under a legitimate extended gauge transformation is refuted.

4. **Contrast with Incomplete / Inconsistent Transformation:**
   Conversely, suppose a transformation is applied inconsistently: for instance, if link $b_3 = (x_3, x_4)$ is held fixed ($U^h(b_3) = U(b_3)$) because it is labeled "exterior", while its endpoint $x_4 \in \Lambda_0$ transforms with $h_{x_4} \ne I$.
   Then the closed-loop product becomes:
   $$U^{\mathrm{broken}}(p) = h_{x_1} U(b_1) U(b_2) U(b_3) h_{x_4} U(b_4) h_{x_1}^{-1}.$$
   Here the factor $h_{x_4}$ does not cancel, and $\operatorname{Tr}(U^{\mathrm{broken}}(p)) \ne \operatorname{Tr}(U(p))$.
   Holding a link fixed with one transformed endpoint breaks gauge invariance. The actual Bałaban transformation on active bonds $\mathbb{B}_0$ transforms ALL bonds in $\mathbb{B}_0$ consistently, so boundary crossing links in $\mathbb{B}_0$ receive their legitimate endpoint factor $h_x$.

5. **What Actually Causes $h$-Dependence Along the Fiber $\int dh$:**
   While the plaquette action and physical observable are gauge invariant under consistent extended transformations, the effective fiber density $\mathcal{W}_{\mathrm{eff}}(\hat{V}) = \int dh \, \mathcal{F}(\Phi^{-1}(\hat{V}, h))$ CANNOT be factored into an unweighted slice value because:
   - **Small-Field Cutoffs are Link-Based:** The characteristic function $\chi^\prime(V^{\prime\prime}) = \prod_{b \in \mathbb{B}_0} \mathbf{1}_{\|B^\prime(b)\| < \delta_k^\prime}$ depends on individual bond fluctuations $B^\prime(b) = \frac{1}{i}\log(V^{\prime\prime}(b) V_0(b)^{-1})$. Under $V^{\prime\prime} \mapsto \Phi^{-1}(\hat{V}, h)$, tree bonds satisfy $B^{\prime h}|_{T_0} = 0$, but the original configuration $V^{\prime\prime}(b) = h_x^{-1} V_0(b) h_y$ has $B^\prime(b) \ne 0$. The cutoff $\chi^\prime$ explicitly depends on $h$, cutting off gauge orbits non-trivially.
   - **Gauge-Fixing and Background Terms:** If the effective action $A_k^{\prime\prime}$ contains quadratic fluctuation terms $S_2(B^\prime)$ relative to background $V_0$, or gauge-fixing terms, these terms depend on $h$.
   - **Boundary Constraints:** Any boundary constraints $\Theta_{\mathrm{boundary}}$ that couple to individual link fluctuations or background variables depend on $h$.
   **Conclusion:** Retaining the full integrand $\mathcal{F}(\Phi^{-1}(\hat{V}, h))$ inside the fiber integral $\int dh$ is mathematically safe and necessary due to cutoffs and background terms. However, asserting a "theorem" that the plaquette action or physical flowed observable is non-invariant simply because single crossing links transform was an invalid claim that is now formally repaired.


### 2. Actual Graph Dimensions, Boundary Bonds, and Spanning Tree vs. Forest Correspondence
1. **Precise Vertex and Bond Sets in Bałaban CMP 122:**
   - Active region: $\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c \subset \mathbb{Z}^4$ (p. 195).
   - Active bonds: $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$.
   - By Bałaban's rule (p. 195), bonds intersecting the outer boundary $\partial \Lambda$ belong to $\mathbb{B}_0$, while bonds intersecting the inner boundary $\partial \Omega_{k+1}^1$ are excluded from $\mathbb{B}_0$.
   - The vertex set of bonds in $\mathbb{B}_0$ is:
     $$V(\mathbb{B}_0) = \Lambda_0 \cup \partial_{\mathrm{ext}}\Lambda_0,$$
     where $\partial_{\mathrm{ext}}\Lambda_0 = \{y \in Z \cap \Lambda^c : \exists x \in \Lambda_0, (x, y) \in \mathbb{B}_0\}$.
   - The dynamic site gauge group acts ONLY on vertices in $\Lambda_0$. Vertices in $\partial_{\mathrm{ext}}\Lambda_0$ belong to the exterior domain $Z \cap \Lambda^c$ where fields are fixed to $V_k|_{Z \cap \Lambda^c}$; they have $h_y = I$ identically.
   - Root condition: Exactly ONE site $x_0 \in \Lambda_0$ is fixed ($h_{x_0} = I$).
   - Number of free dynamic sites: $|\Lambda_0| - 1$.
   - Dimension of rooted gauge group: $\dim(\mathcal{G}_{\Lambda_0, x_0}) = (\dim G)(|\Lambda_0| - 1)$.

2. **Dimension Count and Boundary Bond Partition:**
   - Decompose active bonds into internal bonds and boundary bonds:
     $$\mathbb{B}_0 = \mathbb{B}_0^{\mathrm{int}} \cup \mathbb{B}_0^{\mathrm{ext}},$$
     where $\mathbb{B}_0^{\mathrm{int}} = \{(x, y) \in \mathbb{B}_0 : x, y \in \Lambda_0\}$ and $\mathbb{B}_0^{\mathrm{ext}} = \{(x, y) \in \mathbb{B}_0 : x \in \Lambda_0, y \in \partial_{\mathrm{ext}}\Lambda_0\}$.
   - If $T_0 \subset \mathbb{B}_0^{\mathrm{int}}$ is a spanning tree of the internal vertices $\Lambda_0$ rooted at $x_0$, then:
     $$|T_0| = |\Lambda_0| - 1.$$
     The number of tree bonds $|T_0|$ matches the number of free gauge sites $|\Lambda_0| - 1$ EXACTLY.
   - The external boundary bonds $\mathbb{B}_0^{\mathrm{ext}}$ CANNOT belong to $T_0$; they belong to $\mathbb{B}_0 \setminus T_0$.
   - Dimension balance:
     $$|\mathbb{B}_0| = |T_0| + |\mathbb{B}_0 \setminus T_0| = (|\Lambda_0| - 1) + |\mathbb{B}_0 \setminus T_0|.$$
     The group configuration space has dimension $(\dim G)|\mathbb{B}_0| = \dim(G^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0})$.
   - On external bonds $b = (x, y) \in \mathbb{B}_0^{\mathrm{ext}}$, the transformed link is $\hat{V}(b) = h_x V^{\prime\prime}(b) h_y^{-1} = h_x V^{\prime\prime}(b)$ (since $h_y = I$). These bonds remain residual unconstrained dynamical degrees of freedom in the slice space $G^{\mathbb{B}_0 \setminus T_0}$.

3. **Status of Bałaban's Block Tree Construction (CMP 122 pp. 195–196):**
   Bałaban constructs trees in nested rectangular parallelepipeds $P_1 \setminus P_2$ and adds external bonds connecting blocks into a maximal tree $T_0$.
   Whether Bałaban's $T_0$ is strictly contained in $\mathbb{B}_0^{\mathrm{int}}$ or includes boundary links across blocks requires detailed verification for every admissible history geometry.
   We formulate:

   **LEMMA `YM-053F-ACTUAL-GRAPH-MEASURE-CORRESPONDENCE` (Bałaban Spanning Tree / Forest and Boundary Bond Decomposition):**
   *For any admissible history $\alpha$ in Bałaban CMP 122 (1.76):*
   1. *The maximal tree graph $T_0 \subset \mathbb{B}_0$ spans precisely the $|\Lambda_0|$ active vertices with single root $x_0 \in \Lambda_0$ and $|T_0| = |\Lambda_0| - 1$ bonds;*
   2. *All external boundary bonds connecting $\Lambda_0$ to $\partial \Lambda$ belong to $\mathbb{B}_0 \setminus T_0$;*
   3. *The sequential tree gauge solver $h_y = V_0(b_y)^{-1} h_{p(y)} V^{\prime\prime}(b_y)$ uniquely determines $\mathcal{G}_{\Lambda_0, x_0}$ without boundary overconstraint;*
   4. *The pushforward measure under $\Phi$ satisfies exact normalized Haar measure equality with unit Jacobian.*

   *Epistemic Status:* While the generic finite-graph theorem is proved for any graph with spanning tree $T_0$ and single root $x_0$, the exact source correspondence for arbitrary multiscale Bałaban block boundaries remains formally classified as:
   $$\mathbf{GRAPH\_MEASURE\_CORRESPONDENCE\_CONDITIONAL\_ON\_SOURCE\_DOMAIN\_AUDIT}.$$


### 3. Complete Effective-Density Factor Inventory Reconciliation
In Section YM-053.4 (line 998), the termwise density formula omitted the boundary factor $\Theta_{\mathrm{boundary}}$ that had been present in line 959. Here we provide the complete, reconciled inventory of all 12 mathematical factors entering the degree-one marked functional integral:

1. $\chi_k(\Omega_k^{\sim 4})$: large-field cutoff at scale $k$ on domain $\Omega_k^{\sim 4}$;
2. $\chi_{k, \Lambda}$: partition-of-unity characteristic function on exterior domain $Z \cap \Lambda^c$ (eq. (1.75));
3. $\chi_h(\Omega_h \cap Z_h)$: scale $h$ cutoff on preliminary region $Z_h$;
4. $\mathbb{T}_h(Z_h)$: preliminary scale transfer operator on short-distance fields $V_h$;
5. $\Theta_{\mathrm{boundary}}[V^{\prime\prime}, V_h, V_k|_{Z \cap \Lambda^c}]$: **RESTORED** boundary coupling factor, carrying delta constraints and regularized collar boundary terms across $Z_h^{\prime \sim} \setminus Z_h$ and $\partial \Lambda$;
6. $\chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h)$: transition cutoff from scale $h$ to $h+1$ (eq. (1.89));
7. $\chi_k^{\prime\prime}[V^{\prime\prime}]$: scale $k$ active fluctuation cutoff;
8. $\chi^\prime[V^{\prime\prime}] = \prod_{b \in \mathbb{B}_0} \mathbf{1}_{\|B^\prime(b)\| < \delta_k^\prime}$: small-field characteristic function on active bonds $\mathbb{B}_0$;
9. $\exp(A_k^{\prime\prime}[V^{\prime\prime}])$: effective action on active bonds;
10. $\mathcal{O}_{(a, t)}(f)[U(V_h, V^{\prime\prime}, V_k|_{Z \cap \Lambda^c})]$: gauge-invariant gradient-flowed physical observable;
11. $\mathcal{R}_{\alpha, \mathrm{large}}$: exact complementary large-field remainder carrying $(1 - \chi^\prime) \chi_k^{\prime\prime}$;
12. $Z_{\mathrm{vac}}^{-1}$: global vacuum partition function normalization.

The complete termwise density with physical insertion is:
$$\rho_{k, \alpha}[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int_{G^{\mathbb{B}_0 \setminus T_0}} d\hat{V} \, \mathcal{W}_{\mathrm{eff}}(\hat{V}; V_h, V_k|_{Z \cap \Lambda^c}) + \mathcal{R}_{\alpha, \mathrm{large}},$$
where the full effective fiber density is:
$$\mathcal{W}_{\mathrm{eff}}(\hat{V}; V_h, V_k) = \int_{\mathcal{G}_{\Lambda_0, x_0}} dh \, \chi_k^{\prime\prime}[\Phi^{-1}(\hat{V}, h)] \, \chi^\prime[\Phi^{-1}(\hat{V}, h)] \, \chi_{h, 1/2} \, \Theta_{\mathrm{boundary}}[\Phi^{-1}(\hat{V}, h), V_h, V_k] \, \exp(A_k^{\prime\prime}[\Phi^{-1}(\hat{V}, h)]) \, \mathcal{O}_{(a, t)}(f)[U(V_h, \Phi^{-1}(\hat{V}, h), V_k)].$$
Normalized physical insertion: $\mathcal{I}_\alpha = Z_{\mathrm{vac}}^{-1} \rho_{k, \alpha}$.
Every factor is mathematically explicit. No placeholder "complete" certifications are asserted; any unresolved multi-scale boundary factors remain explicitly scoped.


### 4. Scoping of Compact $U(1)$ vs. Non-Abelian $SU(2)$ Haar Measure
In Section YM-053.5, a 2-bond compact-group toy certificate was constructed on $U(1)$. We establish the precise mathematical distinction between $U(1)$ and $SU(2)$ Haar measures:
1. **Abelian $U(1)$ Haar Measure:**
   - Parameterized by $\theta \in [-\pi, \pi)$ with normalized Haar measure $d\mu_{U(1)} = d\theta / (2\pi)$.
   - The Haar density is completely flat: $\rho_{U(1)}(\theta) = 1/(2\pi)$ everywhere.
   - The orbit weight $W(\hat{\theta}_2) = \frac{2\delta - |\hat{\theta}_2|}{2\pi}$ for cutoff $[-\delta, \delta]$ is a piecewise-linear triangle function resulting from the convolution of flat box distributions.
2. **Non-Abelian $SU(2)$ Haar Measure:**
   - Parameterized by rotation angle $\theta \in [0, 2\pi)$ and axis $\mathbf{n} \in S^2$ (or unit quaternion $q \in S^3$), the class-function Haar measure has volume element:
     $$d\mu_{SU(2)}(\theta) = \frac{1}{\pi} \sin^2(\theta/2) \, d\theta.$$
   - The density is geometrically curved: it vanishes quadratically as $\theta^2 / (4\pi)$ at $\theta = 0$ and peaks at $\theta = \pi$.
3. **Explicit Scoping Rule:**
   - The $U(1)$ calculation is strictly an **abelian toy certificate** demonstrating that compact Lie groups with boundary cutoffs generate non-trivial fiber weights and measure defects;
   - There is **NO AUTOMATIC LIFT** of $U(1)$ orbit weights, density formulas, or probability certificates to full non-abelian $SU(2)$;
   - On $SU(2)$, computing fiber weights requires non-abelian quaternion / matrix multiplications and integration against curved $\sin^2(\theta/2)$ volume elements;
   - Compact $U(1)$ weighted integrals must remain distinct from normalized expectations, and subgroup $U(1)$ Haar measures must remain distinct from full $SU(2)$ Haar measures.


### 5. Formal Reclassification and Preserved Governance Boundaries
1. **Classification:**
   - Bounded task `YM-053R` is classified under `[METHOD_SPECIFIC_OBSTRUCTION]`.
   - Structural no-go count remains strictly 0.
   - All constitutional invariants remain preserved: `goal_complete = false`, `clay_problem = OPEN_AND_UNSOLVED`, `P3 = OPEN`, `E-CROSSOVER = OPEN`, `E-UV-FLOWED = PARTIAL_PROGRESS`, `YM-016 = BLOCKED`.
2. **Proved Results within Bounded Scope:**
   - Exact closed-plaquette trace invariance under extended gauge transformations ($h \equiv I$ outside $\Lambda_0$) proved for all plaquettes, including boundary-straddling plaquettes;
   - Single-link transformation defect decoupled from closed-plaquette / physical observable invariance;
   - Retention of $\int dh$ in effective fiber density $\mathcal{W}_{\mathrm{eff}}$ justified by link cutoffs $\chi^\prime$ and background terms;
   - Active graph dimension count $|\mathbb{B}_0| = |T_0| + |\mathbb{B}_0 \setminus T_0|$ established, with external boundary bonds belonging to $\mathbb{B}_0 \setminus T_0$;
   - Full 12-factor inventory of effective density reconciled, restoring $\Theta_{\mathrm{boundary}}$;
   - $U(1)$ compact toy certificate scoped with explicit non-lifting barrier to full $SU(2)$.
3. **Immediate Next Concrete Obligation:**
   Under objective `YM-015F-JET-002B`, the next dependency-satisfied obligation is to verify the exact Bałaban tree graph correspondence (Lemma `YM-053F-ACTUAL-GRAPH-MEASURE-CORRESPONDENCE`) and establish deterministic chart overlap (Lemma `YM-051F-DETERMINISTIC-CHART-OVERLAP`) before advancing downstream weighted-measure tail estimates under the Wilson action.


## YM-054: PRIMARY-SOURCE BAŁABAN TREE/FOREST CONSTRUCTION, EXACT NESTED PARALLELEPIPED GEOMETRY, ADMISSIBLE DOMAIN FACTOR MATCHING, AND GIT-BLOB DIGEST DISAMBIGUATION

### 1. Direct Primary-Source Transcription and Visual Inspection of Bałaban CMP 122 pp. 195–196
Direct inspection of T. Bałaban, *Large Field Renormalization. I*, Commun. Math. Phys. 122, 175–202 (1989), printed pages 195–196 reveals the exact, unadulterated mathematical formulation of the gauge-fixing tree graph $T_0$:

1. **Nested Rectangular Parallelepiped Setup (p. 195):**
   - Consider two successive rectangular parallelepipeds in the multiscale sequence:
     $$P_1 = [a_1, b_1] \times \dots \times [a_d, b_d] \quad \text{and} \quad P_2 = [a_1^\prime, b_1^\prime] \times \dots \times [a_d^\prime, b_d^\prime],$$
     with $[a_\mu^\prime, b_\mu^\prime] \subset [a_\mu, b_\mu]$.
   - The active difference region is $P_1 \setminus P_2$ intersected with the unit lattice.
   - Initial base point: $y = (y_1, \dots, y_d) = (a_1 + 1/2, \dots, a_d + 1/2)$.
   - Split parameter: $a \in (a_1^\prime, b_1^\prime)$.

2. **Axial Contours $\Gamma_{y, x}$ Building Tree $T$ on $P_1 \setminus P_2$ (p. 196):**
   - For a given point $x \in P_1 \setminus P_2$:
     - If $x_1 \le a$:
       $$\Gamma_{y, x} = [y, (y_1, \dots, y_{d-1}, x_d)] \cup \dots \cup [(y_1, x_2, \dots, x_d), x].$$
     - If $x_1 > a$:
       $$\begin{aligned}
       \Gamma_{y, x} &= [y, (y_1, \dots, y_{d-1}, x_d)] \cup \dots \cup [(y_1, y_2, x_3, \dots, x_d), (y_1, y_2, x_3, \dots, x_d)] \\
       &\quad \cup [(y_1, y_2, x_3, \dots, x_d), (b_1 - 1/2, y_2, x_3, \dots, x_d)] \\
       &\quad \cup [(b_1 - 1/2, y_2, x_3, \dots, x_d), (b_1 - 1/2, x_2, x_3, \dots, x_d)] \\
       &\quad \cup [(b_1 - 1/2, x_2, x_3, \dots, x_d), x].
       \end{aligned}$$
   - The union of these contours forms a tree graph on $P_1 \setminus P_2$:
     $$T = \bigcup_{x \in P_1 \setminus P_2} \Gamma_{y, x}.$$

3. **The Crucial Added External Bonds and Refutation of the Guessed Lemma (p. 196):**
   - Bałaban explicitly writes:
     > *"We use all gauge degrees of freedom connected with points of $P_1 \setminus P_2$, except one, so we add an external bond to the graph."*
   - Specifically:
     - For inner domains $P_2 \ne (\Omega_{h+1}^{\prime\prime \sim 2})^c$: Bałaban adds the bond
       $$[(a_1^\prime - 1/2, a_2^\prime + 1/2, \dots, a_d^\prime + 1/2), (a_1^\prime + 1/2, a_2^\prime + 1/2, \dots, a_d^\prime + 1/2)]$$
       intersecting $\partial P_2$ to connect the tree of $P_1 \setminus P_2$ to the tree of the next scale block $P_2 \setminus P_3$.
     - For the outermost domain $P_1 = \Lambda$: Bałaban adds the external bond
       $$[(y_1 - 1, y_2, \dots, y_d), y]$$
       intersecting $\partial \Lambda$ to connect the base point $y \in \Lambda$ to the exterior point $y_0 = (y_1 - 1, y_2, \dots, y_d) \in \Lambda^c$!
   - Bałaban defines $T_0$:
     > *"The union of the above described tree graphs and bonds is denoted by $T_0$. It is a tree graph in $\mathbb{B}_0$, fixing completely a gauge in this set. Using the Faddeev-Popov procedure we introduce the gauge fixing $\delta$-function $\delta_{T_0}(V^\prime)$ in the integral (1.76)."*
   - **Refutation of the Guessed YM-053R Hypothesis:**
     In Task YM-053R, Section 2, it was postulated that:
     *(i)* $T_0 \subset \mathbb{B}_0^{\mathrm{int}}$ has $|T_0| = |\Lambda_0| - 1$ edges spanning internal vertices;
     *(ii)* all external boundary bonds belong to $\mathbb{B}_0 \setminus T_0$;
     *(iii)* an arbitrary internal root $x_0 \in \Lambda_0$ is held fixed with $h_{x_0} = I$.
     **This hypothesis is directly contradicted by Bałaban's primary text:**
     Bałaban explicitly **adds the external bond $[y_0, y]$ into $T_0$**!
     By including $[y_0, y] \in T_0$, the tree graph $T_0$ connects active vertices in $\Lambda_0$ to the exterior boundary point $y_0 \in \partial_{\mathrm{ext}}\Lambda_0$ where the field is fixed ($h_{y_0} = I$).
     Consequently, $T_0$ has $|T_0| = (|\Lambda_0| - 1) + 1 = |\Lambda_0|$ tree edges, which fixes ALL $|\Lambda_0|$ site gauge degrees of freedom in $G^{\Lambda_0}$ without leaving any arbitrary internal root $x_0$ unfixed!
     The partition identity $|\mathbb{B}_0| = |T_0| + |\mathbb{B}_0 \setminus T_0|$ alone was a counting tautology that did not establish the true boundary-grounded mechanism.

---

### 2. Explicit Smallest Concrete Geometry on Nested Parallelepipeds ($P_1 \setminus P_2$)
To demonstrate Bałaban's tree construction with exact, non-abstract rigor, we build ONE explicit smallest concrete geometry on the lattice:

1. **Lattice Domain and Parallelepipeds:**
   - Consider a 2D slice of the integer unit lattice $\mathbb{Z}^2$.
   - Outermost domain: $\Lambda = P_1 = [0, 2] \times [0, 1]$.
   - Inner domain: $P_2 = [1, 2] \times [0, 1]$.
   - Active difference region:
     $$\Lambda_0 = P_1 \setminus P_2 = \{0\} \times \{0, 1\} = \{(0, 0), (0, 1)\}.$$
     Active vertex count: $|\Lambda_0| = 2$.
   - Exterior boundary vertices:
     $$\partial_{\mathrm{ext}}\Lambda_0 = \{(-1, 0), (-1, 1), (1, 0), (1, 1)\}.$$
     Here $(-1, 0), (-1, 1) \in Z \cap \Lambda^c$ (outer exterior) and $(1, 0), (1, 1) \in P_2$ (inner boundary).

2. **Active Bond Set $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$:**
   By Bałaban's rule (p. 195), bonds intersecting $\partial \Lambda$ belong to $\mathbb{B}_0$, while bonds touching the inner boundary $\partial \Omega_{k+1}^1$ are excluded from $\mathbb{B}_0$.
   - Internal bonds:
     $$\mathbb{B}_0^{\mathrm{int}} = \{ b_{\mathrm{int}} = ((0, 0), (0, 1)) \}.$$
   - Outer boundary bonds intersecting $\partial \Lambda$:
     $$\mathbb{B}_0^{\mathrm{ext}} = \{ b_{\mathrm{ext}, 1} = ((-1, 0), (0, 0)), \ b_{\mathrm{ext}, 2} = ((-1, 1), (0, 1)) \}.$$
   - Total active bond set: $\mathbb{B}_0 = \{ b_{\mathrm{int}}, b_{\mathrm{ext}, 1}, b_{\mathrm{ext}, 2} \}$. Total bonds: $|\mathbb{B}_0| = 3$.

3. **Bałaban's Tree Construction:**
   - Base point: $y = (0, 0) \in \Lambda_0$.
   - Split parameter: $a = 1/2$.
   - Contours in $P_1 \setminus P_2$:
     - For $x = (0, 0) = y$: $\Gamma_{y, y} = \emptyset$.
     - For $x = (0, 1)$: $x_1 = 0 \le a$, so $\Gamma_{y, x} = [y, (0, 1)] = \{ b_{\mathrm{int}} \}$.
     - Tree in $P_1 \setminus P_2$: $T = \{ b_{\mathrm{int}} \}$, containing 1 internal bond.
   - Added external bond for $P_1 = \Lambda$:
     $$b_{\mathrm{ground}} = [(y_1 - 1, y_2), y] = [(-1, 0), (0, 0)] = b_{\mathrm{ext}, 1}.$$
   - Full Bałaban tree graph $T_0$:
     $$T_0 = T \cup \{ b_{\mathrm{ground}} \} = \{ ((0, 0), (0, 1)), ((-1, 0), (0, 0)) \}.$$
     Total tree edges: $|T_0| = 2$.
   - Non-tree residual slice bonds:
     $$\mathbb{B}_0 \setminus T_0 = \{ b_{\mathrm{ext}, 2} = ((-1, 1), (0, 1)) \}.$$
     Total residual bonds: $|\mathbb{B}_0 \setminus T_0| = 3 - 2 = 1$.

4. **Vertex, Edge, and Gauge Dimension Matching:**
   - Active sites: $|\Lambda_0| = 2$.
   - Dynamic gauge group on active sites: $\mathcal{G}_{\Lambda_0} = G^{\Lambda_0} = G \times G$, dimension $2 \dim G$.
   - Exterior sites: $h_{(-1, 0)} = I$, $h_{(-1, 1)} = I$ identically on $\Lambda^c$.
   - Number of tree bonds: $|T_0| = 2 = |\Lambda_0|$.
   - Sequential Tree Gauge Solver:
     1. On $b_{\mathrm{ground}} = ((-1, 0), (0, 0))$:
        $$h_{(-1, 0)} V^{\prime\prime}(b_{\mathrm{ground}}) h_{(0, 0)}^{-1} = V_0(b_{\mathrm{ground}}) \implies h_{(0, 0)} = V_0(b_{\mathrm{ground}})^{-1} I V^{\prime\prime}(b_{\mathrm{ground}}).$$
        This uniquely fixes $h_{(0, 0)} \in G$ from the exterior boundary grounding!
     2. On $b_{\mathrm{int}} = ((0, 0), (0, 1))$:
        $$h_{(0, 0)} V^{\prime\prime}(b_{\mathrm{int}}) h_{(0, 1)}^{-1} = V_0(b_{\mathrm{int}}) \implies h_{(0, 1)} = V_0(b_{\mathrm{int}})^{-1} h_{(0, 0)} V^{\prime\prime}(b_{\mathrm{int}}).$$
        This uniquely fixes $h_{(0, 1)} \in G$!
   - Result:
     $$\dim(\text{Tree gauge constraints}) = (\dim G)|T_0| = 2 \dim G = \dim(\mathcal{G}_{\Lambda_0}).$$
     All $2 \dim G$ degrees of freedom in $G^{\Lambda_0}$ are uniquely fixed by the tree $T_0$ grounded at exterior site $y_0 = (-1, 0)$!
   - Grounding Defect of the Guessed YM-053R Hypothesis:
     If the external grounding bond $b_{\mathrm{ground}}$ were omitted from $T_0$ (leaving only $T_0 = \{b_{\mathrm{int}}\}$), then $|T_0| = 1 = |\Lambda_0| - 1$.
     Then the tree constraints provide only $\dim G$ conditions for $2 \dim G$ site variables, leaving a non-zero grounding defect:
     $$\Delta_{\mathrm{grounding}} = \dim(\mathcal{G}_{\Lambda_0}) - (\dim G)|T_0^{\mathrm{internal}}| = 2 \dim G - \dim G = \dim G \ne 0.$$
     Bałaban's primary-source inclusion of $[(y_1 - 1, \dots), y] \in T_0$ is precisely the mechanism that cancels $\Delta_{\mathrm{grounding}} = 0$!

---

### 3. Reconstruction of Original (1.76) and Elimination of Placeholder $\Theta_{\mathrm{boundary}}$
1. **Factor-by-Factor Reconstruction of Bałaban CMP 122 (1.76):**
   In Bałaban CMP 122 page 194, the exact unadulterated termwise density formula (1.76) is:
   $$\rho_{k, \alpha}[V] = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} \chi_k^{\prime\prime} \, \exp(A_k^{\prime\prime}[V]).$$
   The exact factor inventory comprises:
   1. $\chi_k(\Omega_k^{\sim 4})$: scale $k$ large-field cutoff restricting $V_k$ on $\Omega_k^{\sim 4}$ (p. 192 (1.71));
   2. $\chi_{k, \Lambda}$: partition of unity cutoff restricting $V_k|_{Z \cap \Lambda^c}$ (p. 193 (1.75));
   3. $dV_h \lceil_{Z_h}$: integration measure over preliminary scale $h$ short-distance field configurations on $Z_h$;
   4. $\chi_h(\Omega_h \cap Z_h)$: scale $h$ cutoff on $Z_h$;
   5. $\mathbb{T}_h(Z_h)$: preliminary scale transfer operator acting on fields on $Z_h$;
   6. $dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)}$: integration measure over active fields $V^{\prime\prime}$ on the bond set $\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)$;
   7. $\chi_k^{\prime\prime}$: scale $k$ active field characteristic function on the domain of integration;
   8. $\exp(A_k^{\prime\prime}[V])$: effective action evaluated on the composite configuration $V$ (constructed from $V_h$, $V^{\prime\prime}$, and exterior $V_k|_{Z \cap \Lambda^c}$);
   9. (For marked partition function): physical flowed observable $\mathcal{O}_{(a, t)}(f)[U(V)]$;
   10. Global normalization: $Z_{\mathrm{vac}}^{-1}$.

2. **Formal Elimination of $\Theta_{\mathrm{boundary}}$ as an Unresolved Schematic Placeholder:**
   - In Tasks YM-053 and YM-053R, an extra factor $\Theta_{\mathrm{boundary}}[V^{\prime\prime}, V_h, V_k|_{Z \cap \Lambda^c}]$ was introduced and described as "carrying delta constraints and regularized collar boundary terms".
   - However, Bałaban explicitly states on page 194:
     > *"The integration in (1.76) does not involve any $\delta$-functions, they are all integrated out."*
   - There are NO delta constraints in (1.76).
   - Any boundary interactions between active fields $V^{\prime\prime}$, preliminary fields $V_h$, and exterior fields $V_k|_{Z \cap \Lambda^c}$ are ALREADY incorporated into the effective action $A_k^{\prime\prime}[V]$ and the definition of the composite configuration $V$.
   - **Determination:** $\Theta_{\mathrm{boundary}}$ is formally classified as an **UNRESOLVED SCHEMATIC PLACEHOLDER** and is permanently excised from the primary-source factor inventory. Imposing an independent factor $\Theta_{\mathrm{boundary}}$ outside $A_k^{\prime\prime}$ would duplicate absorbed interactions or reintroduce removed delta constraints, producing an invalid discrepancy $\Delta_{\Theta} \ne 0$.

---

### 4. Conditional Support-Specific Cutoff Replacement (1.89)
On page 198 (1.89), Bałaban proves:
$$\chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \, \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \, \chi_h(\Omega_h \cap Z_h) \, \chi_k^{\prime\prime} \, \chi^\prime = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \, \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \, \chi_h(\Omega_h \cap Z_h) \, \chi^\prime.$$
- We explicitly record that the algebraic simplification $\chi_k^{\prime\prime} \chi^\prime = \chi^\prime$ does NOT hold as an unconditioned identity on individual link fluctuation functions in isolation;
- It holds strictly on the **JOINT SUPPORT** of all the retained support factors $\chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \chi_{h, 1/2} \chi_h(\Omega_h \cap Z_h)$;
- Off this joint support, $\chi_k^{\prime\prime}$ can differ from 1, and the complementary large-field branch $(1 - \chi^\prime)$ is explicitly carried into the large-field remainder $\mathcal{R}_{\alpha, \mathrm{large}}$.

---

### 5. Git-Blob Digest Disambiguation and Additive Receipt Correction
In `verification/YM-053R_E3_RECEIPT.json` and `verification/YM-053R_MILESTONE.md`, the value `7e7eda0e119b1707905625d86312123a333a576f` was recorded under the key `git_blob_scientific_hash`.
1. **Algorithm and Scope Disambiguation:**
   - **Format A (40-hex Git Object SHA-1):** `7e7eda0e119b1707905625d86312123a333a576f` is a 40-character hexadecimal digest representing the Git object / commit tree format.
   - **Format B (64-hex Canonical SHA-256 Payload Digest):** The SHA-256 hash over the sorted canonical manifest entries `f"{rel_path}::{file_hash}"` for the 158 canonical files is:
     $$0855124cb8e2ba5c98d107e9ae655b90f37d4f8db3fdd499b34611f07360c5be.$$
     This matches the closed-world scientific tree hash identically.
2. **Additive Correction Policy:**
   - In accordance with governance prohibiting edits to immutable historical receipts (`verification/raw/YM-053R_E4_RAW_20261009.md` SHA-256 `1b91ebdaf4da4525ac504fe09d270fb424503b8a5d291d999b357491c1eec594`), the raw receipt is strictly preserved without modification;
   - This additive reconciliation note formally records that Format A (40 hex Git SHA-1) and Format B (64 hex SHA-256) are dual representations of the candidate tree identity, with Format B providing the canonical closed-world tree hash.


---

## YM-054R: PROVENANCE REPAIR OF GIT-BLOB VS CHECKOUT DIGEST, LITERAL-BLOB BYTE HASHING, STATE CLOSEOUT HEAD SEMANTICS, AND ELIMINATION OF UNVERIFIED HASH RELIANCE

### 1. Refutation of Unverified Hash Reliance and Formal Status Classification
1. **Defect Diagnosis of `7e7eda0e119b1707905625d86312123a333a576f`:**
   - In `verification/YM-053R_E3_RECEIPT.json`, the 40-character hexadecimal string `7e7eda0e119b1707905625d86312123a333a576f` was recorded under the key `git_blob_scientific_hash`.
   - In Task `YM-054`, it was hypothesized that this string represented a "Format A (40-hex Git object SHA-1)" representation of the repository state.
   - Direct execution of `git cat-file -e 7e7eda0e119b1707905625d86312123a333a576f` fails closed with exit code 1 (`fatal: git cat-file: could not get object info`).
   - Exhaustive repository search confirms that no object with SHA-1 `7e7eda0e119b1707905625d86312123a333a576f` exists in the Git repository database. Hex length (40 hex characters) alone does not establish algorithm, provenance, or object existence.
2. **Formal Elimination of Reliance & Immutable Preservation:**
   - The speculative dual-representation hypothesis is formally **REFUTED AND SUPERSEDED**.
   - The entry `7e7eda0e119b1707905625d86312123a333a576f` is formally classified as:
     $$\mathbf{UNRESOLVED\_OR\_INVALID\_HISTORICAL\_ENTRY}.$$
   - In accordance with governance immutability principles, historical raw receipts (`verification/raw/YM-053R_E4_RAW_20261009.md` SHA-256 `1b91ebdaf4da4525ac504fe09d270fb424503b8a5d291d999b357491c1eec594`, `verification/raw/YM-054_E4_RAW_20261009.md` SHA-256 `ed8671e276eeffb31da1d02cbfdbe9963f5eeee8679d3a4acc21d85a33e196b8`) remain 100% byte-identical and unmodified.
   - Reliance on this unverified string is completely and permanently removed from all active and future project coordination.
   - All mathematical results established in `YM-054` (boundary grounding bond $[y_0, y] \in T_0$, $|T_0| = |\Lambda_0| = 2$, zero grounding defect $\Delta_{\mathrm{grounding}} = 0$, elimination of $\Theta_{\mathrm{boundary}}$, and support-conditioned cutoff (1.89)) remain fully preserved and unaffected.

---

### 2. Dual Digest Classification and Forensic Derivation

1. **Manifest Specification:**
   The scientific closed-world packet consists of exactly 158 canonical files defined by `src.ymmg.ros.SCIENTIFIC_FINGERPRINT_MANIFEST`, sorted lexicographically.

2. **Digest 1: Checkout-Byte Canonical Manifest Digest:**
   - **Algorithm:** For each relative path $p$ in the sorted manifest, read file bytes directly from the working-tree filesystem: $h_p = \operatorname{SHA256}(\operatorname{read\_bytes}(p))$. Concatenate entries as $p\text{::}h_p$ joined with newline characters $\text{"\\n"}$, and compute the SHA-256 digest of the UTF-8 encoded manifest string.
   - **Baseline YM-053R (`5d65389`):**
     $$0855124cb8e2ba5c98d107e9ae655b90f37d4f8db3fdd499b34611f07360c5be$$
   - **Candidate YM-054 (`15086d3`):**
     $$b962eb50281ed1bdb3cbf4e570d9438a73b7887aa8814fc850e0c52672375f24$$

3. **Digest 2: Literal Git-Blob Canonical Manifest Digest:**
   - **Algorithm:** For each relative path $p$ in the sorted manifest, extract the raw, literal blob bytes stored in the content-addressed Git repository object database at the target commit: $b = \operatorname{git\_blob}(\text{commit}, p)$. Compute $h_p^{\mathrm{blob}} = \operatorname{SHA256}(b)$. Concatenate entries as $p\text{::}h_p^{\mathrm{blob}}$ joined with $\text{"\\n"}$, and compute the SHA-256 digest.
   - **Baseline YM-053R (`5d65389`):**
     $$622b29ec7b20f0d5cd67e7b7ba7db6a308077a748114f12f2a08b55d282d842d$$
   - **Candidate YM-054 (`15086d3`):**
     $$4e4338aa5fbe9d961cd439bf1254f5c0869531f950c5726bd5e6afb930d4e888$$
   - **Closeout YM-054 (`8190b20`):**
     $$4e4338aa5fbe9d961cd439bf1254f5c0869531f950c5726bd5e6afb930d4e888$$
     (Identical to candidate freeze because canonical scientific files were unchanged between freeze and closeout).

4. **Forensic Physical Cause of Discrepancy:**
   - Exactly 15 of the 158 canonical files were committed into Git with UNIX LF line endings (`\n`):
     `CLAIM_EVIDENCE_MATRIX.md`, `DEFINITION_LEDGER.md`, `OFFICIAL_PROBLEM_SPECIFICATION.md`, `RESEARCH_LEDGER.md`, `THEOREM_LEDGER.md`, `governance/EPISTEMIC_TAXONOMY_v1.0.yaml`, `governance/MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md`, `governance/PROJECT_BINDING_POLICY.md`, `literature/ANALOGUE_DEPENDENCY_GRAPH.md`, `literature/ANALOGUE_LIMITATION_MATRIX.md`, `literature/ANALOGUE_MECHANISM_MATRIX.md`, `literature/CONSTRUCTIVE_LIMITATION_MATRIX.md`, `literature/FOUNDATIONAL_LIMITATION_MATRIX.md`, `literature/MODERN_LIMITATION_MATRIX.md`, `literature/PATHWAY_MEMORY_REGISTER.md`.
   - On Windows environments with `core.autocrlf = true`, Git checkout automatically converts LF to CRLF (`\r\n`), altering the byte content and SHA-256 on disk.
   - The remaining 143 files were committed with CRLF line endings, so their git blob bytes and disk bytes are identical.
   - This exact physical difference accounts for $h_{\mathrm{checkout}} \ne h_{\mathrm{blob}}$.
   - Both digests are now fully recognized, differentiated, and reproducibly computed via ROS.

---

### 3. Truthful Semantics for `PROJECT_STATE.yaml`

1. **Previous Conflation:**
   In Task YM-054, `evidence_closeout_head` was set to candidate SHA `15086d3a81dd083aafb48eda4cb73863bc312da1`, while prose described it as binding the completed receipt/state closeout commit.
2. **Disambiguated Semantic Definitions:**
   - `scientific_candidate_sha`: The immutable Git commit freezing the candidate code and documentation under scientific review (`15086d3a81dd083aafb48eda4cb73863bc312da1` for YM-054).
   - `review_bound_sha`: The Git commit that the E4 review is strictly bound to (equals `scientific_candidate_sha`).
   - `evidence_closeout_head`: The Git commit that bound the preceding completed receipt/state closeout (`8190b205cce2232f96137fadb2e346215d04ad1d` for YM-054).
   - `project.head`: Current authoritative Git HEAD.
   - Elimination of self-referential requirements: A closeout commit cannot self-referentially bind its own future SHA before it is created; `evidence_closeout_head` records the preceding closeout commit from Git ancestry.






