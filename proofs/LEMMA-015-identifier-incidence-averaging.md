# LEMMA-015 — identifier-incidence averaging

**Label: PROVED**

## Statement

Let an `S`-gate parent circuit have a finite nonempty family `J` of paired
restrictions. For each `j in J`, jointly quotient the two restricted copies
and let `q_j` be the number of surviving semantic residual classes. Assign
each class to one parent-gate label appearing in it, as in LEMMA-013, and let
`r_{v,j} in {0,1,2}` be the number of classes assigned to label `v`.

Define the signed incidence entry and row score

`a_{v,j}=1-r_{v,j}` and `A_v=sum_{j in J} a_{v,j}`.

Then

`sum_{j in J}(S-q_j)=sum_v A_v`.

Consequently, for every real `L`, if

`sum_v A_v >= |J| L`,

then at least one `j in J` satisfies `q_j<=S-L`.

## Model card

| Field | Value |
|---|---|
| Computational model | Acyclic Boolean parent circuit; finitely many pairs of restrictions; exact joint semantic residual quotients |
| Uniform/non-uniform | Fully non-uniform semantic classification and arbitrary fixed representatives |
| Circuit size | Exact aggregate identity and an averaging implication |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one in the intended application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer incidence counting only |
| Asymptotic quantifiers | Every finite parent circuit, every finite nonempty restriction family, every representative assignment, and every real threshold `L` |
| Regime | Worst-case exact multi-output circuit computation |

## Proof

For each fixed `j`, LEMMA-013 gives

`S-q_j=sum_v(1-r_{v,j})=sum_v a_{v,j}`.

Summing over `j` and exchanging the two finite sums proves the identity. If
every column had `q_j>S-L`, then every `S-q_j<L`, so their sum would be
strictly less than `|J|L`. The displayed aggregate lower bound therefore
forces at least one column with `q_j<=S-L`. QED.

## Scope

The identity does not assert that the aggregate is positive. It converts the
many-identifier route into an explicit row-charging obligation: positive
disappearance incidences must exceed negative split incidences by the full
average target.
