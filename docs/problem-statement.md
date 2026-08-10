# Exact problem statement

**Result label: PROVED** for the standard equivalences cited here; **no terminal
separation is claimed**.

## Encoding and machine conventions

Strings are binary. A language is a subset of `{0,1}*`. The uniform machine
model is a deterministic or nondeterministic multitape Turing machine with a
fixed finite alphabet and the usual unit-cost transition measure. Changing
among standard reasonable Turing-machine variants changes running time by at
most a polynomial and therefore does not change `P` or `NP`.

`P` is the union over constants `c >= 1` of languages decided by a deterministic
machine that halts on every length-`n` input within `n^c + c` steps.

`NP` is the union over constants `c >= 1` of languages `L` for which a
deterministic verifier `V` satisfies

`x in L` iff there exists `y`, `|y| <= |x|^c + c`, with `V(x,y)=1`,

and `V` halts within `(|x|+|y|)^c + c` steps on every pair.

`SAT` uses a fixed, polynomial-time parsable binary encoding of propositional
formulas over `AND`, `OR`, and `NOT`. Malformed encodings are rejected.

## Terminal statement T-UNIFORM — EXPLORATORY

There is no pair `(M,c)` consisting of a deterministic multitape Turing machine
and a constant `c >= 1` such that, for every binary string `x` of length `n`,
`M(x)` halts within `n^c+c` steps and accepts exactly when `x` encodes a
satisfiable formula.

### Model card T-UNIFORM

| Field | Value |
|---|---|
| Computational model | Deterministic multitape Turing machine; fixed binary SAT encoding |
| Uniform/non-uniform | Uniform |
| Circuit size | N/A; Turing-time statement |
| Circuit depth | N/A |
| Fan-in | Formula encoding uses fan-in two AND/OR and fan-in one NOT |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | For every machine `M` and constant `c`, there exists an input `x` on which correctness or the `|x|^c+c` bound fails |
| Regime | Worst-case decision, total language, no promise |

Cook-Levin gives the following **PROVED** equivalence (EQ-COOK): `SAT` is NP-complete under uniform deterministic
polynomial-time many-one reductions. Consequently:

`T-UNIFORM` iff `SAT notin P` iff `P != NP`.

## Terminal-sufficient statement T-NONUNIFORM — EXPLORATORY

For every constant `k >= 1` and every family `(C_n)` of Boolean circuits over
fan-in-two `AND/OR` and fan-in-one `NOT` with at most `n^k+k` gates, there are
infinitely many lengths `n` for which `C_n` fails to compute `SAT` correctly on
all `n`-bit strings.

### Model card T-NONUNIFORM

| Field | Value |
|---|---|
| Computational model | Acyclic Boolean circuits over `{AND, OR, NOT}` |
| Uniform/non-uniform | Non-uniform; one arbitrary circuit per input length |
| Circuit size | At most `n^k+k` gates in the negated upper-bound assumption |
| Circuit depth | Unrestricted, at most circuit size |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | Polynomial advice is equivalent to the circuit family; no additional advice |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | For every fixed `k` and family, infinitely many failure lengths; equivalently no family has polynomial size for all lengths |
| Regime | Worst-case exact decision, total language, no promise |

`T-NONUNIFORM` is `SAT notin P/poly`; it is open. The **PROVED** bridge
BR-NONUNIFORM says that every uniform polynomial-time machine has
polynomial-size circuits, so `T-NONUNIFORM` implies `T-UNIFORM`, and therefore
implies `P != NP`. The converse is not known and must never be assumed.

## Alternative success branch

A `P = NP` proof must exhibit a deterministic machine `M`, a fixed exponent
`c`, a proof of correctness on every encoded formula, a proof of total halting,
and the worst-case `n^c+c` bound. Empirical performance, average-case behavior,
randomized success, promise restrictions, or an unproved subroutine do not
qualify.
