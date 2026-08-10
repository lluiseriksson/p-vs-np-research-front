# LEMMA-092 — an explicit length-88 block repairs the mask-8 quintuple

**Label: PROVED**

Let `j=526344`, whose binary expansion is
`10000000100000001000`. The neutral block `01 T_j` has length 88. Place it at
coordinate 20. On coordinates `(88,96,104,107,108)`, treating a coordinate
outside the block as the surrounding all-one padding, the resulting bits are
exactly `11101`. Its zero mask is therefore 8.

The direct bit-string check and complete symbolic length-88 oracle agree. By
LEMMA-091 the shifted representative is not reachable through length 84, so
88 is the first admissible block-length increment that repairs this particular
obstruction.

This is one local repair. It does not establish complete width-five coverage,
a circuit lower bound, or progress on the terminal P-versus-NP statement.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma neutral block, all-one surrounding padding, and five-coordinate incidence |
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
