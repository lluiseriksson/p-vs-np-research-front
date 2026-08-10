# GATE-004AD — three-block sparsity through signed width four

**Label: PROVED**

There is a fixed alphabet of universally neutral blocks of maximum length 68
such that, after allowing up to three nonoverlapping translated blocks per
slot option and retaining the all-one and `A_rho` options, every disjoint
non-tautological common signed clause family of width at most four has at most
142 members per slot.

Three blocks can realize patterns with three prescribed zeros on distant
quadruples, while `A_rho` supplies `0000` away from six positions. The first
attack is a finite four-coordinate translation certificate analogous to
LEMMA-071. A surviving unbounded matching for every fixed alphabet falsifies
the gate.

The complete identifier-1-through-68 audit finds a stable failure, isolated
in LEMMA-073. A targeted length-48 enrichment still has 35 failures among
530,604 reduced types. LEMMA-074 strengthens this to the complete alphabet of
all identifiers 1 through 1,023: pattern `1110` remains absent on offsets
`{0,5,9,10}`. The next attack must use length at least 52; explicit longer
identifiers repair the returned representatives, so the full gate remains
falsifiable rather than rejected.

LEMMA-075 completes the repair with a fixed 92-identifier alphabet of maximum
block length 68. Its exhaustive `4*71^3` certificate realizes all fourteen
ordinary nonzero masks, while the all-one and `A_rho` options supply masks 0
and 15. Every common signed clause through width four hits a 142-coordinate
set per slot. This proves the gate as a witness construction only. The new
positive rigidity question is GATE-004AE.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block neutral contexts, one long option, signed clauses through width four, and matching |
| Uniform/non-uniform | Uniform finite alphabet/placements; later circuits fully non-uniform |
| Circuit size | No lower bound; proved matching bound `142s` across `s` slots |
| Circuit depth | Fixed blocks bounded; long option may have linear depth; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and translation |
| Asymptotic quantifiers | Fixed `L=68,c_4=142`; every sufficiently large `rho`; every disjoint width-at-most-four common family |
| Regime | Exact witness-construction theorem; not a circuit lower bound or terminal result |
