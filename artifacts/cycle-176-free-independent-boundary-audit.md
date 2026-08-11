# Cycle 176 — free independent boundary audit

**Label: PROVED**

LEMMA-210 gives an exact physical exchange certificate. If the unchanged
function at a counted boundary `b` is already an independent wire, deleting
`b` saves one gate. If it is one AND, OR, or NOT gate over existing globally
`u`-independent nondescendant signals, retargeting the physical gate `b`
preserves every gate function and size while removing exactly that direct
`h`-boundary from `R_0`.

GATE-004DC-COMPARABILITY-BASIS-ONE-ONLY supplies the matching structural
limit. Its five-input DAG has a comparable defect confined to `00/10` and a
globally independent boundary output, but the exact independent predecessor
pool is only `x,y,z,t,NOT t`; the output `xy OR z` is outside basis radius one
of that pool. The witness is explicitly nonminimal and therefore refutes only
the semantics-only inference.

## Classification

- LEMMA-210: `PROVED`
- GATE-004DC-COMPARABILITY-BASIS-ONE-ONLY: `NO-GO`
- GATE-004DD: `EXPLORATORY`

The active gate must now use minimum joint cost or exact pruning to pay for a
missing independent factor; comparability alone is exhausted.

## Review boundary

`verification/free_local_realization_audit.py` checks 32 assignments and the
complete basis-radius-one pool. The human DAG proof carries the labels. Fable
and `fable-bridge` are disabled and were not invoked. No independent
mathematical certification or formal verification is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined unrestricted AND/OR/NOT endpoint plus one explicit finite nonminimal witness |
| Uniform/non-uniform | Every endpoint with a supplied basis-one certificate for LEMMA-210; one uniform five-input witness for the no-go |
| Circuit size | Wire certificate saves one gate; one-gate certificate preserves size; witness has ten gates and makes no minimum claim |
| Circuit depth | Unrestricted target; constant witness depth |
| Fan-in | AND/OR two; NOT one; boundary and witness fanouts audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities, basis distance, and physical DAG rewiring |
| Asymptotic quantifiers | Every qualifying endpoint certificate; all 32 witness assignments and all radius-one candidates over five independent predecessors |
| Regime | Exact sufficient exchange plus semantics-only no-go; not a SAT lower bound or terminal result |
