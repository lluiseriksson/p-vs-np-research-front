# GATE-004DO — force an independently certified sealed cut

**Label: EXPLORATORY**

LEMMA-220 makes a sealed frontier sufficient. LEMMA-221 and NG-163 show that
the canonical semantic difference frontier cannot be used to establish the
parent equality from which it is defined.

## Falsifiable theorem

For every refined minimum endpoint with `D_b^DAG>0`, construct disjoint
aligned-host rewrites and, for each rewrite, a set `S` such that:

1. `S` is disjoint from every retargeted host and from the parent output, and
   in the union of the old and new DAGs every directed path from a retargeted
   host to the parent output meets `S`;
2. every `s in S` has the same full four-code Boolean function before and
   after the rewrite;
3. each equality in item 2 is derived from named local expressions, exact
   satisfying-pruning maps, or previously proved endpoint identities without
   assuming parent-output equality or defining `S` through the global
   difference set;
4. all vertices retargeted before the cut, all exits, and all shared fanouts
   are named, and the disjoint physical hosts cover `D_b^DAG`; and
5. replacement size and the earlier potentials `W,Q` do not increase, while
   size or `R_0` strictly descends.

Alternatively, trace a path avoiding every independently equal cut to a first
unmatched four-code signature at the output and prove that it forces a third
satisfying loss, a non-bridge deletion, a forbidden cycle-coordinate change,
or a strict `W,Q,R_0` descent.

The theorem is falsified by a refined minimum endpoint with positive aligned
circuit deficit for which every adequately paid host rewrite either lacks an
independently proved equal cut or reaches the output with no named resource or
potential contradiction. Merely testing that the final output is equal,
constructing `Delta` from global semantic comparison, or citing endpoint
minimality without an explicit exchange is inadmissible.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with paired old/new host-rewrite DAGs and certified vertex cuts |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; disjoint paid hosts cover `D_b^DAG` and replacement size does not increase |
| Circuit depth | Unrestricted; cut distance and rewritten region depth unbounded |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; every old/new path, exit, and shared consumer audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean functions, directed vertex cuts, physical losses, potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, counted boundary, proposed host rewrite, and residual branch |
| Regime | Exact worst-case noncircular seal-certification gate; not a SAT lower bound or terminal result |

## Cycle-188 audit

LEMMA-222 proves the exact directed-cut implication. LEMMA-223 shows that
equalities in the three satisfying prunings leave an arbitrary defect at code
`10`, so satisfying-row certification alone is NG-164. GATE-004DP replaces
this gate with the explicit obligation to kill or physically charge every
nonzero code-`10` cut defect. GATE-004DO remains `EXPLORATORY`.
