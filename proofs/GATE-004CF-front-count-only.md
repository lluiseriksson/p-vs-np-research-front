# GATE-004CF-FRONT-COUNT-ONLY — cancellation fronts do not charge injectively

**Label: NO-GO**

## Tempting inference

Count the two distinct fronts `d,c` from LEMMA-184, add the fresh `t` branch,
and infer that at least three separate binary eliminations are required.

## Failure

LEMMA-186 constructs arbitrarily many distinct live first-cancellation gates
fed by one varying signal, while every incoming `01/11` difference is the same
Boolean function. All those fronts can therefore represent repeated fanout of
one semantic obligation rather than independent deletion demands. Neither the
number of fronts nor the number of reconvergence cycles supplies an injective
map to eliminated gates.

The construction is not a minimum plateau circuit and does not refute
GATE-004CF. It closes front-count-only lower bounds. A successful deletion-
budget proof must show that three obligations occupy regions that no one
rank-neutral contraction event can cover simultaneously.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted AND/OR/NOT fanout DAGs compared with plateau deletion accounting |
| Uniform/non-uniform | Uniform finite counterfamily for every front multiplicity; no minimum-parent claim |
| Circuit size | Arbitrarily many fronts with one-dimensional difference span; no deletion lower bound |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean difference functions over `F_2` and undirected reconvergence cycles |
| Asymptotic quantifiers | Every positive number of cancellation fronts in the explicit family |
| Regime | Structural no-go for front-count-only charging; not a plateau counterexample, SAT lower bound, or terminal result |
