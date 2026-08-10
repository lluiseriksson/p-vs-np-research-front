# GATE-004Z-FORMULA-BOUNDARY-ONLY — close the signed-triple tail at minimum binary count

**Label: NO-GO**

## Scope

Combine essential-input connectivity, its formula equality case, Morizumi
formula inversion complexity, and Markov circuit inversion complexity to
prove the factorized `4m-1` standalone signed-triple circuit minimum for
growing `m`, then use that as the size component of GATE-004Z.

## Quantitative failure

LEMMA-065 proves the strongest dichotomy supplied by these ingredients:

`C(W_m)>=min(4m-1,3m+ceil(log_2(m+1)))`.

It proves exact size for `m=1,2,3,4`. For every `m>=5`, one extra binary gate
escapes the formula case and Markov's general-circuit theorem requires only
logarithmically many NOT gates. The gap below `4m-1` is

`m-1-ceil(log_2(m+1))`,

which is linear asymptotically.

## Scope control

This does not exhibit a smaller circuit and does not refute exact standalone
size. Even an exact standalone theorem would not automatically prove
additivity over the canonical base or preservation of the `5m` displayed
quotient classes. GATE-004Z therefore remains open.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits, binary connectivity equality, formula and circuit inversion complexity, and disjoint factorized signed triples |
| Uniform/non-uniform | Fully non-uniform circuits; uniform signed-triple family |
| Circuit size | Exact through `m=4`; lower `3m+ceil(log_2(m+1))` versus upper `4m-1` from `m=5`, with stated gap |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice and graph connectivity only |
| Asymptotic quantifiers | Every `m>=1`; method insufficient for every `m>=5` and linearly short asymptotically |
| Regime | Quantitative method no-go only; exact growing size, base additivity, quotient survival, GATE-004Z, GATE-004X, and P versus NP remain open |
