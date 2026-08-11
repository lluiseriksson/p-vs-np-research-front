# GATE-004DY — classify zero-excess endpoint port vectors

**Label: EXPLORATORY**

LEMMA-237 and NG-173 show that exact joint minimization can return the whole
physical port region without releasing a gate. The next endpoint-sensitive
gate must distinguish such equality cases rather than assume them away.

## Falsifiable theorem

For an operational residual endpoint, let `A` be the complete set of
admissible nondescendant signals, `P` its full old/new four-code port-transfer
vector, `U` the deduplicated exterior physical region, `C_A(P)` the minimum
shared-DAG cost, and `q_A(P)` the LEMMA-236 distinct non-input coordinate
count. Define

```text
replacement excess  e = |U| - C_A(P),
minimum overhead    h = C_A(P) - q_A(P).
```

Prove, for every residual endpoint, an exact trichotomy:

1. `e>0`, and an explicit acyclic parent-preserving replacement converts the
   saving into real hosts or strict `W,Q,R_0` descent;
2. `e=0,h=0`, and the equality normal form injects its coordinate-source
   gates into distinct satisfying losses, marked origins, or contraction
   resources sufficient for `D_b^DAG`, or violates an endpoint identity; or
3. `e=0,h>0`, and every unavoidable auxiliary-only gate receives a named,
   nonduplicated physical charge, or its shared dependency forces a strict
   exchange, potential descent, or four-code contradiction.

The theorem is falsified by a refined minimum endpoint with `e=0` whose
coordinate gates and auxiliary gates admit neither the required injection nor
an exchange, descent, or signature contradiction. `C_A(P)<=|U|` must be
proved from the actual region interface; coordinate equality, admissibility,
acyclicity, parent preservation, and all fanouts must be recorded explicitly.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with complete multi-output four-code port vector and named physical region |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple with residual ports |
| Circuit size | Parent `K+2`; exact quantities `|U|`, `C_A(P)`, `q_A(P)`, `e`, and `h` |
| Circuit depth | Unrestricted; minimum shared realization and endpoint transfer depth unbounded |
| Fan-in | AND/OR two; NOT one; fanout, output sharing, admissible inputs, and physical deduplication audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean vector functions, exact shared-DAG cost, potentials, contraction maps, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, admissible signal, vector coordinate, minimum realization, and residual branch |
| Regime | Exact worst-case zero-excess endpoint gate; not a generic vector theorem, SAT lower bound, or terminal result |
