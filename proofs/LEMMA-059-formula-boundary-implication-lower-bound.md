# LEMMA-059 — the formula boundary makes one through four implications exact

**Label: PROVED**

## Statement

For

`W_m=AND_{i=1}^m (a_i OR NOT b_i)`,

let `r=ceil(log_2(m+1))`. Then

`C(W_m)>=min(3m-1,2m+r)`

and `C(W_m)<=3m-1`. Consequently

`C(W_m)=3m-1` for `m=1,2,3,4`.

For `m>=5`, this combined certificate leaves gap

`m-1-r`

below the displayed circuit.

## Equality in binary connectivity forces a formula

Every `W_m` input is essential, so LEMMA-058 gives at least `2m-1` binary
gates. Consider an output cone with exactly `2m-1` binary gates. Contract each
maximal path of unary NOT gates. The resulting directed acyclic multigraph has
`2m` essential input sources, `2m-1` binary vertices, and exactly
`2(2m-1)` incoming edges at binary vertices.

Its underlying undirected multigraph is connected because every essential
input reaches the output. It has

`(2m)+(2m-1)=4m-1`

vertices and `4m-2` edges, exactly one fewer edge than vertices. Therefore it
is a tree. In particular it has no reconvergent fanout, repeated binary input,
or shared unary branch. Expanding the contracted NOT paths shows that the
original output cone is a fan-out-one formula.

## Two-case lower bound

Let a circuit for `W_m` have `B` binary and `N` NOT gates.

- If `B=2m-1`, the preceding argument makes it a formula. The increasing
  chain from LEMMA-058 has `m` decreases. Morizumi's formula inversion theorem
  gives `N>=m`, hence `B+N>=3m-1`.
- If `B>=2m`, Markov's circuit inversion theorem gives `N>=r`, hence
  `B+N>=2m+r`.

Every circuit falls into one case, proving the minimum of the two bounds.
The direct clause-and-conjunction circuit has size `3m-1`.

For `m<=4`, `m-1<=ceil(log_2(m+1))`, so the first term is the smaller or equal
lower bound and matches the upper bound. For `m>=5`, the second term is
smaller and the displayed gap is `m-1-r`. QED.

## Scope

This settles two more finite standalone cases but does not prove the growing
identity, additivity relative to the GATE-004W base, or semantic quotient
survival. No finite exact case is promoted to asymptotic evidence.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits; equality case of fan-in-two connectivity; Markov circuit and Morizumi formula inversion complexity |
| Uniform/non-uniform | Fully non-uniform finite circuits; uniform implication family and chain witness |
| Circuit size | Lower `min(3m-1,2m+ceil(log_2(m+1)))`, upper `3m-1`; exact for `1<=m<=4` |
| Circuit depth | Unrestricted; formula conclusion is derived only in the minimum-binary-gate case |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice and graph connectivity only; no algebraic circuit model |
| Asymptotic quantifiers | Every `m>=1`; exact finite cases `m=1,2,3,4`; explicit remaining gap for every `m>=5` |
| Regime | Worst-case exact standalone-function bound; not a base direct sum, quotient theorem, or SAT lower bound |
