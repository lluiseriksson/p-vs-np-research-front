# LEMMA-080 — free-bit coverage leaves a token-boundary quintet obstruction

**Label: PROVED**

Adjoin the LEMMA-079 basis to the 94-identifier Cycle-074 alphabet, removing
duplicates, for 412 identifiers total and maximum neutral-block length 68.
No union of at most four nonoverlapping aligned blocks realizes zero mask 16,
bit pattern `11110`, on `(70,71,80,85,86)`. The original explicit interval DP
and the bitset-compressed DP agree that mask 16 is the only missing ordinary
mask on this quintuple.

Translate offsets `{0,1,10,15,16}` by multiples of twenty with a 68-coordinate
boundary margin. These quintuples are disjoint and alignment is preserved.
`A_rho` realizes `11110` on at most one because each occurrence consumes four
of its six one positions. Hence the family retains `N/20-O(1)` disjoint common
signed width-five clauses

`NOT z_1 OR NOT z_2 OR NOT z_3 OR NOT z_4 OR z_5`.

The exact gap-at-most-20 audit checks 640,000 types and returns 497 failures,
down from 1,787 before adding the basis. Together with LEMMA-079, this locates
the remaining defect outside arbitrary free-bit projections: fixed token and
gamma-boundary geometry must also be covered. It does not rule out a refined
length-68 alphabet.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts, two independent interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform fixed 412-identifier alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/20-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Alphabet-specific exact obstruction; not a circuit or terminal result |
