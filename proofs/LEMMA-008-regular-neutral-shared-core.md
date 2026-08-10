# LEMMA-008 — the exact neutral family admits a linear shared-core shell

**Label: PROVED**

## Statement

Let `A_k={P_{k,l}:0<=l<=k}` be the ENC-004 neutral-prefix family, let
`p=12k` with `k>=1`, and let `G(z)` be any Boolean function on at least one
input. There is a Boolean function `F(a,w,z)` such that:

1. `F(b,w,z)=G(z)` for every `b in A_k`;
2. every one of the `p` coordinates of `a` is essential for `F`; and
3. `S(F)-S(G) <= 3p+5`.

Hence the exact Hamming geometry, regular parser-state pattern, identical
output residuals, prefix essentiality, and circuit minimality of the ENC-004
family do not generically force a superlinear-in-`p` restriction loss or any
loss depending on the complexity of the shared core.

## Model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits and the explicit ENC-004 prefix set |
| Uniform/non-uniform | Fully non-uniform circuit complexity; `k` is fixed per function |
| Circuit size | Minimum gate count; shared-core shell overhead at most `3p+5` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | The explicit finite prefix family is part of the function definition |
| Oracle access | None |
| Field/algebraic model | None; XOR is expanded into four Boolean gates |
| Asymptotic quantifiers | Every `k>=1` and every positive-arity Boolean core `G` |
| Regime | Worst-case exact total Boolean functions; no promise or distribution |

## Linear recognizer

Write `X=1^12` and `W=01T`. LEMMA-006 gives

`A_k={X^{k-l}W^l:0<=l<=k}`.

Thus a `p`-bit word is in `A_k` exactly when every twelve-bit block is either
`X` or `W` and no `W` block is immediately followed by an `X` block.

For each block, testing equality to `X` costs 11 AND gates. The word `W` has
six zero coordinates, so testing equality to `W` costs six NOT gates and 11
AND gates. One OR tests block validity, for 29 gates per block. The `k-1`
forbidden adjacent pairs, their OR, the final negation, and conjunction with all
block-validity bits use fewer than `3k` further gates. Including one final NOT,
the predicate

`OUT_k(a)=1 iff a notin A_k`

therefore has a circuit of at most `32k <= 3p` gates.

## Shared-core construction

Define

`F(a,w,z)=G(z) XOR (OUT_k(a) AND w)`.

The final AND and XOR cost five gates, so `S(F)<=S(G)+3p+5`. On every
`b in A_k`, `OUT_k(b)=0`, giving residual `G` exactly. Since the family has
minimum Hamming distance six, flipping any single coordinate of any `b in A_k`
leaves the family. Setting `w=1` therefore witnesses essentiality of that
coordinate, exactly as in LEMMA-007.

After restricting a minimum circuit for `F` by any `b in A_k` and normalizing
constants, the result computes `G` and has at least `S(G)` gates. Its loss is
therefore at most `3p+5`. QED.

## Scope

This construction reproduces all audited *output-level* features of the
neutral SAT prefixes but is not SAT-gamma. It rules out a generic cross-table
argument based only on those features. A proof of GATE-004F must use an
additional property of internal gates in minimum SAT circuits.
