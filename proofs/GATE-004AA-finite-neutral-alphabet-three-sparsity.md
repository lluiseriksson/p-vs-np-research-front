# GATE-004AA — a finite neutral alphabet suppresses signed clauses through width three

**Label: NO-GO**

## Rejected theorem

Call a binary block `B` *universally neutral* when its length is divisible by
four and, for every suffix string `phi`, `B phi` parses exactly when `phi`
parses and has the same satisfiability value. For a fixed length bound `L`,
let `N_L` contain every universally neutral block of length at most `L`.

For `rho>L`, form a length-`4rho` slot family from:

1. every ENC-020 coordinate-dense option;
2. the tunable block `A_rho`; and
3. every four-aligned placement of every block in `N_L`, with all-one gaps.

The proposed claim was that there exist absolute constants `L,c_3` such that, for every
`rho>L`, every pairwise variable-disjoint family of common signed clauses of
width at most three has at most `c_3` members per slot.

## Structural counterexample

LEMMA-067 supplies exactly the falsifier. For every fixed `L`, choose
`D=floor(4rho/3)>=max(L,16)` and the `D` disjoint triples
`(i,i+D,i+2D)`. Every single translated bounded block has zeros on at most one
coordinate of a triple, so it misses all four patterns with at least two
zeros. The sole `A_rho` option can add only one pattern. At least three missing
patterns, and therefore at least three common signed clauses, remain on every
triple.

Thus the family has at least `D` disjoint common width-three clauses per slot,
contradicting every constant `c_3` as `rho` grows.

## Consequence

The failure uses only the one-bounded-block-per-option geometry, not the
contents or neutrality of the alphabet. Enlarging a fixed alphabet cannot
repair it. A constructive successor must allow multiple independently placed
blocks in each option or change the product geometry. GATE-004AB tests the
two-block repair.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total SAT-gamma parser contexts, finite neutral block alphabets, aligned translations, independent slot products, and signed clause matching through width three |
| Uniform/non-uniform | Uniform finite alphabet once `L` is fixed; uniform placements and parameters; later circuit adversary fully non-uniform |
| Circuit size | No lower bound; actual disjoint common signed-triple packing at least `floor(4rho/3)` per slot |
| Circuit depth | Neutral blocks have constant depth/length for fixed `L`; tunable block may have linear NOT depth; later circuits unrestricted |
| Fan-in | Encoded and circuit AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite parser-state actions and Boolean pattern incidence only |
| Asymptotic quantifiers | Every fixed proposed `L,c_3`; all sufficiently large `rho`; explicit disjoint counterfamily |
| Regime | Structural witness-construction no-go; not a circuit lower bound, promise statement, average-case statement, or terminal result |
