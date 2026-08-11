# LEMMA-215 — essential inputs require binary merges

**Label: PROVED**

Let one output of a finite fan-in-at-most-two Boolean DAG depend essentially
on `N>=1` distinct source signals. Its transitive input cone contains at least
`N-1` binary gates. Consequently an AND/OR/NOT circuit computing that output
has at least `N-1` gates, even with unrestricted fanout and arbitrary NOTs.

## Proof

Choose for every essential source a directed path to the output and take their
union `H`. Prune any edge not used by those paths. Its underlying undirected
graph is connected because every selected path ends at the same output. Write
`U` and `B` for the numbers of unary and binary non-source vertices in `H`.
Every retained non-source vertex has indegree one or two, so `H` has at most
`U+2B` retained edges and can be chosen with exactly its used incoming edges.
A connected graph on `N+U+B` vertices has at least `N+U+B-1` edges. Therefore

```text
U + 2B >= N + U + B - 1,
```

and `B>=N-1`. All vertices of `H` lie in the original output cone, proving
the claim. This argument permits reconvergence and arbitrary fanout.

The lemma is only an arity bound. It gives no superlinear circuit lower bound
and does not distinguish formulas from DAGs beyond the essential-source count.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite Boolean DAG with unary and binary gates; application to constant-free AND/OR/NOT circuits |
| Uniform/non-uniform | Every finite non-uniform circuit and chosen output |
| Circuit size | At least `N-1` binary gates in the output cone when `N` sources are essential |
| Circuit depth | Unrestricted |
| Fan-in | At most two; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed dependency graph and component merging |
| Asymptotic quantifiers | Every integer `N>=1`, every finite DAG, and every set of `N` essential source signals |
| Regime | Exact worst-case arity lower bound; not a superlinear lower bound, SAT lower bound, or terminal result |
