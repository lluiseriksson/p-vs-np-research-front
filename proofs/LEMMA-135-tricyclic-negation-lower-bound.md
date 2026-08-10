# LEMMA-135 — three cycles save at most two NOT gates

**Label: PROVED**

For every fixed `p>=1` and every `m>=3`, any pruned cycle-rank-three circuit
computing either `W_m` or `NOT W_m` contains at least `m-2` NOT gates.

Let the circuit have `q` NOT gates and let `K` be its undirected 2-core.

## Case 1: a cycle-separating articulation

Suppose an articulation `s` separates a nonempty cyclic region from the
output side. Choose an outermost such region in the block-cut tree. The
subcircuit on that side, including `s`, computes a nonconstant bit `z=A(X)`;
replacing it by input `z` leaves a downstream circuit `D(z,Y)`. Cycle ranks
add across a one-vertex sum, so the two ranks are `r` and `3-r` for
`r in {1,2}`. Both factors therefore have cycle rank at most two.

Apply LEMMA-121. If one clause is cut, fixing the attained value that forces
it true leaves the selected polarity of `W_{m-1}` downstream. LEMMA-119,
LEMMA-123, and LEMMA-133 give at least `m-2` downstream NOT gates for residual
rank zero, one, or two respectively.

If no clause is cut, write `a+b=m`. The factor of rank at most one costs at
least its full clause count by LEMMA-119/123; the rank-two factor costs at
least its clause count minus one by LEMMA-133. The empty and one-clause
boundary cases only strengthen this statement by constancy or Markov's
bound. Hence the two disjoint NOT budgets sum to at least `m-1`, and in
particular `q>=m-2`.

## Case 2: a 2-connected core

Assume `K` has no articulation. Orient its edges in the circuit direction and
choose a source vertex `s` of this finite acyclic orientation. The trees
feeding `s` together with `s` form a formula `A(X)` with output bit `z` and
`h` NOT gates. Every input in `X` reaches the output only through `z`.

The core has minimum degree two. Because it is 2-connected, deleting `s`
leaves it connected. If `d` is the core degree of `s`, the residual cycle
rank before further pruning is

`3-d+1 = 4-d <=2`.

Fixing an attained value of `z`, propagating constants, and pruning cannot
increase this rank and leaves at most `q-h` NOT gates.

Apply LEMMA-121 again. With one cut clause, the residual selected polarity of
`W_{m-1}` has rank at most two and therefore needs at least `m-2` NOT gates.
With no cut clause, the upstream formula costs `a` NOTs and the residual
rank-at-most-two circuit costs at least `b-1` for `a+b=m`; the cases `b<=1`
are at least as strong by direct formula/Markov bounds. Thus `q>=m-1` in the
uncut case and `q>=m-2` in the cut case.

The two cases exhaust the core, proving the theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned cycle-rank-three AND/OR/NOT circuits, block-cut decompositions, and core-source restrictions |
| Uniform/non-uniform | Every individual non-uniform circuit for either polarity of `W_m` |
| Circuit size | NOT count at least `m-2`; binary gate count unrestricted beyond exact cycle rank three |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2`, vertex sums, Boolean cofactors, and lower-rank inversion |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=3`, and every pruned circuit with cycle rank three |
| Regime | Exact worst-case tricyclic NOT lower bound; not a general circuit-size or terminal result |
