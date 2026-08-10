# LEMMA-050 — bounded zero runs leave an exact local-clause tail

**Label: PROVED**

## Statement

Let `Z` be any family of bit strings on an outer region of length `P`, and
suppose no member contains more than `rho` consecutive zero bits. Put

`w=rho+1`, `m=floor(P/w)`.

Partition the first `wm` coordinates into `m` consecutive width-`w` windows,
and let `Q_i` be the positive OR of the bits in window `i`. Then `Q_i=1` on
every member of `Z`.

For every nonconstant base `H` of exact unrestricted circuit size `K`,

`F=H AND product_{i=1}^m Q_i`

has exact size `K+wm`. Under two restrictions giving distinct nonconstant
base residuals, its displayed minimum circuit has joint quotient size at least
`(w+1)m` and signed loss at most

`K-m=K-floor(P/(rho+1))`.

The loss is negative whenever `floor(P/(rho+1))>K`.

## Proof

A width-`rho+1` window cannot be all zero by hypothesis, so every window OR
is one throughout `Z`. The windows are disjoint. LEMMA-048 gives exact size
`K+wm`, quotient at least `(w+1)m`, and loss at most `K-m`. The fewer than
`w` unused trailing inputs are ignored; restriction and lifting preserve
exact complexity. QED.

## Dense neutral-alphabet application

Consider arbitrary concatenations of the ten ENC-022 neutral blocks

`01 T_j`, `10 F_j`, `j in {1,2,4,8,16}`,

separated by any four-divisible all-one runs. For identifiers
`1,2,4,8,16`, direct inspection gives maximum internal zero-run lengths

- `3,4,5,6,7` for `01 T_j`; and
- `2,3,4,5,6` for `10 F_j`.

Their terminal zero runs have lengths at most four, and a following block has
initial zero run at most one. Thus a block boundary has zero run at most five;
an all-one gap breaks the run. Every arbitrary-block-count context therefore
has `rho=7`.

LEMMA-050 supplies `m=floor(P/8)` disjoint common width-eight clauses, exact
parent size `K+8m`, quotient at least `9m`, and loss at most `K-m`. Dense use
of this finite block alphabet still fails whenever `floor(P/8)>K`.

## Scope

This result allows an arbitrary, even linear, number of blocks. It assumes a
bound on consecutive zero runs. Escaping it requires zero runs of length at
least approximately `P/(K+1)`, or syntax interactions outside the isolated
outer context. Long zero runs alone are not asserted sufficient for loss.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total Boolean functions, bounded raw-coordinate zero runs, disjoint positive window clauses, globally minimum unrestricted circuits, and semantic joint quotients |
| Uniform/non-uniform | Arbitrary witness family and fully non-uniform base/minimum circuit; uniform consecutive-window construction |
| Circuit size | Exact `K+(rho+1)m`; quotient at least `(rho+2)m`; signed loss at most `K-m`, where `m=floor(P/(rho+1))` |
| Circuit depth | Unrestricted; displayed OR and AND chains may be sequential |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer run-length bookkeeping only; computation is Boolean |
| Asymptotic quantifiers | Every finite `P,rho`, every string family with maximum zero run at most `rho`, every nonconstant base, and every distinct nonconstant row pair |
| Regime | Worst-case exact total-function method obstruction; not a SAT circuit lower bound |
