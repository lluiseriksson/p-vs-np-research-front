# GATE-004DS-CYCLE-EXISTENCE-AS-LOSS — the provenance cycle is not lost

**Label: NO-GO**

Scope: in the common-origin branch of LEMMA-228, count the resulting
undirected provenance cycle as a destroyed coordinate or satisfying-pruning
payment merely because it exists.

LEMMA-229 proves the opposite at the active endpoint. Exact plateau rank
equality and LEMMA-174 map every nonzero parent coordinate, including the
swap-provenance cycle, to a nonzero coordinate in each of `00,01,11`. Edges
may contract and representatives may change, but no cycle-space dimension is
lost. LEMMA-202's subdivision witness shows explicitly that two physical
vertices can disappear by contractions while the coordinate survives.

The cycle may still support a marked-edge uncrossing or minimum-cost argument.
What fails is charging its existence as a lost resource without proving such
an additional statement.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact-plateau unrestricted AND/OR/NOT output-cone multigraph and its three satisfying restriction minors |
| Uniform/non-uniform | Every finite non-uniform hypothetical endpoint with a supplied common-origin provenance cycle |
| Circuit size | Parent `K+2`; two binary gates lost per satisfying minor, all cyclic changes rank-neutral |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Cycle-space isomorphisms and contractions over `F_2` |
| Asymptotic quantifiers | Every endpoint provenance cycle and every satisfying code |
| Regime | Cycle-existence-as-loss no-go; not exclusion of marked-support exchanges, SAT lower bound, or terminal result |
