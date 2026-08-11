# GATE-004AW-PREFIXES-ONLY — exact OR substitution closes quotient stability

**Label: NO-GO**

LEMMA-146 transfers a minimum implication circuit to a minimum width-five
circuit and guarantees `2m` new OR-prefix quotient classes. The third OR
output `P_i` may already be represented by an inherited row cofactor equal to
`t_i`, losing as many as `m` further classes.

Independently, LEMMA-145 gives only the implication baseline `Q_J>=3m`, one
linear `m` below the desired `4m-o(m)`. Combining only the unconditional
bounds yields `Q_F>=5m`, not the `7m-o(m)` stability target. Thus exact size
substitution and guaranteed prefixes do not address either missing surplus.

This no-go neither exhibits a small canonical quotient nor refutes
GATE-004AW/AV/AU. It requires separate bounds on implication cross-row surplus
and on raw-`t_i` cofactors.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact OR substitution into minimum implication circuits and two-row semantic quotient transfer |
| Uniform/non-uniform | Uniform derived-input gadgets; fully non-uniform inherited minimum circuit |
| Circuit size | Exact `+3m` parent size, but only `+2m` unconditional quotient transfer and `3m` implication baseline |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean functional substitution and row-cofactor equality only |
| Asymptotic quantifiers | Every `m>=1`, every nonconstant base, and every minimum implication circuit under the prefix-only method |
| Regime | Quantitative no-go for prefix-only transfer; GATE-004AW/AV/AU/AG/AE remain open |
