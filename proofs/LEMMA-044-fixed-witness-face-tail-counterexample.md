# LEMMA-044 — fixed-coordinate witness faces admit exact fresh tails

**Label: PROVED**

## Statement

Let `H(r,u)` be any nonconstant total Boolean function with minimum
unrestricted circuit size `K`. Let `z_1,...,z_m` be fresh raw inputs and put

`G(r,z,u)=H(r,u) AND z_1 AND ... AND z_m`.

Then:

1. `C(G)=K+m`;
2. on the face `z=1^m`, `G(r,1^m,u)=H(r,u)` exactly; and
3. if two designated row residuals `H(r_0,.)` and `H(r_1,.)` are distinct
   nonconstant functions, their semantic joint quotient in the displayed
   minimum circuit for `G` contains at least `2m` distinct active tail
   classes.

Thus any prescribed local agreement table supported entirely on a
codimension-`m` raw face can coexist with signed row-pair loss at most `K-m`,
provided its two base residuals admit such a total extension `H`.

## Proof

LEMMA-037 iterated over the fresh inputs gives `C(G)=C(H)+m=K+m`, so a
minimum circuit for `H` followed by the displayed AND chain is globally
minimum. The face identity is immediate.

Under row `r_b`, the appended traces are

`H(r_b,u) AND z_1 AND ... AND z_k`, `1<=k<=m`.

Changing `k` changes the essential fresh-input set. At fixed `k`, the two
functions remain distinct after setting all `z_i=1`. They are nonconstant and
non-input, hence all `2m` survive in the semantic joint quotient. Therefore

`|C(G)|-q <= (K+m)-2m=K-m`.

This proves every item. QED.

## Application to common-padded DNF witnesses

ENC-019 places every commonly outer-padded witness in the face `z=1^m`.
Take `H` to recognize the remaining canonical compact DNF encoding and output
whether its represented partial assignments make the selected ENC-016
condition satisfiable; extend it arbitrarily off those cores. Complete-
assignment cores ensure the two diagonal residuals are distinct and
nonconstant. A standard parser plus DNF scan gives a circuit of size
`poly(R,L,t)` for core budget `t=poly(R,L)`.

Choose the fixed exponent `c>0` smaller than the reciprocal of that polynomial
degree. Along infinitely many lengths with `L=floor(c log_2 n)`, reserve a
multiple-of-four block

`m=n-(6L+13)-t`.

Then `m/K -> infinity`. The resulting ambient functions agree with SAT at all
commonly padded compact DNF witness strings but have negative diagonal loss.
This does not falsify full GATE-004U, whose witness set also includes dense or
short-padding encodings outside every growing fixed-coordinate face.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits, local agreement on a fixed raw-coordinate face, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform base `H`; uniform fresh-coordinate extension and explicit common-padding application |
| Circuit size | Exact size `K+m`; quotient at least `2m`; signed loss at most `K-m` |
| Circuit depth | Base unrestricted; displayed fresh AND tail adds `m` layers |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; the witness face is a Boolean-coordinate subcube |
| Asymptotic quantifiers | Every finite nonconstant base and `m>=1`; common-padding application on infinitely many compatible lengths for sufficiently small fixed `c>0` |
| Regime | Worst-case exact total-function computation; method obstruction for local witness-face agreement, not SAT-gamma on all suffixes |

