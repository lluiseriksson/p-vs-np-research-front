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
replacing `S` by the resulting sub-DAG preserves the parent function, uses no
more gates, and strictly lowers an earlier potential or `R_0`. Consequently no
such boundary exists in an `R_0`-extremal minimum parent.

## Proof

By the same comparability argument as LEMMA-205, the meet or join prescribed
by LEMMA-204 is exactly one row-zero cofactor of `r`. LEMMA-203 gives
`r_01=r_11`, so the full replacement signal is the global cofactor
`r|_{u=sigma}` on both rows.

Specialize the occurrence of raw `u` entering `S` to `sigma` and propagate
constants. Conditions 3 and 4 imply that the resulting acyclic AND/OR/NOT
sub-DAG `S^sigma` computes `r|_{u=sigma}`, contains at most `|S|` gates, and
that every gate in `S^sigma` is globally `u`-independent.

At `b`, all four cofactors are unchanged by LEMMA-204. At every other direct
consumer of `r`, the computed function is unchanged by condition 5. Condition
2 leaves no further edge from the modified region. A topological induction
from these direct consumers therefore shows that every gate outside
`S^sigma` computes its former function. In particular, the parent output is
unchanged even though `r` had shared fanout.

If specialization removes a gate, minimum size is contradicted. Otherwise
the size is unchanged. Gates outside the replacement keep their functions,
and every replacement gate is globally `u`-independent, so the earlier
potentials `W` and `Q` cannot increase. A strict decrease in either is already
an earlier lexicographic contradiction.

If `W` and `Q` stay equal, the boundary `b` is no longer counted by `R_0`
because its replacement input has equal `00/10` cofactors. No boundary outside
the secondary consumers can change. A secondary direct consumer that is also
an `h`-boundary either was already counted or loses, rather than gains, a
counterflow input because `r|_{u=sigma}` is globally `u`-independent; all its
other inputs are unchanged. The distinguished physical gate `h` cannot lie in
`S`: it has the outgoing edge `h -> b`, whereas condition 2 permits only edges
leaving `r`. Hence no new direct `h`-boundary is created inside `S^sigma`.
Thus `R_0` strictly decreases, contradicting the refined extremal choice.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted AND/OR/NOT plateau with a consumer-masked cofactor region |
| Uniform/non-uniform | Every finite non-uniform refined endpoint and every comparable counterflow satisfying conditions 1–5 |
| Circuit size | Replacement has at most the region size; strict saving or equal-size strict lexicographic descent |
| Circuit depth | Unrestricted; specialization and replacement remain acyclic |
| Fan-in | AND/OR two; NOT one; every secondary direct consumer of the shared output is audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Pointwise Boolean order, meet/join, cofactor specialization, and DAG topological induction |
| Asymptotic quantifiers | Every nonconstant base, hypothetical refined parent, comparable counterflow, and supplied consumer-masked region |
| Regime | Exact worst-case sufficient shared-fanout exchange theorem; not existence of masking, exclusion of unsafe or incomparable cases, SAT lower bound, or terminal result |
