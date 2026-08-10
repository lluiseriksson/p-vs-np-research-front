# LEMMA-021 — complementary columns force a large prefix-dependent top region

**Label: PROVED**

## Statement

Let `F:{0,1}^p x {0,1}^m->{0,1}` and let `C` be any acyclic circuit for `F`.
Suppose fixed prefix rows `alpha_1,...,alpha_t` and `2^R` suffix columns `y_a`
give pairwise distinct vectors

`(F(alpha_i,y_a))_{i=1}^t`,

and at least two row residual functions `F(alpha_i,.)` are different.

Call a gate prefix-dependent if its semantic gate function depends on at least
one of the first `p` inputs. Starting at the output, traverse backwards through
prefix-dependent gates only. Stop whenever an incoming node is a prefix input,
a suffix input, or a prefix-independent gate. The stopped suffix inputs and
prefix-independent gates are the suffix-boundary signals of this top region.

Then the top region has at least `R` suffix-boundary signal nodes and at least
`R` prefix-dependent binary gates.

For every fixed `0<c<1`, ENC-009 and ENC-010 give this matrix at every
sufficiently large `SAT-gamma_n` using the full bit-length-`ell` identifier
block, where `ell=floor(c log_2 n)` and `R=2^(ell-1)`. Hence every unrestricted
circuit at those lengths has at least `R=Omega(n^c)` binary gates in its
prefix-dependent top region, not merely somewhere in its suffix-only core.

## Model card

| Field | Value |
|---|---|
| Computational model | Total Boolean functions with prefix/suffix partition; semantic dependence classification inside unrestricted acyclic circuits |
| Uniform/non-uniform | Every individual non-uniform circuit satisfying the matrix hypothesis |
| Circuit size | At least `R` suffix-boundary nodes and `R` prefix-dependent binary gates in the top output region |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; finite column counting and graph connectivity |
| Asymptotic quantifiers | Every finite circuit and row/column family satisfying the hypotheses; every fixed `0<c<1` and all sufficiently large lengths in the SAT corollary |
| Regime | Worst-case exact total-function computation; internal structural count, not quotient loss |

## Proof

Every suffix-boundary node computes a Boolean function of the suffix alone.
Let there be `k` such nodes. Once their `k` values and a prefix row are fixed,
the reduced top region determines the output. Thus the vector over all fixed
rows is determined by a `k`-bit boundary-value vector. There can be at most
`2^k` distinct output columns. The hypothesis supplies `2^R`, so `k>=R`.

The top region's underlying undirected multigraph is connected: every included
gate was reached backwards from the output. Let it contain `B` binary gates,
`U` unary gates, `k` suffix-boundary source nodes, and `a` prefix-input source
nodes. The two distinct row residuals imply that the output depends on the
prefix block, so `a>=1`. The graph has

`k+a+B+U` vertices and `2B+U` incoming circuit edges. Connectedness gives

`2B+U >= k+a+B+U-1`,

hence `B>=k+a-1>=R`.

ENC-009 supplies the required `2^R` complementary columns, and its false/true
row pair for every identifier consists of different residual functions.
ENC-010 pads their common base length to the exact suffix length for every
sufficiently large `n`, because `n^c log n=o(n)` and identifier 1 lies outside
the selected block. The corollary follows. QED.

## Scope

The lemma locates a polynomially large prefix-dependent region when
`ell=Theta(log n)`. It does not show that gates in this region disappear,
collide, or avoid splitting under any conditioned pair. That transfer is
GATE-004J.
