# EVALUATOR OWNERSHIP POLICY (v2.9.3)

## Separation of Evaluator and Evaluated
- Evaluator scripts (`tests/`, `scripts/check_repo.py`, `scripts/seal_checkpoint.py`, `scripts/capture_verifier_output.py`) are protected assets.
- A worker implementing a scientific task may not weaken test assertions to achieve artificial test passes.
- All test modifications must be accompanied by explicit justifications and verified under regression tests.
