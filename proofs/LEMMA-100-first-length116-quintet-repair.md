# LEMMA-100 — an explicit length-116 block repairs the mask-16 quintuple

**Label: PROVED**

Let `j=67125314`, whose binary expansion is
`100000000000100000001000010`. The neutral block `01 T_j` has length 116.
Placed at coordinate 84, it reads exactly `11110` on
`(116,128,136,141,142)`, realizing mask 16.

The direct bit string and complete symbolic length-116 oracle agree. LEMMA-099
proves the shifted type unreachable through length 112, so 116 is the first
admissible increment repairing this representative.

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
| Regime | Local worst-case repair lemma; not promise, average-case, distributional, universality, circuit, or terminal progress |
