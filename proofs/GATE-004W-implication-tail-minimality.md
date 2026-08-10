# GATE-004W — implication-tail minimality or representation-independent quotient survival

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical polynomial-size GATE-004V base `H(r,u)` and the
`m=(2rho-4)s` disjoint common implications from LEMMA-056, let

`F=H AND Q_1 AND ... AND Q_m`.

Prove at least one of the following exact alternatives:

1. `C(F)=C(H)+3m`, and some minimum circuit realizes at least `4m` active
   diagonal joint-quotient tail classes; or
2. without assuming that displayed circuit is minimum, exhibit one minimum
   circuit for `F` whose diagonal joint quotient has size at least
   `C(F)-C(H)+m` beyond the base contribution.

Either alternative gives diagonal signed loss at most `K-m`. Since the
canonical base has `K=o(P)` for a sufficiently small fixed context exponent
and LEMMA-056 gives `m=P/2-4s=Theta(P)`, it would falsify GATE-004V at
infinitely many compatible lengths.

The theorem is falsified by a proved family of canonical-base instances for
which every minimum circuit has larger loss than the required bound, or by an
exact structural obstruction to both alternatives.

## First proof attempt and quantitative failure

LEMMA-057 applies essential-input gate elimination to all `b_i`. It proves

`K+2m <= C(F) <= K+3m`.

The lower certificate is short by exactly `m`, the same surplus that the
displayed `4m` classes would create. Global minimization is free to remove
those `m` gates and may change the semantic quotient. Thus this restriction
argument does not prove either alternative.

## Next attack

Audit whether the full four-cofactor table of each implication pair forces a
third gate per pair in a disjoint composition, or whether a shared-polarity
construction compresses multiple implications. Any claimed direct-sum step
must be proved for unrestricted DAG circuits and cannot treat the clauses as
black-box gates.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for the canonical GATE-004V base conjoined with the explicit disjoint common implication family; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Uniform base description, witness family, clauses, and parameters; fully non-uniform minimizing circuits |
| Circuit size | Target loss at most `K-m`; current exact bracket `K+2m <= C(F) <= K+3m`, with displayed quotient at least `4m` only before minimality is established |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean syntax/circuits; affine prefix geometry over `F_2` only in the inherited base rows |
| Asymptotic quantifiers | Fixed sufficiently small `c>0`; every sufficiently large compatible length; `rho,s,m` as in GATE-004V and LEMMA-056; exact statement for the canonical base family |
| Regime | Worst-case exact counterexample gate to GATE-004V; not a SAT lower bound and not a terminal result |
