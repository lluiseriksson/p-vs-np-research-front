# LEMMA-125 — every bicyclic core is theta, figure-eight, or dumbbell

**Label: PROVED**

Let `G` be a connected undirected multigraph of cycle rank two, with no
self-loops. Repeatedly delete degree-zero and degree-one vertices to obtain
its nonempty 2-core, then suppress maximal degree-two paths. The resulting
kernel has exactly one of three forms:

1. two vertices joined by three parallel kernel edges (theta);
2. one vertex carrying two kernel loops (figure-eight); or
3. two vertices joined by one kernel edge, with one kernel loop at each
   endpoint (dumbbell).

Kernel loops represent ordinary cycles before suppression; the original
multigraph itself need not contain self-loops. In the last two cases the
original core has an articulation separating a leaf cycle block from the
rest. The theta core has no such cycle-separating articulation.

## Proof

Leaf deletion and degree-two suppression preserve cycle rank. In the 2-core,

`sum_v (deg(v)-2) = 2E-2V = 2`.

Every summand is nonnegative. Hence either one vertex has degree four and all
others degree two, or two vertices have degree three and all others degree
two. Suppression turns the first case into one degree-four vertex with its
four half-edges paired as two loops: figure-eight.

In the second case, the two degree-three vertices supply six half-edges. Each
suppressed path either joins the two vertices or returns to its starting
vertex. Degree parity leaves only three cross paths (theta), or one cross path
plus one returning path at each endpoint (dumbbell). These exhaust the
possibilities and give the articulation statement after expanding the paths.

## Model card

| Field | Value |
|---|---|
| Computational model | Connected undirected cycle-rank-two multigraph cores obtained from Boolean output cones |
| Uniform/non-uniform | Every individual finite graph; no circuit family assumption |
| Circuit size | No gate lower bound; exact three-type topological classification |
| Circuit depth | Not applicable to the undirected core; original circuit remains a finite DAG |
| Fan-in | Original circuit AND/OR two and NOT one; graph statement uses undirected degrees |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Cycle rank over `F_2`; no algebraic circuit model |
| Asymptotic quantifiers | Every finite connected loopless multigraph with cycle rank exactly two |
| Regime | Exact structural graph theorem; not a Boolean lower bound or terminal result |
