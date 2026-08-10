# LEMMA-090 — an explicit length-84 block repairs the boundary quintuple

**Label: PROVED**

Let `j=278594`, whose binary expansion is
`1000100000001000010`. Both standard neutral blocks

- `01 T_j`, and
- `10 F_j`

have length 84. Place either block at coordinate 60. On coordinates
`(84,88,96,101,102)` its bits are exactly `11110`, so its zero mask is 16.

This is checked directly from the SAT-gamma bit string. The complete symbolic
alphabet through length 84 also reaches mask 16. LEMMA-089 proves that the
corresponding shifted representative is not reachable through length 80, so
84 is the first admissible block-length increment in this four-divisible
encoding that repairs this particular obstruction.

The result repairs one local type only. It does not prove complete width-five
coverage, a circuit lower bound, or any statement about P versus NP.

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
