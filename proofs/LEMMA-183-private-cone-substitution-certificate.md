# LEMMA-183 — a budgeted private cone certifies mask uncrossing

**Label: PROVED**

Let `C` be a one-sided parent from GATE-004CC, with masked edge
`e=(p,d)` and semantic replacement `p^dagger` from LEMMA-182. Let `R` be a
set of noninput gates satisfying all of the following.

1. The sub-DAG induced by `R` has unique output `p`.
2. Its only edge from `R` to a gate outside `R` is `e`.
3. Every incoming edge to `R` comes from a fixed boundary set `B` outside
   `R`.

Suppose there is an acyclic AND/OR/NOT subcircuit `R^dagger`, using only the
same available boundary signals `B`, whose output computes `p^dagger` and
such that

- `|R^dagger| <= |R|`; and
- if equality holds, replacing `R` by `R^dagger` either strictly lowers its
  number of pair-sensitive gates, or preserves that number and strictly
  lowers its number of gates with distinct `01/11` cofactors.

Then `C` is not a `(T_j,V_j)`-lexicographically extremal minimum circuit.

## Proof

Delete `R`, insert `R^dagger`, and feed its output to the former edge into
`d`. Condition 2 ensures that no other consumer is changed. The boundary
condition makes this an admissible acyclic substitution. LEMMA-182 says all
four cofactors, hence the full function, of `d` remain unchanged. Inducting
topologically above `d`, every downstream gate and the parent output remain
unchanged.

If `|R^dagger|<|R|`, the resulting circuit is smaller than the minimum parent,
a contradiction. If the sizes are equal, all gates outside the replaced
region compute their former functions. The stated local sensitivity change
therefore becomes a strict lexicographic decrease of `(T_j,V_j)`, again a
contradiction. Thus the displayed certificate excludes an extremal minimum
parent.

The lemma is deliberately conditional on an explicit realization and its
budget. It does not assert that every one-sided mask has such a private cone
or such a realization.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted AND/OR/NOT DAG with an explicitly private replaceable sub-DAG |
| Uniform/non-uniform | Every individual finite non-uniform one-sided parent and every supplied substitution certificate |
| Circuit size | Replacement uses at most the private-region gate count; strict saving or equal-size lexicographic descent |
| Circuit depth | Unrestricted; replacement must remain acyclic |
| Fan-in | AND/OR two; NOT one; arbitrary ambient fanout, but the replaced region has one outgoing edge |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and DAG substitution only |
| Asymptotic quantifiers | Every operational GATE-004CC parent admitting the stated finite certificate |
| Regime | Exact worst-case conditional exchange lemma; not existence of a certificate, a SAT lower bound, or terminal result |
