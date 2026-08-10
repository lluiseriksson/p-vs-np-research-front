# LEMMA-039 — neutral off-cube duplication has no generic forcing power

**Label: PROVED**

## Statement

Let `H(r,y)` be any total Boolean function and let `u` be a fresh input. Define

`F(u,r,y)=H(r,y)`.

Then the exact unrestricted AND/OR/NOT circuit complexities satisfy

`C(F)=C(H)`.

Moreover, `F(0,r,y)=F(1,r,y)=H(r,y)`, and some minimum circuit for `F` has no
gate depending semantically on `u`. Consequently, equality between an
embedded row and one adjacent off-cube row, even together with ambient
minimum circuit size, cannot by itself force any gate disappearance,
collision, or positive parent-to-quotient loss.

## Proof

Lift a minimum circuit for `H` to the larger input set by leaving `u` unused.
This gives `C(F)<=C(H)`. Conversely, restrict `u=0` in any circuit for `F`.
The restricted circuit computes `H`; simplifying constants cannot increase
its gate count, so `C(H)<=C(F)`. Hence equality holds. The lifted minimum
circuit ignores `u` at every gate and realizes two identical adjacent rows.

This is a method obstruction only. ENC-015 proves that the full SAT halo also
contains four non-neutral relations. The lemma does not say that those mixed
relations, considered simultaneously across all contexts, lack forcing power.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total Boolean functions and globally minimum acyclic AND/OR/NOT circuits |
| Uniform/non-uniform | Fully non-uniform size identity for every finite function `H`; uniform fresh-coordinate extension |
| Circuit size | Exact equality `C(F)=C(H)`; a minimum implementation has zero `u`-dependent gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite total Boolean function `H` and every fresh input coordinate `u` |
| Regime | Worst-case exact total-function computation; generic method obstruction, not a claim about the entire SAT-gamma halo |

