# LEMMA-137 — dependency-cone Hall expansion holds through eight indices

**Label: PROVED**

For every circuit `C` for `W_m`, every spanning tree of its undirected output
cone, and every clause-index set `I` with `1<=|I|<=8`, the dependency-cone
neighborhoods of GATE-004AL satisfy

`|union_{i in I} P_i(T)| >= |I|`.

## The eighth case

Suppose an eight-index set were deficient. After restriction and pruning as
in LEMMA-116, its residual `W_8` circuit would have NOT count `q`, cycle rank
`c`, and

`q+c<=7`.

Markov gives `q>=ceil(log_2(9))=4`. For `c=0`, LEMMA-119 gives `q>=8`; for
`c=1`, LEMMA-123 gives `q>=8`; for `c=2`, LEMMA-133 gives `q>=7`; and for
`c=3`, LEMMA-135 gives `q>=6`. Each of these contradicts `q+c<=7`. If
`c>=4`, Markov gives `q+c>=8`, also a contradiction.

Together with LEMMA-136, this proves every subset size through eight.

## Model card

| Field | Value |
|---|---|
| Computational model | Dependency-cone NOT/non-tree-edge neighborhoods and restricted `W_8` circuits |
| Uniform/non-uniform | Every individual non-uniform parent circuit and every selected block set of size at most eight |
| Circuit size | Hall union lower bound exactly `|I|` for `1<=|I|<=8` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean restrictions and finite Hall matching |
| Asymptotic quantifiers | Every `m>=1`, every spanning tree, and every `I` with `1<=|I|<=min(8,m)` |
| Regime | Exact worst-case local Hall theorem; size nine, full matching, SAT lower bounds, and P versus NP remain open |
