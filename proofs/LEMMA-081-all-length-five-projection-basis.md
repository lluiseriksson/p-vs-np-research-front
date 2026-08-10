# LEMMA-081 — projection-complete representatives for every identifier length

**Label: PROVED**

For each identifier bit length from one through fifteen, there is an explicit
finite subset whose restrictions realize every assignment on every set of at
most five non-leading bit positions. The union contains 2,066 identifiers.

For `n` free positions, `verification/covering_basis.py` uses strength
`min(5,n)` and deterministically enumerates hash-derived rows until every
column-pattern obligation is removed. The row counts for `n=0,...,14` are

`1,2,4,8,16,32,63,113,181,211,213,266,327,325,304`.

The exact checker verifies no missing obligation at any length. Coverage at
strength five implies coverage at every smaller strength by extending a
smaller column set to five columns and then restricting the realized pattern.

For a fixed aligned placement and at most five selected outer coordinates,
the induced bits of `01 T_j` or `10 F_j` are determined by fixed syntax bits
and at most five distinct non-leading identifier columns; repeated occurrences
of a column in the two variable copies must agree. Therefore the basis contains
an identifier of the same length inducing every five-coordinate mask induced
by any identifier of that length. Taking all lengths, the 2,066-row basis is
behaviorally complete on five coordinates for all identifiers 1 through
32,767.

This is a finite projection theorem only. It does not assert universality of
unions of blocks or any circuit consequence.

## Model card

| Field | Value |
|---|---|
| Computational model | Gamma-coded identifier words, exact covering arrays, and five-coordinate projections |
| Uniform/non-uniform | Uniform deterministic construction of a fixed representative basis; no circuit selected |
| Circuit size | No lower bound; 2,066 representatives cover every five-coordinate behavior of 32,767 identifiers |
| Circuit depth | Not applicable; later circuits unrestricted |
| Fan-in | Encoded formulas later use AND/OR two and NOT one |
| Randomness | None; SHA-256 is only a deterministic public row generator |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite binary incidence only |
| Asymptotic quantifiers | Exact finite statement for all fifteen identifier lengths and every projection of size at most five |
| Regime | Projection-equivalence theorem; not a circuit, promise, average-case, or terminal result |
