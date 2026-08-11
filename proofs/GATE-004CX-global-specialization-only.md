# GATE-004CX-GLOBAL-SPECIALIZATION-ONLY — shared fanout blocks naive cofactor replacement

**Label: NO-GO**

Comparability identifies `r^dagger` with one cofactor of `r`, but it does not
authorize replacing a shared gate `r` globally.

Let `x,y,z,s,u,t` be raw inputs and define

`g=u OR x`, `h=g AND y`, `n=NOT h`,

`a=u OR t`, `v=NOT a`, `r=x OR v`, and `b=h AND r`.

Then

`r_00=1`, `r_10=x`, and `r_01=r_11=x`,

while every cofactor of `b` equals `x AND y`. Thus the AND erasure is the
comparable cofactor `r|_{u=1}=x`.

Now give `r` a second live consumer:

`c=r OR z`, `d=c AND s`, `o=b OR d`.

Globally replacing `r` by `x` changes `o` at
`u=0,t=0,x=y=z=0,s=1`. The auxiliary gates `a,v,r,c,d,o` are all
`01/11`-aligned, so adjoining them does not enlarge the local carrier
`{g,h,n}`. The gadget is nonminimal, not the implication table, and not a
plateau witness.

The example refutes only naive global specialization. It does not show that
every edge-local rewrite costs an extra gate. LEMMA-205 succeeds precisely
when a cofactor-private replacement region is supplied.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite unrestricted AND/OR/NOT shared-fanout gadget |
| Uniform/non-uniform | One uniform six-input local witness; no minimum-parent claim |
| Circuit size | Constant nonminimal DAG; no lower-bound or exact replacement-cost claim |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `r` has two live outgoing edges |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors and pointwise comparability |
| Asymptotic quantifiers | Every assignment to `x,y,z,s,u,t` in the displayed witness |
| Regime | Global-specialization-only no-go; not a minimum plateau counterexample, SAT lower bound, or terminal result |
