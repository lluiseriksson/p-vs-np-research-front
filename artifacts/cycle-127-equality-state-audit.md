# Cycle 127 equality-state audit

## Exact potential

**Label: PROVED**

LEMMA-156 combines maximal-deficit formula rigidity with the primary
Morizumi lower-bound potential. Every endpoint minimum is variable-read-once;
on every canonical tail chain its `m`-NOT down-state potential starts at zero,
ends at `m`, rises exactly one at each clause failure, and stays constant at
each repair.

## Scalar boundary

**Label: NO-GO**

Constant potential can hide paired NOT-state swaps. An explicit abstract
two-label trace has the exact required cardinalities but no persistent label
for the first clause. This is not a formula-realizability counterexample.

## Next attack

**Label: EXPLORATORY**

GATE-004BC asks for one neutral clause restriction that prunes at least one
NOT from the equality formula. Iterating that single operation proves the
maximal-deficit localization gate GATE-004BB.

## Scope

**Label: EXPLORATORY**

No one-clause pruning theorem, full positive-deficit localization, SAT lower
bound, or terminal result is claimed.
