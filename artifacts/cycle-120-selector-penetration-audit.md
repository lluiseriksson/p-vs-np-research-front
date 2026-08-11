# Cycle 120 selector-penetration audit

## Minimum-circuit exclusion

**Label: PROVED**

LEMMA-149 proves that no gate function in a minimum circuit can depend on an
inessential output variable.

## Exact quotient accounting

**Label: PROVED**

LEMMA-150 proves `Q<=s+D_a` and rewrites GATE-004AX exactly as

`D_a-E_row-b>=m-Delta-3K`.

Thus any canonical witness needs `m-o(m)` gates genuinely penetrated by the
row selector.

## Arbitrary-base boundary

**Label: NO-GO**

GATE-004AX-ARBITRARY-BASE gives an exact family with two identical
nonconstant residuals, `C(J)=3m`, and every minimum circuit independent of the
row selector. Its quotient is at most `3m`, so the generalized target fails by
`m`.

## Active reformulation

**Label: EXPLORATORY**

GATE-004AY is algebraically equivalent to GATE-004AX and makes the missing
canonical obligation explicit: force linear selector penetration while
charging row collapses and raw-input collisions.

## Scope

**Label: EXPLORATORY**

No canonical selector-penetration lower bound, quotient-stability theorem,
SAT lower bound, or terminal result is claimed.
