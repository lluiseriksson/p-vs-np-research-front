# LEMMA-053 — common disjoint positive clauses pack into six bits per slot

**Label: PROVED**

## Statement

Let `B_{rho,s}` be the balanced slot-product family from LEMMA-052. Let
`Q_1,...,Q_m` be positive OR clauses on pairwise disjoint sets of outer raw
coordinates, and suppose every `Q_i` is one on every member of
`B_{rho,s}`. Then

`m<=6s`.

The bound is independent of clause widths, placement geometry, and whether
the clauses are consecutive, distant, or otherwise structured.

## Proof

The family contains the all-long member

`a=A_rho A_rho ... A_rho`

with `s` copies. The exact block `A_rho=01 10 V_j 11 V_j` has six one bits:
one in each binary operator token, two in the NOT token, and one in each of
the two power-of-two variable codes. Hence `a` has exactly `6s` one positions.

Every common positive clause must be one on `a`, so its coordinate set
contains at least one of those `6s` positions. Because the clauses use
pairwise disjoint coordinate sets, select a different all-long one position
for each clause. This injects the `m` clauses into a set of size `6s`, proving
`m<=6s`. QED.

## Consequence for the exact clause tail

For `s=floor((R-1)/8)`, LEMMA-052 gives the eligible base-size floor
`K>=R-1`, while

`m<=6s<=3(R-1)/4<=K`.

LEMMA-048 certifies loss at most `K-m` for a disjoint positive-clause
extension. Its generic negativity certificate requires `m>K`, which is
impossible here. Therefore no choice of disjoint common positive clauses can
reproduce the established exact negative-tail proof against GATE-004V.

This does not prove nonnegative actual loss: additional quotient classes could
exist, and signed, overlapping, or non-clausal predicates are outside the
lemma.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact balanced neutral slot products and pairwise variable-disjoint positive raw-coordinate OR clauses |
| Uniform/non-uniform | Uniform all-long witness and counting injection; arbitrary non-uniform clause selection |
| Circuit size | At most `6s` disjoint common positive clauses; below the eligible base floor `K>=R-1` for `s=floor((R-1)/8)` |
| Circuit depth | Candidate clause and later circuits unrestricted; counting proof independent of depth |
| Fan-in | Clauses may be implemented with fan-in-two OR; later AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set packing only |
| Asymptotic quantifiers | Every `rho>=7,s>=1`, every pairwise disjoint family of positive clauses common to the full product; explicit comparison for all sufficiently large `R` |
| Regime | Worst-case exact witness-family method boundary; not a circuit lower bound or positive loss theorem |
