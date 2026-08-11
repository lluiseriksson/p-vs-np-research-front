# GATE-004CR-HANDOFF-COUNT-ONLY — exact-table circuits can have many handoffs

**Label: NO-GO**

For every `m>=1`, extend the exact-table construction of LEMMA-197. Retain

`A=x AND NOT y`, `g=u AND x`, `h=g OR y`, `n=NOT h`,
`F=A AND (t OR n)`.

For fresh `z_i`, put

`r_i=(NOT x AND z_i) OR NOT t`, `b_i=h AND r_i`,
`c_i=b_i OR NOT b_i`.

Let `C` be any AND tree over the `c_i` and output `O=F AND C`. Every `c_i=1`,
so the output table is exact. For each `i`,

`(b_i)_01=(b_i)_11=y AND NOT x AND z_i`,

while `(b_i)_00=y` and `(b_i)_10=x OR y`. Thus all `m` gates are distinct
handoffs, and `H_{01,11}={g,h,n}` remains unchanged.

The family is deliberately redundant and not minimum or a plateau. It proves
that handoff number, pair-sensitivity count, and exact-table consistency alone
cannot charge the two-gate budget.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted AND/OR/NOT single-output exact-table family |
| Uniform/non-uniform | Uniform family for every positive `m`; no minimum-parent claim |
| Circuit size | `O(m)` redundant circuit with `m` distinct handoffs |
| Circuit depth | Unrestricted target; logarithmic tautology-tree depth is available |
| Fan-in | AND/OR two; NOT one; `h` fanout at least `m+1` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every `m>=1` and every assignment to the displayed inputs |
| Regime | Handoff-count-only no-go; not a plateau counterexample, SAT lower bound, or terminal result |
