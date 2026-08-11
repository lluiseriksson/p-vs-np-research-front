# LEMMA-218 — the carrier charge leaves at most two or four losses

**Label: PROVED**

At the size-three switching endpoint, let `C={g,h}` be the two binary carrier
gates and `L_00,L_01,L_11` the exact two-element satisfying-pruning loss sets.
Then:

1. in the `g=u AND p`, `h=g OR q` orientation,
   `L_00=L_01=C` and
   `|(L_00 union L_01 union L_11) minus C|<=2`;
2. in the `g=u OR p`, `h=g AND q` orientation,
   `L_11=C` and
   `|(L_00 union L_01 union L_11) minus C|<=4`.

Thus the six-gate union cap of LEMMA-216 never represents six uncharged
resources at this endpoint.

## Proof

LEMMA-193 proves the displayed exact equalities. In the first orientation,
removing `C` deletes all of `L_00` and `L_01`, leaving only `L_11 minus C`, a
subset of the two-element set `L_11`. In the second orientation, removing `C`
deletes `L_11`, leaving `(L_00 union L_01) minus C`, whose cardinality is at
most `|L_00|+|L_01|=4`. No gate is counted twice.

The bounds can be smaller through overlap with `C` or between the remaining
sets. The lemma supplies caps, not injections from deficit units.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT exact plateau with the size-three alternating carrier |
| Uniform/non-uniform | Every finite non-uniform hypothetical endpoint in either LEMMA-193 orientation |
| Circuit size | Parent `K+2`; exact two-gate losses; uncharged union at most two in AND→OR and four in OR→AND |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Physical gate sets and exact carrier deletion identities |
| Asymptotic quantifiers | Every nonconstant base, endpoint, orientation, and satisfying loss triple |
| Regime | Exact worst-case residual resource cap; not an injection, SAT lower bound, or terminal result |
