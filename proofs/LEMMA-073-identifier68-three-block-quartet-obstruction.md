# LEMMA-073 — identifier-68 three-block contexts retain a linear quartet packing

**Label: PROVED**

For the neutral alphabet `01 T_j,10 F_j`, `1<=j<=68`, no union of at most
three nonoverlapping aligned blocks realizes pattern `1110` on the
representative quartet `(36,57,61,62)`. The deterministic interval-DP
certificate is `reached_masks`; its bit 8 is zero.

Translate the offset set `{0,21,25,26}` by starts `8k` that remain at least
36 coordinates from both slot boundaries. These quartets are pairwise
disjoint: no nonzero difference among the four offsets is divisible by eight.
Modulo-four translation and the 36 length bound preserve the missing pattern.

The long option `A_rho` can realize `1110` on at most two of these disjoint
quartets, because each occurrence consumes three distinct one positions and
`A_rho` has six ones. Discarding those two leaves `N/8-O(1)` disjoint common
clauses

`NOT z_1 OR NOT z_2 OR NOT z_3 OR z_4`.

This refutes only the identifier-1-through-68 specialization of GATE-004AD.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block neutral contexts, interval-DP pattern certificate, one long option, signed width-four clauses, and matching |
| Uniform/non-uniform | Uniform identifier-68 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-four packing `N/8-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible `N`; every eligible translation except at most two |
| Regime | Alphabet-specific exact witness obstruction; not a circuit or terminal result |
