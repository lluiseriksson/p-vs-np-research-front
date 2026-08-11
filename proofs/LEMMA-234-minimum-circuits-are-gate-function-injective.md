# LEMMA-234 — minimum circuits are injective on reachable gate functions

**Label: PROVED**

In a minimum finite acyclic AND/OR/NOT circuit, no two distinct gates that
reach the output compute the same global Boolean function of the raw inputs.
Consequently, distinct reachable external port gates in a minimum endpoint
have distinct global gate functions.

## Proof

This is the unrestricted, no-restriction instance of the semantic quotient in
LEMMA-005. Order the circuit topologically. If two reachable gates `a,b`
compute the same function, choose the earlier one, say `a`. Redirect every
outgoing edge of `b` to `a`; if `b` is the designated output, designate `a`
instead. Since `a` is earlier, it cannot depend on `b`, so the redirection
creates no directed cycle. Every consumer and the output receive the same
Boolean function, and `b` becomes dead. Removing it strictly decreases size,
contradicting minimality.

The statement is semantic and nonconstructive: it asserts no efficient test
for gate-function equality. Distinct functions are not thereby free hosts or
separate savings under a proposed rewrite.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum finite unrestricted constant-free AND/OR/NOT DAG with free wires |
| Uniform/non-uniform | Every finite non-uniform minimum circuit |
| Circuit size | Any duplicate reachable gate would give a strict one-gate reduction |
| Circuit depth | Unrestricted; topological redirection does not increase depth |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and redirected exactly |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact global Boolean gate functions; no algebraic computation |
| Asymptotic quantifiers | Every finite minimum circuit and every pair of reachable gates |
| Regime | Exact worst-case duplicate-elimination theorem; not an equivalence algorithm, host payment, SAT lower bound, or terminal result |
