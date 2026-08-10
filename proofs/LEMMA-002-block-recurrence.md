# LEMMA-002 — Block-restriction recurrence implies a superlinear bound

**Label: PROVED**

## Statement

Let `S : N -> R_{>=0}`. Suppose there are constants `A,B>0`, `0<=beta<1`,
`delta>0`, and `n0` such that for every integer `n>=n0` there is an integer
`m=m(n)` satisfying

`n-A n^beta <= m < n`

and

`S(n) >= S(m) + B n^(beta+delta)`.

Then `S(n)=Omega(n^(1+delta))`.

### Model card

| Field | Value |
|---|---|
| Computational model | Abstract size recurrence; circuit application uses general Boolean circuit gate count |
| Uniform/non-uniform | Not applicable to abstract lemma; application is non-uniform |
| Circuit size | Recurrence gain `B n^(beta+delta)` over length loss at most `A n^beta` |
| Circuit depth | Unrestricted in the intended application |
| Fan-in | AND/OR two; NOT one in the intended application |
| Randomness | None |
| Advice | None in the lemma |
| Oracle access | None |
| Field/algebraic model | Real-valued nonnegative recurrence; no algebraic computation model |
| Asymptotic quantifiers | Fixed constants; every integer `n>=n0`; one smaller `m(n)` per `n` |
| Regime | Worst-case size recurrence |

## Proof

Starting at `n_0=n`, repeatedly choose `n_{i+1}=m(n_i)` until the first index
`r` with `n_r<n0`. The sequence decreases by at least one, so it terminates.
Write `d_i=n_i-n_{i+1}`. The hypotheses give

`1 <= d_i <= A n_i^beta`

and, after telescoping,

`S(n) >= B sum_{i<r} n_i^(beta+delta)`.

Since `d_i <= A n_i^beta`,

`n_i^(beta+delta) >= (d_i/A) n_i^delta`.

For every real `x` in `[n_{i+1},n_i]`, `x^delta <= n_i^delta`, hence

`d_i n_i^delta >= integral_{n_{i+1}}^{n_i} x^delta dx`.

Therefore

`S(n) >= (B/A) integral_{n_r}^{n} x^delta dx`

`= (B/(A(1+delta))) (n^(1+delta)-n_r^(1+delta))`.

Because `n_r<n0` is bounded independently of `n`, this is
`Omega(n^(1+delta))`.

## Circuit corollary

Let `S(n)` be the minimum number of gates computing `SAT-gamma` on all `n`-bit
strings. If every minimum length-`n` circuit has a projection to a length-`m`
SAT slice with `n-A n^beta <= m<n`, and the projected circuit has an equivalent
derived circuit using at most `S(n)-B n^(beta+delta)` gates, then GATE-004 holds
with the same `delta`.

The recurrence is proved; existence of those projections with that circuit
loss is exactly the open GATE-004B.
