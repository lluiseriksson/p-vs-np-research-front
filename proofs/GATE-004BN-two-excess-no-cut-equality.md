# GATE-004BN — prune the surviving two-excess no-cut cases

**Label: EXPLORATORY**

Assume the GATE-004BM premise and one of the three no-cut cases in LEMMA-166.

## Falsifiable theorem

Some neutral implication-clause restriction leaves a circuit for `J_{j-1}`
with `N+r<=j+1`.

The proof must use Boolean gate functions or restriction survival beyond the
source degree, ranks, regional clause counts, and regional NOT counts. The
abstract no-go GATE-004BM-SOURCE-RANK-COUNTS-ONLY proves that those data alone
cannot supply the conclusion.

The first subcase to audit is `r>=2,d=2`, where both regional lower bounds are
equalities. A valid proof must either turn equality in LEMMA-119/139 into a
clause-private resource or expose a second no-bypass interface.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted implication circuits in the no-cut LEMMA-166 equality/slack cases |
| Uniform/non-uniform | Every individual non-uniform surviving two-excess parent; uniform symmetric tail family |
| Circuit size | Parent `N+r=j+2`; target after one neutral clause restriction `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2`, `sigma>=3`, and no-cut parent in one of the three LEMMA-166 cases |
| Regime | Exact worst-case remaining local subgate for GATE-004BM; not a SAT lower bound or terminal result |
