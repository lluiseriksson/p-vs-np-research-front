# GATE-004AH-SINGLE-COFACTOR-ONLY — canonical cofactor size proves the tradeoff

**Label: NO-GO**

The attempted route assigns every positive variable and charges the exact
size of the resulting negative-literal cofactor. LEMMA-112 exhausts these
cofactors: their sizes are `|S|`, their maximum is `m`, and their average is
`m/2`.

Therefore one cofactor supplies at most an `m`-gate residual lower bound, far
below the `6m-1` parent target. Averaging independent residual sizes supplies
only `m/2`; summing them would count the same parent gate under many mutually
exclusive restrictions and is invalid without a proved multi-cofactor direct
sum or semantic-survival theorem. Residual distinctness alone does not repair
that double counting.

This is a method no-go only. It does not refute the binary/NOT tradeoff,
GATE-004AH, GATE-004AG, GATE-004AE, an unrestricted SAT circuit lower bound,
or P versus NP. The next attack must couple several canonical cofactors inside
one parent circuit rather than lower-bound them independently.

## Model card

| Field | Value |
|---|---|
| Computational model | Full positive-variable cofactors of unrestricted circuits and exact residual circuit size |
| Uniform/non-uniform | Uniform canonical restrictions; fully non-uniform parent circuit |
| Circuit size | Individual residual at most `m`, average exactly `m/2`, versus parent target `6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions and subset incidence only |
| Asymptotic quantifiers | Every `m>=1` and all `2^m` canonical positive cofactors |
| Regime | Structural no-go for independent single-cofactor charging; larger gates remain open |
