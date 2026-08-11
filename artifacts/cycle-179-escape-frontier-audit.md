# Cycle 179 — escape-frontier audit

**Label: PROVED**

LEMMA-213 exactly characterizes the maximum admissible private reservoir as
the eligible ancestors that cannot reach an escape-frontier vertex. This turns
the physical-budget premise of LEMMA-212 into a deterministic reachability
invariant, but deliberately assigns no cost to a path or frontier edge.

GATE-004DF-ESCAPE-COUNT-ONLY gives the quantitative obstruction. For every
`n>=3`, a `3n+11`-gate single-output witness computes the unchanged boundary
function `(AND_i x_i) OR w`, whose exact formula size is `n`. Its private
reservoir has size one and deficit `n-2`, while the escape frontier has only
three exits, including only one noncarrier live escape. Thus frontier-edge
cardinality cannot fund the deficit.

## Classification

- LEMMA-213: `PROVED`
- GATE-004DF-ESCAPE-COUNT-ONLY: `NO-GO`
- GATE-004DG: `EXPLORATORY`

GATE-004DG replaces edge counting by joint semantic replacement cost across
all live consumers and satisfying prunings. No SAT lower bound or terminal
implication is claimed.

## Review boundary

`verification/private_reservoir_family_audit.py` checks the exact Boolean
identities and consumer-closure fixed point for `n=3,...,8`. The general
algebra, formula leaf lower bound, and reachability theorem are human proofs.
Fable and `fable-bridge` were not invoked. No independent mathematical
certification or formal verification is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite unrestricted AND/OR/NOT DAG theorem plus an explicit uniform single-output family |
| Uniform/non-uniform | Every finite DAG for the theorem; one uniform construction for every `n>=3`, each member non-uniform |
| Circuit size | Family `3n+11`; exact target formula size `n`; private deficit `n-2`; no minimum claim |
| Circuit depth | Unrestricted theorem; family depth linear in `n` |
| Fan-in | AND/OR two; NOT one; arbitrary fanout theorem and three-exit family frontier |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities, formula leaf counting, and directed reachability |
| Asymptotic quantifiers | Every finite eligible ancestor DAG; every `n>=3` and every family assignment |
| Regime | Exact topology theorem plus escape-count no-go; not a SAT lower bound or terminal result |
