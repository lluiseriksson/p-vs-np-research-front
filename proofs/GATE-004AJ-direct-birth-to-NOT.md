# GATE-004AJ-DIRECT-BIRTH-TO-NOT — first birth nodes are negations

**Label: NO-GO**

The first internal node where the canonical cofactor difference becomes
`u_i`-dependent cannot be charged directly by declaring that node a NOT gate.
LEMMA-114 proves the opposite: NOT complements both compared cofactors and
therefore preserves their XOR difference exactly. If the difference first
depends on `u_i` at a node, that node must be binary.

This closes only the zero-length trace from a birth event to a negation. It
does not rule out charging a distinct NOT elsewhere in the birth node's
ancestor or descendant cone, nor charging an independent reconvergence. The
birth-resource matching in GATE-004AJ and all larger gates remain open.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired canonical cofactor profiles at nodes of unrestricted AND/OR/NOT circuits |
| Uniform/non-uniform | Every individual non-uniform parent circuit; uniform clause-indexed comparison |
| Circuit size | No lower bound; direct identification of each first birth node with a NOT is impossible |
| Circuit depth | Unrestricted finite DAG |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean XOR comparison only |
| Asymptotic quantifiers | Every `m>=1`, every clause index, and every first birth node from LEMMA-114 |
| Regime | Structural no-go for direct birth-to-NOT charging; nonlocal resource matching remains open |
