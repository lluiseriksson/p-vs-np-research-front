# Cycle 132 external-leaf defect audit

## Defect theorem

**Label: PROVED**

LEMMA-161 proves that `L` fixed external leaf occurrences can hide at most
`L` of the clause-private NOTs visible in a residual `W_b` formula. The proof
is an injection from bad disjoint NOT subtrees to external leaf occurrences.

## No-cut closure

**Label: PROVED**

GATE-004BG-NO-CUT applies the defect theorem to both formula regions. If
neither side contained a private clause, `j<=h+2=K+3-sigma`, contradicting
the operational `j>=K+sigma` for `sigma>=2`.

## Next attack

**Label: EXPLORATORY**

GATE-004BI isolates the sole-cut partition. LEMMA-161 closes it whenever
`j-1>h_Y+3` via LEMMA-162; the remaining constant-width edge must use equality of the two
`z` occurrences and the semantics of the cut-clause half.

## Scope

**Label: EXPLORATORY**

No sole-cut closure, full unicyclic pruning, SAT lower bound, or terminal
result is claimed.
