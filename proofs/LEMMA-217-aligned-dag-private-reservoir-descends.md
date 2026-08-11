# LEMMA-217 — an aligned DAG with a private reservoir descends

**Label: PROVED**

Use the refined minimum endpoint and let `b` be counted by `R_0`. Suppose its
unchanged Boolean function `B` has a constant-free AND/OR/NOT **DAG** `T` with
`m>=1` gates over existing signals, and assume:

1. every non-output gate function of `T` is independent of both fresh inputs
   `u,t`;
2. there is a consumer-closed set `E` of exactly `m-1` strict ancestors of
   `b`, excluding all distinguished carrier vertices, such that every old edge
   leaving `E` targets `E union {b}`; and
3. every external input signal of `T` is globally `u`-independent, distinct
   from `E union {b}`, and not a descendant of any replacement vertex.

Then the parent is not the refined minimum endpoint. Map the `m-1` non-output
vertices of `T` bijectively to `E`, map its output vertex to `b`, and retarget
the physical vertices in a topological order. Sharing inside `T` is retained.

## Proof

The new internal edges follow the acyclic topology of `T`. Condition 3 rules
out an external-input back edge, so the physical rewrite remains acyclic. The
new function at `b` is exactly `B`; all old outgoing edges of `b` remain.
Every old use of a function in `E` ended inside `E union {b}`, whose inputs are
all retargeted. Therefore every exterior function and the parent output remain
unchanged. No gate is added, and dead-gate propagation can only decrease size.

Every new gate in `E` is independent of `u,t`, so it cannot add a gate counted
by `W` or a `u`-sensitive handoff counted by `Q`. The distinguished carrier is
unchanged. Thus earlier potentials do not increase; a strict decrease already
contradicts extremality. At equality, every new input occurrence at `b` comes
from a globally `u`-independent external signal or aligned gate in `E`, so `b`
no longer consumes `h` and leaves `R_0`. No other boundary changes or enters.
Hence `R_0` strictly decreases, contradiction.

LEMMA-212 is the formula-tree special case. Define `A_b^DAG` as the minimum
number of non-output gates in any certificate satisfying conditions 1 and 3,
and let `rho_b` be the maximum admissible private-reservoir size. Then

```text
D_b^DAG = max(0, A_b^DAG - rho_b)
```

is no larger than the former formula deficit `D_b`. Every refined endpoint
must have `D_b^DAG>0`; otherwise this lemma applies.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically refined minimum unrestricted constant-free AND/OR/NOT DAG with free wires |
| Uniform/non-uniform | Every finite non-uniform endpoint and supplied aligned-DAG/private-reservoir certificate |
| Circuit size | `m-1` reservoir vertices and `b` are repurposed; size does not increase |
| Circuit depth | Unrestricted; certificate topology and nondescendant external inputs preserve acyclicity |
| Fan-in | AND/OR two; NOT one; internal sharing and fanout unrestricted; reservoir consumer-closed toward `b` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean DAG functions, physical rewiring, and lexicographic potentials |
| Asymptotic quantifiers | Every `m>=1`, nonconstant base, refined endpoint, counted boundary, and supplied certificate |
| Regime | Exact worst-case sufficient exchange; not certificate existence, SAT lower bound, or terminal result |
