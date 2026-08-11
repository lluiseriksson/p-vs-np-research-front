# GATE-004BQ-FORMULA-RESIDUAL — close primary sources whose fixing is acyclic

**Label: PROVED**

In the operational GATE-004BQ descent range, suppose the primary source has
degree `d` and deleting it leaves rank zero. Then some neutral tail-clause
restriction leaves `N+r<=j+1`.

## Operational margin

The local descent is needed only for `j>K+sigma-2`, so
`j>=K+sigma-1`. Since the nonconstant base has at least one essential input
and `sigma=K-h+1>=3`, we have `K>=h+2>=3` and hence `j>=5`.

LEMMA-166 leaves two acyclic-residual primary cases:

1. `r=1,d=2`, with `N=j+1`; or
2. `r=2,d=3`, with `N=j`.

Choose a value of the primary base input whose base cofactor is nonzero.
LEMMA-171 gives at least `j-d` parent-private tail NOTs. This is positive in
both cases because `j>=5` and `d<=3`. Neutralizing one corresponding clause
deletes a NOT and cannot increase rank. Starting from `N+r=j+2`, the
restricted resource is at most `j+1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned two-excess implication circuits with a primary base source and acyclic fixed-source residual |
| Uniform/non-uniform | Every individual non-uniform operational parent; uniform symmetric tail |
| Circuit size | Parent `N+r=j+2`; restricted target `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary source degree two or three |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Formula external-leaf defects and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational `j>K+sigma-2`, `sigma>=3`, and primary-source parent with zero residual rank |
| Regime | Exact worst-case subgate of GATE-004BQ; cyclic degree-two residuals remain open; not a SAT lower bound or terminal result |
