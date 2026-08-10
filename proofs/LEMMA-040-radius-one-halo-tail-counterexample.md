# LEMMA-040 — the full radius-one halo schema admits fresh-tail expansion

**Label: PROVED**

## Statement

For every `d>=1`, put `R=2^d`. There is an explicit nonconstant total Boolean
function `D_d` with a prefix block consisting of an edge bit `q` and three
copies `A,B,C` of a `d`-bit context, and suffix inputs

`w, (y_s)_{s in {0,1}^d}, (a_s)_{s in {0,1}^d}`,

such that:

1. on every cube row `(q,s,s,s)`,

   `D_d=w AND [y_s if q=1 else NOT y_s]`;

2. independently toggling one coordinate of `A`, `B`, or `C` produces all
   six pointwise semantic forms in ENC-015, under the correspondence
   `x_j=y_s`, `x_j'=y_t`, `x_k=a_s`, where `t` is the neighboring context;
3. all designated cube and radius-one halo rows are distinct; and
4. if `K_d=C(D_d)` and

   `F_{d,m}=D_d AND z_1 AND ... AND z_m`

   for fresh suffix inputs, then `C(F_{d,m})=K_d+m`, while every cube context's
   exact semantic joint quotient has at least `2m` active classes.

Thus every context has signed loss at most `K_d-m`, which is negative for
`m>K_d`. The entire pointwise radius-one halo schema, together with all
GATE-004P on-cube hypotheses and ambient global minimality, does not force
positive quotient loss for arbitrary total functions.

## The total base function

Represent a context as a bit vector. On `(q,A,B,C)` define `D_d` by cases.

- If `A=B=C=s`, use the cube residual in item 1.
- If exactly two blocks equal `s`, the remaining block equals
  `t=s XOR e_i` for one coordinate `i`, and its position is first, middle, or
  final, use the following table.
- On every other prefix row, output zero.

| `q` | Outlying block | Value after removing the common factor `w` |
|---:|---|---|
| 1 | first | `y_s OR (y_t AND NOT a_s)` |
| 1 | middle | `y_s` |
| 1 | final | `y_t OR (y_s AND NOT a_s)` |
| 0 | first | `NOT y_s` |
| 0 | middle | `NOT y_s OR NOT y_t` |
| 0 | final | `NOT y_t` |

This finite case definition is a total Boolean function and therefore has a
finite unrestricted circuit. It is nonconstant, for example on a cube row
with `q=w=y_s=1`.

## Row uniqueness and exact halo semantics

Every halo row has exactly two equal context blocks. Their common value
uniquely recovers the base context `s`; the unequal block uniquely recovers
first/middle/final; and its unique differing coordinate recovers `i` and
`t`. Hence no two designated halo rows collide, and none is a cube row.

The table is precisely the simplified ENC-015 pointwise gadget table after
the displayed variable substitution. In particular it simultaneously has
the two neutral identities, neighboring negative conditioning, the exact
negative union

`w( NOT y_s OR NOT y_t)=(w AND NOT y_s) OR (w AND NOT y_t)`,

and the two corresponding positive mixed unions. This construction copies
the relation schema only; `D_d` is not `SAT-gamma`.

## Minimum size, shattering, and quotient expansion

LEMMA-037 applied to the nonconstant base gives

`C(F_{d,m})=C(D_d)+m=K_d+m`.

Choose a minimum circuit for `D_d` and append the fresh AND chain. On the cube
row `(q,s,s,s)`, its `k`-th appended trace is

`T_{q,k}=w AND [y_s if q=1 else NOT y_s] AND z_1 AND ... AND z_k`.

For `q in {0,1}` and `1<=k<=m`, these `2m` functions are nonconstant,
non-input, and pairwise distinct: `k` changes the essential tail set and `q`
changes the polarity of essential dependence on `y_s`. All therefore survive
as distinct active classes in the two-row semantic joint quotient.

The two cube branches OR to the context-independent function
`w AND z_1 AND ... AND z_m`. Setting `w=z_1=...=z_m=1` and varying all `y_s`
realizes every complementary output column. For either fixed `q`, every
appended trace also depends on the full-cube context selector `s`, so taking
`m>=R` supplies the GATE-004P trace-region bound. This proves every claimed
property and the negative-loss conclusion. QED.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits for an explicit total Boolean function, an affine triplicated context cube, its complete radius-one halo, and exact semantic joint quotients |
| Uniform/non-uniform | Explicit uniformly described function family; `K_d` is the non-uniform minimum size of each finite base |
| Circuit size | Exact parent size `K_d+m`; quotient at least `2m`; signed loss at most `K_d-m` |
| Circuit depth | Base unrestricted; displayed fresh tail adds `m` layers, with depth unrestricted in the minimum-size identity |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Context and halo geometry over `F_2`; computation is Boolean |
| Asymptotic quantifiers | Every `d>=1`; every `m>=1`; negative loss for `m>K_d`, and all inherited trace hypotheses for `m>=max(K_d+1,R)` |
| Regime | Worst-case exact total-function computation; method obstruction matching the ENC-015 pointwise schema, not SAT-gamma |

