# GATE-004DJ — bound deficit or force an external resource

**Label: EXPLORATORY**

LEMMA-216 caps all satisfying-pruning losses at six distinct physical gates.
NG-159 shows that pruning-only payment is impossible without an endpoint bound
on the private deficit.

## Falsifiable theorem

For every refined minimum endpoint and counted boundary `b`, prove either

```text
D_b <= |L_00 union L_01 union L_11 minus C|,
```

where `C` is the explicitly prior-charged carrier/resource set, together with
an injective physical charge, or exhibit at least
`D_b-|union minus C|` additional distinct resources among minimum joint
cofactor savings, private/non-bridge gates, or a strict same-size potential
descent. In particular, prove `D_b<=6` if no external resource is used.

The theorem is falsified by a refined minimum endpoint with `D_b` larger than
the deduplicated uncharged loss union plus every named external resource and
with no strict descent. Local comparable semantics cannot establish the bound;
minimum size and exact cross-pruning physical correspondence must enter the
proof. Raw, unmasked, no-formula, and incomparable branches remain explicit.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau with exact physical satisfying-loss sets |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; deficit injected into at most six pruning gates plus distinct external resources |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; all shared losses, carrier charges, fanouts, bridges, and external regions audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Physical loss-set union, minimum joint Boolean circuits, potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual comparable, raw, unmasked, no-formula, or incomparable boundary |
| Regime | Exact worst-case bounded-deficit/external-resource gate; not a SAT lower bound or terminal result |
