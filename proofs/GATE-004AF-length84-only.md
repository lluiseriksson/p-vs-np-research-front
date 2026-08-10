# GATE-004AF-LENGTH84-ONLY — use every standard block through length 84

**Label: NO-GO**

LEMMA-091 proves that the complete identifier range 1 through 524,287 retains
a linear common signed width-five packing under four-block options. Therefore
no subset, covering basis, or alternative selection of standard blocks of
length at most 84 can prove GATE-004AF.

This closes only the bounded-length specialization. Blocks of length at least
88 and the full GATE-004AF construction remain open. No circuit lower bound or
terminal conclusion is inferred.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform complete length-at-most-84 alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot |
| Regime | Bounded-length witness no-go; GATE-004AF and P versus NP remain open |
