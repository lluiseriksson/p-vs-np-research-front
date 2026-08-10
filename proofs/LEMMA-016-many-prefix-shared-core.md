# LEMMA-016 — many prefixes can retain one shared core

**Label: PROVED**

## Statement

Let `G(z)` be any nonconstant Boolean function on at least one input and let
`p,R>=1` with `2R<=2^p`. There is a
Boolean function `F(x,z)` with `p` designated prefix inputs and `R` distinct
pairs of distinct prefix assignments `(alpha_{j,0},alpha_{j,1})` such that:

1. every one of the `2R` restrictions is exactly `G`;
2. the OR of either pair is exactly `G`;
3. `S(F)=S(G)`; and
4. there is a minimum circuit for `F` whose joint semantic quotient for every
   pair has exactly `S(F)` gates.

Thus an arbitrarily large supply of equal-length paired restrictions, even
with an exact OR reconstruction, does not by itself imply any positive
parent-to-joint-quotient loss.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted acyclic Boolean circuits; distinct complete assignments to designated prefix inputs; exact semantic quotient |
| Uniform/non-uniform | Fully non-uniform circuits and prefix choices |
| Circuit size | Zero parent-to-joint gap for every candidate pair |
| Circuit depth | Unrestricted |
| Fan-in | Any fixed complete Boolean basis; intended basis has AND/OR fan-in two and NOT fan-in one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every nonconstant Boolean function `G` of positive arity and all integers `p,R>=1` satisfying `2R<=2^p` |
| Regime | Worst-case exact total Boolean functions; method-specific counterexample |

## Proof

Choose `2R` distinct strings in `{0,1}^p`, pair them arbitrarily, and set

`F(x,z)=G(z)`.

Every designated restriction is `G`, so each pair ORs to `G`. A minimum
circuit for `G`, with the unused `x` inputs merely present, computes `F`; hence
`S(F)<=S(G)`. Conversely, fixing `x` in any circuit for `F` gives a circuit
for `G` without adding gates, so `S(G)<=S(F)`. Therefore the sizes are equal.

Use a minimum `G` circuit as the minimum parent circuit for `F`. Under every
prefix assignment all its gate residuals are unchanged. Minimality in the
AND/OR/NOT basis excludes dead gates, duplicate gate functions, gates equal to
a free input, and constant gate functions: in each case redirection and the
Boolean identities for a constant AND/OR/NOT operand remove a gate. The two
restricted copies therefore quotient class-for-class to that same circuit,
with `q_j=S(G)=S(F)` for every `j`. (For a projection, all three quantities
are zero.) QED.

## Scope

SAT-gamma is not independent of its conditioned prefixes. The lemma only
blocks promotion of prefix multiplicity and OR reconstruction alone. A valid
GATE-004H proof must use a quantitatively proved SAT-specific dependence
property.
