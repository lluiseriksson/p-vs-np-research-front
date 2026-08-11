# GATE-004BI — prune the sole-cut unicyclic partition

**Label: EXPLORATORY**

Assume the GATE-004BG parent is in LEMMA-160's sole-cut case. There are no
upstream whole clauses, all `j-1` other clauses are downstream, and the
upstream formula has at most one NOT.

## Falsifiable theorem

In the operational range `j>K+sigma-1`, prove that some neutral clause
restriction leaves `N+r<=j`.

A compatible minimum sole-cut unicyclic parent preserving all resources under
every neutral clause restriction falsifies the theorem.

## Remaining quantitative edge

Fixing the downstream base leaves, both occurrences of `z`, and the
downstream half of the cut clause leaves a formula for `W_{j-1}`. LEMMA-161
therefore gives private whole-clause NOTs whenever

`j-1>h_Y+3`.

LEMMA-162 proves closure for all instances satisfying that inequality. At the
boundary allowed by `j>=K+sigma` and `h=K+1-sigma`, only a constant-width gap
remains, most notably `sigma=2`. The next audit must exploit that the two `z`
leaves carry the same bit and that the cut-clause half is not an arbitrary
external leaf.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unicyclic implication circuits in the sole-cut one-bit factorization |
| Uniform/non-uniform | Every individual non-uniform sole-cut parent; uniform clause family |
| Circuit size | Exact `N=j,r=1`; downstream `j-1` whole clauses; target restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted with one cycle |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, formula external-leaf defects, and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `sigma>=2` and `j>K+sigma-1` in the sole-cut stratum |
| Regime | Falsifiable worst-case remaining branch of GATE-004BG; not full GATE-004BE/BD/BA, a SAT lower bound, or terminal result |
