# GATE-004Z — factorized signed-triple minimality or quotient survival

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical GATE-004X base and the `m=P/4` signed triples from
LEMMA-061, prove at least one exact alternative:

1. the factorized circuit in LEMMA-064 is minimum, so `C(F)=K+4m`, and some
   minimum circuit has at least `5m` active diagonal tail classes; or
2. a minimum circuit has diagonal quotient contribution beyond the base of
   at least `C(F)-K+m`.

Either alternative yields loss at most `K-m` and falsifies GATE-004X for all
sufficiently large compatible parameters. The gate is falsified by a proved
canonical-base family for which both alternatives fail.

## Current attempt

LEMMA-062 proves only `C(F)>=K+3m`, exactly `m` below the factorized upper
bound. Essential-variable restriction therefore consumes the full desired
quotient surplus. As with GATE-004W, clause-local syntax cannot be treated as
an additive black box inside unrestricted DAG circuits.

## Next attack

LEMMA-065 completes the minimum-binary/formula-boundary audit. It proves the
standalone factorized circuit exact only for `m<=4`; from `m=5`, the method
leaves gap `m-1-ceil(log_2(m+1))`. The next attack must control the
binary-for-NOT tradeoff away from equality or bypass standalone size with a
direct minimum-quotient argument over the canonical base. Any result must
audit polarity sharing and semantic quotient classes, not merely count a
particular representation.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for the canonical GATE-004X base conjoined with factorized disjoint signed triples; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Uniform canonical base, clauses, factorization, and parameters; fully non-uniform minimizing circuits |
| Circuit size | Target size `K+4m` or quotient surplus `C(F)-K+m`; current lower bound `K+3m`; displayed quotient `5m` only before minimality |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean syntax/circuits; inherited affine prefix geometry over `F_2` only in the base rows |
| Asymptotic quantifiers | Fixed sufficiently small context exponent; every sufficiently large compatible length; `m=P/4`; exact canonical-base statement |
| Regime | Worst-case exact falsification gate for GATE-004X; not a SAT lower bound or terminal result |
