# Cycle 126 maximal-deficit rigidity audit

## Equality-stratum theorem

**Label: PROVED**

LEMMA-155 proves that maximal deficit `Delta_m=sigma` forces every endpoint
minimum circuit to have exactly `m` NOT gates and cycle rank zero. Every NOT
survives every satisfying-base restriction, whose residual is a formula for
`W_m` with the same exact resource count.

## Localization boundary

**Label: NO-GO**

Rank zero, an endpoint count of `m` NOT gates, and survival under the base
restriction do not by themselves control what happens when clause signals
are fixed. The explicit wrong-polarity formula in
GATE-004BB-ENDPOINT-COUNTS-ONLY isolates the missing target semantics; it is
not a minimum-circuit or canonical counterexample.

## Next attack

**Label: EXPLORATORY**

GATE-004BB asks for maximal-deficit localization by `K+sigma` clauses. The
next proof attempt must classify equality in the formula inversion bound for
the exact one-negative clauses, or give a minimum-preserving exchange that
localizes the endpoint formula.

## Scope

**Label: EXPLORATORY**

No full positive-deficit localization, quotient stability, SAT lower bound,
or terminal result is claimed.
