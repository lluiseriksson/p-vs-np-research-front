# Cycle 152 — four-code kernel audit

**Label: PROVED**

LEMMA-185 combines plateau equality with the graph-minor audit: every
satisfying restriction loses exactly two binary gates but no NOT or cycle-rank
resource. Cyclic gates can disappear only by rank-neutral contraction; no
non-bridge edge can be deleted.

GATE-004CE-FOUR-CODE-SIGNATURES-ONLY is `NO-GO`. An explicit AND/OR/NOT
circuit has the exact cofactor table `A,A,0,A`, two cancellation fronts, and a
shared cycle surviving all three satisfying restrictions. It is deliberately
not claimed minimum.

GATE-004CF is the next exact brick: use minimum-parent structure to require a
third binary elimination or a noncontractible cycle-edge deletion within the
two-gate budget, unless a private substitution certificate exists.

## Classification

- LEMMA-185: `PROVED`
- GATE-004CE-FOUR-CODE-SIGNATURES-ONLY: `NO-GO`
- GATE-004CF: `EXPLORATORY`
- GATE-004CE: remains `EXPLORATORY`
