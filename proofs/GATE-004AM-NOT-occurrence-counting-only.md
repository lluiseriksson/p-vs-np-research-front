# GATE-004AM-NOT-OCCURRENCE-COUNTING-ONLY — unfolding count excludes the stratum

**Label: NO-GO**

Formula unfolding and inversion-count comparison alone do not exclude the
unicyclic three-NOT stratum. If `k` parent NOT gates lie on two directed paths
to the output, the unfolded formula contains `3+k` NOT occurrences. Formula
inversion requires five, so the method yields only `k>=2`.

Both remaining integer patterns are numerically feasible for this bound:

- two duplicated NOTs give exactly five occurrences;
- three duplicated NOTs give six occurrences.

Thus occurrence counting reaches, but does not exceed, the required formula
inversion complexity. Repeating it cannot produce a contradiction. The next
argument must use which clause-indexed cofactor changes each duplicated NOT
can support, or another function-specific placement invariant.

This no-go does not exhibit a circuit. GATE-004AM was subsequently proved by
the one-bit factorization and cofactor-partition argument; occurrence counting
itself remains insufficient. GATE-004AL beyond size five remains open.

## Model card

| Field | Value |
|---|---|
| Computational model | Unicyclic formula unfolding and formula inversion complexity for `W_5` |
| Uniform/non-uniform | Every individual non-uniform circuit in the exact `c=1,q=3` stratum |
| Circuit size | Parent NOT count three; unfolded count five or six after the necessary duplication |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank and Boolean-lattice inversion only |
| Asymptotic quantifiers | Every candidate unicyclic three-NOT circuit for the fixed `W_5` |
| Regime | Quantitative no-go for occurrence counting; function-specific exclusion remains open |
