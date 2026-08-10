# GATE-004AD-INITIAL-LENGTH68-REPAIR-ONLY — first explicit longer repair set

**Label: NO-GO**

The first 86-identifier length-68 repair set closes every Cycle-070
counterquartet and 1,000 sampled reduced types, but the exhaustive audit finds
six failures among 1,431,644 types. They all start in residue 1 and omit zero
mask 8:

`(69,72,77,78)`, `(69,73,77,78)`, `(69,74,77,78)`,
`(69,75,77,78)`, `(69,76,81,82)`, `(69,77,81,82)`.

Run each residue with `quartet_type_audit_fast.py --length68-initial` to
reproduce the counts. This is a subset-specific NO-GO, not a length-68
obstruction: six additional identifiers repair the displayed failures.
LEMMA-075 covers its audited subdomain but its all-quartet extension is open.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block neutral contexts and four-coordinate pattern incidence |
| Uniform/non-uniform | Uniform fixed 86-identifier alphabet; no circuit selected |
| Circuit size | No lower bound; six finite missing-pattern types |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Exhaustive over all `4*71^3` reduced quartet types |
| Regime | Subset-specific construction no-go; the repaired alphabet remains exploratory globally, with P versus NP open |
