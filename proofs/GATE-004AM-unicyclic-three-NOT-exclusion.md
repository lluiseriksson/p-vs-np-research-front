# GATE-004AM — exclude unicyclic three-NOT circuits for `W_5`

**Label: EXPLORATORY**

## Falsifiable theorem

Prove that no pruned AND/OR/NOT circuit computing the five-block
four-positive/one-negative product `W_5` can simultaneously have cycle rank
one and exactly three NOT gates.

One explicit circuit with those parameters falsifies the theorem.

## Exact bridge

LEMMA-117 proves that every deficient quintet in GATE-004AL restricts to
exactly this stratum. Excluding it proves the Hall inequality for every
quintet. Together with LEMMA-116, subset sizes through five would then be
closed. This remains a local prerequisite, not a full Hall theorem or SAT
lower bound.

LEMMA-118 narrows the topology: at least two NOT gates must lie in the
two-path region and be duplicated by formula unfolding. The active task is to
show that the fixed five clause-indexed decreases cannot be distributed among
two or three duplicated NOT gates around a single reconvergence.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for `W_5` with exact output-cone cycle rank and NOT count |
| Uniform/non-uniform | Every individual non-uniform five-block circuit |
| Circuit size | Target exclusion of the exact `c=1,q=3` stratum; binary count is `25` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean cofactor and inversion structure |
| Asymptotic quantifiers | The fixed five-block function and every pruned circuit with `c=1,q=3` |
| Regime | Exact finite structural gate for quintet Hall; not a full family lower bound or terminal result |
