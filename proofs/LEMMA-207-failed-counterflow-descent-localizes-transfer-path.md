# LEMMA-207 — failed `R_0` descent localizes a transfer path

**Label: PROVED**

Let `D` be a finite circuit carrying the refined endpoint annotations and a comparable counterflow boundary
`b` whose other input is `r`. Let `S` satisfy conditions 1–4 of LEMMA-206, and
let `D^sigma` be obtained by specializing `S` to the cofactor selected by the
AND/OR operation at `b`. Assume that the selected cofactor is nonconstant,
that constant propagation is confined to `S`, and that the physical DAG
outside `S` is retained. Assume also that `D` and `D^sigma` compute the same
parent function and that specialization does not increase circuit size. The
constant-cofactor case is excluded because propagation through `b` already
saves a gate as in LEMMA-205.

For every physical gate outside `S`, compare its Boolean function in `D` and
`D^sigma`. Let `Delta` be the set of outside gates whose functions differ.
Then:

1. every gate in `Delta` is reachable from the changed signal `r` by a
   directed path whose outside vertices all lie in `Delta`;
2. because the parent output is unchanged, every maximal changed path in the
   parent output cone ends at a changed gate all of whose direct consumers
   within that cone are unchanged masking consumers; and
3. if `R_0(D^sigma) >= R_0(D)`, there is a newly counted direct `h`-boundary
   `c` whose other input `q` lies in `Delta`, changes from equal `00/10`
   cofactors in `D` to unequal `00/10` cofactors in `D^sigma`, and is reached
   from `r` by a changed path.

Thus every failure of strict `R_0` descent in this comparable specialization
has an explicit counterflow-transfer path. The theorem localizes the transfer;
it does not bound the path, factor its gates, or charge a satisfying minor.

## Minimum-size audit

LEMMA-209 sharpens the size premise: under conditions 1–4, every nonconstant
selected cofactor removes at least one gate from `S`, while a constant
selected cofactor saves through `b`. Therefore, when the parent function is
preserved, `D^sigma` is strictly smaller than `D`. No instance of this theorem
can occur inside a minimum parent. The transfer-path conclusion remains a
valid semantic diagnostic for the explicit nonminimal families in NG-150,
NG-151, and NG-152, but it is not a residual minimum-parent branch.

## Proof

Only the output signal of `S` changes at the interface: condition 2 of
LEMMA-206 says every edge leaving `S` leaves `r`, and all gates outside `S`
retain their operations and their other inputs. If an outside gate changes,
at least one of its input functions changed. Repeating this predecessor choice
backwards in the acyclic DAG must terminate at `r`; it cannot terminate at an
unchanged raw input or an unchanged outside gate. Reversing the predecessor
sequence proves item 1.

Starting from any changed outside gate, follow a changed direct consumer while
one exists. Finiteness and acyclicity make the process terminate. The parent
output is not changed by hypothesis, so the terminal changed gate is not an
output whose function differs. Within the parent output cone, each of its
direct consumers is therefore unchanged and masks the propagated difference.
This proves item 2.

At `b`, LEMMA-204 preserves the boundary function while replacing `r` by the
globally `u`-independent cofactor `r|_{u=sigma}`. Hence `b` leaves `R_0`.
The distinguished gate `h` is not in `S`, by the same outgoing-edge argument
as LEMMA-206, and specialization creates no direct `h`-boundary inside `S`.

If the total `R_0` count does not decrease, at least one boundary `c` outside
`S` that was not counted in `D` is counted in `D^sigma`. Its input from `h`
is the same physical signal in both circuits. Therefore its other input `q`
had equal row-zero cofactors before and unequal row-zero cofactors after, so
the function at `q` changed and `q` lies in `Delta`. Item 1 supplies the
changed path from `r` to `q`. This proves item 3.

## Model card

| Field | Value |
|---|---|
| Computational model | Two finite unrestricted AND/OR/NOT DAGs with the same physical exterior, related by one nonconstant comparable cofactor specialization inside a unique-output region |
| Uniform/non-uniform | Every finite non-uniform annotated circuit and every specialization satisfying the stated interface and output hypotheses |
| Circuit size | Under the stated isolation hypotheses the specialized circuit is strictly smaller by LEMMA-209; hence the theorem has no minimum-parent instance |
| Circuit depth | Unrestricted; transfer path length is finite but unbounded |
| Fan-in | AND/OR two; NOT one; all changed predecessors, consumers, and direct `h`-boundaries are audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean functions and finite DAG reachability |
| Asymptotic quantifiers | Every nonconstant base, qualifying comparable boundary, specialization, and resulting changed-gate set |
| Regime | Exact worst-case semantic localization theorem; not a cost theorem, plateau exclusion, SAT lower bound, or terminal result |
