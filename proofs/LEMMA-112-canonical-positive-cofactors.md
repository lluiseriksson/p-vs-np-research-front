# LEMMA-112 — every canonical positive cofactor is exactly a negative conjunction

**Label: PROVED**

For

`W_m = AND_{i=1}^m (NOT u_i OR v_{i,1} OR ... OR v_{i,p})`,

fix any subset `S` of `[m]`. Define the full positive-variable assignment
`alpha_S` by setting every `v_{i,j}=0` when `i in S`, and setting
`v_{i,1}=1` (with the remaining positives zero) when `i notin S`. Then

`W_m | alpha_S = AND_{i in S} NOT u_i`.

Its exact unrestricted AND/OR/NOT circuit size is `|S|` (with size zero for
the empty constant-one residual). Consequently the `2^m` canonical residuals
are distinct and

`2^{-m} sum_{S subseteq [m]} C(W_m | alpha_S) = m/2`,

while their maximum complexity is `m`.

## Residual identity

If `i in S`, all positive literals in clause `i` are zero, so the clause
reduces to `NOT u_i`. If `i notin S`, its selected positive literal is one,
so the clause is constant one. Conjoining gives the displayed residual.

## Exact residual size

For nonempty `S`, an OR chain on the `|S|` variables followed by one NOT gate
computes the residual with `|S|` gates. Conversely the residual depends on
all `|S|` inputs, so binary connectivity requires at least `|S|-1` binary
gates. Its decrease parameter is one, so Markov requires at least one NOT.
The lower and upper bounds match.

Distinct subsets have distinct essential-input sets, proving residual
distinctness. The average follows from
`sum_S |S|=m*2^{m-1}`.

## Scope

Every individual canonical cofactor is much easier than the `6m-1` displayed
parent. The result supplies an exact multi-cofactor table, not an additive
charge across restrictions; the same parent gates may contribute to many
cofactors.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact positive-variable restrictions of an unrestricted AND/OR/NOT read-once clause product |
| Uniform/non-uniform | Uniform canonical assignments; exact non-uniform residual circuit size |
| Circuit size | Residual size exactly `|S|`; average `m/2`; maximum `m` |
| Circuit depth | Unrestricted; displayed OR chain may be linear depth |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions and subset incidence only |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, and every subset `S` of `[m]` |
| Regime | Exact worst-case cofactor theorem; not a parent direct sum, quotient theorem, SAT lower bound, or terminal result |
