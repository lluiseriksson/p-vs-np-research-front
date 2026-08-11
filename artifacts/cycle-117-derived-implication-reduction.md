# Cycle 117 derived implication reduction audit

## Exact reduction

**Label: PROVED**

LEMMA-146 proves that the four-positive/one-negative width-five extension has
exact size `3m` plus its implication extension. Substitution preserves
minimum size and transfers `3m-b` quotient classes, with `2m` prefixes
unconditionally new.

## Refined gate

**Label: EXPLORATORY**

GATE-004AW asks for `4m-(Delta+K)` implication quotient and at most
`Delta+K` raw-input cofactor collisions. Together they imply GATE-004AU
exactly.

## Prefix boundary

**Label: NO-GO**

Exact substitution alone leaves two independent linear gaps: implication
cross-row surplus and full-OR output collisions. Prefix-only transfer does not
close quotient stability.

## Scope

**Label: EXPLORATORY**

No implication-stability theorem, SAT lower bound, or terminal result is
claimed.
