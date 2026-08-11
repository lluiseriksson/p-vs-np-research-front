# Cycle 175 — strict specialization saving audit

**Label: PROVED**

LEMMA-209 proves the missing quantitative fact for a `u`-isolated region:
when its output depends essentially on raw `u`, fixing either value of `u`
removes the first gate on a path from `u` to the output. Full AND/OR/NOT
constant propagation adds no gate. If the selected cofactor is nonconstant,
the resulting constant-free region therefore has at most `|S|-1` gates; if it
is constant, propagation through the cancelling boundary also strictly saves.

This strengthens LEMMA-205 and LEMMA-206 from an equal-size potential descent
to an immediate minimum-size contradiction. It also audits LEMMA-207: every
parent-preserving transfer satisfying its isolation interface is necessarily
nonminimal. NG-150, NG-151, and NG-152 remain valid diagnostics but cannot be
minimum-parent witnesses.

## Classification

- LEMMA-209: `PROVED`
- GATE-004DC: `EXPLORATORY`

GATE-004DC retains only edge-local comparable erasure where global
specialization is unavailable or output-changing, plus incomparable erasure.
No unrestricted SAT lower bound or terminal implication is claimed.

## Review boundary

The proof was audited directly in the constant-free AND/OR/NOT basis. Fable
and `fable-bridge` are disabled and were not invoked. No independent
mathematical certification or formal verification is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite constant-free unrestricted AND/OR/NOT DAG regions inside the refined plateau program |
| Uniform/non-uniform | Every finite non-uniform isolated region satisfying LEMMA-209; every hypothetical residual endpoint for GATE-004DC |
| Circuit size | Nonconstant specialization saves at least one region gate; residual gate still requires an exact `K+2` exchange or contradiction |
| Circuit depth | Unrestricted; propagation may reduce depth and residual shared escapes may be arbitrarily deep |
| Fan-in | AND/OR two; NOT one; raw `u` and residual physical signals may have unrestricted fanout |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restriction, constant propagation, pointwise meet/join, and physical DAG topology |
| Asymptotic quantifiers | Both values of `u`, every qualifying finite region, and every hypothetical residual counterflow boundary |
| Regime | Exact local gate-saving theorem and residual design gate; not a SAT lower bound or terminal result |
