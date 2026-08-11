# LEMMA-178 — a two-gate implication plateau forces interleaving

**Label: PROVED**

Let `A(Z)` be a nonconstant Boolean function on `e` essential inputs, let
`K=C(A)`, and let `u,t` be fresh. Put

`F(Z,u,t)=A(Z) AND (t OR NOT u)`.

Call a noninput gate pair-sensitive if its Boolean gate function depends
essentially on at least one of `u,t`.

1. Every AND/OR/NOT circuit for `F` has at least three pair-sensitive gates.
2. If `C(F)=K+2`, then every minimum circuit `C` for `F`, under each of the
   satisfying codes `00`, `01`, and `11`, prunes to a minimum `K`-gate
   circuit for `A`, preserves the NOT count and cycle rank separately, and
   deletes exactly two binary gates.
3. Consequently, under the same two-gate hypothesis, at least one
   pair-sensitive gate of `C` survives as a nonconstant base gate under each
   satisfying code. Any compressed realization must interleave the fresh
   pair with the base computation; it cannot be an exposed two-gate shell.

## Three pair-sensitive gates are necessary

Choose `z_1` with `A(z_1)=1`. After fixing all base inputs to `z_1`, the
function becomes `t OR NOT u`, whose exact circuit size is two: essential-
input connectivity requires a binary gate and nonmonotonicity requires a NOT,
while `NOT u` followed by OR with `t` attains the bound.

Suppose the parent had at most two pair-sensitive gates. Pair-insensitive
gates become constants after the full base assignment, so both sensitive
gates must survive and form a minimum two-gate circuit for the implication.
The earlier gate must be `NOT u` and the output gate must OR it with raw `t`;
these are the only possible one-NOT, one-binary realization depending on both
inputs. Their physical predecessors are therefore raw `u,t`, so the parent
output is globally `t OR NOT u`, independent of `Z`. This contradicts a base
assignment `z_0` with `A(z_0)=0`.

## Equality rigidity

Let a minimum parent have size `K+2`. Its essential-input count is `e+2`, so
the connected output-cone identity gives

`N(C)+r(C)=(K+2)-(e+2)+1=K-e+1`.

Fix any satisfying pair code and prune to a circuit `D` for `A`. Restriction
cannot increase `N` or `r`, while every circuit for `A` has

`N(D)+r(D)=|D|-e+1>=K-e+1`.

The two inequalities force equality throughout. Thus `|D|=K`, its NOT count
and rank equal those of `C` separately, and the total gate loss is exactly
two. Since no NOT is lost, both deleted gates are binary. Part 1 supplies at
least three pair-sensitive parent gates, so at least one survives in the
pruned nonconstant output cone for each satisfying code.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT circuits for a nonconstant base conjoined with one fresh implication pair |
| Uniform/non-uniform | Every individual finite non-uniform base and every minimum parent under the stated equality |
| Circuit size | At least three pair-sensitive gates; under `C(F)=K+2`, every satisfying restriction has exact size `K` and deletes two binary gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every nonconstant finite `A`, every fresh pair, every minimum `K+2` parent, and all three satisfying codes |
| Regime | Exact equality-case rigidity; not exclusion of the two-gate plateau, a SAT lower bound, or terminal result |
