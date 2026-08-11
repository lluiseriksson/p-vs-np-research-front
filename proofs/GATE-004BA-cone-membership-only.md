# GATE-004BA-CONE-MEMBERSHIP-ONLY — shared dependency implies small survival support

**Label: NO-GO**

LEMMA-154 forces at least `d` resources to lie in both base and matched tail
dependency cones. Directed-path membership alone does not imply that such a
resource survives after unrelated clauses are neutralized.

For an explicit semantic witness, let `q_1,...,q_m` be clause signals and
let `H` be a nonconstant base signal. The function

`g=NOT(H AND q_1 AND NOT q_2 AND ... AND NOT q_m)`

can occur at a NOT gate reached from the base and from every clause signal.
It depends essentially on all those signals. Nevertheless, setting any one
of `q_2,...,q_m` to the neutralized clause value one makes the inner
conjunction zero and `g` constant one. Thus a resource matched to clause one
can have dependency-cone membership from all blocks while requiring all of
them to avoid immediate collapse.

This witness is not asserted to occur in a minimum circuit for `J_m`, nor to
realize the resource-saving profile. It closes only the inference from path
membership to a support bound. GATE-004BA needs a minimum-circuit semantic
survival or exchange theorem showing that the `d` overlap resources can be
represented on at most `K+d` clauses, or an alternative small circuit with
the same final saving.

## Model card

| Field | Value |
|---|---|
| Computational model | Boolean gate functions and syntactic base/tail dependency cones |
| Uniform/non-uniform | Explicit non-uniform semantic witness; no minimum-circuit claim |
| Circuit size | Linear-size conjunction witness; no saving or minimum-size assertion |
| Circuit depth | Unrestricted; witness has a binary conjunction tree and one NOT |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean dependence and restriction only |
| Asymptotic quantifiers | Every `m>=2` |
| Regime | Structural no-go for cone-membership-only localization; GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |
