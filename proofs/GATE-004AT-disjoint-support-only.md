# GATE-004AT-DISJOINT-SUPPORT-ONLY — infer a bottleneck from fresh variables

**Label: NO-GO**

The base variables `X` and tail variables `Y` are disjoint, but unrestricted
binary gates may mix them before the final output, fan out into several mixed
regions, and reconverge. Functional disjointness of the input sets does not
imply a one-vertex separator in the directed circuit graph, nor does ordinary
pruning transform an arbitrary minimum circuit into one without a size
argument.

Assuming that all `X` paths first merge at a pure-base gate would assert the
topological conclusion of GATE-004AT rather than derive it. No explicit
smaller circuit or counterexample to GATE-004AT is claimed. The next attack
must exploit canonical witness agreement or prove a size-nonincreasing
uncrossing transformation.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted base-tail circuit DAGs with disjoint primary-input supports |
| Uniform/non-uniform | Every individual non-uniform circuit; support-only method audit |
| Circuit size | No additive lower bound and no proved separator from disjointness alone |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed graph separation only; no algebraic circuit model |
| Asymptotic quantifiers | Every disjoint pair of base/tail variable sets and every unrestricted circuit for their conjunction |
| Regime | Structural no-go for support-only separation; GATE-004AT/AG/AE remain open |
