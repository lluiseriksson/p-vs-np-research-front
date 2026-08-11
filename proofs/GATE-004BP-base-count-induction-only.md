# GATE-004BP-BASE-COUNT-INDUCTION-ONLY — close the primary boundary by arity

**Label: NO-GO**

## Attempt

Iterate LEMMA-170 and use essential base arity as the sole well-founded
measure until every base-only cycle source has been eliminated.

## Failure

If the source formula is the primary base input `x`, compression replaces it
by a fresh input `z` and changes

`H(x,Y)=G(x,Y)`

only by renaming `x` to `z`. Essential base arity is unchanged, the factor
graph is isomorphic at the interface, and `N+r` is unchanged. Thus the
induction makes no strict descent at exactly the remaining boundary.

This is a no-go for the arity measure alone. It is not a circuit
counterexample and does not refute GATE-004BP.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract primary-input interface compression and essential-variable counts |
| Uniform/non-uniform | Every individual base with an essential selected input; no minimum-circuit realization claim |
| Circuit size | Compression preserves every resource count at the primary boundary |
| Circuit depth | Unrestricted ambient factor circuit |
| Fan-in | Interface is a primary input; target basis remains AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean variable renaming and integer arity only |
| Asymptotic quantifiers | Every nonconstant base having an essential distinguished input |
| Regime | Structural no-go for base-arity induction alone; not a refutation of GATE-004BP or a SAT lower bound |
