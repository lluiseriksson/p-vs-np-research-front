# LEMMA-055 — complement-exposed bases admit an exact negative-literal tail

**Label: PROVED**

## Statement

Let `H(x)` be a nonconstant total Boolean function of exact unrestricted
AND/OR/NOT circuit size `K`. Assume its complement has exact size `K-1`; write

`H=NOT G`, with `C(G)=K-1`.

For fresh raw inputs `z_1,...,z_m`, `m>=1`, put

`F=H AND NOT z_1 AND ... AND NOT z_m`.

Then

`C(F)=K+m`.

If two restrictions of the base inputs give distinct nonconstant residuals
`H_0,H_1`, the displayed minimum circuit has at least `2m+2` active semantic
joint-quotient classes contributed by its OR/NOT tail. Its signed parent-to-
quotient loss is therefore at most

`(K+m)-(2m+2)=K-m-2`.

## Exact-size proof

De Morgan's law gives

`F=NOT(G OR z_1 OR ... OR z_m)`.

A minimum circuit for `G`, followed by `m` binary OR gates and one final NOT,
has `(K-1)+m+1=K+m` gates.

For the lower bound, first observe that for every nonconstant `f` and fresh
input `z`,

`C(f AND NOT z)>=C(f)+1`.

Indeed, take any circuit for `f AND NOT z` and choose a topologically earliest
gate depending on `z`. No earlier gate depends on `z`, so that gate directly
uses raw input `z`. After setting `z=0`, it becomes a constant or its other
input and can be removed by semantic normalization. The restricted circuit
computes `f` with at least one fewer gate. Iterating this inequality over the
`m` fresh variables yields `C(F)>=K+m`, matching the construction.

## Joint-quotient count

Under base row `e in {0,1}`, let `G_e=NOT H_e`. The `j`th OR-tail gate
computes

`A_{e,j}=G_e OR z_1 OR ... OR z_j`, `1<=j<=m`,

and the final gate computes `B_e=NOT A_{e,m}`.

For fixed `e`, different `j` have different essential fresh-variable sets.
For fixed `j`, the two rows are distinct because `G_0!=G_1`. Every `A` is
active and nonconstant. The two `B_e` are active, nonconstant, and distinct;
they cannot collide with an `A` because setting `z_1=1` makes every `A` one
and every `B` zero. Thus these gates supply `2m+2` distinct joint classes.

## Balanced-product application boundary

LEMMA-052 proves coordinate density of `B_{rho,s}`: every outer coordinate
takes both values somewhere in the family. Hence no positive or negative raw
unit literal is one on every balanced product member. The exact tail theorem
therefore cannot itself furnish a GATE-004V counterexample. Mixed signed
clauses of width at least two are not covered.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits, fresh negative raw literals, restrictions, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform base and minimum complement circuit; uniform fresh-tail construction |
| Circuit size | Exact `K+m` under `C(NOT H)=K-1`; displayed paired-row quotient has at least `2m+2` tail classes and loss at most `K-m-2` |
| Circuit depth | Base unrestricted; displayed OR chain may have linear depth and ends in one NOT |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every finite nonconstant `H` with `C(NOT H)=C(H)-1`, every `m>=1`, and every pair of distinct nonconstant designated row residuals; balanced-product exclusion for every `rho>=7,s>=1` |
| Regime | Worst-case exact total-function theorem with an explicit polarity hypothesis; not a SAT circuit lower bound |
