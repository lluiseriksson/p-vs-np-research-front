# LEMMA-108 — the three-block slots retain a fixed-sign width-five packing

**Label: PROVED**

Under the hypotheses of LEMMA-076, every distant quintuple `Q_i` admits a
common signed width-five clause with exactly four positive literals and one
negative literal. Consequently there are `floor(N/5)` pairwise
variable-disjoint clauses of this sign type in each sufficiently long slot.

Every ordinary option has zeros on at most three coordinates of `Q_i`.
Therefore it omits all five assignments having exactly four zeros. The one
exceptional option realizes at most one of those five assignments, leaving at
least four absent from the entire option family. Choose any absent assignment
deterministically. The clause falsified by it has a positive literal at each
of its four zero coordinates and one negative literal at its sole one
coordinate. The quintuples are disjoint, so the selected clauses are
variable-disjoint.

For the LEMMA-075 slot family, `B=68` and the exceptional option is `A_rho`.
An independent `s`-slot product therefore has
`m=s*floor(N/5)=Theta(P)` disjoint common clauses of the required sign type.
This refines the sign information in LEMMA-076 but makes no circuit claim.

## Model card

| Field | Value |
|---|---|
| Computational model | Binary option families, three bounded zero intervals, one exceptional option, fixed-sign signed width-five clauses, and matching |
| Uniform/non-uniform | Uniform distant quintuples and deterministic absent-pattern selection; arbitrary qualifying option family |
| Circuit size | No lower bound; fixed-sign common width-five packing at least `floor(N/5)` per slot |
| Circuit depth | Later circuits unrestricted |
| Fan-in | Clause OR binarized to two; one literal uses NOT fan-in one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Every `N,B` with `floor(N/5)>=B`, every qualifying option family, and every `s>=1` in the slot-product application |
| Regime | Exact worst-case combinatorial witness theorem; not a circuit lower bound or terminal result |
