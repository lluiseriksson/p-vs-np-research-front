# GATE-004DU-LONG-SUPPORT-PIGEONHOLE-ONLY — small cores remain

**Label: NO-GO**

Scope: use only oriented loss-union cardinality to conclude that every marked
swap cycle has a physical gate present in all three satisfying minors, then
close the contraction-aware support gate.

LEMMA-231 proves this conclusion only above four support gates in AND→OR and
above six in OR→AND. LEMMA-232 gives abstract exact-loss systems covering all
four or six symbols at the thresholds. Therefore pigeonhole counting leaves
bounded residual cores and cannot close GATE-004DU alone.

The set witnesses are not Boolean endpoints. A symbolic classification may
still rule them out using gate operations, swap signatures, path topology,
or minimality; those are precisely the missing premises.

## Model card

| Field | Value |
|---|---|
| Computational model | Oriented exact physical loss-set accounting for marked support gates |
| Uniform/non-uniform | Every finite hypothetical endpoint for the upper bounds and two finite abstract threshold witnesses |
| Circuit size | Parent `K+2`; union caps four/six; threshold supports four/six |
| Circuit depth | Unrestricted target; not applicable to abstract witnesses |
| Fan-in | Target AND/OR two and NOT one; set argument fan-in independent |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite physical gate sets and cardinality |
| Asymptotic quantifiers | Every marked support and both carrier orientations |
| Regime | Long-support-pigeonhole no-go; not endpoint counterexample, SAT lower bound, or terminal result |
