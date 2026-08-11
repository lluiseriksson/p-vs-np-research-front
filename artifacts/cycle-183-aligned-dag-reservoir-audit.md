# Cycle 183 — aligned-DAG reservoir audit

**Label: PROVED**

LEMMA-217 generalizes the private-reservoir exchange from formulas to shared
DAGs. A topological bijection maps every non-output certificate gate to a
closed noncarrier reservoir and maps the output to `b`; sharing is preserved,
size and earlier potentials do not increase, and `R_0` strictly descends.

The relevant residual is now `D_b^DAG`, the minimum aligned circuit deficit,
which is never larger than the former formula deficit. GATE-004DK asks for a
six-gate bound or distinct external resources on this tighter quantity.

## Classification

- LEMMA-217: `PROVED`
- GATE-004DK: `EXPLORATORY`

No formula-to-circuit equality, SAT lower bound, or terminal implication is
claimed. `verification/aligned_dag_reservoir_audit.py` checks a shared
four-gate certificate on all 16 assignments; the general rewrite is a human
proof. Fable was not invoked; independent certification is not performed.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined unrestricted AND/OR/NOT endpoint and one shared-DAG regression witness |
| Uniform/non-uniform | Every supplied finite aligned certificate; one finite four-input witness |
| Circuit size | `m` physical vertices repurposed; no increase; witness uses four shared DAG vertices |
| Circuit depth | Unrestricted theorem; constant witness depth |
| Fan-in | AND/OR two; NOT one; internal sharing and fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean DAG functions and physical rewiring |
| Asymptotic quantifiers | Every qualifying endpoint certificate; all 16 witness assignments |
| Regime | Exact sufficient exchange and tighter residual definition; not a SAT lower bound or terminal result |
