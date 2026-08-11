# Cycle 121 selector-mobility audit

## Fixed-size mobility

**Label: PROVED**

LEMMA-151 constructs aggregate and interleaved implication circuits of the
same size `K+3m`. Their selector penetration differs from at most `K+1` to at
least `m`; the interleaved quotient has at least `4m` classes and `b=0`.

## Zero-deficit boundary

**Label: CONDITIONAL**

If `Delta=0`, the interleaved architecture is minimum and closes
GATE-004AY/AX. Exact additivity for the canonical base remains unproved, so no
unconditional promotion is made.

## Size-only boundary

**Label: NO-GO**

Equal parent size permits linearly different selector penetration. The
positive-deficit attack needs a normal-form selection among minimum circuits
or a stability theorem for the `Delta` savings.

## Scope

**Label: EXPLORATORY**

No positive-deficit selector balance, canonical exact additivity, SAT lower
bound, or terminal result is claimed.
