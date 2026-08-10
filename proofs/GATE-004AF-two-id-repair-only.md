# GATE-004AF-TWO-ID-REPAIR-ONLY — repair only the first two missing masks

**Label: NO-GO**

Identifiers 1,089 and 1,098 repair the LEMMA-077 representative, but LEMMA-078
exhibits a new translation-stable mask-8 failure and a linear common signed
width-five packing. Exact enumeration also finds 1,787 local failures with all
four gaps at most 20.

This closes only the 94-identifier specialization. A broader same-bound
alphabet or a larger fixed alphabet may still prove GATE-004AF; no circuit
loss or terminal consequence is inferred.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform fixed 94-identifier alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot; exact local audit over 640,000 reduced types |
| Regime | Alphabet-specific no-go; GATE-004AF and P versus NP remain open |
