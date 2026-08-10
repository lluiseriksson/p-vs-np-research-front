# GATE-004AJ — match binary birth events to negations or cycles

**Label: EXPLORATORY**

## Falsifiable theorem

For each clause index `i`, choose a first binary birth node `b_i` supplied by
LEMMA-114. Prove that the `m` indexed birth events `(i,b_i)` can be matched
injectively to the disjoint resource set consisting of the circuit's `N` NOT
gates and `t` coordinates of an output-cone cycle-space basis.

Equivalently, prove a representation-independent tracing rule which assigns
each clause index one such resource and never reuses a resource. A circuit
with `N+t<m`, or an unavoidable collision for every choice of first nodes and
cycle basis, falsifies the theorem.

## Bridge

An injection gives `m<=N+t`. By GATE-004AI and
`t=B-5m+1`, this is exactly `B+N>=6m-1`, the standalone tradeoff in
GATE-004AH. It remains only a prerequisite to the larger minimum-quotient and
SAT bridges.

## Current attempt

The cofactor difference first acquires `u_i`-dependence at `b_i`. Directly
charging `b_i` as a NOT gate fails categorically: LEMMA-114 proves it is
binary. The next viable trace must follow both input cones and the path to the
output, charging either a polarity-changing NOT elsewhere or a reconvergence
whose independent cycle coordinate prevents a formula-local charge.

What remains unproved is the collision bound: one NOT or one cycle coordinate
must not discharge two different clause indices. This is the precise internal
bounded-reuse brick.

LEMMA-115 and GATE-004AK now instantiate a concrete admissibility relation
using assignment-sensitive NOT gates and non-tree edges. Singleton
neighborhoods are nonempty, but the range-free Hall property is false; the
remaining proof must exploit `N<=m-1` to obtain expansion for larger subsets.

The refined GATE-004AL uses full block dependency cones instead. LEMMA-116
establishes its Hall inequalities for every subset of size at most four;
quintets are the first open collision pattern.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits, node cofactor differences, and output-cone cycle-space coordinates |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform clause-indexed witness rule |
| Circuit size | Target injection implies `N+t>=m`, exactly equivalent to `B+N>=6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor comparison and undirected cycle space over `F_2` |
| Asymptotic quantifiers | Every `m>=5`, every pruned circuit in the unresolved inversion range, and every clause index |
| Regime | Exact worst-case internal-witness gate; not a base direct sum, SAT lower bound, or terminal result |
