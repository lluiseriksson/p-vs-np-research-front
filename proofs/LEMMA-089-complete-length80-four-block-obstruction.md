# LEMMA-089 — every length-at-most-80 identifier block retains mask 16

**Label: PROVED**

Identifiers 1 through 262,143 are exactly the complete standard neutral
alphabet of block length at most 80. No union of at most four nonoverlapping
four-aligned blocks from this alphabet realizes zero mask 16, equivalently
pattern `11110`, on `(80,84,92,97,98)`.

The LEMMA-087 symbolic oracle and the literal direct interval DP independently
return mask 16 as the sole missing ordinary mask. Translating offsets
`{0,4,12,17,18}` by multiples of twenty gives disjoint quintuples. The long
option `A_rho` realizes `11110` on at most one such quintuple because each
occurrence consumes four of its six one positions. Hence `N/20-O(1)` common
signed width-five clauses survive.

This is a bounded-alphabet obstruction only. LEMMA-090 gives a length-84
block that repairs this representative, so no stronger conclusion is drawn.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, symbolic and literal interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-262143 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/20-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length witness obstruction; not a circuit or terminal result |
