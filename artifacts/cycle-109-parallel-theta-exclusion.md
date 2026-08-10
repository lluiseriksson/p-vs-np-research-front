# Cycle 109 parallel-theta exclusion audit

## Orientation dichotomy

**Label: PROVED**

LEMMA-129 proves that two binary theta splits are either two parallel sources
or one source followed by a nested split.

## Parallel exclusion

**Label: PROVED**

LEMMA-130 uses exact unfolding equality to place all three NOT gates in the
two source trees, leaving a monotone downstream formula. All negative inputs
must then belong to source groups, but the one-bit dichotomy shows those groups
can cover at most three, four, or two negative inputs according to their cut
patterns—never six.

## Remaining gate

**Label: NO-GO**

Only the nested split remains in GATE-004AQ. Its second bit depends on the
first, so the independent-source proof cannot be reused. A sequential
cofactor and path-region theorem is next; no sextet Hall or terminal result is
claimed.
