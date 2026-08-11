# LEMMA-216 — three exact two-loss budgets have union at most six

**Label: PROVED**

At the exact plateau, let `L_00,L_01,L_11` be the physical binary-gate sets
lost by the three satisfying prunings, after the already defined contraction
correspondence, and suppose each has cardinality two. Then their globally
deduplicated union satisfies

```text
|L_00 union L_01 union L_11| <= 6.
```

Equality holds exactly when the three loss sets are pairwise disjoint.

## Proof

Subadditivity gives

```text
|L_00 union L_01 union L_11|
  <= |L_00| + |L_01| + |L_11| = 6.
```

For three finite sets, equality in this inequality holds exactly when no
element is counted twice, equivalently when every pairwise intersection is
empty. This is physical-set accounting; a gate lost in multiple prunings is
one resource and may be charged only once.

The lemma supplies a hard cap, not six available payments: overlaps can make
the union smaller, and carrier losses already charged elsewhere must also be
removed before applying any residual budget.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact-plateau unrestricted AND/OR/NOT parent with three satisfying restriction minors |
| Uniform/non-uniform | Every finite non-uniform endpoint and its physical loss sets |
| Circuit size | Each satisfying minor loses exactly two binary gates; deduplicated union at most six |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite physical gate sets and inclusion-exclusion |
| Asymptotic quantifiers | Every triple of two-element physical loss sets |
| Regime | Exact worst-case resource cap; not existence of six free payments, SAT lower bound, or terminal result |
