# LEMMA-243 — an irredundant tree cut partitions its antichain leaves

**Label: PROVED**

Let `T` be a finite tree directed from its `k>=1` leaves `S` toward one root
`o`, with every nonroot vertex having one outgoing edge. Let `C` be an
inclusion-minimal vertex set meeting every directed `S`-to-`o` path. Then:

1. `C` is an antichain under reachability;
2. every leaf-to-root path meets exactly one member of `C`; and
3. the nonempty sets

   ```text
   S_c = {s in S : the s-to-o path meets c},   c in C,
   ```

   partition `S`.

Consequently `|C|<=k`, with equality exactly when every cut gate covers one
leaf. A gate covering many leaves still contributes one physical cut vertex.

## Proof

If two cut vertices `c,d` were comparable, suppose `c` reaches `d`. Every
leaf-to-root path meeting `c` would later meet `d`; removing `c` would leave a
cut, contrary to inclusion minimality. Thus `C` is an antichain.

Every leaf path meets `C` by hypothesis. It cannot meet two members, because
two vertices on one directed tree path are comparable. Hence it meets exactly
one. Assigning a leaf to that unique vertex gives pairwise disjoint sets
`S_c` whose union is `S`.

Finally, every vertex of `T` lies on a path from some leaf to the root. For
`c in C`, such a leaf path meets `c`; by uniqueness that leaf belongs to
`S_c`. Thus every block is nonempty, giving `|C|<=|S|`. Equality of the two
finite cardinalities is equivalent to every nonempty block being a singleton.

The theorem is cut accounting only. It does not prove that any cut gate has
equal old/new functions or is a paid host.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite rooted directed tree extracted from a physical fan-in-two circuit DAG |
| Uniform/non-uniform | Every finite non-uniform tree, leaf antichain, root, and inclusion-minimal vertex cut |
| Circuit size | `k` leaves, cut size at most `k`, with exact leaf-block partition |
| Circuit depth | Unrestricted root-path length |
| Fan-in | Tree indegree unrestricted in the abstract statement; application tree has indegree at most two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed reachability, tree paths, and finite set partitions |
| Asymptotic quantifiers | Every integer `k>=1`, tree vertex, leaf, irredundant cut, and induced block |
| Regime | Exact physical cut-capacity theorem; not cut equality, endpoint payment, SAT lower bound, or terminal result |
