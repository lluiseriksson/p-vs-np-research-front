# GATE-004AI — inject clause indices into negations or cycle coordinates

**Label: EXPLORATORY**

## Falsifiable theorem

Let `C` be a pruned unrestricted circuit for the four-positive/one-negative
product `W_m`. Let `N` be its number of NOT gates and let

`t=B-5m+1`

be the cycle-space dimension of its connected undirected output cone, where
`B` is its number of binary gates. Prove that the `m` clause indices admit an
injection into a disjoint union of the `N` NOT gates and `t` coordinates of
some cycle-space basis. In particular,

`m <= N+t`.

The theorem is falsified by any circuit for `W_m` with `N+t<m`; an alleged
injection is also falsified by two clause indices receiving the same target.

## Exact bridge to GATE-004AH

The output cone has `5m+B+N` vertices and `2B+N` edges, so its cycle rank is
exactly `t=B-5m+1`. Thus

`N+t>=m  iff  B+N>=6m-1`.

GATE-004AI is therefore a witness-level formulation of GATE-004AH, not a
weaker surrogate. A proof would establish the standalone size of `W_m`; it
would still not prove additivity over the canonical base, a SAT circuit lower
bound, or P versus NP.

## Attempted witness source

LEMMA-113 provides one transition for each pair `(S,i)`:

`R_S -> R_{S union {i}} = R_S AND NOT u_i`.

The intended proof would trace a transition backward from the output to its
first internal divergence and charge clause index `i` either to a NOT gate or
to an independent reconvergence. The missing step is a representation-
independent rule proving that different clause indices receive different
charges. Raw output transitions do not supply it, because the same output
node witnesses every edge of the restriction cube.

LEMMA-114 now supplies a first internal binary birth event for every clause
index. GATE-004AJ asks to trace those events nonlocally to NOT gates or cycle
coordinates with no collisions. The birth node itself cannot be the NOT
witness.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for the fixed four-positive/one-negative read-once clause product; output-cone cycle space |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform function family |
| Circuit size | Target witness inequality `N+t>=m`, exactly equivalent to `B+N>=6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean restriction cube |
| Asymptotic quantifiers | Every `m>=5` and every pruned circuit for `W_m` in the unresolved inversion range |
| Regime | Exact worst-case witness gate for standalone size; not a base direct sum, SAT lower bound, or terminal result |
