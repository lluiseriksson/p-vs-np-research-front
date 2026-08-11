# LEMMA-202 — abstract cycle alignment across satisfying minors is tautological

**Label: PROVED**

Let `G` be the parent output-cone multigraph at the exact plateau, and for each
satisfying code `s in {00,01,11}` let

`rho_s: Z_1(G;F_2) -> Z_1(G_s;F_2)`

be the cycle-space quotient induced by restriction, pruning, and contraction.
Then every `rho_s` is an isomorphism. Consequently, for any two satisfying
codes `s,t`, the transition map

`T_{s,t}=rho_t o rho_s^{-1}`

is an isomorphism and sends `rho_s(gamma)` to `rho_t(gamma)` for every parent
cycle coordinate `gamma`. In particular, abstract cross-minor alignment of
`gamma_b` supplies no invariant that distinguishes a counterflow cycle from
any other parent cycle.

## Proof

LEMMA-185 gives equal parent and minor cycle rank for every satisfying code
and says that cyclic-core operations are contractions. LEMMA-174 therefore
makes each induced quotient `rho_s` injective. Its domain and codomain have
the same finite dimension, so it is bijective.

For satisfying `s,t`, the inverse `rho_s^{-1}` exists, hence `T_{s,t}` is an
isomorphism. Direct substitution gives

`T_{s,t}(rho_s(gamma))=rho_t(rho_s^{-1}(rho_s(gamma)))=rho_t(gamma)`.

This holds for every `gamma`, without using the boundary, its Boolean
cofactors, or its edge support. The statement does not identify physical
edges across minors: contractions may change every representative.

## Subdivision witness

The lack of support information is real. Subdivide a non-bridge edge `e` of
any connected multigraph `H` by two new degree-two vertices. Contracting two
edges of the resulting three-edge path recovers `H`, preserves cycle rank, and sends every
cycle through the subdivided path to the original cycle through `e`. The same
contraction pattern may be assigned to three formal minor labels. Thus exact
two-vertex disappearance, nonzero coordinate survival, and cross-minor
alignment coexist with no independent coordinate or non-bridge deletion.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact-plateau output-cone multigraphs and satisfying restriction minors |
| Uniform/non-uniform | Every finite non-uniform hypothetical parent and its three satisfying minors |
| Circuit size | Parent `K+2`; each satisfying pruning loses exactly two binary gates; graph witness adds two subdivision vertices |
| Circuit depth | Unrestricted; subdivision witness has arbitrary ambient depth |
| Fan-in | Circuit application retains AND/OR two and NOT one; graph theorem is fan-in independent |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite cycle spaces and linear isomorphisms over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, hypothetical exact-plateau parent, satisfying pair of codes, and parent cycle coordinate |
| Regime | Exact abstract-coordinate theorem; not marked-support transport, Boolean factoring, plateau exclusion, SAT lower bound, or terminal result |
