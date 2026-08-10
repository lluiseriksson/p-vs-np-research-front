# LEMMA-027 — every conditioned SAT pair splits the output label

**Label: PROVED**

## Statement

Fix any `0<c<1` and the full ENC-008 identifier block `J_n` used by
GATE-004L. For every sufficiently large `n`, every minimum circuit `C_n` for
`SAT-gamma_n`, and every `j in J_n`, the parent output label is
prefix-dependent and its two copies under `R_{j,0},R_{j,1}` contribute two
distinct active residual functions. Consequently,

`t_j>=1`

for every `j`, and the output label alone contributes exactly `-|J_n|` to

`sum_j(z_j-t_j)`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits and the exact false/true conditioned prefix pairs |
| Uniform/non-uniform | Every individual non-uniform minimum circuit |
| Circuit size | No lower bound; mandatory one split dependent label per identifier pair |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every fixed `0<c<1`; all sufficiently large `n`; every minimum circuit; every identifier in the selected block |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Proof

Let `H_{j,b}` be the suffix function obtained from `SAT-gamma_n` by fixing the
ENC-008 prefix `R_{j,b}`. ENC-008 identifies it with satisfiability conditioned
on `x_j=b`.

The functions `H_{j,0}` and `H_{j,1}` are distinct. Use the equal-length
literal gadget `A_{j,0}` as a suffix: it is satisfiable under `x_j=0` and
inconsistent with `x_j=1`. ENC-010 pads it to the exact suffix length for all
sufficiently large `n` without mentioning `j` or changing satisfiability.

Each `H_{j,b}` is nonconstant: a padded compatible gadget gives value one,
whereas the all-one suffix is malformed and gives value zero. It is not a free
coordinate projection, because the all-one suffix has every coordinate equal
to one but the function value zero. Hence both residuals are active under the
normalization used in LEMMA-024.

Since the two residual output functions differ, the parent output function
depends on the prefix block. Its label is therefore among the `P_n` dependent
labels. Its two restricted copies contribute the two-element set
`{H_{j,0},H_{j,1}}`, so this label is counted by `t_j` for every `j`. Summing
its contribution `-1` over `J_n` proves the aggregate statement. QED.

## Scope

This is a mandatory negative charge, not a lower bound. A proof of GATE-004L
must find enough disappeared labels to pay for this output split, every other
split label, and the additional polynomial reserve.
