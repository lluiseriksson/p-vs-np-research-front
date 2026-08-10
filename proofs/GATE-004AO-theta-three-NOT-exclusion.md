# GATE-004AO — exclude theta-core three-NOT circuits for `W_6`

**Label: EXPLORATORY**

## Falsifiable theorem

Prove that no pruned AND/OR/NOT circuit computing `W_6` has cycle rank two,
exactly three NOT gates, and a theta 2-core. One explicit circuit with these
parameters falsifies the theorem.

LEMMA-126 excludes every other bicyclic core, so GATE-004AO is exactly
equivalent to the remaining part of GATE-004AN. A proof would close
dependency-cone Hall at subset size six, but no larger subset or terminal
lower bound automatically follows.

The theta kernel has two branch vertices joined by three internally disjoint
core paths and no articulation separating a whole cycle. The next attack must
bound the Boolean interface across a two-vertex separator or classify the
cofactor states carried by the three branches.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned theta-core bicyclic Boolean circuits for fixed `W_6` with exact NOT count |
| Uniform/non-uniform | Every individual non-uniform theta-core candidate |
| Circuit size | Target exclusion of the remaining `c=2,q=3`, 31-binary-gate stratum |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Theta multigraph topology and Boolean separator cofactors |
| Asymptotic quantifiers | Fixed `W_6` and every pruned theta-core circuit with three NOT gates |
| Regime | Exact finite structural gate; not full Hall, a SAT lower bound, or terminal result |
