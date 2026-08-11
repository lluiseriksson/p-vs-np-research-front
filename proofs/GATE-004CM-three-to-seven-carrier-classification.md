# GATE-004CM — classify plateau carriers of sizes three through seven

**Label: EXPLORATORY**

In the unresolved conditional `W=1` branch, LEMMA-190 and LEMMA-192 give

`3<=|H_{01,11}|<=7`.

The carrier contains the terminal edge `h -> n` and at least one earlier gate
on a directed path from raw `u` to `h`. Every gate other than `n` lies in the
union of the three two-element satisfying deletion sets.

## Falsifiable theorem

For every directed carrier and deletion incidence of size three through seven
consistent with LEMMA-179, the four cofactor codes, and rank-neutral pruning,
one of the following holds:

1. a same-size rewrite leaves the switching branch or lowers an earlier
   extremal potential;
2. a LEMMA-183 private-cone certificate exists;
3. some satisfying code needs at least three binary eliminations;
4. some satisfying pruning deletes a non-bridge edge of `gamma`; or
5. the symbolic Boolean cofactor system is unrealizable.

The proof must begin with carrier size three and retain the identity of the
predecessor on the raw-`u` to `h` path. A finite unlabeled graph enumeration
does not prove the Boolean cases.

LEMMA-193 classifies size three as an alternating AND→OR or OR→AND chain and
identifies the neutral deletion pair exactly. The local pattern is realizable
and hence not itself contradictory. GATE-004CN is the active cross-code fanout
exclusion for this first remaining size.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted switching plateau parent at conditional `W=1` with three pruning maps |
| Uniform/non-uniform | Every finite non-uniform operational tuple; finite topology/incidence split with symbolic labels |
| Circuit size | Carrier size three through seven; parent `K+2`; two binary losses per satisfying code |
| Circuit depth | Unrestricted ambient depth; carrier depth at most seven |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and preserved by rewrites |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor identities and cycle minors over `F_2` |
| Asymptotic quantifiers | Every active extremal `W=1` tuple and every valid satisfying pruning triple |
| Regime | Exact worst-case remaining bounded-carrier gate; not a numerical certificate, SAT lower bound, or terminal result |
