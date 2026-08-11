# GATE-004CD — obtain a private budget or charge a shared exit

**Label: EXPLORATORY**

Fix a `(T_j,V_j)`-lexicographically extremal minimum plateau parent and a
one-sided first cancellation `p→d`. If `p` has no other live consumer, let
`R` be the maximal predecessor region ending at `p` whose only outgoing edge
is `p→d`; its boundary consists of all signals entering that region from
outside. If `p` already has another live consumer, take `R` to be empty and
take `p` as the first excluded predecessor with a shared exit.

## Falsifiable theorem

At least one of the following holds.

1. The semantic signal `p^dagger` of LEMMA-182 has an admissible AND/OR/NOT
   realization on the boundary of `R` satisfying the size and lexicographic
   budget of LEMMA-183.
2. A varying predecessor excluded from `R` has an additional live exit, and
   the two routes from that predecessor to the output determine a nonzero
   cycle coordinate that is killed or loses a NOT/cycle resource under at
   least one satisfying restriction.

Alternative 1 contradicts extremality by LEMMA-183. Alternative 2 contradicts
the separate resource preservation in LEMMA-178. A proof would therefore
exclude the one-sided branch. It must exhibit the realization circuit or the
specific cycle coordinate and the satisfying restriction that destroys it;
fanout-one alone is insufficient by GATE-004CC-FANOUT-ONE-ONLY.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted plateau DAG with maximal private predecessor region |
| Uniform/non-uniform | Every individual non-uniform operational one-sided parent; uniform fresh implication pair |
| Circuit size | Private realization within `|R|` with strict lexicographic descent, or one-unit satisfying-minor resource loss |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and partitioned into private versus shared exits |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and undirected cycle space over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004CC parent under the exact two-gate plateau hypothesis |
| Regime | Exact worst-case topological/cost dichotomy gate; not a SAT lower bound or terminal result |
