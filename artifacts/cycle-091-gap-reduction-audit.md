# Cycle 091 aligned-gap reduction audit

## Structural result A

**Label: PROVED**

LEMMA-101 gives an exact counterexample to truncating every gap at one block
length.

## Structural result B

**Label: PROVED**

LEMMA-102 proves the safe geometry-only threshold `2B`.

## Corrected width-three audit

**Label: NUMERICAL**

The corrected LEMMA-071 domain has 22,500 triples (`B=36`, gaps through 75).
The exact bitset verifier returns zero failures, so LEMMA-071 and GATE-004AB
retain their `PROVED` labels with a repaired reduction.

## Corrected width-four domain accounting

**Label: PROVED**

For LEMMA-075 (`B=68`), the safe quartet domain has 10,742,476 types, not
1,431,644. That larger audit was not run on Windows. LEMMA-075 and GATE-004AD
are demoted to `EXPLORATORY`; the old finite certificate remains valid only on
its stated subdomain.

## Targeted length-116 query

**Label: NUMERICAL**

A separate exact length-116 query checked 1,792 predecessor-shaped quintets
and found zero failures. This is `NUMERICAL` evidence only and neither proves
universality nor changes terminal progress.
