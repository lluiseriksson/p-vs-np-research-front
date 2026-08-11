# GATE-004BR-COFACTOR-MINIMA-ONLY — glue the two cofactor minima

**Label: NO-GO**

## Attempt

For each nonzero cofactor `H_c`, use its at-most-one-excess witness and
LEMMA-169 to obtain a circuit for `H_c W_{j-1}` of resource at most `j`.
Infer a resource-`j+1` circuit for

`H(x,Y) W_{j-1}`

by selecting between those two circuits with `x`.

## Failure

The two resource inequalities refer to separate circuits and contain no
identification of their NOT gates, cycles, or tail subgraphs. A Shannon
selector combines two arbitrary witnesses by duplicating both; `N+r` is then
bounded by their sum plus selector cost, not by their maximum plus one.
Abstractly, two disjoint resource sets of size `j` satisfy both cofactor
bounds while their union has size `2j`; no scalar premise chooses a shared
size-`j` realization.

This refutes only the inference from separate minima. It is not a realizable
minimum-parent counterexample and does not refute GATE-004BR.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract pairs of cofactor circuits and their resource sets under Shannon selection |
| Uniform/non-uniform | Two independent non-uniform witnesses; no common-parent realizability claim |
| Circuit size | Each cofactor resource at most `j`; naive union may contain `2j` resources plus selector cost |
| Circuit depth | Unrestricted witnesses |
| Fan-in | Selector target uses binary AND/OR and at most one unary NOT |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite resource sets and Boolean Shannon expansion only |
| Asymptotic quantifiers | Every `j>=1` in the abstract disjoint-witness class |
| Regime | Structural no-go for cofactor-minimum-only gluing; not a refutation of the common-graph gate or a SAT lower bound |
