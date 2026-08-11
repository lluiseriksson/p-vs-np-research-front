# LEMMA-220 — a functionally sealed frontier preserves the parent

**Label: PROVED**

Let `C` and `C'` be finite acyclic AND/OR/NOT circuits on the same raw inputs.
Let `X` be a set of gates containing every physical vertex whose operation or
incoming edges are retargeted. Assume every edge leaving `X` enters a gate in
a finite exterior frontier `S`, and that each `s in S` computes exactly the
same Boolean function in `C'` as in `C`. Then every gate outside `X` that is
downstream of `S`, including the parent output, computes its old function.

## Proof

Order the exterior gates topologically. Frontier functions agree by
hypothesis. Consider the first downstream exterior gate not in `S`. All of its
inputs come from unchanged exterior predecessors or from frontier gates whose
functions agree; no edge can arrive directly from `X` because every such edge
ends in `S`. Applying the same Boolean operation gives the same function.
Induction proves equality at every later exterior gate and the output.

Consequently a host rewrite may change arbitrarily many immediate consumers
provided the entire changed region is included in `X` and its first exterior
frontier is functionally sealed. If the replacement uses no more physical
gates and does not increase `W,Q`, a strict size, potential, or `R_0` decrease
gives the usual refined-endpoint contradiction. The lemma itself asserts no
bound on the depth or size of `X` and no existence of a seal.

## Model card

| Field | Value |
|---|---|
| Computational model | Two finite constant-free unrestricted AND/OR/NOT DAGs related by a marked replacement region |
| Uniform/non-uniform | Every finite non-uniform circuit pair satisfying the sealed-frontier interface |
| Circuit size | No intrinsic bound; application requires replacement size no larger than the marked old region |
| Circuit depth | Unrestricted; changed-region depth finite but unbounded |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and every exit from `X` audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean gate functions and DAG topological induction |
| Asymptotic quantifiers | Every finite circuit pair, changed region, frontier gate, and downstream vertex |
| Regime | Exact worst-case interface theorem; not seal existence, SAT lower bound, or terminal result |
