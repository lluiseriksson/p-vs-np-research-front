# LEMMA-032 — adjacent complementary cofactors can retain an arbitrary hard core

**Label: PROVED**

## Statement

Let `G:{0,1}^m->{0,1}` be any nonconstant, non-input Boolean function with
minimum unrestricted AND/OR/NOT circuit size `M`. Define

`F(s,y)=s XOR G(y)`.

Let `S` be the minimum circuit size of `F`, choose any minimum circuit for
`F`, and let `q` be the size of its full semantic joint quotient under the
adjacent restrictions `s=0,s=1`. Then

`S-q<=4`.

The two output cofactors are the distinct active complementary functions
`G` and `NOT G`. Thus adjacency, complementary active cofactors, and parent
minimality alone cannot force loss growing with an arbitrarily hard shared
core.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted Boolean circuits, one prefix bit, and the exact two-output semantic quotient |
| Uniform/non-uniform | Fully non-uniform; one statement for every finite hard-core function `G` |
| Circuit size | Parent-to-joint-quotient loss at most four, independently of `M` |
| Circuit depth | Unrestricted; displayed upper-bound shell adds constant depth |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite nonconstant non-input `G`; arbitrary unbounded sequence of core complexities `M` if such functions are selected by input length |
| Regime | Worst-case exact total-function computation; generic method obstruction, not SAT-gamma |

## Proof

Starting from an `M`-gate minimum circuit for `G`, compute XOR with four gates:

1. `a=s OR G`;
2. `b=s AND G`;
3. `c=NOT b`;
4. `o=a AND c`.

Therefore `S<=M+4`.

Under `s=0`, the output is exactly `G`; under `s=1`, it is `NOT G`. The joint
quotient of any minimum parent circuit is itself a circuit computing both
outputs. Keeping only its `G` output gives a circuit for `G` with no more than
`q` gates. Hence `q>=M`. Combining the inequalities gives

`S-q<=M+4-M=4`.

Both residual outputs are active because `G` is nonconstant and not an input
coordinate, and complementation preserves those properties. QED.

## Scope

The example has only one adjacent edge and may have only a constant number of
prefix-dependent shell gates. It does not refute GATE-004N, whose SAT witness
matrix forces a polynomial prefix-dependent region across many edges. It
proves that adjacency and minimum size alone cannot replace the missing
multi-identifier SAT argument.
