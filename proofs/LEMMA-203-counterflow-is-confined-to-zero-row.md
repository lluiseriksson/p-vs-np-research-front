# LEMMA-203 — every size-three counterflow is confined to `00/10`

**Label: PROVED**

At the size-three `Q=0` endpoint, let `b!=n` be a direct consumer of `h` whose
other input `r` is `u`-sensitive while `b` is globally `u`-independent. Then

`r_01=r_11` and `r_00!=r_10`.

Thus no counterflow difference is visible in a same-row comparison of two
satisfying codes. Its unique possible row is `00/10`, which contains the
unsatisfying implication code `10`.

## Proof

The canonical carrier is exactly `H_{01,11}={g,h,n}`. If `r` is a gate and
`r_01!=r_11`, then `r` belongs to this set.

It cannot be `h`, because an AND or OR with two identical inputs copies the
`01/11`-sensitive function `h`. It cannot be `n=NOT h`, because `h AND n` is
zero and `h OR n` is one; a constant internal boundary is removable from the
minimum output cone. It cannot be `g`: LEMMA-193 gives either `h=g OR q` or
`h=g AND q`, and absorption makes `b(h,g)` equal to `g` or `h`, both
`01/11`-sensitive. Hence a gate input `r` is outside the carrier and satisfies
`r_01=r_11`.

If `r` is a raw input, only raw `u` can differ between codes `01` and `11`.
For `b=h AND u`, equality would require `h_11=0`; this contradicts
`h_01<h_11` somewhere. For `b=h OR u`, equality would require `h_01=1`
everywhere and hence, by `h_01<=h_11`, would make the two cofactors equal.
Thus `r` is not raw `u`; every other raw input is aligned.

Therefore `r_01=r_11`. Since `r` is a counterflow input, at least one of its
two same-row `u` comparisons differs. The row-one comparison is equal, so
`r_00!=r_10`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau at `W=1`, size-three carrier, and `Q=0` |
| Uniform/non-uniform | Every finite non-uniform hypothetical endpoint parent and counterflow boundary |
| Circuit size | Parent `K+2`; carrier exactly three gates; no new size bound |
| Circuit depth | Unrestricted |
| Fan-in | Boundary AND/OR two; ambient NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors and absorption identities |
| Asymptotic quantifiers | Every nonconstant base, hypothetical size-three `Q=0` parent, and direct counterflow boundary |
| Regime | Exact worst-case row-localization theorem; not a circuit exchange, plateau exclusion, SAT lower bound, or terminal result |
