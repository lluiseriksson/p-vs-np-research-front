# LEMMA-094 — the mask-16 obstruction survives every block through length 96

**Label: PROVED**

Identifiers 1 through 4,194,303 are exactly the complete standard neutral
alphabet of block length at most 96. The exact LEMMA-087 symbolic oracle finds
that no union of at most four nonoverlapping aligned blocks realizes mask 16,
pattern `11110`, on `(96,104,112,117,118)`.

The same query at the intermediate length-92 bound also omits mask 16.
Twenty-four-spaced translations of offsets `{0,8,16,21,22}` are disjoint, and
`A_rho` repairs at most one. Therefore an `N/24-O(1)` common signed width-five
packing survives every standard block through length 96.

The symbolic-oracle equivalence is a proved finite template theorem, not a
heuristic sample. LEMMA-095 gives an explicit length-100 repair, so this result
is not extrapolated beyond its stated bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Complete symbolic four-block neutral alphabet, one long option, signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform complete identifier-1-through-4194303 alphabet and translations; no circuit selected |
| Circuit size | No lower bound; common signed width-five packing `N/24-O(1)` per slot |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently large four-divisible slot; every eligible translation except at most one |
| Regime | Exact complete bounded-length witness obstruction; not a circuit or terminal result |
