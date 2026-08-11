# GATE-004CD-CYCLE-EXISTENCE-ONLY — a shared cycle does not imply resource loss

**Label: NO-GO**

## Tempting inference

Use the reconvergence cycle supplied by a shared exit as the cycle coordinate
that must disappear under a satisfying restriction.

## Failure

Under the exact plateau premise, LEMMA-174 and LEMMA-178 give the opposite
conclusion: every parent cycle coordinate survives every satisfying minor
modulo contractions. Thus cycle existence alone cannot establish the kernel
required by GATE-004CD.

An explicit double-cancellation gadget shows the local compatibility. Let
`x,y,u` be raw inputs, use `XOR` only as an abbreviation for its standard
AND/OR/NOT subcircuit, and put

`r=x XOR y`, `s=NOT r`,

`p=(NOT u AND x) OR (u AND y)`,

`d=p OR r`, `c=p AND s`, and `o=d AND NOT c`.

For both values of `u`, `d=x OR y`, `c=x AND y`, and `o=x XOR y`.
The two edges from `p` lead to distinct cancellation gates `d,c` and
reconverge at `o`. After either restriction of `u`, both branches remain
nonconstant and the cycle survives modulo the contraction of the multiplexer.

This gadget is not claimed minimum or a plateau realization. It shows why a
Boolean signature argument tied to the full four-code table is needed; local
shared-cycle topology supplies no saving.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite AND/OR/NOT double-cancellation DAG plus equal-rank plateau audit |
| Uniform/non-uniform | Uniform finite local identity; no minimum-parent realization claim |
| Circuit size | Constant-size witness; no parent size or lower-bound conclusion |
| Circuit depth | Constant witness; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `p` has two live exits |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean identities and undirected cycle space over `F_2` |
| Asymptotic quantifiers | Every assignment to `x,y,u`; plateau statement covers every satisfying restriction |
| Regime | Structural no-go for cycle-existence-only charging; not a plateau counterexample, SAT lower bound, or terminal result |
