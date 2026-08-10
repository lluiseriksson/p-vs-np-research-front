# LEMMA-069 — the ten ENC-022 blocks retain every aligned signed triple

**Label: PROVED**

For the ten blocks `01 T_j,10 F_j`, `j in {1,2,4,8,16}`, the first three
bits of every aligned four-bit chunk range over exactly
`{000,001,010,011,100,111}`. Two nonoverlapping four-aligned blocks cannot
both meet one aligned chunk. Thus one/two-block options omit both `101` and
`110` there. The sole `A_rho` option adds at most one, so at least one remains
absent on every one of the `rho` disjoint aligned triples. The corresponding
signed clauses are common.

The reference certificate is `enc022_common_aligned_signed_triples` and its
test. This proves no circuit lower bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact ENC-022 one/two-block contexts, one long option, aligned signed triples, and pattern incidence |
| Uniform/non-uniform | Uniform ten-block alphabet and placements; no circuit selected |
| Circuit size | No lower bound; common disjoint signed-triple packing at least `rho` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | Encoded/circuit AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Every `rho>=8` and every aligned chunk |
| Regime | Exact witness-family obstruction; not a circuit or terminal result |
