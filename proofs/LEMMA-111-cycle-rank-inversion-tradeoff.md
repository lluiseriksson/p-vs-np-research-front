# LEMMA-111 — cycle rank gives an all-DAG inversion tradeoff

**Label: PROVED**

Let

`W_m = AND_{i=1}^m (NOT u_i OR v_{i,1} OR ... OR v_{i,p})`

on pairwise-disjoint inputs, for fixed `p>=1`. Put

`r=ceil(log_2(m+1))`

and

`g(m)=min_{t>=0} [t+max(ceil(m/2^t),r)]`.

Then the unrestricted circuit size satisfies

`(p+1)m-1+g(m) <= C(W_m) <= (p+2)m-1`.

Moreover, `g(m)=m` for `1<=m<=4`, while
`g(m)=Theta(log m)` asymptotically. Thus the bound proves the displayed
circuit exact through `m=4`, but its remaining deficit is

`m-g(m)=m-Theta(log m)`.

## Exact cycle rank

Consider any pruned circuit for `W_m`. Let `n=(p+1)m`, let `B` be its number
of binary gates, and let `N` be its number of NOT gates. Essential-input
connectivity gives `B>=n-1`. Set

`t=B-n+1>=0`.

The underlying connected undirected multigraph of the output cone has
`V=n+B+N` vertices and `E=2B+N` edges. Its cycle-space dimension is exactly

`E-V+1=B-n+1=t`.

## At most `2^t` unfolding copies

Fix a vertex `x`, the output vertex `o`, and one undirected simple reference
path `P_0` between them. For every other simple `x`-to-`o` path `P`, the
symmetric difference `P triangle P_0` is an even-degree edge set, hence an
element of the graph's binary cycle space. The map is injective because
`P=(P triangle P_0) triangle P_0`. A `t`-dimensional binary cycle space has
`2^t` elements, so there are at most `2^t` simple paths from `x` to `o`.

Every directed circuit path is one of those simple paths. When the circuit is
unfolded into a fan-out-one formula, a gate is copied once per directed path
to the output and therefore at most `2^t` times. The unfolded formula has at
most `2^t N` NOT gates.

LEMMA-109 gives `d(W_m)=m`, so Morizumi's formula inversion theorem implies

`2^t N>=m`, hence `N>=ceil(m/2^t)`.

Markov independently gives `N>=r`. Therefore every circuit with cycle rank
`t` has size

`B+N >= n-1+t+max(ceil(m/2^t),r)`.

Minimizing over all possible `t` proves the lower bound.

## Optimization audit

For `m<=4`, `t=0` gives value `m`, and every `t>=1` gives at least `m`, so
`g(m)=m`. For `m>=5`, `t=1` already gives a value below `m`, so the method no
longer reaches the displayed upper bound.

Always `g(m)>=r=Omega(log m)`. Conversely, choose

`t=max(0,ceil(log_2(m/r)))`.

Then `ceil(m/2^t)<=r`, so `g(m)<=t+r=O(log m)`. This proves
`g(m)=Theta(log m)` and the stated asymptotic deficit.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuit output cones, binary cycle spaces, formula unfolding, and formula/circuit inversion complexity |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform one-negative clause family |
| Circuit size | Lower `(p+1)m-1+g(m)`, upper `(p+2)m-1`, with exact integer optimization over cycle rank |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Binary cycle space over `F_2` for an undirected multigraph; Boolean-lattice inversion for the computed function |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, and every pruned unrestricted circuit for `W_m` |
| Regime | Exact worst-case all-DAG lower bound and asymptotic method audit; not a base direct sum, quotient theorem, SAT lower bound, or terminal result |
