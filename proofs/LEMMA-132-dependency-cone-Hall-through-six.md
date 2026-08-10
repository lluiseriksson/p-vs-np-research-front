# LEMMA-132 — dependency-cone Hall expansion holds through six indices

**Label: PROVED**

For every circuit `C` for `W_m`, every spanning tree of its undirected output
cone, and every clause-index set `I` with `1<=|I|<=6`, the dependency-cone
neighborhoods of GATE-004AL satisfy

`|union_{i in I} P_i(T)| >= |I|`.

LEMMA-122 proves the result through five. If a sextet failed, LEMMA-124 would
produce a cycle-rank-two three-NOT circuit for `W_6`. GATE-004AN is now proved:
LEMMA-125/126 exclude the cactus cores, LEMMA-127/128 exclude a ternary theta
source, LEMMA-129/130 exclude parallel binary sources, and LEMMA-131 excludes
the final nested split. Therefore no deficient sextet exists.

This closes only local Hall subsets through size six. It does not establish
full Hall expansion for unbounded subsets.

## Model card

| Field | Value |
|---|---|
| Computational model | Dependency-cone NOT/non-tree-edge neighborhoods in unrestricted parent circuits |
| Uniform/non-uniform | Every individual non-uniform parent circuit and every selected block set of size at most six |
| Circuit size | Hall union lower bound exactly `|I|` for `1<=|I|<=6` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; finite Hall matching |
| Asymptotic quantifiers | Every `m>=1`, every spanning tree, and every `I` with `1<=|I|<=min(6,m)` |
| Regime | Exact worst-case local Hall theorem; size seven, full matching, SAT lower bounds, and P versus NP remain open |
