# GATE-004AN-PATH-MULTIPLICITY-ONLY — unfolding count excludes the bicyclic stratum

**Label: NO-GO**

A cycle-rank-two output cone has at most four directed paths from any gate to
the output. If the three NOT gates have path multiplicities `r_1,r_2,r_3`,
unfolding produces `r_1+r_2+r_3` formula NOT occurrences, with each
`1<=r_j<=4`.

Formula inversion for `W_6` requires only

`r_1+r_2+r_3>=6`.

This is compatible with many integer patterns, including `(2,2,2)` and
`(1,1,4)`. Therefore total path multiplicity alone gives no contradiction;
the generic bound is attained at the resource parameters `c=2,q=3`.

The method no-go does not exhibit a circuit or refute GATE-004AN. A successful
proof must use how the two cycles overlap, the dimension of the intervening
Boolean interface, and the clause partition induced by its articulation
components.

## Model card

| Field | Value |
|---|---|
| Computational model | Bicyclic formula unfolding and NOT path multiplicities for fixed `W_6` |
| Uniform/non-uniform | Every individual non-uniform candidate in the exact `c=2,q=3` stratum |
| Circuit size | Three parent NOT gates; unfolded requirement only six total occurrences with multiplicity at most four each |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank and Boolean-lattice inversion only |
| Asymptotic quantifiers | Every candidate bicyclic three-NOT circuit for fixed `W_6` |
| Regime | Quantitative no-go for path-counting alone; topology-specific exclusion remains open |
