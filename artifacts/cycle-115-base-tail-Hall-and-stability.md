# Cycle 115 base-tail Hall and quotient-stability audit

## Lifted Hall lower bound

**Label: PROVED**

LEMMA-144 fixes a satisfying base assignment and applies full tail Hall inside
the joint circuit. It proves `C(H AND W_m)>=h+(p+2)m-1` and bounds the
canonical deficit from the displayed circuit by `K-h+1<=K=o(m)`.

## Semantic stability gate

**Label: EXPLORATORY**

GATE-004AU asks for at least `7m-2(Delta+K)` tail-dependent diagonal classes
in some minimum circuit. Together with LEMMA-144 this would give negative
loss for sufficiently large canonical parameters without exact additivity.

## Failed size-only promotion

**Label: NO-GO**

Distinct global gate functions may collide or become inactive after the two
row restrictions. Parent near-minimality alone does not bound that collapse.
The next brick is a row-cofactor collision charge using canonical suffix
dependence or the explicit slack budget.

## Scope

**Label: EXPLORATORY**

No quotient-stability theorem, SAT lower bound, or terminal result is claimed.
Real progress toward P versus NP remains zero.
