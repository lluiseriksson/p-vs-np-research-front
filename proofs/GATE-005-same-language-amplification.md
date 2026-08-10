# GATE-005 — Same-language exponent amplification for SAT

**Label: EXPLORATORY (downstream; not the active smallest brick)**

## Falsifiable theorem

There exist explicit constants `r0>1` and `eta>0` such that for every integer
`m>=0`,

`SAT-gamma notin SIZE(n^(r0+m eta))`

implies

`SAT-gamma notin SIZE(n^(r0+(m+1) eta))`,

with the exact `SAT-gamma` encoding and the same unrestricted Boolean circuit
model.

### Model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits computing exact `SAT-gamma` language slices |
| Uniform/non-uniform | Fully non-uniform circuit adversary |
| Circuit size | Consecutive exponents `r0+m eta` and `r0+(m+1)eta` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | Polynomial advice represented by arbitrary circuit families |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `r0,eta`; for every integer `m`; each lower bound means infinitely many failure lengths |
| Regime | Worst-case exact total-language decision; malformed encodings reject |

## Role in the map

If GATE-004 supplies the base lower bound at exponent `r0`, iterating GATE-005
would exclude every fixed polynomial exponent and establish
`SAT notin P/poly`. Neither premise is currently proved. GATE-005 must not be
assumed from paddability or self-reducibility: those properties preserve
algorithms and reductions but do not automatically amplify circuit lower-bound
exponents in the harder direction.
