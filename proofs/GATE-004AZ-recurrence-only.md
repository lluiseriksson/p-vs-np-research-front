# GATE-004AZ-RECURRENCE-ONLY — derive early savings from scalar deficits

**Label: NO-GO**

LEMMA-152 proves only that `Delta_0=0`, every increment belongs to
`{0,1,2}`, and the final canonical deficit is at most `K`.

Those numerical constraints permit the sequence

`Delta_0=...=Delta_{m-1}=0`, `Delta_m=1`

whenever `K>=1`. Its last increase is `r=m`, violating
`r<=Delta_m+K` throughout the canonical regime `m>>K`.

Thus monotonicity, the two-unit increment cap, and the final `O(K)` budget do
not locate the savings. This is an arithmetic method no-go, not a circuit
counterexample: the displayed sequence has not been shown realizable as
actual circuit complexities. GATE-004AZ requires an additional structural
principle showing that a saving appearing late can be transported,
replicated, or localized in a way incompatible with the small final budget.

## Model card

| Field | Value |
|---|---|
| Computational model | Integer sequences satisfying only the proved implication-deficit recurrence |
| Uniform/non-uniform | No circuit uniformity claim; numerical abstraction of non-uniform minima |
| Circuit size | `Delta_0=0`, increments in `{0,1,2}`, endpoint at most `K`; late unit jump remains allowed |
| Circuit depth | Not represented by the scalar abstraction |
| Fan-in | Underlying circuit model remains AND/OR two and NOT one, but topology is discarded |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer recurrence only |
| Asymptotic quantifiers | Every `m>K>=1` in the abstract recurrence class |
| Regime | Quantitative no-go for recurrence-only timing; GATE-004AZ/AY/AX/AW/AV/AU/AG/AE remain open |
