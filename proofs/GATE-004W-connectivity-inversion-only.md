# GATE-004W-CONNECTIVITY-INVERSION-ONLY — close implication minimality by support and NOT counts

**Label: NO-GO**

## Scope

Attempt to prove the standalone identity `C(W_m)=3m-1`, and then transfer it
to the GATE-004W base extension, using only:

1. essential-input/output-cone connectivity to count binary gates; and
2. Markov inversion complexity to count NOT gates.

## Quantitative failure

LEMMA-058 gives the complete combined certificate:

`C(W_m)>=2m-1+ceil(log_2(m+1))`.

Against the displayed `3m-1` circuit, its gap is

`m-ceil(log_2(m+1))`,

which grows linearly. The certificate is exact for `m=1,2` but cannot prove
the growing-family identity needed by GATE-004W. It also contains no additive
direct-sum statement relative to a base and no semantic quotient-survival
claim.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits, output-cone connectivity, and Markov NOT-gate inversion complexity |
| Uniform/non-uniform | Fully non-uniform circuits; uniform implication family and increasing-chain witness |
| Circuit size | Combined lower bound `2m-1+ceil(log_2(m+1))`, upper bound `3m-1`, asymptotic gap `m-ceil(log_2(m+1))` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice chain; no algebraic circuit model |
| Asymptotic quantifiers | Every `m>=1`; method becomes quantitatively incomplete for every `m>=3` and has a linear gap asymptotically |
| Regime | Quantitative method no-go only; standalone exact size for growing `m`, GATE-004W, GATE-004V, and P versus NP remain open |
