# LEMMA-046 — paired fresh clauses have exact additive circuit cost

**Label: PROVED**

## Statement

Let `H(x)` be a nonconstant total Boolean function of exact unrestricted
AND/OR/NOT circuit size `K`. Let

`a_1,b_1,...,a_m,b_m`

be fresh raw inputs, and define

`F(x,a,b)=H(x) AND product_{i=1}^m (a_i OR b_i)`,

where `product` denotes Boolean conjunction. Then

`C(F)=K+2m`.

Moreover, suppose two restrictions of some coordinates of `x` give distinct
nonconstant residuals `H_0(u)` and `H_1(u)`. In the displayed minimum circuit
consisting of a minimum circuit for `H`, the `m` clause gates, and a chain of
`m` AND gates, the semantic joint quotient under those restrictions contains
at least `3m` distinct active tail functions. Its signed loss is therefore at
most

`(K+2m)-3m=K-m`.

## Exact-size proof

The displayed construction gives `C(F)<=K+2m`.

For the reverse inequality, use the following elementary restriction fact.
If a non-input Boolean function depends essentially on a raw variable `z`,
then fixing `z` to either value turns any circuit for the function into a
circuit for the restricted function with at least one gate removed. Indeed,
choose the earliest gate in the output cone whose semantic function depends
on `z`. It directly consumes `z`; after the restriction, a NOT gate is
constant and an AND or OR gate is either constant or its other input. Thus
semantic normalization deletes that gate.

Restrict `b_1=0`, then `b_2=0`, and so on. Before each restriction the current
function depends essentially on the selected `b_i`: choose an input with
`H=1`, set `a_i=0`, and satisfy every other clause. The current function is
not a raw input. Each restriction therefore lowers circuit complexity by at
least one. After all `m` restrictions, the residual is

`H(x) AND a_1 AND ... AND a_m`,

whose exact complexity is `K+m` by LEMMA-037. Consequently

`C(F)>=K+m+m=K+2m`,

and equality follows.

## Joint-quotient proof

Write `c_i=a_i OR b_i` and let

`T_{e,j}=H_e(u) AND c_1 AND ... AND c_j`

for `e in {0,1}` and `1<=j<=m`. The `m` clause functions `c_i` are pairwise
distinct because they have disjoint essential-input sets. The `2m` functions
`T_{e,j}` are pairwise distinct: changing `j` changes the essential clause
inputs, while setting every clause input to one distinguishes the two rows by
`H_0!=H_1`. Every `T_{e,j}` also depends on `u`, because `H_e` is
nonconstant, so it cannot equal a clause function. All `3m` functions are
active quotient classes. The loss bound follows from the exact parent size.
QED.

## ENC-020 application

Let `P>=32` be divisible by four and put `m=P/2`. Pair outer coordinates

`a_i=z_i` and `b_i=z_{i+m}` for `0<=i<m`.

Every non-all-one ENC-020 context has, by its construction, all its zero bits
inside one inserted block whose length is at most 16. Paired coordinates are
at distance `m>=16`, so they cannot both be zero. Hence every clause, and
therefore their conjunction, is one on every ENC-020 context despite
coordinate density.

After first using ENC-010 to put compact DNF cores at one common inner length,
take a polynomial-size total base `H(r,u)` that recognizes those cores and
returns their exact conditioned feasibility. It has distinct nonconstant
diagonal residuals. The function

`G(r,z,u)=H(r,u) AND product_i(z_i OR z_{i+m})`

therefore agrees at every ENC-020 placement, has exact size `K+P`, and has
each diagonal loss at most `K-P/2`. For the usual sufficiently small fixed
`c`, the core/parser upper bound is `K=o(P)` and these losses are negative.

This application covers the ENC-020 family only. It need not agree at other
GATE-004U suffix encodings whose zeros can occupy both halves.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits, fresh disjoint two-variable OR clauses, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform base and minimum circuit; uniform fresh-pair extension and explicit half-block coordinate pairing |
| Circuit size | Exact `K+2m`; quotient at least `3m`; signed loss at most `K-m` |
| Circuit depth | Base unrestricted; displayed clause gates have depth one and the AND tail may add `m` layers |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean coordinate and restriction argument only |
| Asymptotic quantifiers | Every finite nonconstant `H` and `m>=1`; ENC-020 application for every four-divisible `P>=32` and sufficiently small fixed `c` |
| Regime | Worst-case exact total-function computation; method obstruction for one neutral-context family, not a SAT circuit lower bound |
