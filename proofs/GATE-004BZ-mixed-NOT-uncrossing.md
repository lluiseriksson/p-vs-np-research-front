# GATE-004BZ — uncross the earliest mixed surviving NOT

**Label: EXPLORATORY**

Assume a pair-minimal two-gate plateau parent from GATE-004BY. Choose a
topologically earliest NOT gate `n=NOT h` whose function depends on `u_j`.
LEMMA-179 makes `h` a mixed pair-sensitive binary gate, with no direct fresh-
pair input, and makes `n` survive all three satisfying codes as a nonconstant
base gate.

## Falsifiable theorem

There is a function- and size-preserving rewrite of the cone through `h,n`
that either:

1. makes `n` pair-insensitive, strictly lowering `T_j`; or
2. exposes a pair-only NOT that is deleted by one satisfying restriction.

The first alternative contradicts pair minimality. The second lowers `N+r`
and supplies the one-step descent. Either closes the hypothetical two-gate
plateau.

Common physical survival does not make the three restricted base signatures
equal; LEMMA-173/NG-118 already forbids that inference. The rewrite must use
the full three-equal/one-zero output table and the fact that all three
restricted parents are minimum circuits for the same `A`.

## Model card

| Field | Value |
|---|---|
| Computational model | Pair-minimal minimum unrestricted plateau circuits localized at an earliest mixed u-sensitive NOT |
| Uniform/non-uniform | Every individual non-uniform operational plateau parent; uniform fresh implication pair |
| Circuit size | Same-size rewrite lowering pair sensitivity, or one satisfying restriction loses a NOT resource |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean gate identities, four pair cofactors, and `N+r` accounting over `F_2` cycle rank |
| Asymptotic quantifiers | Every operational GATE-004BY parent under the two-gate equality |
| Regime | Exact worst-case sufficient local uncrossing gate; not a SAT lower bound or terminal result |
