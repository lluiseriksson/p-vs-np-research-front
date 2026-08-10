# GATE-004AD-LENGTH48-ONLY — use all standard neutral blocks through length 48

**Label: NO-GO**

LEMMA-074 proves that even the complete alphabet of identifiers 1 through
1,023, hence every standard neutral block of length at most 48, retains a
linear packing of common signed width-four clauses under three-block options.
Selecting a clever subset of this alphabet cannot repair the obstruction.

This closes only the length-48 specialization. Explicit identifiers of length
52, 60, and 68 realize the missing patterns on the returned representatives,
so GATE-004AD remains open with a larger fixed alphabet and a correspondingly
larger finite translation audit.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block neutral contexts and signed width-four matching |
| Uniform/non-uniform | Uniform complete length-at-most-48 alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot |
| Regime | Bounded-length witness no-go; GATE-004AD and P versus NP remain open |
