# LEMMA-140 — exact unrestricted circuit size of `W_m`

**Label: PROVED**

For every fixed `p>=1` and every `m>=1`, the unrestricted De Morgan circuit
size of

`W_m = AND_i (NOT u_i OR v_{i,1} OR ... OR v_{i,p})`

is exactly

`C(W_m)=(p+2)m-1`.

## Lower bound

Let a pruned circuit have `B` binary gates, `q` NOT gates, and cycle rank
`r`. Essential-input connectivity gives the exact identity

`B=(p+1)m-1+r`.

If `r=0`, LEMMA-139 gives `q>=m`, hence

`B+q >= (p+2)m-1`.

If `r>=1`, LEMMA-139 gives `q>=m-r+1`, hence the slightly stronger

`B+q >= (p+2)m`.

## Upper bound

The displayed read-once circuit uses one NOT on each `u_i`, `p` binary OR
gates per clause, and `m-1` binary AND gates, for `(p+2)m-1` gates. This
matches the lower bound.

The theorem concerns `W_m` alone. It does not prove that adjoining these
clauses to an arbitrary base circuit costs additively, nor that their semantic
quotient classes survive minimization.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted pruned De Morgan circuits for a disjoint fixed-sign clause product |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform explicit function family |
| Circuit size | Exact `(p+2)m-1`; for `p=4`, exact `6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2` and Boolean cofactor partitions |
| Asymptotic quantifiers | Every fixed `p>=1` and every `m>=1` |
| Regime | Exact worst-case standalone size; not a direct sum, SAT lower bound, or terminal result |
