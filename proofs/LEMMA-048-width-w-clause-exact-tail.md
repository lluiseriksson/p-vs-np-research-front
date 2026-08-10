# LEMMA-048 — disjoint width-w clauses have exact additive circuit cost

**Label: PROVED**

## Statement

Let `H(x)` be a nonconstant total Boolean function with exact unrestricted
AND/OR/NOT circuit size `K`. For `1<=i<=m`, let

`v_{i,1},...,v_{i,w}`

be fresh raw inputs, with all `mw` inputs distinct, and put

`Q_i=OR_{k=1}^w v_{i,k}`,

`F=H AND Q_1 AND ... AND Q_m`.

Then

`C(F)=K+wm`.

If two restrictions of `x` give distinct nonconstant residuals `H_0,H_1`,
the displayed minimum circuit using an OR chain for each clause and an AND
chain above `H` has at least `(w+1)m` active semantic joint-quotient classes.
Its signed loss is at most

`(K+wm)-(w+1)m=K-m`.

## Exact-size proof

The displayed circuit uses `(w-1)m` OR gates and `m` AND gates above a
minimum circuit for `H`, proving the upper bound `K+wm`.

For the lower bound, successively restrict

`v_{i,2}=...=v_{i,w}=0`

for every clause. Before each restriction, the selected variable is essential:
choose `H=1`, set every other clause true, and set the other inputs of the
current clause false. The current function is not a raw input. The earliest-
dependent-gate restriction argument from LEMMA-046 therefore removes at least
one gate for each of the `(w-1)m` restrictions. The final residual is

`H AND v_{1,1} AND ... AND v_{m,1}`,

which has exact size `K+m` by LEMMA-037. Hence

`C(F)>=K+m+(w-1)m=K+wm`.

## Quotient proof

For each clause, the displayed OR chain has `w-1` non-input prefix functions.
Across clauses and prefix lengths these `(w-1)m` functions are distinct by
their essential-input sets. Under row `e`, the `j`th AND-tail gate computes

`H_e AND Q_1 AND ... AND Q_j`.

The `2m` row-tail functions are pairwise distinct by clause support and by
`H_0!=H_1`; they also depend on the base suffix variables and cannot collide
with an OR prefix. Thus the joint quotient contains at least

`(w-1)m+2m=(w+1)m`

classes. QED.

## ENC-022 application

Let `P>=84` be divisible by twelve and put `m=P/3`. Partition the outer
coordinates into triples

`(i,i+m,i+2m)`, `0<=i<m`.

Every ENC-022 context has zeros confined to at most two inserted blocks, each
of length at most 28. Coordinates in a triple are separated by `m>=28`, so
one block cannot contain two of them. Therefore the width-three clause on
each triple is one on every ENC-022 context.

Conjoining all `m` clauses to the common-inner-length DNF core base `H(r,u)`
gives exact parent size `K+3m=K+P`, quotient size at least `4m=4P/3`, and
diagonal loss at most `K-P/3`. For sufficiently small fixed context exponent
`c`, the parser base has `K=o(P)` and the loss is negative. This falsifies
ENC-022-only forcing, not full GATE-004U.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits, disjoint fresh width-w positive clauses, restrictions, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform base and minimum circuit; uniform clause extension and outer-coordinate triple partition |
| Circuit size | Exact `K+wm`; quotient at least `(w+1)m`; signed loss at most `K-m` |
| Circuit depth | Base unrestricted; displayed OR and AND chains unrestricted in depth |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite nonconstant `H`, every `m,w>=1`, and every pair of distinct nonconstant designated row residuals; ENC-022 application at every twelve-divisible `P>=84` |
| Regime | Worst-case exact total-function computation; syntax-family method obstruction, not a SAT circuit lower bound |
