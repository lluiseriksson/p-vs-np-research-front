# LEMMA-141 — full dependency-cone Hall expansion

**Label: PROVED**

For every circuit `C` for `W_m`, every spanning tree `T` of its connected
undirected output cone, and every clause-index subset `I subseteq [m]`, the
dependency-cone neighborhoods of GATE-004AL satisfy

`|union_{i in I} P_i(T)| >= |I|`.

## Proof

The empty set is immediate. For `k=|I|>=1`, restrict every block outside `I`
to true, propagate constants, and prune as in LEMMA-116. If `q` and `r` are
the residual NOT count and cycle rank, the lifting argument gives

`q+r <= |union_{i in I} P_i(T)|`.

The residual computes `W_k`. If `r=0`, LEMMA-139 gives `q>=k`. If `r>=1`, it
gives `q>=k-r+1`, hence `q+r>=k+1`. In either case `q+r>=k`, proving the Hall
inequality.

Hall's theorem therefore injects all `m` clause indices into the NOT gates and
non-tree edges. The fundamental cycles of those non-tree edges form a
cycle-space basis, so this also supplies the witness required by GATE-004AI.

## Model card

| Field | Value |
|---|---|
| Computational model | Dependency-cone NOT/non-tree-edge neighborhoods in unrestricted parent circuits |
| Uniform/non-uniform | Every individual non-uniform parent circuit and every spanning tree |
| Circuit size | Full Hall expansion and an injection into `N+r` resources, implying `N+r>=m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Fundamental cycle bases over `F_2` and finite Hall matching |
| Asymptotic quantifiers | Every `m>=1`, every pruned circuit for `W_m`, every spanning tree, and every index subset |
| Regime | Exact worst-case full Hall theorem for `W_m`; not base additivity, a SAT lower bound, or a terminal result |
