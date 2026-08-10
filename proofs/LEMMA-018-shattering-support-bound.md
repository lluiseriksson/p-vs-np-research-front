# LEMMA-018 — shattering forces support, but only a linear gate count

**Label: PROVED**

## Statement

Let `F:{0,1}^p x {0,1}^m->{0,1}`. Suppose there are fixed prefix strings
`alpha_1,...,alpha_t` and `2^R` suffix strings `y_a`, indexed by
`a in {0,1}^R`, such that the column vectors

`(F(alpha_i,y_a))_{i=1}^t`

are all distinct. Then `F` depends essentially on at least `R` suffix input
coordinates. Every acyclic circuit for `F` over fan-in-two AND/OR and
fan-in-one NOT therefore has at least `R-1` binary gates and at least `R-1`
gates in total.

Applied to ENC-009 with the full bit-length-`ell` identifier block,
`R=2^(ell-1)`, `p=4ell+10`, and the unpadded total input length

`n=(R+1)(4ell+10)-2`,

every circuit for `SAT-gamma_n` has at least `R-1=Omega(n/log n)` gates along
this infinite sequence of lengths.

## Model card

| Field | Value |
|---|---|
| Computational model | Total Boolean functions with a prefix/suffix input partition; unrestricted acyclic Boolean circuits |
| Uniform/non-uniform | Fully non-uniform circuit lower bound at each stated length |
| Circuit size | At least `R-1` binary gates; SAT-gamma corollary `Omega(n/log n)` on explicit lengths |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite `F` satisfying the column hypothesis; SAT corollary for every `ell>=1` and its associated unpadded length |
| Regime | Worst-case exact total-function computation; absolute size only, not average-case, promise, or quotient loss |

## Proof

Let `K` be the set of suffix coordinates on which `F` depends essentially and
write `k=|K|`. Once the prefix is fixed, the full column vector over the
displayed rows is determined by the projection of the suffix onto `K`.
Therefore there are at most `2^k` distinct column vectors. The hypothesis gives
`2^R` of them, so `k>=R`.

Consider the output cone of any circuit for `F` as an undirected connected
graph. Let `s` be its number of input-source vertices, `B` its number of
binary gates, and `U` its number of unary gates. It has `s+B+U` vertices and
`2B+U` incoming circuit edges. Connectedness gives

`2B+U >= s+B+U-1`,

so `B>=s-1`. Every essential coordinate must occur as a source in the output
cone, hence `s>=k>=R` and `B>=R-1`.

For the SAT application, ENC-009 supplies `2^R` distinct complementary
columns at suffix length `R(4ell+10)-2`; adding the conditioned prefix length
`p=4ell+10` gives the displayed `n`. Since `R=2^(ell-1)` and
`n=Theta(R ell)`, while `ell=Theta(log n)`, the bound is
`Omega(n/log n)`. QED.

## Scope

This is an absolute support lower bound. It does not compare a parent circuit
with any conditioned joint quotient, and its graph argument has an at-most-
linear ceiling in the number of input coordinates. It cannot establish
GATE-004 or GATE-004I.
