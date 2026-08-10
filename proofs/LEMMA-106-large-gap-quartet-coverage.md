# LEMMA-106 — every quartet with a gap at least 72 has all ordinary masks

**Label: PROVED**

For the identifier-1-through-68 alphabet, every sufficiently interior ordered
quartet having at least one consecutive coordinate gap of size at least 72
realizes each zero mask 1 through 14 with at most three nonoverlapping aligned
blocks.

Cut at such a gap, from left coordinate `x` to right coordinate `y`. Blocks
used below have length at most 36. After deleting irrelevant blocks, a left
block ends at most at `x+36`, while a right block starts strictly after
`y-36`. Since `y-x>=72`, independently chosen left and right witnesses are
nonoverlapping, and no block meets a selected coordinate across the cut.

It remains to count blocks. An ordinary quartet mask has between one and three
zeros.

- On a singleton component, zero or one block suffices: the identifier-1
  tautology block is `011000111001`, whose zero offsets meet all four residue
  classes modulo four. An aligned translate can therefore zero any interior
  coordinate.
- On a pair, LEMMA-104 gives a one-zero pattern with one block; LEMMA-071's
  pair consequence gives the two-zero pattern with at most two blocks.
- On a triple, LEMMA-071 gives every one- or two-zero pattern with at most two
  blocks, while LEMMA-105 gives the three-zero pattern with at most three.

For a `2+2` cut, the block count is at most the total number of zeros, hence at
most three. For a `1+3` or `3+1` cut, a three-zero triple forces the singleton
to have zero zeros, while a one- or two-zero triple uses at most two blocks and
the singleton at most one. Again the total is at most three.

Consequently every possible quartet obstruction has all three gaps at most
71. The existing LEMMA-075 certificate checks exactly those
`4*71^3=1,431,644` types. This lemma supplies the missing all-gap extension.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact length-at-most-36 neutral blocks, quartet zero masks, component decomposition, and nonoverlap |
| Uniform/non-uniform | Uniform identifiers 1 through 68 and deterministic cut; no circuit selected |
| Circuit size | No lower bound; at most three local witness blocks |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and interval geometry |
| Asymptotic quantifiers | Every sufficiently interior quartet with at least one consecutive gap at least 72 and every ordinary zero mask 1 through 14 |
| Regime | Exact worst-case witness theorem; not a circuit lower bound or terminal result |
