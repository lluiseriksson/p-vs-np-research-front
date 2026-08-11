# GATE-004CK-SIZE-TWO-TOPOLOGY-ONLY — the minimum carrier topology is realizable nonminimally

**Label: NO-GO**

## Tempting inference

Treat `H_{01,11}={h,n}` with `h -> n`, an earliest switching NOT, and the
complete output table `A,A,0,A` as already contradictory.

## Failure

LEMMA-191 realizes exactly those semantic and directed-topology requirements
for every nonconstant base by a uniform six-gate extension. Its first
`01/11` cancellation boundary is the binary gate `i=t OR n`.

The witness is redundant and loses six displayed gates rather than exactly
two when pruned back to the base. It is therefore not a minimum plateau or a
counterexample to GATE-004CK. It proves only that carrier size two, the edge
`h -> n`, earliest-NOT order, binary cancellation, and the four output
cofactors do not by themselves yield a contradiction. Any exclusion must use
minimum size, the three exact two-binary-deletion maps, private-cone cost, or
cycle-rank preservation.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted AND/OR/NOT exact-table extension compared with plateau obligations |
| Uniform/non-uniform | Uniform finite extension for every nonconstant base; no minimum-parent claim |
| Circuit size | Six gates beyond an arbitrary base circuit; difference carrier has exactly two gates |
| Circuit depth | Unrestricted base depth; constant extension depth |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors only |
| Asymptotic quantifiers | Every nonconstant base and every assignment in the LEMMA-191 construction |
| Regime | Structural no-go for size-two-topology-only reasoning; not a plateau counterexample, SAT lower bound, or terminal result |
