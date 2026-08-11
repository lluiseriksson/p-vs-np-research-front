# GATE-004DS — force physical payment from overlap-swap provenance

**Label: EXPLORATORY**

LEMMA-227 reduces a two-changing-input zero-defect gate to exclusive support
masks plus an overlap region where its inputs swap. NG-167 shows that the
functional swap alone is not a physical resource.

## Falsifiable theorem

For every first two-sided cancellation left by GATE-004DR:

1. pay the two exclusive-support regions using path-complete LEMMA-225 masks;
2. on every nonempty overlap support, trace two named old/new defect paths to
   their first distinct physical divergence points and back to the swap gate;
3. prove that their provenance yields a globally uncharged satisfying loss,
   a non-bridge deletion, destruction of a named cycle coordinate, an actual
   retargetable host, or an explicit size-preserving `W,Q,R_0` descent; and
4. deduplicate shared divergence prefixes, swap gates, masks, and cycle
   coordinates across all hosts and defects.

An abstract `01<->10` table, crossbar factorization without a size bound, or
undifferentiated cycle-rank existence is insufficient. The theorem is
falsified by a refined minimum endpoint with positive aligned deficit whose
overlap swaps have completely shared or rank-neutral provenance, insufficient
real hosts, and no exact exchange or potential descent.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with marked overlap-swap defect paths and physical divergence/reconvergence data |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; deduplicated real hosts or physical contradictions must cover residual `D_b^DAG` |
| Circuit depth | Unrestricted; divergence and reconvergence paths unbounded |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; all shared prefixes, masks, swaps, and cycles audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code defect supports, physical DAG paths, potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, overlap assignment region, path pair, and residual branch |
| Regime | Exact worst-case swap-provenance gate; not a SAT lower bound or terminal result |

## Cycle-192 audit

LEMMA-228 turns coexisting physical routes into distinct origins or a
common-origin cycle. LEMMA-229 proves that the latter survives every
satisfying minor by contraction; charging it as a destroyed coordinate is
NG-168. GATE-004DT replaces this gate with distinct-origin certification or a
marked-support exchange on the surviving cycle. GATE-004DS remains
`EXPLORATORY`.
