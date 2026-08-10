# LEMMA-104 — one block realizes either singleton zero on every interior pair

**Label: PROVED**

Using identifiers 1 through 68, every pair of distinct coordinates at least
36 positions from the slot boundaries realizes zero mask 1 and zero mask 2
with one four-aligned neutral block.

For gaps below 36, retain the exact gap. For a gap at least 36, no length-at-
most-36 block meeting one coordinate can meet the other. Reduce the other
coordinate, and the block with it when necessary, by a multiple of four to a
gap in `{36,37,38,39}`. Moving the coordinate not met by the block preserves
its padded one value. Thus there are `4*39=156` types.

`verification/triple_component_audit.py` checks both singleton masks on all
156 types with the literal bitset placement oracle and returns no failures.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact one-block SAT-gamma neutral contexts and two-coordinate zero masks |
| Uniform/non-uniform | Uniform identifiers 1 through 68 and aligned placements; no circuit selected |
| Circuit size | No lower bound; one local block witness |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently interior ordered coordinate pair |
| Regime | Exact local witness theorem; not a circuit lower bound or terminal result |
