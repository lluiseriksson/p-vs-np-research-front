# GATE-004AK — Hall expansion of sensitive resource neighborhoods

**Label: EXPLORATORY**

## Definitions

Fix a pruned circuit for `W_m` in the unresolved range
`ceil(log_2(m+1))<=N<=m-1`. For each `i`, use the witness pair from LEMMA-115
and let `D_i` contain every node whose Boolean value changes and every circuit
edge joining two such nodes.

Choose a spanning tree `T` of the underlying connected undirected output
cone. Its `t=B-5m+1` non-tree edges are the cycle resources. Define the
resource neighborhood `A_i(T)` to consist of:

- every NOT gate in `D_i`; and
- every non-tree edge of `T` that belongs to `D_i`.

## Falsifiable theorem

Prove that some spanning tree `T` satisfies Hall's inequalities

`|union_{i in I} A_i(T)| >= |I|`

for every subset `I` of clause indices. The theorem is falsified by one
low-N circuit for which every spanning tree violates one inequality.

Hall's theorem would give an injection into the `N+t` NOT-or-cycle resources,
proving `m<=N+t` and therefore GATE-004AJ/AI/AH. LEMMA-115 proves only the
singleton inequalities: each `A_i(T)` contains a NOT on a sensitive odd-NOT
path. Expansion for larger index sets is the open collision bound.

## Scope control

The low-N hypothesis is essential to the proposed theorem. The range-free
version is false by the explicit De Morgan formula in the companion no-go.
Thus a proof must use the quantitative negation budget, not only the function's
local sensitivity semantics.

GATE-004AL broadens the neighborhoods to every resource in the full directed
dependency cone of a block. LEMMA-116 proves the resulting Hall inequalities
through subset size four. This supersedes singleton-sensitive incidence as
the active route; size five is the first unresolved dependency-cone case.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits, assignment-sensitive subgraphs, spanning trees, and fundamental cycle resources |
| Uniform/non-uniform | Every individual non-uniform circuit in the low-N range; uniform witness pairs |
| Circuit size | Hall target yields `m<=N+t` and exactly the standalone `B+N>=6m-1` bound |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2`; Boolean sensitivity incidence |
| Asymptotic quantifiers | Every `m>=5`, every pruned circuit with `ceil(log2(m+1))<=N<=m-1`, and every subset of clause indices |
| Regime | Exact worst-case Hall gate; not a base direct sum, SAT lower bound, or terminal result |
