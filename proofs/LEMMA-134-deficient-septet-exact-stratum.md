# LEMMA-134 — every deficient dependency septet is exactly tricyclic with three NOTs

**Label: PROVED**

Fix a parent circuit, spanning tree, and seven-index set `I`. If the union of
the dependency-cone resources `P_i(T)` is Hall-deficient, then it has exactly
six resources. Restricting every other block to true and pruning yields a
`W_7` circuit with exactly three NOT gates and cycle rank exactly three.

## Proof

Let `Q+C<=6` count the NOT and non-tree-edge resources in the deficient union,
and let `q,c` be the residual NOT count and cycle rank. LEMMA-116's lifting
argument gives `q<=Q`, `c<=C`, and `q+c<=6`.

Markov gives `q>=ceil(log_2(8))=3`. If `c=0`, formula inversion gives `q>=7`.
If `c=1`, LEMMA-123 gives `q>=7`. If `c=2`, LEMMA-133 gives `q>=6`, hence
`q+c>=8`. If `c>=4`, Markov already gives `q+c>=7`. Therefore `c=3`, and the
bounds force `q=3` and `q+c=6`.

Consequently every inequality is equality:

`6=q+c <= Q+C <=6`.

Thus `Q=3`, `C=3`, `q=3`, and `c=3`. Since `W_7` has 35 essential inputs,
the residual has `B=35-1+c=37` binary gates and 40 gates total.

## Model card

| Field | Value |
|---|---|
| Computational model | Seven-block restrictions of unrestricted circuits and dependency-cone NOT/non-tree-edge resources |
| Uniform/non-uniform | Every individual non-uniform parent circuit, spanning tree, and deficient seven-index subset |
| Circuit size | Deficiency forces union size six and residual `q=3,c=3`, hence 37 binary and 40 total gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean restrictions and inversion complexity |
| Asymptotic quantifiers | Every parent `m>=7` and every Hall-deficient selected septet |
| Regime | Exact worst-case obstruction stratum; not existence of a deficient septet, a SAT lower bound, or a terminal result |
