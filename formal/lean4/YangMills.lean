/-
Copyright (c) 2026 Yang-Mills and the Mass Gap Project. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Antigravity Primary Worker, Human Constitutional Owner
Task: YM-LEAN-001 (Lean 4 Formalization Scoping)
-/

import YangMills.ClaySpecification
import YangMills.WightmanAxioms
import YangMills.OsterwalderSchraderAxioms
import YangMills.MissingBridgeDAG

/-!
# Yang-Mills and the Mass Gap Formal Library

This root module aggregates the formal mathematical components of the Yang-Mills problem:
1. `ClaySpecification`: The official Millennium Problem statement (Jaffe & Witten 2000).
2. `WightmanAxioms`: Relativistic quantum field theory axioms W0–W5 on $\mathbb{R}^{1,3}$.
3. `OsterwalderSchraderAxioms`: Euclidean axioms OS0–OS4 and the OS reconstruction theorem.
4. `MissingBridgeDAG`: Machine-checkable formalization of the YM-003 proof-dependency DAG and acyclicity theorem.
-/
