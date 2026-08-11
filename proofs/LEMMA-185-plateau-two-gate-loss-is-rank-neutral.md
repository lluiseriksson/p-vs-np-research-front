# LEMMA-185 — every satisfying two-gate loss is cycle-rank neutral

**Label: PROVED**

Assume the exact plateau `C(F)=C(A)+2` and restrict a minimum parent to any
satisfying pair code. In every restriction/pruning account reaching a minimum
circuit for `A`:

1. exactly two gates disappear and both are binary;
2. no NOT resource and no cycle-rank unit disappears; and
3. graph operations on the cyclic core are contractions only. In particular,
   no edge that is non-bridge at its deletion stage can be deleted.

Thus a gate lying on a parent cycle may disappear only through a rank-neutral
contraction. Gate loss by itself is not evidence that a cycle coordinate lies
in the restriction kernel.

## Proof

LEMMA-178 proves the exact two-gate loss, preservation of NOT count and cycle
rank separately, and that the two lost gates are binary. Apply LEMMA-174 to
the output-cone graph reduction. Because initial and final cycle ranks agree,
no intermediate operation can lower rank. Deleting a non-bridge edge lowers
the rank of a connected graph by one, while contractions and deletion of tree
structure preserve it. Consequently all changes to the cyclic core are
contractions and the induced cycle-space map is injective.

The statement does not identify which two binary gates contract or disappear
for any code.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau circuits under satisfying restriction and pruning |
| Uniform/non-uniform | Every individual finite non-uniform plateau parent and satisfying code |
| Circuit size | Exactly two binary gates lost; no NOT or rank loss |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle-space minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant finite base, minimum two-gate plateau parent, and code in `{00,01,11}` |
| Regime | Exact worst-case restriction bookkeeping; not localization of the two gates, a SAT lower bound, or terminal result |
