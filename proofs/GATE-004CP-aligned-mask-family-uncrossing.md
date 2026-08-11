# GATE-004CP — uncross the aligned boundary-mask family

**Label: EXPLORATORY**

LEMMA-195 classifies every shared exit from `h`: AND masks vanish on `Delta`,
and OR masks cover `Delta`. Boundary count alone is unavailable.

## Falsifiable theorem

Every complete aligned-mask family yields one of:

1. common factoring that realizes all boundaries after removing `g,h` at no
   greater size and strictly lowers an extremal potential;
2. a boundary requiring a third neutral-code deletion;
3. a private-cone certificate at the first mask divergence; or
4. reconvergent mask routes forcing deletion of a non-bridge edge.

The proof must charge shared realization cost, cover both mask polarities, and
handle the arbitrarily large local families of the boundary-count no-go.

LEMMA-196 shows that an aligned `01/11` boundary can still carry an unequal
`00/10` signature. Factoring from satisfying masks alone is therefore
`NO-GO`. GATE-004CQ is the active refinement and audits complete four-code
boundary vectors before any global rewrite.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1` with size-three carrier and complete aligned-mask family |
| Uniform/non-uniform | Every finite non-uniform operational tuple |
| Circuit size | Parent `K+2`; neutral loss budget exhausted; boundary family unrestricted |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; all shared fanout and mask subcircuits audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean mask containment and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum size-three-carrier parent |
| Regime | Exact mask-family uncrossing gate; not a SAT lower bound or terminal result |
