# Cycle 110 nested-theta exclusion audit

## Source reduction

**Label: PROVED**

LEMMA-131 fixes the first nested source bit and proves that the residual graph
has cycle rank at most one. The one-bit clause dichotomy then charges `m` NOTs
in the uncut case or `m-1` downstream NOTs in the cut case.

## Exclusion cascade

**Label: PROVED**

For `W_6` with three NOTs, both cases are impossible. GATE-004AQ, GATE-004AP,
GATE-004AO, and GATE-004AN are therefore proved in sequence. LEMMA-132 closes
dependency-cone Hall for all subset sizes one through six.

## Scope

**Label: EXPLORATORY**

The proof is a local fixed-sign circuit theorem. Size seven, full Hall,
minimum-quotient survival, unrestricted SAT lower bounds, and P versus NP
remain open. No proof-assistant certification is claimed.
