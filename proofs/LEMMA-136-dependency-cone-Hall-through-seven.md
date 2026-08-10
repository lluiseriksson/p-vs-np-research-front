# LEMMA-136 — dependency-cone Hall expansion holds through seven indices

**Label: PROVED**

For every circuit `C` for `W_m`, every spanning tree of its undirected output
cone, and every clause-index set `I` with `1<=|I|<=7`, the dependency-cone
neighborhoods of GATE-004AL satisfy

`|union_{i in I} P_i(T)| >= |I|`.

LEMMA-132 proves the result through six. If a septet failed, LEMMA-134 would
produce a cycle-rank-three circuit for `W_7` with exactly three NOT gates.
LEMMA-135 requires at least `7-2=5` NOT gates, so that stratum is empty and
GATE-004AR is proved.

This closes only local Hall subsets through size seven. It does not establish
full Hall expansion for unbounded subsets.

## Model card

| Field | Value |
|---|---|
| Computational model | Dependency-cone NOT/non-tree-edge neighborhoods in unrestricted parent circuits |
| Uniform/non-uniform | Every individual non-uniform parent circuit and every selected block set of size at most seven |
| Circuit size | Hall union lower bound exactly `|I|` for `1<=|I|<=7` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; finite Hall matching |
| Asymptotic quantifiers | Every `m>=1`, every spanning tree, and every `I` with `1<=|I|<=min(7,m)` |
| Regime | Exact worst-case local Hall theorem; larger subsets, full matching, SAT lower bounds, and P versus NP are not implied |
