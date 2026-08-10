# LEMMA-086 — a projection-complete basis through block length 76

**Label: PROVED**

The deterministic covering construction at seventeen-bit identifier length
uses 436 rows and has no missing strength-five projection. Together with all
shorter length bases, it yields 2,873 distinct identifiers.

For every aligned neutral block `01 T_j` or `10 F_j` with
`1<=j<=131071` and every selection of at most five outer coordinates, one of
the 2,873 representatives has the same identifier bit length and induces the
same selected-coordinate pattern. The proof is the fixed-token/free-column
argument of LEMMA-081, now including sixteen free identifier columns.

Thus exact audits using these representatives are behaviorally complete for
the full standard alphabet of block length at most 76. This does not itself
prove four-block universality; it only gives the finite representative basis
for that audit.

## Model card

| Field | Value |
|---|---|
| Computational model | Gamma-coded identifier words, exact covering arrays, and five-coordinate projections |
| Uniform/non-uniform | Uniform deterministic fixed basis; no circuit selected |
| Circuit size | No lower bound; 2,873 representatives cover all five-coordinate behaviors through identifier 131,071 |
| Circuit depth | Not applicable; later circuits unrestricted |
| Fan-in | Encoded formulas later use AND/OR two and NOT one |
| Randomness | None; SHA-256 is only a deterministic public row generator |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite binary incidence only |
| Asymptotic quantifiers | Exact finite statement for all seventeen identifier lengths and projections of size at most five |
| Regime | Projection-equivalence theorem; not a universality, circuit, or terminal result |
