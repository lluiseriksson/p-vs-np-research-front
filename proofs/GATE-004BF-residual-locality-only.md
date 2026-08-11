# GATE-004BF-RESIDUAL-LOCALITY-ONLY — lift residual private NOTs to the parent

**Label: NO-GO**

A NOT gate that specializes to a clause-local function under one satisfying
base assignment need not be clause-local in the parent circuit.

Let `R(X)` be a nonconstant base function that vanishes at a chosen satisfying
assignment `x*`, and consider the gate function

`g_i(X,u_i)=NOT(u_i OR R(X))`.

At `X=x*`, this specializes exactly to `NOT u_i`, so it can occupy the private
NOT position in the residual read-once formula. Globally it depends
essentially on both the base and the clause variable. Setting `u_i=0` leaves
the nonconstant base function `NOT R(X)`. Thus residual semantic locality does
not identify the parent gate's support or prove that the gate itself becomes
constant under a tail restriction.

This gate witness is not asserted to occur in a minimum circuit for `J_j`, to
have cycle rank one, or to survive the full neutral pair restriction when it
has no second output path. It closes only the inference from one satisfying
cofactor's private-NOT role to parent-level resource pruning. GATE-004BF must
use the unique-cycle wiring and all output paths.

## Model card

| Field | Value |
|---|---|
| Computational model | Boolean gate functions under a satisfying-base cofactor and tail restrictions |
| Uniform/non-uniform | Explicit non-uniform semantic witness; no minimum-circuit or realizability-in-stratum claim |
| Circuit size | One displayed mixed NOT gate; no parent-size assertion |
| Circuit depth | Unrestricted ambient circuit |
| Fan-in | OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and essential dependence only |
| Asymptotic quantifiers | Every clause index and every nonconstant base mask with an attained zero |
| Regime | Structural no-go for residual-locality-only lifting; GATE-004BF was later proved using LEMMA-160/163 and GATE-004BE/BD using LEMMA-164/165, while GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |
