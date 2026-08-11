# LEMMA-237 — the diagonal port vector has exact joint cost

**Label: PROVED**

For every `m>=1`, define

```text
D_m(x,y,z_1,...,z_m) = (x AND y AND z_i)_{i=1}^m.
```

Its exact constant-free AND/OR/NOT multi-output gate complexity from the raw
inputs is `m+1`. If the signal `a=x AND y` is already available without being
charged to the exterior region, the exact additional cost of
`(a AND z_i)_{i=1}^m` is `m`.

The same bounds hold after adjoining fresh code inputs `u,t` and repeating
the vector unchanged on all four codes. Thus the conclusion is compatible
with a complete four-row table, but does not assert that the table occurs in
a minimum plateau endpoint.

## Proof

The displayed realization computes `a=x AND y` once and then uses the `m`
gates `a AND z_i`, proving the upper bounds.

The `m` coordinate functions are pairwise distinct and none is an admissible
input signal. LEMMA-236 gives the lower bound `m` when `a` is supplied, so
that bound is exact.

From raw inputs, suppose for contradiction that `m` gates suffice. Equality
in LEMMA-236 makes every gate a designated coordinate source. The first gate
in a topological order therefore computes one of the coordinates, but its
inputs are raw signals. A NOT of one raw signal depends on at most one raw
variable, and an AND or OR of two raw signals depends on at most two. Every
coordinate `x AND y AND z_i` depends essentially on the three distinct raw
variables `x,y,z_i`, a contradiction. Hence at least `m+1` gates are needed.

Adding unused code variables does not change the construction or the lower
argument: the target coordinate still has the three displayed essential
variables, while a first gate can read at most two raw signals.

In the LEMMA-233 diagnostic, the marked-core signal `g=x AND y` is already
present and the exterior port region consists of the `m` gates
`p_i=g AND z_i`. It therefore has exact additional vector cost `m`; joint
minimization alone releases no exterior gate. The diagnostic parent remains
deliberately nonminimal.

## Model card

| Field | Value |
|---|---|
| Computational model | Constant-free multi-output unrestricted AND/OR/NOT DAG for the diagonal vector, with raw or one supplied precomputed signal |
| Uniform/non-uniform | Uniform construction for every `m>=1`; each vector instance and minimum circuit finite and non-uniform |
| Circuit size | Exactly `m+1` from raw inputs; exactly `m` additional gates when `a=x AND y` is supplied |
| Circuit depth | Upper bound two from raw inputs and one after `a`; lower bound depth unrestricted |
| Fan-in | AND/OR two; NOT one; fanout and multi-output designation unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean vector functions, including a code-independent four-row extension |
| Asymptotic quantifiers | Every integer `m>=1`, every coordinate, and every finite realizing DAG |
| Regime | Exact worst-case vector-cost theorem for a diagnostic family; not endpoint minimality, a SAT lower bound, or terminal result |
