# GATE-004CX — realize the row-zero counterflow erasure at exact cost

**Label: EXPLORATORY**

LEMMA-203 confines counterflow to `00/10`, and LEMMA-204 erases it
semantically at the boundary. The remaining obligation is basis-level cost.

Refine the finite extremal choice by minimizing `R_0`, the number of direct
`h`-boundaries whose other input has unequal `00/10` cofactors, after the
previous potentials `W` and `Q`.

## Falsifiable theorem

For every boundary counted by `R_0`, at least one of the following holds:

1. the signal `r^dagger` from LEMMA-204 is realizable on the edge into `b`
   using existing topology and gates freed by the rewrite, with total size at
   most `K+2`, all other consumers unchanged, and strictly smaller `R_0`;
2. one satisfying restriction eliminates a third binary gate;
3. one satisfying restriction deletes an edge that is non-bridge at deletion;
4. the boundary has a private realization certificate.

Item 1 contradicts the refined extremal choice; items 2–4 contradict the
exact plateau bookkeeping or prior private-cone extremality. A proof must give
the explicit gate correspondence and fanout-preserving rewrite. The abstract
meet/join signal alone is invalid by GATE-004CW-SEMANTIC-ERASURE-ONLY.

The theorem fails if a minimum parent can share the `r` cone so that every
edge-local erasure costs an extra gate while all satisfying restrictions
retain their exact two-gate, rank-neutral budgets.

## Cycle-171 audit

LEMMA-205 discharges the comparable case whenever a cofactor-private region
is present. GATE-004CX-GLOBAL-SPECIALIZATION-ONLY shows why a shared `r`
cannot simply be specialized globally. GATE-004CY is the active residual
brick for shared comparable cones or incomparable row-zero cofactors.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, refined by row-zero counterflow count `R_0` |
| Uniform/non-uniform | Every finite non-uniform operational endpoint tuple |
| Circuit size | Parent `K+2`; same-size strict `R_0` descent or exact resource contradiction |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; all fanouts of the replaced signal audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactors, meet/join erasure, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, hypothetical refined minimum parent, and row-zero counterflow boundary |
| Regime | Exact worst-case basis-realization gate; not a SAT lower bound or terminal result |
