# LEMMA-036 — one-hot shattering can expand every minimum joint quotient

**Label: PROVED**

## Statement

For integers `R>=2` and `m>=3`, let the inputs be an edge bit `q`, context
bits `x_1,...,x_R`, column bits `y_1,...,y_R`, and tail bits `z_1,...,z_m`.
Define

`M(x,y)=OR_{i=1}^R (x_i AND y_i)`,

`F(q,x,y,z)=(q OR M(x,y) OR z_1) AND z_2 AND ... AND z_m`.

There is a globally minimum circuit `C_{R,m}` with exactly `2R+m` gates such
that every gate function depends semantically on the context block `x`.

For the `R` one-hot contexts `x=e_i`, use the adjacent pair `q=0,1`. Every
pair has exact semantic joint quotient size

`q_i=2m-2`,

and hence signed parent-to-quotient loss

`|C_{R,m}|-q_i=2R-m+2`.

Choosing `m>2R+2` makes every pair's loss negative; choosing `m` arbitrarily
large makes it arbitrarily negative despite the following simultaneous
properties:

1. all pairs are parallel one-bit edges;
2. the two branch residuals OR to one common suffix function;
3. the `q=0` rows realize all `2^R` output columns on explicit suffix
   witnesses; and
4. every parent gate is context-dependent.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total Boolean functions, globally minimum acyclic circuits, parallel adjacent context pairs, and full semantic joint quotients |
| Uniform/non-uniform | Explicit non-uniform family with a uniform construction for every `R,m` |
| Circuit size | Minimum parent size `2R+m`; every pair quotient `2m-2`; signed loss `2R-m+2` |
| Circuit depth | Depends on the chosen OR/AND trees; minimum lower bound allows unrestricted depth |
| Fan-in | AND/OR two; no NOT gates required |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every `R>=2,m>=3`; negative loss for every `m>2R+2` |
| Regime | Worst-case exact total-function computation; one-hot-context method obstruction, not SAT-gamma |

## Minimum circuit

Compute the `R` terms `t_i=x_i AND y_i`, combine them with `R-1` OR gates to
obtain `M`, use one OR with `q`, one OR with `z_1`, and then `m-1` AND gates
for `z_2,...,z_m`. The total is

`R+(R-1)+2+(m-1)=2R+m`.

The function depends essentially on all `1+2R+m` inputs. For `q,x_i,y_i`,
set the other selectors to zero, the relevant data bit as needed, `z_1=0`,
and `z_2=...=z_m=1`. The input `z_1` is essential when `q=M=0`; each later
`z_k` is essential when `q=1` and all other tail inputs are one. The
connected-output-cone bound therefore requires at least

`(1+2R+m)-1=2R+m`

binary gates. The displayed circuit is globally minimum.

Every term gate depends on `x`. Every partial OR contains a nonempty set of
terms and depends on a context coordinate in that set. The two following OR
gates and every tail AND remain context-dependent by setting `q=z_1=0`, all
tail factors to one, and toggling a selected `x_i` with `y_i=1`.

## Shattering and common union

At context `e_i`,

`F(0,e_i,y,z)=(y_i OR z_1) AND z_2 AND ... AND z_m=:A_i`,

`F(1,e_i,y,z)=z_2 AND ... AND z_m=:Z`.

Since `A_i` implies `Z`, their OR is the same function `Z` for every `i`.
On suffix witnesses with `z_1=0` and `z_2=...=z_m=1`, the `q=0` output is
exactly `y_i`. Varying `(y_1,...,y_R)` realizes all `2^R` column vectors over
the `R` contexts.

## Exact joint quotient

After `x=e_i`, all term and multiplexer gates normalize to constants or the
input `y_i`. Under `q=0`, the active classes are

`y_i OR z_1`,

`(y_i OR z_1) AND z_2`, ..., `A_i`,

for exactly `m` distinct active functions.

Under `q=1`, the first two ORs are constant one and the first tail AND is the
input `z_2`. The active classes are

`z_2 AND z_3`, ..., `Z`,

for exactly `m-2` distinct functions. No class from the first list equals one
from the second because the first list depends essentially on `y_i` and
`z_1`, while the second does not. Thus `q_i=m+(m-2)=2m-2`, proving the signed
loss formula. QED.

## Scope

The contexts are the one-hot vectors in an `R`-bit block. They do not exhaust
the assignments of a compressed `log_2 R`-bit context cube and do not have
ENC-014's disjoint repeated-coordinate affine embedding. GATE-004P isolates
that remaining compact-context hypothesis. The lemma does not refute SAT's
active route.
