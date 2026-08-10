# GATE-004U — syntax-linked DNF witness rigidity

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0`, put `L=floor(c log_2 n)`, `R=2^(L-2)`, and use the full
ENC-016 expanded prefix cube `X_L` of length `p=6L+13`.

Let `D_{L,n}` be the explicit set of length-`n-p` suffix strings obtained as
follows:

1. encode complete or partial assignment conjunctions over all ENC-016
   primary and auxiliary identifiers;
2. combine any nonempty list of them by the exact binary OR formula token;
3. require the unpadded formula to fit; and
4. use ENC-010's identifier-1-fresh padding together with any outer
   double-NOT padding to reach length exactly `n-p`.

Let `G:{0,1}^n->{0,1}` be any total Boolean function satisfying

`G(r,y)=SAT-gamma_n(r,y)`

for every `r in X_L` and every `y in D_{L,n}`. For every minimum unrestricted
circuit `C` for `G`, let `q_s` be its exact semantic joint quotient size under
the two diagonal rows for context `s`. Then

`sum_s (|C|-q_s) >= R(B R^eta+1)`.

The statement is falsifiable by any total-function family matching SAT on all
specified bit-level DNF witnesses but violating the loss inequality.

## SAT bridge

Exact `SAT-gamma_n` satisfies the agreement premise by definition. The
conclusion is the GATE-004Q loss bound, so ENC-013 and LEMMA-014 yield the
first superlinear unrestricted SAT circuit lower bound GATE-004.

## Attack boundary

LEMMA-043 shows that the abstract output-column set carries no forcing power.
ENC-019 and LEMMA-044 close the first syntax-linked attempt as well: witnesses
sharing a growing common outer padding block lie in a fixed raw-coordinate
face, and those coordinates become an exact-minimum fresh tail.

Full GATE-004U remains open because `D_{L,n}` also contains DNFs with only
constant padding overhead. The next audit is padding density: construct and
verify a witness subfamily that still realizes the required multi-witness
patterns but is not contained in any growing fixed-coordinate face. Then test
whether a more general common predicate—not raw coordinates—can retain the
fresh-tail obstruction. No conclusion may use common-padded witnesses alone.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for total functions agreeing with SAT-gamma on the full expanded prefix cube at explicit padded DNF suffix encodings; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit prefix, assignment, OR-composition, and padding maps |
| Circuit size | Average diagonal parent-to-joint-quotient loss at least `B R^eta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix geometry over `F_2`; suffix witnesses use exact Boolean formula syntax |
| Asymptotic quantifiers | Exists fixed sufficiently small `c>0` and `B,eta>0`; every sufficiently large `n`; every eligible total `G`; every minimum circuit; all expanded rows and fitting padded DNF witnesses |
| Regime | Worst-case exact agreement on an explicit total-language subset; no promise or distribution in the ambient function |
