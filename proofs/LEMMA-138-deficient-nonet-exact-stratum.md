# LEMMA-138 — every deficient dependency nonet is exactly tetracyclic with four NOTs

**Label: PROVED**

Fix a parent circuit, spanning tree, and nine-index set `I`. If the union of
the dependency-cone resources `P_i(T)` is Hall-deficient, then it has exactly
eight resources. Restricting every other block to true and pruning yields a
`W_9` circuit with exactly four NOT gates and cycle rank exactly four.

## Proof

Let `Q+C<=8` count union resources and let `q,c` be the residual NOT count and
cycle rank. Then `q<=Q`, `c<=C`, and `q+c<=8` by LEMMA-116.

Markov gives `q>=ceil(log_2(10))=4`. Ranks zero and one require `q>=9` by
LEMMA-119/123. Rank two requires `q>=8` by LEMMA-133, and rank three requires
`q>=7` by LEMMA-135; in each case `q+c>=9`. If `c>=5`, Markov again gives
`q+c>=9`. Therefore `c=4`, and equality forces `q=4` and `q+c=8`.

As in LEMMA-134, all lifting inequalities are equalities, so `Q=4`, `C=4`,
`q=4`, and `c=4`. Since `W_9` has 45 essential inputs, the residual has
`B=45-1+c=48` binary gates and 52 gates total.

## Model card

| Field | Value |
|---|---|
| Computational model | Nine-block restrictions of unrestricted circuits and dependency-cone NOT/non-tree-edge resources |
| Uniform/non-uniform | Every individual non-uniform parent circuit, spanning tree, and deficient nine-index subset |
| Circuit size | Deficiency forces union size eight and residual `q=4,c=4`, hence 48 binary and 52 total gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean restrictions and inversion complexity |
| Asymptotic quantifiers | Every parent `m>=9` and every Hall-deficient selected nonet |
| Regime | Exact worst-case obstruction stratum; not existence of a deficient nonet, a SAT lower bound, or a terminal result |
