# GATE-004AF-LENGTH68-ONLY — use every standard block through length 68

**Label: NO-GO**

LEMMA-082 proves that even the complete identifier range 1 through 32,767,
hence every standard neutral block of length at most 68, retains a linear
packing of common signed width-five clauses under four-block options.
Selecting any subset or any alternative five-projection covering basis within
this length bound cannot repair the obstruction.

This closes only the bounded-length specialization. GATE-004AF remains open
with blocks of length at least 72, and no circuit or terminal conclusion is
inferred.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform complete length-at-most-68 alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot |
| Regime | Bounded-length witness no-go; GATE-004AF and P versus NP remain open |
