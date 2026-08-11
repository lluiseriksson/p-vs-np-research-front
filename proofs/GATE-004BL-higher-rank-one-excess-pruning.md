# GATE-004BL — prune a resource from higher-rank one-excess parents

**Label: PROVED**

Assume `sigma>=2`, `Delta_j=sigma-1`, and let a minimum pruned circuit for
`J_j` have

`N+r=j+1`, `r>=2`.

## Theorem

Some neutral clause restriction leaves `N+r<=j`.

## Position in GATE-004BE

LEMMA-159 excludes rank zero. GATE-004BF, GATE-004BG, and GATE-004BI close
rank one. Thus GATE-004BL is exactly the remaining parent-rank range of the
one-excess pruning gate GATE-004BE.

## Proof

Apply LEMMA-164 to obtain a formula source bit `z` at a core vertex of degree
`d>=2`. Let its formula contain `p` NOT gates. Fixing `z` leaves cycle rank at
most

`r'=r-d+1`.

Apply LEMMA-165 to the source partition.

If no clause is cut, let `a+b=j` count the whole clauses upstream and outside.
Fixing the upstream base leaves shows `p>=a` by LEMMA-119. At the attained
all-upstream-true value of `z`, fix the remaining base leaves to a satisfying
value. The residual computes `W_b` with rank at most `r'`, so LEMMA-139 gives

`N-p>=b-max(r-d,0)`.

Thus `N>=j-max(r-d,0)`. If `r>=d`, this says
`N>=j-r+d`, contradicting `N=j+1-r` because `d>=2`. If `r<d`, it says
`N>=j`, again contradicting `N=j+1-r<=j-1`.

Hence exactly one clause is cut. LEMMA-165 gives no upstream whole clause and
no upstream base input. The source formula depends only on the upstream half
of that clause. Neutralizing the full cut clause makes `z` constant. By
LEMMA-164 the cycle rank drops by at least `d-1>=1`, while the NOT count cannot
increase. Starting from `N+r=j+1`, the restricted resource count is at most
`j`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted implication circuits with one resource excess and cycle rank at least two |
| Uniform/non-uniform | Every individual non-uniform higher-rank parent; uniform symmetric tail |
| Circuit size | Exact `N+r=j+1`, `r>=2`; target restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2` and Boolean restriction semantics |
| Asymptotic quantifiers | Every `j>=2`, `sigma>=2`, and higher-rank parent in the near-maximal descent range |
| Regime | Exact worst-case higher-rank closure of GATE-004BE; not a SAT lower bound or terminal result |
