# LEMMA-229 — a common-origin swap cycle survives every satisfying minor

**Label: PROVED**

At the exact size-three minimum plateau, suppose the common-origin branch of
LEMMA-228 produces a nonzero cycle coordinate `gamma` in the connected parent
output-cone multigraph. Then for every satisfying code
`s in {00,01,11}`, the parent-to-minor restriction maps `gamma` to a nonzero
cycle coordinate. Its representative may be contracted and need not retain
the same physical edges.

## Proof

LEMMA-185 proves that every satisfying restriction loses exactly two binary
gates through rank-neutral operations and changes the cyclic core only by
contractions. Parent and minor cycle ranks are equal. LEMMA-174 therefore
makes the induced map on cycle spaces an isomorphism: no nonzero parent
coordinate maps to zero. Apply it to `gamma`.

This is the same preservation mechanism used for the earlier counterflow
coordinate in LEMMA-201 and the cross-minor audit in LEMMA-202. The result is
survival, not a payment. Any useful conclusion must retain marked edge support
or prove a separate minimum-cost exchange.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT exact plateau and connected undirected parent/minor output-cone multigraphs |
| Uniform/non-uniform | Every finite non-uniform hypothetical endpoint and supplied common-origin provenance cycle |
| Circuit size | Parent `K+2`; each satisfying pruning loses exactly two binary gates without rank loss |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; cycle routes physically marked |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Restriction minors, contractions, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, endpoint, common-origin swap cycle, and satisfying code |
| Regime | Exact worst-case cycle-survival theorem; not cycle independence, host payment, SAT lower bound, or terminal result |
