# LEMMA-170 — compressing a base-only source preserves resource

**Label: PROVED**

Let an essential no-bypass source formula `A(X)` with `p` NOT gates feed a no-cut
factorization of

`H(X,Y) W_j(T)`

and suppose no tail variable belongs to `X`. Put `z=A(X)`. Then there is a
base function `G(z,Y)` such that

`H(X,Y)=G(A(X),Y)`

and the downstream factor computes exactly `G(z,Y)W_j(T)` on both Boolean
values of `z`.

Replacing `A` by the primary input `z` preserves cycle rank and removes
exactly its `p` NOT gates. Conversely, substituting `A` for `z` in any circuit
for `G(z,Y)W_k` preserves cycle rank and adds exactly `p` NOT gates.

If `A` has at least two primary inputs, the compressed base has strictly fewer
essential inputs than `H`. If it has exactly one input and no NOT gate, a
pruned variable-read-once `A` is that primary input itself.

## Proof

All tail variables lie downstream, so the common factor `W_j(T)` can be
cancelled on assignments where it is one. Since both values of the
nonconstant bit `z` are attained and the downstream factor depends on its
code, define `G(c,Y)` as the corresponding base cofactor. This proves the
functional identities on both codes.

The graph of `A` is a tree attached at its output root. Replacing that tree by
a primary-input vertex, or grafting it back at such a vertex, changes neither
`E-V+1` nor any downstream sharing. It removes or adds precisely the NOT gates
inside `A`.

Every leaf of a pruned variable-read-once AND/OR formula without constants is
essential. Collapsing two or more such leaves to the one essential input `z`
strictly lowers essential base arity. With one leaf, no binary gate can remain
in a pruned tree, so `A` is the input.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned Boolean output cones, base-only no-bypass source formulas, and canonical implication tails |
| Uniform/non-uniform | Every individual non-uniform factorization; uniform tail family |
| Circuit size | Compression subtracts exactly `p` NOTs and preserves rank; substitution reverses it |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted downstream and one inside `A` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=1` and every nonconstant base-only no-bypass source factorization |
| Regime | Exact worst-case compression theorem; not by itself a pruning theorem, SAT lower bound, or terminal result |
