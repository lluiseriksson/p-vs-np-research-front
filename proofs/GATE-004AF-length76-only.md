# GATE-004AF-LENGTH76-ONLY — use every standard block through length 76

**Label: NO-GO**

LEMMA-088 proves that the complete identifier range 1 through 131,071 retains
a linear common signed width-five packing under four-block options. Therefore
no subset, covering basis, or alternative selection of standard blocks of
length at most 76 can prove GATE-004AF.

This closes only the bounded-length specialization. Blocks of length at least
80 and the full GATE-004AF construction remain open. No circuit lower bound or
terminal conclusion is inferred.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform complete length-at-most-76 alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot |
| Regime | Bounded-length witness no-go; GATE-004AF and P versus NP remain open |
