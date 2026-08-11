# LEMMA-233 — a fixed marked core can have unbounded parent-live ports

**Label: PROVED**

For every `m>=1` there is a finite constant-free single-output AND/OR circuit
with a fixed three-gate marked cyclic core and `m` distinct exterior fanout
ports from one core gate, each observable on an unmasked parent slice.

## Construction

Use raw inputs `x,y,s_0` and `z_i,s_i` for `1<=i<=m`:

```text
g   = x AND y,
h   = x OR y,
k   = g OR h,
p_i = g AND z_i,
d_0 = s_0 AND k,
d_i = s_i AND p_i,
F   = OR(d_0,d_1,...,d_m).
```

The marked core `{g,h,k}` and its six incident core edges are independent of
`m`. Forgetting direction and including raw sources `x,y`, it has connected
cycle rank `6-5+1=2`. Gate `g` has the core consumer `k` plus the `m` distinct
exterior consumers `p_i`. The full circuit has `3m+4` gates using a binary OR
tree at the output.

Every port is parent-live. Set `s_i=1` and all other selectors, including
`s_0`, to zero; then `F=p_i`. Neither incoming signal can replace that port:
`g=1,z_i=0` distinguishes `p_i` from `g`, while `g=0,z_i=1` distinguishes it
from `z_i`.

A selector-dependent replacement could remain masked outside `s_i=1`; this
lemma does not exclude a certified joint rewrite. It proves that bounded
marked-core size alone neither bounds the number of external ports nor makes
their consumer gates free. The family is deliberately nonminimal and is not
an endpoint.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform family of finite single-output constant-free unrestricted AND/OR DAGs with a marked cyclic core and external ports |
| Uniform/non-uniform | Uniform construction for every `m>=1`; each member finite and non-uniform |
| Circuit size | `3m+4`; marked core exactly three gates and exterior ports `m` |
| Circuit depth | Unrestricted final OR-tree depth; local core/port depth constant |
| Fan-in | AND/OR two; NOT unused; core gate `g` has fanout `m+1` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions, selector isolation, and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `m>=1`, every assignment, every port index, and both displayed input substitutions |
| Regime | Exact bounded-core/unbounded-port theorem; not a minimum endpoint, SAT lower bound, or terminal result |
