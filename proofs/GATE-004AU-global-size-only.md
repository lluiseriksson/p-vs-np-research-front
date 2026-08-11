# GATE-004AU-GLOBAL-SIZE-ONLY — infer diagonal quotient stability from near-minimal size

**Label: NO-GO**

LEMMA-144 proves that the minimum parent size is within `Delta=o(m)` of the
displayed `K+6m` circuit. This alone does not bound the number of semantic
classes after restricting to the two diagonal base rows.

A minimum circuit has no two gates computing the same global function, but
distinct global functions can restrict to the same ordered cofactor pair, and
a globally essential gate can become constant or inactive on both selected
rows. Neither event deletes a gate from the unrestricted parent circuit.
Consequently the global gate deficit `Delta` does not, without an additional
collision theorem, count missing diagonal quotient classes.

This is a method no-go only. It does not exhibit a canonical minimum circuit
with a small quotient and does not refute GATE-004AU/AT/AG/AE.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted parent circuits and their ordered two-row semantic cofactor quotients |
| Uniform/non-uniform | Uniform selected rows; fully non-uniform minimizing circuit |
| Circuit size | Near-minimum deficit `Delta=o(m)` but no class-count lower bound from size alone |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean semantic equivalence under restriction only |
| Asymptotic quantifiers | Every canonical base-tail instance and every minimum circuit considered by the size-only method |
| Regime | Structural no-go for size-only quotient promotion; GATE-004AU/AT/AG/AE remain open |
