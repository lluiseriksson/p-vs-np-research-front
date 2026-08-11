# GATE-004CK — classify the bounded switching-carrier incidences

**Label: EXPLORATORY**

Assume the active switching branch reaches an extremal tuple with `W=1`.
By LEMMA-190 its canonical `01/11` difference carrier `H` has between two and
seven gates, contains the distinguished directed edge `h -> n`, and every
other carrier gate lies in one of the three two-element satisfying deletion
sets.

## Falsifiable theorem

For every directed carrier topology and three-code deletion incidence pattern
consistent with those constraints and with the complete four-code cofactor
table, at least one of the following holds.

1. The Boolean identities give a function- and size-preserving rewrite that
   leaves the switching branch or strictly lowers an earlier extremal
   potential.
2. The topology contains the private-cone realization certificate of
   LEMMA-183.
3. Some satisfying deletion removes a non-bridge edge of the named cycle
   `gamma`, contrary to the rank-neutral plateau minor.
4. The topology/incidence pattern is symbolically unrealizable by AND/OR/NOT
   cofactor functions.

The proof must cover every carrier size `2,...,7`, every placement of the
three two-element deletion sets, the distinguished `h -> n` relation, every
binary equal-output cancellation boundary, and all four restriction codes.
Topology and incidence are finite; Boolean-function labels are not thereby
reduced to a numerical enumeration. Each surviving case requires an explicit
symbolic identity or contradiction.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted switching plateau parent at the conditional floor `W=1`, with canonical carrier and three pruning maps |
| Uniform/non-uniform | Every individual finite non-uniform operational tuple; one uniform finite topology/incidence case split |
| Circuit size | Carrier size two through seven; ambient parent and base size unrestricted; every rewrite must preserve basis cost |
| Circuit depth | Unrestricted ambient depth; bounded carrier depth at most seven |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and preserved by rewrites |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor identities plus undirected cycle minors over `F_2` |
| Asymptotic quantifiers | Every active extremal `W=1` tuple and every valid satisfying pruning triple |
| Regime | Exact worst-case bounded symbolic classification gate; not a numerical certificate, SAT lower bound, or terminal result |
