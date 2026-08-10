# GATE-004AD-IDENTIFIER68-ONLY — reuse the width-three alphabet

**Label: NO-GO**

LEMMA-073 proves that identifiers 1 through 68 with up to three blocks retain
`N/8-O(1)` disjoint common signed width-four clauses. Therefore the alphabet
that proves GATE-004AB cannot simply be reused one width higher. GATE-004AD
remains open for a richer fixed alphabet; no circuit loss is inferred.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block contexts and signed width-four matching |
| Uniform/non-uniform | Uniform identifier-68 alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot |
| Regime | Alphabet-specific no-go; GATE-004AD and P versus NP remain open |
