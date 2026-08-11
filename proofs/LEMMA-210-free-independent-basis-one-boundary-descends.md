# LEMMA-210 — a free independent basis-one boundary realization descends

**Label: PROVED**

Use the refined minimum endpoint and let `b` be a boundary counted by `R_0`.
Suppose the Boolean function computed by `b` has either of the following
realizations in the physical parent DAG:

1. it equals an existing globally `u`-independent signal `a`; or
2. it equals `OP(a_1,a_2)` for `OP` equal to AND or OR, or `NOT a_1`, where
   every displayed signal is globally `u`-independent.

In either case, every displayed signal is an existing physical signal,
distinct from `b`, and not a descendant of `b`.

Then the parent is not the refined minimum endpoint. In case 1 it has a
strictly smaller realization. In case 2 it has a same-size realization with
all earlier potentials unchanged and `R_0` smaller by exactly one.

## Proof

In case 1, redirect every outgoing edge of `b` to `a` and delete `b`.
Acyclicity is preserved because `a` is not a descendant of `b`; every
downstream gate receives the same Boolean function. The parent output is
unchanged and one gate is removed, contradicting minimum size.

In case 2, retain the physical vertex `b` but replace its operation and input
edges by the displayed one-gate realization. The new inputs are not
descendants of `b`, so the DAG remains acyclic. The function at `b` is
unchanged by hypothesis, and therefore a topological induction shows that
every downstream gate retains its function. No gate is added or removed.

All carrier gates and every gate function in the parent are unchanged, so the
earlier semantic potentials `W` and `Q` are unchanged. The retargeted `b` no
longer consumes `h`, because every new input is globally `u`-independent while
`h` is `u`-sensitive. Thus `b` is no longer a direct `h`-boundary. Every other
physical gate and edge is unchanged, so no other direct `h`-boundary changes
status. The count `R_0` decreases by exactly one, contradicting the refined
extremal choice.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically refined minimum unrestricted constant-free AND/OR/NOT DAG with free wires |
| Uniform/non-uniform | Every finite non-uniform endpoint parent and every counted boundary satisfying the basis-one certificate |
| Circuit size | A wire realization saves one gate; a one-gate realization preserves size and strictly lowers `R_0` |
| Circuit depth | Unrestricted; the nondescendant condition guarantees acyclicity after retargeting |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and all outgoing edges of `b` preserved or redirected |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean signal equality and physical DAG rewiring |
| Asymptotic quantifiers | Every nonconstant base, hypothetical refined endpoint, counted boundary, and supplied wire or one-gate certificate |
| Regime | Exact worst-case sufficient exchange theorem; not existence of the certificate, a SAT lower bound, or terminal result |
