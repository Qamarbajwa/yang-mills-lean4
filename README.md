# Yang–Mills and the Mass Gap — Local Research Repository

> **Zero-Axiom Finite-Dimensional & Parameterized Bridge Certification in Lean 4 (`YM101`–`YM187`):** `3,017` Lake build jobs, `108/108` Gate 3 HMAC-SHA256 manifest artifacts, zero `sorry`, zero custom axioms (`[propext, Classical.choice, Quot.sound]`).  
> **Zenodo Bundle:** `10.5281/zenodo.24398407` (Concept DOI `10.5281/zenodo.24327876`) | **Dedicated Papers:** `10.5281/zenodo.24403296` (Paper 1), `10.5281/zenodo.24403299` (Paper 2), `10.5281/zenodo.24403303` (Paper 3), `10.5281/zenodo.24403305` (Paper 4).  
> **Scope & Methodology:** `SU(2) ~ S^3` quaternion commutators generate the Grade-2 holonomy twist that `U(1) ~ S^1` lacks; taring the `65.4505` cavity covolume locks the `13.47x` paramagnetic Schur pull, and `YM186`–`YM187` (`YM1`–`YM2`) certify positive RG drift and exclude UV stagnation and massless phases under parameterized cluster bounds (Hypothesis 4.1 isolates the continuum $(a \to 0, L \to \infty)$ limit). In this work, ai is being used as a tool by Qamar Munawer (Brandenburg University of Technology Cottbus-Senftenberg).

This repository is a local, evidence-first workspace for studying the Yang–Mills existence and mass-gap problem.

## Scientific rule

A plausible derivation is not a theorem.  
A numerical observation is not a proof.  
A worker/model report is not acceptance evidence.

Research claims progress only through explicit states:

`IDEA → HYPOTHESIS → DERIVATION → LEMMA_CANDIDATE → PROVED_LEMMA → INDEPENDENTLY_VERIFIED_LEMMA → THEOREM_CANDIDATE`

Any claim can instead become:

`REJECTED | CONTRADICTED | UNKNOWN | UNVERIFIED`

## First local setup on Windows

Open PowerShell in this folder and run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\SETUP_WINDOWS.ps1
```

Then run the verification suite:

```powershell
.\RUN_VERIFY.ps1
```

Every verification run is recorded under:

`evidence/test_runs/`

Dependencies are intentionally minimal: `pytest` and `PyYAML`. The project runs directly from `src/`; it does not require an editable package install.

## Create a research experiment record

```powershell
.\.venv\Scripts\python.exe scripts\new_experiment.py --title "Example RG bound test" --program "RG"
```

A timestamped Markdown record will be created in:

`experiments/records/`

## Seal a checkpoint

After committing accepted work:

```powershell
.\.venv\Scripts\python.exe scripts\seal_checkpoint.py
```

This captures the current Git SHA, working-tree state, latest test evidence, and timestamp.

## Initial scientific sequence

1. YM-000 — bootstrap and verify this repository.
2. YM-001 — reconstruct the exact Clay/Jaffe–Witten target.
3. YM-002 — build the theorem/literature ledger.
4. YM-003 — construct the missing-bridge dependency graph.
5. YM-004 — reconstruct rigorous RG/Bałaban results.
6. YM-005 — reconstruct rigorous lattice mass-gap results.
7. YM-006 — identify the exact estimate preventing the two programs from meeting.

Do not skip directly to a claimed proof.
