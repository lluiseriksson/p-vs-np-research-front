# LEMMA-076 — three bounded blocks plus one exception retain width five

**Label: PROVED**

Let `N,B` be positive integers with `m=floor(N/5)>=B`. Consider any binary
option family on `N` coordinates in which every ordinary option has all zeros
inside at most three intervals, each of length at most `B`, and there is at
most one arbitrary exceptional option.

For each `0<=i<m`, form the quintuple

`Q_i=(i,i+m,i+2m,i+3m,i+4m)`.

The quintuples are pairwise disjoint. Because consecutive coordinates are at
distance at least `B`, each bounded interval meets at most one coordinate of a
quintuple. Every ordinary option therefore has zeros on at most three of its
five coordinates. It omits all six patterns having four or five zeros:

`C(5,4)+C(5,5)=6`.

The exceptional option realizes only one pattern on each `Q_i`, so at least
five of those six patterns remain absent from the whole family. Each absent
pattern defines a non-tautological signed width-five clause whose unique
falsifying assignment is that pattern. Choose one per quintuple. This gives
`floor(N/5)` pairwise coordinate-disjoint common signed width-five clauses.

More sharply, the exception can realize at most one of the five four-zero
patterns, so at least four such patterns remain absent on every quintuple.
LEMMA-108 records the resulting four-positive/one-negative packing.

Applied to the LEMMA-075 slots, `B=68` and the exceptional option is `A_rho`.
The lemma exposes a next-width tail but says nothing about its exact circuit
cost, minimum representations, or quotient survival.

## Model card

| Field | Value |
|---|---|
| Computational model | Binary option families, three bounded zero intervals, one arbitrary exception, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform distant quintuples; arbitrary bounded alphabets and exceptional option |
| Circuit size | No lower bound; common signed width-five packing at least `floor(N/5)` |
| Circuit depth | Later circuits unrestricted |
| Fan-in | Later AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Every `N,B` with `floor(N/5)>=B`; every qualifying option family |
| Regime | Exact worst-case combinatorial obstruction; not an average-case, promise, circuit, or terminal result |
