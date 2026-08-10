# LEMMA-022 — the boundary-function universe defeats raw pigeonholing

**Label: PROVED**

## Statement

Let `k>=1` Boolean boundary signals be treated as formal inputs. There are
exactly

`2^(2^k)`

Boolean functions of their joint value. Even after excluding the two constants
and the `k` coordinate projections, at least

`2^(2^k)-k-2`

possible active non-input semantic classes remain.

Consequently, for every fixed `c,K>0`, if `k(n)>=A n^c` for some fixed `A>0`,
then for all sufficiently large `n`,

`2 n^K < 2^(2^k(n))-k(n)-2`.

Thus two restricted copies of any polynomial-size `n^K`-gate region do not
exceed the semantic class universe. Pigeonhole counting from boundary arity
alone forces no constants, input equivalences, or collisions.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract Boolean functions of the suffix-boundary values exposed by a restricted circuit top region |
| Uniform/non-uniform | Fully non-uniform semantic class universe |
| Circuit size | Any two-copy polynomial gate count is eventually smaller than the available nontrivial function universe |
| Circuit depth | Unrestricted in the intended circuit application |
| Fan-in | AND/OR two; NOT one in the intended circuit; universe count is basis-independent |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; exact finite Boolean-function counting |
| Asymptotic quantifiers | Every `k>=1`; every fixed positive `c,K,A`; all sufficiently large `n` satisfying `k(n)>=A n^c` |
| Regime | Worst-case semantic capacity bound; method ceiling, not a circuit construction or lower bound |

## Proof

A Boolean function on a `k`-bit domain is specified by one output bit for each
of the `2^k` inputs, giving exactly `2^(2^k)` functions. Removing at most two
constants and `k` projections leaves the displayed number.

If `k(n)>=A n^c`, then `2^k(n)` grows faster than `log_2(n^K)=K log_2 n`.
Hence `2^(2^k(n))` eventually dominates `2n^K+k(n)+2`, proving the inequality.
QED.

## Scope

Actual gate residuals are constrained by their shared parent circuit and by
SAT-gamma. The lemma says only that boundary arity plus region size supplies no
collision: a successful GATE-004J proof must establish a much smaller
SAT-specific trace family or another structural relation among residuals.
