# LEMMA-139 — general cycle-rank/negation tradeoff for `W_m`

**Label: PROVED**

Fix `p>=1`. Let a pruned AND/OR/NOT circuit computing either `W_m` or
`NOT W_m` have undirected cycle rank `r` and `q` NOT gates. For every `m>=1`,

`q >= m-max(r-1,0)`.

Thus ranks zero and one require at least `m` NOT gates, while every rank
`r>=2` requires at least `m-r+1`. Markov's independent lower bound may be
larger when the displayed right-hand side is small.

## Induction on cycle rank

Ranks zero and one are LEMMA-119 and LEMMA-123. Let `r>=2` and assume the
theorem for every smaller rank. If `m-r+1<=0`, the desired inequality is
immediate from `q>=0`; hence assume `m>=r`.

Let `K` be the loopless undirected 2-core of the output cone.
Constants, if present in the ambient convention, are first propagated and
pruned; every remaining source-side bit below is therefore nonconstant and
its attached trees contain primary inputs.

### Articulation case

Suppose `K` has an articulation. Root its block-cut tree toward the unique
core attachment leading through the pruned output-side tree to the output,
and choose an outermost cyclic side. Every directed path from that side to
the output crosses the articulation `s`; no incident edge can point from `s`
back into the side, since it would have to return to `s` and create a directed
cycle. The side together with `s` is therefore a pruned subcircuit `A(X)`
computing a nonconstant bit `z`, and replacing it by input `z` leaves a
downstream circuit `D(z,Y)`.

Cycle rank is additive across the one-vertex sum. Write the two positive
ranks as `r_1+r_2=r`, with `r_1,r_2>=1`, and let `h` be the NOT count of `A`.
Apply LEMMA-121.

- If no clause is cut, write `a+b=m`. The induction hypothesis gives
  `h>=a-r_1+1` and, after fixing the satisfied code of `z`,
  `q-h>=b-r_2+1`; if the latter cofactor prunes to smaller rank, the bound
  only strengthens. Thus `q>=m-r+2`. Empty sides are covered separately:
  nonconstant `z` rules out `a=0`, while `b=0` discards the downstream cost
  and leaves the stronger upstream bound.
- If one clause is cut, there is no `X`-whole clause. The attained value that
  forces it true leaves the selected polarity of `W_{m-1}` downstream, at
  some rank `r_2'<=r_2<=r-1`. The induction hypothesis gives at least
  `m-r_2' >= m-r+1` downstream NOT gates when `r_2'>=1`; if `r_2'=0`,
  LEMMA-119 gives `m-1>=m-r+1` instead.

### No-articulation case

If `K` has no articulation, deleting any vertex leaves it connected. Orient
the core edges in the circuit direction and choose a source vertex `s`. Its
attached trees together with `s` form a formula `A(X)` computing a
nonconstant bit `z` with `h` NOT gates. Every input in `X` reaches the output
only through `z`.

Let `d>=2` be the core degree of `s`. Deleting `s` leaves a connected graph of
cycle rank

`r' = r-d+1 <= r-1`.

Fixing an attained value of `z`, propagating constants, and pruning can only
lower that rank and remove gates outside the residual circuit.

With no cut clause, LEMMA-121 gives an upstream formula cost `h>=a`. If the
residual rank is positive, induction gives at least `b-r'+1` downstream and
therefore `q>=m-r+2`; if it is zero, LEMMA-119 gives `b` and hence the
stronger `q>=m`. The case `b=0` is also stronger. With one cut clause, a
positive-rank residual selected polarity of `W_{m-1}` needs at least
`m-r' >= m-r+1` NOT gates by induction; at rank zero LEMMA-119 gives
`m-1>=m-r+1`.

Both core cases prove `q>=m-r+1` for rank `r`, completing the induction.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted AND/OR/NOT circuits, undirected 2-cores, block-cut trees, and one-bit cofactors |
| Uniform/non-uniform | Every individual non-uniform circuit for either polarity of `W_m`; uniform function family |
| Circuit size | NOT lower `m-max(r-1,0)` at exact cycle rank `r`; binary count otherwise unrestricted |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2`, vertex sums, and Boolean cofactor partitions |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, every integer `r>=0`, and every pruned circuit of exact rank `r` |
| Regime | Exact worst-case function-specific tradeoff; not additivity over an external base, a SAT lower bound, or a terminal result |
