# LEMMA-177 — an exact selector-minimal family retains its resource

**Label: PROVED**

For every `m>=1`, put

`U_m=u_1 OR ... OR u_m`

and

`F_m=NOT(v OR (x AND U_m))`.

Then:

1. the unrestricted AND/OR/NOT circuit size of `F_m` is exactly `m+2`;
2. the minimum possible selector-sensitivity count among minimum circuits is
   exactly `S=3`; and
3. the displayed minimum formula has `N+r=1`, and after every singleton
   restriction `u_i=0` its pruned circuit still has `N+r=1`.

Thus selector-minimality alone does not force a resource loss under any one
of arbitrarily many tail-block neutralizations.

## Exact size

The function has `m+2` essential inputs. A connected output cone therefore
has at least `m+1` binary gates. It is decreasing in `v`, so an AND/OR-only
monotone circuit is impossible and at least one NOT is required. Hence its
size is at least `m+2`. The displayed formula uses an `m-1` gate OR tree,
one AND, one OR, and one NOT, attaining the bound.

## Exact selector sensitivity

Write the two `x`-cofactors as

`A=NOT v`,

`B=NOT(v OR U_m)`.

They are both nonconstant, `B<A` pointwise somewhere, `A` is not constant
one, and `B` is not constant zero. The displayed formula has exactly three
selector-sensitive gates: its final AND, OR, and NOT.

Suppose a circuit had at most two selector-sensitive noninput gates. Its
output is one of them. If it is the first, its cofactor pair has one of the
forms `(1,0)`, `(0,h)`, or `(h,1)` for an `x`-insensitive function `h`, none
of which is `(A,B)`.

Otherwise let `p` be the only earlier sensitive gate. Up to repeated inputs,
its cofactor pair is `(1,0)`, `(0,h)`, or `(h,1)`. The output is `NOT p`,
`p AND k`, or `p OR k` for an insensitive `k`, unless it uses `x` directly,
which yields `(0,p_1)` or `(p_0,1)` and returns to the preceding one-gate
list. Repeating `p` as both binary inputs leaves its pair unchanged. The
possible output pairs have
one of these properties: first cofactor zero or one; second cofactor zero or
one; or first cofactor pointwise at most the second. None matches the strict
nonconstant decreasing pair `(A,B)`. Therefore `S>=3`.

## Stable resource

The displayed formula is a tree with one NOT, so `N+r=1`. Setting any
`u_i=0` merely removes that leaf and its OR attachment. For `m>1` the pruned
formula is the displayed circuit for `F_{m-1}`; for `m=1` it is `NOT v`.
Both retain one NOT and rank zero.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact unrestricted AND/OR/NOT circuit size and selector-sensitive gate functions for an explicit formula family |
| Uniform/non-uniform | Uniform explicit family; lower bounds apply to every non-uniform circuit for each member |
| Circuit size | Exact `m+2`; selector-minimal value exactly three; resource `N+r=1` before and after each `u_i=0` |
| Circuit depth | Unrestricted; displayed OR tree may have arbitrary binary shape |
| Fan-in | AND/OR two; NOT one; fanout unrestricted in lower bounds and one in the witness formula |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, monotonicity, and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every integer `m>=1` and every singleton index `1<=i<=m` |
| Regime | Exact worst-case gadget theorem; tail blocks are not implication pairs and this is not a GATE-004BW counterexample, SAT lower bound, or terminal result |
