# Cycle 181 — joint cofactor-saving audit

**Label: PROVED**

LEMMA-215 proves the exact fan-in arity bound: an output depending essentially
on `N` source signals needs at least `N-1` binary merge gates. Applied to the
NG-157 selected vector, its second output depends on `n+2` available sources,
while an `n+1`-gate shared construction exists. The minimum joint cofactor
circuit size is therefore exactly `n+1`.

GATE-004DH-JOINT-SAVING-ONLY records the consequence: the marked region has
size `n+2`, so its exact joint saving is one, whereas private deficit is
`n-2`. Local joint semantic cost alone cannot pay the deficit.

## Classification

- LEMMA-215: `PROVED`
- GATE-004DH-JOINT-SAVING-ONLY: `NO-GO`
- GATE-004DI: `EXPLORATORY`

GATE-004DI now requires a globally deduplicated resource charge derived from
minimum endpoint structure and exact satisfying-pruning budgets. No SAT lower
bound or terminal implication is claimed.

## Review boundary

`verification/joint_cofactor_saving_audit.py` checks the selected vector and
the size arithmetic for `n=3,...,8`. The general essential-input lower bound
and its exact application are human proofs. Fable and `fable-bridge` were not
invoked. No independent mathematical certification or formal verification is
claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Fan-in-two Boolean DAG arity theorem plus an explicit uniform masked-region family |
| Uniform/non-uniform | Every finite DAG for the theorem; one uniform family for every `n>=3`, each member non-uniform |
| Circuit size | Exact selected joint size `n+1`, region `n+2`, saving one, private deficit `n-2` |
| Circuit depth | Unrestricted theorem; family depth linear in `n` |
| Fan-in | At most two; AND/OR two and NOT one in the application; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Dependency-component merging and exact Boolean cofactors |
| Asymptotic quantifiers | Every finite essential-source set; every `n>=3` and every selected-vector assignment |
| Regime | Exact arity theorem plus local-joint-saving no-go; not a SAT lower bound or terminal result |
