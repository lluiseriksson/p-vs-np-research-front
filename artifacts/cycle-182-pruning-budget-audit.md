# Cycle 182 — satisfying-pruning budget audit

**Label: PROVED**

LEMMA-216 records the exact global cap: three physical loss sets of size two
have a deduplicated union of at most six, with equality only when pairwise
disjoint. Overlap and prior carrier charges reduce the usable residual budget.

GATE-004DI-PRUNING-BUDGET-ONLY records the consequence. Exact satisfying
losses cannot pay an arbitrary `D_b` unless minimum endpoint structure first
bounds the deficit by the uncharged union. The unbounded NG-158 family is only
a nonminimal semantic diagnostic, not an endpoint counterexample.

## Classification

- LEMMA-216: `PROVED`
- GATE-004DI-PRUNING-BUDGET-ONLY: `NO-GO`
- GATE-004DJ: `EXPLORATORY`

GATE-004DJ asks for the missing endpoint deficit bound or distinct external
resources. No SAT lower bound or terminal implication is claimed.

## Review boundary

`verification/pruning_loss_union_audit.py` enumerates all 3,375 ordered triples
of two-subsets of a six-element universe. The general set proof and endpoint
interpretation are human arguments. Fable was not invoked; no independent
mathematical certification or formal verification is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact-plateau unrestricted AND/OR/NOT physical loss sets plus one diagnostic family |
| Uniform/non-uniform | Every finite endpoint loss triple; every diagnostic `n>=3` |
| Circuit size | Three exact losses of two give union at most six; diagnostic deficit `n-2` |
| Circuit depth | Unrestricted endpoint; diagnostic depth linear in `n` |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set union and exact Boolean diagnostic identities |
| Asymptotic quantifiers | Every physical two-set triple and every diagnostic family member |
| Regime | Exact resource cap plus pruning-only no-go; not a SAT lower bound or terminal result |
