# GATE-004CZ — charge unsafe shared or incomparable counterflow

**Label: EXPLORATORY**

LEMMA-206 excludes every comparable counterflow having a region whose
secondary direct consumers mask the selected cofactor specialization.
GATE-004CY-TERMINAL-OUTPUT-ONLY shows that equality only at the parent output
is insufficient: an intermediate consumer can transfer the counted
counterflow to another `h`-boundary.

## Falsifiable theorem

For every residual boundary counted by `R_0`, at least one of the following
holds:

1. **Unsafe shared comparable case.** For the cofactor selected by the
   boundary operation, choose a candidate unique-output region and the first
   secondary direct consumer whose function changes under specialization.
   The changed four-code signature yields a same-size fanout-preserving
   exchange, a strict descent in an earlier potential, a net decrease in the
   total number of counterflow boundaries after all transfers, or a second
   cancellation resource exceeding one satisfying two-gate budget.
2. **Incomparable case.** Both witness regions
   `r_00 AND NOT r_10` and `r_10 AND NOT r_00` are nonzero; transporting their
   explicit witness assignments through the LEMMA-200 masks yields a private
   realization, a non-bridge deletion, or a third satisfying-code gate loss.

The proof must follow every changed immediate-consumer signature until it is
masked or charged. Counting the original boundary without subtracting newly
created boundaries is invalid by GATE-004CY-TERMINAL-OUTPUT-ONLY. For the
incomparable branch, merely naming the two nonzero Boolean regions supplies no
circuit-size bound.

The theorem fails if a refined minimum parent can circulate comparable
counterflow through an arbitrarily long chain of unsafe consumers with zero
net potential change, or can realize incomparable meet/join erasure within
the exact rank-neutral budgets of all satisfying minors.

## Cycle-173 audit

LEMMA-207 proves that every comparable failure of strict `R_0` descent has a
changed path ending at the other input of a newly counted direct
`h`-boundary. GATE-004CZ-TRANSFER-PATH-ONLY realizes such paths at arbitrary
length while preserving the parent and total `R_0`, so path topology alone is
insufficient. GATE-004DA is the active minimum-cost brick: charge the first
transferred boundary using exact pruning data, or resolve the incomparable
branch.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, after consumer-masked comparable exclusion |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; same-size net descent, third satisfying loss, private certificate, or non-bridge contradiction required |
| Circuit depth | Unrestricted; unsafe-consumer chains may have arbitrary depth |
| Fan-in | AND/OR two; NOT one; every changed immediate consumer and transferred boundary audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactors, pointwise order, meet/join, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual unsafe-shared-or-incomparable counterflow boundary |
| Regime | Exact worst-case residual counterflow gate; not a SAT lower bound or terminal result |
