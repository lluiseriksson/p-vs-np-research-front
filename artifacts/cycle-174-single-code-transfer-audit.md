# Cycle 174 — single-code transfer audit

**Label: PROVED**

LEMMA-208 proves that comparable cofactor specialization can alter exterior
gate functions at one code only. Specializing to `sigma=0` changes at most
the unsatisfying code `10`; specializing to `sigma=1` changes at most the
satisfying code `00`. The proof is an exact topological induction and permits
arbitrary reconvergence.

GATE-004DA-SATISFYING-EXTERIOR-ONLY records the sharp limit for `sigma=0`.
Its explicit gadget transfers `R_0` from `b` to `c`, preserves the parent,
and changes only exterior code `10`.
`verification/single_code_transfer_audit.py` checks all eight assignments and
the exact cofactor-function comparisons; the general LEMMA-208 proof and
displayed witness identities, not the regression, carry the labels.

## Classification

- LEMMA-208: `PROVED`
- GATE-004DA-SATISFYING-EXTERIOR-ONLY: `NO-GO`
- GATE-004DB: `EXPLORATORY`

GATE-004DB must use physical minimum-cost data for `sigma=0`, an exact named
third deletion or factoring for the changed `00` cofactor when `sigma=1`, or
resolve the incomparable branch. No plateau exclusion, SAT lower bound, or
terminal implication is claimed.

## Review boundary

Fable and `fable-bridge` remain disabled and were not invoked. The cycle uses
Codex adversarial review and exact Boolean substitution; no independent
mathematical certification is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-code audit inside the refined unrestricted AND/OR/NOT plateau program |
| Uniform/non-uniform | Every qualifying comparable specialization for LEMMA-208; one finite witness for the no-go |
| Circuit size | No size conclusion from localization; constant nonminimal no-go witness |
| Circuit depth | Unrestricted target; constant witness depth |
| Fan-in | AND/OR two; NOT one; arbitrary exterior reconvergence allowed and shared witness fanout audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every qualifying specialization and exterior gate; all eight witness assignments |
| Regime | Exact semantic theorem plus structural no-go; not terminal progress |
