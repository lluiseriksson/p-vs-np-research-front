# LEMMA-164 — every cyclic core has a formula source that lowers rank

**Label: PROVED**

Let a pruned Boolean output cone have connected undirected cycle rank `r>=1`.
There is a core vertex `s` of degree `d>=2` such that:

1. the trees feeding `s`, together with `s`, form a fanout-one formula
   `A(X)` computing a nonconstant bit `z`;
2. every input in `X` reaches the output only through `z`; and
3. fixing an attained value of `z`, propagating constants, and pruning leave
   cycle rank at most `r-d+1<=r-1`.

## Proof

Take the undirected 2-core `K` and orient its edges in circuit direction.

If `K` is one 2-connected block, choose any source vertex `s` of its acyclic
orientation. Deleting `s` leaves `K-s` connected by 2-connectivity.

Otherwise root the block-cut tree toward the block containing the output-side
attachment and choose an outermost cyclic block `B`. Let `a` be its unique
articulation toward the output. No core edge of `B` can point from `a` back
into `B`: every subsequent path to the output would have to return through
`a`, creating a directed cycle. Thus `a` is a sink in `B`. Choose a source
`s` of the orientation of `B`; it is different from `a`. As a nonarticulation
vertex of the 2-connected block `B`, deleting `s` leaves `B-s` connected,
and hence leaves the whole core connected.

In either case `s` has no incoming core edge. Everything feeding it outside
the core lies in attached trees, so their union with `s` is a formula. Its
input variables have no bypass around `s`; prunedness and essentiality make
`z` nonconstant.

Let `d` be the degree of `s` in `K`. Deleting `s` removes `d` edges and one
vertex while preserving connectedness. Therefore the remaining core rank is

`(E-d)-(V-1)+1=r-d+1`.

Fixing `z` and further pruning cannot increase that rank. Minimum core degree
gives `d>=2`.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned finite Boolean DAG output cones, undirected 2-cores, and block-cut trees |
| Uniform/non-uniform | Every individual non-uniform finite output cone |
| Circuit size | No gate lower bound; fixing one formula-source bit lowers rank by at least `d-1>=1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2` and graph connectivity |
| Asymptotic quantifiers | Every connected pruned output cone of cycle rank at least one |
| Regime | Exact worst-case topology theorem; not a Boolean lower bound, SAT lower bound, or terminal result |
