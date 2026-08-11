# LEMMA-191 — the exact table admits a two-gate difference carrier

**Label: PROVED**

Let `A(Z)` be nonconstant, let `C_A` be any AND/OR/NOT circuit for it, and
choose a raw base input `x`. Add six new gates

`q=NOT x`, `c=x OR q`, `h=u AND c`, `n=NOT h`,
`i=t OR n`, and `F=A AND i`.

Then `c=1`, `h=u`, and `n=NOT u`, so

`F=A AND (t OR NOT u)`.

Its four pair cofactors are exactly

`F_00=F_01=F_11=A` and `F_10=0`.

For the satisfying pair `01/11`, the canonical noninput difference carrier is
exactly

`H_{01,11}={h,n}`,

with the distinguished edge `h -> n`. Moreover `n` is the earliest
`u`-sensitive NOT in the displayed topological order.

## Proof

The first identities follow from `x OR NOT x=1`. Under codes `01` and `11`,
every gate of `C_A`, as well as `q` and `c`, has the same cofactor. The gate
`h` has cofactors `0` and `1`, and `n` has cofactors `1` and `0`. Since `t=1`
in both codes, `i=1` in both and the output cofactor is `A` in both. Thus the
only noninput gates with unequal `01/11` cofactors are `h,n`.

The earlier NOT `q` is independent of `u`; `n` depends on `u`, establishing
the earliest-NOT claim. The construction is intentionally redundant: it adds
six gates and is not claimed minimum, extremal, or compatible with the exact
two-deletion plateau budget.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted AND/OR/NOT extension of an arbitrary nonconstant base circuit |
| Uniform/non-uniform | Uniform six-gate extension for every individual finite non-uniform base circuit and chosen raw base input |
| Circuit size | Exactly six displayed new gates beyond the supplied base circuit; no minimum-size claim |
| Circuit depth | Unrestricted base depth; constant additional depth |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor identities only |
| Asymptotic quantifiers | Every nonconstant Boolean base, every supplied base circuit, every chosen raw base input, and every assignment |
| Regime | Exact worst-case construction with a two-gate `01/11` carrier; not a minimum plateau, SAT lower bound, or terminal result |
