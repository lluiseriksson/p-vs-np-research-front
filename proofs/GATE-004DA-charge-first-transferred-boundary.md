# GATE-004DA — charge the first transferred boundary

**Label: EXPLORATORY**

LEMMA-207 shows that every comparable specialization preserving the parent
function but failing to lower `R_0` creates a changed path from `r` to a newly
counted direct `h`-boundary. GATE-004CZ-TRANSFER-PATH-ONLY shows that path
existence, length, and changed-gate count are insufficient without minimum
cost or pruning data.

## Falsifiable theorem

For every residual boundary counted by `R_0`, at least one of the following
holds:

1. **Comparable transfer case.** Specialize the selected cofactor and choose
   the first newly counted direct `h`-boundary `c` on a LEMMA-207 transfer
   path. The sub-DAG from `r` through the other input `q` of `c` admits a
   same-size fanout-preserving factoring with a strict net decrease of `R_0`
   and no increase of earlier potentials, or one satisfying restriction
   loses a third binary gate, deletes a non-bridge edge, or exposes a private
   realization certificate.
2. **Incomparable case.** Both nonzero regions
   `r_00 AND NOT r_10` and `r_10 AND NOT r_00` can be followed through the
   exact LEMMA-200 masks to a same-size factoring, a private realization, a
   non-bridge deletion, or a third satisfying-code gate loss.

For item 1, the proof must compare the complete set of boundaries removed and
created; charging only the path length or one disappearing boundary is
invalid. It must identify the physical gates surviving each satisfying
pruning and show the exact gate correspondence. For item 2, Boolean witness
regions alone remain semantic data and do not supply a circuit realization.

The theorem fails if a refined minimum parent can move comparable
counterflow between direct `h`-boundaries with zero net potential change and
within every exact two-gate satisfying budget, or if incomparable erasure has
the same property.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, with a localized transfer path or incomparable cofactors |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; same-size net descent, third satisfying loss, private certificate, or non-bridge contradiction required |
| Circuit depth | Unrestricted; transfer sub-DAG depth unbounded |
| Fan-in | AND/OR two; NOT one; every fanout, transferred boundary, and satisfying-pruning survivor audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactors, finite changed-gate paths, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual transferred-or-incomparable counterflow boundary |
| Regime | Exact worst-case minimum-cost transfer gate; not a SAT lower bound or terminal result |
