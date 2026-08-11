# Cycle 184 — oriented loss-budget audit

**Label: PROVED**

LEMMA-218 deducts the exact carrier losses before counting residual pruning
resources. The AND→OR carrier leaves at most two distinct gates; the OR→AND
carrier leaves at most four. GATE-004DK-SIX-UNCHARGED-LOSSES-ONLY records the
six-budget accounting failure.

## Classification

- LEMMA-218: `PROVED`
- GATE-004DK-SIX-UNCHARGED-LOSSES-ONLY: `NO-GO`
- GATE-004DL: `EXPLORATORY`

GATE-004DL asks for the aligned circuit deficit to fit the orientation-specific
residual or forces distinct external resources. No SAT lower bound or terminal
implication is claimed.

`verification/oriented_loss_budget_audit.py` enumerates finite two-set
configurations and confirms residual maxima two and four. The endpoint theorem
is the human deduction from LEMMA-193. Fable was not invoked; independent
certification is not performed.

## Model card

| Field | Value |
|---|---|
| Computational model | Size-three exact-plateau unrestricted AND/OR/NOT physical loss sets |
| Uniform/non-uniform | Every endpoint orientation; finite set regression |
| Circuit size | Residual loss union at most two or four after charging `{g,h}` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite physical set union |
| Asymptotic quantifiers | Every endpoint loss triple in both carrier orientations |
| Regime | Exact residual cap plus accounting no-go; not a SAT lower bound or terminal result |
