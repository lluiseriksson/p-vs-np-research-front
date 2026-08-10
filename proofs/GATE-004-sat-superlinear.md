# GATE-004 — Same-language superlinear circuit lower bound for SAT

**Label: EXPLORATORY**

## Falsifiable theorem

There is an explicit constant `delta>0` such that, for infinitely many input
lengths `n`, every acyclic Boolean circuit over fan-in-two `AND/OR` and
fan-in-one `NOT` that computes the exact `n`-bit `SAT-gamma` slice on all inputs has
more than `n^{1+delta}` gates.

### Model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits computing exact `SAT-gamma` language slices |
| Uniform/non-uniform | Fully non-uniform circuit adversary |
| Circuit size | More than `n^{1+delta}` for one explicit fixed `delta>0` on infinitely many lengths |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | Polynomial advice is represented by the arbitrary circuit family |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `delta>0`; infinitely many `n`; every size-bounded circuit fails on some `n`-bit input |
| Regime | Worst-case exact decision; total language; malformed encodings reject |

## Terminal relevance and limit

This theorem would be a new unrestricted lower bound for the same NP-complete
language used by the terminal statement. It is not enough to prove
`SAT notin P/poly`: a circuit family of size `n^10`, for example, is compatible
with this gate. No terminal progress is credited automatically.

## First attempted route: constant-substitution gate elimination

All current explicit unrestricted-circuit size lower bounds are linear. The
state-of-the-art cited in Li-Yang is `3.1n-o(n)` for affine dispersers, and the
Golovnev-Hirsch-Knop-Kulikov limitation theorem shows that the standard generic
gate-elimination framework—where the induction step is certified for all
functions/circuits using a constant number of substitutions—is bounded by a
constant times `n` determined by that local scheme. Recent 2026
constructive gate-elimination work still proves linear bounds and refuters.

Therefore that generic constant-substitution framework cannot establish this
superlinear SAT gate. A SAT-specific induction step applying only to SAT and its
restricted descendants is not covered by the theorem and remains an attack
surface. This is a method-specific `NO-GO`, not a no-go for GATE-004 itself.

## Active attack surface

A successful proof must introduce a nonlocal mechanism whose certified progress
per restriction grows with `n`, or a non-gate-elimination reduction that retains
unrestricted depth and fan-in-two gates. The next brick is to formulate such a
mechanism with an amortized potential inequality strong enough to sum to
`n^{1+delta}` while explicitly testing naturalness and algebrization.

That mechanism is now isolated as GATE-004B. LEMMA-002 proves that a block
restriction losing at most `A n^beta` input length while certifying
`B n^(beta+delta)` gate loss per step is sufficient. ENC-002 supplies exact
double-negation projections between `SAT-gamma` slices; the open part is the
gate-loss inequality for minimum SAT circuits.
