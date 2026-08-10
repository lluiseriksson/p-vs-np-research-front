# LEMMA-091 — every length-at-most-84 identifier block retains mask 8

**Label: PROVED**

Identifiers 1 through 524,287 are exactly the complete standard neutral
alphabet of block length at most 84. No union of at most four nonoverlapping
four-aligned blocks from this alphabet realizes zero mask 8, equivalently
pattern `11101`, on `(84,92,100,103,104)`.

The complete symbolic audit checks all 640,000 types with first coordinate in
residues 0 through 3 and four gaps in `{1,...,20}`. It finds respectively
`30,31,31,30` failures, for 122 total. On the displayed representative, the
LEMMA-087 symbolic oracle and a literal interval DP over all 524,287
identifiers independently agree that mask 8 is the sole missing ordinary
mask.

Translate offsets `{0,8,16,19,20}` by multiples of twenty-four. These
quintuples are disjoint. The long option `A_rho` realizes `11101` on at most
one because each occurrence consumes four of its six one positions. Thus
`N/24-O(1)` disjoint common signed width-five clauses survive.

This is a complete bounded-alphabet obstruction. Blocks of length at least 88
and the unrestricted GATE-004AF construction remain unaudited.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, symbolic and literal interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-524287 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/24-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length witness obstruction; not a circuit or terminal result |
