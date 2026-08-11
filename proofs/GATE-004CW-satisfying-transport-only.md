# GATE-004CW-SATISFYING-TRANSPORT-ONLY — satisfying minors miss the counterflow difference

**Label: NO-GO**

LEMMA-203 places every counterflow difference in `r_00 XOR r_10`. Therefore
no pair of same-row satisfying restrictions exposes it: `10` is the unique
unsatisfying implication code.

This is genuine underdetermination, not only missing notation. Let
`x,y,z,w,u,t` be independent raw inputs and define

`g=u AND x`, `h=g OR y`,

and

`r=(t AND NOT x) OR
   (NOT t AND ((NOT u AND z) OR
   (u AND ((y AND z) OR (NOT x AND NOT y AND w)))))`.

Put `b=h AND r`. Its satisfying cofactors are

`r_00=z`, `r_01=r_11=NOT x`,

`b_00=y AND z`, `b_01=b_11=y AND NOT x`.

But

`r_10=(y AND z) OR (NOT x AND NOT y AND w)`,

which contains an arbitrary live `w`-dependence invisible in all three
satisfying cofactors. Nevertheless `b_10=y AND z=b_00`, because `h_10=x OR y`
kills the extra region. The circuit is finite and nonminimal; it is not a
plateau witness.

The formula has a realization whose auxiliary gates are all `01/11`-aligned:
form `a=u OR t`, `v=NOT a`, `tbar=NOT t`, `k=u AND tbar`,
`m=(y AND z) OR (NOT x AND NOT y AND w)`, `d=v AND z`, `e=k AND m`,
`j=t AND NOT x`, and `r=(d OR e) OR j`. At `t=1`, these gates are constant
or independent of `u`. Thus the local canonical `01/11` carrier remains
`{g,h,n}` after adjoining `n=NOT h`.

Hence satisfying-minor contraction data alone cannot determine the marked
counterflow transport. Any valid cost argument must include the `10`
cofactor and then separately connect it to a satisfying-code resource bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Size-three endpoint audit plus an explicit finite unrestricted AND/OR/NOT cofactor witness |
| Uniform/non-uniform | Every hypothetical endpoint for the localization; one uniform six-input witness for underdetermination |
| Circuit size | Parent `K+2` in the target; constant nonminimal witness with no lower-bound claim |
| Circuit depth | Unrestricted target; constant-depth witness up to binary association |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every endpoint counterflow; witness identity holds for every assignment to `x,y,z,w,u,t` |
| Regime | Satisfying-transport-only no-go; not a minimum plateau counterexample, SAT lower bound, or terminal result |
