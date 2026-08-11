# LEMMA-145 — each canonical row lower-bounds the diagonal quotient

**Label: PROVED**

Let `C` be any circuit and let two base-row restrictions produce residual
functions `F_0,F_1`. For row `e`, let `A_e` be the set of distinct active
nonconstant semantic functions computed by restricted gates, and let

`Q(C)=|A_0 union A_1|`

be the two-row diagonal quotient size. Then

`Q(C)>=max(C(F_0),C(F_1))`.

## Proof

Under row `e`, remove constant and inactive gates. Process the remaining DAG
in topological order and keep only the earliest gate computing each residual
Boolean function, redirecting every later duplicate to that earlier gate.
This creates no directed cycle. A class equal to a raw input is redirected to
that input. The resulting circuit still computes `F_e` and has at most
`|A_e|` gates. Hence

`|A_e|>=C(F_e)`.

Since `Q(C)>=|A_e|` for both rows, the theorem follows.

For the canonical GATE-004AE rows, `F_e=H_e AND W_m` with `H_e` nonconstant.
If `h_e>=1` is its number of essential base-suffix inputs, LEMMA-144 gives

`C(F_e)>=h_e+6m-1>=6m`.

Thus every parent circuit has diagonal quotient size at least `6m`. This is
one linear `m` below GATE-004AU's `7m-o(m)` target.

## Model card

| Field | Value |
|---|---|
| Computational model | Arbitrary circuits under two fixed row restrictions and semantic merging of residual gates |
| Uniform/non-uniform | Every individual non-uniform parent circuit; uniform designated canonical rows in the application |
| Circuit size | Quotient lower `max(C(F_0),C(F_1))`; canonical consequence at least `6m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean semantic equivalence under restriction only |
| Asymptotic quantifiers | Every finite parent circuit and every pair of row restrictions; every sufficiently large canonical instance in the application |
| Regime | Exact worst-case quotient baseline; not the required cross-row surplus, a SAT lower bound, or a terminal result |
