# GATE-004BC-STATE-COUNTS-ONLY — derive pruning from the scalar NOT-state potential

**Label: NO-GO**

LEMMA-156 fixes the scalar potential along the canonical chain, but the count
does not identify persistent NOT gates.

Already for two abstract NOT labels `a,b`, the down-state sets may evolve as

`empty -> {a} -> {b} -> {a,b} -> {a,b}`.

The first and third arrows represent output-falling `u` steps and increase
cardinality by one. The second and fourth represent repairing `t` steps and
preserve cardinality. At the first repair, however, `a` changes down-to-up
while `b` changes up-to-down. This is compatible with the paired-transition
accounting in Morizumi's proof. For larger `m`, append fresh labels at later
falling steps.

Thus the exact scalar trajectory

`0,1,1,2,2,...,m,m`

does not yield a persistent clause-to-NOT matching or say which NOT becomes
constant under a neutral restriction. The construction is an abstract state
trace, not a realizable formula for `J_m`, and does not refute GATE-004BC. It
closes only a proof using the scalar values of `D` without formula wiring or
gate-function semantics.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract NOT-state sets satisfying the exact scalar potential constraints from a formula lower-bound proof |
| Uniform/non-uniform | Explicit finite abstract trace; no formula-realizability or uniformity claim |
| Circuit size | Two labels suffice for the first swap; extensible to `m` labels with the exact cardinality trajectory |
| Circuit depth | Not represented |
| Fan-in | Not represented; target formula basis remains binary AND/OR and unary NOT |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite sets and integer cardinality only |
| Asymptotic quantifiers | Every `m>=2` in the abstract trace class |
| Regime | Structural no-go for scalar-state-only pruning; GATE-004BC/BB are later proved using LEMMA-157, while GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |
