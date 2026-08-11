# LEMMA-153 — deficits are exact negation-cycle resource savings

**Label: PROVED**

Let `H` depend essentially on `h` inputs and have circuit complexity `K`.
For the nested implication functions `J_j` of LEMMA-152, define

`sigma=K-h+1`.

For a pruned circuit `C` for `J_j`, let `N(C)` be its number of NOT gates and
`r(C)` the cycle rank of the undirected output cone. Put

`mu_j=min_C (N(C)+r(C))`.

Then

`C(J_j)=h+2j-1+mu_j`,

`sigma=mu_0`,

and

`Delta_j=sigma+j-mu_j`.

Moreover,

`j<=mu_j<=sigma+j`,

and `mu_j-mu_{j-1}` belongs to `{0,1}`. A unit deficit increase is exactly a
plateau of the minimum negation-cycle resource count.

## Proof

Every input essential to `J_j` occurs in a pruned connected output cone, so
the cone has `h+2j` input vertices. If it contains `B` binary gates and `N`
NOT gates, it has

`V=h+2j+B+N` vertices and `E=2B+N` edges,

counting parallel circuit wires in the undirected multigraph. Connectedness
gives

`r=E-V+1=B-h-2j+1`,

so

`B+N=h+2j-1+(N+r)`.

Minimizing both sides over pruned circuits proves the first identity. At
`j=0` it gives `K=h-1+mu_0`, hence `mu_0=sigma`. Substituting the size identity
into `Delta_j=K+3j-C(J_j)` gives

`Delta_j=sigma+j-mu_j`.

LEMMA-144 proves `Delta_j<=sigma`, equivalently `mu_j>=j`; the displayed
base-plus-tail circuit gives `mu_j<=sigma+j`. Finally LEMMA-152 says the
deficit increment is zero or one, and the displayed identity gives

`mu_j-mu_{j-1}=1-(Delta_j-Delta_{j-1})`,

so the resource increment is respectively one or zero.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted circuits and undirected output-cone cycle rank |
| Uniform/non-uniform | Fully non-uniform exact minima along the uniform nested implication family |
| Circuit size | Exact `C(J_j)=h+2j-1+mu_j` and `Delta_j=sigma+j-mu_j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2` only; computation remains Boolean |
| Asymptotic quantifiers | Every `j>=0`, every nonconstant finite `H`, and every pruned circuit for the corresponding `J_j` |
| Regime | Exact worst-case resource accounting; not resource localization, quotient stability, a SAT lower bound, or a terminal result |
