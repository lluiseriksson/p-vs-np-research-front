# GATE-004CB-SEMANTIC-ERASURE-ONLY — semantic edge erasure is not a circuit exchange

**Label: NO-GO**

## Tempting inference

Use the abstract signal `p^dagger` from LEMMA-182 as though it were a free
replacement for `p`, and conclude that a one-sided mask has a same-size
rewrite with fewer pair-sensitive gates.

## Failure

LEMMA-182 specifies the four cofactors of one replacement edge, not a circuit
for that function. In the AND/OR/NOT basis, realizing `p_01 AND p_11` or
`p_01 OR p_11` can require extra gates or duplicated cones. Moreover `p` may
feed consumers other than `d`; changing the gate globally can alter those
consumers, while changing only its edge to `d` may require duplicating the
entire feeding cone. Truth-table preservation at `d` therefore supplies no
size-preserving DAG rewrite and no strict decrease of a global sensitivity
potential.

This does not refute GATE-004CB. It isolates the remaining obligation:
realize the semantic erasure using existing topology and exact plateau
minimality, or prove that a satisfying restriction loses a resource.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT DAGs audited against an abstract edge substitution |
| Uniform/non-uniform | Every individual finite non-uniform one-sided parent; no uniform rewrite asserted |
| Circuit size | No bound follows from the semantic identity; duplication cost is uncontrolled |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and explicitly obstructive |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors only; no algebraic computation |
| Asymptotic quantifiers | Every proposed use of LEMMA-182 without an explicit basis-level realization |
| Regime | Structural no-go for semantic-erasure-only reasoning; not a plateau counterexample, SAT lower bound, or terminal result |
