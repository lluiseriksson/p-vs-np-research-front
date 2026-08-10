# LEMMA-126 — a bicyclic three-NOT circuit for `W_6` must have theta core

**Label: PROVED**

No pruned cycle-rank-two, three-NOT circuit for `W_6` can have a figure-eight
or dumbbell 2-core. Consequently every candidate in GATE-004AN must have a
theta core.

## Articulation factorization

By LEMMA-125, either non-theta core has a leaf cycle block separated from the
output side by one articulation vertex `s`. Because every gate reaches the
output, both arcs of that leaf cycle are directed toward `s`. The leaf block,
all trees feeding it, and `s` form a pruned unicyclic subcircuit `A(X)` whose
output bit `z` is the only route from its primary inputs to the rest. Replacing
it by input `z` leaves a downstream circuit `D(z,Y)` of cycle rank at most one.

Let `h` be the NOT count in `A`; the downstream circuit has `3-h` NOT gates.
The bit `z` is nonconstant because every input variable of `W_6` is essential
and variables in `X` have no bypass around the articulation.

## Cofactor contradiction

Apply the bipolar one-bit dichotomy LEMMA-121 to
`W_6(X,Y)=D(z(X),Y)`.

- If one clause is cut, there is no `X`-whole clause. Fixing the attained
  value of `z` that forces the cut clause leaves `W_5` in the downstream
  circuit. A formula downstream needs five NOTs by LEMMA-119, and a
  cycle-rank-one downstream circuit needs five by LEMMA-123. Both contradict
  its count `3-h<=3`.
- If no clause is cut, let `a+b=6` count whole clauses in `X` and `Y`. The
  upstream subcircuit computes `W_a` or its complement, so LEMMA-123 gives
  `h>=a`. Fixing `z` to the satisfied code makes the downstream circuit
  compute `W_b`; LEMMA-119 or LEMMA-123 gives `3-h>=b` according as its cycle
  rank is zero or one. Hence `3>=a+b=6`, a contradiction.

Thus both cactus topologies are impossible.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned bicyclic AND/OR/NOT circuits for fixed `W_6`, block-cut cores, and one-bit articulation factors |
| Uniform/non-uniform | Every individual non-uniform candidate with figure-eight or dumbbell core |
| Circuit size | Excludes `c=2,q=3` on both cactus core types; binary count would be 31 |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected block-cut topology, one-bit cofactors, and Boolean-lattice inversion |
| Asymptotic quantifiers | Every pruned circuit computing fixed `W_6` with cycle rank two, three NOTs, and non-theta core |
| Regime | Exact structural exclusion of cactus cases; theta core and larger gates remain open |
