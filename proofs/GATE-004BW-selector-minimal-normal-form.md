# GATE-004BW — selector-minimal minimum representation has a uniform loss

**Label: EXPLORATORY**

For a gate `g` in a circuit with distinguished primary input `x`, call `g`
selector-sensitive when its Boolean gate function has distinct cofactors at
`x=0` and `x=1`. Among all minimum-size pruned representations of the
GATE-004BU function, choose one minimizing the integer

`S(C)=#{selector-sensitive noninput gates}`.

LEMMA-176 proves that such a representation exists. LEMMA-153 makes `N+r`
identical for all minimum representations.

## Falsifiable theorem

Every selector-minimal representation has a tail clause `i` whose neutral
restriction, with `x` left free, either deletes a NOT gate from the pruned
output cone or lowers its undirected cycle rank.

Either event lowers `N+r` by at least one and proves GATE-004BU. Unlike an
unspecified exchange, selector minimality is an independently defined finite
normal form. The proof must show that absence of a uniform loss permits a
function- and size-preserving rewrite with strictly smaller `S(C)`.

LEMMA-175 prevents proving this by counting changed signatures. Standard
constant propagation and duplicate elimination also give no rewrite in an
already minimum pruned circuit. A successful exchange must use the disjoint
implication semantics and the actual shared directed paths.

## Model card

| Field | Value |
|---|---|
| Computational model | Selector-minimal members of the minimum unrestricted two-excess implication-circuit class |
| Uniform/non-uniform | Extremal choice inside every finite non-uniform minimum-representation set; uniform tail family |
| Circuit size | Minimum size fixed; `N+r` fixed by LEMMA-153; target restriction loses at least one resource |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004BU function and every selector-minimal minimum representation |
| Regime | Exact worst-case sufficient normal-form subgate; not a SAT lower bound or terminal result |
