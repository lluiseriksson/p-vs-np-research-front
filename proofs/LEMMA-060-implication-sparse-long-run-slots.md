# LEMMA-060 — translated fixed long blocks confine all common implications

**Label: PROVED**

## Statement

Fix `rho>=13` and slot length `4rho`. Enlarge the balanced option set by
adding, for every `q in {7,8,9,10,11,12}`, every four-aligned placement of
the fixed neutral block `A_q`, filling the remaining slot coordinates with
one bits. Call the resulting option set `S^+_rho`.

Then:

1. every option is an exact validity- and satisfiability-preserving context;
2. the set is coordinate-dense, contains the all-one option and `A_rho`, and
   has maximum zero run at most `rho`;
3. if a mixed clause `z_i OR NOT z_j` is common to all options, then
   `{i,j}` lies entirely in the first twelve or entirely in the last twelve
   slot coordinates;
4. no negative-negative two-clause is common; and
5. a pairwise variable-disjoint common mixed-clause family has at most twelve
   members per slot.

For the independent `s`-slot product, every pairwise variable-disjoint family
of arbitrary signed binary clauses has at most `18s` members. Every disjoint
positive-clause family of arbitrary width still has at most `6s` members.

## Semantic and run proof

Every `A_q` is the exact identity context from ENC-026 and has length `4q`.
Four-aligned placement leaves four-divisible all-one gaps, hence even NOT
chains, on both sides. Composition preserves exact parsing behavior and
satisfiability. The original ENC-020 options preserve coordinate density and
the all-one member. The option `A_rho` preserves the tunable run. Every added
block has run at most twelve, hence at most `rho`.

## Mixed-clause confinement

A mixed clause `z_i OR NOT z_j` is common exactly when no option realizes
`(z_i,z_j)=(0,1)`. For coordinates separated by at least 48, ENC-020's
length-at-most-16 coordinate-zero witness can zero the first coordinate while
leaving the second outside its block and equal to one.

It remains to inspect ordered pairs at distance below 48. All block starts
and lengths are divisible by four, and every added fixed block has length at
most 48. Thus coverage depends only on the two residues modulo four and their
distance when both points are interior, or on the exact distance from one
boundary. Pairs close to both boundaries occur only at the finite lengths
`52,56,...,92`. Every interior and one-boundary configuration translates into
length 256.

Direct inspection of the explicit ENC-020 blocks and all placements of
`A_7,...,A_12` at those finite lengths shows that the only ordered pairs still
missing one mixed pattern have both endpoints in

`{0,...,11}`

or both in

`{4rho-12,...,4rho-1}`.

The deterministic certificate is
`test_translated_long_blocks_confine_common_implications`. It enumerates only
the explicit bit strings and the finite translation representatives. The
preceding distance/boundary reduction supplies the unbounded quantifier.

Each twelve-vertex boundary region has matching number at most six, so a
disjoint common mixed family has at most twelve clauses per slot. The all-one
option falsifies every negative-negative clause.

## Product and base-floor comparison

For coordinates in distinct slots, coordinate density and product
independence realize all four bit pairs, so no signed binary clause crossing
slots is common. Inside slots, split any disjoint signed binary family into
positive-positive and mixed clauses. The all-long product member has six one
bits per slot, so LEMMA-053 bounds the positive subfamily by `6s`; the mixed
subfamily is at most `12s`. The total is at most `18s`.

Choose

`s=floor((R-1)/24)`.

The eligible base still has `K>=R-1`, while

`18s<=3(R-1)/4<=K`, `6s<=K/4`, and the run-window count remains below
`4s<=K/6`. The all-long interval-cover argument of LEMMA-052 is unchanged.
Thus every established disjoint positive or signed-binary tail lies below the
base floor. This proves no positive quotient loss.

## Scope

Signed clauses of width at least three, overlapping predicates, and arbitrary
nonclausal common predicates remain open. Boundary confinement is a finite-
alphabet syntax theorem, not an unrestricted circuit lower bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact neutral SAT-gamma contexts, independent slot products, signed raw-coordinate binary clauses, matching, and unrestricted-circuit essential-input floors |
| Uniform/non-uniform | Uniform fixed block alphabet, placements, product, and parameters; later circuit adversary fully non-uniform |
| Circuit size | Common disjoint signed-binary packing at most `18s`; arbitrary-width positive packing at most `6s`; both below `K>=R-1` for `s=floor((R-1)/24)` |
| Circuit depth | Contexts may have linear NOT depth; later circuits unrestricted |
| Fan-in | Encoded and circuit AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite bit incidence and modulo-four translation only; no algebraic circuit model |
| Asymptotic quantifiers | Every `rho>=13,s>=1`; finite certificate plus translation for every slot length; explicit comparison for sufficiently large `R` |
| Regime | Worst-case exact total-language witness theorem and method boundary; not a circuit lower bound |
