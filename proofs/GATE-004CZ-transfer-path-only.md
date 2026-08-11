# GATE-004CZ-TRANSFER-PATH-ONLY — transfer paths can be arbitrarily long

**Label: NO-GO**

LEMMA-207 localizes every failed comparable `R_0` descent to a path of changed
signals. The existence, length, or changed-gate count of that path alone does
not force a circuit-size or satisfying-minor charge.

For every integer `m>=0`, use raw inputs `x,y,u,t,z_1,...,z_m` and define

`g=u OR x`, `h=g AND y`,

`a=u OR t`, `v=NOT a`, `r=x OR v`, and `b=h AND r`.

Let

`q_0=r OR u`

and, for `1<=i<=m`,

`q_i=q_{i-1} AND z_i`.

Finally set `c=h AND q_m` and `o=b OR c`. Specializing the region `{a,v,r}`
to `u=1` replaces `r` by `x`. Write `Z_i=z_1 AND ... AND z_i`, with
`Z_0=1`. Before specialization the four-code signature of every `q_i` is

`(Z_i,Z_i,x AND Z_i,Z_i)`;

after specialization it is

`(x AND Z_i,Z_i,x AND Z_i,Z_i)`.

The two functions differ for every `i`: take `x=0` and all relevant `z_j=1`.
Thus

`r -> q_0 -> q_1 -> ... -> q_m`

is a changed path of length `m+1`.

Nevertheless `b` is unchanged with all cofactors `x AND y`, and both before
and after specialization

`(c_00,c_10,c_01,c_11)`

equals

`(x AND y AND Z_m, y AND Z_m, x AND y AND Z_m, y AND Z_m)`.

Hence `c`, `o`, and the parent function are unchanged. The counted boundary
again transfers exactly: `b` loses the unequal row-zero pair `(1,x)`, while
`c` gains `(x AND Z_m,Z_m)`. Therefore `R_0` stays constant for every `m`.

This is an algebraic family, not an inference from a finite experiment. Each
member is nonminimal and not a plateau parent. It refutes only arguments that
charge transfer-path existence, depth, or number of changed gates without
using minimum cost, the exact pruning budgets, or additional topology.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit family of finite unrestricted AND/OR/NOT shared-fanout DAGs |
| Uniform/non-uniform | One uniform construction for every integer `m>=0`; each circuit is a finite non-uniform witness |
| Circuit size | Linear in `m`; every member is nonminimal and gives no lower bound |
| Circuit depth | Linear in `m`; changed path has length `m+1` |
| Fan-in | AND/OR two; NOT one; `r` has two live consumers and the transfer chain has fanout one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors and symbolic conjunctions `Z_i` |
| Asymptotic quantifiers | Every integer `m>=0` and every assignment to `x,y,u,t,z_1,...,z_m` |
| Regime | Transfer-path-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |
