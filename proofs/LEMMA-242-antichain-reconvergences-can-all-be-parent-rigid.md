# LEMMA-242 — every forced antichain reconvergence can be parent-rigid

**Label: PROVED**

For every `k>=2` there is a finite constant-free single-output AND/OR circuit
with `k` pairwise reachability-incomparable parent-live gates and exactly
`k-1` binary gates in a selected common-output reconvergence tree, such that
every one of those merge gates is parent-live and neither of its two inputs
can replace it while the rest of the displayed circuit is held fixed.

## Construction and proof

Use independent raw pairs `(x_i,y_i)` and define

```text
p_i = x_i AND y_i                         (1<=i<=k),
r_2 = p_1 OR p_2,
r_j = r_{j-1} OR p_j                      (3<=j<=k),
F   = r_k.
```

The gates `p_1,...,p_k` form an antichain. Their selected paths to `F` form
the displayed comb, whose merge gates are exactly `r_2,...,r_k`, hence exactly
`k-1`; this attains LEMMA-241's count.

Every `p_i` is parent-live: make its raw pair one and every other pair zero,
so `F=p_i=1`. For a merge `r_j`, first set `p_j=1` and all earlier and later
terms zero. Then `r_j=1` while its left input `r_{j-1}=0`, and this difference
reaches `F`. Conversely set `p_1=1`, `p_j=0`, and all other terms zero. Then
`r_j=1` while its right input `p_j=0`, again with the difference reaching
`F`. Thus neither input is a valid wire substitution for any merge.

The assignments are realizable because each `p_i` has its own raw pair. The
construction is a physical diagnostic and makes no claim that the displayed
single-output circuit is minimum. Repeating it unchanged on four fresh code
rows does not alter the identities.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform family of finite constant-free single-output AND/OR DAGs with an antichain and comb reconvergence tree |
| Uniform/non-uniform | Uniform construction for every `k>=2`; each circuit finite and non-uniform |
| Circuit size | `k` antichain AND gates plus exactly `k-1` OR reconvergence gates |
| Circuit depth | Comb output depth `k`; no minimum-depth claim |
| Fan-in | AND/OR two; NOT unused; antichain fanout one and merge fanout one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions, physical reachability, and rooted-tree merge count |
| Asymptotic quantifiers | Every `k>=2`, antichain gate, merge gate, and both displayed separating assignments |
| Regime | Exact tight parent-rigid reconvergence diagnostic; not a minimum endpoint, SAT lower bound, or terminal result |
