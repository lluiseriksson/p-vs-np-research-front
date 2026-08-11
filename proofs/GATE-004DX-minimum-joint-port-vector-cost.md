# GATE-004DX — minimum joint cost of the complete port vector

**Label: EXPLORATORY**

LEMMA-234 removes exact duplicate port functions in every minimum endpoint.
LEMMA-235 and NG-172 show that distinct global functions can still be
unbounded and are not automatically retargetable hosts. GATE-004DW therefore
requires a joint cost comparison, not class cardinality.

## Falsifiable theorem

For every bounded marked core with residual external ports, define the full
old/new port-transfer vector `P` whose coordinates include every parent-live
occurrence and all four fresh-pair codes. Let `U` be the deduplicated physical
union of gates used exclusively to realize those transfers outside the marked
core. Prove one of:

1. a minimum shared AND/OR/NOT DAG for `P` over admissible nondescendant
   signals uses at most `|U|-r` gates, and the exact replacement supplies `r`
   real hosts or strict `W,Q,R_0` descent;
2. exact joint minimality of `U` injects the residual port obligations into
   distinct satisfying losses, origins, or external resources sufficient for
   `D_b^DAG`; or
3. the bounded core and its port vector violate an exact four-code,
   contraction, or parent-transfer identity.

Every coordinate, shared prefix, fanout, and admissible input must be named.
Separate per-port minima cannot be summed, and the existence of distinct port
functions is not a payment. The theorem is falsified by a refined minimum
endpoint whose complete port vector is jointly minimum at its current cost,
shares too much for an injective charge, and admits no potential descent or
signature contradiction.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with bounded marked core and complete multi-output port-transfer vector |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple with residual ports |
| Circuit size | Parent `K+2`; compare exact deduplicated physical region `U` with minimum shared DAG cost for `P` |
| Circuit depth | Unrestricted; shared joint realization depth unbounded |
| Fan-in | AND/OR two; NOT one; fanout and multi-output sharing unrestricted and audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean vector functions, minimum shared DAGs, physical losses, potentials, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, endpoint, bounded core, port coordinate, admissible signal, and residual branch |
| Regime | Exact worst-case joint-port-cost gate; not a circuit lower bound for SAT or terminal result |

## Cycle-197 audit

LEMMA-236 separates unavoidable coordinate-output gates from auxiliary-only
sharing. LEMMA-237 gives an unbounded diagonal vector with exact exterior cost
`C_A(P)=|U|=m`; generic joint minimization therefore need not save a gate
(NG-173). This does not falsify the displayed endpoint dichotomy because the
diagnostic parent is nonminimal and alternatives 2–3 are endpoint-sensitive.
GATE-004DY now isolates the `e=0` equality cases. GATE-004DX remains
`EXPLORATORY`.
