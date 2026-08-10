# LEMMA-115 — every negative clause input has a sensitive odd-NOT path

**Label: PROVED**

For each clause index `i`, assign the positive variables by `alpha_{ {i} }`,
set every `u_j=0` for `j!=i`, and compare the two full inputs `x_i^0,x_i^1`
with `u_i=0,1`. In every AND/OR/NOT circuit for `W_m`, the nodes whose values
differ between these inputs contain a directed path from `u_i` to the output
with an odd number of NOT gates.

## Proof

LEMMA-112 gives `W_m|alpha_{ {i} }=NOT u_i`, so the output changes from one
to zero while the sole changing primary input `u_i` changes from zero to one.

Trace backward from the changing output. At a changing NOT gate its unique
predecessor changes in the opposite direction. At a changing AND or OR gate,
monotonicity guarantees at least one changing predecessor in the same
direction as the output: a `0->1` output change requires a `0->1` input
change, and a `1->0` output change requires a `1->0` input change. Choose such
a predecessor. The trace cannot end at a fixed primary input, so it ends at
`u_i`.

The change direction flips exactly at NOT gates. It starts `0->1` at `u_i`
and ends `1->0` at the output, hence the chosen path contains an odd number of
NOT gates.

## Model card

| Field | Value |
|---|---|
| Computational model | Assignment-sensitive subgraphs of unrestricted AND/OR/NOT circuits for the fixed-sign clause product |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform witness pair per clause index |
| Circuit size | No size lower bound; at least one sensitive odd-NOT path per negative essential input |
| Circuit depth | Unrestricted finite DAG |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean value changes and path parity only |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, every clause index, and every circuit computing `W_m` |
| Regime | Exact worst-case sensitivity-path theorem; not an additive resource charge, SAT lower bound, or terminal result |
