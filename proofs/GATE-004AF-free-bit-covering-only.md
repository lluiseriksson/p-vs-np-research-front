# GATE-004AF-FREE-BIT-COVERING-ONLY — cover every identifier-bit projection

**Label: NO-GO**

LEMMA-079 supplies exact strength-five coverage on every free identifier-bit
projection. Nevertheless LEMMA-080 exhibits a mask-16 failure caused by the
placement of selected coordinates across fixed syntax and gamma boundaries.
The 412-identifier alphabet retains a linear common width-five packing.

Thus free-bit covering arrays alone do not prove GATE-004AF. The next
construction must cover phased projections of the complete neutral-block
word, including root tokens, unary gamma prefixes, separators, and the second
variable copy. A refined same-bound alphabet remains open.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform fixed 412-identifier alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot; exact local audit over 640,000 types |
| Regime | Construction-method no-go; GATE-004AF and P versus NP remain open |
