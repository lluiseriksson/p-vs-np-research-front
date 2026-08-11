# LEMMA-184 — a shared exit forces a second cancellation front

**Label: PROVED**

In the one-sided branch, write

`Delta(g) = g_01 XOR g_11`.

Thus `Delta(p) != 0`, `Delta(d)=0`, and one edge out of `p` is `p→d`.
Suppose `p` has a second live outgoing edge, meaning that edge begins a
directed path to the parent output. Then:

1. that second path contains a binary gate `c != d` whose predecessor on the
   path has nonzero `Delta` and whose own `Delta` is zero;
2. the routes through `d` and through the second exit determine a nonzero
   undirected cycle coordinate `gamma` in the parent output cone; and
3. under the exact two-gate plateau, `gamma` survives modulo contractions in
   every satisfying restricted minimum circuit.

## Proof

Follow a directed path beginning with the second edge. Its initial signal has
nonzero `Delta`, while the output has `Delta=0` because its `01` and `11`
cofactors both equal `A`. Choose the first gate `c` on this path with zero
`Delta`. Its path predecessor has nonzero `Delta`. A NOT cannot be `c`, since
negation is injective on Boolean functions, so `c` is AND or OR.

The gate is distinct from `d`. The first route reaches `d` directly from `p`.
If the second route reaches `d`, it must enter through the other input `q`;
but `Delta(q)=0`, so its first cancellation occurs at or before `q`, not at
`d`. Otherwise its first cancellation is plainly elsewhere.

Both live routes start at `p` and eventually reach the unique output. At their
first reconvergence, their union contains two distinct undirected routes with
the same endpoints, hence a nonzero cycle coordinate `gamma`. Under the
plateau, LEMMA-178 gives equal parent/minor cycle rank for every satisfying
code. LEMMA-174 then identifies the cycle spaces modulo contractions and says
that no nonzero parent coordinate, including `gamma`, is killed.

This proves a second cancellation front and survival, not a resource loss.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted one-sided plateau DAG with a live shared exit |
| Uniform/non-uniform | Every individual finite non-uniform operational parent |
| Circuit size | No new gate bound; one additional binary cancellation front and one surviving cycle coordinate |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout at `p` at least two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean symmetric differences and undirected cycle space over `F_2` |
| Asymptotic quantifiers | Every GATE-004CD shared-exit parent and all three satisfying restrictions |
| Regime | Exact worst-case topology/signature theorem; not a killed-cycle result, SAT lower bound, or terminal result |
