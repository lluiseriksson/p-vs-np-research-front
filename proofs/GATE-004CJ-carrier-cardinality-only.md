# GATE-004CJ-CARRIER-CARDINALITY-ONLY — seven-gate counting does not contradict the budget

**Label: NO-GO**

## Tempting inference

Use `|H|<=7` and the three two-gate deletion sets to obtain a pigeonhole
contradiction at `W=1` without inspecting topology or Boolean labels.

## Failure

The upper bound is combinatorially tight. On the abstract seven-element set

`H={n,a_00,b_00,a_01,b_01,a_11,b_11}`,

take

`E_s={a_s,b_s}` for s in {00,01,11}.

The three deletion sets have size two, are pairwise disjoint, cover every
element of `H` except the common gate `n`, and satisfy every cardinality
conclusion of LEMMA-190. Smaller carriers arise by identifying or omitting
covered elements. Thus set sizes alone do not force a third deletion in any
code.

This is an abstract incidence witness, not a Boolean-circuit or plateau
realization. It proves exactly that any contradiction must use directed
carrier connectivity, the distinguished edge `h→n`, binary cancellation
boundaries, four-code cofactor equations, or cycle-rank preservation.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract finite carrier/deletion incidence systems audited against unrestricted plateau obligations |
| Uniform/non-uniform | One finite tight set-system witness; no circuit realization claim |
| Circuit size | Seven carrier labels covered by three disjoint two-element deletion sets except one common label |
| Circuit depth | Not applicable to the abstract witness; target circuit depth unrestricted |
| Fan-in | Not applicable to the set system; target retains AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set cover only |
| Asymptotic quantifiers | Every use of only the cardinality constraints in LEMMA-190 |
| Regime | Structural no-go for carrier-cardinality-only reasoning; not a plateau counterexample, SAT lower bound, or terminal result |
