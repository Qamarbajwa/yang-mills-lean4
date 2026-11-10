# Control matrix, evidence requirements, and implementation maturity

Interpretation: `S` = specification only; `P` = Python structural prototype/preflight (not a trusted authorization); `H` = external authenticated host required; `M` = qualified mathematical reviewer; `L` = real isolated Lean required. An item tagged `P` does **not** meet an `H/M/L` requirement.

| Control | What must be prevented | Status | Acceptable evidence |
|---|---|---|---|
| C01 | Original question rewritten | P+H | Owner-signed raw prompt + off-host anchor |
| C02 | Interpretation treated as fact | S+H+M | Typed intuition/meaning decision and evidence |
| C03 | Topic drift between versions | S+H | Source-linked intent chain, owner amendment |
| C04 | Fabricated or missing prompt/result | P+H | Event capture, hash-linked archive, external anchor |
| C05 | Worker claims Lean passed | P+L+H | Real runner receipt, source/toolchain pins |
| C06 | `sorry` in dependencies | P+L | `#print axioms`, independent kernel check |
| C07 | Proof targets wrong theorem | S+M+L | Independently authored comparator challenge + semantic review |
| C08 | Open subgoals presented complete | P+L | Complete goals/obligations inventory, check pass |
| C09 | Invalid inference side-condition | S+M+L | Proof term or line-specific reviewed justification |
| C10 | Hidden/unlisted graph dependencies | P+H+M | Source-derived graph and audited completeness |
| C11 | Wrongly merged parallel paths | P+H | Typed branch policy, evidence-backed merge |
| C12 | Independent branches contaminated | S+H | ACL/read logs, blinded study records |
| C13 | Incorrect 5/10 progress reporting | P | Separate task vs proof status report |
| C14 | Supervisor accepting own outputs | P+H | Trusted actor role + distinct reviewer/acceptor |
| C15 | Model context lost | P+H | Exact context capsule, recall test, checkpoint |
| C16 | Inadequate model used | S+H | Per-task capability evaluations, escalation history |
| C17 | Stronger model exceeds authority | P+H | External least-privilege policy |
| C18 | Version change unnoticed | P+H | Trusted before/after diff and invalidation |
| C19 | Undetected stale diagrams | S+H | Generated views from approved graph digest |
| C20 | Negative results suppressed | P+M | Evidence inventory vs report bi-directional audit |
| C21 | Unsupported cross-project connection | S+H+M | Type, rationale, provenance, boundary, access grant |
| C22 | No real reviewer independence | S+H | Distinct identity, readonly workspace and original review |
| C23 | Unbounded retries/cost | P+H | Leases, quotas, watchdog and receipts |
| C24 | Crash/liveness falsely reported | S+H | Independently measured progress, idle/lease signals |
| C25 | Prompt injection / data exfiltration | S+H | Input trust labels, secrets isolation, tool grants |
| C26 | Invented source/citation | S+H | Source fetch digests and citation lookup |
| C27 | Formal proof under false axioms | S+L+M | Verified allowed axiom set, assumption audit |
| C28 | Invalid independent acceptance | S+H | Signed exact digests and qualified acceptor |
| C29 | Unfounded publication novelty | S+M | Current literature research, novelty claim review |
| C30 | Chrysalis rewires permissions | S+H | L3 human approval, topology diff, reversible cutover |
| C31 | Concurrent workers overwrite state | S+H | CAS single writer, lease and branch read/write log |
| C32 | Uncertain external effects retried | S+H | Idempotency key and effect reconciliation |

**Acceptance rule:** Any C01–C32 tagged H/M/L that has not been met remains NOT VERIFIED. The framework is a working candidate, not a verified end-to-end system.
