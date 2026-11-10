# Suggested record contracts (schema proposal, host not implemented)

Every object is immutable versioned data, not an extra project authority. Actual producer must authenticate actor, tool and source at capture. Never claim the JSON structure alone is authoritative.

## USER_INTENT record
```json
{"id":"UTT-0001","raw_bytes_ref":"archive://...","raw_sha256":"<64hex>","subject_id":"SUBJ-001","actor_authenticated_ref":null,"timestamp_attested_ref":null,"candidate_interpretations":[],"owner_approved_formal_target_ref":null}
```

## PATHWAY record
```json
{"pathway_id":"PATH-1","target_id":"THM-1","status":"EXPLORATORY","method":"analytic","assumptions":[],"preconditions":[],"isolated_branch":true,"evidence_refs":[],"rejected_link_refs":[]}
```

## STEP record
```json
{"step_id":"S001","pathway_id":"PATH-1","goal_before_ref":"...","goal_after_ref":"...","premise_refs":[],"domain":"...","assumption_refs":[],"side_condition_refs":[],"open_goal_refs":[],"transform":"...","formal_source_sha256":null,"lemma_dependencies":[],"candidate_proof_receipt_ref":null,"state":"PROPOSED"}
```

## TASK_CONTEXT_CAPSULE record
```json
{"task_id":"T001","source_snapshot_ref":"...","owner_intent_digest":"...","formal_target_digest":"...","required_source_refs":[],"negative_history_refs":[],"verified_premise_refs":[],"open_obligation_refs":[],"branch_acl_ref":null,"worker_capability_evidence_ref":null,"tool_grant_ref":null,"token_budget":null,"lease_ref":null,"source_read_receipt_ref":null,"recall_check_ref":null,"dispatch":"BLOCKED"}
```

## LEAN_RECEIPT record
```json
{"target_theorem_id":"THM-1","source_tree_sha256":"...","challenge_sha256":"...","toolchain_digest":"...","lake_manifest_sha256":"...","sandbox_attestation_ref":null,"cmd":[],"exit_code":null,"stdout_bytes_ref":null,"stderr_bytes_ref":null,"axiom_list":null,"comparator_ref":null,"host_verifier_identity_ref":null,"result":"NOT_RUN"}
```

## REVIEW + ACCEPTANCE (two separate objects)
```json
{"candidate_sha256":"...","reviewer_authentication_ref":null,"read_only_replay_ref":null,"formal_statement_semantic_audit_ref":null,"status":"NOT_PERFORMED"}
```
```json
{"candidate_sha256":"...","qualified_acceptor_authentication_ref":null,"distinct_from_worker_and_reviewer":null,"owner_authorization_ref":null,"decision":"NOT_ACCEPTED"}
```

## CHANGE_RECORD
```json
{"baseline_snapshot_sha256":"...","post_change_snapshot_sha256":"...","host_calculated_diff_ref":null,"invalidated_steps":[],"invalidated_claims":[],"invalidated_diagrams":[],"invalidated_context_capsules":[],"reenforced_approvals":[],"status":"NOT_APPLIED"}
```

## CLAIM/REPORT record
```json
{"claim_id":"C001","exact_mathematical_statement":"...","quantifiers":"...","domain":"...","assumption_refs":[],"evidence_refs":[],"counterevidence_refs":[],"status":"UNKNOWN","independent_approval_ref":null,"limitations":[],"verified_scope_only":true}
```

All placeholders must be replaced by authenticated source artifacts before any stronger status is permitted. Model-produced data is never proof that an actor, tool invocation or host really exists.
