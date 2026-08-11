# LEMMA-205 — a private comparable counterflow gives exact `R_0` descent

**Label: PROVED**

Use the refined extremal endpoint of GATE-004CX. Let `b` be a counterflow
boundary with other input `r`, and suppose `r_00,r_10` are pointwise
comparable. Assume there is a **cofactor-private region** `S` such that:

1. the sub-DAG induced by `S` has unique output `r`;
2. its only edge to a gate outside `S` is `r -> b`;
3. every incoming noninput signal from outside `S` is globally
   `u`-independent; and
4. raw `u` is the only `u`-dependent source entering `S`.

Then specializing raw `u` inside `S` to one constant, propagating constants,
and replacing `S` by the resulting sub-DAG preserves the parent function and
strictly decreases circuit size. Consequently no such boundary exists in any
minimum parent.

## Proof

Write `R_0=r_00` and `R_1=r_10`. For an AND boundary, LEMMA-204 uses
`R_0 AND R_1`; for an OR boundary it uses `R_0 OR R_1`. Comparability makes
this lattice operation equal to one cofactor:

- AND chooses the smaller of `R_0,R_1`;
- OR chooses the larger.

Let `sigma` be the corresponding value of raw `u`. By LEMMA-203,
`r_01=r_11`; therefore the full abstract signal `r^dagger` from LEMMA-204 is
exactly the global cofactor `r|_{u=sigma}` on both values of `t`.

Counterflow means that `r` depends essentially on raw `u`. If the selected
cofactor is nonconstant, LEMMA-209 gives an acyclic constant-free AND/OR/NOT
sub-DAG `S^sigma` computing `r|_{u=sigma}` with at most `|S|-1` gates. If its
output is constant, propagating that constant through the binary boundary
`b` removes a gate and needs no constant gate in the final circuit.

Condition 2 permits replacing `S` without changing another consumer.
LEMMA-204 says all four cofactors of `b` remain unchanged, so every downstream
gate and the parent output remain unchanged. The resulting parent is strictly
smaller, contradicting minimum size. No equal-size potential argument is
needed.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted AND/OR/NOT plateau with an explicit cofactor-private region |
| Uniform/non-uniform | Every finite non-uniform refined endpoint and every counterflow satisfying the four privacy conditions |
| Circuit size | Every nonconstant selected cofactor uses at most `|S|-1` gates; a constant cofactor also gives a strict parent saving through `b` |
| Circuit depth | Unrestricted; specialization and replacement remain acyclic |
| Fan-in | AND/OR two; NOT one; the replaced region has exactly one outgoing edge |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Pointwise Boolean order, meet/join, and cofactor specialization |
| Asymptotic quantifiers | Every nonconstant base, hypothetical refined parent, comparable counterflow, and supplied private region |
| Regime | Exact worst-case sufficient exchange theorem; not existence of privacy, exclusion of incomparable/shared cases, SAT lower bound, or terminal result |
