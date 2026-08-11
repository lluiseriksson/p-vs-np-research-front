# GATE-004CF — exceed the two-deletion budget or expose a noncontractible edge

**Label: EXPLORATORY**

Assume the GATE-004CE shared-exit parent, its named cycle `gamma`, and absence
of a LEMMA-183 private realization certificate. For each satisfying code,
consider every restriction/pruning reduction to a minimum circuit for `A`.

## Falsifiable theorem

The edgewise four-code signatures on the two cancellation arms force, for at
least one satisfying code, one of the following.

1. Removing all fresh-pair dependence while retaining `A` requires at least
   three binary-gate eliminations.
2. Any reduction using at most two gate eliminations must delete an edge of
   `gamma` that is non-bridge at its deletion stage, rather than merely
   contract cyclic structure.
3. One arm supplies an admissible private realization certificate satisfying
   LEMMA-183.

Alternative 1 contradicts the exact two-binary-gate loss in LEMMA-178.
Alternative 2 contradicts LEMMA-185's rank neutrality. Alternative 3
contradicts lexicographic extremality. Proving the theorem would therefore
establish GATE-004CE and exclude the shared-exit branch.

The proof must use the minimum-parent deletion budget. The full four-code
table and cancellation signatures without that budget are insufficient by
GATE-004CE-FOUR-CODE-SIGNATURES-ONLY.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted plateau DAG with named shared-exit cycle and exact restriction/pruning reductions |
| Uniform/non-uniform | Every individual non-uniform operational GATE-004CE parent; uniform fresh implication pair |
| Circuit size | Lower bound of three required eliminations, forbidden non-bridge deletion within a two-gate budget, or same-size private descent |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor signatures and undirected cycle minors over `F_2` |
| Asymptotic quantifiers | Every operational shared-exit plateau parent and every reduction under each satisfying code |
| Regime | Exact worst-case deletion-budget gate; not a SAT lower bound or terminal result |
