# GATE-004DK — bound aligned circuit deficit or force a resource

**Label: EXPLORATORY**

LEMMA-217 shows that physical rewiring needs an aligned DAG, not a formula.
Hence the relevant residual quantity is `D_b^DAG<=D_b`. LEMMA-216 still caps
the deduplicated satisfying-loss union at six.

## Falsifiable theorem

For every refined minimum endpoint and counted boundary, prove either

```text
D_b^DAG <= |L_00 union L_01 union L_11 minus C| <= 6,
```

with an injective charge to previously uncharged physical gates, or supply
`D_b^DAG` distinct payments after globally deduplicating minimum joint
cofactor savings, private/non-bridge gates, and strict potential descents.

The theorem is falsified by a refined minimum endpoint with positive aligned
circuit deficit larger than the uncharged physical loss union plus every
external resource, and no strict descent. A proof must either construct the
aligned DAG or prove its minimum cost; unfolding a circuit into a formula is
not an admissible cost-preserving step. Raw, unmasked, no-aligned-DAG, and
incomparable branches remain explicit.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau with aligned-DAG cost and exact loss sets |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; aligned circuit deficit paid by at most six pruning gates plus distinct external resources |
| Circuit depth | Unrestricted; aligned certificate DAG depth and sharing unrestricted |
| Fan-in | AND/OR two; NOT one; all sharing, fanouts, losses, bridges, and replacement interfaces audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Minimum aligned Boolean DAGs, physical loss sets, potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and residual comparable, raw, unmasked, no-DAG, or incomparable boundary |
| Regime | Exact worst-case aligned-circuit-deficit gate; not a SAT lower bound or terminal result |

## Cycle-184 audit

LEMMA-218 deducts `{g,h}` and leaves at most two or four pruning resources,
not six. GATE-004DL replaces this gate with the orientation-specific bound.
GATE-004DK remains `EXPLORATORY`; no resource is counted twice.
