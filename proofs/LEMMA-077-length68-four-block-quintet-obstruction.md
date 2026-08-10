# LEMMA-077 — the LEMMA-075 alphabet retains a four-block quintet obstruction

**Label: PROVED**

For the fixed 92-identifier alphabet of LEMMA-075, no union of at most four
nonoverlapping aligned blocks realizes zero mask 16, equivalently bit pattern
`11110`, on the representative quintuple `(68,72,75,77,78)`. Both the original
explicit interval DP and the bitset-compressed earliest-end DP return the same
two missing masks, 12 and 16. A routine regression test checks that equality.

Translate offsets `{0,4,7,9,10}` by multiples of twelve that retain a
68-coordinate margin at both slot boundaries. These quintuples are pairwise
disjoint, and translation by a multiple of four preserves the aligned-block
certificate. The long option `A_rho` realizes `11110` on at most one quintuple:
each realization consumes four distinct one positions, while `A_rho` has only
six ones. Discarding that quintuple leaves `N/12-O(1)` disjoint common clauses

`NOT z_1 OR NOT z_2 OR NOT z_3 OR NOT z_4 OR z_5`.

This refutes only reuse of the LEMMA-075 alphabet at width five. Larger or
differently selected fixed alphabets may repair the missing mask, so
GATE-004AF remains open.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts, two independent interval-DP implementations, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform fixed 92-identifier alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/12-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Alphabet-specific exact witness obstruction; not a circuit or terminal result |
