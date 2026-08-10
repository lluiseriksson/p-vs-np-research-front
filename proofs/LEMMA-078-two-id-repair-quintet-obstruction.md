# LEMMA-078 — the two-identifier quintet repair retains mask 8

**Label: PROVED**

Add identifiers 1,089 and 1,098 to the 92-identifier LEMMA-075 alphabet. They
repair masks 12 and 16 on the LEMMA-077 quintuple without increasing the
maximum block length beyond 68. Nevertheless, no union of at most four
nonoverlapping aligned blocks from this 94-identifier alphabet realizes zero
mask 8, bit pattern `11101`, on `(70,71,76,77,80)`. The explicit and
bitset-compressed interval DPs agree exactly on the single missing mask.

Translate offsets `{0,1,6,7,10}` by multiples of twelve, retaining a
68-coordinate boundary margin. The quintuples are disjoint and alignment is
preserved. `A_rho` realizes `11101` on at most one of them because each
occurrence uses four distinct one positions and `A_rho` has six. Thus
`N/12-O(1)` disjoint common clauses survive:

`NOT z_1 OR NOT z_2 OR NOT z_3 OR z_4 OR NOT z_5`.

The broader gap-at-most-20 audit found 1,787 failed types across 640,000 exact
types, but the theorem uses only the independently checked representative.
This refutes the two-identifier repair, not every length-68 alphabet.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts, two independent interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform fixed 94-identifier alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/12-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Alphabet-specific exact obstruction; not a circuit or terminal result |
