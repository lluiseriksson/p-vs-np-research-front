# Cycle 119 common-mask exchange audit

## Exact exchange

**Label: PROVED**

LEMMA-148 factors an exposed common OR mask out of `b` implication clauses,
rewriting `4b-1` gates as `3b` and saving exactly `b-1`. Therefore no such
module with `b>=2` occurs unchanged in a minimum circuit.

## Normal-form boundary

**Label: NO-GO**

GATE-004AX-COMMON-MASK-ONLY records that a two-row raw cofactor does not imply
an OR-mask representation, a common mask, or exposed clause-local uses. An
XOR with a base predicate vanishing on the selected rows is an exact
constant-overhead witness.

## Next attack

**Label: EXPLORATORY**

GATE-004AX remains active. A proof must derive a minimum-circuit collision
normal form, or charge every non-factorable witness to new quotient classes or
to the `Delta+K` slack. The distributive exchange is available only after
that structural classification.

## Scope

**Label: EXPLORATORY**

No collision normal form, quotient-stability theorem, SAT lower bound, or
terminal result is claimed.
