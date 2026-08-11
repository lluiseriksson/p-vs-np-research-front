# GATE-004BP — eliminate a base-only cycle source

**Label: EXPLORATORY**

Assume a surviving LEMMA-166 no-cut parent whose selected core source has
`a=0`. Equality then gives `p=0` in the exact higher-rank cases; rank one may
place its single slack NOT upstream or downstream.

## Falsifiable theorem

Some neutral implication-clause restriction leaves a circuit for `J_{j-1}`
with `N+r<=j+1`.

Unlike LEMMA-168, a base-only one-bit source need not force
`H=B(X)R(Y)`: its two codes may select two distinct nonzero base cofactors.
LEMMA-169/170 and GATE-004BP-NONTRIVIAL-SOURCE prove that a minimum-arity
counterexample has a primary base-input source. The next attack must either:

1. exploit the two base cofactors selected by that primary input; or
2. show that a tail clause becomes private after the primary split.

GATE-004BP-BASE-COUNT-INDUCTION-ONLY records why arity descent itself stops
there. GATE-004BQ is the active boundary theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned two-excess implication circuits with a no-cut core source depending only on base inputs |
| Uniform/non-uniform | Every individual non-uniform base-only-source parent; uniform symmetric tail |
| Circuit size | Parent `N+r=j+2`; target after one neutral tail restriction `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor pairs and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2`, `sigma>=3`, and remaining LEMMA-166 parent with `a=0` |
| Regime | Exact worst-case remaining subgate of GATE-004BN; not a SAT lower bound or terminal result |
