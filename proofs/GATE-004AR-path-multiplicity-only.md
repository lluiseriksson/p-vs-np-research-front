# GATE-004AR-PATH-MULTIPLICITY-ONLY — unfolding count cannot exclude the tricyclic stratum

**Label: NO-GO**

A cycle-rank-three output cone has at most eight directed paths from any gate
to the output. If the three NOT gates have unfolding multiplicities
`r_1,r_2,r_3`, then

`1<=r_j<=8` and `r_1+r_2+r_3>=7`,

where the second inequality is only the formula inversion requirement for
`W_7`. These inequalities are compatible; for example, they admit `(1,1,5)`
and `(2,2,3)`. Markov's circuit bound is also exactly three. Therefore the
generic path-count and inversion inequalities do not contradict `c=3,q=3`.

This method no-go neither constructs such a circuit nor refutes GATE-004AR.
Further progress requires topology-sensitive information about how the three
cycles share source regions, separators, or NOT gates.

## Model card

| Field | Value |
|---|---|
| Computational model | Tricyclic formula unfolding and NOT path multiplicities for fixed `W_7` |
| Uniform/non-uniform | Every individual non-uniform candidate in the exact `c=3,q=3` stratum |
| Circuit size | Three parent NOT gates; each unfolds at most eight times; only seven total occurrences are required |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Binary cycle space and Boolean-lattice inversion; no algebraic circuit model |
| Asymptotic quantifiers | Fixed `W_7` and every cycle-rank-three candidate with three NOT gates |
| Regime | Quantitative no-go for path multiplicity alone; GATE-004AR remains open |
