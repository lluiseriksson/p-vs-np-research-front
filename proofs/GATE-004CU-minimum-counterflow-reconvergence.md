# GATE-004CU — charge a minimum counterflow reconvergence

**Label: EXPLORATORY**

At the unresolved `Q=0` endpoint, apply LEMMA-200 to every globally
`u`-cancelling boundary. Aligned other inputs give two-row masks; `u`-sensitive
other inputs give counterflows with exact rowwise constraints.

## Falsifiable theorem

For every counterflow boundary in a minimum parent, one of the following holds:

1. its two sensitivity routes share a subfunction whose factoring yields a
   same-size strict extremal descent;
2. the auxiliary route becomes redundant in a neutral satisfying code and
   forces a third deletion;
3. the first counterflow divergence supplies a private-cone certificate; or
4. reconvergence at the boundary creates a named cycle whose satisfying minor
   must delete a non-bridge edge.

If no counterflow exists, all boundaries satisfy aligned mask identities on
both rows and form a separate two-row factoring branch. The local gadget in
GATE-004CT-COUNTERFLOW-LOCAL-ONLY forbids using reconvergence existence alone.

## Cycle-168 audit

LEMMA-201 proves the reconvergence part precisely: every counterflow boundary
creates a named nonzero cycle coordinate, and equal-rank satisfying minors
preserve it modulo contraction. This does not prove item 4. On the contrary,
GATE-004CU-CYCLE-EXISTENCE-ONLY records that cycle existence alone cannot
force cycle loss. GATE-004CV is the active quantitative coordinate/factoring
brick.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, and a counterflow boundary |
| Uniform/non-uniform | Every finite non-uniform operational endpoint tuple |
| Circuit size | Parent `K+2`; same-size descent, third deletion, private certificate, or forbidden cycle loss |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; both sensitivity routes and fanout audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean identities and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum `Q=0` size-three parent with counterflow |
| Regime | Exact worst-case minimum-counterflow gate; not a SAT lower bound or terminal result |
