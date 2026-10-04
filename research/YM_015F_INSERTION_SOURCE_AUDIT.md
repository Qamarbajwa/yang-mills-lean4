# YM-015F insertion and source audit

Date: 2026-10-04. Research candidate only; no governance status changes. Target: `literature/YM-015R2-FLOWED-CONTINUUM-TARGET.md`. Baselines read: YM-015 Bałaban UV ledger and YM-004 primary-source map and small/large-field audit. For current scientific interpretation this audit supersedes the suspect bibliography labels identified below; historical ledgers are preserved. Governance authority remains with the reconciliation record maintained by the parent task.

## Result

No verified primary theorem found in this bounded search supplies the required nonperturbative, cutoff-uniform Wilson-flow clover energy insertion estimate for four-dimensional SU(N) Wilson lattice measures on the stated bare-coupling trajectory. This is a search result, not a proof of nonexistence. L1 remains an unproved target. Its displayed large-field and small-field arguments contain additional gaps beyond merely inserting an observable into an existing expansion.

## Immediate correction of proof shortcuts

1. **Global bad-sector suppression is unsupported.** A polymer estimate decaying with the size of a specified bad polymer does not imply that the event of at least one bad polymer costs the action of the entire lattice. The target writes `mu(Omega_large) <= exp(-c beta V/a^4)` without a verified source theorem. For the union of local bad events, a union bound contains the number of possible positions, rather than an exponential penalty proportional to total volume. Nor are signed effective activities automatically probabilities under the normalized Wilson measure.

   Elementary countermodel: M independent bad-site indicators with probability p=exp(-c beta). Every specified set of m bad sites has probability p^m, while the event that at least one site is bad has probability 1-(1-p)^M, which is at least p. This violates an asserted bound p^M whenever M>1. The model is not a counterexample to Yang–Mills L1; it disproves the logical implication from local size suppression to the proposed global-event estimate.

   Even if a probability estimate of order M exp(-c beta) were available, using the deterministic observable ceiling a^(-4k) requires quantitative exponent comparison. With M of order a^(-4) and beta of order b log(1/a), that crude argument would require cb >= 4(k+1) for boundedness. One fixed exponent does not control every moment order. A flow-adapted localized insertion bound must replace this step.

2. **Linear heat smoothing does not establish nonlinear gauge-flow smoothing.** The nonlinear Duhamel contribution must be controlled in a specified gauge and physically scaled norm, uniformly in lattice spacing and through every small/large-field boundary. Dimensionless small link coordinates do not supply a uniform physical connection bound: U=exp(aA_phys) makes A_phys potentially proportional to a^(-1) times the link coordinate. The target's `||A|| <= chi(a)` needs its units, normalization, gauge slice, and cutoff dependence specified before any continuum PDE estimate applies. No verified estimate justifies the displayed cutoff-independent C/t energy ceiling over its sector.

3. **Vacuum stability does not control source derivatives.** Algebraically z_a(s)=exp(s/a) has z_a(0)=1 for all a, but its kth derivative at zero is a^(-k). Thus bounds at zero source do not imply insertion estimates even for entire source functions. Uniform analyticity radii and uniform source norms, or explicit marked-coefficient estimates, are additional inputs.

4. **An exponential source estimate is stronger than required.** Having every fixed moment finite does not imply a positive moment-generating radius (a lognormal random variable supplies an elementary example). Do not silently strengthen L1 to a common source disk for all degrees. A finite-degree marked algebra avoids this issue.

## Verified source mapping and limits

These rows distinguish author/publisher abstract verification from theorem-level extraction. No numerical polymer exponent or theorem number is imported from inaccessible full text.

