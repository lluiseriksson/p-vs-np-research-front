# Cycle 189 — local defect-cancellation audit

**Label: PROVED**

LEMMA-224 gives exact `F_2` identities for propagating an old/new code-`10`
defect through NOT, AND, and OR. NOT preserves the defect. With one unchanged
binary input, cancellation is exactly support masking; with two changed inputs
the interaction terms must be retained.

GATE-004DP-CANCELLATION-GATE-ONLY is `NO-GO` (NG-165): an explicit
constant-free fragment has a genuine first OR-mask cancellation and unchanged
nonconstant parent but is deliberately redundant and supplies no automatic
endpoint payment. GATE-004DQ asks for a minimum-cost payment in the one-sided
branch or a physical reconvergence contradiction in the two-sided branch.

## Classification

- LEMMA-224: `PROVED`
- GATE-004DP-CANCELLATION-GATE-ONLY: `NO-GO`
- GATE-004DQ: `EXPLORATORY`

`verification/local_defect_cancellation_audit.py` checks all 16 local
`(a,b,alpha,beta)` states and all 16 assignments of the mask witness. The
general identities also have the displayed algebraic proof. Fable was not
invoked; independent certification and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Local paired AND/OR/NOT interfaces plus one finite single-output cancellation witness |
| Uniform/non-uniform | Every local Boolean state; one finite non-uniform diagnostic circuit |
| Circuit size | One local gate; diagnostic old circuit six gates |
| Circuit depth | One local layer; diagnostic depth at most five |
| Fan-in | AND/OR two; NOT one; unrestricted ambient fanout |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions and analytical difference identities over `F_2` |
| Asymptotic quantifiers | Every local state and every diagnostic assignment |
| Regime | Exact local theorem and cancellation-only no-go; not a SAT lower bound or terminal result |
