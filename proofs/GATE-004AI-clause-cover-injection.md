# GATE-004AI — inject clause indices into negations or cycle coordinates

**Label: PROVED**

Let `C` be a pruned circuit for `W_m`, with `N` NOT gates and cycle rank
`t=B-5m+1`. The `m` clause indices admit an injection into the disjoint union
of the `N` NOT gates and `t` coordinates of a cycle-space basis. Consequently

`m<=N+t`.

## Proof and exact bridge

Fix any spanning tree of the connected output cone. LEMMA-141 proves Hall
expansion for the dependency-cone neighborhoods of all clause-index subsets.
Hall's theorem gives an injection into the NOT gates and non-tree edges. The
fundamental cycles indexed by those non-tree edges form a cycle-space basis,
so the targets have the required form.

Since `t=B-5m+1`,

`N+t>=m iff B+N>=6m-1`.

Thus this is the witness-level version of the proved GATE-004AH. Earlier raw
output transitions and the narrower sensitive neighborhoods did not yield an
injection; full dependency cones do. The theorem does not prove additivity
over an external base, a SAT lower bound, or P versus NP.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for `W_m`, dependency cones, and output-cone cycle-space coordinates |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform clause-indexed matching rule |
| Circuit size | Proved witness inequality `N+t>=m`, equivalent to `B+N>=6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Fundamental cycle basis over `F_2`; finite Hall matching |
| Asymptotic quantifiers | Every `m>=1` and every pruned circuit for `W_m` |
| Regime | Exact worst-case witness theorem for standalone size; not a base direct sum, SAT lower bound, or terminal result |
