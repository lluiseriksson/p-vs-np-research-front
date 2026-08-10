# LEMMA-074 — every length-48 identifier block retains a quartet obstruction

**Label: PROVED**

Let the ordinary neutral alphabet contain both `01 T_j` and `10 F_j` for
every identifier `1<=j<=1023`. These are exactly all standard identifier
blocks of length at most 48. No union of at most three nonoverlapping,
four-aligned blocks realizes zero mask 8, equivalently bit pattern `1110`, on
the representative quartet `(48,53,57,58)`.

The claim is a finite exhaustive interval-DP statement. The verifier enumerates
every aligned placement of all 2,046 blocks in a length-256 representative,
deduplicates the induced `(end,start,zero-mask)` triples, and computes every OR
of masks obtainable from at most three nonoverlapping intervals. Bit 8 is
absent, while every other nonzero mask below 15 is present. The regression test
calls `reached_masks_direct` on the complete identifier range.

Translate offsets `{0,5,9,10}` by multiples of twelve, retaining a 48-coordinate
margin at both slot boundaries. The quartets are disjoint and translation by a
multiple of four preserves the certificate. The exceptional long option
`A_rho` realizes `1110` on at most two quartets, because each realization uses
three distinct one positions and `A_rho` has six ones. Thus the complete
length-48 alphabet retains `N/12-O(1)` disjoint common clauses

`NOT z_1 OR NOT z_2 OR NOT z_3 OR z_4`.

Identifiers 1,058, 1,042, and other explicit length-52-or-longer witnesses
repair individual representative failures, so this is a sharp bounded-length
obstruction, not a grammar-wide impossibility theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block neutral contexts, exhaustive interval-DP certificate, one long option, signed width-four clauses, and matching |
| Uniform/non-uniform | Uniform complete length-at-most-48 identifier alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-four packing `N/12-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most two |
| Regime | Complete bounded-length witness obstruction; not a circuit lower bound or terminal result |
