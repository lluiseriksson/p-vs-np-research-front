# LEMMA-172 — nonzero primary cofactors preserve the equality resources

**Label: PROVED**

Assume a GATE-004BR parent with

`N=j+2-r`, `r>=2`,

and degree-two primary source `x`. Let `c` be a value for which the base
cofactor `H_c` is nonzero. Fix `x=c`, then fix the remaining base inputs to
any satisfying assignment of `H_c`, propagate constants, and prune. If the
resulting `W_j` circuit has `q` NOT gates and rank `rho`, then

`q=N`.

If `r>=3`, also

`rho=r-1`.

Thus no NOT is lost under any such satisfying cofactor restriction, and for
rank at least three no cycle-rank unit is lost beyond the one forced by the
degree-two source.

## Proof

LEMMA-164 gives `rho<=r-1`, and restriction gives `q<=N`.

For `r=2`, LEMMA-139 at residual rank zero or one gives `q>=j`. Here
`N=j`, so `q=N`.

Let `r>=3`. Residual rank zero would require `q>=j>N`. For positive residual
rank, LEMMA-139 gives

`q>=j-rho+1>=j-(r-1)+1=j+2-r=N`.

Hence `q=N`. Equality in the second inequality forces `rho=r-1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned two-excess implication circuits under a primary-source cofactor and satisfying-base restriction |
| Uniform/non-uniform | Every individual non-uniform GATE-004BR parent; uniform tail product |
| Circuit size | Exact surviving `q=j+2-r`; exact residual rank `r-1` for `r>=3` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary source fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2`, `r>=2`, every nonzero primary cofactor, and every satisfying assignment of it |
| Regime | Exact worst-case equality rigidity; not neutral-clause pruning, a SAT lower bound, or terminal result |
