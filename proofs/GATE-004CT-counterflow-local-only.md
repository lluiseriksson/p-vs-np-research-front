# GATE-004CT-COUNTERFLOW-LOCAL-ONLY — a second sensitivity route can cancel exactly

**Label: NO-GO**

Take independent `x,y,z,u,t` and define

`g=u AND x`, `h=g OR y`, `n=NOT h`,

`a=u OR t`, `v=NOT a`, `w=NOT t`, `k=u AND w`,

`d=v AND z`, `e=k AND y`, `f=e AND z`,

`j=t AND NOT x`, `r=(d OR f) OR j`, and `b=h AND r`.

At `t=1`, `r=NOT x`, so `b=y AND NOT x` for both values of `u`. At `t=0`,

`r_00=z`, `r_10=y AND z`,

and therefore `b_00=b_10=y AND z`. Thus `b` is globally `u`-independent and
nonconstant, while its second input `r` is `u`-sensitive on row zero. Every
gate in the auxiliary route is aligned on `01/11`, so the local canonical
carrier there remains `{g,h,n}`.

This nonminimal local gadget is not the full output table or a plateau. It
proves that a counterflow and its reconvergence do not locally force a third
deletion or a killed cycle.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit constant-size unrestricted AND/OR/NOT two-route cancellation gadget |
| Uniform/non-uniform | One uniform five-input local witness; no minimum-parent claim |
| Circuit size | Constant-size local DAG; no lower-bound conclusion |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every assignment to `x,y,z,u,t` |
| Regime | Counterflow-local-only no-go; not a plateau counterexample, SAT lower bound, or terminal result |
