# LEMMA-127 — every output-oriented theta core has split budget two

**Label: PROVED**

Orient a theta 2-core as part of a pruned circuit DAG, and let `r` be the
unique core vertex whose attached tree contains the output (or the output
itself if it lies in the core). Then every core vertex other than `r` has at
least one outgoing core edge, `r` has none, and

`sum_{v != r} (outdeg_core(v)-1)=2`.

Consequently exactly one of the following occurs:

1. one branch vertex is a core source of outdegree three, and every other
   non-root core vertex has outdegree one; or
2. exactly two core vertices have outdegree two, and every other non-root
   core vertex has outdegree one.

The second case includes two parallel source splits and a source split
followed by a nested split.

## Proof

Every vertex reaches the output. A core vertex other than `r` cannot leave the
core through an attached tree and return elsewhere, because such a tree meets
the core at only that vertex. Hence it needs an outgoing core edge. Conversely
an outgoing core edge from `r` would eventually return to `r` on the unique
route to the output, creating a directed cycle, so its core outdegree is zero.

A theta core has cycle rank two, hence `E=V+1`. Summing core outdegrees gives

`sum_{v != r}(outdeg(v)-1)=E-(V-1)=2`.

Each summand is a nonnegative integer. Theta vertices have degree at most
three. The only partitions of the excess two are therefore one outdegree-
three vertex or two outdegree-two vertices. An outdegree-three vertex has no
incoming core edge and is a core source.

## Model card

| Field | Value |
|---|---|
| Computational model | DAG orientations of theta 2-cores in pruned Boolean output cones |
| Uniform/non-uniform | Every individual finite theta-core circuit orientation |
| Circuit size | No gate lower bound; exact split-excess total two |
| Circuit depth | Unrestricted finite DAG |
| Fan-in | Original AND/OR two and NOT one; core outdegree at most three |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank and directed outdegree accounting |
| Asymptotic quantifiers | Every output-oriented theta core in which all vertices reach one output |
| Regime | Exact topology theorem; not a Boolean lower bound or terminal result |
