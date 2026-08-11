# GATE-004CG-CARRIER-COVERAGE-ONLY — carrier regions need not be eliminated

**Label: NO-GO**

## Tempting inference

Define three canonical Boolean-difference carrier regions and infer that each
must meet a different binary gate eliminated by a satisfying restriction.

## Failure

Pair-sensitive parent gates may survive a restriction as nonconstant base
computation; LEMMA-178 requires at least one such survivor in every satisfying
minor. A simple family shows arbitrary downstream absorption. Let

`h=u OR x`, `g_i=h OR z_i` for `1<=i<=m`,

and let the output be a binary AND tree over the `g_i`. Before restriction,
every `g_i` depends on `u`. Under `u=0`, the single upstream gate `h` contracts
to `x`, while every `g_i` remains a live binary gate computing `x OR z_i`.
Setting all other `z_j=1` and varying `z_i` shows each survivor is essential.

Thus arbitrarily many carrier routes can be absorbed into the surviving base
cone after one upstream neutralization. A carrier is canonical by LEMMA-187,
but an assignment of one eliminated gate per carrier region is not.

The family is not minimum and is not a plateau counterexample. It closes
carrier-coverage-only counting. A valid proof must compare how carrier regions
are absorbed across all three minimum satisfying minors, not merely within one
chosen pruning.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted AND/OR/NOT fanout DAG under restriction and surviving base absorption |
| Uniform/non-uniform | Uniform finite family for every `m>=1`; no minimum-parent claim |
| Circuit size | `O(m)` pair-sensitive carrier gates survive after one upstream contraction |
| Circuit depth | Unrestricted target; logarithmic output-tree depth in the family |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor carriers only |
| Asymptotic quantifiers | Every positive integer `m` and every assignment to the displayed inputs |
| Regime | Structural no-go for carrier-coverage-only charging; not a plateau counterexample, SAT lower bound, or terminal result |
