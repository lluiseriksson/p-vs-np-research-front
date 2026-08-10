# GATE-004AF-LENGTH72-ONLY — use every standard block through length 72

**Label: NO-GO**

LEMMA-083 proves that the complete identifier range 1 through 65,535 retains
the same linear width-five packing under four-block options. Thus no selection
of standard neutral blocks of length at most 72 proves GATE-004AF.

Identifier 98,370 at length 76 repairs the representative, so this is not a
grammar-wide obstruction. The full gate remains open with the larger bound,
and no circuit or terminal conclusion is inferred.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform complete length-at-most-72 alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot |
| Regime | Bounded-length witness no-go; GATE-004AF and P versus NP remain open |
