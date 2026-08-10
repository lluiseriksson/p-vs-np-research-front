# LEMMA-067 — one bounded block plus one exceptional option retains linear signed triples

**Label: PROVED**

## Statement

Let a slot have length `N`. Suppose its option family consists of:

1. any number of strings whose zero coordinates are each confined to one
   contiguous interval of length at most `L`; and
2. at most one additional arbitrary exceptional string.

Put `D=floor(N/3)` and assume `D>=L`. Then the slot contains `D` pairwise
variable-disjoint common signed clauses of width three.

Specifically, for each `0<=i<D`, use the triple

`(i,i+D,i+2D)`.

At least three signed clauses on that triple are common to every option.

## Proof

The three coordinates in a displayed triple are pairwise separated by at
least `D`. A contiguous interval containing zeros of a bounded option has
length at most `L<=D`, so it contains at most one triple coordinate. Every
bounded option therefore realizes on the triple a pattern with at most one
zero.

There are four three-bit patterns with at least two zeros:

`000,001,010,100`.

None occurs on a bounded option. The one exceptional string realizes only
one pattern on the triple, so at least three of these four patterns remain
absent from the complete option family. For any absent pattern, take the
unique signed clause falsified by that pattern. It is one on every option.

The triples are disjoint because each occupies the same offset in the three
consecutive length-`D` regions. Selecting one common clause per triple gives
`D` disjoint clauses. QED.

## GATE-004AA application

Fix any proposed alphabet bound `L_0` and put `L=max(L_0,16)`. Every ENC-020
option and every single translated member of `N_{L_0}` has all zeros inside
one block of length at most `L`; all gaps are one. The tunable `A_rho` is the
sole exceptional option. For every sufficiently large `rho`, the slot length
`N=4rho` has `floor(N/3)>=L`, so the theorem gives

`floor(4rho/3)`

disjoint common signed triples per slot. This diverges with `rho`, refuting
the constant-per-slot conclusion of GATE-004AA for every fixed alphabet.

## Model card

| Field | Value |
|---|---|
| Computational model | Binary option families, contiguous zero supports, one arbitrary exceptional string, signed width-three clauses, and set packing |
| Uniform/non-uniform | Uniform distant-triple construction; arbitrary finite bounded-block alphabet and arbitrary exceptional option |
| Circuit size | No circuit lower bound; common signed-triple packing at least `floor(N/3)` per slot |
| Circuit depth | Irrelevant to the incidence theorem; later circuits unrestricted |
| Fan-in | Clauses use binary OR after binarization and optional unary NOT; later circuits AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean pattern incidence only |
| Asymptotic quantifiers | Every `N,L` with `floor(N/3)>=L`; every option family of the stated form; GATE-004AA application for every fixed alphabet bound and all sufficiently large `rho` |
| Regime | Worst-case exact combinatorial obstruction; not a circuit lower bound, SAT lower bound, or terminal result |
