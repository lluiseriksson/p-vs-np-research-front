# GATE-004DF — charge the private-reservoir deficit

**Label: EXPLORATORY**

LEMMA-212 removes every counted boundary whose unchanged function has an
aligned formula and enough private ancestors to host every non-root formula
gate. NG-155 shows that fanout one of the counterflow output does not imply
that budget.

## Falsifiable theorem

For a remaining comparable boundary `b`, define `rho_b` as the maximum size
of an admissibly `b`-private strict-ancestor set, excluding `h` and every
distinguished carrier vertex. When an aligned formula over existing
globally `u`-independent nondescendant signals exists, define `A_b` as the
minimum number of its non-root gates and

```text
D_b = max(0, A_b - rho_b).
```

Prove that every refined minimum endpoint with `D_b>0` supplies at least
`D_b` named physical payments outside the private reservoir: gates deleted by
an exact satisfying pruning, repurposable non-bridge gates, or gates in a
consumer-masked region whose specialization strictly saves them. The paid
rewrite must preserve every exterior consumer, not increase size, and give a
strict earlier-potential or `R_0` descent. If no aligned formula exists, prove
one of the same resource contradictions or construct an aligned formula with
an explicitly paid cost. Treat raw/shared counterflow inputs and incomparable
row-zero cofactors as separate quantified branches.

The theorem is falsified by a refined minimum parent for which every aligned
formula has positive deficit (or none exists), all candidate external payment
gates are live bridges or shared consumers, all three satisfying prunings stay
within their exact two-gate losses, and no same-size lexicographic descent is
available. A proof must name every charged vertex and demonstrate disjointness;
aggregate gate counts or formula existence alone do not suffice.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined minimum unrestricted AND/OR/NOT plateau at `W=1`, size-three carrier, `Q=0`, and positive `R_0`, after private-reservoir descent |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; every unit of `D_b` requires a distinct named deletion, repurposing, or strict specialization saving |
| Circuit depth | Unrestricted; aligned formula depth, escape depth, and incomparable reconvergence depth unbounded |
| Fan-in | AND/OR two; NOT one; distinguished carriers excluded from payment; all reservoir exits, raw/shared inputs, bridges, fanouts, and pruning survivors audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean signal equality, formula cost, physical DAG closure, and satisfying cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical residual comparable, no-aligned-formula, raw/shared, or incomparable boundary |
| Regime | Exact worst-case deficit-payment gate; not a SAT lower bound or terminal result |
