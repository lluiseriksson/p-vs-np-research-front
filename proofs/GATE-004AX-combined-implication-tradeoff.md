# GATE-004AX — combined implication surplus-collision tradeoff

**Label: EXPLORATORY**

For the canonical implication function

`J=H AND AND_i(t_i OR NOT u_i)`,

let `C_J` be a minimum circuit, put

`Delta=K+3m-|C_J|`,

let `Q_J` be its two-row diagonal quotient size, and let `b(C_J)` count the
indices `i` for which some inherited gate restricts to raw `t_i` on at least
one designated row.

## Falsifiable theorem

Prove that some minimum `C_J` satisfies the single tradeoff

`Q_J-b(C_J)>=4m-2(Delta+K)`.

A compatible canonical family for which every minimum implication circuit
violates this inequality falsifies the theorem.

## Exact bridge

LEMMA-146 produces a minimum width-five circuit with

`Q_F>=Q_J+3m-b(C_J)`.

The proposed inequality therefore gives

`Q_F>=7m-2(Delta+K)`,

exactly GATE-004AU. Thus GATE-004AX is sufficient for the audited negative
diagonal-loss bridge.

GATE-004AX is strictly less demanding than proving the two inequalities in
GATE-004AW separately: every raw-`t_i` collision may be paid for by an
additional implication quotient class. LEMMA-147 and
GATE-004AW-TWO-ROWS-ONLY show why this combined accounting is necessary.
Two-row semantics alone permit `m` globally non-raw gates to look exactly like
the `m` raw inputs on both rows. The next proof attempt must therefore use
minimum-circuit exchange, additional canonical rows, or an injective charge
from each unpaid collision to surplus quotient structure.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical implication circuits, two-row semantic quotients, and raw-input cofactor collisions |
| Uniform/non-uniform | Uniform canonical rows and implication tail; fully non-uniform minimum-circuit adversary |
| Circuit size | Parent `K+3m-Delta`; target `Q_J-b>=4m-2(Delta+K)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean row cofactors, semantic equivalence classes, and exact functional substitution |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance and some minimum implication circuit for each instance |
| Regime | Worst-case exact implication/collision subgate for GATE-004AU; not a SAT lower bound or terminal result |
