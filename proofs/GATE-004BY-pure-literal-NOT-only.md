# GATE-004BY-PURE-LITERAL-NOT-ONLY — expose `NOT u` inside a plateau

**Label: NO-GO**

## Attempt

Locate a physical `NOT u` gate for the fresh negative literal and delete it
under a satisfying pair restriction, exactly as in the displayed three-gate
extension.

## Failure

Under the two-gate plateau, LEMMA-178 preserves every NOT under each of
`00`, `01`, and `11`. Any NOT whose input depends only on the fixed pair
becomes constant and would be deleted. LEMMA-179 proves more: every NOT that
carries the required negative `u` dependence also depends on base variables,
and its input is already an internal mixed binary gate with no direct `u` or
`t` wire.

Therefore the canonical literal-NOT architecture describes the three-gate
increment, not the only remaining two-gate plateau. Ruling out the plateau
requires uncrossing a mixed surviving NOT; it cannot begin by assuming the
resource is clause-private.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted base–implication circuits under the exact two-gate equality and satisfying-code restrictions |
| Uniform/non-uniform | Every finite non-uniform plateau parent; no uniform normalization supplied |
| Circuit size | All parent NOTs survive; no pure-pair NOT can be the deletable resource |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean polarity and restriction survival only |
| Asymptotic quantifiers | Every nonconstant base, fresh implication pair, and minimum parent satisfying `C(F)=C(A)+2` |
| Regime | Structural no-go for literal-NOT-only pruning; not a counterexample to GATE-004BY, SAT lower bound, or terminal result |
