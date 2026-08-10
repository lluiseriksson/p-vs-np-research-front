# LEMMA-096 — every length-at-most-100 identifier block retains mask 8

**Label: PROVED**

Identifiers 1 through 8,388,607 are exactly the complete standard neutral
alphabet of block length at most 100. No union of at most four nonoverlapping
four-aligned blocks from this alphabet realizes zero mask 8, equivalently
pattern `11101`, on `(100,112,120,123,124)`.

The exact symbolic sweep checks 640,000 types with four gaps in
`{1,...,20}`. It finds `10,12,12,12` failures by residue, 46 total. For the
displayed representative, a separately derived 851-identifier basis covers
every projection of the identifier bits touched by any relevant placement;
the coverage checker returns no failures. The original literal interval DP on
that basis and the LEMMA-087 symbolic oracle independently agree that mask 8
alone is missing.

Translate offsets `{0,12,20,23,24}` by multiples of twenty-eight. These
quintuples are disjoint. `A_rho` realizes `11101` on at most one because each
occurrence consumes four of its six one positions. Hence `N/28-O(1)` disjoint
common signed width-five clauses survive.

LEMMA-097 gives an explicit length-104 repair. This is a complete bounded-
length witness obstruction, not a circuit or terminal result.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete four-block neutral alphabet, symbolic and projection-complete literal interval DPs, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-8388607 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/28-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Complete bounded-length worst-case witness obstruction; not promise, average-case, distributional, circuit, or terminal progress |
