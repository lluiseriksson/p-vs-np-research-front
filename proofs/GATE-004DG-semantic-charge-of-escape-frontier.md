# GATE-004DG — semantically charge the escape frontier

**Label: EXPLORATORY**

LEMMA-213 identifies the exact escape-reachability obstruction to a private
reservoir. NG-156 shows that frontier cardinality cannot pay formula deficit:
one live escape can block an arbitrarily deep and functionally rich cone.

## Falsifiable theorem

For every refined minimum endpoint with positive private deficit `D_b`, choose
the greatest reservoir `E*` and its escape frontier `S`. Partition the
nonprivate ancestor cone by its first reachable frontier consumers. Prove that
the *semantic replacement cost* of these escape regions, jointly across all
their live consumers and all three satisfying prunings, supplies at least
`D_b` distinct physical payments or yields one of:

1. a consumer-masked specialization with strict gate saving;
2. a third binary loss in a named satisfying pruning;
3. a non-bridge deletion or a same-size strict `W,Q,R_0` descent; or
4. an aligned formula with a smaller certified deficit.

The proof must charge shared prefixes only once and preserve every live escape
consumer. It is falsified by a refined minimum parent whose frontier regions
have joint replacement cost below `D_b`, whose three satisfying losses remain
exactly two, and which admits no earlier-potential descent. Raw counterflow
inputs, absence of any aligned formula, and incomparable cofactors remain
explicit separate branches.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau with positive private deficit and exact escape frontier |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; at least `D_b` distinct physical payments or an exact contradiction required |
| Circuit depth | Unrestricted; shared escape regions and reconvergence depth unbounded |
| Fan-in | AND/OR two; NOT one; every frontier edge, live consumer, shared prefix, and pruning survivor audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean replacement cost, directed reachability, and satisfying cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual comparable, raw/shared, no-formula, or incomparable boundary |
| Regime | Exact worst-case semantic-frontier payment gate; not a SAT lower bound or terminal result |

## Cycle-180 audit

LEMMA-214 proves a joint multi-output exchange: common masking pays every gate
that directly consumes raw `u`. GATE-004DG-ENTRY-COUNT-ONLY shows that this
interface payment can be one while `D_b=n-2`; the residual specialized AND
chain remains large. GATE-004DH therefore replaces entry counting by the full
minimum joint cofactor-circuit saving. GATE-004DG retains its `EXPLORATORY`
label; no automatic promotion is made.
