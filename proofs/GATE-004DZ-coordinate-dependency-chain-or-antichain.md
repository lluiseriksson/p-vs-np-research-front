# GATE-004DZ — pay a coordinate dependency chain or antichain

**Label: EXPLORATORY**

LEMMA-238 turns the `e=0,h=0` endpoint branch into a coordinate dependency
poset. NG-174 forbids counting all coordinate gates as independent, while
LEMMA-240 supplies an exact height/width split.

## Falsifiable theorem

For every operational residual endpoint with `e=0,h=0`, use the actual
minimum physical region `U` as a coordinate-only realization. Let `q=|U|`,
let `H,W` be its reachability height and width, and let `D=D_b^DAG` be the
remaining aligned physical deficit. Prove the following exhaustive payment:

1. if `W>=D`, select `D` incomparable coordinate gates and construct
   pairwise nonduplicated, parent-preserving sealed regions or inject them into
   distinct satisfying losses, origins, or contraction resources;
2. if `H>=D`, select a `D`-gate dependency chain and extract distinct physical
   charges along it, or prove a strict `W,Q,R_0` descent, exchange, or
   four-code endpoint contradiction; and
3. if `H<D` and `W<D`, use `q<=HW<(D)^2` to reduce the complete labeled
   coordinate region to a bounded case, without discarding its exterior
   fanouts or parent-transfer functions.

When `D=0` the obligation is vacuous and must not manufacture a host. The
theorem is falsified by a refined endpoint with positive `D` whose selected
chain and antichain gates have only overlapping or parent-essential payment
regions, while the bounded remainder admits no contradiction or descent.

Reachability incomparability is not downstream disjointness; chain membership
is not expendability. Every claimed resource must retain physical identity
through the satisfying contraction maps and pass the independent-cut test.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with a zero-excess, zero-overhead physical port region |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple in the `e=0,h=0` branch |
| Circuit size | Parent `K+2`; coordinate region `q=|U|`, aligned deficit `D_b^DAG`, and `q<=HW` |
| Circuit depth | Unrestricted; coordinate dependency height `H` explicit |
| Fan-in | AND/OR two; NOT one; fanout, antichain reconvergence, chain dependencies, and sealed regions audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean coordinate functions, reachability posets, potentials, contraction maps, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, positive deficit, coordinate gate, chain, antichain, and residual branch |
| Regime | Exact worst-case coordinate-dependency payment gate; not a generic poset payment, SAT lower bound, or terminal result |

## Cycle-199 audit

LEMMA-241 converts every width-`k` common-output antichain into a named tree
with exactly `k-1` binary reconvergences. LEMMA-242 shows that all those gates
may remain parent-live and non-substitutable, so reconvergence count alone is
NG-175. GATE-004EA now attacks independent sealing or physical charging of
the width branch. The height and bounded-remainder branches of GATE-004DZ
remain `EXPLORATORY`.
