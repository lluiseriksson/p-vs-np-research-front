# LEMMA-007 — neutral subcubes can share an arbitrary core

**Label: PROVED**

## Statement

Let `A` be a nonempty subset of `{0,1}^p` with pairwise Hamming distance at
least two, let `r=|A|`, and let `G(z)` be any Boolean function on at least one
input. There is a Boolean function `F(a,w,z)` such that:

1. `F(b,w,z)=G(z)` for every `b in A` and all `(w,z)`;
2. every coordinate of `a` is essential for `F`; and
3. `S(F)-S(G) <= 2pr+5` in the unrestricted fan-in-two AND/OR, fan-in-one NOT
   circuit basis.

Thus `r` separated prefix assignments inducing the same residual function,
even together with essentiality of all prefix coordinates and circuit
minimality, do not generically force a size drop depending on the complexity
of the shared residual core.

## Model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits and coordinate restrictions |
| Uniform/non-uniform | Fully non-uniform circuit complexity; finite set `A` is hardwired |
| Circuit size | Minimum gate count; shared-core shell overhead at most `2pr+5` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | The finite set `A` is part of the function definition, not run-time advice |
| Oracle access | None |
| Field/algebraic model | None; XOR is expanded into four Boolean gates |
| Asymptotic quantifiers | Every `p>=1`, nonempty distance-two set `A`, and positive-arity Boolean function `G` |
| Regime | Worst-case exact total Boolean functions; no promise or distribution |

## Proof

For `b in A`, compute `EQ_b(a)`, which is one exactly when `a=b`, using at
most `p` input negations and `p-1` AND gates, hence at most `2p-1` gates. OR
the `r` equality tests and negate the result. The resulting predicate

`OUT_A(a)=1 iff a notin A`

uses at most

`r(2p-1)+(r-1)+1 = 2pr`

gates. Define

`F(a,w,z)=G(z) XOR (OUT_A(a) AND w)`.

The final AND and four-gate XOR give `S(F)<=S(G)+2pr+5`. For `b in A`,
`OUT_A(b)=0`, so the residual is exactly `G`.

Consequently, after restricting any minimum circuit for `F` by `a=b` and
normalizing constants, the resulting circuit cannot have lost more than
`2pr+5` gates: it computes `G` and therefore has at least `S(G)` gates.

Fix any coordinate `i` and any `b in A`. The distance assumption implies that
the Hamming neighbor `b^i` is not in `A`. With `w=1`, changing `a` from `b` to
`b^i` flips the second XOR input and therefore flips `F`, for every fixed `z`.
Thus every `a_i` is essential. QED.

## Application to LEMMA-006

The neutral-prefix set at length `p=12k` has `r=k+1` and minimum distance six.
LEMMA-007 therefore realizes its entire output-level identity pattern around an
arbitrary shared core with only `O(p^2)` shell overhead. This does not model
SAT's internal gates; it proves that neutral-prefix multiplicity and
essentiality alone cannot supply GATE-004D's collision surplus.
