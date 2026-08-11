# GATE-004CM-SIZE-THREE-LOCAL-ONLY — alternation alone is consistent

**Label: NO-GO**

For independent base signals `x,y`, let

`g=u AND x`, `h=g OR y`, `n=NOT h`, `d=h OR n`.

Across codes `01/11`, the canonical carrier of this local DAG with output `d`
is exactly `{g,h,n}`; the binary gate `d` is an equal constant-one boundary.
The cofactors are

`(g_01,h_01,n_01)=(0,y,NOT y)` and
`(g_11,h_11,n_11)=(x,x OR y,NOT(x OR y))`.

Thus `n` is nonconstant under both codes and code `01` contracts exactly the
local pair `g,h`. The dual OR→AND gadget is obtained by Boolean duality.

This is only a local realization, not a full output-table circuit, a minimum
parent, or a two-gate plateau. It proves that chain shape, alternation, and
one exact local contraction pair alone do not yield a contradiction. A proof
must use all downstream fanout consumers, the equality of full output
cofactors, and the cross-code deletion maps.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit constant-size unrestricted AND/OR/NOT local carrier gadget |
| Uniform/non-uniform | One uniform three-input gadget and its Boolean dual; no minimum-parent claim |
| Circuit size | Three carrier gates plus one explicit binary equalizing boundary |
| Circuit depth | Constant local depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor identities only |
| Asymptotic quantifiers | Every assignment to `u,x,y` in the displayed gadget |
| Regime | Structural no-go for size-three-local-only reasoning; not a plateau counterexample, SAT lower bound, or terminal result |
