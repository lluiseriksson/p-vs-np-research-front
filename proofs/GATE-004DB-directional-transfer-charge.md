# GATE-004DB — charge directional transfer or incomparable erasure

**Label: EXPLORATORY**

LEMMA-208 splits every comparable transfer by the unique changed code.
GATE-004DA-SATISFYING-EXTERIOR-ONLY shows that the `sigma=0` branch is
invisible in all three satisfying exterior cofactor tables. The `sigma=1`
branch changes only satisfying code `00`.

## Falsifiable theorem

For every residual boundary counted by `R_0`, at least one of the following
holds:

1. **Unsatisfying-only comparable transfer (`sigma=0`).** The specialized
   region or the physical path to the first newly counted boundary admits a
   same-size fanout-preserving factoring with strict net `R_0` descent, or its
   topology yields a private certificate or a non-bridge deletion. No charge
   may be inferred from satisfying exterior gate functions alone.
2. **Code-`00` comparable transfer (`sigma=1`).** The unique changed
   satisfying cofactor yields an explicit same-size factoring or forces a
   third binary deletion in the `00` pruning after every removed and newly
   created boundary is reconciled.
3. **Incomparable transfer.** The two nonzero regions
   `r_00 AND NOT r_10` and `r_10 AND NOT r_00` yield a same-size factoring, a
   private realization, a non-bridge deletion, or a third satisfying-code
   gate loss through the exact LEMMA-200 masks.

Every proof branch must give the physical gate correspondence. In item 1,
only topology, the interior specialization, and minimum-cost data can supply
the missing information. In item 2, observing a changed `00` function is not
itself a deletion: the exact minimum pruning must lose a named third binary
gate. In item 3, semantic witness regions still have no automatic basis cost.

The theorem fails if a refined minimum parent can transfer either directional
comparable defect, or realize incomparable erasure, with zero net potential
change and within every exact two-gate satisfying budget.

## Cycle-175 audit

LEMMA-209 closes both directional branches whenever the specialization is
implemented on a qualifying isolated region and preserves the parent
function: the region loses at least one gate, contradicting minimum size.
Consequently the single-code split of LEMMA-208 is diagnostic only for
nonminimal parent-preserving transfer. GATE-004DC is the active gate and keeps
exactly the cases not covered by that argument: comparable erasure must be
edge-local because an isolatable global specialization is unavailable or
output-changing, or the row-zero cofactors are incomparable.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, split by the unique changed code or incomparable cofactors |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; same-size net descent, third satisfying loss, private certificate, or non-bridge contradiction required |
| Circuit depth | Unrestricted; specialized region and transfer path depth unbounded |
| Fan-in | AND/OR two; NOT one; every fanout, code-local change, and pruning survivor audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactors, physical DAG topology, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual directional-or-incomparable counterflow boundary |
| Regime | Exact worst-case directional transfer gate; not a SAT lower bound or terminal result |
