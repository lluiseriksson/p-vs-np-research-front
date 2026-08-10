# LEMMA-014 — a logarithmic-step size recurrence is superlinear

**Label: PROVED**

## Statement

Let `S:N->R_{>=0}`. Suppose there are constants `A,B,delta>0` and `n0`
such that for every integer `n>=n0` there is an integer `m` satisfying

`n-A log_2(n) <= m<n`

and

`S(n)>=S(m)+B n^delta`.

Then

`S(n)=Omega(n^(1+delta)/log n)`.

In particular, for every fixed `0<delta'<delta`,
`S(n)=Omega(n^(1+delta'))`; the recurrence proves a superlinear lower bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract nonnegative size recurrence; intended application to unrestricted circuit gate count |
| Uniform/non-uniform | Not applicable abstractly; non-uniform in circuit application |
| Circuit size | Gain `B n^delta` for length loss at most `A log_2 n` |
| Circuit depth | Unrestricted in circuit application |
| Fan-in | AND/OR two; NOT one in circuit application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Real-valued recurrence only; no algebraic computation model |
| Asymptotic quantifiers | Fixed positive constants; every sufficiently large integer `n` |
| Regime | Worst-case size recurrence |

## Proof

Start at a sufficiently large `N` and repeatedly choose the recurrence witness
until the current length first falls below `N/2`. While it remains at least
`N/2`, each step loses at most `A log_2 N` length and gains at least
`B(N/2)^delta` size. Crossing an interval of length at least `N/2` therefore
requires at least

`N/(2A log_2 N)-1`

steps. Telescoping and using `S>=0` gives

`S(N) >= (N/(2A log_2 N)-1) B(N/2)^delta`

which is `Omega(N^(1+delta)/log N)`. Finally,
`N^(delta-delta')/log N -> infinity` for every `delta'<delta`, proving the
last assertion. QED.
