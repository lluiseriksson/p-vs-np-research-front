# GATE-004CE-FOUR-CODE-SIGNATURES-ONLY — the full table does not force a cycle kernel

**Label: NO-GO**

## Tempting inference

Combine two `01/11` cancellation fronts with
`F_00=F_01=F_11=A`, `F_10=0`, and conclude that their reconvergence cycle is
killed by a satisfying restriction.

## Exact-table witness

Let `x,y,u,t` be raw inputs. Write XOR as an abbreviation for its standard
AND/OR/NOT implementation and define

`r=x XOR y`, `s=NOT r`,

`p=(NOT u AND x) OR (u AND y)`,

`d=p OR r`, `c=p AND s`, `a=d AND NOT c`,

`i=t OR NOT u`, and `F=a AND i`.

For either value of `u`, direct evaluation gives

`d=x OR y`, `c=x AND y`, and `a=x XOR y`.

Consequently, with `A=x XOR y`, the four cofactors are exactly

`F_00=F_01=F_11=A`, `F_10=0`.

The signal `p` has two live exits into the distinct cancellation gates `d,c`.
Under codes `00,01`, its multiplexer contracts to `x`; under code `11`, it
contracts to `y`. In every satisfying case both branches remain nonconstant
and reconverge at `a`, so their cycle survives modulo contraction.

The witness is not claimed minimum, extremal, or a two-gate plateau. It proves
that the full output table and local edgewise signatures alone do not force a
restriction kernel. Any proof of GATE-004CE must use minimum-size structure,
especially the exact two-binary-gate loss of LEMMA-185, or produce the private
certificate.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite AND/OR/NOT circuit computing the exact four-code implication table |
| Uniform/non-uniform | One uniform four-input local family; no minimum-parent realization claim |
| Circuit size | Constant-size nonminimal witness; no lower-bound conclusion |
| Circuit depth | Constant witness; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean identities and cycle contraction over `F_2`; XOR is basis-expanded |
| Asymptotic quantifiers | Every assignment to `x,y,u,t` in the displayed circuit |
| Regime | Structural no-go for four-code-signatures-only reasoning; not a plateau counterexample, SAT lower bound, or terminal result |
