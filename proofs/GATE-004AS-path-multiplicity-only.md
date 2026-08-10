# GATE-004AS-PATH-MULTIPLICITY-ONLY — unfolding count cannot exclude the tetracyclic stratum

**Label: NO-GO**

A cycle-rank-four output cone has at most sixteen directed paths from any gate
to the output. For four NOT gates with unfolding multiplicities
`r_1,...,r_4`, formula inversion for `W_9` supplies only

`1<=r_j<=16` and `r_1+r_2+r_3+r_4>=9`.

The inequalities admit, for example, `(1,1,1,6)` and `(2,2,2,3)`. Markov's
circuit inversion bound is exactly four. Thus generic unfolding and inversion
do not contradict `c=4,q=4`.

This no-go does not construct a circuit or refute GATE-004AS. It requires a
topology-sensitive rank-four reduction.

## Model card

| Field | Value |
|---|---|
| Computational model | Tetracyclic formula unfolding and NOT path multiplicities for fixed `W_9` |
| Uniform/non-uniform | Every individual non-uniform candidate in the exact `c=4,q=4` stratum |
| Circuit size | Four parent NOT gates, each unfolding at most sixteen times, while only nine total occurrences are required |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Binary cycle space and Boolean-lattice inversion; no algebraic circuit model |
| Asymptotic quantifiers | Fixed `W_9` and every cycle-rank-four candidate with four NOT gates |
| Regime | Quantitative no-go for path multiplicity alone; GATE-004AS remains open |
