# LEMMA-038 — fresh tails defeat compressed full-cube shattering loss

**Label: PROVED**

## Statement

For every `d>=1`, put `R=2^d` and let `s in {0,1}^d` index one of `R` suffix
bits `y_s`. With edge bit `q` and suffix bit `w`, define

`B(q,s,y,w)=w AND XNOR(q,y_s)`.

Let `K=C(B)`. For every `m>=1`, add fresh suffix inputs `z_1,...,z_m` and put

`F_m=B AND z_1 AND ... AND z_m`.

Then all of the following hold:

1. `F_m` has minimum unrestricted circuit size exactly `K+m`;
2. the identity embedding of `(q,s)` is a full compressed context cube with
   one unit edge direction and `d=log_2 R` context coordinates;
3. every context pair is adjacent and its two residuals OR to the common
   suffix function `w AND z_1 AND ... AND z_m`;
4. explicit suffix witnesses realize the exact complementary `2^R`-column
   matrix;
5. for either fixed edge polarity, the ambient minimum circuit obtained from
   a minimum circuit for `B` followed by the fresh AND chain has at least `m`
   binary-gate traces depending on `s`; and
6. every context's semantic joint quotient has at least `2m` active classes.

Thus every context has signed loss at most

`(K+m)-2m=K-m`,

which is negative for `m>K`. Taking `m>=R` also satisfies the
`U>=R` trace-region hypothesis of GATE-004P. Hence GATE-004P is false.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted ambient circuits, a full compressed edge/context cube, exact joint quotients, and fresh conjunctive suffix tails |
| Uniform/non-uniform | Explicit function family; `K` is the non-uniform minimum size of the finite XNOR-INDEX base |
| Circuit size | Exact parent size `K+m`; each pair quotient at least `2m`; signed loss at most `K-m` |
| Circuit depth | Base unrestricted; displayed minimum tail adds `m` layers, though the exact size result is depth-independent |
| Fan-in | AND/OR two; NOT one in the base; tail uses AND two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Identity affine embedding over `F_2`; computation is Boolean |
| Asymptotic quantifiers | Every `d>=1`; every `m>=1`; negative loss for `m>K` and all GATE-004P hypotheses for `m>=max(K+1,R)` |
| Regime | Worst-case exact total-function computation; generic counterexample, not SAT-gamma |

## Minimum size and trace region

The base `B` is nonconstant. LEMMA-037 gives

`C(F_m)=C(B)+m=K+m`.

Choose a minimum `K`-gate circuit for `B` and append the `m` fresh AND gates;
this displayed circuit is therefore globally minimum. Since `B` depends on
the context `s`, every appended partial conjunction

`B AND z_1 AND ... AND z_k`

also depends on `s`. These `m` binary labels lie in the fixed-polarity trace
output region, so `U>=m`.

## Common union and shattering

At fixed context `s`,

`B(0,s,.)=w AND NOT y_s`,

`B(1,s,.)=w AND y_s`.

Their OR is `w`, so the two `F_m` branches OR to the context-independent
function `w AND z_1 AND ... AND z_m`.

For `a in {0,1}^R`, take the suffix witness with `y=a`, `w=1`, and every
`z_k=1`. Then

`F_m(q,s,y_a)=1 iff q=a_s`,

which is the exact complementary matrix required by GATE-004P.

## Quotient lower bound

For polarity `b` and tail position `k`, the displayed minimum circuit has the
restricted active residual

`T_{b,k}=w AND [y_s if b=1 else NOT y_s] AND z_1 AND ... AND z_k`.

All `2m` functions are nonconstant and non-input. Within one polarity they
have different essential tail sets; across polarities they have opposite
essential dependence on `y_s`. They are therefore pairwise distinct and all
survive in the semantic joint quotient. Hence `q_s>=2m`, proving the loss
bound. QED.

## Scope

The construction is not SAT-gamma. It proves that compressed full-cube
geometry, shattering, common branch union, ambient minimality, and a large
context trace region still do not imply loss for arbitrary total functions.
The next active gate must use SAT's values on prefix rows outside the affine
cube or another genuinely SAT-specific relation.
