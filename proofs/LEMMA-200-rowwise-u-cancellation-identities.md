# LEMMA-200 — exact rowwise identities for global `u` cancellation

**Label: PROVED**

Fix either row `t=j` at a direct binary boundary `b` of `h`. Write

`H_0=h_0j`, `H_1=h_1j`, `R_0=r_0j`, `R_1=r_1j`,

and `Delta=H_1 AND NOT H_0`. Before the earliest mixed NOT,
`H_0<=H_1`. Then `b_0j=b_1j` is equivalent to the following exact conditions.

For `b=h AND r`:

`H_0 AND (R_0 XOR R_1)=0` and `Delta AND R_1=0`.

For `b=h OR r`:

`NOT H_1 AND (R_0 XOR R_1)=0` and
`Delta AND NOT R_0=0`.

If `r` is `u`-insensitive on the row, these reduce respectively to
`Delta AND R=0` and `Delta AND NOT R=0`, recovering the aligned-mask cases.

## Proof

Partition assignments into the three possible regions allowed by
`H_0<=H_1`: `(0,0)`, `(0,1)`, and `(1,1)`.

For AND, both outputs are zero on `(0,0)`; on `(0,1)` equality is exactly
`R_1=0`; and on `(1,1)` it is exactly `R_0=R_1`. These are the two displayed
conditions. For OR, both outputs are one on `(1,1)`; on `(0,1)` equality is
exactly `R_0=1`; and on `(0,0)` it is exactly `R_0=R_1`. This gives the dual
conditions. Applying the argument independently at `j=0,1` proves global
`u` cancellation.

XOR denotes comparison of Boolean functions, not an added circuit primitive.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted AND/OR/NOT boundary under two `u` cofactors on a fixed `t` row |
| Uniform/non-uniform | Every finite non-uniform circuit, row, and direct binary boundary after the earliest-NOT monotone prefix |
| Circuit size | No bound; exact semantic equivalence |
| Circuit depth | Unrestricted |
| Fan-in | Boundary AND/OR two; ambient NOT one and fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Pointwise Boolean order and symmetric difference notation |
| Asymptotic quantifiers | Every choice of Boolean cofactor functions satisfying `H_0<=H_1` |
| Regime | Exact rowwise cancellation classification; not a cost theorem, plateau exclusion, SAT lower bound, or terminal result |