| Primary source | Verified content / access | Mapping to target and outstanding mismatch |
|---|---|---|
| Bałaban, *Ultraviolet stability of three-dimensional lattice pure gauge field theories*, CMP 102 (1985), 255–275, [primary article PDF](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/46460/220_2005_Article_BF01229380.pdf?sequence=1) | Title and paper opening explicitly specify three dimensions. | The YM-015 ledger labels this entry four-dimensional main UV stability. That identification is incorrect. No 4D insertion theorem follows. |
| Bałaban, *Convergent renormalization expansions for lattice gauge theories*, CMP 119 (1988), 243–285, [publisher](https://link.springer.com/article/10.1007/BF01217741) | Publisher abstract verifies inductive complete densities including large-field domains; completion/convergence there is stated for superrenormalizable models. Full text was subscription restricted during this audit. | Useful architecture; not a verified 4D flowed-observable theorem. Publisher references identify CMP 116, 1–22 as *Renormalization group approach to lattice gauge field theories. II. Cluster expansions*, conflicting with the ledger's title/page assignment. |
| Bałaban, *Large field renormalization. II. Localization, exponentiation, and bounds for the R operation*, CMP 122 (1989), 355–392, [publisher](https://link.springer.com/article/10.1007/BF01238433) | Publisher abstract explicitly states completion of four-dimensional pure-gauge UV stability, formulated in Theorem 1. Full text subscription restricted. | Establishes correct bibliographic home of final 4D stability; does not verify the ledger's precise weighted activity formula, probability interpretation, source derivatives, flow locality, or the target trajectory. Those hypotheses need full theorem extraction. |
| Brydges–Slade, *A renormalisation group method. V. A single renormalisation group step*, [author preprint](https://arxiv.org/abs/1403.7256) | Author abstract specifies finite-range covariance decomposition, a nonperturbative coordinate, and conditional one-step contraction. | Rigorous framework suggests marked polymer norms and localization. Gauge geometry, Wilson measure, flow map, and running nonabelian coupling are missing mappings; no direct transfer is valid. |
| Slade–Tomberg, *Critical correlation functions for the 4-dimensional weakly self-avoiding walk and n-component phi^4 model*, [author preprint](https://arxiv.org/abs/1412.2668) | Author abstract verifies weak-coupling correlation results, including square-component composites, for specified scalar/walk models. | Evidence that composite insertions require a dedicated RG analysis. It supplies no gauge-field, compact-link, or flowed-energy estimate. |
| Lüscher–Weisz, *Perturbative analysis of the gradient flow in non-abelian gauge theories*, [author preprint](https://arxiv.org/abs/1101.0963) | All-loop finiteness after ordinary four-dimensional renormalization is explicitly perturbative. | Correct observable and dimension, wrong type of bound: coefficientwise perturbative finiteness does not bound the full nonperturbative Wilson measure uniformly in a. |

The ledger's phrase “exact Bałaban polymer activity estimate” is not accepted as exact evidence here: its displayed weights and scale-independent constants have not been matched to primary full-text definitions. Earlier accepted documents remain unchanged; this audit records reconciliation work needed rather than revoking their statuses.

## Precise missing lemma: finite-degree marked RG summability

The project's selected finite-source formulation and its elementary coefficient-norm proof are in [YM_015F_SOURCE_JET_REDUCTION.md](YM_015F_SOURCE_JET_REDUCTION.md), lemma YM-015F-JET-002 (OPEN). The connected-expansion formulation below is an optional sufficient refinement of that same missing estimate, not a competing target or a claimed source theorem. It may be more demanding than directly bounding the full source jet.

Fix moment degree q, physical volume, group, positive minimum flow time, and paired labels (t_j,f_j), with ||f_j||_(H^3)<=1. Let A_q=C[eta_1,...,eta_q]/(eta_1^2,...,eta_q^2), with commuting generators. The exact finite-lattice normalized source object is

    R_a(eta) = < product_j (1 + eta_j O_(a,t_j)(f_j)) >.

Its eta_1...eta_q coefficient is exactly the desired qth mixed moment, without factorials or an exponential integrability assumption. A sufficient missing lemma must construct, by the actual Bałaban integration maps, an exact marked connected expansion

    log R_a(eta) = sum_C W_a(C;eta)

in A_q and prove, for every nonempty I subset {1,...,q},

    sup_a sum_C | [eta_I] W_a(C;eta) | <= K_|I|(t_min,L_phys,N).

Here C must include all multiscale connected marked contributions, including terminal coarse-field integration and vacuum/source counterterms; the total sum is in physical smeared normalization. The statement is not merely an unmarked norm with formal differentiation attached. To prove it one must specify the polymer/block metric, source norm, activity regulators, exact source transport through gauge fixing/blocking, treatment of the flow's tails, bad-field contributions, normalization by Z_a(0), and the weak-coupling stopping scale. At arbitrary fixed physical volume the terminal integration cannot be assumed weakly coupled. A multiscale induction valid only below g_* must provide a separate, uniform terminal estimate at that stopping scale.

**Conditional consequence, fully algebraic:** Since the constant coefficient of R_a is one, its logarithm exists as a finite polynomial in the nilpotent ideal. Exponentiating its connected coefficients gives

    [eta_{1,...,q}] R_a = sum_{partitions pi of {1,...,q}} product_{B in pi} [eta_B] log R_a.

Taking absolute values yields the cutoff-independent bound sum_pi product_(B in pi) K_|B|. Rescaling each test function proves L1. This proves only that the missing marked summability lemma is sufficient; it does not construct its activities or prove its analytic estimates. It also explains exactly why vacuum coefficients do not suffice.

## Boundary of downstream conclusions

L2 extraction is conditional on L1 and is for each fixed tuple of flow times, or a countable collection handled diagonally. Uncountably many tuples require additional time equicontinuity/regularity. Permutation symmetry exchanges paired labels (t_j,f_j), not f_j alone while distinct t_j remain fixed. An arbitrary SO(4) rotation generally does not descend to the cubic periodic torus: at fixed torus only lattice-preserving rotations are global symmetries. Local rotational-restoration statements need a separately formulated geometry/limit. No mass gap, reflection positivity, nontriviality, or infinite-volume result is obtained here.

## Next justified work

Retrieve the actual CMP 122 Theorem 1 and inductive activity bounds with exact conventions; correct the dimension/title/page mismatches in a separately reviewed reconciliation. Then develop degree-one marked flowed-energy transport before attempting general q. Its first hard step is a cutoff-uniform, physically normalized flow insertion bound under the conditional fine-field integration, including large-field sectors and the terminal measure. Failure to derive that bound leaves E-UV-FLOWED open.
