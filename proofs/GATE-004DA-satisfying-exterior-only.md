# GATE-004DA-SATISFYING-EXTERIOR-ONLY — `sigma=0` transfer is invisible outside

**Label: NO-GO**

LEMMA-208 proves that specialization to `sigma=0` can change exterior gate
functions only at code `10`, the unique unsatisfying implication code.
Therefore the three satisfying exterior cofactor tables alone cannot detect,
locate, or charge such a transfer.

The branch is nonvacuous. Let `x,u,t` be raw inputs and define

`p=u OR x`, `h=p OR t`,

`a=u OR t`, `v=NOT a`, `r=x OR v`, and `b=h OR r`.

Then

`(r_00,r_10,r_01,r_11)=(1,x,x,x)`

and every cofactor of `b` is `1`. The OR erasure selects the larger row-zero
cofactor, namely the global cofactor `r|_{u=0}` with signature `(1,1,x,x)`.
Thus only `r_10` changes.

Define a second route

`w=NOT t`, `d=u AND w`, `s=x OR d`, `q=r AND s`,

so that

`(s_00,s_10,s_01,s_11)=(x,1,x,x)`.

Before specialization, every cofactor of `q` is `x`. After replacing `r` by
`r|_{u=0}`,

`(q'_00,q'_10,q'_01,q'_11)=(x,1,x,x)`.

Finally let `c=h OR q` and `o=b AND c`. The functions at `b`, `c`, and `o`
are unchanged. The counted boundary transfers from `b`, whose old other input
has row-zero pair `(1,x)`, to `c`, whose new other input has pair `(x,1)`.
All exterior `00`, `01`, and `11` cofactors are identical before and after.

The witness is constant-size, nonminimal, not the implication table, and not
a plateau parent. It establishes no minimum-cost obstruction. It refutes only
arguments that try to charge the `sigma=0` transfer from satisfying exterior
gate functions without using the specialized region, physical topology,
minimum size, or exact pruning correspondence.

## Model card

| Field | Value |
|---|---|
| Computational model | General single-code localization plus one explicit finite unrestricted AND/OR/NOT transfer gadget |
| Uniform/non-uniform | Every qualifying `sigma=0` exterior for invisibility; one uniform three-input local witness for nonvacuity |
| Circuit size | No general size claim; witness is constant-size and nonminimal |
| Circuit depth | Unrestricted target; constant witness depth |
| Fan-in | AND/OR two; NOT one; `r` and `h` have shared fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every qualifying `sigma=0` specialization; every assignment to `x,u,t` in the witness |
| Regime | Satisfying-exterior-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |
