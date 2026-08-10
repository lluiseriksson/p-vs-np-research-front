# GATE-004AR — exclude tricyclic three-NOT circuits for `W_7`

**Label: PROVED**

## Falsifiable theorem

No pruned AND/OR/NOT circuit computing the seven-block
four-positive/one-negative product `W_7` has cycle rank three and exactly
three NOT gates.

## Exact bridge

LEMMA-134 proves that every deficient seven-index dependency-cone Hall set
would restrict to exactly this stratum. Proving this gate would extend the
Hall theorem through size seven. It would not prove full Hall expansion, an
unrestricted SAT circuit lower bound, or either terminal P-versus-NP
statement.

Pure unfolding multiplicity is insufficient by
GATE-004AR-PATH-MULTIPLICITY-ONLY. LEMMA-135 instead proves that every
cycle-rank-three circuit for either polarity of `W_m` needs at least `m-2`
NOT gates. At `m=7` this gives five, contradicting three. LEMMA-136 records
the resulting Hall theorem through size seven.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for fixed `W_7` with exact cycle rank three and three NOT gates |
| Uniform/non-uniform | Every individual non-uniform seven-block circuit in the exact stratum |
| Circuit size | Excludes `c=3,q=3`; a candidate would have 37 binary and 40 total gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean source and articulation cofactors |
| Asymptotic quantifiers | Fixed `W_7` and every pruned circuit with `c=3,q=3` |
| Regime | Exact finite structural exclusion for septet Hall; not a full family lower bound or terminal result |
