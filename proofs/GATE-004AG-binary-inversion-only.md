# GATE-004AG-BINARY-INVERSION-ONLY — connectivity plus inversion closes the tail

**Label: NO-GO**

LEMMA-109 performs the strongest two-case audit supplied by essential-input
connectivity, equality-at-the-formula-boundary, and circuit/formula inversion
complexity. For the standalone four-positive/one-negative tail it gives

`min(6m-1,5m+ceil(log_2(m+1))) <= C(W_m) <= 6m-1`.

The bounds prove the displayed circuit exact only for `m<=4`. For `m>=5`,
the deficit is

`m-1-ceil(log_2(m+1))`,

which is linear. The asymptotic GATE-004AG family has `m=Theta(P)`, so this
method cannot establish displayed minimality. It also counts gates rather
than semantic diagonal quotient classes and therefore cannot establish the
representation-independent alternative.

This is a method no-go. It does not show a smaller circuit, refute
GATE-004AG/GATE-004AE, prove an unrestricted SAT lower bound, or resolve P
versus NP. The next attack must constrain the exchange of extra binary DAG
sharing for fewer negations away from the formula boundary, or work directly
with minimum-circuit quotients over the canonical base.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits, essential-input connectivity, formula-boundary graphs, and Markov/Morizumi inversion complexity |
| Uniform/non-uniform | Fully non-uniform finite circuits; uniform fixed-sign clause family |
| Circuit size | Lower `min(6m-1,5m+ceil(log_2(m+1)))` versus upper `6m-1`; linear asymptotic deficit |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice and graph connectivity only |
| Asymptotic quantifiers | Every `m>=1`; exact method closure for `m<=4` and explicit deficit for every `m>=5` |
| Regime | Structural no-go for the connectivity-plus-inversion method; larger gates remain open |
