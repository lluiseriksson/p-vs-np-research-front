# GATE-004AW — implication surplus plus derived-output collision charge

**Label: EXPLORATORY**

For the canonical implication function

`J=H AND AND_i(t_i OR NOT u_i)`,

let `C_J` be a minimum circuit, put

`Delta=K+3m-|C_J|`,

let `Q_J` be its two-row diagonal quotient size, and let `b(C_J)` count the
indices `i` for which some inherited gate restricts to raw `t_i` on at least
one designated row.

## Falsifiable theorem

Prove that some minimum `C_J` satisfies both

`Q_J>=4m-(Delta+K)`

and

`b(C_J)<=Delta+K`.

A canonical family for which no minimum implication circuit satisfies both
inequalities falsifies the theorem.

## Exact bridge

LEMMA-146 substitutes the four-positive OR gadgets and produces a minimum
width-five circuit with the same deficit `Delta` and

`Q_F>=Q_J+3m-b(C_J)`.

The two target inequalities therefore give

`Q_F>=7m-2(Delta+K)`,

which is GATE-004AU and hence closes the audited width-five obstruction.

LEMMA-145 applied to the implication rows proves only `Q_J>=3m`, and the
trivial collision bound is `b<=m`. GATE-004AW therefore isolates two separate
one-`m` gaps: cross-row implication surplus and row-induced raw-input
collisions. GATE-004AW-PREFIXES-ONLY records why exact substitution alone
does not close either gap.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical implication circuits, two-row semantic quotients, and raw-input cofactor collisions |
| Uniform/non-uniform | Uniform canonical rows and implication tail; fully non-uniform minimum-circuit adversary |
| Circuit size | Parent `K+3m-Delta`; targets quotient `4m-(Delta+K)` and collision count at most `Delta+K` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean row cofactors and exact functional substitution |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance and some minimum implication circuit for each instance |
| Regime | Exact implication/collision subgate for GATE-004AU; not a SAT lower bound or terminal result |
