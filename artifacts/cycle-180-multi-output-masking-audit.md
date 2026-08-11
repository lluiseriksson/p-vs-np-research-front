# Cycle 180 — multi-output masking audit

**Label: PROVED**

LEMMA-214 proves that specializing a jointly masked multi-output region removes
every gate directly consuming raw `u`, while sharing all residual cofactor
computation and adding no exterior gate. This strictly generalizes the
single-output consumer-masked exchange.

GATE-004DG-ENTRY-COUNT-ONLY gives the quantitative limit. Its marked region
has outputs `k,r`, one raw-`u` entry, and live consumers `c=u AND k` and `b`.
Both consumers are unchanged by the `u=1` cofactor replacement, but the
private deficit is `n-2`. Thus entry multiplicity is not the required semantic
cost.

## Classification

- LEMMA-214: `PROVED`
- GATE-004DG-ENTRY-COUNT-ONLY: `NO-GO`
- GATE-004DH: `EXPLORATORY`

GATE-004DH asks for the full minimum joint cofactor-circuit saving rather than
an interface count. No SAT lower bound or terminal implication is claimed.

## Review boundary

`verification/multi_output_masked_audit.py` checks the family identities and
both masked consumers for `n=3,...,8`. The general gate-saving proof and exact
formula lower bound are human arguments. Fable and `fable-bridge` were not
invoked. No independent mathematical certification or formal verification is
claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite unrestricted AND/OR/NOT multi-output exchange plus an explicit uniform single-output family |
| Uniform/non-uniform | Every supplied masked finite region; one uniform family for every `n>=3`, each member non-uniform |
| Circuit size | Exchange saves at least `d`; family has `3n+11` gates, `d=1`, and `D_b=n-2` |
| Circuit depth | Unrestricted theorem; family depth linear in `n` |
| Fan-in | AND/OR two; NOT one; arbitrary region fanout and two marked output consumers |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean cofactors, shared multi-output specialization, and formula leaf counting |
| Asymptotic quantifiers | Every qualifying region and output occurrence; every `n>=3` and every family assignment |
| Regime | Exact sufficient exchange plus entry-count no-go; not a SAT lower bound or terminal result |
