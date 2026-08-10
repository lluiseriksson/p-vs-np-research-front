# LEMMA-088 — every length-at-most-76 identifier block retains mask 16

**Label: PROVED**

Identifiers 1 through 131,071 are exactly the complete standard neutral
alphabet of block length at most 76. No union of at most four nonoverlapping
aligned blocks from this alphabet realizes zero mask 16, pattern `11110`, on
`(76,80,88,93,94)`.

The LEMMA-087 symbolic oracle and the literal direct DP independently return
mask 16 as the sole missing ordinary mask. The symbolic local audit also
checks all 640,000 types having four gaps in `{1,...,20}` and finds 195
failures, with residue counts `53,71,40,31`.

Translate offsets `{0,4,12,17,18}` by multiples of twenty with a 76-coordinate
boundary margin. These quintuples are disjoint. `A_rho` realizes `11110` on at
most one because each occurrence consumes four of its six one positions.
Thus `N/20-O(1)` disjoint common signed width-five clauses survive.

This closes all block lengths through 76 without requiring the remainder of
the `4*79^4` type domain. Blocks of length at least 80 remain unaudited.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, symbolic and literal interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-131071 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/20-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length witness obstruction; not a circuit or terminal result |
