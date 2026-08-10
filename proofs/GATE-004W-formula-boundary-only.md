# GATE-004W-FORMULA-BOUNDARY-ONLY — close the growing direct sum at minimum binary count

**Label: NO-GO**

## Scope

Combine essential-input connectivity, the fact that equality in its binary-
gate bound forces a formula, Morizumi formula inversion complexity, and
Markov general-circuit inversion complexity to certify the displayed
`3m-1` standalone implication circuit for growing `m`.

## Quantitative failure

LEMMA-059 proves the strongest dichotomy supplied by these ingredients:

`C(W_m)>=min(3m-1,2m+ceil(log_2(m+1)))`.

It closes `m=1,2,3,4`. Starting at `m=5`, a circuit may use at least one
binary gate beyond the connectivity minimum, escape the formula conclusion,
and retain only Markov's logarithmic NOT lower bound. The resulting gap from
the displayed circuit is

`m-1-ceil(log_2(m+1))`,

which is linear asymptotically.

## Scope control

This does not exhibit a compressed circuit and does not refute the exact
standalone identity. It proves only that the formula-boundary dichotomy cannot
settle the growing regime required by GATE-004W. A surviving proof must bound
the binary/NOT tradeoff beyond the equality boundary, exploit the full
cofactor structure quantitatively, or prove quotient survival without exact
displayed minimality.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits, binary connectivity equality, formula and circuit inversion complexity |
| Uniform/non-uniform | Fully non-uniform circuits; uniform implication family |
| Circuit size | Exact through `m=4`; lower `2m+ceil(log_2(m+1))` versus upper `3m-1` from `m=5` onward, with stated gap |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice and graph connectivity only |
| Asymptotic quantifiers | Every `m>=1`; method insufficient for every `m>=5` and linearly short asymptotically |
| Regime | Quantitative method no-go only; exact growing size, GATE-004W, GATE-004V, and P versus NP remain open |
