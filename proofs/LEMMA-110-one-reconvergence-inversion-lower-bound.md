# LEMMA-110 — one reconvergence preserves half the formula inversion bound

**Label: PROVED**

Let

`W_m = AND_{i=1}^m (NOT u_i OR v_{i,1} OR ... OR v_{i,p})`

with pairwise-disjoint inputs and fixed `p>=1`. Consider any pruned
fan-in-two AND/OR, fan-in-one NOT circuit for `W_m` having exactly

`B=(p+1)m`

binary gates, one more than the essential-input connectivity minimum. If it
has `N` NOT gates, then

`N >= max(ceil(m/2),ceil(log_2(m+1)))`.

For the four-positive/one-negative tail (`p=4`), every such circuit has size
at least

`5m + max(ceil(m/2),ceil(log_2(m+1)))`.

## The output graph is unicyclic

Put `n=(p+1)m`, the number of essential raw inputs. Form the underlying
undirected multigraph of the pruned output cone, retaining raw inputs, binary
gates, and NOT gates as vertices and retaining every input wire as an edge.
It is connected. It has

`V=n+B+N` and `E=2B+N`.

With `B=n`, its cyclomatic number is

`E-V+1 = B-n+1 = 1`.

Thus the multigraph is unicyclic. Parallel edges are counted normally; a
repeated binary input would itself consume the unique cycle.

## Formula unfolding loses at most a factor two

Unfold the circuit from its output by making one copy of a vertex for every
directed path from that vertex to the output. The result is a fan-out-one
formula computing the same function. A connected unicyclic multigraph has at
most two simple paths between any two vertices. Every directed path in the
circuit is a simple path in that multigraph, so each original gate is copied
at most twice. In particular, the unfolded formula has at most `2N` NOT
gates.

LEMMA-109 proves `d(W_m)=m`. Morizumi's formula inversion theorem therefore
requires every formula for `W_m` to contain at least `m` NOT gates. Hence
`2N>=m` and `N>=ceil(m/2)`.

Independently, Markov's circuit inversion theorem gives
`N>=ceil(log_2(m+1))`. Taking the maximum proves the statement.

## Quantitative boundary

The displayed standalone circuit has total size `(p+2)m-1`. At `p=4`, the
one-reconvergence lower certificate is short by

`m-1-max(ceil(m/2),ceil(log_2(m+1)))`.

It closes this binary-gate stratum through `m=4`, but the deficit is positive
from `m=5` and asymptotic to `m/2`.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuit output cones, undirected cycle rank, formula unfolding, and formula/circuit inversion complexity |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform one-negative clause family |
| Circuit size | At exactly `(p+1)m` binary gates, at least `max(ceil(m/2),ceil(log2(m+1)))` NOT gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected multigraph cycle rank and Boolean-lattice inversion only |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, and every pruned circuit for `W_m` with exactly `(p+1)m` binary gates |
| Regime | Exact worst-case structural lower bound for one binary-gate stratum; not a full minimum-size, quotient, SAT-lower-bound, or terminal theorem |
