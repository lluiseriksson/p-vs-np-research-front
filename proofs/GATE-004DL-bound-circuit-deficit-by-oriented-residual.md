# GATE-004DL — bound circuit deficit by the oriented residual

**Label: EXPLORATORY**

LEMMA-217 supplies the aligned circuit deficit `D_b^DAG`. LEMMA-218 reduces
the uncharged satisfying-loss budget from six to two in the AND→OR carrier or
four in the OR→AND carrier.

## Falsifiable theorem

For every refined minimum endpoint and counted boundary, prove an injective
physical charge satisfying

```text
D_b^DAG <= 2  (AND→OR),
D_b^DAG <= 4  (OR→AND),
```

using only the oriented uncharged loss union, or force the excess from
distinct external joint savings, private/non-bridge gates, or a strict
same-size potential descent. Losses overlapping `{g,h}` or each other cannot
be reused.

The theorem is falsified by a refined minimum endpoint whose aligned circuit
deficit exceeds the oriented residual union plus all deduplicated external
resources and admits no descent. Raw, unmasked, no-aligned-DAG, and
incomparable branches remain explicit.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with aligned-DAG cost and oriented loss sets |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; pruning budget at most two or four after carrier charge |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; all sharing, fanouts, overlaps, bridges, and external regions audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Minimum aligned Boolean DAGs, oriented physical loss sets, potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and residual boundary in either carrier orientation |
| Regime | Exact worst-case oriented-deficit gate; not a SAT lower bound or terminal result |
