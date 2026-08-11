# LEMMA-174 — equal-rank restrictions preserve the cycle space modulo contraction

**Label: PROVED**

Let `G` be a connected undirected output-cone multigraph, and let `G'` be the
connected graph obtained after a Boolean restriction, constant propagation,
and pruning. Regard the graph operations as edge/vertex deletions followed by
contractions of forced series structure. If

`rank(G')=rank(G)`,

then the reduction loses no cycle-space dimension. Lifting contracted paths
identifies the cycle space of `G'` isomorphically with that of `G` over
`F_2`. Only tree structure may be deleted; cycle edges may be contracted but
no nonzero cycle coordinate is killed.

## Proof

For a connected graph, cycle rank is `E-V+1`. Deleting a bridge together with
the discarded component and contracting a non-loop edge both preserve this
number. Deleting an edge that lies on a cycle lowers it by one. All pruning
operations are graph-minor operations and rank never increases.

If initial and final ranks agree, no intermediate operation can lower rank.
Thus every deletion is confined to rank-zero tree structure, while every
operation on the cyclic part is a contraction. A cycle of the contracted
graph lifts by expanding contracted paths; this gives an injective linear map
from its cycle space into that of `G`. The two spaces have equal dimension,
so the lift is an isomorphism.

## GATE-004BS consequence

For `r>=3`, delete the primary source first. LEMMA-172 says that either
nonzero cofactor and any satisfying base restriction leave rank exactly
`r-1`, equal to the source-deleted graph. Hence both codes preserve and can be
identified with the same residual cycle space modulo contractions.

## Model card

| Field | Value |
|---|---|
| Computational model | Connected undirected output-cone multigraphs under restriction minors and contractions |
| Uniform/non-uniform | Every individual finite graph reduction; GATE-004BS consequence is non-uniform |
| Circuit size | No gate bound; exact equality of initial and final cycle rank |
| Circuit depth | Unrestricted |
| Fan-in | Graph theorem; circuit application retains AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Cycle spaces over `F_2` |
| Asymptotic quantifiers | Every connected finite multigraph restriction reduction of equal cycle rank |
| Regime | Exact topology theorem; not clause incidence, resource pruning, a SAT lower bound, or terminal result |
