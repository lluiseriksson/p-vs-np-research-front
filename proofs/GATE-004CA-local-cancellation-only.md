# GATE-004CA-LOCAL-CANCELLATION-ONLY — local mask/cycle data force a saving

**Label: NO-GO**

## Attempt

Infer a deletion or same-size simplification solely from the local alternatives
in LEMMA-181.

## Failure

Both alternatives occur in constant-size Boolean gadgets without a generic
local saving.

- One-sided mask: with
  `n=NOT(v OR (u AND w))`, `q=NOT v AND w`, the gate `n OR q` is `NOT v`
  for both values of `u` although `n` has distinct ordered cofactors.
- Two-sided cancellation: `p=u AND v`, `q=NOT u AND v`, and
  `d=p OR q` give `d=v`. Both inputs change with `u` and their reconvergence
  creates a cycle in the undirected circuit graph.

These gadgets are deliberately not claimed minimum or plateau realizations.
They prove that mask containment, two changing inputs, and a local cycle do
not alone yield the required exchange. Minimum-size equality and survival of
the entire resource set are essential additional premises.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit constant-size AND/OR/NOT cancellation gadgets and local cofactor topology |
| Uniform/non-uniform | Finite non-uniform identities; no minimum-parent realization claim |
| Circuit size | Constant-size witnesses; no global size or resource assertion |
| Circuit depth | Constant in the witnesses; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean identities and one undirected cycle coordinate |
| Asymptotic quantifiers | Every choice of independent Boolean variables in the two displayed identities |
| Regime | Structural no-go for local-cancellation-only reasoning; not a plateau counterexample, SAT lower bound, or terminal result |
