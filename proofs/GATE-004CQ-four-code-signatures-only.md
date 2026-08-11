# GATE-004CQ-FOUR-CODE-SIGNATURES-ONLY — the full table is realizable nonminimally

**Label: NO-GO**

## Tempting inference

Combine the alternating three-gate carrier, a complete four-code boundary
vector, and `F_00=F_01=F_11=A`, `F_10=0`, and infer a contradiction without
using minimum size or the exact pruning budget.

## Failure

LEMMA-197 realizes all those semantic and topological data in one explicit
single-output circuit. Its `01/11` carrier is exactly `{g,h,n}`, and the direct
boundary `b` transfers to an unequal `00/10` signature while the final output
has the exact table.

The construction routes `b` through a tautology and is deliberately
nonminimal. Therefore it is not a plateau counterexample. It proves that the
next argument must use minimum-circuit cost, exact two-gate losses, or a
forbidden cycle-minor operation; signature consistency alone is insufficient.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite unrestricted AND/OR/NOT exact-table circuit compared with minimum-plateau obligations |
| Uniform/non-uniform | One finite non-uniform witness; no minimum-parent claim |
| Circuit size | Constant redundant circuit; no lower-bound conclusion |
| Circuit depth | Constant witness; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactor vectors |
| Asymptotic quantifiers | Every assignment in LEMMA-197 |
| Regime | Structural no-go for four-code-signatures-only reasoning; not a plateau counterexample, SAT lower bound, or terminal result |
