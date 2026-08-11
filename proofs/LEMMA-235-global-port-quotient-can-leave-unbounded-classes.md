# LEMMA-235 — the global port quotient can leave unbounded classes

**Label: PROVED**

For every `m>=1`, the LEMMA-233 diagnostic family has `m` exterior port gates

```text
p_i=(x AND y) AND z_i
```

whose global Boolean functions are pairwise distinct. Hence quotienting that
displayed circuit by exact global gate-function equality leaves at least `m`
distinct port-function classes.

## Proof

For `i!=j`, assign `x=y=1`, `z_i=1`, and `z_j=0`. Then `p_i=1` and `p_j=0`.
Thus no two port functions agree. Each is nonconstant. LEMMA-005 may remove
other duplicate or dead gates in the deliberately nonminimal family, but it
cannot merge these `m` named port gates by function equality.

This is not a lower bound on the minimum circuit for the parent: another
circuit need not materialize the same intermediate functions. It proves only
that the already established global-equality quotient does not bound port
classes as a function of marked-core size.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform LEMMA-233 constant-free AND/OR family under exact global semantic gate quotient |
| Uniform/non-uniform | Uniform construction for every `m>=1`; each member finite and non-uniform |
| Circuit size | Displayed size `3m+4`; at least `m` distinct named port-function classes remain |
| Circuit depth | Unrestricted final OR-tree depth |
| Fan-in | AND/OR two; NOT unused; core fanout `m+1` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact global Boolean functions and semantic quotient classes |
| Asymptotic quantifiers | Every `m>=1` and every distinct pair of port indices |
| Regime | Exact quotient-class lower witness for the displayed circuit; not parent circuit minimality, SAT lower bound, or terminal result |
