# GATE-004BQ — prune a primary base core source

**Label: EXPLORATORY**

Assume a minimum-arity GATE-004BP counterexample. By
GATE-004BP-NONTRIVIAL-SOURCE its selected LEMMA-164 source is a primary base
input `x` with `p=0` and core degree `d>=2`.

## Falsifiable theorem

Some neutral tail-clause restriction leaves `N+r<=j+1`.

The factorization is

`H(x,Y)W_j(T)=F(x,Y,T)`

with two possibly distinct nonzero base cofactors. Replacing `x` by a fresh
input is only a renaming. LEMMA-171 and GATE-004BQ-FORMULA-RESIDUAL prove the
theorem when fixing `x` leaves rank zero, covering rank one and the exceptional
`r=2,d=3` case. GATE-004BR is the sole remainder: `d=2` and positive residual
rank.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned two-excess implication circuits whose selected core source is a primary base input |
| Uniform/non-uniform | Every minimum-arity non-uniform candidate; uniform symmetric tail |
| Circuit size | Parent `N+r=j+2`; target restricted `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary-input fanout at least two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Two Boolean base cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2`, `sigma>=3`, and minimum-arity GATE-004BP candidate |
| Regime | Exact worst-case remaining subgate of GATE-004BP; not a SAT lower bound or terminal result |
