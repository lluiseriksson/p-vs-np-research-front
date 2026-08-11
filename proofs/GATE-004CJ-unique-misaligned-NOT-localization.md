# GATE-004CJ — descend to the unique mandatory misaligned NOT

**Label: EXPLORATORY**

Choose a minimum parent and satisfying pruning triple lexicographically
minimizing the earlier potentials and then `W`. By LEMMA-189, `W>=1`; fix the
earliest switching mixed NOT `n`, which always contributes to `W`.

## Falsifiable theorem

For the extremal tuple, one of the following holds.

1. If `W>1`, a function- and size-preserving AND/OR/NOT rewrite, together with
   a valid pruning triple, preserves the earlier potentials and strictly
   lowers `W`.
2. If `W=1`, `n` is the unique satisfying-signature-misaligned gate in the
   common backbone. Alignment of every other common gate then forces one
   satisfying code to expose the three GATE-004CH carrier regions in three
   distinct binary elimination classes.
3. The attempted rewrite or unique-NOT localization instead yields a
   LEMMA-183 private certificate or deletion of a non-bridge edge of `gamma`.

Alternative 1 contradicts extremality. Alternative 2 contradicts the exact
two-gate deletion budget. Alternative 3 contradicts extremality or LEMMA-185.
Proving the theorem establishes GATE-004CI without assuming the impossible
normal form `W=0`.

Every rewrite must preserve fanout and basis cost, and the `W=1` argument must
identify the three distinct eliminated classes for every valid pruning triple.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted switching plateau parent with earliest mixed NOT and three pruning maps |
| Uniform/non-uniform | Every individual non-uniform operational GATE-004CI tuple; uniform fresh implication pair |
| Circuit size | Same-size strict descent above `W=1`, or three distinct eliminations/private/non-bridge contradiction at `W=1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and preserved by rewrite |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor equality, finite lexicographic potential, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every operational extremal tuple and every satisfying minimum pruning triple |
| Regime | Exact worst-case unique-misalignment gate; not a SAT lower bound or terminal result |
