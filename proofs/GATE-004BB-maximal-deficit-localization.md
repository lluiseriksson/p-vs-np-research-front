# GATE-004BB — localize maximal deficit in the formula stratum

**Label: EXPLORATORY**

Use the notation of LEMMA-153 and assume the endpoint deficit is maximal:

`Delta_m=sigma`.

Put

`k_max=min(m,K+sigma)`.

## Falsifiable theorem

Prove

`Delta_{k_max}=sigma`.

Equivalently, prove that `J_{k_max}` has a circuit with

`N+r<=k_max`.

A compatible base and arbitrarily large clause count for which
`Delta_m=sigma` but `Delta_{k_max}<sigma` falsifies the theorem.

## Relation to the active chain

This is exactly the maximal-deficit stratum of GATE-004BA. A proof would not
settle smaller positive deficits, but it would close the extreme endpoint
left unresolved by the zero-deficit result and would give a genuine special
case of the saving-localization theorem.

LEMMA-155 supplies the new structure: every endpoint minimum circuit is a
formula with exactly `m` NOT gates, and all of them survive every satisfying
base restriction. The missing step is an equality-case formula theorem that
uses the exact implication polarity and minimum-circuit semantics to turn
those global `m` NOT occurrences into a circuit for a prefix of at most
`K+sigma` clauses with resource count at most that prefix length.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical base–implication circuits, with rank-zero endpoint structure supplied by LEMMA-155 |
| Uniform/non-uniform | Uniform symmetric clause family; fully non-uniform circuit minima and prefix circuits |
| Circuit size | Premise `Delta_m=sigma`; target `Delta_min(m,K+sigma)=sigma`, equivalently prefix `N+r<=k_max` |
| Circuit depth | Unrestricted; endpoint minimum circuits are formulas by LEMMA-155 |
| Fan-in | AND/OR two; NOT one; fanout unrestricted in prefix competitors |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean formula semantics and undirected cycle rank over `F_2` only |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance satisfying `Delta_m=sigma` |
| Regime | Falsifiable worst-case maximal-deficit subgate of GATE-004BA; not the full positive-deficit theorem, a SAT lower bound, or a terminal result |
