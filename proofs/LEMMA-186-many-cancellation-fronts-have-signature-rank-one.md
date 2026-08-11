# LEMMA-186 — arbitrarily many cancellation fronts can have signature rank one

**Label: PROVED**

For every integer `m>=1`, there is a finite AND/OR/NOT DAG with one varying
signal `p`, `m` distinct live one-sided `01/11` cancellation fronts, and only
one independent incoming Boolean difference.

## Construction and proof

Use raw inputs `u,x,y,z_1,...,z_m`; a dummy `t` may be fixed to one. Write XOR
as its standard AND/OR/NOT expansion and define

`r=x XOR y`,

`p=(NOT u AND x) OR (u AND y)`,

`q_i=r OR z_i`, `d_i=p OR q_i` for `1<=i<=m`,

and let `O` be a binary AND tree over all `d_i` (or `d_1` when `m=1`).

At `u=0`, `p=x`; at `u=1`, `p=y`. Hence

`Delta(p)=p_01 XOR p_11=x XOR y=r`,

while every `q_i` is pair-stable. Moreover

`d_i|_{u=0}=x OR r OR z_i=x OR y OR z_i`

and

`d_i|_{u=1}=y OR r OR z_i=x OR y OR z_i`.

Thus each `d_i` is a distinct first binary cancellation immediately after
`p`. Every `d_i` is live in `O`: set `x=y=0`, set all `z_j=1` except possibly
`z_i`, and vary `z_i`. Nevertheless all `m` incoming difference labels are
the same function `r`; their span over pointwise XOR has dimension one.

The construction is not minimum and makes no claim about how many gates a
fully pruned restriction deletes. It proves that cancellation-front count is
not signature independence.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite AND/OR/NOT DAG with arbitrary live fanout multiplicity |
| Uniform/non-uniform | Uniform construction for every integer `m>=1`; no minimum-parent claim |
| Circuit size | `O(m)` gates; `m` fronts but Boolean-difference span exactly one |
| Circuit depth | Unrestricted target; construction has logarithmic output-tree depth plus constant local depth |
| Fan-in | AND/OR two; NOT one; fanout of `p` is `m` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean functions as an `F_2` vector space under pointwise XOR |
| Asymptotic quantifiers | Every positive integer `m` and every assignment to the displayed inputs |
| Regime | Exact structural multiplicity theorem; not a deletion lower bound, plateau realization, SAT lower bound, or terminal result |
