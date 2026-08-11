# Cycle 162 — boundary-mask audit

**Label: PROVED**

LEMMA-195 classifies every direct shared exit from `h` through the nonzero
difference region `Delta`: an AND mask is zero on `Delta`, while an OR mask is
one there. A uniform local family has arbitrarily many nonconstant aligned AND
boundaries while preserving `fanout(g)=1`, so boundary count is `NO-GO`.
GATE-004CP must use shared realization cost and reconvergence.

## Classification

- LEMMA-195: `PROVED`
- GATE-004CO-BOUNDARY-COUNT-ONLY: `NO-GO`
- GATE-004CP: `EXPLORATORY`
