# LEMMA-201 — a counterflow creates a surviving cycle coordinate

**Label: PROVED**

Let `b` be a counterflow boundary at the `Q=0` endpoint. Thus `b` directly
consumes the carrier gate `h` and an other input `r`, both `h` and `r` depend
essentially on the raw source `u`, and the Boolean function at `b` is globally
independent of `u`. Then the undirected output-cone multigraph contains a
nonzero cycle coordinate `gamma_b` formed by the two dependency routes into
`b`. In every satisfying restriction `00`, `01`, and `11`, the restriction
minor maps `gamma_b` to a nonzero cycle coordinate. Its representative may be
contracted; literal survival of its original edges is not asserted.

## Proof

Semantic dependence on `u` implies syntactic reachability from the raw input
`u` in the circuit DAG. Choose directed paths `P_h:u -> ... -> h` and
`P_r:u -> ... -> r`. Append the respective boundary edges `h -> b` and
`r -> b`. In the union of these two `u`-to-`b` paths, choose a common vertex
`w` maximal in a topological ordering before their final reconvergence at
`b`. Their suffixes from `w` to `b` are internally vertex-disjoint. Forgetting
orientation, their symmetric difference is a nonzero cycle `gamma_b` over
`F_2`. The nested cases are included: if, for example, `h` lies on `P_r`, one
suffix is the edge `h -> b` and the other runs from `h` through `r` to `b`.
The two boundary inputs cannot coincide, because then `b` would be an
idempotent copy of the `u`-sensitive function `h`, contrary to global
`u`-independence.

For each satisfying code, LEMMA-185 says that the parent-to-base restriction
loses no cycle-rank unit and changes the cyclic core only by contractions.
LEMMA-174 therefore makes the induced cycle-space quotient injective: no
nonzero parent coordinate maps to zero. Applying it to `gamma_b` proves that
its image is nonzero in each of the three satisfying minors. The image need
not retain the same edge support or a simple-cycle representative.

## Exact boundary of the conclusion

The lemma establishes reconvergence and preservation, not a contradiction.
It proves neither that `gamma_b` is independent of the pre-existing base
cycle space nor that preserving it costs an additional gate. Indeed, equal
rank requires its survival modulo contraction.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau circuit at `W=1`, size-three carrier, `Q=0`, with a counterflow boundary; undirected output-cone multigraph |
| Uniform/non-uniform | Every finite non-uniform hypothetical parent in this endpoint |
| Circuit size | Parent `K+2`; every satisfying pruning loses exactly two binary gates by LEMMA-185 |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; both counterflow routes audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean dependency DAG and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, hypothetical minimum endpoint parent, counterflow boundary, and satisfying code in `{00,01,11}` |
| Regime | Exact worst-case topology statement; not cycle independence, a cost lower bound, plateau exclusion, a SAT lower bound, or terminal result |
