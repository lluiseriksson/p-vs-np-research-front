# LEMMA-025 — the labelwise score is implementation-unstable

**Label: PROVED**

## Statement

Let a circuit have a family `J` of prefix-restriction pairs such that, for
every `j`, its two output residual functions are distinct active functions
and neither they nor their complements are constants or free inputs. Append a
chain of `2r` NOT gates to the output, for any integer `r>=1`. The extended
circuit computes exactly the same function, but for every `j`:

1. all `2r` new parent labels are prefix-dependent;
2. every new label contributes two distinct active residual functions;
3. `z_j` is unchanged and `t_j` increases by `2r`; hence
   `z_j-t_j` decreases by `2r`; and
4. the cross-label collision term `kappa_j` increases by at least `4r-2`.

After full semantic quotienting, the even-length NOT chain redirects to the
original output class and adds no required residual class. Thus the same
function admits implementations with arbitrarily negative labelwise score,
even though cross-label collisions compensate in the exact LEMMA-024 identity.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted acyclic Boolean circuits; paired prefix restrictions; semantics-preserving even NOT chains |
| Uniform/non-uniform | Fully non-uniform circuit implementations and semantic quotienting |
| Circuit size | Adds `2r` redundant gates; decreases `z_j-t_j` by exactly `2r` per pair while adding no required quotient class |
| Circuit depth | Increases by `2r`; otherwise unrestricted |
| Fan-in | NOT one; parent may use fan-in-two AND/OR |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite circuit and pair family satisfying the active-distinctness hypothesis; every integer `r>=1` |
| Regime | Worst-case exact total functions; implementation-level method obstruction, not a minimum-circuit statement |

## Proof

An even number of NOT gates preserves the output function. Since the original
two residual outputs for pair `j` are distinct, applying either parity of NOT
to both preserves distinctness. The activity hypothesis ensures that both
residuals of every new label remain active before cross-label merging. Each new
label therefore has within-label multiplicity two, contributes to `t_j`, and
cannot contribute to `z_j`. This proves the first three items.

Before the extension, the dependent trace union already contains the two
original output residuals. Across the `2r` new labels, the sum of within-label
class counts increases by `4r`, while the trace union gains at most the two
complemented output functions. Hence `kappa_j` increases by at least `4r-2`.

Every even-position gate computes the same residual function as the original
output, and all odd-position gates compute its complement. Semantic quotienting
merges equal classes and redirects the final output to the original class, so
the chain supplies no necessary new class. QED.

## SAT-gamma applicability

For every sufficiently large suffix length, the two ENC-008 conditioned SAT
residuals are distinct and nonconstant: equal-length formulas fixing the
selected identifier to false or true separate the branches, while a malformed
suffix and a compatible valid formula give both output values. They are not
free coordinate projections. The all-one suffix is malformed and evaluates to
zero at every coordinate value one, whereas a padded compatible formula
evaluates to one; similarly the all-zero suffix is malformed, ruling out a
negated coordinate when compared with a compatible formula. ENC-010 supplies
the required exact lengths. Therefore the construction applies to any SAT-
gamma circuit as a nonminimum implementation stress test.

## Scope

Minimum circuits cannot contain this removable double-NOT chain. The lemma does
not refute GATE-004L, whose quantifier is over minimum SAT circuits. It proves
that output semantics, conditioned distinctness, and trace labels alone cannot
establish GATE-004L; a proof must use minimality quantitatively or retain the
helpful `kappa_j` term.
