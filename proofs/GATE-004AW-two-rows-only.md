# GATE-004AW-TWO-ROWS-ONLY — bound raw-input collisions from two cofactors

**Label: NO-GO**

LEMMA-147 constructs, for every `m`, globally non-raw functions

`g_i=t_i OR R(X)`

whose cofactors on both designated rows are exactly `t_i`. A single shared
predicate `R`, zero on those rows but nonzero elsewhere, realizes all `m`
functions with only one additional OR gate per index after `R`.

Consequently, the facts that a minimum parent circuit contains no globally
raw-input gate and that its two selected cofactor tables contain raw `t_i`
do not imply `b=o(m)`. Nor does a bilateral raw cofactor automatically create
cross-row quotient surplus: both observed cofactors are the same function.

This no-go does not refute GATE-004AW or exhibit these gates inside a minimum
canonical implication circuit. It closes only arguments using the two
cofactor tables plus global non-rawness and linear-size realizability. The
active GATE-004AX permits a collision to be offset by quotient surplus and
requires minimum-circuit exchange or information from additional canonical
rows.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean parent-gate functions observed under two fixed base restrictions |
| Uniform/non-uniform | Fully non-uniform finite witness family |
| Circuit size | Shared `C(R)` plus `m` binary gates; no minimum-circuit claim |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor semantics only |
| Asymptotic quantifiers | Every `m>=1` and every selected row pair in a base cube containing a third assignment |
| Regime | Structural no-go for a two-rows-only collision argument; GATE-004AX/AW/AV/AU/AG/AE remain open |
