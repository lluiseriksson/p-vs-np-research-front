# LEMMA-228 — coexisting swap provenance is distinct origins or a cycle

**Label: PROVED**

Let `G` be a finite circuit DAG, let `k` be a binary gate with distinct
physical predecessors `p,q`, and let `R` be a marked set of physical origins.
Suppose a marked directed path `P` runs from `r_p in R` through `p` to `k`,
and a marked directed path `Q` runs from `r_q in R` through `q` to `k`. Then:

1. if `r_p != r_q`, the two routes have distinct marked origins; or
2. if `r_p=r_q`, their union contains a nonzero undirected cycle coordinate.

In the second case choose the last common vertex `w` of the two routes before
their final arrival at `k`. The suffixes from `w` to `k` are internally
vertex-disjoint and distinct, so their symmetric difference is a nonzero
cycle over `F_2`.

## Proof

The origin equality gives the exhaustive dichotomy. In the equal-origin case,
both finite paths contain their common start and end. Choose a common vertex
maximal along a topological order subject to lying before the two distinct
input edges into `k`. After that vertex the routes cannot meet before `k`, by
maximality. They are distinct because their last predecessors are `p` and `q`.
Forgetting orientation, the union of two internally disjoint paths with the
same endpoints is a cycle; equivalently their edge-vector sum has zero
boundary and is nonzero.

The lemma is conditional on paths coexisting in one physical DAG. Union-graph
reachability assembled from incompatible old/new edges is not enough. It also
does not prove that distinct origins are free hosts or that the cycle is lost.

## Model card

| Field | Value |
|---|---|
| Computational model | One finite physical circuit DAG with marked origins, paths, and a binary reconvergence gate |
| Uniform/non-uniform | Every finite non-uniform marked DAG satisfying the path premises |
| Circuit size | No bound; two named routes and one binary gate |
| Circuit depth | Unrestricted finite acyclic depth |
| Fan-in | Reconvergence fan-in two; ambient AND/OR two and NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Physical DAG paths and undirected cycle space over `F_2` |
| Asymptotic quantifiers | Every finite DAG, marked origin pair, coexisting path pair, and binary reconvergence |
| Regime | Exact worst-case conditional topology theorem; not path existence, resource loss, SAT lower bound, or terminal result |
