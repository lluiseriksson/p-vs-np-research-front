# GATE-004DC — edge-local comparable or incomparable erasure

**Label: EXPLORATORY**

LEMMA-209 excludes every comparable branch in which a qualifying isolated
region can be specialized while preserving the parent function. The residual
minimum-parent obstruction is therefore not a function-preserving global
transfer.

## Falsifiable theorem

For every residual boundary counted by `R_0`, at least one of the following
holds:

1. **Comparable edge-local case.** Either no region satisfying conditions
   1–4 of LEMMA-206 exists because a physical interior signal has an escaping
   fanout, or specializing every such region to the cofactor selected at `b`
   changes the parent output. Nevertheless, the semantic meet/join erasure at
   the single edge `r -> b` has a fanout-preserving AND/OR/NOT realization
   whose total size does not increase and whose physical boundary audit gives
   strict descent, a third satisfying-code binary deletion, a private
   certificate, or a non-bridge contradiction.
2. **Incomparable case.** The two nonzero witness regions
   `r_00 AND NOT r_10` and `r_10 AND NOT r_00` admit an exact basis-level
   factoring with the same alternatives, after all shared fanouts and all
   three satisfying pruning maps are reconciled.

The theorem fails if a refined minimum parent realizes an edge-local
comparable erasure, or an incomparable erasure, at zero net potential change
and within each exact two-gate satisfying budget. A Boolean identity alone is
not evidence: the proof must name the replacement gates and the physical
correspondence under every pruning.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, after isolated parent-preserving specialization is excluded |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; a same-size strict descent, third satisfying loss, private certificate, or non-bridge contradiction is required |
| Circuit depth | Unrestricted; shared interior escapes and edge-local replacement depth are unbounded |
| Fan-in | AND/OR two; NOT one; every interior and output fanout, replacement edge, and pruning survivor audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactors, meet/join erasure, physical DAG topology, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual comparable-edge-local or incomparable counterflow boundary |
| Regime | Exact worst-case basis-realization gate; not a circuit lower bound for SAT or a terminal result |

## Cycle-176 audit

LEMMA-210 closes every boundary whose unchanged output function is available
from existing globally `u`-independent nondescendant signals at basis distance
zero or one. GATE-004DC-COMPARABILITY-BASIS-ONE-ONLY shows that comparability
and exact cancellation alone do not force that certificate, even when the
counterflow is confined to `00/10`. GATE-004DD is the active gate: use minimum
joint cost or exact pruning to pay for the first missing independent factor,
or resolve the incomparable branch.
