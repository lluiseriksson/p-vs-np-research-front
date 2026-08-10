# LEMMA-020 — global quotient sharing is not pairwise improvement

**Label: PROVED**

## Statement

Let an `S`-gate parent circuit have a finite nonempty family `J` of paired
restrictions. For each `j`, let `A_j` be the set of active semantic residual-
function classes in that pair's normalized joint quotient and put
`q_j=|A_j|`. Quotient all restricted copies from all pairs together and let

`Q=|union_{j in J} A_j|`.

For each global class `f`, let `m_f` be the number of pairs whose set contains
it, and define the cross-pair overlap

`X=sum_f (m_f-1)=sum_j q_j-Q`.

Then

`sum_j(S-q_j)=|J|S-Q-X`.

In particular, a small global quotient `Q` does not imply a positive average
pairwise improvement unless the overlap term `X` is also accounted for.

## Model card

| Field | Value |
|---|---|
| Computational model | One acyclic Boolean parent circuit; finitely many paired restrictions; exact pairwise and globally pooled semantic quotients |
| Uniform/non-uniform | Fully non-uniform semantic classification |
| Circuit size | Exact identity separating global class count from cross-pair overlap multiplicity |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one in the intended application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set and integer multiplicity counting only |
| Asymptotic quantifiers | Every finite parent circuit and every finite nonempty family of restriction pairs |
| Regime | Worst-case exact multi-output circuit computation |

## Proof

Double-count the incidences `(j,f)` with `f in A_j`. Their number is both
`sum_j q_j` and `sum_f m_f`. Since the number of distinct global classes is
`Q=sum_f 1`, subtraction gives

`X=sum_f(m_f-1)=sum_j q_j-Q`.

Substitute `sum_j q_j=Q+X` into
`sum_j(S-q_j)=|J|S-sum_j q_j` to obtain the identity. QED.

## Extremal shared-core example

Let `F(x,z)=G(z)` ignore every designated prefix input, and use a minimum
irredundant circuit for a nonconstant `G` with `S` active gate classes. Under
every restriction pair, `A_j` is the same `S`-element class set. Thus

`q_j=S` for all `j`, `Q=S`, and `X=(|J|-1)S`.

The globally pooled quotient saves `(|J|-1)S` copies, yet the left side of the
identity is zero: no individual pair improves on the parent at all.

## Scope

The lemma does not say that SAT-gamma has maximal cross-pair overlap. It blocks
crediting sharing between different candidate identifiers as though that
sharing occurred inside one candidate pair. A SAT-specific proof may still
bound `Q+X=sum_j q_j` directly.
