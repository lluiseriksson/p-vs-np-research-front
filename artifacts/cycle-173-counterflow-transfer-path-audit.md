# Cycle 173 — counterflow transfer-path audit

**Label: PROVED**

LEMMA-207 proves that a comparable specialization which preserves the parent
function but fails to lower `R_0` must create a changed path from the original
signal `r` to the other input of a newly counted direct `h`-boundary. This is
an exact semantic localization theorem for finite DAGs.

GATE-004CZ-TRANSFER-PATH-ONLY proves the limitation by a symbolic family. For
every `m>=0`, a chain of `m+1` changed signals transfers the counted
counterflow from `b` to `c` while preserving `b`, `c`, the parent output, and
the total `R_0`. `verification/counterflow_transfer_family_audit.py` checks
every assignment for `0<=m<=6`; the displayed formulas for arbitrary `m`, not
that finite regression, carry the `NO-GO` label.

## Classification

- LEMMA-207: `PROVED`
- GATE-004CZ-TRANSFER-PATH-ONLY: `NO-GO`
- GATE-004DA: `EXPLORATORY`

GATE-004DA must use minimum cost and the exact satisfying-pruning budgets to
charge the first newly counted boundary. Route existence, length, and raw
changed-gate count receive no credit. The incomparable branch remains open.
No plateau exclusion, SAT lower bound, or terminal implication is claimed.

## Review boundary

Fable and `fable-bridge` are disabled by binding owner policy and were not
invoked. The cycle uses Codex adversarial review and exact Boolean
substitution; no independent mathematical certification is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact Boolean cofactor and changed-path audit inside the refined unrestricted AND/OR/NOT plateau program |
| Uniform/non-uniform | Every qualifying comparable transfer for LEMMA-207; one uniform family for every `m>=0` for the no-go |
| Circuit size | No size conclusion from localization; no-go family size linear in `m` and nonminimal |
| Circuit depth | Unrestricted target; no-go depth linear in `m` |
| Fan-in | AND/OR two; NOT one; shared fanout, changed paths, and transferred boundaries audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors and finite DAG reachability |
| Asymptotic quantifiers | Every qualifying finite specialization; every integer `m>=0` and all witness assignments |
| Regime | Exact semantic theorem plus structural no-go; not terminal progress |
