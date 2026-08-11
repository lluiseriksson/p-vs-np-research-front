# GATE-004BZ-COFACTOR-ORDER-ONLY — ordered signatures force uncrossing

**Label: NO-GO**

## Attempt

Use only `n_01>=n_11` for the earliest mixed NOT and equality of the final
`01,11` output cofactors to replace the switching cone or charge a resource.

## Failure

Ordered differences can be masked locally by one binary gate. For independent
variables `u,v,w`, put

`n=NOT(v OR (u AND w))`,

`q=NOT v AND w`,

and `d=n OR q`. Then

`n|_{u=0}=NOT v`,

`n|_{u=1}=NOT v AND NOT w`,

so the signatures are distinct and pointwise ordered, while direct Boolean
algebra gives `d=NOT v` under both values of `u`. The OR gate is a first
binary cancellation and no generic local deletion follows from the order.

This gadget is not claimed minimum and is not an implication plateau. It
closes order/equality-only uncrossing. GATE-004CA must use pair minimality,
resource preservation, or the full `00,01,10,11` output table.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted AND/OR/NOT masking gadget and abstract ordered-cofactor inference |
| Uniform/non-uniform | Uniform finite local identity; no minimum-parent realization claim |
| Circuit size | Constant-size masking cone; no parent or resource lower bound |
| Circuit depth | Constant in the witness; target model unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean identities and pointwise order only |
| Asymptotic quantifiers | Every choice of independent Boolean variables in the displayed identity |
| Regime | Structural no-go for cofactor-order-only rewriting; not a plateau counterexample, SAT lower bound, or terminal result |
