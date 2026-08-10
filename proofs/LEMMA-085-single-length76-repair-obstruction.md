# LEMMA-085 — the single length-76 repair retains a shifted mask-16 obstruction

**Label: PROVED**

Adjoin identifier 98,370 to the 412-identifier Cycle-075 alphabet. Although it
repairs the LEMMA-083 representative, no union of at most four nonoverlapping
aligned blocks from this 413-identifier alphabet realizes zero mask 16,
pattern `11110`, on `(78,80,88,93,94)`. The explicit and bitset interval DPs
agree that mask 16 is the only missing ordinary mask.

Translate offsets `{0,2,10,15,16}` by multiples of twenty with a 76-coordinate
boundary margin. The quintuples are disjoint and alignment is preserved.
`A_rho` can repair at most one because each `11110` occurrence uses four of its
six one positions. Hence `N/20-O(1)` disjoint common signed width-five clauses
survive.

The exact gap-at-most-20 audit at bound 76 checks 640,000 types and returns
494 failures, with residue counts `150,132,103,109`. This closes only the
single-identifier repair, not the complete length-76 alphabet.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts, two interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform fixed 413-identifier alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/20-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Alphabet-specific exact obstruction; not a circuit or terminal result |
