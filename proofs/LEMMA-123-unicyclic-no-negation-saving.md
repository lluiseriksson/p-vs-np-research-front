# LEMMA-123 — one cycle cannot save a NOT gate for the fixed-sign product

**Label: PROVED**

For every fixed `p>=1` and every `m>=1`, any pruned cycle-rank-one circuit
computing `W_m` contains at least `m` NOT gates.

## Proof

For `m=1`, Markov's circuit inversion theorem already gives one NOT. Assume
`m>=2` below.

Apply the one-bit factorization of LEMMA-120. Let `h` be the number of NOT
gates in the upstream formula `A(X)` and `q` the total circuit NOT count. The
downstream factor `F(z,Y)` has a formula with `q-h` NOT occurrences. Unfolding
the unique cycle duplicates precisely the `h` upstream NOT gates, so it also
gives a formula for `W_m` with `q+h` NOT occurrences. LEMMA-119 implies

`q+h>=m`.                                                     (1)

Apply the cofactor dichotomy LEMMA-121.

- If no clause is cut, write `a+b=m` for the whole clauses in `X` and `Y`.
  The lemma gives `h>=a` and `q-h>=b`, hence `q>=m`.
- If exactly one clause is cut, there is no `X`-whole clause and LEMMA-121
  gives `q-h>=m-1`. If `h>=1`, then `q>=m`. If `h=0`, inequality (1) gives
  `q>=m` directly.

The cases are exhaustive. Thus an undirected cycle rank of one provides no
NOT-count saving for this function family.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unicyclic AND/OR/NOT circuits for disjoint fixed-sign clause products |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform function family |
| Circuit size | NOT count at least `m`; binary gate count unrestricted beyond cycle rank one |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank, one-bit cofactors, and Boolean-lattice inversion |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, and every pruned circuit with cycle rank one |
| Regime | Exact worst-case unicyclic NOT lower bound; not a general circuit-size or terminal result |
