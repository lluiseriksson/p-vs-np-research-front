# GATE-004CO-BOUNDARY-COUNT-ONLY — arbitrarily many aligned masks can coexist

**Label: NO-GO**

For every `m>=1`, take independent `x,y,z_1,...,z_m` and define

`g=u AND x`, `h=g OR y`, `n=NOT h`,

`R_i=NOT x AND z_i`, `b_i=h AND R_i` for `1<=i<=m`.

Here `Delta=x AND NOT y`, hence `Delta AND R_i=0`, and

`(b_i)_01=y AND NOT x AND z_i=(b_i)_11`.

Every `b_i` is a nonconstant aligned boundary, `g` has fanout one, and `h`
has `m+1` consumers including `n`. Thus boundary or fanout count does not force
a third neutral deletion.

This is a uniform local multi-exit DAG, not a single-output minimum circuit,
the full output table, or a plateau. Only boundary-count reasoning is closed.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted AND/OR/NOT local multi-exit carrier family |
| Uniform/non-uniform | Uniform family for every positive `m`; no minimum-parent claim |
| Circuit size | `O(m)` gates and `m` nonconstant aligned boundaries |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `g` fanout one and `h` fanout `m+1` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and pointwise mask containment |
| Asymptotic quantifiers | Every `m>=1` and assignment to the displayed inputs |
| Regime | Boundary-count-only no-go; not a plateau counterexample, SAT lower bound, or terminal result |
