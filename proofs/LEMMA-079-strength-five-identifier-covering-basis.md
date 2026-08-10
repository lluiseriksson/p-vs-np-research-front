# LEMMA-079 — an explicit strength-five identifier-bit covering basis

**Label: PROVED**

There is an explicit set of 318 fifteen-bit identifiers such that, on every
choice of five among the fourteen non-leading binary positions, all 32 bit
patterns occur.

`verification/covering_basis.py` defines the set deterministically. It hashes
the ASCII strings `p-vs-np-width5-k`, takes the low fourteen bits of the first
two digest bytes, prefixes the mandatory leading one, rejects duplicates, and
stops only when an explicit set of all

`C(14,5)*32 = 64,064`

column-pattern obligations is empty. The independent checker
`strength_five_coverage_failures` recomputes every projection and returns the
empty tuple. A regression test fixes the cardinality at 318 and checks the
complete obligation set.

Every resulting neutral block has length 68. This theorem concerns only the
free binary segment of gamma-coded identifiers. It does not cover fixed root,
unary-prefix, separator, or duplicated-variable token positions and therefore
does not imply GATE-004AF.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit binary covering array and exact finite enumeration |
| Uniform/non-uniform | Uniform deterministic construction of one fixed identifier set; no circuit selected |
| Circuit size | No lower bound; 318 rows cover 64,064 finite obligations |
| Circuit depth | Not applicable; later circuits unrestricted |
| Fan-in | Encoded formulas later use AND/OR two and NOT one |
| Randomness | None; SHA-256 is used only as a deterministic public row generator |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite binary incidence only |
| Asymptotic quantifiers | Exact finite statement over all five-column subsets and all 32 patterns |
| Regime | Identifier-bit construction lemma; not a circuit, average-case, promise, or terminal result |
