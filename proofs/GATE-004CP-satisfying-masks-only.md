# GATE-004CP-SATISFYING-MASKS-ONLY — `01/11` factoring can break `00/10`

**Label: NO-GO**

## Tempting inference

Replace every shared boundary by its common `01/11` expression from
LEMMA-195, thereby removing the carrier contribution `g,h` globally.

## Failure

LEMMA-196 gives `b_01=b_11=y AND NOT x`, but
`b_00=y` and `b_10=x OR y`. Replacing `h` by its neutral expression `y` is
valid on the satisfying row `t=1` and invalid on the row `t=0` that contains
the unique falsifying code `10`.

Thus satisfying-row mask identities alone cannot justify a global circuit
rewrite. Any uncrossing must preserve the complete four-code signature of
every boundary and its downstream consumers.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted AND/OR/NOT four-code boundary gadget compared with plateau rewrites |
| Uniform/non-uniform | One finite local witness; no minimum-parent claim |
| Circuit size | Constant-size witness; no lower-bound conclusion |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean cofactor vectors over `{00,01,10,11}` |
| Asymptotic quantifiers | Every assignment in the LEMMA-196 gadget |
| Regime | Structural no-go for satisfying-masks-only factoring; not a plateau counterexample, SAT lower bound, or terminal result |
