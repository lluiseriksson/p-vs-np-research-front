# LEMMA-223 — three-code equality localizes the entire defect to code 10

**Label: PROVED**

Let `A(u,t,x)` and `B(u,t,x)` be arbitrary Boolean functions, where `x`
denotes any tuple of remaining inputs. If

```text
A_00=B_00,  A_01=B_01,  A_11=B_11,
```

then, as an exact truth-table identity over `F_2`,

```text
A xor B = u AND NOT t AND d(x),
d(x)    = A_10(x) xor B_10(x).
```

Hence the three satisfying pair codes determine every difference except the
single named defect `d` at the unsatisfying code `10`. They imply `A=B` if and
only if `d=0`.

## Proof

At `00,01,11`, the left-hand side is zero by hypothesis and the factor
`u AND NOT t` is also zero. At `10`, that factor is one and both sides equal
`A_10 xor B_10`. These four cases exhaust `(u,t)`.

The implication from three-code equality to full equality is false. For any
raw base input `x`, take

```text
A = x OR (u AND NOT t),
B = x.
```

Their three satisfying cofactors agree, but at `10` they are `1` and `x`, so
`d=NOT x` is nonzero.

LEMMA-208 established the same `10`-only direction for one earlier comparable
counterflow specialization. The present lemma is the general truth-table
interface for arbitrary old/new cut functions; it creates no physical loss or
resource by itself.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact cofactors of arbitrary Boolean functions represented by unrestricted AND/OR/NOT circuits when instantiated |
| Uniform/non-uniform | Every finite non-uniform function pair and every tuple of base inputs |
| Circuit size | Unrestricted; explicit witness uses one NOT, one AND, and one OR versus a wire |
| Circuit depth | Unrestricted; explicit witness depth three |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Truth-table difference over `F_2`; XOR is analytical notation, not an added circuit gate |
| Asymptotic quantifiers | Every base arity, every assignment, every function pair satisfying the three displayed equalities |
| Regime | Exact worst-case four-code identity; not a circuit lower bound, SAT lower bound, or terminal result |
