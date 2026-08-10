# LEMMA-001 — Exponent-ratio invariance under reindexing and padding

**Label: PROVED**

## Statement

Suppose a uniformly indexed family has verifier-time exponents `a(j)>0` and
certified circuit-lower-bound exponents `b(j)>0` in the GATE-002 model.

1. Reindexing by any computable map `j -> h(j)` replaces the ratios by a
   subsequence `b(h(j))/a(h(j))` and cannot turn a globally bounded ratio into
   an unbounded one.
2. Standard polynomial padding `N=(n+j+2)^{q(j)}` with positive, efficiently
   computable `q(j)` changes the usable exponents to at most
   `a'(j)=max(1,a(j)/q(j))` and `b'(j)=b(j)/q(j)`. Hence
   `b'(j)/a'(j) <= b(j)/a(j)` whenever the linear-time floor is relevant, and
   otherwise equality holds.

### Model card

| Field | Value |
|---|---|
| Computational model | Uniformly indexed nondeterministic multitape verifiers and non-uniform general Boolean circuits |
| Uniform/non-uniform | Uniform reindexing/padding; non-uniform circuit lower bounds |
| Circuit size | Source `O(n^{b(j)})`; padded target `O(N^{b(j)/q(j)})` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None for verifiers; arbitrary non-uniform target circuits |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every index and every positive polynomial-padding exponent; fixed index constants absorbed asymptotically |
| Regime | Worst-case exact total-language decision |

## Proof

Reindexing merely selects and repeats existing pairs, so a common upper bound
on all original ratios remains an upper bound after reindexing.

For padding, an original length `n` is represented at length
`N=Theta(n^{q(j)})` for fixed `j`. An original verifier using
`n^{a(j)}` steps runs in `N^{a(j)/q(j)}` steps, subject to at least linear time
for reading an explicit padded input. Conversely, if the padded language had
circuits of size `O(N^d)`, hardwiring the tag and padding would give the source
language circuits of size `O(n^{q(j)d})`. The source lower bound rules this out
only for `q(j)d <= b(j)`, so the transferable padded exponent is
`d=b(j)/q(j)`. Dividing both exponents by `q(j)` preserves the ratio; replacing
the time exponent by one can only reduce it.

## Application

For the Murray-Williams profile `a(k)=c k^4/epsilon`, `b(k)=k`, every
reindexed or polynomially padded profile still has bounded ratio, in fact at
most `epsilon/(c k^3)` along the corresponding original indices. This proves
the scoped reparameterization no-go; it does not constrain new lower-bound
methods with a different exponent profile.
