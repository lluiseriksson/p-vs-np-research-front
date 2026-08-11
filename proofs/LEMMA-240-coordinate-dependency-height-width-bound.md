# LEMMA-240 — coordinate dependency height times width covers all gates

**Label: PROVED**

Let a zero-overhead realization have `q` gates, and partially order its gates
by directed reachability. If `H` is the maximum number of gates on a directed
path and `W` is the maximum size of a pairwise reachability-incomparable set,
then

```text
q <= H W.
```

Consequently `max(H,W)>=sqrt(q)`. This applies in particular to the
coordinate-only realizations characterized by LEMMA-238.

## Proof

For each gate `v`, let `ell(v)` be the maximum number of gates on a directed
path ending at `v`. Its value lies in `{1,...,H}`. If one gate in a fixed
level reaches another, appending that reachability path strictly increases
the latter level. Hence every level set is an antichain and has at most `W`
members. The `H` levels partition all `q` gates, giving `q<=HW`. The square-root
conclusion follows immediately.

The theorem supplies only a dependency chain or antichain. It does not make
antichain gates parent-preserving hosts, make chain gates expendable, or
identify satisfying losses and marked origins.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite acyclic gate-dependency graph of a zero-overhead multi-output AND/OR/NOT realization |
| Uniform/non-uniform | Every finite non-uniform realization |
| Circuit size | `q` gates with exact inequality `q<=HW` |
| Circuit depth | `H` gates on a longest directed path |
| Fan-in | Graph theorem independent of fan-in; target circuit AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite reachability poset; no field computation |
| Asymptotic quantifiers | Every finite zero-overhead DAG, gate, level, path, and antichain |
| Regime | Exact dependency-poset theorem; not a physical host matching, SAT lower bound, or terminal result |
