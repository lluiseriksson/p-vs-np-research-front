# LEMMA-041 — the full expanded context cube admits fresh-tail expansion

**Label: PROVED**

## Statement

For every `d>=1`, put `R=2^d`. On prefix inputs

`q in {0,1}` and `A,B,C in {0,1}^d`

and suffix inputs `w`, `(y_s)_s`, and `(a_s)_s`, define the total function

`E_d(1,A,B,C,y,a,w)`

`=w AND ((y_A AND NOT a_B) OR y_C)`

and

`E_d(0,A,B,C,y,a,w)`

`=w AND ((y_A AND NOT y_B) OR NOT y_C)`.

Under `x_{j(s)}=y_s` and `x_{k(s)}=a_s`, this realizes the complete pointwise
ENC-016 semantic schema on all `2^(3d+1)` expanded-cube rows, not only its
radius-one halo.

Let `K_d=C(E_d)`. For fresh suffix inputs `z_1,...,z_m`, put

`F_{d,m}=E_d AND z_1 AND ... AND z_m`.

Then `C(F_{d,m})=K_d+m`, while the exact semantic joint quotient under every
diagonal context pair `(q,s,s,s)` has at least `2m` active classes. Hence its
signed loss is at most `K_d-m`, negative for `m>K_d`.

Consequently, ambient global minimality, all GATE-004P diagonal hypotheses,
and the complete pointwise ENC-016 expanded-context-cube schema do not force
positive quotient loss for arbitrary total functions.

## Proof

The displayed equations define a total finite Boolean function. On the
diagonal `A=B=C=s`, absorption and contradiction give

`E_d(1,s,s,s,.)=w AND y_s`,

`E_d(0,s,s,s,.)=w AND NOT y_s`.

Thus `E_d` is nonconstant, the diagonal branches OR to `w`, and varying all
`y_s` with `w=1` realizes every complementary output column. The two formulas
also match the positive and negative ENC-016 conditions pointwise for every
independent triple `(A,B,C)`.

LEMMA-037 now gives the exact minimum-size identity

`C(F_{d,m})=C(E_d)+m=K_d+m`.

Choose a minimum circuit for `E_d` and append the `m` fresh AND gates. Under a
diagonal row `(q,s,s,s)`, the appended traces are

`T_{q,k}=w AND [y_s if q=1 else NOT y_s] AND z_1 AND ... AND z_k`

for `1<=k<=m`. They are the same `2m` pairwise-distinct, nonconstant,
non-input functions audited in LEMMA-038 and LEMMA-040. All survive in the
joint quotient, so `q_s>=2m` and

`|C|-q_s<=(K_d+m)-2m=K_d-m`.

For either fixed polarity, every appended trace on the diagonal cube depends
on the selector context `s`; choosing `m>=R` also supplies the large trace
region required by GATE-004P. Therefore all claimed hypotheses coexist with
negative loss for `m>=max(K_d+1,R)`. QED.

## Scope

The construction copies the full pointwise formula-condition schema but does
not equal `SAT-gamma` on every suffix formula. In SAT, each residual applies
existential satisfiability to the displayed condition conjoined with an
arbitrary encoded formula. GATE-004S retains that exact suffix-wide relation.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits for an explicit total Boolean function, the full affine expanded context cube, and exact diagonal joint quotients |
| Uniform/non-uniform | Explicit uniformly described function family; `K_d` is the non-uniform minimum size of each finite base |
| Circuit size | Exact parent size `K_d+m`; quotient at least `2m`; signed loss at most `K_d-m` |
| Circuit depth | Base unrestricted; displayed fresh tail adds `m` layers, with depth unrestricted in the exact size identity |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Expanded context geometry over `F_2`; computation is Boolean |
| Asymptotic quantifiers | Every `d>=1`; every `m>=1`; negative loss for `m>K_d`, with all inherited trace hypotheses for `m>=max(K_d+1,2^d)` |
| Regime | Worst-case exact total-function computation; method obstruction matching the pointwise ENC-016 schema, not SAT-gamma |

