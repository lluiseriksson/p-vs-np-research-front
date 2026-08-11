# GATE-004DH — lower-bound joint cofactor-circuit saving

**Label: EXPLORATORY**

LEMMA-214 pays every raw-`u` entry of a jointly masked multi-output region.
NG-157 shows that entry count can stay one while private deficit is unbounded.

## Falsifiable theorem

For an escape region `S` with output vector `O` and selected cofactor `sigma`,
let `J_sigma(S,O)` be `|S|` minus the minimum constant-free joint circuit size
of the nonconstant cofactor vector `O|_{u=sigma}`, after constant output
occurrences are propagated into their named consumers. Prove that every
refined minimum endpoint with deficit `D_b>0` admits a jointly masked escape
region (or a disjoint collection with shared gates charged once) satisfying

```text
sum J_sigma(S,O) >= D_b,
```

or else yields a third satisfying-pruning loss, non-bridge deletion, or strict
`W,Q,R_0` descent. Every minimum joint circuit and its interface must be named;
the raw number of inputs, outputs, paths, or frontier edges is insufficient.

The theorem is falsified by a refined minimum parent in which all jointly
masked escape-region cofactor savings total less than `D_b`, all satisfying
prunings lose exactly two binary gates, and no earlier descent exists. Regions
with no common masking cofactor, raw counterflow, absence of an aligned
boundary formula, and incomparable cofactors remain explicit branches.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau with marked multi-output escape regions |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; joint cofactor-circuit savings must total at least `D_b` or force an exact contradiction |
| Circuit depth | Unrestricted; joint circuit and shared-region depth unbounded |
| Fan-in | AND/OR two; NOT one; all output occurrences, shared gates, constants, and pruning survivors audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Minimum joint Boolean cofactor circuits, physical DAG interfaces, and satisfying cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual comparable, unmasked, raw/shared, no-formula, or incomparable boundary |
| Regime | Exact worst-case joint-saving gate; not a SAT lower bound or terminal result |
