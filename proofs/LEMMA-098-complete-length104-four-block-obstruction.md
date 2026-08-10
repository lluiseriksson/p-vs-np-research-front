# LEMMA-098 — every length-at-most-104 identifier block retains mask 16

**Label: PROVED**

Identifiers 1 through 16,777,215 are exactly the complete standard neutral
alphabet of block length at most 104. No union of at most four nonoverlapping
four-aligned blocks realizes mask 16, pattern `11110`, on
`(104,116,124,129,130)`.

The exact 640,000-type sweep finds `8,12,12,12` failures by residue, 44 total.
On the displayed representative, a separately derived 985-identifier basis
has zero selected-projection coverage failures. Its literal interval DP and
the symbolic oracle independently agree that only mask 16 is missing.

Twenty-eight-spaced translations of offsets `{0,12,20,25,26}` are disjoint.
`A_rho` repairs at most one because `11110` consumes four of its six one
positions. Thus `N/28-O(1)` common signed width-five clauses survive.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, symbolic and projection-complete literal interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-16777215 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/28-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length worst-case witness obstruction; not promise, average-case, distributional, circuit, or terminal progress |
