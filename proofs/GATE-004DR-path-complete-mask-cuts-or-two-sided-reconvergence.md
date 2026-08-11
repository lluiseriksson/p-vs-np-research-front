# GATE-004DR — path-complete mask cuts or two-sided reconvergence

**Label: EXPLORATORY**

LEMMA-225 closes the semantic one-sided branch: an exact support mask gives an
independent full-function seal. LEMMA-226 and NG-166 require physical payment
to remain on the actually retargeted host set; masks and seal gates are not
additional hosts.

## Falsifiable theorem

For every refined endpoint and every proposed disjoint host set intended to
cover `D_b^DAG`, prove either:

1. every union-DAG path from each retargeted host to the parent meets a
   one-sided cut gate satisfying LEMMA-225, so LEMMA-222 preserves the parent,
   the retargeted hosts alone supply the deduplicated payment, and the complete
   rewrite does not increase `W,Q` while strictly decreasing size or `R_0`; or
2. a path reaches a first two-changing-input cancellation, whose two named
   defect routes force a distinct satisfying loss, non-bridge deletion,
   noncontractible cycle-coordinate change, or strict potential descent.

No mask or seal gate may be counted unless a separate replacement proves it
free, and shared masks, hosts, paths, and reconvergences are globally
deduplicated. The theorem is falsified by a refined minimum endpoint with
positive aligned deficit in which too few real hosts admit path-complete
one-sided cuts and every two-sided branch is rank-neutral, shared, and admits
no descent.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with real host sets, path-complete mask cuts, and two-sided defect routes |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; only actually retargeted disjoint hosts count toward `D_b^DAG` |
| Circuit depth | Unrestricted; host-to-cut and reconvergence paths unbounded |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; every host, mask, seal, and two-sided path audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code cofactors, directed cuts, physical host sets, potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, proposed host, cut path, mask, and two-sided cancellation branch |
| Regime | Exact worst-case path-complete host-certification gate; not a SAT lower bound or terminal result |

## Cycle-191 audit

LEMMA-227 partitions the two-sided branch into exclusive one-sided masks and
an overlap swap. NG-167 shows that the functional swap is not itself a lost
gate or cycle coordinate. GATE-004DS replaces this branch with marked physical
divergence/reconvergence provenance and exact minimum-cost payment. GATE-004DR
remains `EXPLORATORY`.
