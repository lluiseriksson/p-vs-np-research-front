# LEMMA-072 — two bounded blocks plus one exception retain linear signed width four

**Label: PROVED**

Let length `N` options have zeros confined to at most two intervals of length
at most `B`, except for one arbitrary option. Put `D=floor(N/4)>=B` and use
the `D` disjoint quadruples `(i,i+D,i+2D,i+3D)`.

Every ordinary option has zeros on at most two coordinates of a quadruple.
Thus it misses all five patterns with at least three zeros. The exceptional
option adds only one pattern, leaving at least four absent. Each absent pattern
defines a common signed width-four clause. Selecting one per quadruple gives
`D` variable-disjoint common clauses.

For the LEMMA-071 slot family, `B=36`, `N=4rho`, and `A_rho` is the sole
exception, so the packing has size `floor(rho)` per slot for sufficiently
large `rho`.

## Model card

| Field | Value |
|---|---|
| Computational model | Binary option families, two bounded zero intervals, one exception, signed width-four clauses, and matching |
| Uniform/non-uniform | Uniform distant quadruples; arbitrary bounded alphabets and exceptional option |
| Circuit size | No lower bound; common signed width-four packing at least `floor(N/4)` |
| Circuit depth | Irrelevant to incidence; later circuits unrestricted |
| Fan-in | Clause OR two after binarization; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Every `N,B` with `floor(N/4)>=B`; every stated option family |
| Regime | Exact combinatorial obstruction; not a circuit lower bound or terminal result |
