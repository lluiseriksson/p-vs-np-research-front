# GATE-004AO — exclude theta-core three-NOT circuits for `W_6`

**Label: PROVED**

## Falsifiable theorem

No pruned AND/OR/NOT circuit computing `W_6` has cycle rank two,
exactly three NOT gates, and a theta 2-core. One explicit circuit with these
parameters would falsify the theorem, but none exists.

LEMMA-126 excludes every other bicyclic core, so GATE-004AO is exactly
equivalent to the remaining part of GATE-004AN. The proof closes
dependency-cone Hall at subset size six, but no larger subset or terminal
lower bound automatically follows.

The theta kernel has two branch vertices joined by three internally disjoint
core paths and no articulation separating a whole cycle. The proof classifies
the possible directed split orientations and excludes each one.

LEMMA-127 shows that the directed split excess is exactly two. LEMMA-128
excludes the one-ternary-source orientation, and GATE-004AP excludes every
orientation with two binary split vertices. These cases exhaust LEMMA-127.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned theta-core bicyclic Boolean circuits for fixed `W_6` with exact NOT count |
| Uniform/non-uniform | Every individual non-uniform theta-core candidate |
| Circuit size | Excludes the theta part of `c=2,q=3`, 31 binary gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Theta multigraph topology and Boolean separator cofactors |
| Asymptotic quantifiers | Fixed `W_6` and every pruned theta-core circuit with three NOT gates |
| Regime | Exact finite structural exclusion; not full Hall, a SAT lower bound, or terminal result |
