# LEMMA-168 — a positive upstream tail forces base product factorization

**Label: PROVED**

Suppose an essential one-bit no-bypass factorization of

`J_j=H(X_0,Y_0) AND W_a(X_1) AND W_b(Y_1)`

has no cut implication clause and `a>=1`:

`J_j=F(z(X_0,X_1),Y_0,Y_1)`.

Then there are nonzero Boolean functions `B(X_0)` and `R(Y_0)` such that

`H=B AND R`.

Up to exchanging the two codes of `z`,

`z=B AND W_a`

and

`F(z,Y)=z AND R(Y_0) AND W_b(Y_1)`

on both Boolean values of `z`.

## Proof

Varying `X` produces at most two residual functions of `Y`. Whenever
`W_a(X_1)=0`, the residual is zero. When `W_a(X_1)=1`, the residual is

`H_x(Y_0) W_b(Y_1)`.

Because `H` is nonzero, at least one such residual is nonzero. Zero already
uses one of the two available residuals, so every nonzero `H_x` must be the
same function `R`, and every other `H_x` is zero. Define `B(x)=1` exactly
when `H_x=R`. Then `H=B R`.

By the essential-interface hypothesis, its two codes distinguish the zero
residual from `R W_b`. The code selecting the
nonzero residual is therefore exactly the indicator `B W_a`, and the stated
form of `F` follows. Exchanging codes covers the complementary polarity.

## Model card

| Field | Value |
|---|---|
| Computational model | Essential one-bit factorizations of a base conjoined with disjoint implication products |
| Uniform/non-uniform | Every individual non-uniform factorization; uniform tail family |
| Circuit size | No gate lower bound; exact functional product decomposition |
| Circuit depth | Unrestricted |
| Fan-in | Boolean factorization statement; parent basis AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and residual-function cardinality only |
| Asymptotic quantifiers | Every `a>=1`, `b>=0`, nonzero base `H`, and essential no-cut one-bit factorization |
| Regime | Exact worst-case factorization theorem; false without the positive-upstream-tail premise; not a SAT lower bound or terminal result |
