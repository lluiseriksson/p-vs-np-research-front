# LEMMA-122 — dependency-cone Hall expansion holds through five indices

**Label: PROVED**

For every circuit `C` for `W_m`, every spanning tree of its undirected output
cone, and every clause-index set `I` with `1<=|I|<=5`, the dependency-cone
neighborhoods of GATE-004AL satisfy

`|union_{i in I} P_i(T)| >= |I|`.

LEMMA-116 proves the result through four. If a quintet failed, LEMMA-117 would
produce a unicyclic three-NOT circuit for `W_5`. GATE-004AM proves that no such
circuit exists. Therefore no deficient quintet exists.

This closes only the first five local Hall sizes. It does not establish full
Hall expansion for unbounded subsets.

## Model card

| Field | Value |
|---|---|
| Computational model | Dependency-cone NOT/non-tree-edge neighborhoods in unrestricted parent circuits |
| Uniform/non-uniform | Every individual non-uniform parent circuit and every selected block set of size at most five |
| Circuit size | Hall union lower bound exactly `|I|` for `1<=|I|<=5` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; finite Hall matching |
| Asymptotic quantifiers | Every `m>=1`, every spanning tree, and every `I` with `1<=|I|<=min(5,m)` |
| Regime | Exact worst-case local Hall theorem; size six, full matching, SAT lower bounds, and P versus NP remain open |
