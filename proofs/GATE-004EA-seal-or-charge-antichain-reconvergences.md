# GATE-004EA — seal or charge antichain reconvergences

**Label: EXPLORATORY**

LEMMA-241 turns a wide coordinate antichain into a named binary
reconvergence tree. NG-175 shows that the tree's merge gates are not payments
until their parent interfaces are certified.

## Falsifiable theorem

For every operational `e=0,h=0` endpoint and every selected coordinate
antichain `S` of size `k>=D_b^DAG`, extract a LEMMA-241 tree to the parent
output and retain the complete old/new four-code functions on its paths and
merges. Prove at least one of:

1. `D_b^DAG` members of `S` admit pairwise nonduplicated independent equal
   cuts, so LEMMA-222 gives parent-preserving real hosts;
2. distinct first reconvergences inject into enough satisfying losses, marked
   origins, or contraction resources to pay `D_b^DAG`;
3. overlapping seals or charges uncross into a strictly smaller joint region
   or strict `W,Q,R_0` descent; or
4. an unsealed branch-to-merge defect survives to a named four-code endpoint
   contradiction.

The theorem is falsified by a refined minimum endpoint whose wide antichain
has only parent-essential, mutually overlapping reconvergence regions, with
no independent cut, injective charge, uncrossing, descent, or surviving
signature contradiction. A merge may be common to many selected sources and
may lie outside the minimum port region; neither occurrence nor path count is
a payment.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with a zero-overhead coordinate antichain and complete downstream reconvergence tree |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple in the wide-antichain branch |
| Circuit size | Parent `K+2`; antichain size at least `D_b^DAG`, with `k-1` named binary reconvergences before deduplicated payment |
| Circuit depth | Unrestricted; antichain-to-output paths and sealing frontiers unbounded |
| Fan-in | AND/OR two; NOT one; fanout, path overlap, merge sharing, and every cut exit audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean path functions, physical cuts, potentials, contraction maps, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, qualifying antichain, selected tree, merge gate, and residual branch |
| Regime | Exact worst-case antichain-reconvergence payment gate; not a generic graph payment, SAT lower bound, or terminal result |

## Cycle-200 audit

LEMMA-243 proves that an irredundant tree cut partitions the selected leaves,
so physical cut capacity is its number of gates rather than covered paths.
LEMMA-244 gives arbitrary leaf multiplicity behind one independently equal
seal; repeated charging is NG-176. GATE-004EB now separates sufficiently
large cut capacity from heavy shared-seal blocks. GATE-004EA remains
`EXPLORATORY`.
