# LEMMA-214 — a masked multi-output specialization saves every entry gate

**Label: PROVED**

Let `S` be a finite sub-DAG of a constant-free AND/OR/NOT circuit, with a
finite output set `O`. Assume:

1. every edge leaving `S` originates at a vertex of `O`;
2. every incoming noninput signal other than raw `u` is globally
   `u`-independent;
3. raw `u` is the only `u`-dependent source entering `S`;
4. exactly `d>=1` gates of `S` directly consume raw `u`; and
5. for one `sigma in {0,1}`, replacing every outgoing occurrence of every
   `o in O` by its cofactor `o|_{u=sigma}`, with constant propagation, leaves
   every direct exterior consumer's Boolean function unchanged.

Then the parent function has a constant-free realization with at most
`d` fewer gates. Consequently no minimum parent contains such a region.

## Proof

Hardwire `u=sigma` inside `S`. Each of the `d` direct entry gates disappears:
`NOT u` becomes constant, and a binary AND/OR with a constant input becomes a
constant or the other input. Redirect identity cases and propagate constants
forward. Every other gate of `S` is retained at most once or deleted; no new
gate is introduced. Thus all nonconstant output cofactors are jointly realized
using at most `|S|-d` gates, sharing exactly the residual specialized DAG.

Feed those outputs to their former exterior occurrences. Whenever an output
cofactor is constant, propagate that constant through its direct consumers;
an AND/OR/NOT consumer is retained at most once, redirected, or deleted. By
condition 5 every direct consumer keeps its former Boolean function. Condition
1 leaves no other modified edge, so topological induction preserves every
remaining exterior function and the parent output. Because that output is the
former nonconstant parent function, constant propagation terminates without a
constant generator. The exterior gains no gate and `S` loses at least `d`.

This is a sufficient certificate. It does not assert that a frontier region
is jointly masked or that the number of raw-`u` entry gates covers its private
formula deficit.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite constant-free unrestricted AND/OR/NOT DAG with a multi-output cofactor region |
| Uniform/non-uniform | Every finite non-uniform parent and supplied region satisfying conditions 1–5 |
| Circuit size | Joint specialization removes at least the `d` gates directly consuming raw `u`; no exterior gate is added |
| Circuit depth | Unrestricted; specialization and propagation remain acyclic |
| Fan-in | AND/OR two; NOT one; arbitrary internal/output fanout and every direct exterior occurrence audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, shared multi-output DAG specialization, and topological induction |
| Asymptotic quantifiers | Every finite region, every `d>=1`, both possible `sigma`, every output occurrence, and every base assignment |
| Regime | Exact worst-case sufficient gate-saving theorem; not existence of masking, SAT lower bound, or terminal result |
