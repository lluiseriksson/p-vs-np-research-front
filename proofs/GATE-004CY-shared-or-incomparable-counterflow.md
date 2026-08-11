# GATE-004CY — charge shared or incomparable counterflow

**Label: EXPLORATORY**

LEMMA-205 excludes every counterflow that is both comparable and equipped
with a cofactor-private region. Every remaining boundary is therefore shared
or has incomparable row-zero cofactors.

## Falsifiable theorem

For every remaining counterflow boundary, at least one of the following
holds:

1. **Shared comparable case.** The first escape from every candidate
   cofactor region reaches a second live consumer whose four-code signature
   yields a same-size fanout-preserving exchange, a strict earlier potential
   descent, or a second cancellation resource that exceeds a satisfying
   two-gate budget.
2. **Incomparable case.** Both witness regions
   `r_00 AND NOT r_10` and `r_10 AND NOT r_00` are nonzero; transporting them
   through the exact LEMMA-200 masks yields a private realization, a
   non-bridge deletion, or a third satisfying-code gate loss.

A proof must identify the first shared escape or both explicit incomparable
witness assignments and then give the gate/resource correspondence. Merely
specializing `r` globally is invalid by
GATE-004CX-GLOBAL-SPECIALIZATION-ONLY.

The theorem fails if a minimum parent can share every comparable cofactor
cone without an exchange and can realize incomparable meet/join erasure
within the exact rank-neutral budgets of all satisfying minors.

## Cycle-172 audit

LEMMA-206 proves the shared comparable branch whenever every secondary direct
consumer masks the selected cofactor specialization. Terminal output equality
alone is not enough: GATE-004CY-TERMINAL-OUTPUT-ONLY transfers the counted
counterflow from one `h`-boundary to another while preserving the parent
function. GATE-004CZ is the active residual brick for the first unmasked
consumer or incomparable cofactors.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, after private-comparable exclusion |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; same-size descent, third satisfying loss, private certificate, or non-bridge contradiction required |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; every shared escape and fanout audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactors, pointwise order, meet/join, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual shared-or-incomparable counterflow boundary |
| Regime | Exact worst-case residual counterflow gate; not a SAT lower bound or terminal result |
