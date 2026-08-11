# GATE-004BX-EXPOSED-TWO-GATE-SHELL-ONLY — attach the pair outside the base

**Label: NO-GO**

## Attempt

Model a hypothetical two-gate implication saving as a minimum base circuit
plus only two pair-sensitive attachment gates, then enumerate that shell.

## Failure

LEMMA-178 proves that every circuit for `A AND (t OR NOT u)` has at least
three pair-sensitive gates. Therefore an exposed two-gate shell cannot even
realize the required four-cofactor table.

This does not rule out a total size increment of two. Under that equality,
at least one of the three or more pair-sensitive gates survives each
satisfying restriction as a nonconstant gate of a minimum base circuit. The
saved physical gate is obtained only by interleaving pair dependence with a
gate that also performs base work. Assuming an exposed shell discards the
only remaining compression mechanism and repeats the disjoint-support
separator error of GATE-004AT-DISJOINT-SUPPORT-ONLY.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted base–implication circuits compared with an exposed output-only attachment architecture |
| Uniform/non-uniform | Every finite non-uniform base; no uniform normal-form transformation supplied |
| Circuit size | Two-gate exposed shell impossible; a total `K+2` interleaved circuit remains unexcluded |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean four-code table and undirected output-cone accounting |
| Asymptotic quantifiers | Every nonconstant base and every attempted output-only two-gate implication attachment |
| Regime | Structural no-go for exposed-shell-only reasoning; not a counterexample to GATE-004BX, SAT lower bound, or terminal result |
