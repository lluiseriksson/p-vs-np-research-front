# GATE-004AN — exclude bicyclic three-NOT circuits for `W_6`

**Label: EXPLORATORY**

## Falsifiable theorem

Prove that no pruned AND/OR/NOT circuit computing the six-block
four-positive/one-negative product `W_6` has cycle rank two and exactly three
NOT gates. One explicit circuit with those parameters falsifies the theorem.

## Exact bridge

LEMMA-124 proves that every deficient six-index dependency neighborhood
restricts to exactly this stratum. Excluding it would extend GATE-004AL's Hall
inequalities from size five to size six. The candidate has 31 binary gates
and three NOT gates, total size 34 versus the displayed 35.

The active structural task is to generalize LEMMA-120's one-bit articulation
to the possible cycle-rank-two block-cut topologies and combine the resulting
one- or two-bit interfaces with clause cofactor counts.

LEMMA-125 classifies all bicyclic cores, and LEMMA-126 excludes the
figure-eight and dumbbell cases. GATE-004AO is the exact remaining theta-core
subgate.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for fixed `W_6` with exact cycle rank two and three NOT gates |
| Uniform/non-uniform | Every individual non-uniform six-block circuit |
| Circuit size | Target exclusion of `c=2,q=3`; binary count exactly 31, total 34 |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean cofactor interfaces |
| Asymptotic quantifiers | The fixed six-block function and every pruned circuit with `c=2,q=3` |
| Regime | Exact finite structural gate for sextet Hall; not a full family lower bound or terminal result |
