# GATE-004U-SINGLE-LONG-BLOCK-CONTEXTS — long-run sweeps force loss

**Label: NO-GO**

## Falsifiable theorem attempted

Attempted claim: exact SAT-gamma agreement on common-inner-length DNF cores
under every placement of the tunable long-zero block `A_rho` forces positive
diagonal joint-quotient loss because the placements destroy the bounded-window
predicate from LEMMA-050.

This is falsifiable by an agreeing total function with a minimum circuit of
nonpositive loss.

## Counterexample

Every placement has all zeros inside its single block interval of length
`D=4rho`. When `P>=8rho`, put `m=floor(P/2)>=D` and pair coordinate `i` with
`i+m` for `0<=i<m`. One interval of length at most `m` cannot contain both
coordinates, so every clause

`z_i OR z_{i+m}`

is one on every placement.

Conjoin these clauses to the canonical DNF core base `H(r,u)` of exact size
`K`. LEMMA-046/049 give an agreeing total function of exact size `K+2m`,
quotient at least `3m`, and loss at most `K-m`. The loss is negative whenever
`m>K`, including the intended large-padding regime.

## Structural conclusion

Tunable long runs cross the LEMMA-050 premise locally but re-enter the
independent sparse-block no-go. A viable outer-context construction must use
both long runs and enough independently placed blocks that

`floor(P/(b+1))<D`

while also keeping `floor(P/(rho+1))<=K`. Coordinate density and broader DNF
syntax must still be audited separately. Full GATE-004U remains open.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits agreeing with exact SAT-gamma on common-inner-length DNF cores under all single long-block placements; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary/base minimum circuit; uniform long-block placements and distant pairs |
| Circuit size | Counterexample exact size `K+2m`; quotient at least `3m`; loss at most `K-m<0` when `m>K` |
| Circuit depth | Unrestricted base with pairwise OR gates and a sequential AND tail |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer interval geometry only |
| Asymptotic quantifiers | Every `rho>=3`, four-divisible `P>=8rho`, all compact DNF cores and long-block placements, and every regime with `floor(P/2)>K` |
| Regime | Worst-case exact counterexample to single-long-block forcing; not a lower bound and not a counterexample to full GATE-004U |
