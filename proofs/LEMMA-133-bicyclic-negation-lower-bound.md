# LEMMA-133 — two cycles save at most one NOT gate

**Label: PROVED**

For every fixed `p>=1` and every `m>=2`, any pruned cycle-rank-two circuit
computing either `W_m` or `NOT W_m` contains at least `m-1` NOT gates.

## Core reduction

Let the circuit contain `q` NOT gates. By LEMMA-125 its 2-core is either a
theta, a figure-eight, or a dumbbell.

For a figure-eight or dumbbell, choose a leaf cycle block and its
cycle-separating articulation. The block on the input side is a unicyclic
subcircuit `A(X)` with output bit `z`; replacing it by `z` leaves a downstream
circuit of cycle rank at most one.

For a theta, orient every core edge in the circuit direction and choose a
source vertex `s` of this finite acyclic orientation. The trees feeding `s`
together with `s` form a formula `A(X)` with output `z`. If `s` is an internal
degree-two theta vertex, deleting it breaks one of the two independent cycles;
if it is a degree-three branch vertex, deleting it breaks both. Hence fixing
an attained value of `z`, propagating constants, and pruning leave cycle rank
at most one.

In both topologies every input in `X` reaches the output only through `z`.
The bit is nonconstant because all inputs of `W_m` are essential. Let `h` be
the NOT count in `A`; the residual circuit contains at most `q-h` NOT gates.

## Cofactor costs

Apply the bipolar one-bit dichotomy LEMMA-121.

- If no clause is cut, write `a+b=m` for the whole clauses in `X` and outside
  it. The upstream formula/unicyclic lower bound gives `h>=a`; the attained
  satisfied cofactor leaves the selected polarity of `W_b` in a residual
  formula/unicyclic circuit, so `q-h>=b` by LEMMA-119/123. Thus `q>=m`.
- If one clause is cut, there is no `X`-whole clause. An attained value of `z`
  forces that clause true and leaves the selected polarity of `W_{m-1}` in
  the residual formula/unicyclic circuit. Therefore `q-h>=m-1`, and hence
  `q>=m-1`.

The core classification is exhaustive, proving the theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned cycle-rank-two AND/OR/NOT circuits, core decompositions, and one-bit restrictions |
| Uniform/non-uniform | Every individual non-uniform circuit for either polarity of `W_m` |
| Circuit size | NOT count at least `m-1`; binary gate count unrestricted beyond exact cycle rank two |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2`, Boolean cofactors, and formula/unicyclic inversion |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=2`, and every pruned circuit with cycle rank two |
| Regime | Exact worst-case bicyclic NOT lower bound; not a general circuit-size or terminal result |
