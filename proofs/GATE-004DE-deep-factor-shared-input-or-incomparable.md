# GATE-004DE — deep factor, shared input, or incomparable erasure

**Label: EXPLORATORY**

LEMMA-211 removes every comparable boundary whose independent output has an
aligned-inner two-gate formula and whose counterflow input gate is expendable.
NG-154 shows that comparable semantics alone do not bound the formula depth.

## Falsifiable theorem

For every remaining boundary counted by `R_0`, at least one of the following
holds:

1. **Comparable deep/shared case.** Minimum joint cost forces an aligned
   independent intermediate signal or a physical gate that can be repurposed
   to compute it. The resulting complete formula for the unchanged boundary
   output has no net size increase and gives strict earlier-potential or
   `R_0` descent; alternatively, a named satisfying pruning loses a third
   binary gate, deletes a non-bridge edge, or exposes a private certificate.
   This branch must cover every reason LEMMA-211 can fail: basis distance at
   least three, an unaligned inner gate, a raw counterflow input, or shared
   fanout of that input.
2. **Incomparable case.** The two nonzero row-zero witness regions yield the
   same alternatives after exact joint basis cost, shared fanout, and all
   three satisfying pruning maps are reconciled.

The proof must name every new intermediate, every repurposed or deleted gate,
and every affected fanout. Formula existence, essential-variable counting,
and cofactor comparability alone are insufficient. The theorem fails if a
refined minimum parent realizes the deep/shared comparable branch or the
incomparable branch within all exact two-gate satisfying budgets and with no
lexicographic descent.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, after aligned-inner basis-two descent |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; all new independent factors require named physical payment or an exact resource contradiction |
| Circuit depth | Unrestricted; independent formula depth and shared-fanout depth unbounded |
| Fan-in | AND/OR two; NOT one; raw and gate counterflow inputs plus every fanout and pruning survivor audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean signal equality, basis distance, physical DAG topology, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual deep/shared comparable or incomparable boundary |
| Regime | Exact worst-case minimum-joint-cost gate; not a SAT lower bound or terminal result |

## Cycle-178 audit

LEMMA-212 closes the arbitrary-depth aligned branch whenever a closed private
reservoir supplies one physical vertex for every non-root formula gate.
GATE-004DE-FANOUT-ONE-PRIVATE-BUDGET-ONLY shows that fanout one of the final
counterflow output does not force that reservoir: live escape consumers can
leave only one private vertex while the boundary needs two internal hosts.
GATE-004DF therefore replaces this gate operationally and isolates the exact
private-reservoir deficit, absence of an aligned formula, raw/shared inputs,
and incomparable cofactors. GATE-004DE retains its `EXPLORATORY` label; no
automatic promotion is made.
