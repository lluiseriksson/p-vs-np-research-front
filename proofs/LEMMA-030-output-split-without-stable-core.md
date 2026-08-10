# LEMMA-030 — an output split need not hit a stable core

**Label: PROVED**

## Statement

There is an explicit unrestricted AND/OR/NOT circuit whose two prefix
cofactors are distinct active non-input functions but which has no
prefix-independent gate label. Consequently its stable-core collision term in
LEMMA-029 is `lambda=0` despite the split output.

## Model card

| Field | Value |
|---|---|
| Computational model | One explicit acyclic Boolean circuit and one complete one-bit prefix restriction pair |
| Uniform/non-uniform | One finite non-uniform circuit; no minimality claim |
| Circuit size | Eight gates; all eight semantic gate functions depend on the prefix bit |
| Circuit depth | Four in the displayed circuit |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | One explicit finite counterexample suffices against the generic output-only implication |
| Regime | Worst-case exact total-function computation; method obstruction, not a SAT-gamma claim |

## Circuit and proof

Let the prefix input be `x`, and put `g=y_1 AND y_2` and
`h=w_1 AND w_2`. Compute the following eight gates:

1. `n=NOT x`;
2. `a_1=x OR y_1`;
3. `a_2=x OR y_2`;
4. `A=a_1 AND a_2`;
5. `b_1=n OR w_1`;
6. `b_2=n OR w_2`;
7. `B=b_1 AND b_2`;
8. `o=A AND B`.

When `x=0`, `A=g`, `B=1`, and `o=g`. When `x=1`, `A=1`, `B=h`, and `o=h`.
Thus the output residuals are the distinct active functions `g` and `h`.

Every displayed parent gate depends semantically on `x`: witnesses are
immediate for `n,a_1,a_2,b_1,b_2`; `A` switches between `g` and one; `B`
switches between one and `h`; and `o` switches between `g` and `h`. Therefore
`I=0`, so `A_j` in LEMMA-029 is empty and `lambda=0`. QED.

## Scope

The circuit is deliberately not claimed minimum and is not a SAT circuit. It
does not refute GATE-004M. It proves only that a split output, even with two
nontrivial cofactors, cannot by itself guarantee a collision with a stable
core. Minimum-circuit optimality and SAT's multi-identifier relations remain
necessary.
