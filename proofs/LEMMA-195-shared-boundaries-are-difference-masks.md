# LEMMA-195 — every shared `h` boundary masks the difference region

**Label: PROVED**

Assume LEMMA-193. Put `H_0=h_01`, `H_1=h_11`, and
`Delta=H_1 AND NOT H_0`. Then `H_0<=H_1` and `Delta` is nonzero. Every direct
consumer `b!=n` of `h` is binary and has an effective second-input cofactor
`R_01=R_11=R`. Exactly one form holds:

1. `b=h AND R`, with `Delta AND R=0` and `b_01=b_11=H_0 AND R`;
2. `b=h OR R`, with `Delta AND NOT R=0` and `b_01=b_11=H_0 OR R`.

## Proof

LEMMA-180 gives `H_0<=H_1`; switching makes `Delta` nonzero. Since the carrier
contains only `g,h,n`, every direct consumer of `h` other than `n` is a first
outside boundary and is binary by LEMMA-187.

Its other effective input cannot be `h` (idempotence), `n=NOT h` (constant
output), or `g`: in the AND→OR form `h=g OR q`, absorption gives
`h AND g=g` and `h OR g=h`; the other form is dual. Each makes the consumer
removable from a minimum circuit. Hence that input is outside the carrier and
has equal cofactor `R`.

For AND, `H_0 AND R=H_1 AND R` is equivalent to `Delta AND R=0`. For OR,
`H_0 OR R=H_1 OR R` is equivalent to `Delta AND NOT R=0`. The output formulas
follow. This classifies masks but does not bound their number or cost.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau with a size-three switching carrier and every direct shared exit from `h` |
| Uniform/non-uniform | Every finite non-uniform hypothetical parent in this carrier case |
| Circuit size | Parent `K+2`; boundary count unrestricted |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; `g` fanout one, `h` fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Pointwise Boolean order and exact cofactor identities |
| Asymptotic quantifiers | Every nonconstant base, hypothetical minimum size-three carrier, and direct consumer of `h` other than `n` |
| Regime | Exact boundary-mask classification; not an exit bound, plateau exclusion, SAT lower bound, or terminal result |
