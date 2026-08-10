# LEMMA-103 — exact phase-sensitive gap reduction for the length-68 alphabet

**Label: PROVED**

For the 92-identifier LEMMA-075 alphabet, define a block's right overhang at
a selected zero to be `end-position` and its left overhang to be
`position-start`. Among zero coordinates of residue `r` modulo four, the exact
maxima are

`R=(68,67,66,65)` and `L=(64,65,66,67)`.

The upper bounds follow because every block length is a multiple of four and
at most 68. A zero offset congruent to `r` is at least `r` and at most the
largest integer below 68 with that residue. Equality witnesses are:

- right: identifier 16,450 (`T` at offsets 0 and 3; `F` at offsets 1 and 2);
- left: identifier 16,450 (`T` at offsets 64,65,67) and identifier 16,452
  (`T` at offset 66).

Consider a selected-coordinate gap from `x` of residue `a` to `y` of residue
`b`. Delete placed blocks having no selected zero. A left-component block may
zero an earlier selected coordinate `p`, not necessarily `x`. If `p` has
residue `c`, then either `p=x` and `c=a`, or `x-p` is at least the least
positive integer congruent to `a-c` modulo four. Using `R_c=68-c` gives

`end-x <= R_c-(x-p) <= 68-a = R_a`.

The analogous calculation for a right-component block zeroing a later
coordinate `q` gives

`start-y >= -L_b`,

because either `q=y,c=b`, or `q-y` is at least the least positive integer
congruent to `c-b`. Therefore cross-gap nonoverlap is automatic once

`y-x >= R_a+L_b = 132+b-a`.

This threshold already has residue `b-a` modulo four. Translating the entire
right component by a multiple of four reduces every larger congruent gap to
that threshold while preserving bits, alignment, internal order, and all
nonoverlap. Expansion proves the converse. Repeating across gaps is exact.

For a left residue `a`, the retained representative gaps are precisely
`1,...,135-a`, so the phase caps are `(135,134,133,132)`. The three-gap
quartet counts by first residue are

`(2,405,635; 2,387,748; 2,369,994; 2,352,372)`,

totalling `9,515,749`. `verification/phase_gap_reduction.py` independently
derives the overhangs, caps, and count from the literal blocks.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-aligned length-at-most-68 SAT-gamma neutral blocks, nonoverlap, and selected-coordinate zero masks |
| Uniform/non-uniform | Uniform fixed 92-identifier alphabet and deterministic phase reduction; no circuit selected |
| Circuit size | No lower bound; finite-domain reduction only |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and translation modulo four |
| Asymptotic quantifiers | Every selected quartet with adequate slot margins and every union of at most three nonoverlapping blocks from the fixed alphabet |
| Regime | Exact SAT-specific finite-reduction theorem; not universality, a circuit lower bound, or terminal progress |
