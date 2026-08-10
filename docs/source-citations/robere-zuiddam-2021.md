# RZ21 — amortized circuit complexity and formal measures

Robert Robere and Jeroen Zuiddam, “Amortized Circuit Complexity, Formal
Complexity Measures, and Catalytic Algorithms,” ECCC TR21-035, Revision 1,
2021.

- Primary report: https://eccc.weizmann.ac.il/report/2021/035/revision/1/download
- ECCC record: https://eccc.weizmann.ac.il/report/2021/035/
- Accessed: 2026-08-10
- Consumed claim: amortized complexity is the asymptotic cost per output of
  computing many copies of the same function on the same input; the paper
  characterizes it through formal complexity measures for finite-gate circuit
  models.
- General-circuit scope: with arbitrary fanout, one circuit for `f` can feed
  arbitrarily many identical output labels, so the general Boolean-circuit
  amortized cost per copy is `O(1)`. The paper explicitly notes that associated
  formal measures are therefore useless for standard general-circuit lower
  bounds.
- Scope control: GATE-004G asks for two *different* conditioned functions and a
  finite two-output quotient. RZ21 neither proves nor refutes its SAT-specific
  surplus. Its identical-copy duality cannot be promoted to that theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Circuit models over a finite gate set; general Boolean circuits are one instantiation |
| Uniform/non-uniform | Non-uniform circuit-size measure; mathematical duality theorem |
| Circuit size | Amortized limit of minimum size for `m` identical outputs divided by `m` |
| Circuit depth | Model-dependent; unrestricted for the general-circuit observation |
| Fan-in | Fixed finite gate set; arbitrary fanout is crucial for the general-circuit copying observation |
| Randomness | None in the circuit measure or duality statement |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Abstract circuit pre-order; no field in the consumed Boolean claim |
| Asymptotic quantifiers | Limit as number of identical copies `m` tends to infinity, for each fixed Boolean function |
| Regime | Exact same-input multi-output computation |
