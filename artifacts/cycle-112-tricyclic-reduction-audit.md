# Cycle 112 tricyclic reduction audit

## Rank-three lower bound

**Label: PROVED**

LEMMA-135 proves that a cycle-rank-three circuit for either polarity of
`W_m` needs at least `m-2` NOT gates. A cycle-separating articulation splits
the rank as `1+2`; a 2-connected core has a directed source whose deletion
leaves rank at most two.

## Hall consequences

**Label: PROVED**

The bound excludes the `W_7,c=3,q=3` stratum, proving GATE-004AR and
LEMMA-136. Combining the same bound with Markov closes size eight directly in
LEMMA-137. LEMMA-138 reduces any deficient nonet to exact `c=4,q=4`.

## Failed first rank-four attack

**Label: NO-GO**

Generic rank-four unfolding permits up to sixteen copies per NOT, while
formula inversion requires only nine occurrences. This does not prove
GATE-004AS. A topology-sensitive rank-four reduction is next.

## Scope

**Label: EXPLORATORY**

Size-nine Hall, full Hall, unrestricted SAT circuit lower bounds, and P versus
NP remain open. No proof-assistant certification is claimed.
