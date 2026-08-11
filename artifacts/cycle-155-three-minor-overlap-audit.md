# Cycle 155 — three-minor overlap audit

**Label: PROVED**

LEMMA-188 proves that any two satisfying minimum prunings share at least
`K-2` physical parent gates and all three share at least `K-4`; every NOT lies
in the common backbone.

GATE-004CH-OVERLAP-ONLY is `NO-GO`: an exact-table AND/OR/NOT circuit has one
physical binary gate surviving all satisfying restrictions while computing
`x OR z` in two and `y OR z` in the third. Physical overlap is not semantic
alignment. GATE-004CI is the next exact brick and adds the finite potential
`W` counting misaligned common-backbone gates.

## Classification

- LEMMA-188: `PROVED`
- GATE-004CH-OVERLAP-ONLY: `NO-GO`
- GATE-004CI: `EXPLORATORY`
- GATE-004CH: remains `EXPLORATORY`
