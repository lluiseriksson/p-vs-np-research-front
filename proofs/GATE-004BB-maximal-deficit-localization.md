# GATE-004BB — localize maximal deficit in the formula stratum

**Label: PROVED**

Use the notation of LEMMA-153 and assume the endpoint deficit is maximal:

`Delta_m=sigma`.

Put

`k_max=min(m,K+sigma)`.

## Theorem

Then

`Delta_{k_max}=sigma`.

Equivalently, prove that `J_{k_max}` has a circuit with

`N+r<=k_max`.

Indeed, LEMMA-155 turns every endpoint minimum circuit under
`Delta_m=sigma` into a variable-read-once formula with exactly `m` NOT gates.
LEMMA-157 then forces `sigma=0`: the `m` implication pairs consume one private
NOT apiece and no NOT remains for a nontrivial base surplus. Since LEMMA-152
makes `Delta_j` nondecreasing from `Delta_0=0` to `Delta_m=0`, every prefix
deficit is zero. In particular `Delta_{k_max}=0=sigma`.

## Relation to the active chain

This is exactly the maximal-deficit stratum of GATE-004BA. Its proof does not
settle intermediate deficits `0<Delta_m<sigma`; it closes only the extreme
endpoint, which collapses to the already exact zero-deficit stratum.

LEMMA-155 supplies the rank-zero structure, LEMMA-156 audits equality in the
NOT-state potential, and LEMMA-157 supplies the decisive private-NOT theorem
from exact implication polarity and read-once minterm geometry.

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
| Regime | Exact worst-case maximal-deficit subgate of GATE-004BA; not the intermediate positive-deficit theorem, a SAT lower bound, or a terminal result |
