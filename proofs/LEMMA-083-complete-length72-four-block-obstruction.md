# LEMMA-083 — every length-at-most-72 identifier block retains mask 16

**Label: PROVED**

Identifiers 1 through 65,535 are exactly the standard neutral blocks of length
at most 72. No union of at most four nonoverlapping aligned blocks from this
complete alphabet realizes zero mask 16, bit pattern `11110`, on
`(70,71,80,85,86)`.

The direct interval DP enumerates the literal full range and returns mask 16
as the sole missing ordinary mask. Independently, the LEMMA-081 construction
extends to the 371-row strength-five basis for sixteen-bit identifiers; the
combined 2,437 representatives through that length cover every possible
five-coordinate block behavior and give the same DP result.

The translation argument of LEMMA-082 is unchanged. Offsets
`{0,1,10,15,16}` translated by multiples of twenty are disjoint, and `A_rho`
can repair at most one because `11110` consumes four one positions. Hence
`N/20-O(1)` disjoint common signed width-five clauses survive.

This closes all block lengths through 72. It does not cover identifier bit
length seventeen, whose neutral blocks have length 76.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, direct and projection-reduced interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-65535 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/20-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length witness obstruction; not a circuit or terminal result |
