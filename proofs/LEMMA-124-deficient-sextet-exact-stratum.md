# LEMMA-124 — every deficient dependency sextet has the exact `(c,q)=(2,3)` stratum

**Label: PROVED**

Fix a parent circuit, spanning tree, and six-index set `I`. If the union of
the dependency-cone resources `P_i(T)` is Hall-deficient, then it has exactly
five resources. Restricting all other blocks to true and pruning yields a
`W_6` circuit with exactly three NOT gates and cycle rank exactly two. Every
one of the five union resources survives in the corresponding count.

## Proof

Let `Q+C<=5` count the NOT and non-tree-edge resources in the deficient union,
and let `q,c` be the residual NOT count and cycle rank. LEMMA-116's lifting
argument gives `q<=Q`, `c<=C`, and `q+c<=5`.

Markov gives `q>=ceil(log_2(7))=3`. If `c=0`, formula inversion gives
`q>=6`. If `c=1`, LEMMA-123 gives `q>=6`. If `c>=3`, then already
`q+c>=6`. Therefore only `c=2` remains, and the bounds force `q=3` and
`q+c=5`.

As in LEMMA-117,

`5=q+c <= Q+C <=5`,

so every inequality is equality: `Q=3`, `C=2`, `q=3`, and `c=2`.

## Model card

| Field | Value |
|---|---|
| Computational model | Six-block restrictions of unrestricted circuits and dependency-cone NOT/non-tree-edge resources |
| Uniform/non-uniform | Every individual non-uniform parent circuit, spanning tree, and deficient six-index subset |
| Circuit size | Deficiency forces union size five and residual `q=3,c=2`, hence 31 binary gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean restrictions and inversion complexity |
| Asymptotic quantifiers | Every parent `m>=6` and every Hall-deficient selected sextet |
| Regime | Exact worst-case obstruction stratum; not existence of a deficient sextet, SAT lower bound, or terminal result |
