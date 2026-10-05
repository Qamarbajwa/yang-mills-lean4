# YM-015F — constrained coordinates source audit 038

Candidate for review. Read accepted 036 and terminal037. No all-sector or measure-H closure.

## Access and primary extraction

Ordinary PowerShell HTTP download of [CMP109](https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104116842) returned 5,490,078 bytes, 54 PDF pages on 2026-10-05. Bytes were extracted in memory; printed266/PDF18 was rendered to a temporary image and visually checked. Python urllib separately returned a one-page denial. Inspected printed265–268; not the complete article or predecessors.

Source-derived extraction (under 200 words): printed266,(2.9),

    chi_k = product_{b in T^(k) \ {b_0(c): c in T^(k+1)}} chi({|B'(b)| < epsilon_1}).

The alternative coupling-dependent threshold immediately below (2.9) is g_k/gamma_k times epsilon_1. Printed267 states induced restrictions on excluded bonds use `O(epsilon_1)`. Printed265 defines `V'=V(V^(k))^(-1)` and `B'=(1/i)log V'`, under regular-background assumptions. Printed267,(2.10), retains `dB' sigma(B') delta(tilde Q(B'))`, the cutoff, gauge-fixing expression and action; constant factors `sigma_0` enter `N'_k`. The analytic transformation `B'=B-hD(B)` linearizes the constraint to `delta(QB)`, followed by coupling scaling. Printed268 eliminates constrained bonds, writes `B'=CB`, and obtains Gaussian covariance `(C* A^(k) C)^(-1)`. There `N'_k` is the integral at `U_(k+1)=1`. Predecessor pointers: printed267, Sect.C [15], Sect.E [14]; printed265, Sect.G [15].

## Own interpretation and remaining obligations

The cutoff is stated in background-dependent fluctuation coordinates and excludes bonds fixed by the constraint. It is not an independently imposed unrestricted bound on every original group variable. The initial multiplication reading of the alternate threshold was challenged by visual review and is withdrawn. The division reading is corroborated by the displayed page and independent primary-text acquisition before freeze. Damaged text extraction alone must not determine that formula.

For a source jet transported through this map, every selected insertion coefficient must be rewritten through the actual sequence of coordinate and gauge transformations. Its Jacobians, constrained variables, cutoff support and integrability must be retained. This is an obligation inferred from change of variables, not a source-insertion theorem extracted from the paper. Vacuum normalization at the identity does not supply global Wilson normalization; the scalar-factor and terminal-functional obligations of 037 remain.

The displayed coordinate integral supplies additional dictionary entries but does not establish the complete finite positive constrained-measure interpretation H of 036. No all-sector density reconstruction, physical Wilson-flow coordinate representation, source counterterm estimate, marked large-field summability, uniform terminal density-ratio bound, continuum construction or mass gap is claimed.

[CMP119](https://link.springer.com/article/10.1007/BF01217741) and [CMP122](https://link.springer.com/article/10.1007/BF01238433) again exposed subscription previews only. CMP122 reference4 identifies *Large field renormalization. I. The basic step of the R operation*, CMP122,175–202, as a useful next primary target; its full text was not inspected here. Public-access failures are access gaps, not impossibility results.
