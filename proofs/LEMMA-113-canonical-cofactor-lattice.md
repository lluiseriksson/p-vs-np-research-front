# LEMMA-113 — the canonical cofactors form the full conjunction lattice

**Label: PROVED**

Retain the canonical positive assignments `alpha_S` and residuals

`R_S = W_m | alpha_S = AND_{i in S} NOT u_i`

from LEMMA-112. For every `S subseteq [m]` and `i notin S`,

`R_{S union {i}} = R_S AND NOT u_i`,

and the two residual functions are distinct. Hence the output cofactor profile
changes on every one of the `m*2^(m-1)` edges of the subset cube and assumes
all `2^m` distinct residual functions.

Nevertheless, this entire profile belongs to the single output node of every
parent circuit for `W_m`: restricting that node by `alpha_S` gives `R_S` for
each `S`. Therefore neither the number of distinct output cofactors nor the
number of cube edges on which the output cofactor changes is, by itself, a
lower bound on the number of parent gates.

## Proof

The displayed transition follows immediately by separating the new factor
`NOT u_i` from the conjunction. To witness distinctness, set `u_i=1` and set
every `u_j=0` for `j in S`; then `R_S=1` and
`R_{S union {i}}=0`. There is one such transition for each ordered pair
`(S,i)` with `i notin S`, and their count is
`sum_S (m-|S|)=m*2^(m-1)`.

For any circuit computing `W_m`, its output node computes `W_m`. Under every
canonical restriction it therefore computes the corresponding `R_S`.
Counting these functions or transitions repeatedly at that same node cannot
produce distinct gate witnesses without an additional internal-survival or
first-divergence theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Canonical positive-variable restrictions of unrestricted AND/OR/NOT circuits for the fixed-sign clause product |
| Uniform/non-uniform | Uniform restriction cube; every individual non-uniform parent circuit |
| Circuit size | No size lower bound; `2^m` output cofactors and `m*2^(m-1)` changing cube edges can occur at one output node |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions and the subset lattice only |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, every `S subseteq [m]`, and every `i notin S` |
| Regime | Exact worst-case cofactor-profile theorem and counting limitation; not a parent lower bound, SAT lower bound, or terminal result |
