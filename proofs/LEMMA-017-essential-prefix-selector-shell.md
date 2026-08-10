# LEMMA-017 — prefix essentiality can live in a small selector shell

**Label: PROVED**

## Statement

Let `G(z)` be any nonzero Boolean function, let `p>=2`, and let
`1<=R<=2^(p-2)`. There is a Boolean function `F(x,z)`, with `p` designated
prefix inputs, and `R` pairs of distinct complete prefix assignments such
that:

1. `F` depends essentially on every prefix coordinate;
2. all `2R` restricted functions are exactly `G`, and either pair ORs to `G`;
3. the minimum shared two-output size of every pair is exactly `S(G)`; and
4. `S(F)-S_2(G,G)<=4p-3`.

Thus even essential dependence on every prefix coordinate, exponentially many
candidate pairs, and exact OR reconstruction do not force more than linear-in-
prefix-length function-level parent-to-pair overhead.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted acyclic single- and two-output Boolean circuits; complete assignments to designated prefix inputs |
| Uniform/non-uniform | Fully non-uniform circuits and prefix-pair choice |
| Circuit size | Parent-to-minimum-pair gap at most `4p-3` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every nonzero Boolean function `G`, every `p>=2`, and every `1<=R<=2^(p-2)` |
| Regime | Worst-case exact total Boolean functions; method-specific counterexample |

## Proof

Let `D(x)` be the parity of the `p` prefix inputs and set

`F(x,z)=D(x) AND G(z)`.

For every prefix coordinate, fixing a `z` with `G(z)=1` and flipping that
coordinate flips `F`; hence all prefix coordinates are essential. There are
`2^(p-1)` odd-parity strings. Choose any `2R` of them and pair them
arbitrarily. On each selected prefix, `D=1`, so the residual is exactly `G`
and the OR of either pair is `G`.

With free fanout, a minimum circuit for `G` serves both identical outputs, and
either output of a shared circuit computes `G`. Therefore
`S_2(G,G)=S(G)`. Compute a two-input XOR as

`(a OR b) AND NOT(a AND b)`

using four gates. Chaining `p-1` such XORs computes `D` with `4(p-1)` gates;
one final AND with `G` gives

`S(F)<=S(G)+4(p-1)+1=S_2(G,G)+4p-3`.

This proves the claimed gap. QED.

## Scope

The selected residuals here are identical, whereas SAT's identifier-
conditioned residuals have additional semantic structure. The lemma blocks
only an argument from essential prefix dependence, candidate count, and OR
reconstruction without a quantitative use of that SAT-specific structure.
