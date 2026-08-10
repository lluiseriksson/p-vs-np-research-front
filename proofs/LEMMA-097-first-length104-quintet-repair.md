# LEMMA-097 — an explicit length-104 block repairs the mask-8 quintuple

**Label: PROVED**

Let `j=8390664`, whose binary expansion is
`100000000000100000001000`. The neutral block `01 T_j` has length 104. Place
it at coordinate 24. With the surrounding context bits equal to one, its bits
on `(104,116,124,127,128)` are exactly `11101`; its zero mask is 8.

The direct bit string and complete symbolic length-104 oracle agree. LEMMA-096
shows that the shifted type is unreachable through length 100, so 104 is the
first admissible block-length increment repairing this representative.

This is one local repair, not complete width-five coverage or a circuit result.

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
| Regime | Local worst-case repair lemma; not promise, average-case, distributional, universality, circuit, or terminal progress |
