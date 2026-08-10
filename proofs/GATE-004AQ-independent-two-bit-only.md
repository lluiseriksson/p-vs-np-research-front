# GATE-004AQ-INDEPENDENT-TWO-BIT-ONLY — reuse the parallel-source proof

**Label: NO-GO**

The nested orientation does not factor through two independent bits
`z_1(X_1),z_2(X_2)`. Its second split value has the form
`z_2=H(z_1,X_2)` and therefore can depend on the first source variables through
`z_1`. Applying LEMMA-121 independently to `X_2` as though `z_2` ignored
`X_1` would assume a false variable partition.

Likewise, the exact unfolding budget differs: NOT gates before the first split
can have more output paths than gates introduced between the splits. The
parallel equality placing all NOTs in independent source trees does not carry
over automatically.

This is a method no-go only. It does not refute GATE-004AQ. A sequential
cofactor theorem and region-specific path accounting are required.

## Model card

| Field | Value |
|---|---|
| Computational model | Nested theta split and attempted independent two-bit factorization |
| Uniform/non-uniform | Every individual non-uniform nested theta candidate |
| Circuit size | No lower bound; parallel-source NOT allocation cannot be imported |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Sequential Boolean interfaces and directed path regions |
| Asymptotic quantifiers | Every candidate in GATE-004AQ |
| Regime | Structural no-go for independent-bit reuse; sequential interface remains open |
