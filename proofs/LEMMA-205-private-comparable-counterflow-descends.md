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
and replacing `S` by the resulting sub-DAG preserves the parent function,
uses no more gates, and strictly lowers `R_0`. Consequently no such boundary
exists in an `R_0`-extremal minimum parent.

## Proof

Write `R_0=r_00` and `R_1=r_10`. For an AND boundary, LEMMA-204 uses
`R_0 AND R_1`; for an OR boundary it uses `R_0 OR R_1`. Comparability makes
this lattice operation equal to one cofactor:

- AND chooses the smaller of `R_0,R_1`;
- OR chooses the larger.

Let `sigma` be the corresponding value of raw `u`. By LEMMA-203,
`r_01=r_11`; therefore the full abstract signal `r^dagger` from LEMMA-204 is
exactly the global cofactor `r|_{u=sigma}` on both values of `t`.

Specialize the occurrence of raw `u` entering `S` to `sigma` and propagate
constants through `S`. All other boundary signals of `S` are unchanged by
condition 3. The resulting acyclic AND/OR/NOT sub-DAG `S^sigma` computes
`r|_{u=sigma}` and has at most `|S|` gates. If its output is constant,
propagating that constant through the binary boundary `b` only saves more
gates and needs no constant gate in the final circuit.

Condition 2 permits replacing `S` without changing another consumer.
LEMMA-204 says all four cofactors of `b` remain unchanged, so every downstream
gate and the parent output remain unchanged. A strict gate saving contradicts
minimum size. If the size is equal, the former boundary `b` is no longer
counted by `R_0`. Every gate of `S^sigma` is globally `u`-independent because
all its nonraw boundary signals are so, and raw `u` was fixed. Therefore the
earlier potentials `W` and `Q` cannot increase; a strict decrease in either is
already an earlier lexicographic contradiction. If both remain equal, all
gates outside the private replacement retain their functions, no new direct
consumer of `h` is introduced, and `R_0` strictly decreases. This contradicts
the refined extremal choice.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted AND/OR/NOT plateau with an explicit cofactor-private region |
| Uniform/non-uniform | Every finite non-uniform refined endpoint and every counterflow satisfying the four privacy conditions |
| Circuit size | Replacement has at most the private-region size; strict saving or equal-size strict `R_0` descent |
| Circuit depth | Unrestricted; specialization and replacement remain acyclic |
| Fan-in | AND/OR two; NOT one; the replaced region has exactly one outgoing edge |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Pointwise Boolean order, meet/join, and cofactor specialization |
| Asymptotic quantifiers | Every nonconstant base, hypothetical refined parent, comparable counterflow, and supplied private region |
| Regime | Exact worst-case sufficient exchange theorem; not existence of privacy, exclusion of incomparable/shared cases, SAT lower bound, or terminal result |
