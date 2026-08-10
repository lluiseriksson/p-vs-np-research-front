# LEMMA-051 — power-of-two identifiers give tunable long-zero neutral blocks

**Label: PROVED**

## Statement

For every integer `rho>=3`, put `j=2^(rho-3)` and define

`A_rho=01 T_j`, where `T_j=OR(V_j,NOT(V_j))`.

Then:

1. `A_rho` is an exact identity formula context `AND(true,hole)`;
2. `|A_rho|=4rho`;
3. its maximum zero-run length is exactly `rho`; and
4. the run of length `rho` begins at offset three.

For every four-divisible `P>=4rho`, placing `A_rho` at a four-divisible offset
and filling the remaining outer positions with ones preserves exact validity
and satisfiability for every source string.

Moreover, every consecutive window of length at most `rho-3` whose start `a`
satisfies

`3<=a<=P-4rho+3`

is all zero in some such placement.

## Proof

Elias gamma coding gives

`gamma(2^q)=0^q 1 0^q`.

With `q=rho-3`, the variable code is

`V_j=0^(q+2) 1 0^q`.

The block is `01 10 V_j 11 V_j`, so its length is

`2+2+(2q+3)+2+(2q+3)=4q+12=4rho`.

The zero at offset three immediately precedes the `q+2` leading zeros of the
first `V_j`, producing a run of length `q+3=rho`. All other runs are shorter:
the second variable begins after `11`, and each trailing run has length `q`.
The context semantics are `AND(T_j,hole)=hole`, including exact malformed-
source rejection.

For the sweep, choose the largest `r<=a` with `r=3 mod 4`, and place the block
at `s=r-3`. Then `s` is four-divisible, `0<=s<=P-4rho`, and the long run is
`[r,r+rho)`. Since `a-r<=3`, every window of length at most `rho-3` starting
at `a` lies inside that run. QED.

## Method audit

The construction defeats the particular bounded-window clauses fully inside
the swept band. It uses only one non-one block of length `4rho`. When
`P>=8rho`, LEMMA-049 applies with `b=1`, `D=4rho`, and
`m=floor(P/2)`: distant width-two clauses remain common. Long zero runs alone
therefore do not escape the independent sparse-block obstruction.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma formula contexts, power-of-two Elias gamma identifiers, raw zero-run geometry, and single-block placements |
| Uniform/non-uniform | Uniform construction in `rho`, source string, padding length, and swept window |
| Circuit size | No lower bound; block length exactly `4rho`; sparse-block application has loss at most `K-floor(P/2)` via LEMMA-049 |
| Circuit depth | The encoded tautology has constant formula-tree depth; outer one runs may add linear NOT depth; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer run-length and congruence geometry only |
| Asymptotic quantifiers | Every integer `rho>=3`, every four-divisible `P>=4rho`, every source string, and every swept window satisfying the stated bounds |
| Regime | Worst-case exact total-language syntax theorem and scoped method audit; not a circuit lower bound |
