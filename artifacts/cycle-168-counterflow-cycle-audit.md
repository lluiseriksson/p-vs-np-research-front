# Cycle 168 — counterflow-cycle audit

**Label: PROVED**

LEMMA-201 turns each counterflow boundary into a named nonzero cycle
coordinate `gamma_b`: the two `u`-dependent routes diverge after their last
common vertex and reconverge at the boundary. Exact plateau rank preservation
then forces that coordinate to remain nonzero in all three satisfying minors,
although contractions may change its edge support.

This closes the “cycle exists, therefore it is lost” route as `NO-GO`.
GATE-004CV now asks for the missing quantitative step: separate the coordinate
from common base topology or factor the reuse into a strict descent.

## Classification

- LEMMA-201: `PROVED`
- GATE-004CU-CYCLE-EXISTENCE-ONLY: `NO-GO`
- GATE-004CV: `EXPLORATORY`

No SAT lower bound, plateau exclusion, or terminal implication is claimed.
