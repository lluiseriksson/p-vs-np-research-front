# LEMMA-065 — the formula boundary makes one through four signed-triple tails exact

**Label: PROVED**

## Statement

For pairwise-disjoint triples, put

`W_m=AND_{i=1}^m (p_i OR NOT(u_i AND v_i))`

and `r=ceil(log_2(m+1))`. Then

`C(W_m)>=min(4m-1,3m+r)`

and `C(W_m)<=4m-1`. Consequently

`C(W_m)=4m-1` for `m=1,2,3,4`.

For `m>=5`, this combined certificate leaves gap

`m-1-r`

below the factorized circuit.

## Exact decrease parameter

Along any increasing Boolean-lattice chain, one clause `Q_i` can make at
most one transition from one to zero. Its zero set is exactly

`p_i=0, u_i=v_i=1`.

Once `p_i` becomes one, the clause remains one; before that, once both
`u_i,v_i` become one, it remains zero until `p_i` changes. Every decrease of
the conjunction must include a one-to-zero transition of some clause, so the
number of conjunction decreases is at most `m`.

The bound is attained. Start with every variable zero. For each `i` in turn,
raise `u_i`, then `v_i`, causing `W_m` to fall, and then raise `p_i`, causing
it to rise. Previously repaired clauses remain one and later clauses are one
at all-zero inputs. Thus the inversion decrease parameter is exactly

`d(W_m)=m`.

## Minimum binary count and formula boundary

All `3m` variables are essential, so output-cone connectivity forces at
least `3m-1` binary gates. The equality proof in LEMMA-059 applies verbatim
with `3m` sources: after contracting unary NOT paths, a connected output cone
with `3m` input vertices and `3m-1` binary vertices has one fewer edge than
vertices and is a tree. Expanding the unary paths gives a fan-out-one formula.

Let a circuit have `B` binary gates and `N` NOT gates.

- If `B=3m-1`, the circuit is a formula. Morizumi's formula inversion theorem
  and `d(W_m)=m` give `N>=m`, hence size at least `4m-1`.
- If `B>=3m`, Markov's circuit inversion theorem gives
  `N>=ceil(log_2(m+1))=r`, hence size at least `3m+r`.

This proves the stated minimum. The factorized formula has `3m` clause gates
and `m-1` conjunction gates, so its size is `4m-1`.

For `m<=4`, `r>=m-1`, and the lower bound matches the construction. Starting
at `m=5`, its gap is `m-1-r`, which grows linearly.

## Scope

The theorem closes only four finite standalone cases. It neither proves the
growing identity nor makes standalone size additive over the canonical
GATE-004Z base. It gives no representation-independent semantic quotient
bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits; Boolean-lattice inversion complexity; equality case of fan-in-two connectivity |
| Uniform/non-uniform | Fully non-uniform finite circuits; uniform disjoint signed-triple family and chain witness |
| Circuit size | Lower `min(4m-1,3m+ceil(log_2(m+1)))`, upper `4m-1`; exact for `1<=m<=4` |
| Circuit depth | Unrestricted; formula conclusion only at the minimum binary-gate boundary |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice and graph connectivity only; no algebraic circuit model |
| Asymptotic quantifiers | Every `m>=1`; exact finite cases `m=1,2,3,4`; explicit remaining gap for every `m>=5` |
| Regime | Worst-case exact standalone-function bound; not a base direct sum, quotient theorem, SAT lower bound, or terminal result |
