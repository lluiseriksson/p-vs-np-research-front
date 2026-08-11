# Cycle 118 two-row collision audit

## Structural witness

**Label: PROVED**

LEMMA-147 proves that `m` globally non-raw functions may all restrict to their
corresponding raw inputs on both selected rows while costing only one shared
base predicate plus `m` binary gates.

## Closed method

**Label: NO-GO**

GATE-004AW-TWO-ROWS-ONLY records that two cofactor tables, global non-rawness,
and linear-size realizability cannot yield the desired `b=o(m)` collision
bound.

## Refined gate

**Label: EXPLORATORY**

GATE-004AX replaces the two separate GATE-004AW inequalities by the weaker
and exactly sufficient tradeoff

`Q_J-b>=4m-2(Delta+K)`.

A collision may now be paid for by cross-row quotient surplus. A proof must
use minimum-circuit exchange, more canonical rows, or an injective structural
charge; the two observed rows alone are insufficient.

## Scope

**Label: EXPLORATORY**

No minimum-circuit collision bound, implication-stability theorem, SAT lower
bound, or terminal result is claimed.
