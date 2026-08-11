# LEMMA-219 — restriction-lost gates can remain parent-essential

**Label: PROVED**

For every `m>=1` there is a constant-free single-output AND/OR/NOT circuit
with exactly `m` named binary gates deleted when one raw input is fixed to
zero, while substituting those gates by their zero-cofactors changes the
unrestricted parent function.

## Construction

Use raw inputs `v` and `x_i,z_i,s_i` for `1<=i<=m`. Define

```text
e_i = v OR x_i,
a_i = e_i AND z_i,
d_i = s_i AND a_i,
F   = OR_i d_i
```

with a binary OR tree for the final disjunction. The circuit has `4m-1`
gates.

At `v=0`, each `e_i` becomes the wire `x_i` and is deleted. Every `a_i` becomes
`x_i AND z_i`, every `d_i` remains a nonconstant binary AND, and every OR-tree
gate remains nonconstant: assign its two subtrees independently through their
selectors. Hence exactly the `m` gates `{e_i}` disappear under this
restriction.

Yet globally replacing every `e_i` by its zero-cofactor `x_i` changes the
parent. For any chosen `i`, set `v=1`, `x_i=0`, `z_i=s_i=1`, and all other
selectors zero. The original output is one through `e_i=1`; the specialized
replacement output is zero. Thus every named lost gate is parent-essential to
the displayed interface.

For `m=2`, one restriction loses exactly two binary gates and neither is a
free parent-level host. The family is deliberately nonminimal and makes no
plateau claim.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform family of finite single-output constant-free AND/OR/NOT DAGs |
| Uniform/non-uniform | Uniform construction for every `m>=1`; each member finite and non-uniform |
| Circuit size | `4m-1`; exactly `m` named binary gates lost at `v=0` |
| Circuit depth | OR tree may be balanced or arbitrary; unrestricted ambient depth |
| Fan-in | AND/OR two; NOT unused; named gates have fanout one and final tree fanout one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean restriction, constant propagation, and selector isolation |
| Asymptotic quantifiers | Every `m>=1`, every assignment, and each named gate `e_i` |
| Regime | Exact restriction-versus-parent theorem; not a minimum endpoint, SAT lower bound, or terminal result |
