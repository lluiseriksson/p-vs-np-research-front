# ILO20 — minimization of multi-output Boolean circuits

Rahul Ilango, Bruno Loff, and Igor Carboni Oliveira, “NP-Hardness of Circuit
Minimization for Multi-Output Functions,” ECCC TR20-021, 2020.

- Primary report: https://eccc.weizmann.ac.il/report/2020/021/download
- ECCC record: https://eccc.weizmann.ac.il/report/2020/021/
- Accessed: 2026-08-10
- Consumed claim: computing the minimum circuit size of a truth-table-given
  total multi-output Boolean function is NP-hard under many-one polynomial-time
  randomized reductions, for general unrestricted Boolean circuits.
- Scope control: this is hardness of the *minimization problem*. It supplies no
  size lower bound for the explicit pair `(CSAT_0,CSAT_1)`, no joint-quotient
  surplus, and no implication to P versus NP.

## Model card

| Field | Value |
|---|---|
| Computational model | General multi-output Boolean circuits over AND, OR, and NOT; function supplied by full truth table |
| Uniform/non-uniform | Uniform randomized reduction to a decision problem about non-uniform circuits |
| Circuit size | Gate count compared with an input threshold `s` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR/NOT basis as defined in the report; no fan-in-sensitive conclusion is consumed |
| Randomness | Polynomial-time randomized many-one reduction |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Worst-case family of truth-table instances over input/output arities and size threshold |
| Regime | Exact total multi-output functions; decision/minimization complexity, not an explicit-function lower bound |
