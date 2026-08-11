# GATE-004BR-ZERO-COFACTOR — close a vanishing primary cofactor

**Label: PROVED**

Assume GATE-004BR and suppose one base cofactor of the primary input `x` is
zero. Then some neutral tail restriction has resource at most `j+1`.

## Proof

The other cofactor is a nonzero function `R`, and

`H=e_c(x) AND R`,

where `e_c` is either `x` or `NOT x`.

Fixing `x` to its nonzero code removes the degree-two source and leaves a
circuit for `R W_j` with resource at most

`N+(r-1)=j+1`.

LEMMA-169 gives a circuit for `R W_{j-1}` with resource at most `j`.
Conjoin the literal `e_c(x)`. This adds no cycle and at most one NOT, so the
resulting circuit for `H W_{j-1}` has resource at most `j+1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned two-excess implication circuits with a degree-two primary source and one zero base cofactor |
| Uniform/non-uniform | Every individual non-uniform parent in the stated case; uniform symmetric tail |
| Circuit size | Parent `N+r=j+2`; reconstructed restricted target `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary source fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor factorization and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004BR parent having exactly one nonzero primary cofactor |
| Regime | Exact worst-case subgate of GATE-004BR; two distinct nonzero cofactors remain open; not a SAT lower bound or terminal result |
