# GATE-004CS-SEMANTIC-PRIVATE-ONLY — `u`-insensitive exits can remain essential

**Label: NO-GO**

Let

`g=u AND x`, `h=g OR y`, `n=NOT h`, `r=NOT x`, `b=h AND r`.

Then `g` has fanout one to `h`, while `h` feeds both `n` and `b`. Yet

`b=((u AND x) OR y) AND NOT x = y AND NOT x`

globally. Thus `b` is nonconstant, independent of `u`, and can carry essential
base computation while using the shared physical edge from `h`.

This local nonminimal gadget is not the full output table or a plateau. It
proves that semantic uniqueness of the `u`-sensitive child does not supply the
physical private-cone certificate of LEMMA-183.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit constant-size unrestricted AND/OR/NOT local carrier gadget |
| Uniform/non-uniform | One uniform three-input witness; no minimum-parent claim |
| Circuit size | Constant-size local DAG; no lower-bound conclusion |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `g` fanout one and `h` fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Global Boolean identity only |
| Asymptotic quantifiers | Every assignment to `u,x,y` |
| Regime | Semantic-private-only no-go; not a plateau counterexample, SAT lower bound, or terminal result |
