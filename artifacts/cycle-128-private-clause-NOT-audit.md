# Cycle 128 private-clause NOT audit

## Read-once localization

**Label: PROVED**

LEMMA-157 proves that every implication pair is a canonical two-leaf OR
subtree after unate normalization. Opposite variable polarities force a
private NOT in each disjoint pair subtree. With exactly `m` NOT gates, these
private gates exhaust the formula and every neutral clause restriction prunes
one.

## Extreme-stratum closure

**Label: PROVED**

No NOT remains for the base, so it has a monotone read-once formula and
`sigma=0`. Hence a positive maximal deficit cannot occur. GATE-004BC is proved
and GATE-004BB collapses to the zero-deficit recurrence.

## Next attack

**Label: EXPLORATORY**

GATE-004BD isolates the first unresolved stratum `mu_m=m+1`, equivalently
`Delta_m=sigma-1`. Its satisfying-base residual may have one cycle, one extra
NOT, or a higher-rank equality configuration, so read-once uniqueness alone
no longer applies.

## Scope

**Label: EXPLORATORY**

No intermediate-deficit localization, full GATE-004BA, SAT lower bound, or
terminal result is claimed.
