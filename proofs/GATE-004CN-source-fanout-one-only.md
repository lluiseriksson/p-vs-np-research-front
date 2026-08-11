# GATE-004CN-SOURCE-FANOUT-ONE-ONLY — isolating `g` does not isolate `h`

**Label: NO-GO**

In the AND→OR local form, take

`g=u AND x`, `h=g OR y`, `n=NOT h`, `r=NOT x`, `b=h AND r`.

The gate `g` has fanout one, solely to `h`, but `h` has distinct consumers
`n,b`. Moreover

`b_01=y AND NOT x=b_11`,

so `b` is a nonconstant equal-cofactor boundary outside `H_{01,11}` and
survives the neutral contraction `h->y`. Thus carrier canonicity and source
fanout one do not make the two binary carrier gates a private cone.

This is a local nonminimal gadget, not the complete output table or a plateau.
It closes only the inference from `fanout(g)=1` to private fanout of `h`.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit constant-size unrestricted AND/OR/NOT local carrier with a shared equalizing boundary |
| Uniform/non-uniform | One uniform four-input gadget; no minimum-parent claim |
| Circuit size | Three carrier gates plus aligned mask and boundary gates |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `g` fanout one and `h` fanout at least two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor identities only |
| Asymptotic quantifiers | Every assignment to `u,x,y` in the displayed gadget |
| Regime | Structural no-go for source-fanout-one-only privacy; not a plateau counterexample, SAT lower bound, or terminal result |
