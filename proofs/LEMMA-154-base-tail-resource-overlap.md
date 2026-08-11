# LEMMA-154 — every deficit unit forces a base-tail shared resource

**Label: PROVED**

Let `C` be a minimum pruned circuit for `J_m`, let `h,K,sigma` be as in
LEMMA-153, and put `d=Delta_m`. Fix any spanning tree `T` of the undirected
output cone. Its resource set `R_T` consists of all NOT gates and all non-tree
edges, so

`|R_T|=N+r=mu_m=sigma+m-d`.

Let `P_i(T)` be the tail dependency neighborhood of clause `i`. Let `B(T)`
be the resources lying on a directed path from an essential base input to the
output. Then there is a Hall matching of the `m` clause indices into `R_T`
whose image intersects `B(T)` in at least `d` resources. Equivalently, at
least `d` distinct clauses are matched to resources that lie in both a tail
dependency cone and a base dependency cone.

## Proof

LEMMA-141, lifted to the joint circuit as in LEMMA-144, gives

`|union_{i in I}P_i(T)|>=|I|`

for every clause subset. Hall's theorem supplies an injection

`f:[m] -> R_T`, `f(i) in P_i(T)`.

Its image `A=f([m])` has size `m`.

Now set every tail clause identically true, propagate constants, and prune.
The residual computes `H`. Every surviving NOT gate and every residual cycle
resource lifts to an original resource on a directed base-input-to-output
path, exactly as in the restriction lifting of LEMMA-116. Since every circuit
for `H` has `N+r>=K-h+1=sigma`, it follows that

`|B(T)|>=sigma`.

Both `A` and `B(T)` lie in the resource universe `R_T`. Therefore

`|A intersection B(T)|>=|A|+|B(T)|-|R_T|`

`>=m+sigma-(sigma+m-d)=d`.

Because `f` is injective, these shared resources correspond to at least `d`
distinct matched clause indices.

## Boundary

The theorem proves overlap, not localization. A resource can lie syntactically
on both base and clause paths yet disappear when other clauses are set true.
GATE-004BA-CONE-MEMBERSHIP-ONLY records why cone membership alone does not
bound the clause support needed to retain the saving.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted circuits, dependency cones, Hall matchings, and NOT/non-tree-edge resources |
| Uniform/non-uniform | Every individual non-uniform minimum circuit and every spanning tree; uniform implication clauses |
| Circuit size | Resource universe `sigma+m-d`; overlap of tail matching and base cone at least `d` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Fundamental cycle resources over `F_2` and finite Hall matching |
| Asymptotic quantifiers | Every `m>=1`, every nonconstant finite base, every minimum pruned `J_m` circuit, and every spanning tree |
| Regime | Exact worst-case overlap theorem; not saving survival, quotient stability, a SAT lower bound, or a terminal result |
