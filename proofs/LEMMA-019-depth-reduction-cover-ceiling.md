# LEMMA-019 — OR-of-CNF component counting has a linear ceiling

**Label: PROVED**

## Statement

For a nonzero Boolean function `f:{0,1}^n->{0,1}`, let `T_w(f)` be the minimum
number of width-at-most-`w` CNFs whose OR is exactly `f`, where `w>=1`. Then

`1<=T_w(f)<=|f^(-1)(1)|<=2^n`.

Consequently, combine any structural theorem of the form

“every size-`s` circuit has `T_w(f)<=2^(s/c)`”

with an arbitrary lower bound on `T_w(f)`. The resulting circuit-size lower
bound `s>=c log_2 T_w(f)` can never exceed `c n`. In particular, using GKW20's
`w=16,c=3.9` reduction and only the number of CNF components can never prove a
superlinear unrestricted circuit lower bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact OR covers by bounded-width CNFs; application to unrestricted acyclic Boolean circuits through the GKW20 structural theorem |
| Uniform/non-uniform | Fully non-uniform representations and circuit lower bounds |
| Circuit size | Component-count method yields at most `c n`; `3.9n` for the cited reduction |
| Circuit depth | Parent circuits unrestricted; reduced representation depth three in OR-of-CNF form |
| Fan-in | Parent basis as in GKW20; CNF clause width at most `w` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every `n>=1`, every nonzero `n`-bit Boolean function, every `w>=1`, and every positive reduction constant `c` |
| Regime | Worst-case exact total Boolean functions; representation-count method ceiling |

## Proof

For every satisfying assignment `a`, form the conjunction of the `n` unit
clauses that accepts exactly `a`. This is a width-one CNF. ORing these CNFs over
all `a in f^(-1)(1)` computes exactly `f`, proving
`T_w(f)<=|f^(-1)(1)|<=2^n`. Nonzeroness gives the lower bound one.

If a size-`s` circuit implies `T_w(f)<=2^(s/c)`, then
`s>=c log_2 T_w(f)` is the strongest lower bound obtainable by comparing the
minimum component count with that upper bound. But `log_2 T_w(f)<=n`, so this
quantity is at most `cn`. Substituting `c=3.9,w=16` proves the final assertion.
QED.

## Scope

This ceiling proof concerns the number of top OR components only. A method
using clause counts, correlations, pseudorandomness, or other internal
structure requires its own theorem and is not ruled out. None is supplied for
SAT-gamma here.
