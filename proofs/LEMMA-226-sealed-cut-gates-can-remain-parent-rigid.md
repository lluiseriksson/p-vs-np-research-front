# LEMMA-226 — sealed cut gates can remain live at the parent interface

**Label: PROVED**

For every `m>=1` there is a constant-free single-output AND/OR/NOT circuit
with `m` one-sided support-mask seals after a rewrite, while every seal must
retain its displayed function on an unmasked selector slice, neither incoming
signal can replace it, and all seals share one physical mask signal.

## Construction

Use fresh inputs `u,t`, base inputs `w`, and `x_i,s_i` for `1<=i<=m`:

```text
n   = NOT t,
q   = u AND n,
b   = q OR w,
a_i = x_i OR q,          a'_i = x_i,
c_i = a_i OR b,
d_i = s_i AND c_i,
F   = OR_i d_i.
```

The old circuit has `4m+2` gates, including a binary OR tree for `F`.
Replacing every `a_i` by `a'_i` deletes or repurposes exactly those `m`
displayed gates. For every `i`,

```text
old c_i = (x_i OR q) OR (q OR w)
        = x_i OR q OR w
        = x_i OR (q OR w)
        = new c_i.
```

Thus each `c_i` is an independently certified one-sided seal, and every path
from `a_i` to `F` meets it. The single signal `b` is shared by all `m` seals.

Each `c_i` is parent-live in the following exact sense. Set `s_i=1` and every
other selector to zero; the parent becomes `c_i`. Therefore any retargeting
that changes `c_i` on this selector slice changes the parent. In particular,
neither incoming signal can replace `c_i`: use
`q=0,x_i=0,w=1` against `a_i`, or `q=0,x_i=1,w=0` against `b`.

A replacement that depends on selectors and differs only when `s_i=0` could
remain masked. The lemma does not exclude such a jointly certified rewrite;
it shows that the seal is not free merely from its equality before and after
the upstream host rewrite.

The family is deliberately nonminimal. It proves that the actual retargetable
hosts `{a_i}` may be counted once, while neither the shared mask `b` nor the
live seal gates `{c_i}` are additional free hosts without a separate exact
replacement theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform family of finite single-output constant-free unrestricted AND/OR/NOT DAGs with paired host rewrites |
| Uniform/non-uniform | Uniform construction for every `m>=1`; each member finite and non-uniform |
| Circuit size | Old size `4m+2`; exactly `m` displayed host gates removed or repurposed; no minimality claim |
| Circuit depth | Unrestricted OR-tree depth; all local seals have constant distance from their hosts |
| Fan-in | AND/OR two; NOT one; `q` and shared mask `b` have unbounded family fanout |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean functions, selectors, and physical gate identities |
| Asymptotic quantifiers | Every `m>=1`, every assignment, every seal index, and both displayed input substitutions |
| Regime | Exact seal-versus-payment separation; not a minimum endpoint, SAT lower bound, or terminal result |
