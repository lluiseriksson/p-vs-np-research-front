# LEMMA-028 — a small total extension of every affine INDEX table

**Label: PROVED**

## Statement

Let `R,p,m>=1`. Let

`rho_{j,b} in {0,1}^p` for `j in {1,...,R}` and `b in {0,1}`

be `2R` distinct prefix rows. Let `y_0,d_1,...,d_R in {0,1}^m`, where every
`d_j` is nonzero and the supports of the `d_j` are pairwise disjoint. Put

`y_a=y_0 XOR XOR_{j:a_j=1} d_j` for `a in {0,1}^R`.

There is a total Boolean function `F:{0,1}^{p+m}->{0,1}` computed by an
AND/OR/NOT circuit with at most

`2Rp+3R+p-1`

gates such that, for every `j,b,a`,

`F(rho_{j,b},y_a)=1 iff b=a_j`.

The circuit has fan-in two AND/OR gates, fan-in one NOT gates, and depth at
most

`2+ceil(log_2 p)+ceil(log_2(2R))`.

For the conditioned `SAT-gamma` rows in ENC-008 and the affine witnesses in
ENC-012, `p=O(log R)`. Hence the complete affine complementary-INDEX table is
compatible with a total unrestricted circuit of size `O(R log R)`. When
`R=Theta(n^c)` for fixed `0<c<1`, this is `o(n)`.

## Model card

| Field | Value |
|---|---|
| Computational model | Total Boolean functions and acyclic AND/OR/NOT circuits extending prescribed values on distinct prefix rows and an affine suffix subspace |
| Uniform/non-uniform | Uniform explicit construction; the resulting circuit is a valid non-uniform circuit at each finite parameter tuple |
| Circuit size | At most `2Rp+3R+p-1`; `O(R log R)` for the ENC-008 row width |
| Circuit depth | At most `2+ceil(log_2 p)+ceil(log_2(2R))` using balanced trees |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine witness notation over `F_2`; the computing circuit is Boolean, not algebraic |
| Asymptotic quantifiers | Every finite `R,p,m>=1`, every `2R` distinct rows, and every base with nonzero pairwise-disjoint affine directions; asymptotic corollary for fixed `0<c<1` |
| Regime | Worst-case exact total-function computation; prescribed behavior only on the displayed row/subspace product, zero on unlisted prefix rows in the constructed extension |

## Construction

For each `j`, choose a pivot coordinate `q_j` in `supp(d_j)`. Disjointness
implies that on every affine witness

`a_j = y_a[q_j] XOR y_0[q_j]`.

Thus `a_j` and its complement are available from the suffix input bit
`y[q_j]` and one shared NOT gate.

Create one NOT of each of the `p` prefix inputs. For every row `rho_{j,b}`,
let `E_{j,b}` be the AND of the `p` matching input literals. A balanced tree
uses `p-1` AND gates and makes `E_{j,b}=1` exactly on that prefix row. Define

`L_{j,1}=a_j` and `L_{j,0}=NOT a_j`,

using the pivot bit and its shared complement with the orientation determined
by `y_0[q_j]`. Finally compute

`F(x,y)=OR_{j=1}^R OR_{b in {0,1}} (E_{j,b}(x) AND L_{j,b}(y))`.

On `x=rho_{j,b}`, exactly one equality indicator is one because all rows are
distinct. On `y=y_a`, its associated literal is one exactly when `b=a_j`.
On an unlisted prefix row every equality indicator is zero, so the construction
is a total extension and returns zero there.

## Gate and depth audit

The construction uses:

- `p` shared prefix NOT gates;
- `R` shared suffix-pivot NOT gates;
- `2R(p-1)` equality-tree AND gates;
- `2R` term AND gates; and
- `2R-1` final OR-tree gates.

Their sum is `2Rp+3R+p-1`. Input negations add depth at most one, an equality
tree adds `ceil(log_2 p)`, a term adds one, and the final tree adds
`ceil(log_2(2R))`, proving the stated depth bound. QED.

## Consequence and scope

The exact affine geometry and complementary-INDEX values in ENC-012 do not,
by themselves, imply a superlinear unrestricted-circuit lower bound or a
positive parent-minus-quotient loss. A universal implication from only those
data would apply to the explicit small extension above and is therefore false.

This is not a small circuit for `SAT-gamma`: the extension deliberately ignores
SAT's values away from the selected witness table. It leaves GATE-004L open
only for an argument that uses off-table SAT semantics, minimum-circuit
structure tied to those semantics, or the omitted cross-label collision term.
