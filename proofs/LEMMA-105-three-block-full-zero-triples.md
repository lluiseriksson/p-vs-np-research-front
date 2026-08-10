# LEMMA-105 — three blocks realize `000` on every interior triple

**Label: PROVED**

Using identifiers 1 through 68, every triple of distinct coordinates at least
36 positions from the slot boundaries realizes zero mask 7 with at most three
nonoverlapping four-aligned neutral blocks.

LEMMA-102 with `B=36` safely reduces each gap to `{1,...,75}`. Hence the exact
domain has `4*75^2=22,500` types. The full-mask mode of
`QuartetAuditor.reached_masks_positions` keeps mask 7 rather than discarding
it as irrelevant to the earlier ordinary-mask audits. The exhaustive checker
`full_zero_triple_failures` returns no failures.

This complements LEMMA-071, which already realizes the six nonempty proper
zero masks with at most two blocks.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block SAT-gamma neutral contexts and full-zero triple incidence |
| Uniform/non-uniform | Uniform identifiers 1 through 68, placements, and safe finite reduction; no circuit selected |
| Circuit size | No lower bound; at most three local blocks |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every sufficiently interior ordered coordinate triple |
| Regime | Exact local witness theorem; not a circuit lower bound or terminal result |
