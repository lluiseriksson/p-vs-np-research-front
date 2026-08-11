# Cycle 177 — basis-two boundary audit

**Label: PROVED**

LEMMA-211 gives a physical payment for one missing independent factor. When
the counterflow input gate has fanout one and the unchanged boundary output
has a two-gate formula whose inner function is independent of both fresh
inputs, the input vertex computes the inner gate and `b` computes the outer
gate. Size does not increase, earlier potentials do not increase, and the
counted direct `h`-boundary disappears.

GATE-004DD-COMPARABILITY-BASIS-TWO-ONLY supplies the sharp semantics-only
limit. Its six-input DAG has a comparable defect confined to `00/10`, a
fanout-one counterflow input, and boundary output `xyz OR w`. The exact
independent predecessor pool is `x,y,z,w,t,NOT t`; every two-gate formula over
that pool has at most three leaves, while the output depends essentially on
four base variables. The witness is nonminimal and therefore does not refute
minimum-cost factor forcing.

## Classification

- LEMMA-211: `PROVED`
- GATE-004DD-COMPARABILITY-BASIS-TWO-ONLY: `NO-GO`
- GATE-004DE: `EXPLORATORY`

GATE-004DE retains deep or unaligned factors, raw/shared counterflow inputs,
and incomparable cofactors. No SAT lower bound or terminal implication is
claimed.

## Review boundary

`verification/free_basis_two_realization_audit.py` checks all 64 assignments,
the exact independent pool, and all 220 distinct radius-two functions it
generates. The human proof and essential-variable argument carry the labels.
Fable and `fable-bridge` were not invoked. No independent mathematical
certification or formal verification is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined unrestricted AND/OR/NOT endpoint plus one explicit finite nonminimal witness |
| Uniform/non-uniform | Every endpoint with the aligned-inner basis-two/expendable-input certificate; one uniform six-input witness for the no-go |
| Circuit size | Two physical gates are repurposed with no increase; witness has thirteen gates and makes no minimum claim |
| Circuit depth | Unrestricted target; constant witness depth |
| Fan-in | AND/OR two; NOT one; certificate input and witness `r` have fanout one to `b` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities, basis distance, essential-variable counting, and physical rewiring |
| Asymptotic quantifiers | Every qualifying endpoint certificate; all 64 witness assignments and every radius-two formula over six independent predecessors |
| Regime | Exact sufficient exchange plus bounded-basis no-go; not a SAT lower bound or terminal result |
