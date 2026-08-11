# LEMMA-212 — an aligned formula with a private reservoir descends

**Label: PROVED**

Use the refined minimum endpoint and let `b` be a boundary counted by `R_0`.
Suppose the Boolean function `B` computed at `b` has a constant-free
AND/OR/NOT formula `T` with `m >= 1` gates over existing signals, and assume:

1. every non-root gate function of `T` is independent of both fresh inputs
   `u,t`;
2. there is a set `E` of exactly `m-1` strict ancestors of `b`, disjoint from
   `h` and every distinguished carrier vertex used to define `W,Q,R_0`, such
   that every edge leaving `E` targets a vertex of `E` or `b`;
3. every formula leaf is globally `u`-independent, is distinct from
   `E union {b}`, and is not a descendant of any vertex of `E union {b}`.

Then the parent is not the refined minimum endpoint. Map the non-root formula
gates bijectively to `E` and the root to `b`. Retargeting those physical
vertices realizes `T`, preserves the parent function, does not increase size,
and gives an earlier-potential decrease or strict `R_0` descent.

## Proof

View `T` as a rooted formula tree. Choose any topological bijection from its
`m-1` non-root gate occurrences to `E`; the particular old topology inside
`E` is irrelevant because every mapped vertex is retargeted. Retarget the
vertices in formula order, and retarget `b` to the root operation. Condition 3
precludes every new leaf-to-formula back edge. Formula order precludes every
new internal back edge, so the replacement DAG is acyclic.

The new function at `b` is exactly `B`. Every old edge leaving `b` is retained,
so all descendants outside the replaced region keep their functions by
topological induction. Old functions in `E` disappear, but condition 2 says no
vertex outside `E union {b}` consumed them. Thus the parent output is unchanged.
No physical gate is added. If constant propagation or the rewrite makes a
gate dead, deleting it gives a strict size contradiction; otherwise size is
unchanged.

Every new function on `E` is independent of both `u,t` by condition 1. Hence
the rewrite cannot add a misaligned common gate counted by `W`. It also creates
no new `u`-sensitive direct child of `h`, so `Q` cannot increase. All functions
outside `E union {b}`, including the distinguished carrier, and the function
at `b` are unchanged. Therefore `W,Q`
do not increase. A strict decrease in either contradicts the earlier
lexicographic choice.

Assume instead that `W,Q` remain equal. Every new input to `b` is either a
globally `u`-independent leaf or the output of a non-root formula gate in `E`,
which is also globally `u`-independent. Thus the retargeted `b` no longer
consumes the `u`-sensitive carrier `h` and leaves `R_0`. No new boundary enters
`R_0`: replacement gates in `E` are globally `u`-independent, `b` keeps its
function, and every vertex outside the replaced region is unchanged. Hence
`R_0` strictly decreases, contradicting the refined endpoint.

LEMMA-210 is the case `m=1`; LEMMA-211 is the case `m=2` with the counterflow
input as the one-vertex reservoir. This lemma proves only a sufficient exchange
certificate. It does not prove that a residual minimum boundary has an aligned
formula or a sufficiently large private reservoir.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically refined minimum unrestricted constant-free AND/OR/NOT DAG with free wires |
| Uniform/non-uniform | Every finite non-uniform endpoint parent and every counted boundary supplied with the aligned-formula/private-reservoir certificate |
| Circuit size | `m` physical vertices (`m-1` in `E` and `b`) are repurposed; size does not increase and may strictly decrease after propagation |
| Circuit depth | Unrestricted; nondescendant leaves and formula order guarantee acyclicity |
| Fan-in | AND/OR two; NOT one; `E` excludes distinguished carrier vertices, every edge leaving `E` stays in `E union {b}`, and fanout of `b` is retained |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean signal equality, rooted formulas, and physical DAG rewiring |
| Asymptotic quantifiers | Every `m>=1`, nonconstant base, hypothetical refined endpoint, counted boundary, and supplied certificate |
| Regime | Exact worst-case sufficient exchange theorem; not existence of the certificate, a SAT lower bound, or terminal result |
