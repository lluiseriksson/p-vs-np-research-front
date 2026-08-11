# LEMMA-173 — a surviving NOT can change its tail signature

**Label: PROVED**

For distinct tail variables `u_i,u_k` and a primary bit `x`, the gate

`g=NOT(u_i OR (x AND u_k))`

is nonconstant under both primary cofactors, but

`g|_{x=0}=NOT u_i`

and

`g|_{x=1}=NOT(u_i OR u_k)`.

Thus survival of the same physical NOT gate under both codes does not imply a
common clause-private signature. Neutralizing clause `i` at `u_i=0` makes the
first cofactor constant one but leaves `NOT u_k` in the second.

## Proof

Direct substitution gives the displayed identities. The construction uses
no `NOT x`; the only NOT is the displayed outer gate and it remains
nonconstant in both cofactors before clause neutralization.

## Model card

| Field | Value |
|---|---|
| Computational model | One explicit non-uniform AND/OR/NOT gate gadget under a primary-input cofactor |
| Uniform/non-uniform | Explicit non-uniform gadget; no minimum-parent realization claim |
| Circuit size | One outer NOT, one OR, and one AND; no global resource assertion |
| Circuit depth | Three in the displayed basis |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean substitution only |
| Asymptotic quantifiers | Every pair of distinct tail variables and both values of `x` |
| Regime | Exact semantic witness; not a GATE-004BS counterexample, SAT lower bound, or terminal result |
