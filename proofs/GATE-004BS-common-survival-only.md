# GATE-004BS-COMMON-SURVIVAL-ONLY — infer a stable clause resource

**Label: NO-GO**

## Attempt

Use LEMMA-172's fact that every parent NOT survives both nonzero primary
cofactors to infer that some surviving NOT is private to the same tail clause
in both codes and is deleted by neutralizing that clause.

## Failure

LEMMA-173 gives one physical NOT gate that survives both codes while its tail
signature changes from `NOT u_i` to `NOT(u_i OR u_k)`. Neutralizing clause
`i` deletes the cofactor-zero specialization but leaves a nonconstant
`NOT u_k` specialization at cofactor one. Common survival therefore contains
neither common clause identity nor uniform neutralization.

The gadget is not asserted to realize an exact minimum parent. This closes
only the inference from survival data alone and does not refute GATE-004BS.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit mixed primary-tail NOT gadget and abstract common-survival inference |
| Uniform/non-uniform | Non-uniform local witness; no minimum-circuit realization claim |
| Circuit size | One surviving NOT gadget; no parent resource assertion |
| Circuit depth | Constant |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and gate support only |
| Asymptotic quantifiers | Every tail with at least two distinct negative variables |
| Regime | Structural no-go for common-survival-only identity; not a refutation of GATE-004BS or a SAT lower bound |
