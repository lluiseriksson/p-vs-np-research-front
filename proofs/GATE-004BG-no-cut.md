# GATE-004BG-NO-CUT — prune the unicyclic no-cut partition

**Label: PROVED**

Assume the GATE-004BG parent is in LEMMA-160's no-cut case, with `a`
`X`-whole clauses upstream and `b=j-a` `Y`-whole clauses downstream. In the
operational descent range

`j>K+sigma-1`, `sigma>=2`,

some neutral clause restriction leaves `N+r<=j`.

## Proof

Let `h_X,h_Y` be the numbers of essential base-input leaves in the upstream
and downstream formula regions. The one-bit factorization partitions the
base inputs, so

`h_X+h_Y<=h`.

LEMMA-160 gives exactly `a` upstream and `b` downstream NOT gates.

Fix the upstream base leaves as in LEMMA-160. The upstream residual computes
`W_a` or its complement. Apply LEMMA-161 with `L=h_X`: if `a>h_X`, an
upstream clause has a private original NOT.

For the downstream formula, fix its base leaves and the two occurrences of
the duplicated input `z` to the attained all-upstream-true code. The residual
computes `W_b`. Apply LEMMA-161 with `L=h_Y+2`: if `b>h_Y+2`, a downstream
clause has a private original NOT.

If neither inequality held, then

`j=a+b<=h_X+h_Y+2<=h+2`.

But `sigma=K-h+1`, so `h+2=K+3-sigma`. The operational range gives the
integer bound `j>=K+sigma`, and for `sigma>=2`,

`K+sigma>K+3-sigma`.

Contradiction. Thus one side has a clause-private NOT. Its gate lies in a
fanout-one formula region of the unicyclic factorization. Neutralizing that
clause deletes the NOT; the remaining cycle rank is at most one. Starting
from `N=j,r=1`, the restricted resource count is at most `j`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unicyclic implication circuits in the no-cut one-bit factorization and formula external-leaf restrictions |
| Uniform/non-uniform | Every individual non-uniform no-cut parent in the uniform clause family |
| Circuit size | Exact parent `N=j,r=1`; restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted globally and one in each factor formula region |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, formula-tree ancestry, and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `sigma>=2` and every integer `j>K+sigma-1` in the no-cut unicyclic stratum |
| Regime | Exact worst-case closure of the no-cut branch of GATE-004BG; sole-cut branch and GATE-004BF remain open |
