# LEMMA-180 — earliest-NOT signature dichotomy

**Label: PROVED**

Assume GATE-004BZ and let `n=NOT h` be a topologically earliest NOT whose
gate function depends essentially on the fresh negative input `u`. Write
`n_ab` and `h_ab` for the cofactors at `(u,t)=(a,b)`.

Then

`h_00 <= h_10`, `h_01 <= h_11`,

and hence

`n_00 >= n_10`, `n_01 >= n_11`

pointwise as Boolean functions of the remaining variables. Exactly one of
the following cases holds:

1. **satisfying-signature stability:** `n_01=n_11`, in which case the
   essential `u` dependence of `n` occurs between `00` and `10`; or
2. **satisfying-signature switching:** `n_01!=n_11`, in which case every
   directed path from `n` to the output contains a first gate whose `01` and
   `11` cofactors are equal after a predecessor on that path has unequal
   cofactors. Every such first cancellation gate is binary.

## Monotonicity before the first NOT

Every earlier NOT gate is `u`-insensitive by the choice of `n`; injectivity of
negation also makes its input `u`-insensitive. Starting from raw `u` and all
`u`-independent signals, topological induction through AND/OR gates shows
that every `u`-sensitive signal before `n`, including `h`, is monotone
nondecreasing in `u`. This gives the two inequalities for `h`; applying NOT
reverses them.

If `n_01=n_11`, essential `u` dependence cannot occur at `t=1`, so it occurs
at `t=0`. Otherwise `n_01` and `n_11` differ. The output cofactors at `01`
and `11` are both the same base function `A`. Along any path from `n` to the
output, equality must therefore appear for the first time. A NOT gate cannot
be that first gate because it preserves inequality of Boolean functions, so
the first cancellation gate is AND or OR.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted plateau circuits localized before and after an earliest u-sensitive NOT |
| Uniform/non-uniform | Every individual finite non-uniform GATE-004BZ parent |
| Circuit size | No new size bound; exact ordered cofactor and first-cancellation classification |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean pointwise order and cofactors only |
| Asymptotic quantifiers | Every operational two-gate plateau and every topologically earliest u-sensitive NOT in it |
| Regime | Exact local structural dichotomy; not an uncrossing theorem, SAT lower bound, or terminal result |
