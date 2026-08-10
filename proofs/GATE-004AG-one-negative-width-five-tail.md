# GATE-004AG — one-negative width-five tail minimality or quotient survival

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical GATE-004AE base `H` and the
`m=s*floor(N/5)=Theta(P)` disjoint common clauses from LEMMA-108, let

`F = H AND Q_1 AND ... AND Q_m`,

where every `Q_i` has four positive literals and one negative literal. Because
every `Q_i` is common to the LEMMA-075 slot product, `F` agrees with the base
`H` on every canonical witness used by GATE-004AE. Prove at least one exact
alternative:

1. the LEMMA-107 upper circuit is minimum, so `C(F)=C(H)+6m`, and some
   minimum circuit has at least `7m` active diagonal tail classes; or
2. a minimum circuit has diagonal quotient contribution beyond the base of
   at least `C(F)-C(H)+m`.

Either alternative gives signed diagonal loss at most `K-m`. In the canonical
parameter regime `K=o(P)` and `m=Theta(P)`, so it would falsify GATE-004AE for
all sufficiently large compatible lengths. A proof that both alternatives
fail on the canonical base falsifies this gate.

## First attempt

LEMMA-107 proves only

`K+5m <= C(F) <= K+6m`.

The displayed upper circuit has `7m` tail classes, but the lower certificate
is short by exactly `m`, the entire surplus needed for negative loss. Global
minimization may remove those gates and merge their semantic classes. The
essential-variable restriction route therefore does not prove either
alternative.

LEMMA-109 next audits the binary-gate/negation tradeoff. It proves the
standalone displayed circuit exact for `m<=4`, but its combined connectivity
and inversion certificate has linear gap
`m-1-ceil(log_2(m+1))` from `m=5`. The next attack must constrain this tradeoff
away from the formula boundary or establish quotient survival directly for a
minimum circuit over the canonical base. Clause-local syntax cannot be
assumed additive inside an unrestricted DAG.

LEMMA-110 resolves the first DAG stratum: with one extra binary gate, the
output graph is unicyclic and formula unfolding forces at least `ceil(m/2)`
NOT gates. The factor-two loss remains linear and does not close the gate.
The active structural question is now the general cycle-rank tradeoff between
extra binary gates, unfolding multiplicity, and required negations.

LEMMA-111 completes that tradeoff for every DAG and every binary-gate count.
Its optimized surplus is only `g(m)=Theta(log m)`, leaving linear gap to the
displayed circuit. Pure unfolding is therefore exhausted. The next attack
must exploit the particular distribution of the `u_i` negative variables
through reconvergent subgraphs or bypass size minimality with a direct
semantic quotient theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted Boolean circuits for the canonical GATE-004AE base conjoined with disjoint four-positive/one-negative width-five clauses; exact diagonal semantic quotients |
| Uniform/non-uniform | Uniform canonical witnesses and clause selection; fully non-uniform minimizing circuits |
| Circuit size | Target size `K+6m` or quotient surplus `C(F)-K+m`; proved bracket `K+5m<=C(F)<=K+6m`; displayed quotient `7m` only before minimality |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean circuits; inherited affine prefix geometry over `F_2` only in the base rows |
| Asymptotic quantifiers | Every sufficiently large compatible canonical parameter choice with `m=s*floor(N/5)` and the LEMMA-108 clause family |
| Regime | Worst-case exact falsification gate for GATE-004AE; not a SAT lower bound or terminal result |
