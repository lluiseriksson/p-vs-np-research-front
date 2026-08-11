# GATE-004CY-TERMINAL-OUTPUT-ONLY — output preservation can transfer counterflow

**Label: NO-GO**

Preserving only the parent output under a shared comparable specialization
does not imply strict `R_0` descent. A changed intermediate consumer can move
the counted counterflow to a different direct `h`-boundary.

Let `x,y,u,t` be raw inputs and define

`g=u OR x`, `h=g AND y`,

`a=u OR t`, `v=NOT a`, `r=x OR v`, and `b=h AND r`.

As in GATE-004CX-GLOBAL-SPECIALIZATION-ONLY,

`r_00=1`, `r_10=x`, and `r_01=r_11=x`,

and specializing the region `{a,v,r}` to `u=1` replaces `r` by `x` while
leaving every cofactor of `b` equal to `x AND y`.

Give `r` a second live consumer and reconverge it through another direct
`h`-boundary:

`q=r OR u`, `c=h AND q`, and `o=b OR c`.

Before specialization,

`(q_00,q_10,q_01,q_11)=(1,1,x,1)`.

After replacing `r` by `x`,

`(q'_00,q'_10,q'_01,q'_11)=(x,1,x,1)`.

Nevertheless every cofactor of `c` is unchanged:

`(c_00,c_10,c_01,c_11)=(x AND y,y,x AND y,y)`,

and the same is true after specialization. Therefore `b`, `c`, `o`, and the
parent function are all preserved. But the boundary counted by `R_0` moves:
`b` loses the unequal input pair `(1,x)`, while `c` gains the unequal pair
`(x,1)` through `q'`. Hence `R_0` does not decrease.

The witness is constant-size, nonminimal, not the implication table, and not
a plateau parent. It refutes only the inference from terminal output equality
to lexicographic descent. LEMMA-206 avoids the transfer by requiring every
secondary **direct** consumer of the specialized region output to remain
functionally unchanged.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite unrestricted AND/OR/NOT shared-fanout and reconvergence gadget |
| Uniform/non-uniform | One uniform four-input local witness; no minimum-parent claim |
| Circuit size | Constant nonminimal DAG; no lower bound or plateau claim |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `r` has two live consumers and `h` has two direct boundaries |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors and pointwise comparability |
| Asymptotic quantifiers | Every assignment to `x,y,u,t` in the displayed witness |
| Regime | Terminal-output-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |
