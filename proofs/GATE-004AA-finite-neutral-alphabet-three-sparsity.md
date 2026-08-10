# GATE-004AA — a finite neutral alphabet suppresses signed clauses through width three

**Label: EXPLORATORY**

## Falsifiable theorem

Call a binary block `B` *universally neutral* when its length is divisible by
four and, for every suffix string `phi`, `B phi` parses exactly when `phi`
parses and has the same satisfiability value. For a fixed length bound `L`,
let `N_L` contain every universally neutral block of length at most `L`.

For `rho>L`, form a length-`4rho` slot family from:

1. every ENC-020 coordinate-dense option;
2. the tunable block `A_rho`; and
3. every four-aligned placement of every block in `N_L`, with all-one gaps.

Prove that there exist absolute constants `L,c_3` such that, for every
`rho>L`, every pairwise variable-disjoint family of common signed clauses of
width at most three has at most `c_3` members per slot.

The claim is falsified by proving that for every fixed `L` the resulting slot
family retains an unbounded disjoint common signed-clause packing of width at
most three.

## Why this is the next positive construction gate

LEMMA-066 shows that attacking the current aligned signed triples through
exact circuit size merely returns to the unresolved implication direct sum.
GATE-004AA instead asks whether a fixed, exact syntax alphabet can remove the
entire width-three incidence vulnerability while preserving coordinate
density, the all-one option, and the tunable `A_rho` run.

If proved, choose the slot count with a sufficiently large constant divisor
so that `c_3 s<K`, while retaining all run-window and all-long packing bounds.
This would define a stronger positive witness gate. It would still leave
overlapping width-at-least-four and nonclausal predicates, and it would not
establish circuit loss by itself.

## First attack

Characterize universally neutral blocks by the finite parser-state action of
their token stream, enumerate the resulting aligned three-coordinate pattern
alphabet for increasing `L`, and either find a constant alphabet whose common
signed-triple matching is boundary-confined or extract a translation-invariant
obstruction valid for every `L`.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total SAT-gamma parser contexts, finite neutral block alphabets, aligned translations, independent slot products, and signed clause matching through width three |
| Uniform/non-uniform | Uniform finite alphabet once `L` is fixed; uniform placements and parameters; later circuit adversary fully non-uniform |
| Circuit size | No lower bound; target common signed width-at-most-three matching at most `c_3 s`, chosen below base floor `K` |
| Circuit depth | Neutral blocks have constant depth/length for fixed `L`; tunable block may have linear NOT depth; later circuits unrestricted |
| Fan-in | Encoded and circuit AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite parser-state actions and Boolean pattern incidence only |
| Asymptotic quantifiers | Exists fixed constants `L,c_3`; every integer `rho>L`; every disjoint common signed clause family of width at most three; later every sufficiently large canonical parameter |
| Regime | Worst-case exact witness-construction gate; not a circuit lower bound, promise statement, average-case statement, or terminal result |
