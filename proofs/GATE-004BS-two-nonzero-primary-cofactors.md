# GATE-004BS — exploit two nonzero primary cofactors on one cyclic graph

**Label: EXPLORATORY**

Assume the remaining GATE-004BR case. The primary base input `x` has two
distinct nonzero cofactors `H_0,H_1`. By LEMMA-172, every satisfying
restriction of either cofactor preserves all `N=j+2-r` NOT gates; for
`r>=3` it also preserves residual rank `r-1` exactly.

## Falsifiable theorem

Some neutral tail-clause restriction in the common parent graph leaves
`N+r<=j+1`.

Separate minimum circuits for `H_0 W_{j-1}` and `H_1 W_{j-1}` do not suffice,
by GATE-004BR-COFACTOR-MINIMA-ONLY. LEMMA-173 further shows that common gate
survival does not preserve clause signature. GATE-004BT is the next sufficient
brick: find a NOT with the same neutral constant in both codes, or a common
cycle coordinate lost in both.

## Model card

| Field | Value |
|---|---|
| Computational model | One common pruned two-excess circuit with a degree-two primary source and two distinct nonzero base cofactors |
| Uniform/non-uniform | Every individual non-uniform remaining parent; uniform symmetric tail |
| Circuit size | Exact parent `N+r=j+2`; target restricted `N+r<=j+1`; cofactor resources rigid by LEMMA-172 |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary source fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Common-graph Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational `j>K+sigma-2`, `sigma>=3`, and GATE-004BR parent with two nonzero cofactors |
| Regime | Exact worst-case remaining subgate of GATE-004BR; not a SAT lower bound or terminal result |
