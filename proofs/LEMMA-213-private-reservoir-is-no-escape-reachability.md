# LEMMA-213 — the maximum private reservoir is the no-escape region

**Label: PROVED**

Let `b` be a gate in a finite DAG. Let `A` be the strict gate ancestors of
`b` that are eligible for repurposing, after excluding every distinguished
carrier vertex. Define the escape frontier

```text
S = {v in A : v has a consumer outside A union {b}}.
```

Let `Pred_A(S)` contain every vertex of `A` from which a directed path lying
in `A` reaches `S`, including `S`. Then the unique greatest admissibly
`b`-private set is

```text
E* = A minus Pred_A(S).
```

Here admissibly `b`-private means that every edge leaving the set targets the
set or `b`. Thus private-reservoir size is an exact reachability invariant,
not a fanout count.

## Proof

Take `v in E*` and any consumer `c` of `v`. If `c` is outside `A union {b}`,
then `v` belongs to `S`, a contradiction. If `c` is in `A` but not in `E*`,
then `c` reaches `S` inside `A`, so the edge `v -> c` makes `v` reach `S`,
again a contradiction. Hence every consumer of `v` lies in `E* union {b}`;
`E*` is admissibly private.

Conversely, let `E` be any admissibly private set. It contains no vertex of
`S`, since such a vertex has a consumer outside `A union {b}` and therefore
outside `E union {b}`. If a path in `A` from `v` to `S` exists and `v` were in
`E`, closure applied successively along the path would put its terminal
frontier vertex in `E`, a contradiction. Thus `E` is disjoint from
`Pred_A(S)` and is contained in `E*`. Therefore `E*` is the unique greatest
admissibly private set.

The theorem gives an exact structural audit and a linear-time reverse
reachability algorithm. It does not assign distinct cost to frontier paths:
many ancestors can reach the same escape.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite directed acyclic gate graph underlying an unrestricted constant-free AND/OR/NOT circuit |
| Uniform/non-uniform | Every finite non-uniform circuit DAG, chosen gate `b`, and declared distinguished-carrier set |
| Circuit size | No lower bound; reservoir computed in linear graph time from all eligible ancestors and consumer edges |
| Circuit depth | Unrestricted finite depth |
| Fan-in | Circuit AND/OR two and NOT one; graph theorem permits arbitrary fanout and audits every consumer |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact directed reachability and greatest consumer-closed fixed point |
| Asymptotic quantifiers | Every finite DAG, eligible ancestor, frontier vertex, and directed path in `A` |
| Regime | Exact worst-case topology theorem; not a cost injection, circuit lower bound, SAT lower bound, or terminal result |
