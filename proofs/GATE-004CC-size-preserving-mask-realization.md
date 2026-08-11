# GATE-004CC — realize one-sided mask erasure at equal size

**Label: EXPLORATORY**

For a circuit `C` and fresh pair `j`, let

- `T_j(C)` be the number of noninput gates depending on `u_j` or `t_j`;
- `V_j(C)` be the number of noninput gates whose `01` and `11` cofactors
  differ.

Among minimum circuits for the hypothetical two-gate plateau, choose one
lexicographically minimizing `(T_j,V_j)`. Such a choice exists because there
are finitely many labelled size-minimum DAGs on the fixed finite input set.

## Falsifiable theorem

At every one-sided first cancellation in this extremal parent, the abstract
edge erasure of LEMMA-182 can be realized by an AND/OR/NOT DAG computing the
same parent function, with the same number of gates, with `T_j` not increased,
and with `V_j` strictly decreased; or one of the three satisfying restrictions
loses a NOT or cycle-rank resource.

The first outcome contradicts lexicographic minimality; the second contradicts
LEMMA-178. Proving this theorem therefore excludes the one-sided branch of
GATE-004CA. A proof must explicitly account for every consumer of `p` and for
the basis cost of the replacement signal; LEMMA-182 alone is insufficient.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted AND/OR/NOT plateau circuits |
| Uniform/non-uniform | Every individual non-uniform operational one-sided parent; uniform fresh implication pair |
| Circuit size | Exact same-size rewrite with nonincreasing `T_j` and strictly decreasing `V_j`, or one-unit resource loss |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and must be audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors plus undirected `N+r` accounting over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004CB parent under the exact two-gate hypothesis |
| Regime | Exact worst-case realization gate; not a SAT lower bound or terminal result |
