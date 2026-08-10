# GATE-004AF-SINGLE-LENGTH76-REPAIR-ONLY — add only identifier 98,370

**Label: NO-GO**

LEMMA-084 repairs the old representative, but LEMMA-085 finds a shifted
mask-16 failure and a linear common signed width-five packing. The exact local
failure count remains 494. Thus one length-76 identifier is not a sufficient
basis for GATE-004AF.

The complete length-76 alphabet is not rejected: LEMMA-086 supplies its
projection-complete representative set, and initial sampling finds no failure.
That evidence remains EXPLORATORY pending an exhaustive or analytic audit.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts and signed width-five matching |
| Uniform/non-uniform | Uniform fixed 413-identifier alphabet; no circuit selected |
| Circuit size | No lower bound; linear surviving packing |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large compatible slot; exact local audit over 640,000 types |
| Regime | Alphabet-specific no-go; complete GATE-004AF and P versus NP remain open |
