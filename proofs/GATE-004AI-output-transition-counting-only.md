# GATE-004AI-OUTPUT-TRANSITION-COUNTING-ONLY — cube changes force distinct charges

**Label: NO-GO**

The attempted route counts the `m*2^(m-1)` adjacent canonical restrictions on
which the output residual changes and tries to extract `m` distinct internal
witnesses. LEMMA-113 shows why that inference is invalid: the single output
node of every circuit for `W_m` has all `2^m` residual functions as its
cofactor profile and changes on every cube edge.

Thus an exponential number of output-profile changes is compatible with one
fixed parent node. Dividing the edge count by an unproved bound on how many
edges a gate may witness is circular; the output already witnesses all of
them. Any valid clause-cover injection must define an internal first-
divergence or survival witness and separately prove bounded reuse across
clause indices.

This is a method no-go only. It does not refute the injection in GATE-004AI,
the equivalent tradeoff GATE-004AH, GATE-004AG/AE, an unrestricted SAT
circuit lower bound, or P versus NP.

## Model card

| Field | Value |
|---|---|
| Computational model | Canonical cofactor profiles of nodes in unrestricted AND/OR/NOT parent circuits |
| Uniform/non-uniform | Uniform restriction cube; every individual non-uniform parent circuit |
| Circuit size | No lower bound from `2^m` profiles or `m*2^(m-1)` changing output edges alone |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restriction cube; no algebraic circuit model |
| Asymptotic quantifiers | Every `m>=1`, every canonical cube edge, and every circuit computing `W_m` |
| Regime | Structural no-go for raw output-transition counting; internal bounded-reuse gates remain open |
