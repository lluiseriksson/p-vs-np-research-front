# GATE-004DC-COMPARABILITY-BASIS-ONE-ONLY

**Label: NO-GO**

Comparability and exact cancellation do not force the free independent
basis-one certificate of LEMMA-210.

## Witness

Use raw inputs `u,t,x,y,z` and the following constant-free AND/OR/NOT DAG:

`nt = NOT t`

`a = u AND z`

`c = x OR a`

`d = y OR a`

`h = c AND d`

`e = u AND x`

`f = e AND y`

`j = f AND nt`

`r = z OR j`

`b = h OR r`.

Boolean absorption gives

`h = (x OR uz) AND (y OR uz) = xy OR uz`,

`r = z OR uxy NOT t`,

and

`b = xy OR z`.

Thus `b` is globally `u`-independent and directly consumes the `u`-sensitive
signal `h`. The other input has exact cofactors

`r_00=z`, `r_10=z OR xy`, and `r_01=r_11=z`.

They form a comparable row-zero counterflow of precisely the type in
LEMMA-203/204.

Before `b`, the only globally `u`-independent physical signals are raw
`x,y,z,t` and `nt`. Every other displayed gate changes under some assignment
when `u` is flipped. A wire or NOT of one signal from this pool depends on at
most one raw variable; an AND or OR of two pool signals depends on at most two
of `x,y,z`. But `b=xy OR z` depends essentially on all three. Hence no wire or
one-gate realization over the available independent nondescendant signals
computes `b`.

The witness does not refute LEMMA-210 and is not claimed minimum. It shows
that comparability, row localization, and boundary cancellation alone cannot
produce its certificate. A minimum-cost or exact-pruning argument is still
required.

`verification/free_local_realization_audit.py` checks all 32 assignments, all
four cofactor identities, the exact independent-signal pool, and every wire,
NOT, AND, and OR candidate over that pool. The displayed algebra and essential
variable argument carry the `NO-GO` label; the script is a regression check.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite constant-free unrestricted AND/OR/NOT DAG with a comparable counterflow boundary |
| Uniform/non-uniform | One uniform five-input local witness; no minimum-parent claim |
| Circuit size | Ten-gate nonminimal witness; no lower bound or plateau claim |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `h` and `r` feed the direct boundary `b` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities and basis-distance-one enumeration |
| Asymptotic quantifiers | Every assignment to `u,t,x,y,z` and every wire or one-gate expression over the exact independent predecessor pool |
| Regime | Comparability-plus-semantics-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |
