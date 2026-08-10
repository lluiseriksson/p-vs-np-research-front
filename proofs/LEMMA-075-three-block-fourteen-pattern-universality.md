# LEMMA-075 — a finite three-block alphabet is universal through width four

**Label: PROVED**

Let `J` be the following fixed set of 92 identifiers:

- every integer from 1 through 68;
- `69,80,98,102,130,260,324,529,1013`;
- `1028,1042,1044,1058,1060,1092,1156,1284`;
- `4130,4162,4164,4228,16450,16452,16516`.

Every block `01 T_j` or `10 F_j` for `j in J` has length at most 68. For every
four distinct interior coordinates, aligned placements of at most three
nonoverlapping blocks realize each zero mask from 1 through 14.

## Finite reduction and certificate

Translate the first coordinate by a multiple of four to `68+r`, `0<=r<4`.
For each consecutive gap at least 68, delete a multiple of four until the gap
lies in `{68,69,70,71}`. No length-at-most-68 interval can meet coordinates on
both sides of such a gap, and translating the complete right component by a
multiple of four preserves block contents, alignment, order, and
nonoverlap. Gaps below 68 remain unchanged. Thus it suffices to check

`4 * 71^3 = 1,431,644`

representative types. A length-360 representative leaves at least 68
coordinates at both boundaries.

`verification/quartet_type_audit_fast.py` exhaustively checks all four residue
partitions and returns zero failures. It represents placements by exact
position bitsets and keeps the earliest-ending witness for each accumulated
zero mask after one, two, and three blocks. Earlier ending dominates every
later continuation, so this compression is equivalent to the original
interval DP. It reproduces the Cycle-069 failure counts `18,33,9,11` exactly
and agrees with the original DP on direct comparison cases.

## Hitting-set consequence

Include the all-one option and the long option `A_rho`. The all-one option
supplies zero mask 0. On every quartet avoiding its six one positions,
`A_rho` supplies mask 15. Hence all 16 bit patterns occur on every interior
quartet avoiding those six positions.

Any non-tautological common signed clause of width at most four must therefore
meet one of the first 68 coordinates, the last 68 coordinates, or the six one
positions of `A_rho`; otherwise, at every sufficiently large slot length,
extend its support to a clean interior quartet and choose the option carrying
its falsifying pattern. This is a hitting set of size at most 142.
Consequently every disjoint family of non-tautological common signed clauses
of width at most four has at most 142 members per slot and at most `142s`
members in an independent `s`-slot product. Cross-slot clauses obey the same
bound because the product chooses each slot option independently.

This proves GATE-004AD only as a witness-family theorem. It proves no circuit
loss, lower bound, or terminal separation.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block SAT-gamma neutral contexts, finite pattern certificate, signed clauses through width four, hitting sets, and slot products |
| Uniform/non-uniform | Uniform fixed 92-identifier alphabet, placements, reduction, and parameters; later circuits fully non-uniform |
| Circuit size | No lower bound; disjoint common signed width-at-most-four packing at most `142s` |
| Circuit depth | Fixed blocks bounded; `A_rho` may have linear NOT depth; later circuits unrestricted |
| Fan-in | Encoded and later AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation only |
| Asymptotic quantifiers | Every sufficiently large compatible slot, every interior type, every disjoint common width-at-most-four family, and every `s>=1` |
| Regime | Exact worst-case witness-family theorem; not a circuit lower bound, average-case claim, promise claim, or terminal result |
