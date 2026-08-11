# GATE-004AV-SEPARATE-ROW-SIZES-ONLY — add the two row-complexity lower bounds

**Label: NO-GO**

LEMMA-145 gives `|A_e|>=C(F_e)` on each row, but the diagonal quotient is

`|A_0 union A_1|=|A_0|+|A_1|-|A_0 intersection A_1|`.

The separate lower bounds give no upper bound on the intersection. Indeed, a
size-`K+6m` circuit may compute the entire `W_m` tail first and conjoin it with
`H` only at the final gate. Its `6m-1` tail gates are row-independent and
therefore contribute the same classes to both rows. This circuit need not be
minimum when `Delta>0`; it is a witness that row-complexity inequalities alone
do not control overlap.

Thus summing the two lower bounds silently assumes the missing cross-row
collision theorem. No counterexample to GATE-004AV is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Two restricted circuits, their semantic class sets, and an explicit shared-tail parent architecture |
| Uniform/non-uniform | Every individual non-uniform circuit under the size-only method; uniform two rows |
| Circuit size | Each row needs at least `6m`, but their class intersection may contain `6m-1` shared tail functions |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set union/intersection and Boolean semantic restriction only |
| Asymptotic quantifiers | Every `m>=1` and every canonical base with two nonconstant row residuals |
| Regime | Quantitative no-go for separate-row addition; GATE-004AV/AU/AG/AE remain open |
