# LEMMA-037 — a fresh conjunction has exact additive circuit cost

**Label: PROVED**

## Statement

Let `f:{0,1}^n->{0,1}` be a nonconstant Boolean function, and let `z` be a
fresh input. For unrestricted AND/OR/NOT circuit size `C(.)`,

`C(f AND z)=C(f)+1`.

Consequently, for fresh inputs `z_1,...,z_m`,

`C(f AND z_1 AND ... AND z_m)=C(f)+m`.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total Boolean functions and globally minimum acyclic AND/OR/NOT circuits |
| Uniform/non-uniform | Fully non-uniform size identity for every finite `f`; uniform iteration over fresh variables |
| Circuit size | Exact additive increase of one per fresh conjunctive input |
| Circuit depth | Unrestricted in the lower bound; upper construction may add one layer per variable |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite nonconstant `f` and every integer `m>=1` |
| Regime | Worst-case exact total-function computation |

## Proof

An optimal circuit for `f` followed by one AND gate gives
`C(f AND z)<=C(f)+1`.

For the reverse inequality, let `D` be any circuit of size `T` for `f AND z`.
The function is nonconstant and depends essentially on `z`. In the output
cone, choose a topologically earliest gate whose semantic function depends on
`z`. No earlier gate depends on `z`, so this gate directly consumes the raw
input `z`; its other input, if any, is `z` or a `z`-independent signal.

Fix `z=1`. A first dependent NOT becomes a constant. A first dependent AND
becomes its other input (or a constant), and a first dependent OR becomes a
constant. In every case this gate is removed by semantic normalization. The
restricted circuit computes `f` with at most `T-1` gates. Therefore

`C(f)<=T-1`,

so every `D` has `T>=C(f)+1`. Equality follows. Since conjunction with a fresh
variable preserves nonconstancy, iteration proves the `m`-variable identity.
QED.

## Scope

The nonconstant hypothesis is necessary: the constant-one function conjoined
with `z` is the raw input `z` and needs no gate. The lemma is an exact
minimum-circuit statement, not a restriction-model lower bound.
