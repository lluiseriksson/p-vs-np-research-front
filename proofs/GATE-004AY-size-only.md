# GATE-004AY-SIZE-ONLY — infer selector penetration from parent size

**Label: NO-GO**

LEMMA-151 gives two circuits for the same implication function with exactly
the same size `K+3m`. In the aggregated-tail architecture,
`D_a<=K+1`; in the interleaved architecture, `D_a>=m` and `Q>=4m`.

Therefore circuit size, including the value of the displayed deficit, does
not determine selector penetration even before minimization. Associative
placement of the same conjunction gates moves a linear number of gates into
or out of the selector-dependent region without changing size.

This no-go does not refute the existential GATE-004AY. In the zero-deficit
case, the high-penetration architecture is minimum and closes the gate. For
positive deficit, however, size data alone do not say whether any minimum
architecture retains the interleaved classes. A size-preserving normal-form
selection or a quantitative stability theorem for the `Delta` savings is
required.

## Model card

| Field | Value |
|---|---|
| Computational model | Two explicit unrestricted circuits for the same base–implication conjunction |
| Uniform/non-uniform | Fully non-uniform base circuit; uniform aggregate/interleaved comparison |
| Circuit size | Equal exact displayed size `K+3m`; selector penetration ranges from at most `K+1` to at least `m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean associativity and semantic row dependence only |
| Asymptotic quantifiers | Every `m>=1` and every base with two distinct nonconstant row residuals |
| Regime | Structural no-go for size-only selector accounting; GATE-004AY/AX/AW/AV/AU/AG/AE remain open for positive deficit |
