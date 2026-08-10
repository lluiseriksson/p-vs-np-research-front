# GATE-004Y — signed-triple tail minimality or quotient survival

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical polynomial-size GATE-004X base `H(r,u)` and the
`m=rho*s=P/4` disjoint common signed triples selected in LEMMA-061, put

`F=H AND Q_1 AND ... AND Q_m`.

Exhibit one minimum circuit for `F` whose diagonal joint quotient exceeds the
base contribution by at least

`C(F)-C(H)+m`.

This gives signed diagonal loss at most `K-m`. For the canonical parameters,
`K=o(P)` and `m=P/4`, so it would falsify GATE-004X at all sufficiently large
compatible lengths.

The gate is falsified by a proved canonical-base family on which both
alternatives fail, or by a structural theorem ruling out the demanded
quotient surplus for every minimum representation.

## Current proof attempt

LEMMA-062 sets both negatively occurring inputs in each clause to one and
LEMMA-063 applies global De Morgan sharing. Together they prove

`K+3m<=C(F)<=K+4m+1`.

The clausewise circuit has `6m` tail classes but costs `K+5m` and is provably
nonminimum for `m>=2`. The compressed circuit costs `K+4m+1` and exposes only
`4m+2` tail/output classes, yielding displayed loss `K-1`, not `K-m`.
Neither representation establishes the required minimum-circuit quotient.

## Next attack

Determine whether every minimum circuit must retain at least `m-1` additional
semantic classes beyond the compressed representation, or construct a
minimum representation showing that this is impossible. Any successful
argument must address unrestricted DAG sharing, complement reuse, and the
paired-row quotient directly; treating clauses as black boxes is invalid.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for the canonical GATE-004X base conjoined with the explicit disjoint common signed triples; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Uniform canonical base, witness family, clause selection, and parameters; fully non-uniform minimizing circuits |
| Circuit size | Target loss at most `K-m`; current bracket `K+3m<=C(F)<=K+4m+1`; compressed displayed quotient has only `4m+2` tail/output classes |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean syntax/circuits; affine prefix geometry over `F_2` only in the inherited base rows |
| Asymptotic quantifiers | Fixed sufficiently small `c>0`; every sufficiently large compatible length; `rho,s,m` as in GATE-004X and LEMMA-061; exact statement for the canonical base family |
| Regime | Worst-case exact falsification gate for GATE-004X; not a SAT lower bound and not a terminal result |
