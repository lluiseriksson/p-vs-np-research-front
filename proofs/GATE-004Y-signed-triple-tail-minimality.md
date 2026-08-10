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

LEMMA-062 sets both negatively occurring inputs in each clause to one, while
LEMMA-064 factors each clause locally. Together they prove

`K+3m<=C(F)<=K+4m`.

The factorized circuit has `5m` tail classes and would give loss `K-m` if
minimum. But the lower certificate is short by `m`, and minimum-circuit
quotient survival is unproved. GATE-004Z isolates this concrete alternative.
The separate global De Morgan circuit of LEMMA-063 exposes only `4m+2`
tail/output classes, illustrating representation instability.

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
| Circuit size | Target loss at most `K-m`; current bracket `K+3m<=C(F)<=K+4m`; factorized displayed quotient at least `5m`, but only before minimality is established |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean syntax/circuits; affine prefix geometry over `F_2` only in the inherited base rows |
| Asymptotic quantifiers | Fixed sufficiently small `c>0`; every sufficiently large compatible length; `rho,s,m` as in GATE-004X and LEMMA-061; exact statement for the canonical base family |
| Regime | Worst-case exact falsification gate for GATE-004X; not a SAT lower bound and not a terminal result |
