# GATE-004DO-SATISFYING-CUT-ONLY — three equal rows do not seal a cut

**Label: NO-GO**

Scope: certify that every candidate cut gate has equal old/new functions in
the three satisfying codes `00,01,11`, then invoke LEMMA-222 as if the cut
were equal on the unrestricted parent.

LEMMA-223 gives the exact missing quantity. At every cut gate `s`, the old/new
difference is

```text
u AND NOT t AND d_s(x).
```

The satisfying prunings say nothing about `d_s`. The constant-free witness

```text
A=x OR (u AND NOT t),   B=x
```

has `d_s=NOT x`, so it passes all three satisfying-row comparisons and still
fails the full-function premise of LEMMA-222. This is an interface no-go; it
does not refute an endpoint argument that forces `d_s=0` or charges its first
downstream cancellation physically.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired unrestricted constant-free AND/OR/NOT cut-gate functions with the exact three satisfying cofactors |
| Uniform/non-uniform | Every finite non-uniform candidate cut; one explicit constant-size witness |
| Circuit size | Unrestricted target; witness has three gates on one side and a raw wire on the other |
| Circuit depth | Unrestricted target; witness depth three |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean cofactors and analytical `F_2` difference signatures |
| Asymptotic quantifiers | Every candidate cut function pair; every assignment to the base tuple |
| Regime | Satisfying-rows-only seal no-go; not an endpoint counterexample, SAT lower bound, or terminal result |
