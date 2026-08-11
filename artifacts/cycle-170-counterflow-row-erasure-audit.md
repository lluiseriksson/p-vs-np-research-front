# Cycle 170 — counterflow row-localization and erasure audit

**Label: PROVED**

LEMMA-203 confines every size-three counterflow to the `00/10` row. The
`01/11` cofactors of its auxiliary input are equal, so no same-row pair of
satisfying minors exposes the counterflow difference.

LEMMA-204 then gives an exact semantic erasure: use the meet of the two
row-zero cofactors at an AND boundary and their join at an OR boundary. All
four boundary cofactors remain unchanged. The replacement is an abstract edge
function, not a same-size circuit.

A finite regression enumerated all 64 assignments of the explicit six-input
underdetermination witness and all admissible Boolean quadruples in the
meet/join identities. Both checks passed. The human proofs, not the finite
regression, carry the `PROVED` labels.

## Classification

- LEMMA-203: `PROVED`
- GATE-004CW-SATISFYING-TRANSPORT-ONLY: `NO-GO`
- LEMMA-204: `PROVED`
- GATE-004CW-SEMANTIC-ERASURE-ONLY: `NO-GO`
- GATE-004CX: `EXPLORATORY`

GATE-004CX now asks for an explicit fanout-preserving basis rewrite or an
exact resource contradiction. No plateau exclusion, SAT lower bound, or
terminal implication is claimed.
