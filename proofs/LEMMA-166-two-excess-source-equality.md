# LEMMA-166 — exact source cases at resource excess two

**Label: PROVED**

Let a minimum pruned circuit for `J_j` satisfy

`N+r=j+2`

under the GATE-004BM premise `sigma>=3`. Apply LEMMA-164 at a core source of
degree `d`, and apply LEMMA-165 to its one-bit factorization.

Then rank zero is impossible. A sole-cut partition always has a neutral
clause restriction that lowers `N+r` by at least one. In a no-cut partition,
the only cases not contradicted by LEMMA-119/139 are:

1. `r=1,d=2`, with one aggregate unit of slack;
2. `r>=2,d=2`, with equality in both regional NOT lower bounds; or
3. `r=2,d=3`, again with equality in both regional NOT lower bounds.

## Proof

If `r=0`, the circuit is a formula with `j+2` NOT gates. LEMMA-159 with
`s=2` gives `sigma<=2`, contradicting `sigma>=3`.

In a sole-cut partition, LEMMA-165 gives no upstream whole clause and no
upstream essential base input. Neutralizing the cut makes the source bit
constant, and LEMMA-164 lowers rank by at least `d-1>=1`; NOT count cannot
increase. Hence the restricted resource is at most `j+1`.

Now suppose no clause is cut. Write `a+b=j` and let the source formula contain
`p` NOT gates. Exactly as in GATE-004BL,

`p>=a`

and

`N-p>=b-max(r-d,0)`.

If `r>=d`, summing gives `N>=j-r+d`. Since `N=j+2-r`, necessarily `d<=2`.
Core degree gives `d=2`, and equality of the sums forces equality in both
regional bounds.

If `r<d`, connectedness after source deletion in LEMMA-164 gives
`r-d+1>=0`, so `d=r+1`. The lower bound is `N>=j`, whereas
`N=j+2-r`; hence `r<=2`. For `r=1` this leaves one aggregate unit of slack
and `d=2`. For `r=2` it forces `d=3` and equality in both regional bounds.
These are all cases.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted implication circuits, cyclic core sources, and one-bit residual partitions |
| Uniform/non-uniform | Every individual non-uniform two-excess parent; uniform symmetric tail family |
| Circuit size | Exact parent `N+r=j+2`; sole-cut target at most `j+1`; exact surviving no-cut cases |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2`, Boolean cofactors, and integer resource inequalities |
| Asymptotic quantifiers | Every `j>=2`, `sigma>=3`, and compatible minimum two-excess parent |
| Regime | Exact worst-case necessary classification for GATE-004BM; not pruning of every no-cut case, a SAT lower bound, or terminal result |
