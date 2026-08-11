# GATE-004DD — pay for the first missing independent factor

**Label: EXPLORATORY**

LEMMA-210 removes every counted boundary whose unchanged output has a wire or
one-gate realization over existing globally `u`-independent nondescendant
signals. NG-153 shows that comparable semantics alone do not force such a
realization.

## Falsifiable theorem

For every remaining boundary counted by `R_0`, at least one of the following
holds:

1. **Comparable missing-factor case.** A minimum joint realization of the
   physical outputs forces a reusable globally `u`-independent factor. Adding
   that factor and retargeting `b` can be paid for by deleting or repurposing a
   named `u`-sensitive gate, with no size increase and strict descent; or the
   exact correspondence under one satisfying pruning loses a named third
   binary gate, deletes a non-bridge edge, or exposes a private certificate.
2. **Incomparable case.** The two nonzero witness regions of the row-zero
   cofactors yield the same alternatives after their joint basis cost, shared
   fanout, and all three satisfying pruning maps are reconciled.

For item 1, merely writing the boundary function as a two-gate formula is
insufficient. The proof must identify the new factor, the physical gate that
pays for it, every affected fanout, and the exact before/after gate count. The
theorem fails if a refined minimum parent can keep the first independent
factor at basis distance at least two while every potential and every exact
two-gate satisfying budget remains unchanged.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, after basis-distance-one descent |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; one new independent factor must be paid by a named deletion/repurposing or a strict resource contradiction |
| Circuit depth | Unrestricted; factor distance and shared-fanout depth unbounded |
| Fan-in | AND/OR two; NOT one; all inputs, fanouts, replacement gates, and pruning survivors audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean signal equality, basis distance, physical DAG topology, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual comparable-missing-factor or incomparable boundary |
| Regime | Exact worst-case minimum-joint-cost gate; not a SAT lower bound or terminal result |
