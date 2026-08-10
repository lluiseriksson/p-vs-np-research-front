# LEMMA-129 — two binary theta splits are parallel or nested

**Label: PROVED**

In the two-binary-split case of LEMMA-127, at least one split vertex is a core
source. Exactly one of the following occurs:

1. both split vertices are core sources (parallel-source case); or
2. exactly one is a core source and the other has one incoming and two
   outgoing core edges (nested-split case).

## Proof

Every finite acyclic orientation has a core source. A source in the theta
2-core has undirected degree two or three. Degree two makes it one of the
outdegree-two split vertices; degree three would make it an outdegree-three
source, the already excluded case of LEMMA-128. Hence at least one of the two
binary splits is a source.

The other split either has core indegree zero and is a second source, or has
degree three with one incoming edge and two outgoing edges. No other indegree
is compatible with outdegree two and core degree at most three.

## Model card

| Field | Value |
|---|---|
| Computational model | Acyclic orientations of two-binary-split theta cores |
| Uniform/non-uniform | Every individual remaining theta-core orientation |
| Circuit size | No gate lower bound; exact parallel/nested orientation dichotomy |
| Circuit depth | Unrestricted finite DAG |
| Fan-in | Original AND/OR two and NOT one; core degree at most three |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed theta topology only |
| Asymptotic quantifiers | Every theta orientation in GATE-004AP |
| Regime | Exact topology theorem; not a Boolean lower bound or terminal result |
