# LEMMA-109 — the formula boundary closes four one-negative tail cases

**Label: PROVED**

For pairwise-disjoint inputs, put

`W_m = AND_{i=1}^m (NOT u_i OR v_{i,1} OR ... OR v_{i,p})`

for fixed `p>=1`, and let `r=ceil(log_2(m+1))`. Then

`C(W_m) >= min((p+2)m-1,(p+1)m+r)`

and `C(W_m)<=(p+2)m-1`. Consequently the displayed circuit is exact for
`1<=m<=4`. For `p=4`,

`min(6m-1,5m+r) <= C(W_m) <= 6m-1`.

For every `m>=5`, these measures leave the explicit gap `m-1-r`.

## Exact inversion decrease

Along an increasing Boolean-lattice chain, one clause can fall from one to
zero at most once: this happens only when `u_i` rises while all its positive
variables remain zero. Once any positive variable rises, that clause remains
one. Every decrease of the conjunction contains a decrease of some clause,
so `d(W_m)<=m`.

Equality is attained. Start with all inputs zero. For each `i`, first raise
`u_i`, making the conjunction fall, and then raise `v_{i,1}`, making it rise.
Previously repaired clauses remain one and future clauses remain one because
their `u` input is zero. Hence `d(W_m)=m`.

## Binary connectivity and formula boundary

All `(p+1)m` raw inputs are essential. Therefore the output cone contains at
least `(p+1)m-1` binary gates. If equality holds, contract maximal NOT paths.
The resulting connected graph has `(p+1)m` input sources and exactly one
fewer binary merger than sources, hence one fewer edge than vertices. It is a
tree, so expanding the unary paths gives a fan-out-one formula.

Let a circuit have `B` binary and `N` NOT gates.

- If `B=(p+1)m-1`, the formula conclusion and Morizumi's formula inversion
  theorem give `N>=d(W_m)=m`, hence total size at least `(p+2)m-1`.
- If `B>=(p+1)m`, Markov's circuit inversion theorem gives
  `N>=ceil(log_2(m+1))=r`, hence total size at least `(p+1)m+r`.

The direct circuit uses `p+1` gates per clause and `m-1` conjunction gates,
for `(p+2)m-1`. Since `r>=m-1` exactly for `m<=4`, the bounds match in those
four cases. Starting at `m=5`, the remaining gap is `m-1-r`, which grows
linearly.

## Scope

This proves four finite standalone cases and a quantitative asymptotic
barrier. It does not prove additive composition with the GATE-004AG base or
representation-independent quotient survival.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits; Boolean-lattice inversion complexity; equality case of fan-in-two connectivity |
| Uniform/non-uniform | Fully non-uniform finite circuits; uniform disjoint one-negative clause family and chain witness |
| Circuit size | Lower `min((p+2)m-1,(p+1)m+ceil(log_2(m+1)))`, upper `(p+2)m-1`; exact for `1<=m<=4` |
| Circuit depth | Unrestricted; formula conclusion only at the minimum binary-gate boundary |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice and graph connectivity only; no algebraic circuit model |
| Asymptotic quantifiers | Every fixed `p>=1` and every `m>=1`; exact finite cases `m=1,2,3,4`; explicit remaining gap for every `m>=5` |
| Regime | Worst-case exact standalone-function bound; not a base direct sum, quotient theorem, SAT lower bound, or terminal result |
