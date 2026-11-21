# Rosetta Subtractive Quotient Solver

High-performance linear algebra engine based on subtractive quotient projection and Schur complement condensation.

Author: Qamar Munawer  
Affiliation: Brandenburg University of Technology Cottbus-Senftenberg  
Methodology: ai is being used as a tool  
Epistemic Status: Practical engineering numerical toolkit (`status: verified-finite`). All Clay Millennium Problems remain strictly OPEN.

---

## 1. Executive Summary

Standard numerical PDE solvers (finite element, finite difference, lattice field solvers) often suffer severe performance degradation when solving coupled systems containing near-zero mode leakage channels:
* Acoustic zero-modes in building structural dynamics (HBIM)
* Rigid body modes in structural elasticity
* Low-frequency thermal drift in multiscale transport
* Gauge zero-modes and abelian photon channels in gauge field theory

When solved monolithically:
$$
\begin{pmatrix} A & B^T \\ B & D \end{pmatrix} \begin{pmatrix} x_A \\ x_D \end{pmatrix} = \begin{pmatrix} b_A \\ b_D \end{pmatrix}
$$
the near-zero eigenvalues of block $A$ inflate the global condition number to $\kappa(M) > 10^6$, causing iterative Krylov solvers (GMRES, CG) to stall or diverge.

The **Rosetta Subtractive Quotient Solver** eliminates this bottleneck by taring out the leakage channel before solving the physical sector:
1. **Tare the physical load vector:**
   $$
   b_D^{\text{tared}} = b_D - B A^{-1} b_A
   $$
2. **Solve the well-conditioned physical Schur complement system:**
   $$
   S = D - B A^{-1} B^T, \quad S x_D = b_D^{\text{tared}}
   $$
3. **Back-substitute into the leakage sector:**
   $$
   x_A = A^{-1} (b_A - B^T x_D)
   $$

---

## 2. Benchmark Verification

On a coupled 100-dimensional ill-conditioned benchmark system ($50 \times 50$ leakage block with eigenvalues down to $10^{-5}$ coupled to a $50 \times 50$ physical sector):
* Monolithic matrix condition number: $\kappa(M) = 1.01 \times 10^6$
* Schur complement condition number: $\kappa(S) = 5.16$
* **Condition number reduction ratio: $196,074\times$**
* Subtractive solve residual: $\|M x - b\| = 1.03 \times 10^{-12}$
* Benchmark receipt status: **PASS** (`rosetta_subtractive_solver_receipt.json`)

---

## 3. Quick Start

### Running Unit Tests
```bash
python -m unittest engineering_spinoffs/subtractive_solver/test_subtractive_solver.py
```

### Running Benchmark
```bash
python engineering_spinoffs/subtractive_solver/rosetta_subtractive_solver.py
```

### Python API Usage
```python
import numpy as np
from rosetta_subtractive_solver import SubtractiveQuotientSolver

# Define blocks A (leakage), B (coupling), D (physical)
solver = SubtractiveQuotientSolver(A, B, D)

# Solve in decoupled stages
x_A, x_D = solver.solve(b_A, b_D)
```

---

## 4. Verification and Epistemic Integrity

This toolkit implements verified finite-dimensional linear algebra algorithms. In accordance with strict epistemic integrity protocols:
* `status: verified-finite`
* `open_horizon_lock: STRICTLY OPEN`
* All four Clay Millennium Problems (Yang-Mills Mass Gap, Navier-Stokes Smoothness, Riemann Hypothesis, Hodge Conjecture) remain strictly open.
