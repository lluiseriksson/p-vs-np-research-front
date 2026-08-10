# GATE-004AR — exclude tricyclic three-NOT circuits for `W_7`

**Label: EXPLORATORY**

## Falsifiable theorem

Prove that no pruned AND/OR/NOT circuit computing the seven-block
four-positive/one-negative product `W_7` has cycle rank three and exactly
three NOT gates. One explicit circuit with those parameters falsifies the
theorem.

## Exact bridge

LEMMA-134 proves that every deficient seven-index dependency-cone Hall set
would restrict to exactly this stratum. Proving this gate would extend the
Hall theorem through size seven. It would not prove full Hall expansion, an
unrestricted SAT circuit lower bound, or either terminal P-versus-NP
statement.

Pure unfolding multiplicity is insufficient by
GATE-004AR-PATH-MULTIPLICITY-ONLY. The next attack must classify connected
cycle-rank-three kernels and identify a source or articulation restriction
that lowers the residual rank enough for LEMMA-119/123/133.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for fixed `W_7` with exact cycle rank three and three NOT gates |
| Uniform/non-uniform | Every individual non-uniform seven-block circuit in the exact stratum |
| Circuit size | Target exclusion of `c=3,q=3`; 37 binary and 40 total gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean source and articulation cofactors |
| Asymptotic quantifiers | Fixed `W_7` and every pruned circuit with `c=3,q=3` |
| Regime | Exact finite structural gate for septet Hall; not a full family lower bound or terminal result |
