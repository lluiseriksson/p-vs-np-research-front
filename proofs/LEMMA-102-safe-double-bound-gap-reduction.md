# LEMMA-102 — `2B..2B+3` is a safe aligned finite gap reduction

**Label: PROVED**

Let every allowed block be a binary interval of length at most `B`, with start
coordinate divisible by four. Fix finitely many selected coordinates and a
budget of at most `k` pairwise nonoverlapping blocks. For zero-mask incidence,
every consecutive selected-coordinate gap at least `2B` may be replaced by the
unique congruent value in `{2B,2B+1,2B+2,2B+3}`. This preserves exactly the
obtainable masks.

First delete any placed block that has no zero on a selected coordinate; this
does not change the zero mask and can only relax nonoverlap. At a gap from
`x` to `y` with `y-x>=2B`, no remaining block meets selected coordinates on
both sides. Partition the blocks accordingly. A left block has end at most
`x+B`. A right block has start strictly greater than `y-B`. Translate every
right selected coordinate and every right block left by the same multiple of
four until the gap is in `{2B,...,2B+3}`. Bits, alignment, internal order, and
same-side nonoverlap are unchanged. At the new gap, each right start is still
strictly greater than `x+B`, so cross-side blocks remain nonoverlapping.

The reverse operation translates the right component farther right and cannot
create an overlap. Repeating at each large gap proves exact equivalence.

Consequently, for maximum length `B=116`, a geometry-only complete five-
coordinate reduction has gaps in `{1,...,235}`, not merely `{1,...,20}` or
`{1,...,119}`. It contains

`4 * 235^4 = 12,199,202,500`

residue/gap types before any SAT-specific compression. A smaller domain needs
an additional normal-form theorem about the actual neutral blocks.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite aligned bounded intervals, nonoverlap, selected-coordinate zero masks |
| Uniform/non-uniform | Uniform geometric reduction for every finite block alphabet |
| Circuit size | No circuit claim |
| Circuit depth | Irrelevant |
| Fan-in | Irrelevant to the interval theorem |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and translation modulo four |
| Asymptotic quantifiers | Every `B,k`, every finite length-at-most-`B` alphabet, and every selected-coordinate tuple with adequate slot margins |
| Regime | Exact finite-reduction theorem; not a universality, circuit, or terminal result |
