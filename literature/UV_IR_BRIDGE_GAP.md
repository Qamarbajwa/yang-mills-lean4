# YM-002F — UV–IR Bridge Gap

## Working bridge under test

`UV asymptotic freedom / RG control → controlled continuum construction →
nontriviality → nonperturbative IR correlation control → positive spectral gap
→ OS/Hilbert-space reconstruction`.

The repository evidence supports the arrows as requirements and partial
programs, not as a completed chain.

| Segment | Known left/right result | Exact missing connection | Uniformity/limits involved | Source refs |
|---|---|---|---|---|
| UV running | Gross–Wilczek/Politzer negative beta; Bałaban UV stability in finite V | Extend UV inductive estimates through the strong-coupling crossover | `a→0`, RG scale `k`, fixed `V` then `V→∞` | THM-YM-0006; THM-YM-0018; NEG-CONST-001 |
| Continuum measure | MRS constructs Schwinger distributions with `Lambda_IR>0` | Remove the IR regulator while retaining a nontrivial, gauge-invariant measure | `a→0`, `Lambda_IR→0`, volume removal | THM-YM-0020; NEG-CONST-002 |
| Nontriviality | Pure YM is expected to be interacting; Chatterjee's Higgs limit is Gaussian | Exclude a Gaussian/trivial limit for pure scalar-free 4D YM | scaling of interactions and renormalized observables | THM-YM-0030; YM-REQ-014 |
| IR correlations | SZZ proves exponential decay at strong lattice coupling; 3D monopole models prove screening | Obtain gauge-invariant decay on the weak-coupling continuum trajectory | `beta→∞`, `a→0`, `V→∞`; constants uniform in `a,V` | THM-YM-0027; THM-YM-0013; NEG-MOD-003 |
| Spectral gap | OS/lattice reflection positivity supplies reconstruction machinery; lattice gaps exist in restricted regimes | Identify a positive Hamiltonian gap `Delta` and prove it persists under both limits | transfer matrix → continuum Hilbert space; volume and cutoff limits | THM-YM-0005; THM-YM-0009; YM-REQ-007/019 |
| Gauge-invariant observables | Wilson-loop/area-law bounds and propagator mechanisms exist | Control the local gauge-invariant operator algebra and connect observables to spectrum | loop perimeter→∞, regulator removal, gauge fixing independence | YM-REQ-009/013; THM-YM-0028/0029; YM-002E |

## Current best theorems

1. Perturbative UV asymptotic freedom and renormalizability (A).
2. Finite-volume 4D UV stability and IR-regulated constructive Schwinger
   functions (B).
3. Infinite-volume strong-coupling lattice spectral/correlation bounds (C).
4. OS reconstruction and lattice reflection positivity (A), conditional on
   suitable Schwinger functions.
5. Exact lower-dimensional and modified-theory mechanisms (D), which expose
   transfer barriers rather than close the pure-4D chain.

## Exact unknown

No accepted record supplies a theorem giving, for every compact simple group,
one nontrivial 4D continuum measure with OS/Wightman control and a positive
Hamiltonian spectral gap. The project synthesis therefore identifies a missing
interface, not a proved obstruction theorem.

## Why existing results do not close it

The strongest UV and IR results live in different regimes or models. Fixed
cutoff and strong-coupling statements do not provide the weak-coupling
continuum limit; gauge-fixed propagator scales do not identify a gauge-invariant
Hamiltonian spectrum; conditional programs leave load-bearing hypotheses open;
and analogue mechanisms change dimension, matter content, supersymmetry, large
`N`, or the underlying duality. These are precise scope boundaries, not claims
that no future construction can bypass them.
