# LEMMA-035 — a minimum context-dependent chain can expand under quotienting

**Label: PROVED**

## Statement

For every integer `m>=3`, define

`F_m(s,y_1,...,y_m)=(s OR y_1) AND y_2 AND ... AND y_m`.

There is a globally minimum `m`-gate AND/OR circuit for `F_m` in which every
gate function depends semantically on the context bit `s`. Nevertheless, the
full semantic joint quotient of that minimum circuit under `s=0,s=1` has
exactly `2m-3` active gate classes. Thus

`|C_m|-q_m=3-m`,

which is zero for `m=3` and negative for every `m>=4`.

Consequently, global minimum size and an arbitrarily large context-dependent
top region do not generically imply even one gate of positive joint-quotient
loss.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total Boolean functions, globally minimum acyclic circuits, one context bit, and a two-output semantic joint quotient |
| Uniform/non-uniform | Explicit non-uniform circuit family, with a uniform description for every `m>=3` |
| Circuit size | Minimum parent size exactly `m`; joint quotient size exactly `2m-3`; signed loss `3-m` |
| Circuit depth | `m` in the displayed left-associated chain; lower bound allows unrestricted depth |
| Fan-in | AND/OR two; no NOT gates used or needed |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every integer `m>=3` |
| Regime | Worst-case exact total-function computation; generic method obstruction, not SAT-gamma |

## Minimum circuit

Use the gates

`g_1=s OR y_1`,

`g_k=g_{k-1} AND y_k` for `2<=k<=m`.

This is an `m`-gate circuit for `F_m`. The function depends essentially on all
`m+1` input sources: `s` and `y_1` are witnessed by setting every later
`y_k=1`, and each later `y_k` is witnessed by setting `s=1` and all other
later inputs to one. The connected-output-cone edge bound from LEMMA-018 says
that every fan-in-two circuit depending on `m+1` sources has at least `m`
binary gates. The displayed circuit is therefore globally minimum.

Every `g_k` depends on `s`. Under `s=0` it is

`A_k=y_1 AND ... AND y_k`,

while under `s=1` it is one for `k=1`, the input `y_2` for `k=2`, and

`B_k=y_2 AND ... AND y_k`

for `k>=3`. These cofactor functions differ for every label.

## Exact quotient count

Semantic normalization removes `g_1` from both copies because its residuals
are an input and a constant. It removes the `s=1` copy of `g_2` because that
residual is the input `y_2`.

The active classes are therefore

`A_2,...,A_m`

and

`B_3,...,B_m`.

There are `m-1` functions of the first kind and `m-2` of the second. They are
all nonconstant, non-input, and pairwise distinct: their essential suffix-input
sets are respectively `{y_1,...,y_k}` and `{y_2,...,y_k}`. Hence no semantic
merge occurs and

`q_m=(m-1)+(m-2)=2m-3`.

Subtracting from the minimum parent size proves the identity. QED.

## Scope

The family has only two contexts and does not realize SAT's `2^R` assignment
columns across `R` contexts. It does not refute GATE-004O. It proves that the
size of the context-dependent region, full semantic dependence, and global
minimum size cannot establish GATE-004O without the simultaneous shattering
relations supplied by SAT.
