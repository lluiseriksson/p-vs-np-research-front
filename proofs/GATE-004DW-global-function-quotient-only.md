# GATE-004DW-GLOBAL-FUNCTION-QUOTIENT-ONLY — distinct ports remain unbounded

**Label: NO-GO**

Scope: merge globally equal port gates using LEMMA-005/234 and infer that a
bounded marked core has only boundedly many residual port classes or enough
free physical hosts.

LEMMA-234 proves that a minimum endpoint has already performed every such
duplicate merge. LEMMA-235 shows the quantitative limitation: a fixed marked
core can support `m` pairwise distinct port functions for arbitrary `m`, so
the global-function quotient alone leaves unboundedly many classes.

The diagnostic family is nonminimal and does not prove an endpoint with those
ports. Nor does it refute a joint-circuit cost or parent-transfer theorem that
charges distinct classes. It refutes only bounding or paying them from exact
function inequality itself.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT duplicate elimination plus the LEMMA-233 diagnostic family |
| Uniform/non-uniform | Every finite minimum circuit for injectivity; every diagnostic `m>=1` for unbounded classes |
| Circuit size | One gate per global function in a minimum circuit; diagnostic retains at least `m` port classes |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact global Boolean gate functions and quotient classes |
| Asymptotic quantifiers | Every minimum circuit and every diagnostic `m>=1` |
| Regime | Global-function-quotient-only no-go; not endpoint counterexample, SAT lower bound, or terminal result |
