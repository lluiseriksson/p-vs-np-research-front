# GATE-004BR — prune a degree-two primary source with cyclic residual

**Label: EXPLORATORY**

Assume the remaining GATE-004BQ case:

- the core source is a primary base input `x`;
- its degree is `d=2`;
- parent rank is `r>=2`;
- fixing `x` leaves rank at most `r-1>=1`; and
- exact two-excess accounting gives `N=j+2-r`.

## Falsifiable theorem

Some neutral tail-clause restriction leaves `N+r<=j+1`.

Each nonzero `x` cofactor has a witness circuit of resource at most `j+1`,
but separate cofactor minima cannot be glued for free. The next attack must
use their common downstream graph: either extend LEMMA-171 to a cyclic
residual with an explicit rank defect, or prove that both outgoing `x` paths
force a shared tail-private resource.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned two-excess implication circuits with a degree-two primary base source and positive residual rank |
| Uniform/non-uniform | Every individual non-uniform remaining parent; uniform symmetric tail |
| Circuit size | Exact parent `N+r=j+2`; target restricted `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary source fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Two Boolean cofactors, common cyclic downstream graph, and cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational `j>K+sigma-2`, `sigma>=3`, and remaining parent with `r>=2,d=2` |
| Regime | Exact worst-case remaining subgate of GATE-004BQ; not a SAT lower bound or terminal result |
