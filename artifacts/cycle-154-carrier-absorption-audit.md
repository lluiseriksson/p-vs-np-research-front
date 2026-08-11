# Cycle 154 — carrier absorption audit

**Label: PROVED**

LEMMA-187 defines a pruning-independent Boolean-difference carrier and proves
that its equal-output boundary gates are binary. This gives canonical regions
but does not make them deletion events.

GATE-004CG-CARRIER-COVERAGE-ONLY is `NO-GO`: after one upstream contraction,
arbitrarily many pair-sensitive downstream gates can survive as essential base
computation. GATE-004CH is the next exact brick. It must compare all three
minimum satisfying pruning maps and show that carrier absorption is cross-code
incompatible, or turn a shared absorption into the private/non-bridge
contradiction.

## Classification

- LEMMA-187: `PROVED`
- GATE-004CG-CARRIER-COVERAGE-ONLY: `NO-GO`
- GATE-004CH: `EXPLORATORY`
- GATE-004CG: remains `EXPLORATORY`
