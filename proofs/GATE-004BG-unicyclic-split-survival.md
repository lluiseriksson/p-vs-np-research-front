# GATE-004BG — turn the unicyclic NOT split into clause pruning

**Label: PROVED**

Use LEMMA-120 to factor a GATE-004BF parent through its unique duplicated bit,
and use LEMMA-160 to enter either the no-cut or sole-cut tail partition.

## Theorem

In each permitted partition, some neutral clause restriction deletes an
allocated NOT or breaks the unique cycle, leaving `N+r<=j`.

GATE-004BG-NO-CUT proves the no-cut case throughout the operational range.
LEMMA-163 and GATE-004BI prove the sole-cut case by neutralizing the cut
clause and making the duplicated source bit constant.

## Exact remaining cases

- No cut: `a` whole clauses upstream consume exactly `a` upstream NOTs, and
  `b` whole clauses downstream consume exactly `b` downstream NOTs.
- Sole cut: all `j-1` whole clauses are downstream and consume at least
  `j-1` of the `j` NOTs; the upstream formula has at most one.

The missing statement is no longer a count bound. It is a survival theorem
for equality-case formula occurrences embedded on the two sides of one
cycle.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unicyclic implication circuits, their one-bit formula factorization, and neutral clause restrictions |
| Uniform/non-uniform | Every individual non-uniform unicyclic parent; uniform symmetric clauses |
| Circuit size | Exact `N=j,r=1` and LEMMA-160 split; target restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted with one cycle |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2` in either LEMMA-160 partition case |
| Regime | Exact worst-case closure of the unicyclic partitions in GATE-004BF; not higher-rank GATE-004BE/BD/BA, a SAT lower bound, or a terminal result |
