# LEMMA-082 — every length-at-most-68 identifier block retains mask 16

**Label: PROVED**

The standard neutral block for identifier `j` has length
`12+4*floor(log_2 j)`. Thus identifiers 1 through 32,767 are exactly the
complete standard alphabet of block length at most 68.

No union of at most four nonoverlapping aligned blocks from this complete
alphabet realizes zero mask 16, bit pattern `11110`, on
`(70,71,80,85,86)`. There are two independent finite certificates:

1. the explicit interval DP directly enumerates all 32,767 identifiers and
   returns mask 16 as the sole missing ordinary mask;
2. LEMMA-081 reduces every possible five-coordinate block behavior to 2,066
   representatives, and the compressed DP returns the same result.

Translate offsets `{0,1,10,15,16}` by multiples of twenty with a
68-coordinate boundary margin. The quintuples are disjoint. `A_rho` can
realize `11110` on at most one because each occurrence consumes four distinct
one positions and it has six. Consequently every sufficiently long slot
retains `N/20-O(1)` disjoint common signed clauses

`NOT z_1 OR NOT z_2 OR NOT z_3 OR NOT z_4 OR z_5`.

This closes every length-at-most-68 specialization of GATE-004AF. Identifiers
of bit length sixteen give block length 72 and are not covered.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, direct and projection-reduced interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-32767 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/20-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length witness obstruction; not a circuit or terminal result |
