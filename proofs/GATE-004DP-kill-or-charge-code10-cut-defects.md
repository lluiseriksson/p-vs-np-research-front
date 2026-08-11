# GATE-004DP — kill or charge every code-10 cut defect

**Label: EXPLORATORY**

LEMMA-222 reduces parent preservation to an independently equal cut.
LEMMA-223 shows that exact satisfying-pruning equality leaves precisely one
Boolean defect per candidate cut gate:

```text
d_s(x)=C_s(1,0,x) xor C'_s(1,0,x).
```

## Falsifiable theorem

For every refined minimum endpoint with `D_b^DAG>0`, construct disjoint paid
host rewrites and a structural cut `S` meeting LEMMA-222 such that every
`d_s=0`; or, for each nonzero defect, trace its support through the code-`10`
parent cone to the first gate where it is cancelled and prove one of:

1. an explicit size-nonincreasing uncrossing strictly decreases `W,Q,R_0`;
2. the cancellation exposes a previously uncharged satisfying loss or a
   non-bridge deletion;
3. it destroys a named cycle coordinate rather than merely contracting it; or
4. its physical region supplies a disjoint host payment toward `D_b^DAG`.

All defects sharing gates or a cancellation front must be deduplicated, and
every old/new path from a retargeted host to the parent must be named. The
theorem is falsified by a refined endpoint with positive aligned deficit whose
nonzero code-`10` cut defects all cancel without a paid host, extra loss,
noncontractible cycle change, or strict potential descent. Equality on only
`00,01,11` and terminal-output equality are inadmissible substitutes.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with paired host rewrites, structural cuts, and code-10 defect propagation |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; disjoint payments cover `D_b^DAG` and every replacement is size-nonincreasing |
| Circuit depth | Unrestricted; defect propagation and cancellation depth unbounded |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; every shared defect path and cancellation front audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code cofactors, `F_2` difference signatures, physical losses, potentials, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, candidate host rewrite, cut gate, nonzero defect, and residual branch |
| Regime | Exact worst-case code-10 defect gate; not a SAT lower bound or terminal result |

## Cycle-189 audit

LEMMA-224 classifies the first cancellation algebraically into a one-sided
mask or a two-changing-input interaction. NG-165 shows that the local event is
not itself a physical payment. GATE-004DQ replaces this gate with the exact
minimum-cost mask-region or two-path reconvergence obligation. GATE-004DP
remains `EXPLORATORY`.
