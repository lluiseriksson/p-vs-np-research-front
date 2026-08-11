# Cycle 172 — consumer-masked counterflow audit

**Label: PROVED**

LEMMA-206 extends the exact comparable-cofactor descent from a private output
to shared fanout whose secondary direct consumers are all functionally
unchanged by the selected specialization. The proof preserves basis cost,
audits every outgoing edge, and uses a topological induction to keep the
remainder of the DAG unchanged.

GATE-004CY-TERMINAL-OUTPUT-ONLY supplies the sharp limitation. In its explicit
gadget, global specialization preserves the parent output and both displayed
`h`-boundary functions, but changes an intermediate consumer from row-zero
signature `(1,1)` to `(x,1)`. The counted counterflow moves from `b` to `c`,
so `R_0` stays constant. `verification/counterflow_transfer_audit.py` checks
all 16 assignments and the four cofactor-function comparisons; the human
substitution proofs, not the regression, carry the labels.

## Classification

- LEMMA-206: `PROVED`
- GATE-004CY-TERMINAL-OUTPUT-ONLY: `NO-GO`
- GATE-004CZ: `EXPLORATORY`

The residual theorem must charge the first unmasked direct consumer or the
two nonzero witness regions of incomparable cofactors. No plateau exclusion,
SAT lower bound, or terminal implication is claimed.

## Independent review

An independent Fable High pass was considered but no mathematical prompt was
sent because the selected local profile was unauthenticated. The owner then
ended Fable usage for this front. The cycle therefore relies on Codex's
adversarial self-audit and the exact finite regression; no second-model
validation is claimed or required as a workflow dependency.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact Boolean cofactor audit inside the refined unrestricted AND/OR/NOT plateau program |
| Uniform/non-uniform | Every consumer-masked comparable certificate for the proof; one finite witness for the no-go |
| Circuit size | No gate increase in LEMMA-206; constant nonminimal no-go witness |
| Circuit depth | Unrestricted target; constant witness depth |
| Fan-in | AND/OR two; NOT one; shared fanout and every immediate consumer audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean cofactors; no algebraic circuit model |
| Asymptotic quantifiers | Every qualifying certificate for LEMMA-206; all 16 witness assignments for the regression |
| Regime | Exact worst-case sufficient theorem plus structural no-go; not terminal progress |
