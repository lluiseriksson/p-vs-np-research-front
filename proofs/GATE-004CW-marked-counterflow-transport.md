# GATE-004CW — marked Boolean transport around the counterflow cycle

**Label: EXPLORATORY**

LEMMA-202 shows that abstract cycle coordinates align tautologically. The
smallest remaining counterflow brick must retain the physical support of
`gamma_b` and the Boolean data that restrictions transport along both arms.

## Falsifiable theorem

Fix a counterflow boundary `b`, a last-divergence cycle `gamma_b`, and label
every vertex on its two arms by its full four-code cofactor vector. For each
satisfying code, record the exact parent edges contracted and the two binary
gates eliminated. Then at least one of the following holds:

1. the marked transports on the two arms yield an explicit Boolean factoring
   rewrite with the same gate count and a strict secondary-potential descent;
2. some satisfying transport requires a third binary gate to disappear;
3. some satisfying transport deletes an edge that is non-bridge at deletion;
4. the counterflow boundary has a private realization certificate.

A proof must exhibit the rewrite or the offending marked edge/gate. Cycle
dimension, an unmarked isomorphism, or a choice of basis is insufficient by
GATE-004CV-ABSTRACT-COORDINATE-ONLY. The theorem fails if all three marked
transports fit within their exact two-gate contraction budgets and no
factoring or private certificate follows.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, with a marked counterflow cycle |
| Uniform/non-uniform | Every finite non-uniform operational endpoint tuple |
| Circuit size | Parent `K+2`; exact same-size descent, third deletion, non-bridge loss, or private certificate required |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; every marked arm edge, contraction, and fanout audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactor vectors plus cycle-space contractions over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, hypothetical minimum `Q=0` parent, counterflow boundary, chosen last-divergence cycle, and satisfying code |
| Regime | Exact worst-case marked-transport gate; not a SAT lower bound or terminal result |
