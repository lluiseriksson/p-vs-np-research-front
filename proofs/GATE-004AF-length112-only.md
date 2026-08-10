# GATE-004AF-LENGTH112-ONLY — use every standard block through length 112

**Label: NO-GO**

LEMMA-099 proves that the complete identifier range through 67,108,863 retains
a linear common signed width-five packing under four-block options. Therefore
no standard-block construction restricted to length at most 112 proves
GATE-004AF.

LEMMA-100 repairs the displayed type at length 116. The complete length-116
audit and the full gate remain open. No circuit lower bound or terminal
conclusion is inferred.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform complete length-at-most-112 alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot |
| Regime | Bounded-length worst-case witness no-go; GATE-004AF and P versus NP remain open |
