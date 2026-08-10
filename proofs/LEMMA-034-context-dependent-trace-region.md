# LEMMA-034 — adjacent SAT rows force a large context-dependent trace region

**Label: PROVED**

## Statement

Fix `L>=3`, one polarity `b`, and the ENC-014 affine context embedding

`s -> Q_{j(s),b}`

for `s in {0,1}^{L-2}`. Let `C` be any unrestricted circuit computing
`SAT-gamma` at a length large enough to contain the padded ENC-009 assignment
witnesses for all `R=2^(L-2)` target identifiers.

Substitute the affine prefix coordinates of `Q_{j(s),b}` into `C`, leaving
`s` and the suffix bits as inputs. In the resulting trace circuit, at least
`R` parent binary-gate labels lie in the output top region and have semantic
gate traces that depend on the context `s`.

This conclusion holds separately for `b=0` and `b=1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted SAT-gamma circuits after an explicit affine substitution of the prefix inputs by constants and context literals |
| Uniform/non-uniform | Every individual non-uniform parent circuit; uniform affine substitution |
| Circuit size | At least `R=2^(L-2)` context-dependent parent binary-gate labels in each fixed-polarity trace top region |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; affine substitution needs at most `L-2` shared unary NOTs and no added binary gates |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix parametrization over `F_2`; traced computation is Boolean |
| Asymptotic quantifiers | Every `L>=3`, both fixed polarities, every sufficiently large compatible total input length, and every parent circuit |
| Regime | Worst-case exact total-language computation; internal structural count, not quotient loss |

## Proof

ENC-014 maps each prefix coordinate to a constant, a context input `s_i`, or
its complement. Substitute these into the parent circuit. Shared complements
require at most `L-2` unary NOT gates; no binary gate is added. Every binary
gate in the trace circuit is therefore a labeled copy of a parent binary gate.

For each assignment vector `a in {0,1}^R`, ENC-009 and ENC-010 provide a
common-length suffix witness `y_a` fixing the target identifiers. Pointwise
conditioning from ENC-013 gives

`SAT-gamma(Q_{j(s),b} y_a)=1 iff b=a_{j(s)}`.

As `a` ranges over all assignments, the output column vectors over all
contexts `s` are all `2^R` possible bit vectors (complemented when `b=0`).
Thus the trace function satisfies LEMMA-021 with the context block as its
prefix and the `y_a` as suffix columns.

LEMMA-021 supplies at least `R` context-dependent binary gates in the trace
top region. Since the affine substitution added no binary gates, all of them
come from distinct parent binary-gate labels. QED.

## Scope

The lemma separates the forced large region from the four-gate common-edge
shell of LEMMA-033. It does not prove that fixing a context makes those gates
constant, dead, or shared. That remaining average elimination statement is
GATE-004O.
