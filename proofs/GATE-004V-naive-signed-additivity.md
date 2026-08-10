# GATE-004V-NAIVE-SIGNED-ADDITIVITY — signed clauses inherit the positive exact-cost formula

**Label: NO-GO**

## Falsifiable route attempted

Attempt: extend LEMMA-048 to signed disjoint clauses by assigning a fixed
extra gate charge to each negated literal, so the exact extension cost and
joint-quotient loss depend only on base size `K`, clause widths, and literal
signs. Apply that identity to any signed clauses common to the balanced slot
product.

The route predicts, already for one fresh negative unit clause, a fixed
increment

`C(H AND NOT z)-C(H)`

independent of the nonconstant disjoint base `H`.

## Failure

LEMMA-054 gives two exact cases. With `H=x`, the increment is two. With
`H=NOT x`, De Morgan sharing computes the extension as `NOT(x OR z)`, and the
increment is one. The base size and the signed suffix alone therefore do not
determine the additive cost.

Hence LEMMA-048 cannot be promoted to signed clauses merely by counting NOT
gates per literal. Any valid signed-tail theorem must track at least output
polarity or complement-complexity data, and must reprove its quotient count
for the selected implementation.

## Scope and next attack

This is a no-go for a specific accounting method. It neither excludes signed
common predicates nor supports positive GATE-004V rigidity. A complement-
sensitive signed-clause analysis and overlapping/nonclausal predicates remain
open.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits for a nonconstant base conjoined with a fresh negated literal; intended exact semantic joint-quotient application |
| Uniform/non-uniform | Fully non-uniform base; explicit finite counterexamples to a universal accounting identity |
| Circuit size | The same fresh signed unit tail has increments two over `x` and one over `NOT x` |
| Circuit depth | Unrestricted; exact lower bounds rule out sizes below the displayed size-two circuits |
| Fan-in | `AND`/`OR` two; `NOT` one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Universal proposed identity over all nonconstant disjoint bases is falsified by two variables; no asymptotic circuit claim is made |
| Regime | Worst-case exact method no-go; signed predicates, GATE-004V, and P versus NP remain open |
