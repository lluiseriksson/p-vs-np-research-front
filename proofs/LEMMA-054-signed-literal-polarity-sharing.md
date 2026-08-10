# LEMMA-054 — a fresh negated literal has base-dependent additive cost

**Label: PROVED**

## Statement

Let circuit size count fan-in-two `AND`/`OR` gates and fan-in-one `NOT`
gates, with raw inputs free. For distinct raw inputs `x,z`,

`C(x)=0`, `C(NOT x)=1`,

while

`C(x AND NOT z)=2=C(NOT x AND NOT z)`.

Consequently there is no constant `Delta`, determined only by the fresh
signed unit clause `NOT z`, such that

`C(H AND NOT z)=C(H)+Delta`

for every nonconstant base `H` on inputs disjoint from `z`.

## Proof

The input `x` is free, so `C(x)=0`. The function `NOT x` has the one-gate
implementation `NOT(x)` and is neither constant nor a raw input, so its size
is exactly one.

Both two-variable targets have two-gate implementations:

- `x AND NOT z` is computed by `NOT(z)` followed by `AND`;
- `NOT x AND NOT z` is computed as `NOT(x OR z)`.

Neither target has a one-gate implementation. A one-gate circuit is either a
`NOT` of one raw input, hence depends on only one variable, or an `AND`/`OR`
of the two raw inputs (allowing repetitions does not add a function). The
latter possibilities are `x AND z` and `x OR z`, neither of which is either
target. Thus both target sizes are exactly two.

Taking first `H=x` and then `H=NOT x`, the increments caused by conjoining
`NOT z` are respectively two and one. A base-independent `Delta` cannot
exist. QED.

## Consequence for the signed-clause audit

LEMMA-048's exact positive-clause identity works by charging fresh monotone
clause gates and fresh conjunction gates. A negated literal can instead share
polarity through De Morgan's law with the base output. Therefore a signed
extension theorem must retain complement/polarity information about the base;
the base size `K` and the signed clause width alone are insufficient.

This does not show that a signed common-predicate counterexample to GATE-004V
exists or does not exist.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact minimum unrestricted Boolean circuits over raw inputs |
| Uniform/non-uniform | Finite exact non-uniform circuit complexity; the two witnesses are explicit |
| Circuit size | `C(x)=0`, `C(NOT x)=1`, and both two-variable targets have exact size two; increments two and one |
| Circuit depth | At most two in the displayed implementations; lower bound covers unrestricted depth at size at most one |
| Fan-in | `AND`/`OR` two; `NOT` one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Exact finite statement for every pair of distinct raw inputs `x,z`; universal impossibility over all nonconstant disjoint bases follows from two bases |
| Regime | Worst-case exact total-function complexity; method audit only, not a SAT lower bound |
