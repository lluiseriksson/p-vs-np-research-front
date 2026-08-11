# LEMMA-241 — a common-sink antichain has a binary reconvergence tree

**Label: PROVED**

Let `S` be a `k>=1` vertex antichain under directed reachability in a finite
DAG of indegree at most two. If every vertex of `S` reaches one common vertex
`o`, then the DAG contains a directed subgraph from `S` to `o` with exactly
`k-1` vertices of retained indegree two. Its other nonleaf vertices have
retained indegree one, every nonroot vertex has retained outdegree one, and
its retained leaves are exactly `S`.

Thus in a fan-in-two circuit, `k` incomparable parent-live gates reaching one
output force `k-1` distinct downstream binary reconvergence gates. The theorem
names physical gates; it does not make them expendable or parent preserving
under retargeting.

## Proof

For every vertex that lies on a path from `S` to `o`, choose one outgoing edge
that advances toward `o`; for example, choose an edge that decreases shortest
distance to `o`. Starting at each member of `S`, retain the unique path obtained
by repeatedly following the chosen edge, and let `T` be the union of these
paths.

Every nonroot vertex of `T` has retained outdegree one. Every retained vertex
reaches `o`, so the underlying graph is connected; acyclicity and the unique
successor property make it a rooted tree directed toward `o`. No path from
one member of `S` can enter another member of `S`, because that would make the
two comparable. Conversely, every non-`S` vertex of `T` has an incoming edge
on at least one selected path. Hence the retained indegree-zero vertices are
exactly the `k` members of `S`.

Let `U` and `B` count the retained nonleaf vertices of indegree one and two.
The tree has `k+U+B` vertices and therefore `k+U+B-1` edges. Summing retained
indegrees gives `U+2B` edges, so

```text
U + 2B = k + U + B - 1,
B = k - 1.
```

Original indegree is at most two, so every retained indegree-two vertex is a
physical binary gate. This is the reachability-antichain analogue of the
essential-source count in LEMMA-215; no essential-source premise is used.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite DAG of indegree at most two; application to physical AND/OR/NOT circuit reachability |
| Uniform/non-uniform | Every finite non-uniform DAG, antichain, and common sink |
| Circuit size | Extracted tree has exactly `k-1` distinct retained indegree-two vertices |
| Circuit depth | Unrestricted; selected paths may have arbitrary unary length |
| Fan-in | At most two; original fanout unrestricted, retained nonroot outdegree one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed reachability and finite rooted-tree edge counting |
| Asymptotic quantifiers | Every integer `k>=1`, finite DAG, `k`-vertex reachability antichain, common sink, and selected path union |
| Regime | Exact physical reconvergence-count theorem; not host availability, endpoint minimality, SAT lower bound, or terminal result |
