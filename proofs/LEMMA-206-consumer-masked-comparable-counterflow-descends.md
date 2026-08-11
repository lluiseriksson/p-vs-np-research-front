# LEMMA-206 — consumer-masked comparable counterflow descends

**Label: PROVED**

Use the refined extremal endpoint of GATE-004CX. Let `b` be a counterflow
boundary with other input `r`, and suppose `r_00,r_10` are pointwise
comparable. Let `sigma` be the cofactor selected by LEMMA-204: the smaller
cofactor for an AND boundary and the larger cofactor for an OR boundary.

Assume there is a **consumer-masked cofactor region** `S` such that:

1. the sub-DAG induced by `S` has unique output `r`;
2. every edge from `S` to a gate outside `S` leaves `r` and reaches either
   `b` or a gate in a finite set `C` of secondary direct consumers;
3. every incoming noninput signal from outside `S` is globally
   `u`-independent;
4. raw `u` is the only `u`-dependent source entering `S`; and
5. for every `c` in `C`, replacing every input occurrence of `r` at `c` by
   `r|_{u=sigma}` leaves the Boolean function computed at `c` unchanged.

Then specializing raw `u` inside `S` to `sigma`, propagating constants, and
replacing `S` by the resulting sub-DAG preserves the parent function and
strictly decreases circuit size. Consequently no such boundary exists in any
minimum parent.

## Proof

By the same comparability argument as LEMMA-205, the meet or join prescribed
by LEMMA-204 is exactly one row-zero cofactor of `r`. LEMMA-203 gives
`r_01=r_11`, so the full replacement signal is the global cofactor
`r|_{u=sigma}` on both rows.

Counterflow makes `r` depend essentially on raw `u`. If the selected cofactor
is nonconstant, LEMMA-209 gives an acyclic constant-free AND/OR/NOT sub-DAG
`S^sigma` computing `r|_{u=sigma}` with at most `|S|-1` gates. If it is
constant, propagation through `b` gives the strict saving from LEMMA-205.

At `b`, all four cofactors are unchanged by LEMMA-204. At every other direct
consumer of `r`, the computed function is unchanged by condition 5. Condition
2 leaves no further edge from the modified region. A topological induction
from these direct consumers therefore shows that every gate outside
`S^sigma` computes its former function. In particular, the parent output is
unchanged even though `r` had shared fanout.

The exterior uses exactly its former physical gates, while `S^sigma` uses at
least one fewer gate than `S`. Hence the parent is strictly smaller,
contradicting minimum size. No equal-size potential or transfer-path argument
is needed.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted AND/OR/NOT plateau with a consumer-masked cofactor region |
| Uniform/non-uniform | Every finite non-uniform refined endpoint and every comparable counterflow satisfying conditions 1–5 |
| Circuit size | Every nonconstant selected cofactor uses at most `|S|-1` gates; a constant cofactor also gives a strict parent saving through `b` |
| Circuit depth | Unrestricted; specialization and replacement remain acyclic |
| Fan-in | AND/OR two; NOT one; every secondary direct consumer of the shared output is audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Pointwise Boolean order, meet/join, cofactor specialization, and DAG topological induction |
| Asymptotic quantifiers | Every nonconstant base, hypothetical refined parent, comparable counterflow, and supplied consumer-masked region |
| Regime | Exact worst-case sufficient shared-fanout exchange theorem; not existence of masking, exclusion of unsafe or incomparable cases, SAT lower bound, or terminal result |
