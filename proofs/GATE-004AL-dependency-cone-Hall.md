# GATE-004AL — Hall expansion of dependency-cone resources

**Label: EXPLORATORY**

## Resource neighborhoods

Fix a pruned circuit `C` for the four-positive/one-negative product `W_m` and
a spanning tree `T` of its connected undirected output cone. The resource set
consists of all `N` NOT gates and the `t=B-5m+1` non-tree edges of `T`.

For clause index `i`, let `P_i(T)` contain every resource lying on at least one
directed path from one of the five inputs
`{u_i,v_{i,1},...,v_{i,4}}` to the output. A non-tree edge is included when
that directed circuit edge lies on such a path.

## Falsifiable theorem

Prove that some spanning tree `T` satisfies

`|union_{i in I} P_i(T)| >= |I|`

for every subset `I subseteq [m]`. One circuit for which every spanning tree
has a deficient subset falsifies the theorem.

Hall's theorem would inject the `m` clause indices into the `N+t` resources,
giving `m<=N+t` and exactly GATE-004AJ/AI/AH. Unlike the narrower sensitive
neighborhoods of GATE-004AK, dependency cones retain NOT gates whose values
do not change on a particular witness pair but which are required to process
that block's positive variables.

LEMMA-116 proves every Hall inequality with `|I|<=4`. The smallest unresolved
subset has size five.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits, directed dependency cones, spanning trees, and non-tree-edge cycle resources |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform clause-block neighborhoods |
| Circuit size | Full Hall expansion would imply `m<=N+t` and `B+N>=6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; finite bipartite matching |
| Asymptotic quantifiers | Every `m>=5`, every pruned circuit for `W_m`, and every subset of clause indices |
| Regime | Exact worst-case dependency-cone Hall gate; not a base direct sum, SAT lower bound, or terminal result |
