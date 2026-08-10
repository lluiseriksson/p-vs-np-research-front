# LEMMA-117 — every deficient dependency quintet has the exact `(c,q)=(1,3)` stratum

**Label: PROVED**

Fix a circuit for `W_m`, a spanning tree `T`, and a five-index set `I`. If its
dependency-cone resource union from GATE-004AL is Hall-deficient, then that
union has exactly four resources. After restricting all blocks outside `I`
to true, propagating constants, and pruning, the residual circuit for `W_5`
has exactly three NOT gates and cycle rank exactly one. Every resource in the
four-element union survives in the corresponding count.

## Proof

Let `Q` and `C` be the numbers of NOT-gate and non-tree-edge resources in the
union. Deficiency gives

`Q+C <= 4`.

Let `q` and `c` be the NOT count and cycle rank after the five-block
restriction and pruning. The lifting argument of LEMMA-116 gives

`q<=Q`, `c<=C`, and therefore `q+c<=4`.

LEMMA-111 for `W_5` gives

`q >= max(ceil(5/2^c),ceil(log_2(6)))`.

If `c=0`, then `q>=5`; if `c>=2`, Markov already gives `q>=3`, so
`q+c>=5`. Both contradict `q+c<=4`. Hence `c=1`, and the same bound gives
`q>=3`. It follows that `q=3` and `q+c=4`.

Now

`4=q+c <= Q+C <=4`.

All inequalities are equalities, so `Q+C=4`, `q=Q=3`, and `c=C=1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Five-block restrictions of unrestricted circuits and dependency-cone NOT/non-tree-edge resources |
| Uniform/non-uniform | Every individual non-uniform parent circuit, spanning tree, and deficient five-index subset |
| Circuit size | Deficiency forces exactly four union resources and residual counts `q=3,c=1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean restriction and inversion complexity |
| Asymptotic quantifiers | Every parent `m>=5` and every Hall-deficient selected quintet |
| Regime | Exact worst-case obstruction stratum; not existence of a deficient quintet, SAT lower bound, or terminal result |
