# GATE-004DD-COMPARABILITY-BASIS-TWO-ONLY

**Label: NO-GO**

Comparable row-zero cancellation does not force the aligned-inner basis-two
certificate of LEMMA-211, even when the counterflow input has fanout one.

## Witness

Use raw inputs `u,t,x,y,z,w` and the constant-free AND/OR/NOT DAG

`nt = NOT t`

`a = u AND w`

`c = x OR a`

`d = y OR a`

`e = c AND d`

`f = z OR a`

`h = e AND f`

`g = u AND x`

`i = g AND y`

`j = i AND z`

`k = j AND nt`

`r = w OR k`

`b = h OR r`.

Absorption gives

`h = xyz OR uw`,

`r = w OR uxyz NOT t`,

and

`b = xyz OR w`.

Consequently `b` is globally `u`-independent, directly consumes the
`u`-sensitive carrier signal `h`, and its fanout-one other input has cofactors

`r_00=w`, `r_10=w OR xyz`, and `r_01=r_11=w`.

This is a comparable counterflow confined exactly to `00/10`.

Before `b`, the globally `u`-independent physical signals are precisely raw
`x,y,z,w,t` and `nt`. Each depends on at most one of the four essential base
variables `x,y,z,w`. Any constant-free formula with at most two gates has at
most three leaves, so every such formula over this pool depends on at most
three of those four variables. The target `xyz OR w` depends essentially on
all four. It therefore has no wire, one-gate, or two-gate realization over
the available independent predecessor pool.

The witness is deliberately nonminimal and does not refute LEMMA-211 or a
minimum-cost forcing theorem. It shows that comparability, row localization,
fanout one, and exact cancellation alone cannot bound the missing independent
factor to basis distance two.

`verification/free_basis_two_realization_audit.py` checks all 64 assignments,
the exact cofactor table, the exact independent predecessor pool, and every
constant-free formula of basis radius at most two. The algebra and essential
variable argument carry the `NO-GO` label.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite constant-free unrestricted AND/OR/NOT DAG with a comparable fanout-one counterflow input |
| Uniform/non-uniform | One uniform six-input local witness; no minimum-parent claim |
| Circuit size | Thirteen-gate nonminimal witness; no lower bound or plateau claim |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `r` has fanout exactly one to `b` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities, essential-variable counting, and complete basis-radius-two enumeration |
| Asymptotic quantifiers | Every assignment to `u,t,x,y,z,w` and every constant-free formula of at most two gates over the exact independent predecessor pool |
| Regime | Comparability-plus-bounded-basis-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |
