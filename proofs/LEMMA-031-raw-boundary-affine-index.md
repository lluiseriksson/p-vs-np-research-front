# LEMMA-031 — affine INDEX with a raw boundary and no stable gates

**Label: PROVED**

## Statement

Let `R,p>=1`, and let `rho_{j,b} in {0,1}^p`, for
`j in {1,...,R}` and `b in {0,1}`, be `2R` distinct prefix rows. There is a
total Boolean function

`F:{0,1}^p x {0,1}^{4R}->{0,1}`

and an AND/OR/NOT circuit `C` with all of the following properties:

1. `C` has at most `2Rp+4R+p-1` gates and depth at most
   `3+ceil(log_2 p)+ceil(log_2(2R))`;
2. every gate function of `C` depends semantically on the prefix block;
3. for each row `rho_{j,b}`, the residual `F(rho_{j,b},.)` is the AND of two
   dedicated suffix inputs, so the two residuals for a fixed `j` are distinct
   active non-input functions;
4. the `2^R` suffix witnesses form an affine subspace with nonzero disjoint
   directions, and on them

   `F(rho_{j,b},y_a)=1 iff b=a_j`; and

5. the prefix-dependent top region has `4R` raw suffix-input boundary nodes,
   no prefix-independent gate boundary node, and therefore `I=0` and
   `lambda_j=0` for every `j` in LEMMA-029.

Thus neither the affine complementary-INDEX table, distinct active output
cofactors, nor LEMMA-021's polynomial suffix-boundary count can by themselves
force a positive stable-core collision term.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit total Boolean function and acyclic AND/OR/NOT circuit with a prefix/suffix partition |
| Uniform/non-uniform | Uniform explicit family; a valid non-uniform circuit at every parameter tuple |
| Circuit size | At most `2Rp+4R+p-1`; every gate is prefix-dependent |
| Circuit depth | At most `3+ceil(log_2 p)+ceil(log_2(2R))` |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine witness notation over `F_2`; computation is Boolean |
| Asymptotic quantifiers | Every finite `R,p>=1` admitting `2R` distinct `p`-bit rows |
| Regime | Worst-case exact total-function computation; method counterexample, not minimum and not SAT-gamma |

## Construction

Give identifier `j` a four-bit suffix block

`(u_{j,1},u_{j,2},v_{j,1},v_{j,2})`.

The affine base block is `0011`, and direction `d_j` is one on all four
coordinates of block `j` and zero elsewhere. The directions are nonzero with
pairwise disjoint supports. On witness `y_a`,

`u_{j,1}=u_{j,2}=a_j`

and

`v_{j,1}=v_{j,2}=NOT a_j`.

As in LEMMA-028, build the row-equality indicator `E_{j,b}` from shared NOTs
of the prefix inputs and a balanced `p`-literal AND tree. Define

`G_{j,1}=E_{j,1} AND u_{j,1} AND u_{j,2}`,

`G_{j,0}=E_{j,0} AND v_{j,1} AND v_{j,2}`,

using two binary AND gates for each term, and output the balanced OR of all
`2R` terms. Distinct row codes make exactly one equality indicator true on a
listed row. Consequently the full residuals are

`F(rho_{j,1},.)=u_{j,1} AND u_{j,2}`

and

`F(rho_{j,0},.)=v_{j,1} AND v_{j,2}`.

They are distinct nonconstant non-coordinate functions on the full suffix
cube and evaluate to `a_j` and `NOT a_j` on the affine witnesses.

## Every gate is prefix-dependent

Each shared prefix NOT and each partial equality conjunction is a nonconstant
function of the prefix. Each term gate contains a nonconstant equality
indicator; choose its suffix inputs to be one and compare a matching with a
nonmatching prefix to witness dependence.

Every partial or final OR gate combines a nonempty set of row terms. Set the
dedicated suffix pair of one included row to one and all other dedicated pairs
to zero. The OR is one on that row and zero on another prefix row, so it also
depends on the prefix. Hence no gate is prefix-independent.

All `4R` suffix inputs occur in the output cone and the backwards traversal of
LEMMA-021 stops at them. Since every internal gate is prefix-dependent, there
is no prefix-independent gate on the boundary. This proves property 5.

## Gate and depth count

The circuit uses `p` shared prefix NOTs, `2R(p-1)` equality ANDs, `4R` term
ANDs, and `2R-1` output ORs. Their sum is `2Rp+4R+p-1`. The balanced equality
and output trees give the stated depth. QED.

## Scope

The construction is not claimed minimum, and its off-row behavior is not
SAT-gamma. It does not refute GATE-004M. It proves that the next attack cannot
identify LEMMA-021's boundary signals with stable gate functions or infer
`lambda_j>0` from the selected table. Minimum SAT structure and values away
from the witness table remain indispensable.
