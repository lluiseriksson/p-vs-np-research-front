# Cycle 123 negation-cycle resource localization audit

## Sharpened recurrence

**Label: PROVED**

LEMMA-152 is strengthened: implication deficits increase only by zero or one.
The proof uses `u_j=1` and the exact one-gate cost of conjoining a fresh
positive input.

## Exact resource identity

**Label: PROVED**

LEMMA-153 proves

`C(J_j)=h+2j-1+mu_j`, `Delta_j=sigma+j-mu_j`,

where `mu_j` is the minimum `N+r`. A saving is exactly a plateau in this
resource count.

## Small-witness gate

**Label: EXPLORATORY**

GATE-004BA asks that the final deficit already be attained by
`min(m,K+Delta_m)` clauses. It is exactly equivalent to GATE-004AZ.

## Hall boundary

**Label: NO-GO**

A cycle incidence system satisfies every Hall inequality but has surplus one
on every proper subset and zero surplus only globally. Hall cardinalities
alone therefore permit a final unit saving.

## Scope

**Label: EXPLORATORY**

No Boolean-circuit saving localization, positive-deficit stability, SAT lower
bound, or terminal result is claimed.
