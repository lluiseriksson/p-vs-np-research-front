# LEMMA-095 — an explicit length-100 block repairs the mask-16 quintuple

**Label: PROVED**

Let `j=4210754`, whose binary expansion is
`10000000100000001000010`. The neutral block `01 T_j` has length 100. Placed
at coordinate 72, its bits on `(100,108,116,121,122)` are exactly `11110`, so
it realizes zero mask 16.

The direct bit string and complete symbolic length-100 oracle agree. LEMMA-094
shows that the shifted type is unreachable through length 96, making 100 the
first admissible block-length increment that repairs this representative.

This is one local repair, not complete width-five coverage or a circuit result.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma neutral block and five-coordinate incidence |
| Uniform/non-uniform | One explicit uniform identifier and aligned placement; no circuit selected |
| Circuit size | No lower bound; one missing mask repaired |
| Circuit depth | Fixed finite encoding depth; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Exact finite witness, reusable by four-aligned translation |
| Regime | Local repair lemma; not universality, circuit, or terminal progress |
