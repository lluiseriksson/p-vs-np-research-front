# GATE-004BA-GENERIC-DIRECT-SUM — import a basis-agnostic disjoint-support theorem

**Label: NO-GO**

The route would assert that computations on disjoint variable blocks are
additive, or admit an optimal circuit respecting the visible decomposition,
without proving that statement in the exact repository basis.

PAUL76 proves that this intuition fails strongly in a standard combinational
circuit model: for every `epsilon>0`, arbitrarily complex scalar functions
`f` exist for which the OR of two disjoint copies has complexity at most
`(1+epsilon)C(f)`, rather than approximately `2C(f)`. It also gives
nonoptimality of the evident disjoint-decomposition architecture.

This is not a counterexample to GATE-004BA. Paul's model allows general
two-input switching gates and counts only indegree-two gates; the repository
uses fan-in-two AND/OR and counted unary NOT. The composition and functions
also differ from `H AND product_i(t_i OR NOT u_i)`.

Accordingly, the no-go is methodological and exact: no theorem may be
transferred from disjointness or a richer basis without a proved simulation
and quantitative loss bound. GATE-004BA must exploit the one-negative clause
semantics, the NOT-plus-cycle resource identity, or an AND/OR/NOT-specific
exchange.

## Model card

| Field | Value |
|---|---|
| Computational model | Audit comparing general binary switching circuits with the repository's counted AND/OR/NOT basis |
| Uniform/non-uniform | Fully non-uniform finite-function results in both models; no uniform-family transfer |
| Circuit size | PAUL76 permits disjoint-copy OR complexity `(1+epsilon)C(f)` in its model; no numeric bound imported into the repository model |
| Circuit depth | Unrestricted in both models |
| Fan-in | PAUL76 general two-input switching gates; target AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean switching functions; no algebraic circuit claim |
| Asymptotic quantifiers | Every `epsilon>0` in PAUL76's existence theorem; every attempted basis-agnostic promotion in the repository |
| Regime | Literature-backed no-go for generic direct-sum inference; GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |
