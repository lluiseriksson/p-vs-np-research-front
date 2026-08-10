# LEMMA-049 — bounded zero-block count leaves an exact clause tail

**Label: PROVED**

## Statement

Let `Z` be any family of bit strings on an outer region of length `P`. Suppose
the zero positions of every `z in Z` are contained in the union of at most
`b` intervals, each of length at most `D`. Put

`w=b+1`, `m=floor(P/w)`,

and assume `m>=D`. For `0<=i<m`, define the disjoint width-`w` clauses

`Q_i=OR_{t=0}^b z_{i+tm}`.

Then every `Q_i` is one on every member of `Z`.

For any nonconstant base `H` of exact circuit size `K`, the extension

`F=H AND product_{i=0}^{m-1} Q_i`

has exact unrestricted circuit size

`K+wm`.

Under any two restrictions giving distinct nonconstant base residuals, the
displayed minimum circuit has joint quotient size at least `(w+1)m`, and its
signed loss is at most

`K-m`.

Thus the extension has negative loss whenever

`floor(P/(b+1))>K`

and `floor(P/(b+1))>=D`.

## Proof

Coordinates within one `Q_i` are separated by exactly `m`. An interval of
length at most `D<=m` has coordinate diameter at most `m-1`, so it contains at
most one member of the group. At most `b` zero intervals can therefore zero
at most `b` of its `b+1` coordinates. At least one clause input remains one,
proving `Q_i=1` throughout `Z`.

The `m` groups are disjoint and use the first `(b+1)m<=P` coordinates.
LEMMA-048 with width `w=b+1` gives exact size `K+wm`, at least `(w+1)m`
quotient classes, and loss at most `K-m`. Any leftover outer coordinates are
ignored; restriction and lifting preserve exact complexity, as in LEMMA-039.
The two displayed inequalities make the loss negative and validate the
geometric premise. QED.

## SAT-syntax consequence

For neutral-padding families whose non-one bits occur inside `b=b(P)` blocks
of maximum length `D=D(P)`, common-inner-length DNF agreement cannot force
positive loss by itself whenever the canonical base size `K(P)` satisfies

`D(P)<=floor(P/(b(P)+1))` and `K(P)<floor(P/(b(P)+1))`.

In particular, every fixed `b,D` fails with a linear negative term. More
generally, any regime `b=o(P/K)` with `D=o(P/b)` fails. Avoiding this theorem
requires a sufficiently dense block count, sufficiently long blocks, or
syntax interactions outside the isolated outer-context family.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact total Boolean functions, zero supports covered by bounded coordinate intervals, disjoint positive clauses, globally minimum unrestricted circuits, and semantic joint quotients |
| Uniform/non-uniform | Arbitrary witness family and fully non-uniform base/minimum circuit; uniform distant-group construction |
| Circuit size | Exact `K+(b+1)m`; quotient at least `(b+2)m`; signed loss at most `K-m`, where `m=floor(P/(b+1))` |
| Circuit depth | Unrestricted; displayed OR and AND chains may be sequential |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer interval geometry only; computation is Boolean |
| Asymptotic quantifiers | Every finite `P,b,D` satisfying `floor(P/(b+1))>=D`, every qualifying string family, every nonconstant base, and every distinct nonconstant row pair |
| Regime | Worst-case exact total-function method obstruction; not a SAT circuit lower bound |
