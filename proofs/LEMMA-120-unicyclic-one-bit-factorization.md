# LEMMA-120 — every unicyclic output cone has a one-bit formula factorization

**Label: PROVED**

Let `C` be a pruned finite Boolean DAG whose connected undirected output-cone
multigraph has cycle rank one. Then its unique undirected cycle consists of
two directed paths from a unique source vertex `s` to a unique sink vertex
`r`. The vertices upstream of `s`, together with `s`, form a fan-out-one
formula `A(X)` computing one bit `z`.

Every gate in `A` has exactly two directed paths to the output, and every gate
outside `A` has exactly one. If `A` contains `h` NOT gates and `C` contains
`q` in total, the computed function factors as

`C(X,Y)=F(A(X),Y)`,

where `F(z,Y)` has a formula with exactly `q-h` NOT occurrences; the input
`z` may occur at two leaves.

## Topology proof

Delete the edges of the unique cycle. Every remaining component is a tree
attached to one cycle vertex. The output is either on the cycle or in the
unique tree attached at some cycle vertex `r`. Since every vertex reaches the
output, every cycle vertex has a directed path along cycle edges to `r`.
The DAG has no directed cycle. Consequently the cycle orientation has `r` as
its unique sink and a unique source `s`; its two arcs are directed from `s`
to `r`. The statement also covers a length-two multicycle of parallel wires.

Every component attached to `s` on the input side is directed toward `s`:
an edge directed away could not return to the output without creating another
undirected cycle. Their union with `s` is therefore an undirected tree with a
unique directed path from every vertex to `s`, hence a formula `A`.

A vertex in `A` reaches the output along the two cycle arcs, while a vertex
outside `A` has only the unique route in its attached tree and then along one
cycle arc or the output tree. An extra route, including one caused by primary
input fanout, would create a second undirected cycle and contradict rank one.

Thus the primary inputs `X` of `A` reach the rest of the circuit only through
`z=s(X)`. Replacing `A` by a fresh input `z` gives the factorization. Unfolding
the remaining cycle duplicates only the leaf `z`; all downstream gates have
one output path. The resulting formula for `F` retains exactly the `q-h` NOT
gates outside `A`.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unicyclic Boolean DAG output cones and fan-out-one factorization |
| Uniform/non-uniform | Every individual non-uniform unicyclic circuit |
| Circuit size | Splits `q` NOT gates into `h` upstream formula NOTs and exactly `q-h` downstream formula NOTs |
| Circuit depth | Unrestricted finite DAG |
| Fan-in | Circuit basis AND/OR two and NOT one; parallel repeated wires allowed as a multigraph |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected graph cycle rank only |
| Asymptotic quantifiers | Every pruned connected output cone with cycle rank exactly one |
| Regime | Exact structural factorization; not a function-specific lower bound or terminal result |
