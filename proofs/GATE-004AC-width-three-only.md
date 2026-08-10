# GATE-004AC-WIDTH3-ONLY — width-three sparsity controls all disjoint tails

**Label: NO-GO**

LEMMA-072 constructs `floor(rho)` disjoint common signed width-four clauses
per slot in the two-block family. Hence the 78-coordinate bound through width
three cannot be extrapolated to all widths and does not alone justify
GATE-004AC rigidity. No circuit loss follows from the width-four packing;
exact tail cost and quotient survival remain unproved.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact two-block slot products and signed clause matching |
| Uniform/non-uniform | Uniform witnesses; no circuit selected |
| Circuit size | No lower bound; width-four packing linear per slot |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large `rho` |
| Regime | Width-threshold method no-go only; GATE-004AC and P versus NP remain open |
