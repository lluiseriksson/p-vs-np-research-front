# LEMMA-128 — the ternary-source theta orientation cannot compute `W_6` with three NOTs

**Label: PROVED**

No theta-core circuit in GATE-004AO whose split budget is realized by one
outdegree-three source can compute `W_6` with three NOT gates.

## One-bit factorization

Let `s` be the unique ternary core source from LEMMA-127. Its attached input
tree together with `s` is a fan-out-one formula `A(X)` computing one bit `z`.
Every path from an input in `X` to the output passes through `s`. All other
core vertices have outdegree one, so replacing `A` by input `z` and unfolding
the three occurrences of that leaf produces a downstream formula `F(z,Y)`.

If `A` contains `h` NOT gates, `F` contains exactly `3-h`. The input set `X`
is nonempty: a gate `s` has predecessors in its attached tree, while a primary
source is itself an input. The bit `z` is nonconstant because every variable
of `W_6` is essential and no input in `X` bypasses `s`. If `s` is itself a
primary input, the same argument applies with `A=z` and `h=0`.

## Cofactor contradiction

Apply LEMMA-121 to `W_6(X,Y)=F(z(X),Y)`.

- With one cut clause, `F` has an attained restriction equal to `W_5`, which
  needs five formula NOTs by LEMMA-119, contradicting `3-h<=3`.
- With no cut clause, let `a+b=6` count the whole clauses in `X` and `Y`.
  LEMMA-121 gives `h>=a` and `3-h>=b`, hence `3>=6`.

Thus the ternary-source orientation is impossible. Every remaining candidate
has exactly two binary split vertices.

## Model card

| Field | Value |
|---|---|
| Computational model | Ternary-source theta-core AND/OR/NOT circuits for fixed `W_6` and one-bit source factorization |
| Uniform/non-uniform | Every individual non-uniform theta candidate with one outdegree-three split |
| Circuit size | Excludes the ternary-source part of `c=2,q=3`; binary count would be 31 |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; source fanout three is unrestricted circuit fanout |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Theta orientation, one-bit cofactors, and formula inversion |
| Asymptotic quantifiers | Fixed `W_6` and every ternary-source theta-core circuit with exactly three NOTs |
| Regime | Exact orientation-stratum exclusion; two-binary-split theta cases remain open |
