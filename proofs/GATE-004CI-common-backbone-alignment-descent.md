# GATE-004CI — align the common backbone or expose three classes

**Label: EXPLORATORY**

Among all minimum plateau parents and valid triples of satisfying minimum
prunings, retain the previous lexicographic minima and then minimize

`W = number of gates g surviving all three prunings with not (g_00=g_01=g_11)`.

This extremal tuple exists because the input set, parent size, labelled DAG
set, and pruning choices are finite. LEMMA-188 gives a common physical
backbone of at least `K-4` gates and places every NOT in it.

## Falsifiable theorem

For the extremal tuple, one of the following holds.

1. If `W>0`, a cross-code shared-absorption subcone admits a same-size
   AND/OR/NOT rewrite and pruning triple that does not increase the earlier
   potentials and strictly lowers `W`.
2. If `W=0`, the aligned common backbone forces one satisfying code to expose
   the three GATE-004CH carrier regions in three distinct binary elimination
   classes.
3. The attempted alignment instead yields a LEMMA-183 private realization
   certificate or forces deletion of a non-bridge edge of `gamma`.

Alternative 1 contradicts extremality; alternative 2 contradicts the exact
two-gate loss; alternative 3 contradicts extremality or LEMMA-185. Proving the
theorem establishes GATE-004CH.

Every rewrite must account for fanout and basis cost. LEMMA-188 supplies only
physical overlap, and GATE-004CH-OVERLAP-ONLY shows why equal functions cannot
be inferred without the descent.

LEMMA-189 proves that the active switching branch has the unavoidable floor
`W>=1`, contributed by the earliest mixed NOT, and that at most six total
misaligned gates can be hidden outside the common backbone.
GATE-004CI-ZERO-ALIGNMENT-ONLY rules out treating `W=0` as a free normal form.
GATE-004CJ refines the descent to `W>1` and the unique mandatory-NOT case
`W=1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau parent plus three minimum satisfying pruning maps |
| Uniform/non-uniform | Every individual non-uniform operational GATE-004CH tuple; uniform fresh implication pair |
| Circuit size | Same-size strict `W` descent, three distinct eliminations versus budget two, or private/non-bridge contradiction |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and must be preserved by rewrite |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor equality, finite extremal potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every operational minimum parent/pruning triple under the exact two-gate plateau hypothesis |
| Regime | Exact worst-case common-backbone alignment gate; not a SAT lower bound or terminal result |
