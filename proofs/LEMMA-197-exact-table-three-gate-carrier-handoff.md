# LEMMA-197 — the exact table admits a three-gate carrier handoff

**Label: PROVED**

There is a finite AND/OR/NOT circuit computing the exact implication table
whose canonical `01/11` carrier is the three-gate alternating chain and which
contains a direct boundary aligned under `01/11` but switching under `00/10`.

Let

`A=x AND NOT y`,

`g=u AND x`, `h=g OR y`, `n=NOT h`, `i=t OR n`, `F=A AND i`,

`r=NOT x OR NOT t`, `b=h AND r`, `s=NOT b`, `c=b OR s`,

and let the final output be `O=F AND c`.

Then `c=1`, so `O=F`, and

`O_00=O_01=O_11=A`, `O_10=0`.

Moreover `H_{01,11}={g,h,n}`, while

`b_01=b_11=y AND NOT x`, `b_00=y`, `b_10=x OR y`.

## Proof

If `A=1`, then `x=1,y=0`, so `h=u`, `n=NOT u`, and
`F=t OR NOT u`. If `A=0`, the final AND defining `F` makes `F=0`. Hence
`F=A AND (t OR NOT u)` and the four output cofactors are exact. The tautology
`c=b OR NOT b` leaves the output unchanged while keeping the boundary path in
the physical output cone.

Across `01/11`, only `g,h,n` differ: `i=1` in both codes; `b` is aligned by
the calculation in LEMMA-196; and negation plus the tautology preserve that
alignment downstream. The four cofactors of `b` are exactly those of
LEMMA-196.

The circuit is intentionally redundant because of `c` and the final AND. It
is not claimed minimum, extremal, or a two-gate plateau.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite unrestricted AND/OR/NOT circuit for an exact base–implication function |
| Uniform/non-uniform | One finite non-uniform exact-table construction; no minimum-parent claim |
| Circuit size | Constant-size redundant circuit; canonical `01/11` carrier has three gates |
| Circuit depth | Constant; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every assignment to `x,y,u,t` in the displayed circuit |
| Regime | Exact full-table nonminimal realization; not a plateau counterexample, SAT lower bound, or terminal result |
