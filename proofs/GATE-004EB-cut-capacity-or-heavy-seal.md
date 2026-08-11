# GATE-004EB — pay cut capacity or exploit a heavy shared seal

**Label: EXPLORATORY**

LEMMA-243 replaces branch coverage by physical cut capacity. NG-176 shows
that a single equal gate may seal arbitrarily many selected antichain paths.

## Falsifiable theorem

For every wide-antichain operational endpoint, extract a LEMMA-241 tree and
search for an independently certified inclusion-minimal equal cut satisfying
LEMMA-222. If such a cut `C` exists, partition the selected coordinate leaves
into the LEMMA-243 blocks `S_c`. Prove at least one of:

1. a cut `C` exists with `|C|>=D_b^DAG`, and `D_b^DAG` distinct physical cut gates inject into
   parent-preserving hosts, satisfying losses, marked origins, or contraction
   resources without duplication;
2. a cut `C` exists and some heavy block `S_c` supports an explicit joint replacement of its whole
   pre-seal region that releases enough gates or strictly decreases
   `W,Q,R_0`;
3. a cut `C` exists and two heavy blocks or their seals uncross into a larger-capacity equal cut or
   a strictly smaller physical region; or
4. no path-complete independently equal cut exists, and the first unsealed
   four-code defect survives to a named endpoint contradiction.

The theorem is falsified by a refined minimum endpoint with `|C|<D_b^DAG`
whose heavy blocks are jointly minimum and parent-essential, whose seals do
not uncross or inject into distinct resources, and whose unsealed defects all
cancel without descent. Cut membership, equality, block coverage, physical
identity, and every exit of a proposed replacement region must be explicit.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with a coordinate-antichain tree and independently equal irredundant cut |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple in the sealed or unsealed width branch |
| Circuit size | Parent `K+2`; physical cut capacity `|C|`, deficit `D_b^DAG`, and complete heavy pre-seal regions |
| Circuit depth | Unrestricted; leaf-to-cut and cut-to-output paths unbounded |
| Fan-in | AND/OR two; NOT one; fanout, shared seals, cut exits, and block overlap audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cut functions, exact shared-DAG cost, potentials, contraction maps, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, minimal equal cut, cut block, heavy region, and residual branch |
| Regime | Exact worst-case cut-capacity/heavy-seal gate; not a generic cut theorem, SAT lower bound, or terminal result |
