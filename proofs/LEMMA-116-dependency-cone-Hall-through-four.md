# LEMMA-116 — dependency-cone Hall expansion holds through four indices

**Label: PROVED**

For every circuit `C` for `W_m`, every spanning tree `T` of its undirected
output cone, and every clause-index set `I` with `1<=|I|<=4`, the
dependency-cone neighborhoods from GATE-004AL satisfy

`|union_{i in I} P_i(T)| >= |I|`.

## Restriction to the selected blocks

Put `k=|I|`. For each clause outside `I`, set one of its positive variables
to one. The restricted output is exactly the `k`-block product `W_k` on the
five inputs of each selected block.

Propagate constants and prune every node that no longer reaches the output.
Every remaining nonconstant node lifts to a directed path from a selected
block input to the original output: trace backward to a remaining primary
input and forward before simplification. Consequently every surviving NOT
gate belongs to `union_{i in I} P_i(T)`.

Graphically, constant propagation and removal of identity gates perform edge
deletions and contractions; neither operation increases cycle rank. The
original edges relevant to the residual cone lie on selected-block paths.
The tree edges among them create no cycle, and each included non-tree edge can
increase cycle rank by at most one. Hence the residual cycle rank is at most
the number of original non-tree edges in the same neighborhood union.

Let `q` and `c` be respectively the residual NOT count and cycle rank. If the
neighborhood union had fewer than `k` resources, then

`q+c <= |union_{i in I} P_i(T)| < k`.

But LEMMA-111 applied to `W_k` with `p=4` proves `q+c>=g(k)=k` for
`1<=k<=4`. This contradiction proves the Hall inequality.

## Boundary

At `k=5`, LEMMA-111 gives only `q+c>=g(5)=4`. The same restriction argument
therefore stops one resource short; it does not prove the quintet Hall
inequality.

## Model card

| Field | Value |
|---|---|
| Computational model | Full block restrictions of unrestricted AND/OR/NOT circuits, dependency cones, and output-cone cycle rank |
| Uniform/non-uniform | Every individual non-uniform parent circuit; every selected block set of size at most four |
| Circuit size | Hall union lower bound exactly `|I|` for `1<=|I|<=4` |
| Circuit depth | Unrestricted; restriction and pruning preserve a finite DAG |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean restrictions |
| Asymptotic quantifiers | Every `m>=1`, every circuit for `W_m`, every spanning tree, and every `I` with `1<=|I|<=min(4,m)` |
| Regime | Exact worst-case local Hall theorem; quintets, full matching, SAT lower bounds, and the terminal problem remain open |
