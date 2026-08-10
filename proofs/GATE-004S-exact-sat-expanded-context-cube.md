# GATE-004S — exact SAT rigidity on the expanded context cube

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0`, put `L=floor(c log_2 n)`, `d=L-2`, `R=2^d`, and let `X_L` be
the full ENC-016 set of `2^(3d+1)` length-`p=6L+13` prefix rows.

Let `G:{0,1}^n->{0,1}` be any total Boolean function satisfying

`G(r,y)=SAT-gamma_n(r,y)`

for every `r in X_L` and every suffix `y in {0,1}^{n-p}`. For every minimum
unrestricted circuit `C` for `G`, let `q_s` be its exact semantic joint
quotient size under the two diagonal ENC-014 rows for context `s`. Then

`sum_s (|C|-q_s) >= R(B R^eta+1)`.

This is falsifiable by any total-function family agreeing exactly with SAT on
the expanded-cube cylinder but violating the inequality. LEMMA-041 does not
falsify it because that construction copies only the pointwise condition
schema; it does not agree with SAT's residual functions on arbitrary encoded
suffix formulas.

## Bridge

Take `G=SAT-gamma_n`. The agreement premise is immediate. The conclusion is
the GATE-004Q loss bound, and ENC-013 plus LEMMA-014 then yield GATE-004, the
first superlinear unrestricted SAT circuit lower bound.

## First attack

For fixed `(A,B,C)`, expand each ENC-016 residual into its at most two
conditioned-SAT disjuncts. Audit the resulting global incidence system across
all `R^3` triples: which exact conditioned residual functions repeat, which
unions overlap, and whether any minimum parent circuit can retain a fresh-tail
family while satisfying every suffix-wide identity. Pointwise truth-table
agreement receives no credit after LEMMA-041.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for total functions agreeing exactly with SAT-gamma on the full ENC-016 prefix cylinder; exact semantic joint quotients on its diagonal |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit expanded-cube and diagonal restriction families |
| Circuit size | Average diagonal parent-to-joint-quotient loss at least `B R^eta+1`, with `R=2^(L-2)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix geometry over `F_2`; computation and SAT residuals remain Boolean |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every eligible total `G`; every minimum circuit; all expanded rows and suffixes in the agreement premise |
| Regime | Worst-case exact total-function agreement with total SAT-gamma; no promise or distribution |

