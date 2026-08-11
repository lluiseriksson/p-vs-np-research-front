# GATE-004CC-FANOUT-ONE-ONLY — a private edge does not pay for semantic erasure

**Label: NO-GO**

## Tempting inference

Assume `p` has no consumer except the masked edge `p→d`, and conclude that
LEMMA-182 can replace `p` within the same local gate budget.

## Quantitative obstruction

Let `x,u,t` be raw inputs and set

`p = u OR x`, `q = t AND NOT x`, and `d = p OR q`.

The sole consumer of `p` is `d`. At the satisfying codes `01,11`,
`q_01=q_11=NOT x`, while `p_01=x`, `p_11=1`, so `d_01=d_11=1` is a
one-sided OR mask. LEMMA-182's canonical signal retains the two `t=0`
cofactors of `p` and meets the two `t=1` cofactors. It is exactly

`p^dagger = x OR (u AND NOT t)`.

This function has exact AND/OR/NOT size three. The displayed expression gives
three gates. For the lower bound, all three inputs are essential, so the
connected output cone needs at least two binary gates. The function is
nonmonotone in `t`, so it also needs a NOT. Hence the one-gate region computing
`p` cannot pay for its three-gate canonical replacement.

The whole gadget is not asserted to be a minimum plateau circuit; global
rewrites may simplify it. The witness refutes only the inference from private
fanout to a budgeted realization. GATE-004CC therefore needs an actual
private-cone budget certificate or a global plateau-specific exchange.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit finite AND/OR/NOT masking DAG and exact basis-size comparison |
| Uniform/non-uniform | One uniform three-input local identity; no minimum-parent realization claim |
| Circuit size | `p` has size one; its canonical `p^dagger` has exact size three |
| Circuit depth | Constant witness; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `p` has fanout one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean basis complexity only |
| Asymptotic quantifiers | Every Boolean assignment to `x,u,t` in the displayed witness |
| Regime | Structural and quantitative no-go for fanout-one-only realization; not a plateau counterexample, SAT lower bound, or terminal result |
