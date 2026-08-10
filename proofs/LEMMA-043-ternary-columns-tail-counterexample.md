# LEMMA-043 — ternary multi-witness columns admit fresh-tail expansion

**Label: PROVED**

## Statement

For every `d>=1`, put `R=2^d`. There is an explicit total Boolean function on
the full ENC-016 expanded prefix cube whose outputs:

1. have exactly the ENC-017 equality classes and multiplicities;
2. have one context-independent diagonal branch union;
3. include all complete-assignment columns; and
4. realize all `3^R` compact ternary diagonal patterns required by GATE-004T.

If its minimum base size is `K_d`, appending `m` fresh conjunctive suffix
inputs gives exact minimum size `K_d+m`, while every diagonal semantic joint
quotient retains at least `2m` active classes. Loss is at most `K_d-m` and is
negative for `m>K_d`. Therefore GATE-004T is false.

## Product-domain construction

For every primary variable `x_s`, use bits `l^x_s,h^x_s` saying that zero or
one is allowed. For every auxiliary variable `u_s`, use analogous bits
`l^u_s,h^u_s`. Let

`V=AND_s (l^x_s OR h^x_s) AND (l^u_s OR h^u_s)`

assert that all `2R` domains are nonempty. On expanded prefix `(q,A,B,C)`,
define

`D_d(1,A,B,C)=V AND (h^x_C OR (h^x_A AND l^u_B))`,

`D_d(0,A,B,C)=V AND (l^x_C OR (h^x_A AND l^x_B))`.

These expressions say exactly that the corresponding ENC-016 condition has
a satisfying assignment in the product domain.

Singleton domains encode complete assignments. Therefore two expanded
conditions induce the same `D_d` residual if and only if they are logically
equivalent: inequivalent conditions are distinguished by a singleton domain.
This proves the exact ENC-017 incidence table.

On the diagonal `A=B=C=s`, absorption gives

`D_d(1,s,s,s)=V AND h^x_s`,

`D_d(0,s,s,s)=V AND l^x_s`.

Their OR is the common function `V`. Choosing each primary domain as
zero-only, one-only, or both and taking all auxiliary domains to be both
realizes all `3^R` ternary patterns. Singleton choices give the complete-
assignment columns.

## Minimum size and negative quotient loss

The base is nonconstant. Put

`F_{d,m}=D_d AND z_1 AND ... AND z_m`.

LEMMA-037 gives `C(F_{d,m})=K_d+m`. A minimum base circuit followed by the
fresh AND chain is therefore globally minimum. Under diagonal context `s`,
its appended traces are

`V AND h^x_s AND z_1 AND ... AND z_k`

and

`V AND l^x_s AND z_1 AND ... AND z_k`

for `1<=k<=m`. These `2m` functions are nonconstant, non-input, and pairwise
distinct by their essential tail sets and by the zero-only/one-only domain
choices. Thus `q_s>=2m` and loss is at most `K_d-m`.

The tail does not remove any required GATE-004T property: setting all `z_k=1`
recovers every assignment and ternary column, equality of tailed residuals is
equivalent to equality of base residuals by that same setting, and the common
diagonal union becomes `V AND z_1 AND ... AND z_m`.

To match GATE-004T's input-length quantifiers, embed `(q,A,B,C)` in the
ENC-016 varying prefix coordinates and reject other prefix settings. The
fixed-coordinate recognizer, product-domain validity circuit, and a constant
number of `R`-way selector trees give `K_d=O(R+L)`. For any fixed `0<c<1`,
with `L=floor(c log_2 n)` the remaining suffix budget

`m=n-(6L+13)-4R`

is positive and satisfies `m/K_d -> infinity`. Hence arbitrarily large
compatible lengths violate the claimed positive loss bound. QED.

## Boundary

This construction matches the prescribed output columns but does not use the
bit-level encodings of the suffix formulas that produce them. Any next gate
must retain explicit formula-composition geometry or exact SAT-gamma values
on all suffix strings; existence of even the complete compact column family
is insufficient.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits on the full expanded prefix cube, product-domain multi-witness suffixes, and exact diagonal semantic joint quotients |
| Uniform/non-uniform | Explicit uniformly described base; `K_d` is its non-uniform minimum size; uniform affine embedding into the exact prefix coordinates |
| Circuit size | `K_d=O(R+L)` upper bound; exact tailed size `K_d+m`; quotient at least `2m`; loss at most `K_d-m` |
| Circuit depth | Selector and validity base unrestricted in the minimum lower bound; displayed fresh tail adds `m` layers |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Expanded affine prefix geometry over `F_2`; computation is Boolean |
| Asymptotic quantifiers | Every `d>=1,m>=1`; for every fixed `0<c<1`, arbitrarily large compatible `n` have `m>K_d` and negative loss |
| Regime | Worst-case exact total-function computation; method obstruction, not SAT-gamma and not suffix-syntax preserving |
