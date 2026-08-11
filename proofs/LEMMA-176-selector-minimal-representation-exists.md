# LEMMA-176 — a selector-minimal minimum representation exists

**Label: PROVED**

Fix a Boolean function `F(x,Z)` that depends essentially on every variable
in its finite input set, and fix the basis
`{AND,OR,NOT}` with binary AND/OR and unary NOT. Among all minimum-size
pruned circuits for `F`, there is one minimizing

`S(C)=#{noninput gates g : g|_{x=0} != g|_{x=1}}`.

Moreover every such minimum circuit has the same value of `N+r`.

## Proof

Let the minimum gate count be `s`. Topologically number the `s` gates. Each
gate has one of three labels and chooses its predecessor or predecessors from
the fixed input set and earlier gate numbers. There are therefore only
finitely many syntactic circuits of size `s`, and hence finitely many that
compute `F`. The nonempty set of their integer values `S(C)` has a minimum.
Pruning any unused output-cone material cannot increase size or `S`, so a
pruned minimizer exists.

For completeness, if `B` is the binary-gate count and `e` the fixed number
of essential input sources, connected output-cone counting gives
`r=B-e+1`. Hence `N+r=(B+N)-e+1=s-e+1`, the exact identity used in
LEMMA-153. Thus every pruned minimum representation has the same resource
sum.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite deterministic AND/OR/NOT DAG representations with one distinguished primary input |
| Uniform/non-uniform | Extremal existence for each individual finite non-uniform function; no uniform selector algorithm |
| Circuit size | Minimum total gate count; exact common `N+r` inherited from LEMMA-153 |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every finite Boolean function essential in every listed input, with one distinguished input, and all its minimum circuits |
| Regime | Exact finite extremal-existence lemma; not an exposure theorem, circuit lower bound, SAT lower bound, or terminal result |
