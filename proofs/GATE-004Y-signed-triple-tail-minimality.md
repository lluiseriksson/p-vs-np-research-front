# GATE-004Y — signed-triple tail minimality or quotient survival

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical polynomial-size GATE-004X base `H(r,u)` and the
`m=rho*s=P/4` disjoint common signed triples selected in LEMMA-061, put

`F=H AND Q_1 AND ... AND Q_m`.

Prove at least one of the following exact alternatives:

1. `C(F)=C(H)+5m`, and some minimum circuit realizes at least `6m` active
   diagonal joint-quotient tail classes; or
2. without assuming the displayed circuit minimum, exhibit one minimum
   circuit for `F` whose diagonal joint quotient exceeds the base
   contribution by at least `C(F)-C(H)+m`.

Either alternative gives signed diagonal loss at most `K-m`. For the
canonical parameters, `K=o(P)` and `m=P/4`, so it would falsify GATE-004X at
all sufficiently large compatible lengths.

The gate is falsified by a proved canonical-base family on which both
alternatives fail, or by a structural theorem ruling out the demanded
quotient surplus for every minimum representation.

## Current proof attempt

LEMMA-062 sets both negatively occurring inputs in each clause to one. It
proves

`K+3m<=C(F)<=K+5m`.

The displayed upper circuit has the desired `6m` tail classes, but the lower
certificate is short by `2m`. Global minimization can use this entire slack
and need not preserve the displayed gates or their semantic classes.

## Next attack

Classify the standalone conjunction of the two permitted signed-triple types
by binary-gate connectivity and inversion complexity, then audit whether any
standalone bound is additive over the canonical base. A successful argument
must address unrestricted DAG sharing and complement reuse; treating clauses
as black boxes is invalid.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for the canonical GATE-004X base conjoined with the explicit disjoint common signed triples; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Uniform canonical base, witness family, clause selection, and parameters; fully non-uniform minimizing circuits |
| Circuit size | Target loss at most `K-m`; current bracket `K+3m<=C(F)<=K+5m`, with displayed quotient at least `6m` only before minimality is established |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean syntax/circuits; affine prefix geometry over `F_2` only in the inherited base rows |
| Asymptotic quantifiers | Fixed sufficiently small `c>0`; every sufficiently large compatible length; `rho,s,m` as in GATE-004X and LEMMA-061; exact statement for the canonical base family |
| Regime | Worst-case exact falsification gate for GATE-004X; not a SAT lower bound and not a terminal result |
