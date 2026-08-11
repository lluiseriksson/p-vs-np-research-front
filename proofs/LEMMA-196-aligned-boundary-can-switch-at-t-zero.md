# LEMMA-196 — a satisfying-aligned boundary can switch at `t=0`

**Label: PROVED**

There is a constant-size AND/OR/NOT local gadget in which a direct boundary of
the size-three `01/11` carrier has equal nonconstant `01/11` cofactors but
unequal `00/10` cofactors.

Take independent base inputs `x,y` and define

`g=u AND x`, `h=g OR y`, `n=NOT h`,
`r=NOT x OR NOT t`, and `b=h AND r`.

Then

`b_01=b_11=y AND NOT x`,

while

`b_00=y` and `b_10=x OR y`.

## Proof

At `t=1`, `r=NOT x`. Hence

`b_01=y AND NOT x`

and

`b_11=(x OR y) AND NOT x=y AND NOT x`.

At `t=0`, `r=1`, so `b=h`; substituting `u=0,1` gives the displayed unequal
cofactors. Thus `b` lies outside `H_{01,11}` but inside `H_{00,10}`.

The gadget is local and nonminimal. It does not realize the full output table
or a plateau. It proves that satisfying-row alignment places no automatic
constraint on the falsifying row.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit constant-size unrestricted AND/OR/NOT local carrier and boundary gadget |
| Uniform/non-uniform | One uniform four-input gadget; no minimum-parent claim |
| Circuit size | Constant; three carrier gates plus a `t`-dependent mask and boundary |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every assignment to `x,y,u,t` in the displayed gadget |
| Regime | Exact local four-code separation; not a plateau counterexample, SAT lower bound, or terminal result |
