# Cycle 197 — exact diagonal joint-port cost

**Label: PROVED**

LEMMA-236 proves the universal coordinate-output lower bound and characterizes
equality: a circuit with exactly one gate per distinct non-input coordinate
has no auxiliary-only gate. LEMMA-237 applies it to the diagonal port vector,
whose exact cost is `m+1` from raw inputs and exactly `m` after the shared
signal `a=x AND y` is supplied.

Consequently, the LEMMA-233 exterior region is already a minimum joint
realization of its diagonal vector. Universal strict saving from functional
joint minimization is NG-173. The family is nonminimal and does not close or
falsify the endpoint-sensitive GATE-004DX. GATE-004DY isolates the remaining
zero-excess endpoint cases using the exact quantities `e=|U|-C_A(P)` and
`h=C_A(P)-q_A(P)`.

## Classification

- LEMMA-236: `PROVED`
- LEMMA-237: `PROVED`
- GATE-004DX-FUNCTIONAL-JOINT-SAVING-ONLY: `NO-GO`
- GATE-004DX: `EXPLORATORY`
- GATE-004DY: `EXPLORATORY`

`verification/diagonal_joint_port_cost_audit.py` checks the finite truth-table
premises through `m=8`. The general minimality claims use the direct structural
proofs. Fable was not invoked; independent certification, endpoint existence,
and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Constant-free multi-output AND/OR/NOT diagonal vector diagnostics and the refined endpoint cost decomposition |
| Uniform/non-uniform | Every finite diagonal instance; GATE-004DY ranges over every finite non-uniform residual endpoint |
| Circuit size | Exact diagnostic costs `m+1` raw and `m` supplied; endpoint quantities `|U|`, `C_A(P)`, `q_A(P)`, `e`, and `h` |
| Circuit depth | Unrestricted lower bounds and endpoint depth |
| Fan-in | AND/OR two; NOT one; fanout and multi-output sharing unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean vectors; endpoint potentials, contractions, and cycle spaces over `F_2` remain open |
| Asymptotic quantifiers | Every `m>=1`; GATE-004DY every residual endpoint and minimum joint realization |
| Regime | Exact vector-cost lemmas and scoped no-go; not endpoint proof, SAT lower bound, or terminal result |
