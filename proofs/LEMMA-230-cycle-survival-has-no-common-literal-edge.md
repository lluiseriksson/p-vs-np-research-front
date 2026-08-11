# LEMMA-230 — cycle survival need not leave a common literal edge

**Label: PROVED**

There is a connected parent multigraph with cycle rank one and three
rank-preserving two-contraction minors such that the parent cycle maps to a
nonzero cycle in every minor, but no parent edge remains uncontracted in all
three minors.

## Construction and proof

Let the parent be the six-cycle with edge set

```text
E={e_0,e_1,e_2,e_3,e_4,e_5}.
```

Define three labeled minors by contracting respectively

```text
K_00={e_0,e_1},  K_01={e_2,e_3},  K_11={e_4,e_5}.
```

The parent has `V=6,E=6`, hence connected cycle rank `E-V+1=1`. Each minor
contracts two non-loop cycle edges, reducing both `E` and `V` by two and
retaining rank one. The six-cycle coordinate maps to the resulting four-edge
cycle and is nonzero in each minor.

However,

```text
(E minus K_00) intersection (E minus K_01) intersection (E minus K_11)
= E minus (K_00 union K_01 union K_11)
= empty.
```

Thus cycle-space survival and even exact knowledge of all three contraction
maps do not imply a literal parent edge left uncontracted everywhere. The
lemma is a graph witness; it does not claim that every abstract contraction
triple is realized by the active Boolean endpoint.

## Model card

| Field | Value |
|---|---|
| Computational model | Connected undirected parent multigraph and three labeled contraction minors |
| Uniform/non-uniform | One finite non-uniform graph witness; general set identity for the displayed partition |
| Circuit size | Six parent cycle edges/vertices; each minor contracts two edges and vertices |
| Circuit depth | Not applicable to the graph witness; circuit application has unrestricted depth |
| Fan-in | Graph theorem; circuit target retains AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Cycle rank and contraction maps over `F_2` |
| Asymptotic quantifiers | All three displayed minors and every edge of the six-cycle |
| Regime | Exact graph no-common-edge witness; not Boolean endpoint realizability, SAT lower bound, or terminal result |
