# LEMMA-033 — parallel edge influence fits in a four-gate shell

**Label: PROVED**

## Statement

Let `M:{0,1}^d x {0,1}^m->{0,1}` be any total Boolean function and define

`F(q,s,y)=q XOR M(s,y)`.

If `M` has an `S`-gate unrestricted AND/OR/NOT circuit, then `F` has an
`S+4`-gate circuit in which at most four gates depend semantically on the edge
coordinate `q`. For every context `s`, the two adjacent cofactors are

`F(0,s,.)=M(s,.)`

and

`F(1,s,.)=NOT M(s,.)`.

In particular, `M` may be the context multiplexer whose residuals realize the
entire complementary-INDEX matrix. Output influence on every edge of a
parallel affine family still does not force more than four `q`-dependent
gates.

## Model card

| Field | Value |
|---|---|
| Computational model | Total Boolean functions and unrestricted acyclic AND/OR/NOT circuits with one edge coordinate and a context block |
| Uniform/non-uniform | Uniform shell construction around an arbitrary non-uniform core circuit |
| Circuit size | At most `S+4`; at most four gates depend on `q` |
| Circuit depth | Core unrestricted; shell adds constant depth |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite context/suffix function `M`; arbitrarily many parallel contexts |
| Regime | Worst-case exact total-function computation; method obstruction, not SAT-gamma |

## Proof

Use the four XOR-shell gates from LEMMA-032:

`a=q OR M`, `b=q AND M`, `c=NOT b`, and `o=a AND c`.

All gates of the chosen circuit for `M` are independent of `q`; only these four
new gates can depend on it. Direct evaluation gives `o=q XOR M`, and fixing
`q` gives the displayed complementary cofactors for every context. QED.

## Scope

The lemma controls only dependence on the common edge direction. If `M`
realizes many context residuals, its circuit may have a large region depending
on the context bits. LEMMA-034 proves that SAT's affine row family forces such
a context-dependent region. GATE-004O asks whether complete context
restriction removes or merges a polynomial part of it.
