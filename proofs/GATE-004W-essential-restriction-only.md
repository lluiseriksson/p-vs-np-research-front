# GATE-004W-ESSENTIAL-RESTRICTION-ONLY — certify implication-tail minimality by one restriction per negative variable

**Label: NO-GO**

## Scope

Attempt to prove the `K+3m` displayed implication-tail circuit minimum by
successively fixing each negative variable `b_i=1`, charging one removed gate
per essential restriction, and then invoking the exact fresh-conjunction
identity on the residual.

## Quantitative failure

LEMMA-057 proves exactly what this certificate yields. The `m` restrictions
remove at least `m` gates and leave `H AND a_1 AND ... AND a_m`, of size
`K+m`. The resulting lower bound is only `K+2m`, whereas displayed minimality
requires `K+3m`.

The missing `m` gates equal the entire desired negative-loss margin: the
displayed circuit has `4m` tail classes, so its prospective loss is `K-m`.
The restriction certificate therefore cannot close GATE-004W without a new
two-variable or multi-clause direct-sum argument.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits, disjoint implication tails, earliest-dependent-gate restrictions, and exact fresh-conjunction complexity |
| Uniform/non-uniform | Fully non-uniform base and circuit; uniform restriction sequence |
| Circuit size | Certificate lower bound `K+2m`, displayed upper bound `K+3m`, exact shortfall `m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every finite nonconstant base and every `m>=1`; method statement for the specified one-restriction-per-negative-variable certificate |
| Regime | Quantitative method no-go only; GATE-004W, GATE-004V, and P versus NP remain open |
