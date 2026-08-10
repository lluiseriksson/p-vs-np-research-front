# LEMMA-061 — implication-sparse slots retain a linear signed-triple packing

**Label: PROVED**

## Statement

Fix `rho>=13` and the enhanced length-`4rho` slot option set `S^+_rho`
from LEMMA-060. In every aligned chunk

`(z_{4k},z_{4k+1},z_{4k+2}), 0<=k<rho`,

at least one of the clauses

`NOT z_{4k} OR z_{4k+1} OR NOT z_{4k+2}`

and

`NOT z_{4k} OR NOT z_{4k+1} OR z_{4k+2}`

is one on every slot option. Consequently one slot contains `rho`
pairwise variable-disjoint common signed width-three clauses, and the
independent `s`-slot product contains `rho*s=P/4` such clauses.

More generally, every common clause meeting multiple slots contains a
slot-local common subclause. Since `S^+_rho` has no common unit literal,
every cross-slot common width-three clause contains a common slot-local
binary subclause. Hence any variable-disjoint family of cross-slot common
width-three clauses has at most `18s` members by LEMMA-060.

## Aligned-chunk proof

A clause is false on exactly one assignment to its three variables. The two
displayed clauses are false respectively on `101` and `110`.

Remove the single tunable option `A_rho` from `S^+_rho`. Every remaining
non-all-one option is a four-aligned placement of an ENC-020 block or of one
of `A_7,...,A_12`. Direct inspection of this fixed block alphabet shows that
the first three bits of every aligned four-bit chunk belong to

`{000,001,010,011,100,111}`.

Thus neither `101` nor `110` occurs in an aligned chunk among the fixed
options. At a given chunk, the one additional string `A_rho` contributes
only one three-bit pattern, so it can introduce at most one of the two
missing patterns. At least one remains absent from the complete option set,
and the clause falsified by that absent pattern is common. The `rho` aligned
triples are disjoint. Taking the same construction independently in every
slot gives `rho*s`; since `P=4rho*s`, this equals `P/4`.

The fixed-alphabet inspection and the full quantified construction are
reproduced by
`test_implication_sparse_slots_retain_common_signed_triples`. The test is a
certificate of the explicit bit calculation, not proof-assistant
verification.

## Product localization proof

Partition the literals of a clause by slots. If no nonempty slot-local
subclause were common in its slot, then for every involved slot one could
choose an option falsifying all literals assigned to that slot. Product
independence combines those choices into a product member falsifying the
whole clause, contradicting commonness.

For a width-three clause spanning multiple slots, the common local subclause
has width one or two. Coordinate density excludes width one. Choose one
common binary subclause from every clause in a variable-disjoint cross-slot
family. These chosen pairs remain variable-disjoint, so LEMMA-060 bounds
their number by `18s`.

## Scope

The `P/4` packing is a semantic feature of the witness family, not a circuit
lower bound or a counterexample to GATE-004X. Turning it into negative
diagonal loss requires an exact unrestricted-circuit cost or
representation-independent quotient theorem for the signed triples. That is
GATE-004Y.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact neutral SAT-gamma contexts, independent slot products, signed raw-coordinate width-three clauses, and set packing |
| Uniform/non-uniform | Uniform explicit block alphabet, options, clause choice, slots, and parameters; no circuit selected |
| Circuit size | No lower bound; within-slot common signed-triple packing exactly certified at `rho*s=P/4`; cross-slot disjoint width-three packing at most `18s` |
| Circuit depth | Irrelevant to the incidence proof; later circuits unrestricted |
| Fan-in | Clause OR binarized to fan-in two; literals may use fan-in-one NOT; later circuits AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean pattern incidence and Cartesian products only |
| Asymptotic quantifiers | Every `rho>=13` and `s>=1`; all `rho` aligned chunks and all product members |
| Regime | Worst-case exact witness-family theorem; not a circuit lower bound, promise statement, average-case statement, or terminal result |
