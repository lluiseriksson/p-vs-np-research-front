# GATE-004CB — uncross a one-sided first-cancellation mask

**Label: EXPLORATORY**

Assume a pair-minimal two-gate plateau in the switching branch of GATE-004CA.
Use the notation of LEMMA-181 and suppose the first cancellation gate has

`q_01=q_11`.

## Falsifiable theorem

The mask containment at `d` admits a function- and size-preserving rewrite
that strictly lowers the fresh-pair sensitivity count `T_j`, or one satisfying
restriction loses a NOT/cycle resource.

This excludes the one-sided branch. The remaining two-sided branch has a
specific cycle coordinate that survives all three satisfying minors and must
be handled separately.

GATE-004CA-LOCAL-CANCELLATION-ONLY shows that the Boolean mask identity alone
is insufficient. The rewrite must use pair minimality, the fact that each
satisfying minor is a minimum circuit for the same `A`, and the fourth zero
cofactor.

## Model card

| Field | Value |
|---|---|
| Computational model | Pair-minimal minimum plateau circuits with a one-sided first binary mask |
| Uniform/non-uniform | Every individual non-uniform operational one-sided branch; uniform fresh implication pair |
| Circuit size | Same-size strict decrease of `T_j`, or one-unit satisfying-code resource loss |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean mask containment and undirected `N+r` accounting |
| Asymptotic quantifiers | Every operational GATE-004CA parent in the one-sided mask case |
| Regime | Exact worst-case one-sided cancellation subgate; not a SAT lower bound or terminal result |
