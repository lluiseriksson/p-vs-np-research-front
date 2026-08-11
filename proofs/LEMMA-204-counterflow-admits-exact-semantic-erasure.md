# LEMMA-204 — row-zero counterflow admits exact semantic erasure

**Label: PROVED**

Use LEMMA-203 at a counterflow boundary `b` with other input `r`. There is an
abstract replacement signal `r^dagger`, independent of raw `u`, that preserves
all four cofactors of `b`.

Leave the aligned row unchanged:

`r^dagger_01=r^dagger_11=r_01=r_11`.

On row zero define

- if `b=h AND r`,
  `r^dagger_00=r^dagger_10=r_00 AND r_10`;
- if `b=h OR r`,
  `r^dagger_00=r^dagger_10=r_00 OR r_10`.

Replacing only the edge from `r` to `b` by `r^dagger` leaves the Boolean
function at `b`, and hence every downstream function, unchanged while erasing
the counterflow on that edge.

## Proof

Row one is immediate because the two cofactors of `r` are already equal.

For row zero write `H_0=h_00`, `H_1=h_10`, `R_0=r_00`, `R_1=r_10`, with
`H_0<=H_1`. Suppose first that `b` is AND. LEMMA-200 gives

`H_0 AND (R_0 XOR R_1)=0`

and

`(H_1 AND NOT H_0) AND R_1=0`.

On `H_0=1`, the first identity makes `R_0=R_1`, so replacing either by
`R_0 AND R_1` changes nothing. On `H_0=0,H_1=1`, the second identity makes
`R_1=0`, so the replacement is zero and both original boundary outputs are
zero. On `H_0=H_1=0`, every boundary output is zero. Thus all row-zero AND
cofactors are preserved.

For OR, LEMMA-200 gives equality of `R_0,R_1` on `H_1=0` and `R_0=1` on
`H_0=0,H_1=1`. Replacing them by `R_0 OR R_1` therefore preserves the output
on these regions, while `H_0=H_1=1` makes every output one. This proves the
dual claim.

The signal is specified semantically. The proof does not construct it at the
same circuit cost or preserve other fanouts of `r`.

## Model card

| Field | Value |
|---|---|
| Computational model | Boolean cofactor functions at a counterflow AND/OR boundary; abstract edge substitution |
| Uniform/non-uniform | Every finite non-uniform size-three `Q=0` endpoint counterflow |
| Circuit size | No size claim; all four boundary cofactors are preserved exactly |
| Circuit depth | Unrestricted ambient circuit |
| Fan-in | Boundary AND/OR two; ambient NOT one; `r^dagger` is abstract and fanout of `r` remains unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice meet/join and exact four-code cofactors |
| Asymptotic quantifiers | Every nonconstant base, hypothetical endpoint parent, counterflow boundary, and base assignment |
| Regime | Exact worst-case semantic identity; not a basis-level rewrite, plateau exclusion, SAT lower bound, or terminal result |
