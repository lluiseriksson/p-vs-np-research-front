# GATE-004CV — separate or factor the counterflow cycle coordinate

**Label: EXPLORATORY**

LEMMA-201 supplies a named parent coordinate `gamma_b`, but LEMMA-174 forces
it to survive every satisfying minor. The next attack must determine whether
that coordinate is merely a contracted presentation of base topology or
requires an additional independent resource.

## Falsifiable theorem

For every counterflow boundary `b` in a minimum `Q=0` endpoint, at least one
of the following holds:

1. the contraction images of `gamma_b` can be traced to a common base-cycle
   coordinate, and the resulting two-route identity factors to a same-size
   circuit with a strict secondary-potential descent;
2. `gamma_b` contributes an independent coordinate beyond the common base
   cycle space in some satisfying minor, contradicting exact rank equality;
3. realizing its image forces a third parent gate to disappear in some
   satisfying code, contradicting the exact two-gate loss; or
4. a required edge is deleted while non-bridge, contradicting LEMMA-185.

The theorem is false if a minimum counterflow can reuse base topology under
all three contractions without enabling the factoring in item 1. Merely
exhibiting `gamma_b` or counting its edges is not evidence for any item.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, with named counterflow-cycle coordinates |
| Uniform/non-uniform | Every finite non-uniform operational endpoint tuple |
| Circuit size | Parent `K+2`; exact descent, third deletion, or topology contradiction required |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; contraction images and fanout audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean identities and cycle-space quotient maps over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum `Q=0` parent with a counterflow boundary |
| Regime | Exact worst-case coordinate-localization gate; not a SAT lower bound or terminal result |
