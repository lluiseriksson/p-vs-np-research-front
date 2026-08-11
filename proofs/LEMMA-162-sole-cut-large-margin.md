# LEMMA-162 — sole-cut pruning above the external-leaf margin

**Label: PROVED**

In the sole-cut setting of GATE-004BI, let `h_Y` be the number of base-input
leaves in the downstream formula. If

`j-1>h_Y+3`,

then some neutral whole-clause restriction leaves `N+r<=j`.

## Proof

Fix the `h_Y` downstream base leaves to a satisfying value, fix both
occurrences of `z` to the attained code that forces the cut clause true, and
fix the single downstream variable belonging to the cut clause. The residual
formula computes `W_{j-1}` on the `j-1` downstream whole clauses.

These are `L=h_Y+3` external leaf occurrences. LEMMA-161 gives at least

`j-1-(h_Y+3)>0`

whole clauses with an original private NOT in the downstream formula. That
region has fanout one in the unicyclic parent. Neutralizing such a clause
deletes its NOT. The remaining cycle rank is at most one, so the parent
resource total falls from `j+1` to at most `j`.

## Model card

| Field | Value |
|---|---|
| Computational model | Sole-cut unicyclic implication circuits and downstream formula external-leaf restrictions |
| Uniform/non-uniform | Every individual non-uniform sole-cut parent satisfying the margin |
| Circuit size | Exact parent `N=j,r=1`; target restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted globally and one downstream |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, tree ancestry, and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2` and every sole-cut factorization with `j-1>h_Y+3` |
| Regime | Exact worst-case large-margin sole-cut closure; boundary cases and full GATE-004BI remain open |
