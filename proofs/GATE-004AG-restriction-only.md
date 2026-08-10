# GATE-004AG-RESTRICTION-ONLY — essential restrictions prove the tail gate

**Label: NO-GO**

The attempted route restricts the unique negative variable in each of the
`m` disjoint width-five clauses and invokes the exact positive-clause theorem
LEMMA-048. LEMMA-107 shows that this proves only

`C(F)>=K+5m`,

whereas the displayed circuit costs `K+6m`. The missing `m` gates are exactly
the quotient surplus required to force loss at most `K-m`. Thus essential-
variable gate elimination, even combined with exact positive-tail cost,
cannot certify GATE-004AG without an additional direct-sum or
representation-independent quotient theorem.

This is a method no-go only. It neither supplies a smaller minimum circuit nor
refutes GATE-004AG, GATE-004AE, an unrestricted SAT circuit lower bound, or P
versus NP.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits, essential-variable restrictions, disjoint one-negative width-five clause tails, and diagonal quotient targets |
| Uniform/non-uniform | Fully non-uniform base and minimizing circuit; uniform restriction method |
| Circuit size | Method lower bound `K+5m` versus upper `K+6m`; exact deficit `m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every finite nonconstant base and every `m>=1` qualifying disjoint clause family |
| Regime | Structural no-go for the restriction-only proof method; all larger gates remain open |
