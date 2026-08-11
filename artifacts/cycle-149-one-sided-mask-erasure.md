# Cycle 149 — one-sided mask erasure audit

**Label: PROVED**

LEMMA-182 proves an exact semantic normal form for the one-sided first
cancellation. At an OR mask, meet the two satisfying cofactors of the path
input; at an AND mask, join them. On that input edge the `01/11` difference
vanishes while all four cofactors of the cancellation gate remain unchanged.

GATE-004CB-SEMANTIC-ERASURE-ONLY is `NO-GO`: the new edge signal has no free
AND/OR/NOT realization, and shared fanout prevents treating an edge change as
a global gate replacement. GATE-004CC is the next exact gate: realize the
erasure at equal size in a circuit lexicographically minimizing pair
sensitivity and satisfying-signature variation, or force a forbidden resource
loss.

## Classification

- LEMMA-182: `PROVED`
- GATE-004CB-SEMANTIC-ERASURE-ONLY: `NO-GO`
- GATE-004CC: `EXPLORATORY`
- GATE-004CB: remains `EXPLORATORY`
