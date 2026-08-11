# GATE-004BT — find a resource neutralized uniformly in both primary codes

**Label: EXPLORATORY**

Assume GATE-004BS and its common parent graph.

## Falsifiable theorem

There is a tail clause `i` such that, after its neutral restriction, either:

1. one parent NOT gate becomes the same constant under both `x=0` and `x=1`;
   or
2. one common cycle-space coordinate is destroyed under both primary codes.

In the first case the gate is constant with `x` free because the two Boolean
codes agree. In the second case restoring the degree-two source adds at most
one rank unit to a residual already missing one. Either conclusion gives
`N+r<=j+1` and proves GATE-004BS.

LEMMA-173 shows that survival of a gate in both codes is insufficient; the
same neutral outcome or common cycle loss must be proved from exact
minimality and shared path topology.

LEMMA-174 now identifies the equal-rank cofactors with one common residual
cycle space. GATE-004BT-CYCLE-SPACE-ONLY shows that vector-space equality
still does not align clause labels. GATE-004BU is the active incidence gate.

## Model card

| Field | Value |
|---|---|
| Computational model | One common minimum two-excess circuit under both nonzero primary cofactors and neutral tail restrictions |
| Uniform/non-uniform | Every individual non-uniform GATE-004BS parent; uniform symmetric tail |
| Circuit size | Exact parent `N+r=j+2`; one uniform resource loss implies target `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary source fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean two-code equality and common undirected cycle space over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004BS parent with two distinct nonzero cofactors |
| Regime | Exact worst-case sufficient subgate for GATE-004BS; not a SAT lower bound or terminal result |
