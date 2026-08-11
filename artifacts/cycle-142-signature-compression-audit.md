# Cycle 142 — signature-compression audit

**Label: PROVED**

LEMMA-175 shows that one surviving NOT and only three selector-dependent gates
can mix arbitrarily many tail variables between two primary cofactors.
Consequently changed clause signatures cannot be injected into
selector-dependent resources.

GATE-004BU-SIGNATURE-COUNT-ONLY records this inference as `NO-GO`, consistent
with the earlier selector-mobility audit. GATE-004BV is opened for the exact
remaining route: a size-preserving normal-form exchange exposing one uniform
neutral NOT or cycle path.

## Classification

- LEMMA-175: `PROVED`
- GATE-004BU-SIGNATURE-COUNT-ONLY: `NO-GO`
- GATE-004BV: `EXPLORATORY`
- GATE-004BU: remains `EXPLORATORY`
