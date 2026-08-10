# GATE-004AP — exclude the two-binary-split theta orientations

**Label: PROVED**

## Falsifiable theorem

Prove that no theta-core cycle-rank-two circuit with exactly two outdegree-two
core split vertices and exactly three NOT gates computes `W_6`.

No such circuit exists. By
LEMMA-127/128 this is exactly the remaining orientation stratum of
GATE-004AO.

The two splits can be parallel, arising from two distinct core sources, or
nested, with a source split feeding a later non-source split. A valid proof
must derive the corresponding two-bit or sequential-bit functional interface
before applying clause cofactor counts.

LEMMA-129 makes this dichotomy exact, and LEMMA-130 excludes the parallel
source case. GATE-004AQ proves the sole remaining nested orientation empty.
Therefore every two-binary-split theta orientation is excluded.

## Model card

| Field | Value |
|---|---|
| Computational model | Two-binary-split theta-core bicyclic circuits for fixed `W_6` with three NOT gates |
| Uniform/non-uniform | Every individual non-uniform remaining theta orientation |
| Circuit size | Excludes the final orientation strata inside `c=2,q=3`, 31 binary gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed theta split structure and Boolean two-bit/sequential interfaces |
| Asymptotic quantifiers | Fixed `W_6` and every theta-core candidate with exactly two binary core splits |
| Regime | Exact finite structural exclusion; not full Hall, a SAT lower bound, or terminal result |
