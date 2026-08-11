# GATE-004AL — Hall expansion of dependency-cone resources

**Label: PROVED**

Fix a pruned circuit `C` for `W_m` and any spanning tree `T` of its connected
undirected output cone. The resource set consists of all `N` NOT gates and the
`t=B-5m+1` non-tree edges. For clause index `i`, let `P_i(T)` contain every
resource on a directed path from one of that block's five inputs to the
output.

For every subset `I subseteq [m]`,

`|union_{i in I} P_i(T)|>=|I|`.

## Proof

LEMMA-116 establishes the restriction-and-lifting inequality: after setting
all blocks outside `I` true and pruning, the residual `W_k` circuit, where
`k=|I|`, has NOT count `q`, cycle rank `r`, and

`q+r<=|union_{i in I}P_i(T)|`.

LEMMA-139 gives `q+r>=k` at every rank. Therefore every dependency-cone Hall
inequality holds. LEMMA-141 records the full theorem and its matching
consequence. This closes the finite ladder through LEMMA-138 and proves the
resource injection GATE-004AI.

Unlike GATE-004AK's narrower assignment-sensitive neighborhoods, dependency
cones retain resources needed to process a block even when their values do
not change on one selected witness pair.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits, directed dependency cones, spanning trees, and non-tree-edge resources |
| Uniform/non-uniform | Every individual non-uniform circuit, every spanning tree, and uniform clause-block neighborhoods |
| Circuit size | Full Hall expansion proves `m<=N+t` and `B+N>=6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Fundamental cycle bases over `F_2`; finite bipartite matching |
| Asymptotic quantifiers | Every `m>=1`, every pruned circuit for `W_m`, every spanning tree, and every clause-index subset |
| Regime | Exact worst-case dependency-cone Hall theorem; not a base direct sum, SAT lower bound, or terminal result |
