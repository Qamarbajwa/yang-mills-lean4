-- Illustrative statements only; this file has NOT been checked by Lean here.
namespace MathGov

theorem step1 (n : Nat) : n + 0 = n := by
  simp

theorem step2 (n : Nat) : n = n + 0 := by
  simpa using (step1 n).symm

end MathGov
