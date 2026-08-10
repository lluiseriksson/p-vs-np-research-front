# LEMMA-093 — every length-at-most-88 identifier block retains mask 16

**Label: PROVED**

Identifiers 1 through 1,048,575 are exactly the complete standard neutral
alphabet of block length at most 88. No union of at most four nonoverlapping
four-aligned blocks from this alphabet realizes zero mask 16, equivalently
pattern `11110`, on `(88,96,104,109,110)`.

The complete symbolic audit checks 640,000 gap-at-most-20 local types and
finds `21,30,30,30` failures by residue, 111 total. On the displayed type, the
symbolic oracle and a literal DP over all 1,048,575 identifiers independently
agree that mask 16 alone is missing.

Translations of offsets `{0,8,16,21,22}` by multiples of twenty-four are
disjoint. `A_rho` realizes `11110` on at most one because each occurrence
consumes four of its six one positions. Hence `N/24-O(1)` common signed
width-five clauses survive.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, symbolic and literal interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-1048575 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/24-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length witness obstruction; not a circuit or terminal result |
