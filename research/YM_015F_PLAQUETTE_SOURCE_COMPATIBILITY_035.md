# YM-015F plaquette-source compatibility audit 035

Date: 2026-10-04. Writer research artifact; unreviewed, no accepted-state promotion. Inputs inspected: raw `verification/raw/YM-015F-JET-002A_WRITER_RAW_20261004.md`, canonical `governance/YM_AUTONOMOUS_DISCOVERY_ARCHITECTURE.md`, and `literature/YM-015R2-FLOWED-CONTINUUM-TARGET.md`. The latter specifies the target, not established insertion estimates; its sector and smoothing assertions are not premises here.

## Primary-source extraction (under 200 words)

[Section V, equation (82), Theorem 4 equations (83)/(84), and Remark 16](https://arxiv.org/html/2205.07376v2#S5) concern periodic, unflowed scaled plaquettes. The field is P=a^(d/2) F^u=sqrt(gamma) ImTr(U_p-1), gamma=a^(d-4)/g^2. The normalized generating function is a source-decorated partition function divided by its vacuum partition function; the sources couple directly to P. Equation (83) uses z_u(rJ_j), numerator exponent 2^d Lambda_r/(r Lambda_s), and denominator exponent 2^d(Lambda_r+Lambda_e)/(r Lambda_s), inside each of r factors. Equation (84) uses gamma^(-N^2/2) and a Gaussian source bound. [Section II, periodic-bond paragraph](https://arxiv.org/html/2205.07376v2#S2) gives Lambda_e=dL^(d-1), Lambda_s=L^d. [Remark 1](https://arxiv.org/html/2205.07376v2#S1) concentrates the text on U(N), describing SU(N) as requiring modifications. Remark 16 prints H=A_p/(a^4 g) and S=a^d H, asserting a carryover of methods. It gives no flowed clover identification. The displayed formula's coupling normalization and the SU(N) modification require extraction before import.

## Independent algebra: exact boundary cancellation

These calculations use (83)/(84), not a new theorem about the target. Put q=N^2/2, A=2^d Lambda_r/(r Lambda_s), B=2^d(Lambda_r+Lambda_e)/(r Lambda_s), c=c'_u, and h=pi^2 N/8. Substitute z_u(rJ_j)<=gamma^(-q)exp(c+h r^2|J_j|^2), z_l>=gamma^(-q)exp(c_l). Each factor contributes

    gamma^[q(B-A)] exp[A c-B c_l+A h r^2|J_j|^2].

Thus the boundary exponent is 2^(d-1)N^2 Lambda_e/(r Lambda_s) PER FACTOR, and 2^(d-1)N^2 Lambda_e/Lambda_s for the WHOLE PRODUCT. The full bound obtained by this substitution is

    gamma^[2^(d-1)N^2 Lambda_e/Lambda_s]
      * exp[2^d Lambda_r/Lambda_s (c-c_l)
            -2^d Lambda_e/Lambda_s c_l
            +(pi^2 N/8)2^d r Lambda_r/Lambda_s sum_j |J_j|^2].

This also exposes a coefficient-check task: literal substitution into the displayed thermodynamic product retains 2^d(d-1) in the quadratic coefficient and removes 1/r from the constant coefficient. The later printed bound should therefore be checked against the PDF/proof; do not silently use its displayed constants.

For the target diagonal d=4, L=L_phys/a (even lattice subsequence), Lambda_e/Lambda_s=4/L=4a/L_phys EXACTLY. The product boundary factor is

    gamma^[32 N^2 a/L_phys].

With gamma=1/g_0^2(a)=Theta(log(1/a)), its logarithm is O(a log log(1/a))->0. It tends to one and is bounded on a sufficiently small AF tail. At fixed L, g->0 can make this upper estimate diverge. That does not show divergence of the actual generating function, falsify Theorem 4, or obstruct the fixed-physical-volume AF diagonal. No independent limits have been interchanged here.

## Independent observable and normalization diagnostics

The source derivative in Theorem 4 inserts P, not a physical curvature square. The scaling multiplier of the partition function cancels in the normalized ratio; it does not cancel field or coupling factors in a source derivative. Restoring F^u multiplies each insertion by a^(-d/2); a pointwise bound on P alone therefore supplies no uniform physical bound.

For fundamental SU(2), every group matrix has real trace, so P=0 identically. For SU(N) in a smooth traceless curvature expansion, Tr F=0: the trace-linear field misses the leading nonabelian curvature information. Quadratic energy can remain nonzero. These are algebraic observable-mismatch diagnostics, not counterexamples to a theorem about P.

Using the source parametrization U_p=exp(i g a^2 F+...), the independent smooth-field expansion gives A_p=||U_p-1||_HS^2 approximately g^2 a^4 Tr(F^2). The printed Remark 16 choice H=A_p/(a^4 g) consequently has leading term g Tr(F^2), whereas a conventional curvature-square matching would require division by g^2 under this convention. Do not correct the printed formula silently or identify S with the target energy. The precise target clover convention, including any absorbed coupling, must be matched first. Likewise, changing from U(N) Haar eigenvalue integrals (dimension N^2) to SU(N) (dimension N^2-1) needs a proved determinant-constrained integral and constants; replacing the exponent alone is insufficient.

Even a verified unflowed action-density moment estimate does not supply fixed-positive-physical-flow clover estimates. The flow acts on links, the clover involves several plaquettes, and a uniform source bound at bounded r does not control a smeared source whose number of lattice points grows like a^(-4) without additional estimates.

## XFER-YM-PLAQUETTE-035 (conditional proposal)

- Source branch: periodic Wilson plaquette reflection/Haar bounds, arXiv:2205.07376v2 Theorem 4.
- Target branch: YM-015F-L1 on a fixed physical four-torus, SU(N), AF trajectory, flowed clover energy tested in H^3.
- Mechanism: normalize sources explicitly, use reflection bounds for a compatible insertion majorant, then Cauchy estimates for moments.
- Verified mapping: compact finite lattice, positive normalized Wilson measure, gauge-invariant observables; boundary geometry is compatible with the AF diagonal after the calculation above. The raw conditional-kernel receipt transports finite-cutoff degree-one insertions exactly, with constant-one Jensen domination only.
- Essential missing hypotheses: proved SU(N) source theorem; exact quadratic-field coupling convention; cutoff-uniform source radius and bounds for the actual flowed clover insertion; a flow comparison or dominated source representation with physical-time constants; control of smeared-source support growth and all moment orders; source-decorated RG activities and normalization denominators if individual signed polymers are used. Positive full-measure contraction cannot be assigned to signed polymer pieces.
- Allowed conclusion now: candidate method and a corrected boundary-factor compatibility test. No closure of L1, continuum construction, local OS edge, or mass gap follows.
- Failure class: METHOD_SPECIFIC_OBSTRUCTION (observable/source mismatch and missing hypotheses), not structural no-go.

## Next bounded extraction

Retrieve the author PDF for v2 and extract only Remark 16, Theorem 4, and Section VI.5, with equation/page locators. Resolve the g versus g^2 quadratic normalization, the displayed constant discrepancies, and whether the quadratic source carryover has a bounded complex-source disk or an entire-source estimate. Then extract the determinant-one Haar constraint and an explicit SU(N) version from the cited group-integration reference or a primary author proof. Stop at the first missing lemma; formulate that exact source inequality before attempting any unflowed-to-flowed transfer. This is the next research task, not an asserted existing theorem.

No governance, accepted revision, DAG edge, or scientific invariant is changed by this artifact.
