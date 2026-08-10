# LEMMA-130 — parallel theta sources cannot compute `W_6` with three NOTs

**Label: PROVED**

No candidate in GATE-004AP with two parallel core sources computes `W_6`.

## Exact formula budget

Let the two source trees compute `z_1=A_1(X_1)` and `z_2=A_2(X_2)`, with
`h_1,h_2` NOT gates. The attached trees and input sets are disjoint; an edge
between them would create an additional core path. All remaining core vertices
have outdegree one.

Replacing both source trees by inputs and unfolding their two uses gives a
formula `F(z_1,z_2,Y)` with exactly `3-h_1-h_2` NOT gates. The full unfolding
has exactly `3+h_1+h_2` NOT occurrences. LEMMA-119 requires at least six, so

`h_1+h_2=3`

and the downstream formula `F` contains no NOT gate.

## Negative inputs cannot be downstream

The NOT-free formula `F` is monotone nondecreasing in every `Y` input. Each
`u_i` is an essential decreasing input of `W_6`, while neither source bit
depends on a variable placed in `Y`. Therefore all six negative inputs
`u_i` lie in `X_1 union X_2`.

## Per-source cofactor charge

For each `j`, regard all variables outside `X_j` as the other side of the
factorization through the one bit `z_j`. LEMMA-121 applies separately.

- If no clause is cut by `X_j`, every negative input in `X_j` belongs to an
  `X_j`-whole clause. If there are `n_j` such inputs, the source formula needs
  `h_j>=n_j` NOT gates.
- If a clause is cut by `X_j`, it is the only touched clause and there is no
  `X_j`-whole clause. Hence `X_j` contains at most one negative input:
  `n_j<=1`.

If neither source cuts a clause, then
`6=n_1+n_2<=h_1+h_2=3`. If one cuts, the other covers at most its `h_j<=3`
whole negative inputs, so the total is at most four. If both cut, the total is
at most two. Every case contradicts the six negative inputs. Thus the parallel
orientation is impossible.

## Model card

| Field | Value |
|---|---|
| Computational model | Parallel-source theta-core circuits, independent source formulas, and a NOT-free downstream formula |
| Uniform/non-uniform | Every individual non-uniform parallel-source candidate for fixed `W_6` |
| Circuit size | Excludes the parallel part of `c=2,q=3`; all three NOTs would have to lie in source trees |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed theta topology, one-bit cofactors, and formula inversion |
| Asymptotic quantifiers | Fixed `W_6` and every parallel two-source theta circuit with three NOT gates |
| Regime | Exact orientation-stratum exclusion; nested split remains open |
