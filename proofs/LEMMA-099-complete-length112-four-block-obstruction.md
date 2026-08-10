# LEMMA-099 — the mask-16 obstruction survives every block through length 112

**Label: PROVED**

Identifiers 1 through 67,108,863 are exactly the complete standard neutral
alphabet of block length at most 112. No union of at most four nonoverlapping
aligned blocks realizes mask 16, pattern `11110`, on
`(112,124,132,137,138)`.

The exact symbolic oracle omits mask 16 at both intermediate length 108 and
length 112. At length 112, a separately derived 1,232-identifier basis has
zero selected-projection coverage failures; its literal DP agrees exactly.
Twenty-eight-spaced translations of `{0,12,20,25,26}` leave
`N/28-O(1)` common signed width-five clauses after at most one `A_rho` repair.

LEMMA-100 gives an explicit length-116 repair, so the claim is not extrapolated
beyond its stated bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, symbolic and projection-complete literal interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-67108863 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/28-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Exact complete bounded-length worst-case witness obstruction; not promise, average-case, distributional, circuit, or terminal progress |
