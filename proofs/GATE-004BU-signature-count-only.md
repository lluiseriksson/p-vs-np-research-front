# GATE-004BU-SIGNATURE-COUNT-ONLY — charge changing clauses to selector resources

**Label: NO-GO**

## Attempt

If no clause has a common cycle/NOT loss, charge each clause whose neutral
outcome differs between `x=0` and `x=1` to a distinct selector-dependent gate.
Use `j` changing signatures to force linear selector penetration and then a
resource contradiction.

## Failure

LEMMA-175 mixes arbitrarily many tail variables into the cofactor signature
of one surviving NOT while only three gates depend on `x`. Thus the map from
changed tail blocks to selector-dependent gates need not be injective or even
have growing image. LEMMA-151 and NG-105 independently show that selector
penetration is representation-dependent and carries no size premium by
itself.

The witness is not claimed to compute the canonical implication product in a
minimum parent. It closes signature-count-only charging, not GATE-004BU.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit selector-tail mixing gadgets and abstract signature-to-resource charging |
| Uniform/non-uniform | Uniform local gadget family; no minimum-circuit realization claim |
| Circuit size | `m` mixed tail variables with only three selector-dependent gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and integer incidence counts only |
| Asymptotic quantifiers | Every `m>=1` |
| Regime | Structural no-go for signature-count-only selector charging; not a refutation of GATE-004BU or a SAT lower bound |
